"""Exact checks for the global optimum of the restricted unequal-mass model.

The theorem and the continuation argument are written in optimalidad_global.md.
All signs used here are certified with rational interval arithmetic. Numerical
approximations in the report are only for readability, never acceptance tests.
"""
import bootstrap
from bootstrap import ROOT
from fractions import Fraction as F
from math import comb
import hashlib
import json
import sympy as S


class Interval:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)

    def __add__(self, other):
        other = other if isinstance(other, Interval) else Interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __mul__(self, other):
        other = other if isinstance(other, Interval) else Interval(other)
        products = [x * y for x in (self.lo, self.hi)
                    for y in (other.lo, other.hi)]
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def report(self):
        return {"lo": str(self.lo), "hi": str(self.hi),
                "lo_approx": float(self.lo), "hi_approx": float(self.hi)}


a, q, r, w, z, t = S.symbols("a q r w z t")
p = 9*a**8 + 72*a**7 + 288*a**6 + 448*a**5 + 470*a**4 + 88*a**3 - 208*a**2 - 128*a - 15
pa = S.Poly(p, a)
assert pa.count_roots(0, 1) == 1
boxes = [box for box, multiplicity in pa.intervals(eps=S.Rational(1, 10**45))
         if 0 < box[0] < box[1] < 1 and multiplicity == 1]
assert len(boxes) == 1
al, au = boxes[0]
assert pa.count_roots(al, au) == 1
ai = Interval(F(str(al)), F(str(au)))
print('Algebraic root isolated exactly.', flush=True)


def reduce_a(expr):
    return S.rem(S.Poly(expr, a), pa).as_expr()


def enclose(expr):
    """Horner evaluation of a polynomial on the isolating interval for a."""
    value = Interval(0)
    for coef in S.Poly(expr, a).all_coeffs():
        value = value * ai + F(str(coef))
    return value


def rational_enclose(expr):
    num, den = S.fraction(S.cancel(expr))
    ni, di = enclose(num), enclose(den)
    assert not di.lo <= 0 <= di.hi
    return ni * Interval(1/di.hi, 1/di.lo)


def bernstein_certificate(expr, variable, endpoint, sign, reduce=False):
    """Certify a polynomial sign on [0, endpoint] from every Bernstein coefficient."""
    poly = S.Poly(expr, variable)
    n = poly.degree()
    coefficients = []
    for j in range(n + 1):
        coefficient = S.expand(sum(poly.nth(k) * endpoint**k
            * S.Rational(comb(j, k), comb(n, k)) for k in range(j + 1)))
        if reduce:
            coefficient = reduce_a(coefficient)
        box = enclose(coefficient)
        assert box.lo > 0 if sign == 1 else box.hi < 0
        coefficients.append({"polynomial_in_a": str(coefficient), **box.report()})
    return {"degree": n, "endpoint": str(endpoint), "sign": sign,
            "coefficients": coefficients}


K = 1 + 2*q - q*q
D = r*r*(-2*(q+1)**2*w*w + 4*(1-q*q)*w + 2*K) + K*w*w
R = 4*r*r + K*w*w + 4*(1-q*q)*w - 4*(q+1)**2
c = (4+2*a)/(7+a)
U = (-2*a + 5*q + 1)/(3*a+1)
L = ((a+2)*q + 2*a-1)/((a+7)*q-3*a-1)
g1 = (2*r+2+2*q)/(4*r+3+q)
g2 = (2+2*r*(1+q))/(4*r+3+q)
assert S.cancel(g1.subs(r, U)-c) == 0
assert S.cancel(g2.subs(r, L)-c) == 0
assert S.cancel(U.subs(q, a)-1) == 0
assert S.cancel(L.subs(q, a)-1) == 0
assert S.cancel(S.diff(L, q) + 5*(a*a+4*a-1)/((a+7)*q-3*a-1)**2) == 0
assert enclose(a*a+4*a-1).lo > 0
assert ai.lo > S.Rational(13, 20) and ai.hi < S.Rational(33, 50)
assert rational_enclose(c-S.Rational(2, 3)).lo > 0
rmax = U.subs(q, 1)
rmin = L.subs(q, 1)
assert S.cancel(rmax*rmin-1) == 0
assert rational_enclose(rmin-S.Rational(31, 50)).lo > 0
assert rational_enclose(S.Rational(8, 5)-rmax).lo > 0
assert enclose((7+a)*S.Rational(31, 50)-2-a).lo > 0

ratio = (a*a+6*a+1)/(a+1)**2
wstar = S.cancel((4*a*a+8*a-(1+2*a-a*a)*ratio)/(4*(1-a*a)))
for expr in (wstar*wstar-ratio, D.subs({r: 1, q: a, w: wstar}),
             R.subs({r: 1, q: a, w: wstar})):
    numerator, denominator = S.fraction(S.cancel(expr))
    assert reduce_a(numerator) == 0
    denominator_box = enclose(denominator)
    assert not denominator_box.lo <= 0 <= denominator_box.hi
assert rational_enclose(wstar-1).lo > 0
assert rational_enclose(2-wstar).lo > 0

# All degree candidates have 1 < w < 2 if D,R >= 0.
bounds = {}
for name, expr, expected_den in [
    ("R_at_w1_rU", R.subs({r: U, w: 1}), (3*a+1)**2),
    ("D_at_w2_rL", D.subs({r: L, w: 2}), ((a+7)*q-3*a-1)**2),
]:
    numerator = S.cancel(expr * expected_den)
    assert S.fraction(numerator)[1] == 1
    numerator = S.expand(numerator.subs(q, a+(1-a)*t))
    bounds[name] = bernstein_certificate(numerator, t, S.Integer(1), -1)
print('Degree and phase-ratio bounds verified.', flush=True)

# On the coarse box containing every candidate, D and R decrease in q.
# D_q decreases with w >= 1; at w=1 it is -16*r^2*q+2*(1-q).
coefficient_w2 = -4*S.Rational(31, 50)**2*(1+S.Rational(13, 20)) + 2*(1-S.Rational(13, 20))
Dq_upper = -16*S.Rational(31, 50)**2*S.Rational(13, 20) + 2*(1-S.Rational(13, 20))
Rq_upper = -24*S.Rational(13, 20)
assert coefficient_w2 < 0 and Dq_upper < 0 and Rq_upper < 0
assert S.expand(S.diff(D, q).subs(w, 1) - (-16*r*r*q+2*(1-q))) == 0

# Along either active degree boundary, a positive resultant excludes a common
# root of D,R. No numerical root finding is used for this step.
res4 = S.cancel(S.resultant(D, R, w)/4)
assert S.expand(res4.subs(r, 1) - p.subs(a, q)) == 0
boundaries = {}
for name, qq, denominator, direction, endpoint in [
    ("r_ge_1", ((1+3*a)*r+2*a-1)/5, S.Integer(5), 1, S.Rational(3, 5)),
    ("r_le_1", ((1+3*a)*r+2*a-1)/((7+a)*r-2-a),
     (7+a)*r-2-a, -1, S.Rational(19, 50)),
]:
    raw, actual_denominator = S.fraction(S.together(res4.subs(q, qq)))
    assert S.expand(actual_denominator-denominator**8) == 0
    raw_poly = S.Poly(raw, r)
    reduced = sum(reduce_a(coef)*r**monomial[0]
                  for monomial, coef in raw_poly.terms())
    shifted = S.Poly(S.expand(reduced.subs(r, 1+direction*z)), z)
    coefficients = [reduce_a(shifted.nth(k)) for k in range(shifted.degree()+1)]
    assert coefficients[0] == 0
    quotient = sum(coef*z**(k-1) for k, coef in enumerate(coefficients) if k > 0)
    cert = bernstein_certificate(quotient, z, endpoint, 1, reduce=True)
    cert.update({"q_boundary": str(qq), "positive_denominator_power": str(denominator**8),
                 "quotient_after_root_reduction": str(quotient),
                 "factor_removed": "z", "r_substitution": str(1+direction*z)})
    boundaries[name] = cert
    print(name, 'resultant sign verified.', flush=True)

# At q=1 both endpoints are infeasible. Convexity bounds s^2-4s+1 by
# its negative endpoint values throughout s in [(31/50)^2,(8/5)^2].
endpoint_values = [s*s-4*s+1 for s in (S.Rational(31, 50)**2, S.Rational(8, 5)**2)]
assert all(v < 0 for v in endpoint_values)
assert S.expand(D.subs(q, 1) - (4*r*r+(2-8*r*r)*w*w)) == 0
assert S.expand(R.subs(q, 1) - (4*r*r+2*w*w-16)) == 0

report = {
    "claim": "Global maximum of the restricted reduced model is (4+2a)/(7+a), uniquely at r=1,q=a,w=w_star; no claim for all templates or finite splitting.",
    "root_polynomial": str(p), "root_interval": [str(al), str(au)],
    "root_interval_approx": [float(al), float(au)],
    "connectivity_interval": rational_enclose(c).report(),
    "rmin_interval": rational_enclose(rmin).report(),
    "rmax_interval": rational_enclose(rmax).report(),
    "wstar_interval": rational_enclose(wstar).report(),
    "phase_ratio_bounds": bounds,
    "Dq_coarse_upper": str(Dq_upper), "Rq_coarse_upper": str(Rq_upper),
    "boundary_resultants": boundaries,
    "q1_infeasibility_endpoint_values": [str(v) for v in endpoint_values],
    "source_sha256": hashlib.sha256((ROOT/'verify_global_optimum.py').read_bytes()).hexdigest(),
    "sympy_version": S.__version__, "all_assertions_passed": True,
}
(ROOT/'global_optimum_certificate.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({"all_assertions_passed": True,
    "connectivity": report['connectivity_interval'],
    "bernstein_degrees": {name: cert['degree'] for name, cert in boundaries.items()},
    "bernstein_min_lower_approx": {name: min(v['lo_approx'] for v in cert['coefficients'])
                                  for name, cert in boundaries.items()}}, indent=2))
