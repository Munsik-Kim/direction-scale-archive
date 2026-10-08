from .common import *
X=np.array([[1.,.5],[0.,math.sqrt(3)/2]])
U=np.array([[math.cos(PHI0[0]),math.cos(PHI0[1])],[math.sin(PHI0[0]),math.sin(PHI0[1])]])
W0=U@np.linalg.inv(X);delta=-.8+math.asin(.1)
KEYS={"STRONG":np.array([[0.,0.],[1.,1.]]),"WEAK":np.column_stack([[0.,1.],[-math.sin(delta),math.cos(delta)]])}
MODELS=["H1_FIXED_VO","H1_TRAIN_VO","H3_TRAIN_VO"]
def heads(model):return 3 if model=="H3_TRAIN_VO" else 1
def kappas(model):return np.array([.25,1.,4.]) if heads(model)==3 else np.ones(1)
def initial(model):
 h=heads(model);v=np.full(h,2.);o=np.array([0.,.5,0.]) if h==3 else np.array([.5])
 return np.r_[W0.ravel(),1.,v,o]
def unpack(y,model):
 h=heads(model);return np.asarray(y[:4]).reshape(2,2),float(y[4]),np.asarray(y[5:5+h]),np.asarray(y[5+h:5+2*h])
def evaluate(y,data,model):
 W,beta,v,o=unpack(y,model);ks=KEYS[data];kappa=kappas(model)
 q=W@X;radii=np.linalg.norm(q,axis=0)
 if np.min(radii)<1e-10 or not np.all(np.isfinite(y)):raise FloatingPointError("DOMAIN_OR_NUMERICAL_UNRESOLVED")
 n=q/radii;d=2*np.sum(n*ks,axis=0);z=beta*d[:,None]*kappa
 A=np.exp(logsigmoid(z));Ac=np.exp(logsigmoid(-z));kernel=np.exp(logsigmoid(z)+logsigmoid(-z))
 c=v*o;S=float(c.sum());gamma=Ac@c;alpha=A@c
 # Stable alpha-1: use A+Ac=1 analytically; no 1-sigmoid subtraction.
 ep=(S-1.)-gamma;L=ep**2+gamma**2
 gc=2*(ep[:,None]*A+gamma[:,None]*Ac)
 gz=2*c[None,:]*(ep-gamma)[:,None]*kernel
 ld=(gz*kappa*beta).sum(axis=1);lb=(gz*kappa*d[:,None]).sum(axis=1)
 gd=2*(ks-n*np.sum(n*ks,axis=0))/radii
 gu=gd*ld[None,:];gW=np.array([np.outer(gu[:,i],X[:,i]) for i in range(2)])
 gv=gc*o;go=gc*v
 grad=np.column_stack([gW.reshape(2,4),lb,gv,go])
 return dict(W=W,beta=beta,v=v,o=o,c=c,S=S,q=q,n=n,radii=radii,d=d,z=z,A=A,Ac=Ac,alpha=alpha,gamma=gamma,ep=ep,L=L,J=float(P@L),gc=gc,gz=gz,ld=ld,lb=lb,gd=gd,gu=gu,gW=gW,gv=gv,go=go,grad=grad)
def field(y,data,model,scale,rho,boundary=False,unprojected=False):
 e=evaluate(y,data,model);g=P@e["grad"];vel=-g.copy()
 if model=="H1_FIXED_VO":vel[5:]=0
 vel[4]=(-g[4]/rho) if scale=="JOINT" else 0.
 if boundary:vel[4]=0.
 elif not unprojected and y[4]<=0:vel[4]=max(0.,vel[4])
 return vel
def rows(data):
 out=[]
 for i in range(2):
  for vp in [-1.,1.]:
   for vm in [-1.,1.]:
    for swap in [0,1]:
     keys=np.array([KEYS[data][:,i],-KEYS[data][:,i]]);values=np.array([vp,vm])
     if swap:keys=keys[::-1];values=values[::-1]
     out.append(dict(data=data,group=i+1,x=X[:,i].tolist(),keys=keys.tolist(),values=values.tolist(),target=vp,weight=float(P[i]/8),order=swap))
 return out
def raw_forward(y,model,x,keys,values,return_scores=False):
 # Target/group/order annotations are deliberately absent from this signature.
 W,beta,v,o=unpack(y,model);q=W@np.asarray(x);n=q/np.linalg.norm(q)
 scores=kappas(model)[:,None]*beta*(np.asarray(keys)@n)[None,:]
 a=np.exp(scores-scores.max(axis=1,keepdims=True));a/=a.sum(axis=1,keepdims=True)
 head_out=(a@(np.asarray(values))) * v
 pred=float(o@head_out)
 return (pred,scores,a,head_out) if return_scores else pred
def diagnostics(y,data,model,scale,rho):
 e=evaluate(y,data,model);g=P@e["grad"];vt=field(y,data,model,scale,rho)*rho
 Lparts=[float(e["grad"][1,:4]@vt[:4]),float(e["grad"][1,4]*vt[4]),
         float(e["grad"][1,5:5+heads(model)]@vt[5:5+heads(model)]),
         float(e["grad"][1,5+heads(model):]@vt[5+heads(model):])]
 gap=[float(-rho*P[j]*(e["gd"][:,1]@e["gu"][:,j])*(X[:,j]@X[:,1])) for j in range(2)]
 expected=-rho*np.dot(g[:4],g[:4])
 if scale=="JOINT" and (y[4]>0 or -g[4]>0):expected-=g[4]**2
 if model!="H1_FIXED_VO":expected-=rho*np.dot(g[5:],g[5:])
 c_velocity=vt[5:5+heads(model)]*e["o"]+e["v"]*vt[5+heads(model):]
 expected_c=-rho*(e["v"]**2+e["o"]**2)*(P@e["gc"]) if model!="H1_FIXED_VO" else np.zeros(heads(model))
 out=dict(L2_W_dt=Lparts[0],L2_beta_dt=Lparts[1],L2_V_dt=Lparts[2],L2_O_dt=Lparts[3],
  L2_total_chain_dt=sum(Lparts),gap2_from_group1_dt=gap[0],gap2_from_group2_dt=gap[1],
  energy_chain_dt=float(g@vt),energy_expected_dt=float(expected),energy_error=abs(float(g@vt)-expected),
  c_factorization_error=float(np.linalg.norm(c_velocity-expected_c)),
  conditional_gradients=e["grad"],weighted_gradients=P[:,None]*e["grad"],
  group_scale_forces=-P*e["lb"])
 for j in range(2):
  vj=-rho*P[j]*e["grad"][j].copy()
  vj[4]=(-P[j]*e["grad"][j,4]) if scale=="JOINT" and (y[4]>0 or -g[4]>0) else 0.
  if model=="H1_FIXED_VO":vj[5:]=0
  out[f"L2_W_from_group{j+1}_dt"]=float(e["grad"][1,:4]@vj[:4])
  out[f"L2_VO_from_group{j+1}_dt"]=float(e["grad"][1,5:]@vj[5:])
 return out
