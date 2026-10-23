"""Numerical outer projection with coupled flow/mass inequalities.

Results are proposals, not equilibria or a rigorous upper bound.
"""
import bootstrap
from bootstrap import ROOT
from pathlib import Path
import argparse,hashlib,json
import numpy as np
from scipy.optimize import minimize


def constraints(x):
    a,b,c,k,l,w,z,u=x
    chi=np.array([a,b,c]);E=1+w*w+z*z
    v1=np.array([-k*w,2*b*w-k-l*z,-l*w])
    v2=np.array([-2*a+k*w,k-l*z,2*c*z-l*w])
    v3=np.array([-k*w,l*z-k,l*w])
    cross=np.sqrt([a*b,b*c]);floor=(2*u-1)/(2*(1-u))
    ell=u/(1+2*chi)
    A0=max(ell[0],u-.5); C0=max(ell[2],u-.5)
    LB=max(ell[1],a*A0,c*C0)
    LA=max(A0,b*LB); LC=max(C0,b*LB)
    LW=max(u-.5,a*LA,c*LC)
    low=np.array([LA,LB,LC,LW])
    D=max(low*(u-low));s=1-sum(low[:3])
    complements=[1-low[2]-low[3],1-low[3]-low[0],1-low[0]-low[1],1-low[1]-low[2]]
    R=min(complements)
    upper=np.array([min(1-u,1-sum(low)+low[i]) for i in range(3)])
    return np.r_[E-v1@v1,E-v2@v2,E-v3@v3,
                 1-cross-np.abs([k,l]),cross-np.abs([k,l]),chi-floor,
                 1-sum(low),1-u-low,2*s*s-max(a,c)*D,
                 np.array(complements)**2-2*D,
                 (1-low[1]-low[3])**2-2*b*D,
                 chi*R*R-(u-upper)**2]


def main():
    p=argparse.ArgumentParser();p.add_argument('--starts',type=int,default=24)
    p.add_argument('--id',default='20261020-flow-v1');p.add_argument('--seed',type=int,default=200071)
    args=p.parse_args();out=ROOT/f'mass_flow_projection_{args.id}.json';assert not out.exists()
    q=.6505691669447988;a=(1+q)/2
    base=np.array([a,a,a,1-a,1-a,1.3982781340204612,1.,.6929077063695864])
    rng=np.random.default_rng(args.seed);rows=[]
    bounds=[(.5,1.6)]*3+[(-.5,.5)]*2+[(.03,7.)]*2+[(.68,.74)]
    for k in range(args.starts):
        x=base.copy()
        if k:x[:7]*=np.exp(rng.normal(0,.25,7));x=np.clip(x,*np.array(bounds).T)
        result=minimize(lambda t:-t[-1],x,method='SLSQP',bounds=bounds,
                        constraints={'type':'ineq','fun':constraints},options={'ftol':2e-12,'maxiter':700})
        row={'start':k,'initial':x.tolist(),'parameters':result.x.tolist(),'mu':float(result.x[-1]),
             'minimum_constraint':float(min(constraints(result.x))),'success':bool(result.success),
             'message':str(result.message),'iterations':int(result.nit)}
        rows.append(row);print(json.dumps({n:row[n] for n in ['start','mu','minimum_constraint','success']}),flush=True)
    out.write_text(json.dumps({'seed':args.seed,'bounds':bounds,'results':rows,
                              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                              'scope':'Numerical necessary outer projection only. No finite-template certification or rigorous upper bound.'},indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':main()
