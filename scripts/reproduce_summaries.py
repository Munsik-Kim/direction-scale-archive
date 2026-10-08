"""Reaggregate selected saved records only. No model, optimizer, ODE or optimization."""
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "2"
import argparse, csv, json, math, sys
from pathlib import Path
from fractions import Fraction
from collections import defaultdict, Counter
import numpy as np

def rows(path):
    with Path(path).open(newline="", encoding="utf8") as f:
        return list(csv.DictReader(f))

def exact_area(values):
    """Registered 11-node step grid: endpoint 1/20; interior 1/10."""
    if len(values) != 11:
        raise ValueError("INCOMPLETE_REGISTERED_GRID")
    return sum((Fraction(1,20) if j in (0,10) else Fraction(1,10))*x for j,x in enumerate(values))

def validate_counts(records, groups):
    indexed = {}
    for r in records:
        key=(r["arm"], int(r["step"]), r["group"])
        if key in indexed:
            raise ValueError("DUPLICATE_EVALUATION_KEY")
        if r["group"] not in groups or int(r["n"])!=groups[r["group"]]:
            raise ValueError("GROUP_DENOMINATOR_MISMATCH")
        n=int(r["n"]);correct=int(r["correct"])
        if not 0<=correct<=n:
            raise ValueError("INVALID_CORRECT_COUNT")
        indexed[key]=r
    arms=sorted({r["arm"] for r in records})
    expected={(a,k,g) for a in arms for k in range(0,1001,100) for g in groups}
    if set(indexed)!=expected:
        raise ValueError("INCOMPLETE_REGISTERED_GRID")
    return indexed,arms

def h3_state(state, data):
    W=state[:4].reshape(2,2);beta=float(state[4]);v=state[5:8];o=state[8:11];c=v*o
    X=np.array([[1.,.5],[0.,math.sqrt(3)/2]])
    delta=-.8+math.asin(.1)
    keys=np.array([[0.,0.],[1.,1.]]) if data=="STRONG" else np.array([[0.,-math.sin(delta)],[1.,math.cos(delta)]])
    q=W@X;n=q/np.linalg.norm(q,axis=0);d=2*np.sum(n*keys,axis=0)
    kappa=np.array([.25,1.,4.]);z=beta*d[:,None]*kappa
    a=np.exp(-np.logaddexp(0.,-z));b=np.exp(-np.logaddexp(0.,z))
    M=np.stack([a,b],axis=1);res=np.einsum("ijk,k->ij",M,c)-np.array([1.,0.])
    L=np.sum(res**2,axis=1);D=np.vstack([math.sqrt(.95)*M[0],math.sqrt(.05)*M[1]])
    target=np.array([math.sqrt(.95),0.,math.sqrt(.05),0.]);r=D@c-target
    return {"d":d,"z":z,"L":L,"J":float(.95*L[0]+.05*L[1]),"beta":beta,"c":c,"M":M,"D":D,"r":r,"target":target,"G":v*v+o*o}

def raw_population_loss(state,data):
    """Independent raw 16-row mathematical formula; not a neural Forward."""
    X=np.array([[1.,.5],[0.,math.sqrt(3)/2]])
    delta=-.8+math.asin(.1)
    keys=np.array([[0.,0.],[1.,1.]]) if data=="STRONG" else np.array([[0.,-math.sin(delta)],[1.,math.cos(delta)]])
    W=state[:4].reshape(2,2);v=state[5:8];o=state[8:11];beta=state[4]
    answer=[]
    for i in range(2):
        q=W@X[:,i];q=q/np.linalg.norm(q);losses=[]
        for vp in (-1.,1.):
            for vm in (-1.,1.):
                for swap in (False,True):
                    kk=np.array([keys[:,i],-keys[:,i]]);vv=np.array([vp,vm])
                    if swap:kk=kk[::-1];vv=vv[::-1]
                    scores=np.array([.25,1.,4.])[:,None]*beta*(kk@q)[None,:]
                    weights=np.exp(scores-scores.max(axis=1,keepdims=True));weights/=weights.sum(axis=1,keepdims=True)
                    pred=float(o@(v*(weights@vv)))
                    losses.append((pred-vp)**2)
        answer.append(float(np.mean(losses)))
    return np.array(answer)

def summarize(input_root):
    base=Path(input_root).resolve()/"selected"; summary=[];details={};checks={}
    def add(cid,family,metric,value,unit,scope,source,level="stored_aggregate",fraction=""):
        summary.append(dict(claim_id=cid,experiment_family=family,metric=metric,value=format(float(value),".17g"),
          exact_fraction=fraction,unit=unit,scope=scope,source_level=level,source_file="selected/"+source))
    for seed in (1103,1104):
        filename=f"swin_{seed}_train_hard_counts.csv";rec=rows(base/filename)
        index,arms=validate_counts(rec,{"01":184,"10":56});u={}
        for arm in arms:
            err=[sum(Fraction(int(index[arm,k,g]["n"])-int(index[arm,k,g]["correct"]),int(index[arm,k,g]["n"])) for g in ("01","10"))/2 for k in range(0,1001,100)]
            u[arm]=exact_area(err)
            add(f"swin{seed}_{arm}_U","swin_common_clipping","U_train_H_error",u[arm],"mean error rate over steps","240-image census; groups equally weighted; C=1000",filename,"recorded_group_counts",str(u[arm]))
        ncc=u["NATIVE_COMMON_CLIP"];hcc=u["HOLD_COMMON_CLIP"];delta=ncc-hcc
        add(f"swin{seed}_delta","swin_common_clipping","NCC_minus_HCC_error_AUC",delta,"error-rate area","same dataset; one paired training seed",filename,"recorded_group_counts",str(delta))
        rec=rows(base/f"swin_{seed}_validation_counts.csv");ix,arms=validate_counts(rec,{"00":467,"01":466,"10":133,"11":133})
        for arm in arms:
            end=[ix[arm,1000,g] for g in ("00","01","10","11")]
            rates=[Fraction(int(t["correct"]),int(t["n"])) for t in end]
            wga=min(rates);freq=Fraction(sum(int(t["correct"]) for t in end),1199)
            add(f"swin{seed}_{arm}_wga","swin_common_clipping","final_validation_WGA",wga,"accuracy","k=1000; min over four groups",f"swin_{seed}_validation_counts.csv","recorded_group_counts",str(wga))
            add(f"swin{seed}_{arm}_frequency","swin_common_clipping","final_validation_frequency_accuracy",freq,"accuracy","observed validation group frequencies",f"swin_{seed}_validation_counts.csv","recorded_group_counts",str(freq))
        checks[f"swin{seed}_primary_matches_saved"]=str(delta)=={1103:"37/25760",1104:"-99/51520"}[seed]
    pilot=rows(base/"swin_pilot_validation_groups.csv")
    for seed in (1101,1102):
        rec=[r for r in pilot if int(r["seed"])==seed];ix,arms=validate_counts(rec,{"00":467,"01":466,"10":133,"11":133})
        areas={}
        for arm in arms:
            ce=[sum(float(ix[arm,k,g]["CE"]) for g in ("01","10"))/2 for k in range(0,1001,100)]
            areas[arm]=float(exact_area([Fraction.from_float(x) for x in ce]))
            endpoint=min(Fraction(int(ix[arm,1000,g]["correct"]),int(ix[arm,1000,g]["n"])) for g in ("00","01","10","11"))
            add(f"pilot{seed}_{arm}_wga","swin_pilot","final_validation_WGA",endpoint,"accuracy","k=1000; original clipping policies", "swin_pilot_validation_groups.csv","recorded_group_counts",str(endpoint))
        delta=areas["NATIVE"]-areas["HOLD"]
        add(f"pilot{seed}_delta","swin_pilot","Delta_H_validation_CE",delta,"nat","full-horizon trapezoid; two hard groups equally weighted", "swin_pilot_validation_groups.csv","recorded_group_CE")
        saved=next(r for r in rows(base/"swin_pilot_primary.csv") if int(r["seed"])==seed and r["split"]=="validation")
        checks[f"pilot{seed}_CE_match"]=abs(delta-float(saved["Delta_H"]))<1e-12
    q13=rows(base/"qwen_evidence_counts.csv")
    for split in ("DEV","HELDOUT"):
        rr={t["condition"]:t for t in q13 if t["split"]==split}
        if set(rr)!={"EO","N","C","QO","CF"}:raise ValueError("INCOMPLETE_CONDITION_SET")
        for cond,t in rr.items():
            if int(t["registered_n"])!=128 or int(t["observed_n"])!=128:raise ValueError("INCOMPLETE_QWEN_DENOMINATOR")
            for metric,key in (("EM","EM_count_observed"),("decoy","decoy_count_observed")):
                add(f"qwen13_{split}_{cond}_{metric}","qwen_evidence",metric+"_count",int(t[key]),"count out of 128","historical split; aggregate-only", "qwen_evidence_counts.csv")
        d=Fraction(int(rr["C"]["decoy_count_observed"])-int(rr["N"]["decoy_count_observed"]),128)
        add(f"qwen13_{split}_delta","qwen_evidence","C_minus_N_decoy_rate",d,"rate","128 unique questions; five paired variants", "qwen_evidence_counts.csv",fraction=str(d))
    q14=rows(base/"qwen_layer0_counts.csv")
    for split in ("DEV","HELDOUT"):
        vals={}
        for rex in ("1","4/5","5/4"):
            sub={t["condition"]:t for t in q14 if t["split"]==split and t["r_exact"]==rex}
            if set(sub)!={"EO","N","C","QO","CF"}:raise ValueError("INCOMPLETE_SCALE_GRID")
            for t in sub.values():
                if int(t["expected_n"])!=128 or int(t["completed_n"])!=128:raise ValueError("INCOMPLETE_SCALE_DENOMINATOR")
            vals[rex]=Fraction(int(sub["C"]["negative_count"])-int(sub["N"]["negative_count"]),128)
            add(f"qwen14_{split}_{rex}_D","qwen_layer0","C_minus_N_decoy_rate",vals[rex],"rate","r multiplies scores; gains multiply by sqrt(r); reused split", "qwen_layer0_counts.csv",fraction=str(vals[rex]))
        p14=vals["1"]-vals["4/5"]
        add(f"qwen14_{split}_P14","qwen_layer0","P14_BASE_minus_LOW_contrast",p14,"rate","reused HELDOUT is primary; DEV auxiliary", "qwen_layer0_counts.csv",fraction=str(p14))
    layers=rows(base/"qwen_radial_layer_contributions.csv")
    for split in ("DEV","HELDOUT"):
        for cond in ("EO","N","C","CF"):
            group=[t for t in layers if t["split"]==split and t["condition"]==cond]
            if sorted(int(t["layer"]) for t in group)!=list(range(28)):raise ValueError("INCOMPLETE_LAYER_CENSUS")
            slope=math.fsum(float(t["answer_directional_contribution"]) for t in group)
            add(f"qwen15_{split}_{cond}_slope","qwen_radial","answer_loss_directional_derivative",slope,"nat/answer-token per unit t","one DEV-N-selected direction; no training trajectory", "qwen_radial_layer_contributions.csv","stored_layer_contributions")
    cells=rows(base/"controlled_loss_coordinate_cells.csv");statuses=Counter(t["status"] for t in cells)
    details["controlled_loss_coordinate_status_counts"]=dict(statuses)
    for status,count in statuses.items():
        add("controlled_"+status,"controlled_loss_coordinate",status,count,"cells out of 54","three losses x two coordinates x nine rates", "controlled_loss_coordinate_cells.csv")
    paths=rows(base/"attention_vo_all_path_summaries.csv")
    details["attention_vo_24_logical_paths"]={r["logical_path"]:r["wrong_rank_low_both_fraction"] for r in paths}
    add("P17","attention_vo","P17_wrong_rank_low_both_occupation",0,"fraction of registered slow-time horizon",
        "STRONG/H3/JOINT/rho=.003; raw grid recomputation below", "states/STRONG_H3_TRAIN_VO_JOINT_0.003_grid.npz","saved_synthetic_state","0")
    endpoint_reports={r["path_id"]:r for r in rows(base/"readout_endpoints_reported.csv")}
    state_map={};grid_out=[];maxloss=0.;invariant=0.;p17=None
    for f in sorted((base/"states").glob("*_grid.npz")):
        pid=f.name[:-len("_grid.npz")];data=pid.split("_")[0]
        with np.load(f,allow_pickle=False) as z:tau=z["tau_grid"].copy();states=z["state_grid"].copy()
        if states.shape!=(401,11) or not np.allclose(tau,np.arange(401)/10,atol=1e-13,rtol=0):raise ValueError("INVALID_STATE_GRID")
        state_map[pid]=states
        es=[]
        for j,state in enumerate(states):
            e=h3_state(state,data);es.append(e)
            inv=state[5:8]**2-state[8:11]**2
            invariant=max(invariant,float(np.max(np.abs(inv-np.array([4.,3.75,4.]))/(1+np.array([4.,3.75,4.])))))
            grid_out.append(dict(path_id=pid,data=data,tau=float(tau[j]),d1=e["d"][0],d2=e["d"][1],beta=e["beta"],L1=e["L"][0],L2=e["L"][1],J=e["J"],actual_c_norm=float(np.linalg.norm(e["c"]))))
        for j in (0,400):
            maxloss=max(maxloss,float(np.max(np.abs(raw_population_loss(states[j],data)-es[j]["L"]))))
        end=es[-1];reported=endpoint_reports[pid]
        for k in ("L1","L2","J","R_actual"):
            val=end["L"][0] if k=="L1" else end["L"][1] if k=="L2" else end["J"] if k=="J" else np.linalg.norm(end["c"])
            if abs(val-float(reported[k]))>1e-10:raise ValueError("SAVED_ENDPOINT_MISMATCH")
        for g in (0,1):
            add(f"{pid}_L{g+1}","attention_vo","final_group_MSE",end["L"][g],"MSE","tau=40; fixed paths reused across two rho labels", "states/"+f.name,"saved_synthetic_state")
        wrong=[int(e["beta"]>0 and e["d"][1]<0 and np.all(e["z"][1]<0) and np.all(e["L"]<=.1)) for e in es]
        occ=sum((Fraction(1,800) if j in (0,400) else Fraction(1,400))*b for j,b in enumerate(wrong))
        if pid=="STRONG_H3_TRAIN_VO_JOINT_0.003":p17=occ
    if p17 is None:raise ValueError("PRIMARY_STATE_MISSING")
    summary=[r for r in summary if r["claim_id"]!="P17"]
    add("P17","attention_vo","P17_wrong_rank_low_both_occupation",p17,"fraction of slow-time horizon","401 nodes; continuous absence not certified",
      "states/STRONG_H3_TRAIN_VO_JOINT_0.003_grid.npz","saved_synthetic_state",str(p17))
    checks["raw_population_vs_closed_risk_max_abs"]=maxloss;checks["VO_invariant_max_scaled_drift"]=invariant
    anchor="STRONG_H3_TRAIN_VO_JOINT_0.003";e=h3_state(state_map[anchor][-1],"STRONG")
    records=rows(base/"readout_target_norm_records.csv")
    rec=next(t for t in records if t["path_id"]==anchor and int(t["index"])==400)
    coeff=np.array(json.loads(rec["feasible_coeff"]));loss=np.sum((np.einsum("ijk,k->ij",e["M"],coeff)-[1.,0.])**2,axis=1)
    if np.any(loss>.1):raise ValueError("PUBLIC_ANCHOR_WITNESS_NOT_FEASIBLE")
    lo=float(rec["R_lo"]);hi=float(rec["R_hi"]);actual=float(np.linalg.norm(e["c"]));witness_norm=float(np.linalg.norm(coeff))
    add("readout_norm_lower","readout_posthoc","target_norm_lower_recorded",lo,"L2 coefficient norm","fixed attention; both group MSE<=.1; old solver not rerun", "readout_target_norm_records.csv","recorded_static_bracket")
    add("readout_norm_upper","readout_posthoc","target_norm_upper_witness",witness_norm,"L2 coefficient norm","original feasible coefficient evaluated only, not fitted", "readout_target_norm_records.csv","saved_static_witness")
    add("readout_norm_actual","readout_posthoc","actual_coefficient_norm",actual,"L2 coefficient norm","tau=40; factorized V/O", "states/"+anchor+"_grid.npz","saved_synthetic_state")
    u,s,vt=np.linalg.svd(e["D"],full_matrices=True);cls=vt.T@((u[:,:3].T@e["target"])/s)
    add("readout_LS_norm","readout_posthoc","weighted_LS_coefficient_norm",np.linalg.norm(cls),"L2 coefficient norm","unconstrained weighted LS; different from .1-per-group target", "states/"+anchor+"_grid.npz","saved_synthetic_state")
    beff=e["D"]*np.sqrt(e["G"])[None,:];ub,sb,vb=np.linalg.svd(beff,full_matrices=True)
    energy=float((ub[:,2]@e["r"])**2);share=energy/e["J"]
    add("small_singular_energy_share","readout_posthoc","instantaneous_residual_small_resolved_subspace_fraction",share,"fraction","instantaneous residual share; not causal failure attribution", "states/"+anchor+"_grid.npz","saved_synthetic_state")
    gc=2*e["D"].T@e["r"];jvo=-float(np.dot(gc*e["G"],gc))
    add("readout_Jdot_VO","readout_posthoc","weighted_Jdot_VO",jvo,"MSE per unit slow tau","instantaneous formula; no numerical integration", "states/"+anchor+"_grid.npz","saved_synthetic_state")
    details["anchor_witness_losses"]=loss.tolist();details["anchor_witness_norm"]=witness_norm
    details["bracket_lower_is_historical_record"]="No new minimization, high-precision dual optimization, or certificate was run."
    quadr=rows(base/"readout_quadrature_unresolved.csv")
    add("unresolved_quadratures","readout_posthoc","INTEGRAL_UNRESOLVED",sum(r["status"]=="INTEGRAL_UNRESOLVED" for r in quadr),"records out of 18",
        "historical .1/.2-grid checks; no attempt to resolve", "readout_quadrature_unresolved.csv")
    checks["no_new_model_solver_or_learning"]=True
    if not all(v for k,v in checks.items() if k.endswith("_match") or k.endswith("_saved")):raise ValueError("SOURCE_SUMMARY_DISCREPANCY")
    return summary,details,checks,grid_out

def write_csv(path, records):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",newline="",encoding="utf8") as f:
        w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input",required=True,type=Path);ap.add_argument("--out",required=True,type=Path)
    args=ap.parse_args();out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
    result,details,checks,grid=summarize(args.input)
    write_csv(out/"summary.csv",result);write_csv(out/"h3_reconstructed_grid.csv",grid)
    (out/"reaggregation.json").write_text(json.dumps({"status":"SAVED_RECORDS_REAGGREGATED","details":details,"checks":checks,"scope":"No historical training/inference/integration rerun."},indent=2)+"\n")
    print(json.dumps({"rows":len(result),"saved_states":len(grid),"P17":next(r["exact_fraction"] for r in result if r["claim_id"]=="P17"),"checks":checks}))
if __name__=="__main__":
    main()
