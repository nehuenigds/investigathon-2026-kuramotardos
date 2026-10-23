"""Independent standard-library replay of the complete rational box tree.

Does not import the builder, its leaf predicates, NumPy or an eigensolver.
The strengthened projection is proved in cota_flujos_por_masa.md.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt,comb
import argparse,hashlib,json

ROOT=Path(__file__).resolve().parent


def replay(data):
    assert data['complete'] is True
    u=Q(data['target']);assert Q(2,3)<u<Q(3,4)
    lower=(2*u-1)/(2*(1-u));upper=1/lower
    region=[(lower,upper)]*3
    assert data['root']==[[str(a),str(b)] for a,b in region]
    denominator=int(data['sqrt_denominator']);assert denominator==10**8
    assert data['mass_constraint_variant']=='coupled_mass_flow_v1'
    counts={'boxes':0,'splits':0,'capacity':0,'mass_flow_upper':0,'mass_flow_sum':0,'whole_mass_projection':0,
            'aggregate_cut':0,'central_mass_projection':0,'variance_scale':0,'matrix':0,'bernstein_matrix':0}
    depth_max=0;margin=None
    def traverse(node,box,depth):
        nonlocal depth_max,margin
        counts['boxes']+=1;depth_max=max(depth_max,depth)
        assert depth<=120
        if 'dimension' in node:
            assert set(node)=={'dimension','left','right'}
            d=node['dimension'];assert type(d) is int and 0<=d<3
            lo,hi=box[d];mid=(lo+hi)/2
            lhs=list(box);rhs=list(box);lhs[d]=(lo,mid);rhs[d]=(mid,hi)
            counts['splits']+=1
            traverse(node['left'],lhs,depth+1);traverse(node['right'],rhs,depth+1)
            return
        a,A=box[0];b,B=box[1];c,C=box[2]
        reason=node['reason'];assert reason in counts and reason not in ('boxes','splits')
        if reason not in ('matrix','bernstein_matrix'):assert set(node)=={'reason'}
        if reason=='capacity':assert a*b>1 or b*c>1
        elif reason in ('mass_flow_upper','mass_flow_sum','whole_mass_projection','aggregate_cut','central_mass_projection','variance_scale'):
            ell=[u/(1+2*v) for v in (A,B,C)]
            baseA=max(ell[0],u-Q(1,2));baseC=max(ell[2],u-Q(1,2))
            lowB=max(ell[1],a*baseA,c*baseC)
            lowA=max(baseA,b*lowB);lowC=max(baseC,b*lowB)
            lowW=max(u-Q(1,2),a*lowA,c*lowC)
            minimum=[lowA,lowB,lowC,lowW]
            assert min(minimum)>0
            if reason=='mass_flow_upper':assert max(minimum)>1-u
            elif reason=='mass_flow_sum':assert sum(minimum)>1
            else:
                assert sum(minimum)<=1 and max(minimum)<=1-u<u/2
                D=max(t*(u-t) for t in minimum)
                s=1-sum(minimum[:3])
                # Complements of AB, BC, CW and WA, in that order.
                R=[1-minimum[2]-minimum[3],1-minimum[3]-minimum[0],
                   1-minimum[0]-minimum[1],1-minimum[1]-minimum[2]]
                assert min(R)>0
                if reason=='whole_mass_projection':assert max(a,c)*D>2*s*s
                elif reason=='aggregate_cut':assert min(R)**2<2*D
                elif reason=='central_mass_projection':assert 2*b*D>(1-minimum[1]-minimum[3])**2
                else:
                    upper=[min(1-u,1-sum(minimum)+minimum[i]) for i in range(3)]
                    assert any(hi*min(R)**2<(u-top)**2 for hi,top in zip((A,B,C),upper))
        elif reason=='matrix':
            assert set(node)=={'reason','alpha','weights'}
            alpha=Q(node['alpha']);assert 0<=alpha<=1
            v,w,z=map(Q,node['weights']);assert v>0 and w>0 and z>0
            def cap(x):
                r=Q(isqrt(x.numerator*denominator*denominator//x.denominator),denominator)
                assert r*r<=x<(r+Q(1,denominator))**2
                return min(Q(1,2),1-r)
            k,l=cap(a*b),cap(b*c);assert k>=0 and l>=0
            def minimum_quadratic(weight,linear,top):
                assert weight>0 and linear>=0
                return weight*top*top-linear*top if linear>=2*weight*top else -linear*linear/(4*weight)
            qa=2*(alpha*B+(1-alpha)*A)
            qc=2*(alpha*B+(1-alpha)*C)
            coupling=abs(2*alpha-1)
            r1=v*(4*(1-alpha)*a*a-1)+minimum_quadratic(v,qa*w+coupling*l*z,k)
            r2=w*(4*alpha*b*b-1)+minimum_quadratic(w,qa*v,k)+minimum_quadratic(w,qc*z,l)
            r3=z*(4*(1-alpha)*c*c-1)+minimum_quadratic(z,qc*w+coupling*k*v,l)
            assert min(r1,r2,r3)>0
            margin=min(r1,r2,r3) if margin is None else min(margin,r1,r2,r3)
        else:
            assert reason=='bernstein_matrix'
            assert set(node)=={'reason','alpha','subdivision_depth'}
            alpha=Q(node['alpha']);assert 0<=alpha<=1
            level=node['subdivision_depth'];assert type(level) is int and 0<=level<=3
            def interval_sum(*args):return sum(v[0] for v in args),sum(v[1] for v in args)
            def interval_times(v,w):
                r=[x*y for x in v for y in w];return min(r),max(r)
            def times(v,s):return interval_times(v,(s,s))
            IA=(4*(1-alpha)*a*a-1,4*(1-alpha)*A*A-1)
            IB=(4*alpha*b*b-1,4*alpha*B*B-1)
            IC=(4*(1-alpha)*c*c-1,4*(1-alpha)*C*C-1)
            assert IA[0]>0
            IP=(alpha*b+(1-alpha)*a,alpha*B+(1-alpha)*A)
            IQ=(alpha*b+(1-alpha)*c,alpha*B+(1-alpha)*C)
            IP4=times((IP[0]**2,IP[1]**2),Q(4));IQ4=times((IQ[0]**2,IQ[1]**2),Q(4))
            ABminus=interval_sum(IA,IB,times(IP4,Q(-1)))
            BCminus=interval_sum(IB,IC,times(IQ4,Q(-1)))
            r=2*alpha-1
            middle=interval_sum(IA,IB,IC,times(IP4,Q(-1)),times(IQ4,Q(-1)),
                                times(IB,-r*r),times(interval_times(IP,IQ),8*r))
            one=(Q(1),Q(1))
            P2={(0,0):interval_times(IA,IB),(1,0):ABminus,(0,1):IA,(2,0):one,(1,1):one}
            P3={(0,0):interval_times(interval_times(IA,IB),IC),(1,0):interval_times(IC,ABminus),
                (0,1):interval_times(IA,BCminus),(2,0):IC,(0,2):IA,(1,1):middle,
                (2,1):(1-r*r,1-r*r),(1,2):(1-r*r,1-r*r)}
            def upper_cap(v):
                root=Q(isqrt(v.numerator*denominator**2//v.denominator),denominator)
                assert root*root<=v<(root+Q(1,denominator))**2
                return min(Q(1,2),1-root)
            K,L=upper_cap(a*b),upper_cap(b*c);assert K>=0 and L>=0
            n=2**level
            for i in range(n):
                for j in range(n):
                    x0,x1=K*K*Q(i,n),K*K*Q(i+1,n)
                    y0,y1=L*L*Q(j,n),L*L*Q(j+1,n)
                    def beta(index,power,lo,hi):
                        return sum(Q(comb(power,t)*comb(index,t),comb(2,t))*lo**(power-t)*(hi-lo)**t
                                   for t in range(min(index,power)+1))
                    for polynomial in (P2,P3):
                        for p in range(3):
                            for q in range(3):
                                low=sum(value[0]*beta(p,ii,x0,x1)*beta(q,jj,y0,y1)
                                        for (ii,jj),value in polynomial.items())
                                assert low>0
        counts[reason]+=1
    traverse(data['tree'],region,0)
    assert counts==data['counts'] and depth_max==data['max_depth']
    assert margin==Q(data['minimum_row_margin'])
    assert counts['boxes']==2*counts['splits']+1
    return {'covered_root_exactly':True,'all_leaves_verified':True,'target':str(u),
            'counts':counts,'max_depth':depth_max,'minimum_row_margin':str(margin)}


def main():
    p=argparse.ArgumentParser();p.add_argument('--certificate',default='profile_upper_certificate_06934-v1.json')
    args=p.parse_args();path=ROOT/args.certificate
    data=json.loads(path.read_text(encoding='utf-8'));report=replay(data)
    report.update(certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  scope='Exact replay of covering and rational leaf inequalities. The written reduction is required; not an upper bound on all Kuramoto graphs or independent human review.')
    output=path.with_name(path.stem+'_verification.json')
    output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report))


if __name__=='__main__':main()
