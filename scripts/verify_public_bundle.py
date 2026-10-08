"""Check only the public payload, links, numeric arrays and saved summaries."""
import os
os.environ["CUDA_VISIBLE_DEVICES"]=""
for _name in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS"):os.environ[_name]="2"
import argparse, csv, hashlib, json, re, sys
from pathlib import Path
import numpy as np
from reproduce_summaries import summarize, rows

PRIVATE_RULES = {
    "personal_home_locator": re.compile("/"+"home"+"/"+r"[A-Za-z0-9_.-]+"),
    "mounted_personal_locator": re.compile("/"+"mnt"+"/"+r"[a-z]/"),
    "private_drive_locator": re.compile("drive"+r"\.google"+r"\.com/(?:file|drive)"),
    "credential_value": re.compile(r"(?:ghp_|github_pat_|sk-proj-)[A-Za-z0-9_-]{16,}|Bearer\s+[A-Za-z0-9_.-]{16,}"),
    "private_network_locator": re.compile(r"(?:https?://|ssh\s+)\d{1,3}(?:\.\d{1,3}){3}"),
}
FORBIDDEN_BASENAMES={".env","INTERNAL_PROVENANCE.json","PUBLICATION_RECEIPT.json","PUBLICATION_REPORT_KO.md","DELIVERY_PROOF.json"}
FORBIDDEN_SUFFIXES={".safetensors",".pt",".pth",".ckpt",".otf",".ttf",".zip",".pkl",".pickle"}
def eligible(root):
    # Root Git metadata belongs to a clone/worktree, never to the public payload.
    # Nested .git directories remain visible and are rejected below.
    root = Path(root)
    found = []
    for directory, dirs, names in os.walk(root, followlinks=False):
        current = Path(directory)
        dirs[:] = [name for name in dirs if name != "__pycache__"
                   and not (current == root and name in {".git", "reproduced", "checks"})]
        for name in names:
            p = current / name
            if p.suffix == ".pyc" or (current == root and name == ".git"):
                continue
            if p.is_file():
                found.append(p)
    return sorted(found)
def verify(root,manifest_required=True):
    root=Path(root).resolve();files=eligible(root);issues=[];links=0
    for p in files:
        rel=str(p.relative_to(root))
        if p.is_symlink() or ".git" in p.relative_to(root).parts:issues.append({"file":rel,"reason":"symlink_or_git"})
        if p.name in FORBIDDEN_BASENAMES or p.suffix.lower() in FORBIDDEN_SUFFIXES:
            issues.append({"file":rel,"reason":"forbidden_file_class"})
        if p.stat().st_size>10*1024**2:issues.append({"file":rel,"reason":"single_file_size"})
        if p.suffix==".npz":
            with np.load(p,allow_pickle=False) as z:
                for key in z.files:
                    if z[key].dtype.hasobject or z[key].dtype.kind not in "biufc":
                        issues.append({"file":rel,"reason":"non_numeric_state_dtype","field":key})
                    if not np.all(np.isfinite(z[key])):issues.append({"file":rel,"reason":"nonfinite_array","field":key})
        if p.suffix in {".md",".tex",".json",".csv",".py",".txt",".sh"}:
            text=p.read_text(encoding="utf8")
            for label,pattern in PRIVATE_RULES.items():
                if pattern.search(text):issues.append({"file":rel,"reason":label})
            if p.suffix==".md":
                for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)",text):
                    dest=match.group(1).split("#",1)[0]
                    if not dest or re.match(r"^[a-z]+://",dest):continue
                    links+=1
                    if dest.startswith("/") or not (p.parent/dest).resolve().exists():
                        issues.append({"file":rel,"reason":"broken_or_absolute_link","target":dest})
            if p.suffix==".tex":
                if re.search(r"\\(?:write18|openout|immediate\s*\\write18)\b",text):
                    issues.append({"file":rel,"reason":"unsafe_tex_external_command"})
                for dest in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}",text):
                    links+=1
                    if not (p.parent/dest).is_file():issues.append({"file":rel,"reason":"missing_tex_figure","target":dest})
    total=sum(p.stat().st_size for p in files)
    if total>50*1024**2:issues.append({"reason":"payload_size"})
    manifest=root/"PUBLIC_MANIFEST.json"
    if manifest.exists():
        m=json.loads(manifest.read_text())
        listed={x["path"]:x for x in m["files"]}
        actual={str(p.relative_to(root)):p for p in files if p!=manifest}
        if set(actual)!=set(listed):issues.append({"reason":"manifest_membership"})
        for rel,p in actual.items():
            if rel in listed and hashlib.sha256(p.read_bytes()).hexdigest()!=listed[rel]["sha256"]:
                issues.append({"file":rel,"reason":"manifest_hash"})
    elif manifest_required:issues.append({"reason":"manifest_missing"})
    calculated,details,checks,grid=summarize(root/"results")
    recorded=rows(root/"results/summary.csv")
    rec={r["claim_id"]:r for r in recorded}
    if len(rec)!=len(recorded):issues.append({"reason":"duplicate_summary_claim"})
    for r in calculated:
        old=rec.get(r["claim_id"])
        if old is None or old["exact_fraction"]!=r["exact_fraction"] or abs(float(old["value"])-float(r["value"]))>1e-10*max(1,abs(float(r["value"]))):
            issues.append({"claim_id":r["claim_id"],"reason":"summary_arithmetic_mismatch"})
    return {"status":"PASS_PUBLIC_PAYLOAD_CHECKS" if not issues else "FAIL","issues":issues,"files":len(files),"bytes":total,"relative_links_checked":links,
      "saved_states_recalculated":len(grid),"model_or_solver_invoked":False,"PDF_status":"PDF_NOT_BUILT" if not (root/"manuscript/main.pdf").exists() else "PDF_PRESENT_REQUIRES_SEPARATE_RENDER_AUDIT"}
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--root",required=True,type=Path);ap.add_argument("--no-manifest",action="store_true",help="Before packaging only; final archive must include its manifest")
    a=ap.parse_args();r=verify(a.root,not a.no_manifest);print(json.dumps(r,indent=2));sys.exit(0 if not r["issues"] else 1)
if __name__=="__main__":main()
