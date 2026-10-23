"""Exact arithmetic for the (2,2,2,1) quarter-turn leading-profile model.

The three scalar tests characterize an aggregate second-order completion.
They do not by themselves classify a finite floating-point candidate.
Finite rational templates are accepted only by verify_rational_template.check.
"""
from fractions import Fraction as F

SHEETS = [0, 0, 1, 1, 2, 2, 3]
EDGES = [(0,2),(0,3),(1,2),(1,3),(2,4),(2,5),(3,4),(3,5),(4,6),(5,6),(6,0),(6,1)]
TREE = [0, 2, 4, 6, 8, 9]
V = [[1,1,1],[0,2,0],[-1,1,1],[0,0,0]]
Z = [[F(-1,2),0,0],[F(1,2),0,0],[0,F(-1,2),0],
     [0,F(1,2),0],[0,0,F(-1,2)],[0,0,F(1,2)],[0,0,0]]
CYCLES = [{0:-1,2:1,10:-1,11:1},
          {0:-1,1:1,4:-1,6:1}, {4:-1,5:1,8:-1,9:1}]


def unequal_profile(r,q,w,t,rho=F(1)):
    r,q,w,t,rho = map(F,[r,q,w,t,rho])
    assert r>0 and 0<q<1 and w>0 and (1-q)/2<t<(1+q)/2
    assert 0<rho<=1
    X,Y = 2*t,2*(1-t)
    m = [r*X,r*Y,Y,X,r*X,r*Y,1+q]
    g,xy = 1+q,r*X*Y
    a = [xy,2*r*g*t-xy,2*r*g*(1-t)-xy,xy,
         xy,2*r*g*(1-t)-xy,2*r*g*t-xy,xy,
         2*r*g*t,2*r*g*(1-t),2*r*g*t,2*r*g*(1-t)]
    u = [-(1-t),t,-t*w,(1-t)*w,-(1-t),t,F(0)]
    return {'masses':list(map(str,m)), 'adjacent_conductances':[str(rho*v) for v in a],
            'offsets':list(map(str,u)), 'parameters':{'r':str(r),'q':str(q),'w':str(w),'t':str(t),'rho':str(rho)}}


def solve(A, rhs):
    n = len(rhs)
    M = [[F(x) for x in row]+[F(y)] for row,y in zip(A,rhs)]
    for i in range(n):
        j = next(j for j in range(i,n) if M[j][i])
        M[i],M[j] = M[j],M[i]
        pivot = M[i][i]
        M[i] = [x/pivot for x in M[i]]
        for j in range(n):
            if j != i:
                a = M[j][i]
                M[j] = [x-a*y for x,y in zip(M[j],M[i])]
    return [row[-1] for row in M]


def tree_flow(rhs):
    assert sum(rhs) == 0
    A = [[F(int(EDGES[e][0]==i)-int(EDGES[e][1]==i)) for e in TREE] for i in range(6)]
    values = solve(A,rhs[:6])
    out = [F(0)]*12
    for e,v in zip(TREE,values):
        out[e] = v
    return out


def divergence(a):
    out = [F(0)]*7
    for (i,j),v in zip(EDGES,a):
        out[i] += v
        out[j] -= v
    return out


def blocks(m,a,u):
    J = [m[0]*m[1],m[2]*m[3],m[4]*m[5]]
    E = sum(J[k]*(u[2*k]-u[2*k+1])**2 for k in range(3))
    C = [[sum(v*(u[i]-u[j])*(V[SHEETS[i]][k]-V[SHEETS[j]][k])*(Z[i][l]-Z[j][l])
              for (i,j),v in zip(EDGES,a)) for l in range(3)] for k in range(3)]
    P = [[sum(C[k][l]*C[t][l]/J[l] for l in range(3)) for t in range(3)] for k in range(3)]
    return J,E,C,P


def analyze(profile, strict=False):
    m = list(map(F,profile['masses']))
    a = list(map(F,profile['adjacent_conductances']))
    u = list(map(F,profile['offsets']))
    assert len(m)==7 and len(a)==12 and len(u)==7
    assert all(v>0 for v in m), 'positive masses'
    assert all(0<v<=m[i]*m[j] for (i,j),v in zip(EDGES,a)), 'adjacent capacity'
    assert divergence(a)==[0]*7, 'zeroth-order equilibrium'
    cuts = [sum(a[e]*(u[i]-u[j]) for e,(i,j) in enumerate(EDGES) if SHEETS[i]==k) for k in range(4)]
    assert cuts==[0]*4, 'first-order leaf cuts'
    J,E,C,P = blocks(m,a,u)
    slack = [E-P[k][k] for k in range(3)]
    assert E>0, 'nonzero splitting'
    assert all(v>=0 for v in slack), 'second-order obstruction'
    if strict:
        assert all(v<m[i]*m[j] for (i,j),v in zip(EDGES,a)), 'interior adjacent densities'
        assert all(u[2*k]!=u[2*k+1] for k in range(3)), 'three nonzero splits'
        assert all(v>0 for v in slack), 'strict second-order obstruction'
    M = [sum(m[i] for i in range(7) if SHEETS[i]==k) for k in range(4)]
    degrees = [M[SHEETS[i]] for i in range(7)]
    for (i,j),v in zip(EDGES,a):
        degrees[i] += v/m[i]
        degrees[j] += v/m[j]
    return {'J':J,'E':E,'C_modal':C,'P_modal':P,'slack':slack,
            'mu':min(degrees)/sum(m),'degrees':[d/sum(m) for d in degrees]}


def tangent(profile):
    result = analyze(profile,strict=True)
    m,a,u = (list(map(F,profile[key])) for key in ['masses','adjacent_conductances','offsets'])
    E,P = result['E'],result['P_modal']
    s12,s13,s23 = P[0][1],P[0][2],P[1][2]
    target = [(E-s12+s13-s23)/4,(E+s12-s13-s23)/4,
              (E-s12-s13+s23)/4,(E+s12+s13+s23)/4]
    internal = [F(0)]*7
    for k in range(3):
        i,j = 2*k,2*k+1
        force = m[i]*m[j]*(u[i]-u[j])
        internal[i] += force
        internal[j] -= force
    first = tree_flow(internal)
    def cuts(values):
        return [sum(values[e]*(u[i]-u[j]) for e,(i,j) in enumerate(EDGES) if SHEETS[i]==k) for k in range(4)]
    baseline = cuts(first)
    delta = [x-y for x,y in zip(target,baseline)]
    widths = [u[2*k+1]-u[2*k] for k in range(3)]
    lC = delta[2]/widths[2]
    lB = (delta[1]+lC*widths[2])/widths[1]
    lA = (delta[0]+lB*widths[1])/widths[0]
    for cycle,weight in zip(CYCLES,[lA,lB,lC]):
        for e,value in cycle.items():
            first[e] += weight*value
    assert divergence(first)==internal
    assert cuts(first)==target
    result.update(first_order_conductances=first,aggregate_weights=target)
    return result


def finite(profile,h):
    h = F(h)
    assert h>0
    result = tangent(profile)
    m,a,u = (list(map(F,profile[key])) for key in ['masses','adjacent_conductances','offsets'])
    P = [[F(int(SHEETS[i]==SHEETS[j])) for j in range(7)] for i in range(7)]
    for (i,j),v,dv in zip(EDGES,a,result['first_order_conductances']):
        P[i][j] = P[j][i] = (v+h*dv)/(m[i]*m[j])
    z = []
    for k,v in zip(SHEETS,u):
        t = h*v/2
        c,s = (1-t*t)/(1+t*t),2*t/(1+t*t)
        for _ in range(k):
            c,s = -s,c
        z.append((c,s))
    sine = lambda i,j: z[i][1]*z[j][0]-z[i][0]*z[j][1]
    residual = [sum(m[i]*m[j]*P[i][j]*sine(i,j) for j in range(7)) for i in range(7)]
    correction = tree_flow([-b for b in residual])
    for e in TREE:
        i,j = EDGES[e]
        P[i][j] = P[j][i] = P[i][j]+correction[e]/(m[i]*m[j]*sine(i,j))
    assert all(sum(m[j]*P[i][j]*sine(i,j) for j in range(7))==0 for i in range(7))
    return {'x':[str(v/sum(m)) for v in m], 'z':[[str(v) for v in zz] for zz in z],
            'P':[[str(v) for v in row] for row in P], 'h':str(h),
            'model':'Homogeneous weighted seven-cluster template; interior leading adjacent densities; zero opposite links.'}
