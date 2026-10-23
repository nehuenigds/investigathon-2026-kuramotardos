"""Exact leaf predicates for a covariance-domain exclusion certificate.

All acceptance uses Fractions and integer square-root bounds. Numerical
eigenvectors used by the builder are only proposals for rational witnesses.
"""
from fractions import Fraction as F
from math import isqrt

SQRT_DEN=10**8


def sqrt_lower(x):
    assert x>=0
    return F(isqrt(x.numerator*SQRT_DEN**2//x.denominator),SQRT_DEN)


def covariance_caps(box):
    a,b,c=[p[0] for p in box]
    return min(F(1,2),1-sqrt_lower(a*b)),min(F(1,2),1-sqrt_lower(b*c))


def impossible(box,u):
    (a,A),(b,B),(c,C)=box
    if a*b>1 or b*c>1:return 'capacity'
    f=[u/(1+2*v) for v in [A,B,C]]
    s=1-sum(f)
    if s<0:return 'mass_sum'
    # Every f_j <= 1-u < u/2. Each split leaf supplies an upper bound
    # on the common scale N^2, so all three must be retained.
    assert F(2,3)<u<F(3,4)
    fmax=max(f)
    if max(a,c)*fmax*(u-fmax)>2*s*s:return 'whole_mass'
    return None


def quadratic_min(v,d,K):
    assert v>0 and d>=0 and K>=0
    t=min(K,d/(2*v))
    return v*t*t-d*t


def row_bounds(box,alpha,weights):
    assert 0<=alpha<=1 and all(v>0 for v in weights)
    (a,A),(b,B),(c,C)=box
    K,L=covariance_caps(box)
    assert K>=0 and L>=0
    v,w,z=weights
    d1=2*(alpha*B+(1-alpha)*A)*w+abs(2*alpha-1)*L*z
    d3=2*(alpha*B+(1-alpha)*C)*w+abs(2*alpha-1)*K*v
    d21=2*(alpha*B+(1-alpha)*A)*v
    d23=2*(alpha*B+(1-alpha)*C)*z
    return [v*(4*(1-alpha)*a*a-1)+quadratic_min(v,d1,K),
            w*(4*alpha*b*b-1)+quadratic_min(w,d21,K)+quadratic_min(w,d23,L),
            z*(4*(1-alpha)*c*c-1)+quadratic_min(z,d3,L)]


def split(box,dimension):
    a,b=box[dimension];mid=(a+b)/2
    left=list(box);right=list(box)
    left[dimension]=(a,mid);right[dimension]=(mid,b)
    return left,right
