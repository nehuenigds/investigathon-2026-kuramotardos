"""Exact coupled mass lower bounds from products of flow/mass ratios."""
from fractions import Fraction as F
from profile_upper_interval_refined import covariance_caps,row_bounds,split,SQRT_DEN


def lower_masses(box,u):
    (a,A),(b,B),(c,C)=box
    ell=[u/(1+2*v) for v in (A,B,C)]
    A0=max(ell[0],u-F(1,2));C0=max(ell[2],u-F(1,2))
    # Any admissible y obeys a*y_A <= y_B,y_W;
    # b*y_B <= y_A,y_C; c*y_C <= y_B,y_W.
    LB=max(ell[1],a*A0,c*C0)
    LA=max(A0,b*LB);LC=max(C0,b*LB)
    LW=max(u-F(1,2),a*LA,c*LC)
    return [LA,LB,LC,LW]


def impossible(box,u):
    assert F(2,3)<u<F(3,4)
    (a,A),(b,B),(c,C)=box
    if a*b>1 or b*c>1:return 'capacity'
    low=lower_masses(box,u)
    if max(low)>1-u:return 'mass_flow_upper'
    if sum(low)>1:return 'mass_flow_sum'
    D=max(v*(u-v) for v in low)
    s=1-sum(low[:3])
    if max(a,c)*D>2*s*s:return 'whole_mass_projection'
    R=[1-low[2]-low[3],1-low[3]-low[0],1-low[0]-low[1],1-low[1]-low[2]]
    if min(R)**2<2*D:return 'aggregate_cut'
    if 2*b*D>(1-low[1]-low[3])**2:return 'central_mass_projection'
    upper=[min(1-u,1-sum(low)+low[i]) for i in range(3)]
    for (_,hi),top in zip(box,upper):
        if hi*min(R)**2<(u-top)**2:return 'variance_scale'
    return None
