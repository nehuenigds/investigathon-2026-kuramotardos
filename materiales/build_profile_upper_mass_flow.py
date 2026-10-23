"""Build an exact covering certificate. Floats only propose alpha and weights."""
import bootstrap
from bootstrap import ROOT
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,time
import numpy as np
from scipy.optimize import minimize_scalar
from profile_upper_mass_flow_interval import covariance_caps,impossible,row_bounds,split,SQRT_DEN
from profile_matrix_bernstein import prove as bernstein_prove


def proposals(box):
    a,b,c=[float((v+w)/2) for v,w in box]
    # Boundary covariances guide the candidate vector; acceptance checks the
    # whole covariance interval, not just these values or the midpoint.
    k,l=[float(v) for v in covariance_caps(box)]
    candidates=[]
    for numerator in range(5,96,5):
        alpha=numerator/100
        M=np.array([[4*(1-alpha)*a*a+k*k-1,-2*k*(alpha*b+(1-alpha)*a),-abs(2*alpha-1)*k*l],
                    [-2*k*(alpha*b+(1-alpha)*a),4*alpha*b*b+k*k+l*l-1,-2*l*(alpha*b+(1-alpha)*c)],
                    [-abs(2*alpha-1)*k*l,-2*l*(alpha*b+(1-alpha)*c),4*(1-alpha)*c*c+l*l-1]])
        values,vectors=np.linalg.eigh(M)
        v=np.abs(vectors[:,0]);v/=max(v)
        weights=[F(str(max(.001,round(float(t),6)))) for t in v]
        candidates.append((float(values[0]),F(numerator,100),weights))
    return sorted(candidates,reverse=True,key=lambda t:t[0])[:5]


def main():
    p=argparse.ArgumentParser();p.add_argument('--target',default='69291/100000')
    p.add_argument('--id',default='069291-v1');p.add_argument('--max-boxes',type=int,default=500000)
    p.add_argument('--max-depth',type=int,default=80);args=p.parse_args()
    out=ROOT/f'profile_upper_certificate_{args.id}.json';assert not out.exists()
    u=F(args.target);floor=(2*u-1)/(2*(1-u));root=[(floor,1/floor)]*3
    counters={'boxes':0,'splits':0,'capacity':0,'mass_flow_upper':0,'mass_flow_sum':0,'whole_mass_projection':0,
              'aggregate_cut':0,'central_mass_projection':0,'variance_scale':0,'matrix':0,'bernstein_matrix':0}
    started=time.monotonic();max_depth=0;minimum=None
    def visit(box,depth=0):
        nonlocal max_depth,minimum
        counters['boxes']+=1;max_depth=max(max_depth,depth)
        if counters['boxes']%5000==0:
            print(json.dumps({**counters,'depth':max_depth,'elapsed':round(time.monotonic()-started,2)}),flush=True)
        assert counters['boxes']<=args.max_boxes and depth<=args.max_depth,('budget',counters,depth,box)
        reason=impossible(box,u)
        if reason:counters[reason]+=1;return {'reason':reason}
        for _,alpha,weights in proposals(box):
            bounds=row_bounds(box,alpha,weights)
            if min(bounds)>0:
                counters['matrix']+=1;minimum=min(bounds) if minimum is None else min(minimum,*bounds)
                return {'reason':'matrix','alpha':str(alpha),'weights':list(map(str,weights))}
        if depth>=6:
            a,b,c=[float((v+w)/2) for v,w in box]
            k,l=[float(v) for v in covariance_caps(box)]
            def spectral(t):
                M=np.array([[4*(1-t)*a*a+k*k-1,-2*k*(t*b+(1-t)*a),(2*t-1)*k*l],
                            [-2*k*(t*b+(1-t)*a),4*t*b*b+k*k+l*l-1,-2*l*(t*b+(1-t)*c)],
                            [(2*t-1)*k*l,-2*l*(t*b+(1-t)*c),4*(1-t)*c*c+l*l-1]])
                return -np.linalg.eigvalsh(M)[0]
            optimum=minimize_scalar(spectral,bounds=(.02,.98),method='bounded',options={'xatol':1e-10})
            alpha=F(str(round(float(optimum.x),8)))
            for level in ([1,2,3] if depth>=24 else [1]):
                if bernstein_prove(box,alpha,depth=level) is not None:
                    counters['bernstein_matrix']+=1
                    return {'reason':'bernstein_matrix','alpha':str(alpha),'subdivision_depth':level}
        # A/C symmetry is not assumed. Split every uncertain interval in full.
        dimension=max(range(3),key=lambda d:box[d][1]-box[d][0])
        left,right=split(box,dimension);counters['splits']+=1
        return {'dimension':dimension,'left':visit(left,depth+1),'right':visit(right,depth+1)}
    try:tree=visit(root)
    except AssertionError as error:
        (ROOT/f'profile_upper_attempt_{args.id}.json').write_text(json.dumps({'complete':False,'counts':counters,
           'elapsed':time.monotonic()-started,'error':str(error),'target':str(u)},indent=2)+'\n',encoding='utf-8')
        raise
    data={'complete':True,'target':str(u),'root':[[str(a),str(b)] for a,b in root],
          'sqrt_denominator':SQRT_DEN,'mass_constraint_variant':'coupled_mass_flow_v1','tree':tree,'counts':counters,'max_depth':max_depth,
          'minimum_row_margin':str(minimum),'elapsed_seconds':time.monotonic()-started,
          'builder_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'predicate_sha256':hashlib.sha256((ROOT/'profile_upper_mass_flow_interval.py').read_bytes()).hexdigest(),
          'scope':'Covariance relaxation domain covered exactly; the written reduction and independent replay are required for a leading-profile upper bound. No universal Kuramoto upper bound.'}
    out.write_text(json.dumps(data,separators=(',',':'))+'\n',encoding='utf-8')
    print(json.dumps({'complete':True,'target':str(u),'counts':counters,'max_depth':max_depth,'elapsed':data['elapsed_seconds']}),flush=True)


if __name__=='__main__':main()
