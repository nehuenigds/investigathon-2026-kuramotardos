"""Exact identities for the attributed quarter-turn obstruction and its example.

This checks the new finite lemma and bindings, not the entire asymptotic proof.
No floating-point stability classification, search, or tree reconstruction.
"""
from pathlib import Path
import hashlib
import json
import bootstrap
import sympy as S

ROOT = Path(__file__).resolve().parent


def verify():
    angles = S.symbols('theta0:4', real=True)
    A, B, C, D, U, V = S.symbols('A B C D U V', nonnegative=True)
    edges = [(0, 1, A), (1, 2, B), (2, 3, C), (0, 3, D), (0, 2, U), (1, 3, V)]
    energy = sum(w * (1 - S.cos(angles[i] - angles[j])) for i, j, w in edges)
    base = dict(zip(angles, [0, S.pi/2, S.pi, 3*S.pi/2]))
    grad = S.Matrix([S.diff(energy, q).subs(base) for q in angles])
    assert grad == S.Matrix([D-A, A-B, B-C, C-D])
    hessian = S.hessian(energy, angles).subs(base)
    q1, q2 = S.Matrix([1, 0, -1, 0]), S.Matrix([1, 2, 1, 0])
    assert (q1.T * hessian * q1)[0] == -4*U
    assert (q2.T * hessian * q2)[0] == -4*V
    t = S.symbols('t', real=True)
    T, r = S.symbols('T r', positive=True)
    equal = {A:T, B:T, C:T, D:T, U:0, V:0}
    moved = dict(zip(angles, [-t, S.pi/2+t, S.pi, 3*S.pi/2]))
    difference = (energy.subs(moved) - energy.subs(base)).subs(equal)
    assert S.trigsimp(difference - T*(S.sin(2*t)-2*S.sin(t))) == 0
    cosine, sine = (1-r*r)/(1+r*r), 2*r/(1+r*r)
    points = [(cosine, -sine), (-sine, cosine), (-1, 0), (0, -1)]
    dot = lambda u, v: u[0]*v[0] + u[1]*v[1]
    circle_energy = sum(w*(1-dot(points[i], points[j])) for i,j,w in edges).subs(equal)
    rational_difference = S.factor(circle_energy - 4*T)
    assert rational_difference == -8*T*r**3/(1+r*r)**2

    x = [S.Rational(1,8)]*6 + [S.Rational(1,4)]
    leaves = [0,0,1,1,2,2,3]
    points0 = [(1,0),(0,1),(-1,0),(0,-1)]
    P = [[S.Integer((leaves[i]-leaves[j]) % 4 != 2) for j in range(7)] for i in range(7)]
    z0 = [points0[j] for j in leaves]
    sindiff = lambda u,v: u[1]*v[0]-u[0]*v[1]
    residual = [sum(x[j]*P[i][j]*sindiff(z0[i],z0[j]) for j in range(7)) for i in range(7)]
    assert residual == [0]*7
    degree = [sum(x[j]*P[i][j] for j in range(7)) for i in range(7)]
    assert min(degree) == S.Rational(3,4)
    H = S.zeros(7)
    for i in range(7):
        for j in range(i+1,7):
            w = x[i]*x[j]*P[i][j]*dot(z0[i],z0[j])
            H[i,i] += w; H[j,j] += w; H[i,j] -= w; H[j,i] -= w
    block = S.Matrix([[1,-1],[-1,1]])/64
    assert H == S.diag(block,block,block,S.zeros(1))
    assert H*S.ones(7,1) == S.zeros(7,1) and H.rank() == 3
    def E(z):
        return sum(x[i]*x[j]*P[i][j]*(1-dot(z[i],z[j])) for i in range(7) for j in range(i+1,7))
    assert E(z0) == S.Rational(1,4)
    examples = []
    for value in (S.Rational(1,10),S.Rational(1,100),S.Rational(1,1000)):
        co, si = cosine.subs(r,value), sine.subs(r,value)
        points1 = [(co,-si),(-si,co),(-1,0),(0,-1)]
        assert all(S.factor(dot(z,z)-1) == 0 for z in points1)
        z1 = [points1[j] for j in leaves]
        diff = S.factor(E(z1)-E(z0))
        assert diff == -value**3/(2*(1+value**2)**2) and diff < 0
        examples.append({'tan_half_angle':str(value),'energy_difference':str(diff)})

    n, ni, nj, e = S.symbols('n ni nj e', positive=True)
    assert S.cancel((ni/n)*(nj/n)*(e/(ni*nj))-e/n**2) == 0
    bindings = ['cota_perfil_general.md','cota_capacidades_agregadas.md','cota_flujos_06934.md',
                'cota_minimos_locales_06934.md','profile_upper_certificate_06934-v1.json',
                'profile_upper_certificate_06934-v1_verification.json','verify_profile_upper_mass_flow.py']
    cert = json.loads((ROOT/'profile_upper_certificate_06934-v1.json').read_text())
    replay = json.loads((ROOT/'profile_upper_certificate_06934-v1_verification.json').read_text())
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    assert cert['complete'] and cert['target'] == '3467/5000'
    assert replay['covered_root_exactly'] and replay['all_leaves_verified']
    assert replay['certificate_sha256'] == sha(ROOT/'profile_upper_certificate_06934-v1.json')
    assert replay['verifier_sha256'] == sha(ROOT/'verify_profile_upper_mass_flow.py')
    return {'finite_identities_passed':True,'source':'Lepsveridze-Zhang v1 Lemma 11, adapted to weighted templates',
            'opposite_modal_forms':['-4*U','-4*V'],'rational_energy_difference':str(rational_difference),
            'baseline_equilibrium_checked_before_hessian':True,'baseline_mu':'3/4',
            'baseline_hessian_psd_by_blocks':True,'baseline_hessian_rank':3,'baseline_transverse_zero_modes':3,
            'baseline_is_not_a_local_minimum':True,'examples':examples,
            'perturbed_points_claimed_as_equilibria':False,'aggregation_energy_coefficient_identity':True,
            'existing_tree_bound_by_hash':True,'tree_reexecuted':False,'tree_reconstructed':False,
            'source_sha256':{name:sha(ROOT/name) for name in bindings},
            'verifier_source_sha256':sha(Path(__file__)),
            'scope':'Exact finite obstruction, illustrative descents and source bindings. The asymptotic implication also requires the written reduction; not independent human review or novelty verification.'}


if __name__ == '__main__':
    report = verify()
    (ROOT/'quarter_turn_local_minima_verification.json').write_text(
        json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('finite_identities_passed','baseline_mu',
                     'baseline_hessian_psd_by_blocks','baseline_is_not_a_local_minimum',
                     'existing_tree_bound_by_hash','tree_reexecuted')}))
