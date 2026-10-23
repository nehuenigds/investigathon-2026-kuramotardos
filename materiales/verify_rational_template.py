"""Standard-library-only exact verifier for rational-coordinate templates.

No tolerance, transcendental evaluation, numerical eigensolver or constructor
is used for acceptance. Strict LDL is on a rotation gauge, equivalent to strict
positivity on the rotation complement because the full Hessian kills 1.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
import argparse

ROOT = Path(__file__).resolve().parent


def check(row):
    x = [F(v) for v in row['x']]
    z = [[F(v) for v in rr] for rr in row['z']]
    P = [[F(v) for v in rr] for rr in row['P']]
    m = len(x)
    assert m>=2 and len(z)==m and len(P)==m, 'dimensions'
    assert all(len(rr)==2 for rr in z) and all(len(rr)==m for rr in P), 'dimensions'
    assert sum(x)==1 and all(v>0 for v in x), 'masses'
    assert all(c*c+s*s==1 for c,s in z), 'unit circle'
    assert any(v!=z[0] for v in z[1:]), 'synchrony'
    assert all(P[i][j]==P[j][i] and 0<=P[i][j]<=1
               for i in range(m) for j in range(m)), 'densities'
    C = [[z[i][0]*z[j][0]+z[i][1]*z[j][1] for j in range(m)] for i in range(m)]
    S = [[z[i][1]*z[j][0]-z[i][0]*z[j][1] for j in range(m)] for i in range(m)]
    residual = [sum(x[j]*P[i][j]*S[i][j] for j in range(m)) for i in range(m)]
    assert all(v==0 for v in residual), 'equilibrium'
    strength = [sum(x[j]*P[i][j]*C[i][j] for j in range(m)) for i in range(m)]
    assert all(v>0 for v in strength), 'internal stability'
    H = [[-x[i]*x[j]*P[i][j]*C[i][j] if i!=j else F(0)
          for j in range(m)] for i in range(m)]
    for i in range(m): H[i][i] = -sum(H[i])
    assert all(sum(rr)==0 for rr in H), 'rotation identity'
    L = [[F(0) for _ in range(m-1)] for _ in range(m-1)]
    pivots = []
    for i in range(m-1):
        pivot = H[i][i]-sum(L[i][k]**2*pivots[k] for k in range(i))
        assert pivot>0, 'transverse stability: nonpositive LDL pivot at '+str(i)
        pivots.append(pivot)
        L[i][i] = F(1)
        for j in range(i+1,m-1):
            L[j][i] = (H[j][i]-sum(L[j][k]*L[i][k]*pivots[k] for k in range(i)))/pivot
    degrees = [sum(P[i][j]*x[j] for j in range(m)) for i in range(m)]
    report = {'exact_equilibrium':True,'residual':[str(v) for v in residual],
              'strict_transverse_stability':True,'LDL_pivots':[str(v) for v in pivots],
              'internal_strengths':[str(v) for v in strength],
              'mu':str(min(degrees)),'degrees':[str(v) for v in degrees],
              'above_11_16':min(degrees)>F(11,16),
              'nonsynchronous':True,'method':'Exact fractions, unit-circle coordinates, exact gauge LDL; no floating-point acceptance.'}
    if 'realization_denominator' in row:
        D = int(row['realization_denominator'])
        assert D>0 and D%2==0, 'realization denominator'
        assert all((v*D).denominator==1 for v in x), 'mass denominator'
        assert all((v*D).denominator==1 for rr in P for v in rr), 'density denominator'
        assert all(P[i][i]<=1-F(1,D) for i in range(m)), 'diagonal realization slack'
        # N=m(m+3)/2. Since 8N < 2^b and D < 2^k, log(8DN)<k+b.
        N = m*(m+3)//2
        k, b = D.bit_length(), (8*N).bit_length()
        cm = min(strength)
        lhs = cm*D-3
        assert lhs>0 and lhs*lhs>8*D*(k+b), 'realization sufficient condition'
        n = D*D
        mu = min(degrees)
        assert (mu*n).denominator==1, 'integer minimum degree'
        report['realization'] = {'source':'O Keeffe v1, Lemma 2; existential shift-set realization, not an enumerated graph.',
            'D':str(D),'ell':1,'n':str(n),'minimum_degree':str(mu*n),
            'normalization_delta_over_n':str(mu),
            'normalization_proposal':str(mu+F(1,n)),
            'normalization_delta_over_n_minus_1':str(mu*n/F(n-1)),
            'ln_8DN_strict_upper':k+b,'condition_checked_exactly':True}
    return report


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data',default='rational_template_data.json')
    parser.add_argument('--control-equilibrium',action='store_true')
    parser.add_argument('--control-zero-mode',action='store_true')
    args=parser.parse_args()
    data_path=ROOT/args.data
    row = json.loads(data_path.read_text(encoding='utf-8'))
    if args.control_equilibrium:
        row['P'][0][2]=row['P'][2][0]=str(F(row['P'][0][2])-F(1,10**8))
    if args.control_zero_mode:
        row = {'x':['1/4']*4,'z':[['1','0'],['0','1'],['-1','0'],['0','-1']],
               'P':[['1','1','0','1'],['1','1','1','0'],['0','1','1','1'],['1','0','1','1']]}
    report = check(row)
    report['data_sha256'] = hashlib.sha256(data_path.read_bytes()).hexdigest()
    report['verifier_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output=data_path.with_name(data_path.stem.removesuffix('_data')+'_certificate.json')
    output.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['LDL_pivots','internal_strengths','degrees']},indent=2))


if __name__ == '__main__':
    main()
