"""An exact feasible point of the outer relaxation, not a Kuramoto template.

This guards against interpreting a failed covering as an improved upper bound.
Uses only the standard library and does not import the search or predicates.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent


def verify():
    a=c=F(8427,10000);b=F(101,125)
    k=l=F(8739,50000);w=F(28993,20000);z=F(1)
    energy=1+w*w+z*z
    forms=[[-k*w,2*b*w-k-l*z,-l*w],[-2*a+k*w,k-l*z,2*c*z-l*w]]
    stability=[energy-sum(t*t for t in v) for v in forms]
    capacities=[(1-k)**2-a*b,(1-l)**2-b*c,a*b-k*k,b*c-l*l]
    assert 0<k<1 and 0<l<1 and min(stability+capacities)>0
    rows=[]
    for u in [F(1733,2500),F(69291,100000)]:
        floor=(2*u-1)/(2*(1-u))
        assert all(floor<v<1/floor for v in (a,b,c))
        ell=[u/(1+2*t) for t in (a,b,c)]
        initialA=max(ell[0],u-F(1,2));initialC=max(ell[2],u-F(1,2))
        B=max(ell[1],a*initialA,c*initialC)
        A=max(initialA,b*B);C=max(initialC,b*B)
        W=max(u-F(1,2),a*A,c*C)
        low=[A,B,C,W]
        assert 0<min(low)<=max(low)<1-u<u/2
        D=max(t*(u-t) for t in low)
        s=1-A-B-C
        R=[1-C-W,1-W-A,1-A-B,1-B-C]
        upper=[min(1-u,1-sum(low)+low[i]) for i in range(3)]
        margins={'mass_sum':1-sum(low),'whole_mass_projection':2*s*s-max(a,c)*D,
                 'aggregate_cut':min(R)**2-2*D,
                 'central_mass_projection':(1-B-W)**2-2*b*D,
                 'variance_scale':min(t*min(R)**2-(u-top)**2 for t,top in zip((a,b,c),upper))}
        assert min(margins.values())>0
        rows.append({'target':str(u),'lower_masses':list(map(str,low)),
                     'strict_margins':{key:str(value) for key,value in margins.items()}})
    return {'verified':True,'parameters':dict(zip(('a','b','c','k','l','w','z'),map(str,(a,b,c,k,l,w,z)))),
            'stability_margins':list(map(str,stability)),
            'covariance_capacity_margins':list(map(str,capacities)),
            'mass_projection':rows,
            'scope':'Strict rational feasible point of the projected necessary inequalities only. No masses, flow matrices, phases, equilibrium, or Hessian witness is supplied. Not a Kuramoto counterexample or a new lower bound.'}


if __name__=='__main__':
    report=verify()
    report['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'mass_flow_relaxation_witness.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verified':True,'outer_relaxation_targets':[v['target'] for v in report['mass_projection']],
                      'is_kuramoto_template':False}))
