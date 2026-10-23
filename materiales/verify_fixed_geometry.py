"""Standard-library-only exact primal/dual certificate for fixed geometry.

No optimizer, numerical eigenvalues, constructor coefficients or tolerance is
used. The upper bound is valid even for semidefinite cluster Hessians, hence
for every strict template in the precisely specified fixed-geometry class.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse
from verify_rational_template import check as check_lower

ROOT=Path(__file__).resolve().parent


def positive_definite(M):
    k=len(M);assert k>0 and all(len(a)==k for a in M),'dual dimensions'
    assert all(M[i][j]==M[j][i] for i in range(k) for j in range(k)),'dual symmetry'
    L=[[F(i==j) for j in range(k)] for i in range(k)];pivots=[]
    for i in range(k):
        d=M[i][i]-sum(L[i][j]**2*pivots[j] for j in range(i))
        assert d>0,'dual PSD: nonpositive pivot'
        pivots.append(d)
        for j in range(i+1,k):L[j][i]=(M[j][i]-sum(L[j][r]*L[i][r]*pivots[r] for r in range(i)))/d
    return pivots


def check(data):
    geom=data['geometry'];x=list(map(F,geom['x']));z=[list(map(F,a)) for a in geom['z']]
    sheets=geom['sheets'];h=F(geom['h']);m=len(x)
    model=geom.get('density_model','adjacent_only')
    assert model in ['adjacent_only','all_offdiagonal'],'density model'
    all_pairs=model=='all_offdiagonal'
    assert sum(x)==1 and all(v>0 for v in x),'masses'
    assert len(z)==m and all(len(a)==2 for a in z),'circle dimensions'
    assert all(c*c+s*s==1 for c,s in z),'circle'
    assert h>0 and len(sheets)==m and set(sheets)==set(range(4)),'four sheets'
    C=[[a[0]*b[0]+a[1]*b[1] for b in z] for a in z]
    S=[[a[1]*b[0]-a[0]*b[1] for b in z] for a in z]
    # Construct a lifting independently of the SDP's coefficient assembly.
    T=[[F(int(g==j))/h for j in range(3)] for g in sheets]
    for g in range(4):
        ids=[i for i,v in enumerate(sheets) if v==g]
        for i in ids[:-1]:
            for a in range(m):T[a].append(F(int(a==i)-int(a==ids[-1])))
    k=len(T[0]);dual=data['dual']
    Q=[list(map(F,a)) for a in dual['PSD_multiplier']]
    assert len(Q)==k,'dual dimensions'
    pivots=positive_definite(Q)
    lam=list(map(F,dual['degree_weights']));eta=list(map(F,dual['equilibrium_multipliers']))
    assert len(lam)==len(eta)==m and all(v>=0 for v in lam) and sum(lam)==1,'degree multipliers'
    W=[[sum(T[i][a]*Q[a][b]*T[j][b] for a in range(k) for b in range(k)) for j in range(m)] for i in range(m)]
    coeff=[];constant=F(0);edges=[]
    for i in range(m):constant+=lam[i]*(x[i] if all_pairs else sum(x[j] for j in range(m) if sheets[i]==sheets[j]))
    for i in range(m):
        for j in range(i+1,m):
            trace_piece=x[i]*x[j]*C[i][j]*(W[i][i]+W[j][j]-2*W[i][j])
            balance_piece=(eta[i]-eta[j])*x[i]*x[j]*S[i][j]
            if all_pairs:
                edges.append((i,j));coeff.append(lam[i]*x[j]+lam[j]*x[i]+trace_piece+balance_piece)
            elif sheets[i]==sheets[j]:constant+=trace_piece+balance_piece
            elif (sheets[i]-sheets[j])%4 in [1,3]:
                edges.append((i,j));coeff.append(lam[i]*x[j]+lam[j]*x[i]+trace_piece+balance_piece)
    upper=constant+sum(max(F(0),v) for v in coeff)
    assert upper==F(dual['upper']) and constant==F(dual['constant']),'upper bound replay'
    assert [str(v) for v in coeff]==dual['edge_coefficients'],'coefficient replay'
    witness=data['lower_witness'];lower=check_lower(witness)
    assert witness['x']==geom['x'] and witness['z']==geom['z'],'witness geometry'
    P=[list(map(F,a)) for a in witness['P']]
    for i in range(m):
        for j in range(m):
            if all_pairs:
                if i==j:assert P[i][j]==1,'diagonal pattern'
            elif sheets[i]==sheets[j]:assert P[i][j]==1,'same-sheet pattern'
            elif (sheets[i]-sheets[j])%4==2:assert P[i][j]==0,'opposite-sheet pattern'
    lo=F(lower['mu']);assert lo<=upper,'primal dual order'
    # The same lifted PSD multiplier W is valid for nearby geometries. With
    # coordinate errors eps_z and mass errors eps_x, |Delta C|,|Delta S|<=4eps_z
    # and |Delta(x_i*x_j)|<=2eps_x. max(0,a) is 1-Lipschitz.
    mass_L=F(1) if all_pairs else sum(lam[i]*sum(sheets[j]==sheets[i] for j in range(m)) for i in range(m))
    point_L=F(0)
    for i in range(m):
        for j in range(i+1,m):
            if not all_pairs and (sheets[i]-sheets[j])%4==2:continue
            size=abs(W[i][i]+W[j][j]-2*W[i][j])+abs(eta[i]-eta[j])
            mass_L+=2*size;point_L+=4*x[i]*x[j]*size
            if all_pairs or sheets[i]!=sheets[j]:mass_L+=lam[i]+lam[j]
    threshold=F(6929,10000)
    assert upper<threshold,'chosen demonstration threshold'
    exponent=0
    while upper+(mass_L+point_L)*F(1,10**exponent)>=threshold:exponent+=1
    radius=F(1,10**exponent);box_upper=upper+(mass_L+point_L)*radius
    # Every feasible p satisfies mu <= lambda*d + tr(Q T^T H T) + eta*b.
    # The added trace is >=0, balance is zero, and p in [0,1] gives the box bound.
    report={'exact_lower':str(lo),'exact_upper':str(upper),'exact_gap':str(upper-lo),
            'lower_approx':float(lo),'upper_approx':float(upper),'gap_approx':float(upper-lo),
            'dual_positive_definite':True,'dual_LDL_pivots':[str(v) for v in pivots],
            'lower_strict':True,'exact_lower_equilibrium':lower['exact_equilibrium'],
            'class':('Given masses and rational unit-circle points; every off-diagonal density free in [0,1], diagonal densities one.' if all_pairs else 'Given masses and rational unit-circle points; complete same-sheet densities, absent opposite-sheet densities, every adjacent density free in [0,1].'),
            'upper_valid_for':'All equilibria in this class with cluster Hessian positive semidefinite; no strictness or internal-stability assumption needed for the upper bound.',
            'no_claim':'No global upper bound over arbitrary geometries, other patterns, or all simple graphs.',
            'acceptance':'Fractions only; numerical SDP status and eigenvalues ignored.'}
    report.update(neighborhood={'mass_coordinate_radius':str(radius),
                'circle_coordinate_radius':str(radius),'mass_Lipschitz_bound':str(mass_L),
                'circle_Lipschitz_bound':str(point_L),'exact_upper':str(box_upper),
                'upper_approx':float(box_upper),'strictly_below':str(threshold),
                'conditions':'Same link pattern; new masses positive and summing to one; new points on the unit circle; entrywise mass and circle-coordinate errors bounded by the stated radii; equilibrium and PSD cluster Hessian.',
                'not_assumed':'Reflection, centered offsets, fixed q, fixed w, or leading-order constraints.'})
    return report


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--data',default='fixed_geometry_005_data.json')
    args=parser.parse_args();path=ROOT/args.data
    report=check(json.loads(path.read_text(encoding='utf-8')))
    report.update(data_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  lower_verifier_sha256=hashlib.sha256((ROOT/'verify_rational_template.py').read_bytes()).hexdigest())
    out=path.with_name(path.stem.removesuffix('_data')+'_certificate.json')
    out.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['lower_approx','upper_approx','gap_approx','dual_positive_definite','lower_strict','class','neighborhood']},indent=2))


if __name__=='__main__':main()
