"""Exact interval Bernstein certificates for three Sylvester minors."""
from fractions import Fraction as F
from math import comb
from profile_upper_interval_refined import covariance_caps

def iv(x):return x if isinstance(x,tuple) else (F(x),F(x))
def add(x,y):
    x,y=iv(x),iv(y);return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    x,y=iv(x),iv(y);v=[a*b for a in x for b in y];return min(v),max(v)
def scale(x,y):return mul(x,F(y))
def sub(x,y):return add(x,scale(y,-1))

def coefficients(box,t):
    (a,A),(b,B),(c,C)=box
    aa=(4*(1-t)*a*a-1,4*(1-t)*A*A-1)
    bb=(4*t*b*b-1,4*t*B*B-1)
    cc=(4*(1-t)*c*c-1,4*(1-t)*C*C-1)
    p=(t*b+(1-t)*a,t*B+(1-t)*A)
    q=(t*b+(1-t)*c,t*B+(1-t)*C)
    r=2*t-1
    p4=scale(mul(p,p),4);q4=scale(mul(q,q),4)
    d2={(0,0):mul(aa,bb),(1,0):sub(add(aa,bb),p4),(0,1):aa,
        (2,0):iv(1),(1,1):iv(1)}
    mid=add(add(aa,bb),cc)
    mid=sub(sub(mid,p4),q4);mid=sub(mid,scale(bb,r*r));mid=add(mid,scale(mul(p,q),8*r))
    d3={(0,0):mul(mul(aa,bb),cc),(1,0):mul(cc,sub(add(aa,bb),p4)),
        (0,1):mul(aa,sub(add(bb,cc),q4)),(2,0):cc,(0,2):aa,
        (1,1):mid,(2,1):iv(1-r*r),(1,2):iv(1-r*r)}
    return aa,d2,d3

def bernstein_lower(poly,x0,x1,y0,y1):
    power={}
    for (i,j),v in poly.items():
        for k in range(i+1):
            for l in range(j+1):
                factor=comb(i,k)*comb(j,l)*x0**(i-k)*(x1-x0)**k*y0**(j-l)*(y1-y0)**l
                power[k,l]=add(power.get((k,l),iv(0)),scale(v,factor))
    lows=[]
    for k in range(3):
        for l in range(3):
            total=iv(0)
            for i in range(k+1):
                for j in range(l+1):
                    total=add(total,scale(power.get((i,j),iv(0)),F(comb(k,i)*comb(l,j),comb(2,i)*comb(2,j))))
            lows.append(total[0])
    return min(lows)

def prove(box,t,depth=1):
    aa,d2,d3=coefficients(box,t)
    if aa[0]<=0:return None
    K,L=covariance_caps(box)
    if min(K,L)<0:return None
    n=2**depth;minimum=aa[0]
    for i in range(n):
        for j in range(n):
            x0,x1=K*K*F(i,n),K*K*F(i+1,n)
            y0,y1=L*L*F(j,n),L*L*F(j+1,n)
            for polynomial in (d2,d3):
                low=bernstein_lower(polynomial,x0,x1,y0,y1)
                if low<=0:return None
                minimum=min(minimum,low)
    return minimum
