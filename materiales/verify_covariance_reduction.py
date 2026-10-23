"""Exact identities behind the variance/covariance necessary relaxation."""
import bootstrap
from bootstrap import ROOT
from pathlib import Path
import hashlib,json
import sympy as S

f,g,h,x,y=S.symbols('f g h x y',real=True)
kA,kB,kC=S.symbols('kA kB kC',positive=True)
edges=[(0,2),(0,3),(1,2),(1,3),(2,4),(2,5),(3,4),(3,5),(4,6),(5,6),(6,0),(6,1)]
a=[x,f-x,g-x,1-f-g+x,y,g-y,h-y,1-g-h+y,h,1-h,f,1-f]
u=[-(1-f)*kA,f*kA,-(1-g)*kB,g*kB,-(1-h)*kC,h*kC,0]
sheet=[0,0,1,1,2,2,3]
modal=S.Matrix([[1,1,1],[0,2,0],[-1,1,1],[0,0,0]])
Z=S.zeros(7,3)
for i in range(6):Z[i,i//2]=S.Rational(-1 if i%2==0 else 1,2)
C=S.zeros(3)
for (i,j),v in zip(edges,a):
    du=modal[sheet[i],:]-modal[sheet[j],:];dz=Z[i,:]-Z[j,:]
    C+=v*(u[i]-u[j])*du.T*dz
ab=x-f*g;bc=y-g*h
expected=S.Matrix([[-ab*kB,2*g*(1-g)*kB-ab*kA-bc*kC,-bc*kB],
                   [-2*f*(1-f)*kA+ab*kB,ab*kA-bc*kC,2*h*(1-h)*kC-bc*kB],
                   [-ab*kB,bc*kC-ab*kA,bc*kB]])
assert all(S.expand(v)==0 for v in C-expected)

jA,jB,jC=S.symbols('jA jB jC',positive=True)
zA,zB,zC=S.symbols('zA zB zC',positive=True)
chi=[f*(1-f)/jA,g*(1-g)/jB,h*(1-h)/jC]
kap=ab/S.sqrt(jA*jB);lam=bc/S.sqrt(jB*jC)
L1=S.Matrix([[-kap,0,0]])  # actual modal rows are written explicitly below
normal=expected.subs({kA:zA/S.sqrt(jA),kB:zB/S.sqrt(jB),kC:zC/S.sqrt(jC)})*S.diag(1/S.sqrt(jA),1/S.sqrt(jB),1/S.sqrt(jC))
want=S.Matrix([[-kap*zB,2*chi[1]*zB-kap*zA-lam*zC,-lam*zB],
               [-2*chi[0]*zA+kap*zB,kap*zA-lam*zC,2*chi[2]*zC-lam*zB],
               [-kap*zB,lam*zC-kap*zA,lam*zB]])
assert all(S.simplify(v)==0 for v in normal-want)

A,B,D,K,L,alpha=S.symbols('A B D K L alpha',real=True)
M1=S.Matrix([[0,-K,0],[-K,2*B,-L],[0,-L,0]])
M2=S.Matrix([[-2*A,K,0],[K,0,-L],[0,-L,2*D]])
combo=alpha*M1.T*M1+(1-alpha)*M2.T*M2
explicit=S.Matrix([[4*(1-alpha)*A*A+K*K,-2*K*(alpha*B+(1-alpha)*A),(2*alpha-1)*K*L],
                   [-2*K*(alpha*B+(1-alpha)*A),4*alpha*B*B+K*K+L*L,-2*L*(alpha*B+(1-alpha)*D)],
                   [(2*alpha-1)*K*L,-2*L*(alpha*B+(1-alpha)*D),4*(1-alpha)*D*D+L*L]])
assert all(S.expand(v)==0 for v in combo-explicit)

# For a positive 2x2 transport of total one, Delta is its determinant.
p,r,s=S.symbols('p r s',positive=True);t=1-p-r-s
delta=p*t-r*s
variance=(p+r)*(s+t)*(p+s)*(r+t)
assert S.expand(variance-(p-delta)*(t-delta))==0
assert S.expand(variance-delta**2-(p*t*(r+s)+r*s*(p+t)))==0
root=S.symbols('root',nonnegative=True)
identity=S.expand((root-delta)**2-variance-delta*(p+t-2*root))
assert S.expand(identity.subs(root**2,p*t))==0

# Determinants used by the separate interval Bernstein checker.
A0,B0,C0,p0,q0,r0=S.symbols('A0 B0 C0 p0 q0 r0',real=True)
matrix=S.Matrix([[A0+K*K,-2*K*p0,r0*K*L],
                 [-2*K*p0,B0+K*K+L*L,-2*L*q0],
                 [r0*K*L,-2*L*q0,C0+L*L]])
minor2=A0*B0+(A0+B0-4*p0*p0)*K*K+A0*L*L+K**4+K*K*L*L
det3=(A0*B0*C0+C0*(A0+B0-4*p0*p0)*K*K+A0*(B0+C0-4*q0*q0)*L*L
      +C0*K**4+A0*L**4
      +(A0+B0+C0-4*p0*p0-4*q0*q0-r0*r0*B0+8*r0*p0*q0)*K*K*L*L
      +(1-r0*r0)*(K**4*L*L+K*K*L**4))
assert S.expand(matrix[:2,:2].det()-minor2)==0
assert S.expand(matrix.det()-det3)==0
jj=S.symbols('J0:3',positive=True);bb=S.symbols('beta0:3',nonnegative=True)
kk=S.symbols('width0:3',real=True);zz=S.symbols('correction0:3',real=True)
completion=sum(jj[i]*kk[i]**2+jj[i]*zz[i]**2 for i in range(3))
original=sum(bb[i]*jj[i]*kk[i]**2+bb[i]*jj[i]*zz[i]**2 for i in range(3))
assert S.expand(completion-original-sum((1-bb[i])*jj[i]*(kk[i]**2+zz[i]**2) for i in range(3)))==0
report={'all_assertions_passed':True,'sympy':S.__version__,
        'modal_cross_block':[[str(S.factor(v)) for v in row] for row in expected.tolist()],
        'weighted_squared_form':[[str(v) for v in row] for row in explicit.tolist()],
        'transport_bound':'abs(kappa)+sqrt(chi_left*chi_right)<=1',
        'sylvester_minor_polynomials_verified':True,
        'internal_completion_monotonicity_identity_verified':True,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Algebraic identities. Inequalities and continuous-profile reduction are proved in cota_perfil_general.md. Not a universal Kuramoto bound or independent human review.'}
(ROOT/'covariance_reduction_certificate.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_assertions_passed':True,'transport_identity':True,'three_normalized_tests':True,'weighted_form':True}))
