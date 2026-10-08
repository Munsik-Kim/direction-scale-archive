"""Render six fixed topics from public saved records; no scientific run."""
import os
os.environ["CUDA_VISIBLE_DEVICES"]=""
for _name in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS"):os.environ[_name]="2"
import argparse, math, sys
from pathlib import Path
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", str(Path.cwd()/"reproduced"/".matplotlib-cache"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from reproduce_summaries import rows, summarize
COLORS={"FIXED":"#db7b24","JOINT_0.1":"#4481b1","JOINT_0.003":"#a54141"}
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"legend.frameon":False})
def save(fig,path):
    fig.savefig(path,dpi=165,bbox_inches="tight",metadata={"Software":"Direction-Scale saved-record reproduction"})
    plt.close(fig)
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument("--input",required=True,type=Path);ap.add_argument("--out",required=True,type=Path)
    a=ap.parse_args();s=a.input.resolve()/"selected";out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
    gf=rows(s/"restricted_uniform_gf.csv")
    fig,ax=plt.subplots(figsize=(7.4,3.5))
    for case in sorted({r["case_id"] for r in gf}):
        rr=sorted([r for r in gf if r["case_id"]==case],key=lambda r:float(r["rho"]))
        ax.plot([float(r["rho"]) for r in rr],[math.sqrt(float(r["rho"]))*float(r["log1p_T0"])/float(r["c_star"]) for r in rr],"o-",ms=4,label=case)
    ax.axhline(1,color="black",ls="--",lw=.8,label="Theorem's limiting ratio")
    ax.set_xscale("log");ax.set_xlabel("Direction/scale rate ratio rho");ax.set_ylabel("sqrt(rho) log(1+T0) / c(initialization)")
    ax.set_title("Nine initializations; stored direct-scale copy-MSE flow")
    ax.legend(ncol=3,fontsize=7);fig.tight_layout();save(fig,out/"01_restricted_delay.png")
    cells=rows(s/"controlled_loss_coordinate_cells.csv")
    fig,axes=plt.subplots(1,2,figsize=(9.5,3.6),sharey=True)
    for ax,coord in zip(axes,("DIRECT","LOG")):
        for loss,color in (("SQUARED_COPY","#a54141"),("LOGISTIC_VALUE","#4481b1"),("POINTER_CE","#388163")):
            rr=sorted([r for r in cells if r["coordinate"]==coord],key=lambda r:float(r["rho"]),reverse=True)
            rr=[r for r in rr if r["loss"]==loss]
            observed=[r for r in rr if r["status"]=="COMPLETE_EVENT"];censored=[r for r in rr if r["status"]!="COMPLETE_EVENT"]
            ax.plot([float(r["rho"]) for r in observed],[float(r["log1p_T0"]) for r in observed],"o-",color=color,ms=4,label=loss)
            if censored:
                ax.scatter([float(r["rho"]) for r in censored],[float(r["censor_q"]) for r in censored],marker="^",color=color)
        ax.set_xscale("log");ax.set_xlabel("rho");ax.set_title(coord+" scale coordinate");ax.grid(alpha=.15)
    axes[0].set_ylabel("Physical log(1+T0)")
    axes[1].legend(fontsize=7);fig.suptitle("Triangles: right-censored horizon, not correction events",fontsize=11);fig.tight_layout();save(fig,out/"02_loss_and_scale_coordinate.png")
    fig,axes=plt.subplots(1,2,figsize=(9.2,3.5),sharey=True)
    for ax,seed in zip(axes,(1103,1104)):
        rr=rows(s/f"swin_{seed}_train_hard_counts.csv")
        for arm,color in (("NATIVE_COMMON_CLIP","#4481b1"),("HOLD_COMMON_CLIP","#db7b24")):
            er=[]
            for k in range(0,1001,100):
                tt=[r for r in rr if r["arm"]==arm and int(r["step"])==k]
                er.append(sum((int(r["n"])-int(r["correct"]))/int(r["n"]) for r in tt)/2)
            ax.plot(range(0,1001,100),er,"o-",color=color,label="NCC" if arm.startswith("NATIVE") else "HCC",ms=4)
        ax.set_title(f"Training seed {seed}");ax.set_xlabel("Optimizer step");ax.grid(alpha=.15)
    axes[0].set_ylabel("Mean error of full Hard census (184 and 56)")
    axes[1].legend();fig.tight_layout();save(fig,out/"03_swin_seed_reversal.png")
    q14=rows(s/"qwen_layer0_counts.csv");fd=rows(s/"qwen_radial_finite_means.csv")
    fig,axes=plt.subplots(1,2,figsize=(9.5,3.5))
    for cond,color in (("N","#4481b1"),("C","#a54141")):
        vv=[next(r for r in q14 if r["split"]=="HELDOUT" and r["r_exact"]==rex and r["condition"]==cond) for rex in ("4/5","1","5/4")]
        axes[0].plot([.8,1,1.25],[int(r["negative_count"]) for r in vv],"o-",color=color,label=cond)
    axes[0].set_xlabel("Layer-0 score multiplier r (gain sqrt(r))");axes[0].set_ylabel("Strict decoy count / 128 reused questions");axes[0].set_title("P14 = -1/128; C decoys do not decrease");axes[0].legend()
    for cond,color in (("EO","#6b6f76"),("N","#4481b1"),("C","#a54141"),("CF","#388163")):
        rr=[r for r in fd if r["split"]=="HELDOUT" and r["condition"]==cond]
        pairs=[(0.,0.)]+[(float(r["epsilon"]),float(r["plus_actual_change"])) for r in rr]+[(-float(r["epsilon"]),float(r["minus_actual_change"])) for r in rr]
        pairs.sort();axes[1].plot([x for x,y in pairs],[y for x,y in pairs],"o-",color=color,label=cond,ms=4)
    axes[1].axhline(0,color="black",lw=.6);axes[1].set_xlabel("t: fixed DEV-N gain direction");axes[1].set_ylabel("Change in mean answer CE (nat/token)")
    axes[1].set_title("P15: N and C both decrease");axes[1].legend(ncol=2,fontsize=8);fig.tight_layout();save(fig,out/"04_qwen_opposed_and_joint_decrease.png")
    summary,details,checks,grid=summarize(a.input)
    fig,axes=plt.subplots(2,3,figsize=(10,5.2),sharex=True,sharey=True)
    for row,data in enumerate(("STRONG","WEAK")):
        for col,policy in enumerate(("FIXED_SLOW","JOINT_0.1","JOINT_0.003")):
            pid=f"{data}_H3_TRAIN_VO_{policy}";rr=[r for r in grid if r["path_id"]==pid];ax=axes[row,col]
            ax.plot([r["tau"] for r in rr],[r["L1"] for r in rr],label="Group 1",color="#4481b1")
            ax.plot([r["tau"] for r in rr],[r["L2"] for r in rr],label="Group 2",color="#a54141")
            ax.axhline(.1,color="black",ls="--",lw=.6);ax.set_yscale("symlog",linthresh=.001);ax.set_title(data+" / "+policy,fontsize=9);ax.grid(alpha=.15)
            if col==0:ax.set_ylabel("Actual population MSE")
            if row==1:ax.set_xlabel("Slow time tau")
    axes[0,0].legend(fontsize=8);fig.suptitle("Attention-only three-head V/O: all six unique paths",fontsize=12);fig.tight_layout();save(fig,out/"05_attention_vo_actual_losses.png")
    norms=rows(s/"readout_target_norm_records.csv")
    fig,axes=plt.subplots(1,2,figsize=(9.6,3.7))
    for policy,color in (("JOINT_0.003","#a54141"),("FIXED_SLOW","#db7b24")):
        pid="STRONG_H3_TRAIN_VO_"+policy
        nn=sorted([r for r in norms if r["path_id"]==pid],key=lambda r:float(r["tau"]))
        gg=[r for r in grid if r["path_id"]==pid]
        axes[0].plot([r["tau"] for r in gg],[r["actual_c_norm"] for r in gg],color=color,label=policy+" actual",lw=1.5)
        axes[0].plot([float(r["tau"]) for r in nn],[float(r["R_hi"]) for r in nn],"o--",color=color,label=policy+" target bound",ms=4)
        axes[0].fill_between([float(r["tau"]) for r in nn],[float(r["R_lo"]) for r in nn],[float(r["R_hi"]) for r in nn],color=color,alpha=.2)
    axes[0].set_yscale("log");axes[0].set_xlabel("Slow time tau; targets only at seven fixed nodes");axes[0].set_ylabel("L2 output coefficient norm");axes[0].legend(fontsize=7)
    end=rows(s/"readout_endpoints_reported.csv")
    for i,r in enumerate(end):
        ds=np.array(__import__("json").loads(r["D_singular_values"]));axes[1].plot([1,2,3],ds,"o-",ms=4,label=r["path_id"].replace("_H3_TRAIN_VO",""))
    axes[1].set_yscale("log");axes[1].set_xticks([1,2,3]);axes[1].set_xlabel("Singular value index of weighted D");axes[1].set_ylabel("Singular value at tau=40")
    axes[1].legend(fontsize=6);fig.tight_layout();save(fig,out/"06_readout_required_norm_and_spectrum.png")
    print("Rendered six saved-record figures.")
if __name__=="__main__":main()
