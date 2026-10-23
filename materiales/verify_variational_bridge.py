"""Audit identities at the finite-to-modal bridge; not a full proof verifier.

Exact assertions and high-precision numerical controls are reported separately.
No constructor, tree replay, numerical eigensolver, or temporary output in W.
"""
import bootstrap
from bootstrap import ROOT
from pathlib import Path
from fractions import Fraction as F
import copy
import hashlib
import json
import sympy as S
import mpmath as mp
from verify_rational_template import check as strict_check

if not __debug__:
    raise RuntimeError('Run without -O: assertions are required.')

SHEETS = (0, 0, 1, 1, 2, 2, 3)
BASE = ((1, 0), (0, 1), (-1, 0), (0, -1))
ADJ = ((0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (2, 5),
       (3, 4), (3, 5), (4, 6), (5, 6), (6, 0), (6, 1))
INTERNAL = ((0, 1), (2, 3), (4, 5))
OPPOSITE = ((0, 4), (0, 5), (1, 4), (1, 5), (2, 6), (3, 6))
PAIRS = INTERNAL + ADJ + OPPOSITE
assert len({frozenset(pair) for pair in PAIRS}) == 21
U_LEAF = S.Matrix([[1, 1, 1], [0, 2, 0], [-1, 1, 1], [0, 0, 0]])
U = S.Matrix([list(U_LEAF[SHEETS[i], :]) for i in range(7)])
Z = S.zeros(7, 3)
for i in range(6):
    Z[i, i // 2] = S.Rational(-1 if i % 2 == 0 else 1, 2)


def symbolic_checks():
    h, d = S.symbols('h d', real=True)
    edge_checks = []
    internal_block = S.zeros(3)
    for index, (i, j) in enumerate(PAIRS):
        base = (SHEETS[i] - SHEETS[j]) * S.pi / 2
        sine = S.expand_trig(S.sin(base + h * d))
        cosine = S.expand_trig(S.cos(base + h * d))
        if (i, j) in INTERNAL:
            rhs = h * d * S.sin(h * d) - h * d * sine
            lhs = S.Integer(0)
            dz = Z[i, :] - Z[j, :]
            internal_block += S.Symbol('a' + str(index)) * dz.T * dz
        elif (i, j) in OPPOSITE:
            rhs = -h * d * S.sin(h * d) - h * d * sine
            lhs = S.Integer(0)
        else:
            lhs = cosine
            rhs = S.sin(h * d) - h * d * S.cos(h * d) - h * d * sine
            assert S.simplify(cosine - S.sin(h * d)) == 0
            assert S.simplify(sine + S.cos(h * d)) == 0
        assert S.simplify(lhs - rhs) == 0, ('residual identity', i, j)
        for alpha in range(2):
            square = (U[i, alpha] - U[j, alpha]) ** 2
            if (i, j) in INTERNAL:
                assert square == 0
            elif (i, j) in ADJ:
                assert square == 1
            else:
                group = 0 if SHEETS[i] in (0, 2) else 1
                assert square == (4 if alpha == group else 0)
        for alpha in range(3):
            for beta in range(3):
                du = U[i, alpha] - U[j, alpha]
                dz = Z[i, beta] - Z[j, beta]
                if (i, j) in ADJ:
                    assert abs(du) == 1 and abs(dz) <= S.Rational(1, 2)
                if (i, j) in OPPOSITE:
                    assert abs(du * dz) <= 1
        edge_checks.append([i, j])
    assert internal_block == S.diag(*S.symbols('a0:3'))
    assert S.diff(S.sin(h * d), h).subs(h, 0) == d

    jj = S.symbols('J0:3', positive=True)
    bb = S.symbols('beta0:3', real=True)
    kk = S.symbols('width0:3', real=True)
    zz = S.symbols('correction0:3', real=True)
    cc = S.symbols('cross0:3', real=True)
    original = sum(bb[i] * jj[i] * (kk[i] ** 2 + zz[i] ** 2) + 2 * cc[i] * zz[i] for i in range(3))
    completed = sum(jj[i] * (kk[i] ** 2 + zz[i] ** 2) + 2 * cc[i] * zz[i] for i in range(3))
    assert S.expand(completed - original - sum((1 - bb[i]) * jj[i] * (kk[i] ** 2 + zz[i] ** 2) for i in range(3))) == 0
    minimizer = completed.subs({zz[i]: -cc[i] / jj[i] for i in range(3)})
    assert S.expand(minimizer - sum(jj[i] * kk[i] ** 2 - cc[i] ** 2 / jj[i] for i in range(3))) == 0

    # Rational bookkeeping of the analytic bounds in the note. Trigonometric
    # inequalities and PSD implications remain part of its written proof.
    assert (F(7, 3) / 2) / F(7, 8) == F(4, 3)
    assert F(4, 3) + 4 * F(4, 3) == F(20, 3)
    assert F(1, 2) + F(1, 3) == F(5, 6)
    return {'all_assertions_passed': True, 'edge_residual_identities': edge_checks,
            'modal_square_factors': True, 'internal_block_normalization': True,
            'mixed_block_factor_bounds': True, 'completion_and_minimizer_identities': True,
            'bound_constant_bookkeeping': True}


def rational_circle(offset):
    r = F(offset, 1000)
    return ((1 - r * r) / (1 + r * r), 2 * r / (1 + r * r))


def degenerate_row(beta, offsets):
    x = [F(1, 8)] * 6 + [F(1, 4)]
    p = [[F(int(i == j)) for j in range(7)] for i in range(7)]
    z = []
    for i, offset in enumerate(offsets):
        c, s = rational_circle(offset)
        c0, s0 = BASE[SHEETS[i]]
        z.append([c0 * c - s0 * s, s0 * c + c0 * s])
    for k, (i, j) in enumerate(INTERNAL):
        p[i][j] = p[j][i] = F(beta[k])
        if beta[k]:
            assert z[i] == z[j], 'Nonzero internal edge must be synchronized in this block control.'
    return {'x': list(map(str, x)), 'z': [[str(v) for v in row] for row in z],
            'P': [[str(v) for v in row] for row in p]}


def block_psd_check(row):
    x = list(map(F, row['x']))
    z = [[F(v) for v in pair] for pair in row['z']]
    p = [[F(v) for v in pair] for pair in row['P']]
    assert sum(x) == 1 and all(v > 0 for v in x)
    assert all(c * c + s * s == 1 for c, s in z)
    residual = [sum(x[j] * p[i][j] * (z[i][1] * z[j][0] - z[i][0] * z[j][1]) for j in range(7)) for i in range(7)]
    assert residual == [F(0)] * 7, 'Exact equilibrium before PSD.'
    nonzero_blocks = 0
    for i in range(7):
        for j in range(i + 1, 7):
            assert p[i][j] == p[j][i] and 0 <= p[i][j] <= 1
            if (i, j) not in INTERNAL:
                assert p[i][j] == 0
            elif p[i][j]:
                assert z[i] == z[j]
                assert x[i] * x[j] * p[i][j] > 0
                nonzero_blocks += 1
    return {'exact_equilibrium': True, 'psd_method': 'Disjoint nonnegative 2x2 Laplacian blocks and zero rows',
            'hessian_rank': nonzero_blocks, 'strict_transverse_stability': False}


def numerical_bridge(row):
    def num(value):
        f = F(value)
        return mp.mpf(f.numerator) / f.denominator
    x = list(map(num, row['x']))
    z = [[num(v) for v in pair] for pair in row['z']]
    p = [[num(v) for v in pair] for pair in row['P']]
    offsets = []
    for i, (c, s) in enumerate(z):
        c0, s0 = BASE[SHEETS[i]]
        offsets.append(mp.atan2(s * c0 - c * s0, c * c0 + s * s0))
    offsets = [value - offsets[6] for value in offsets]
    h = max(map(abs, offsets))
    assert 0 < h <= mp.mpf(1) / 4
    u = [value / h for value in offsets]
    H = mp.matrix(7)
    a = {}
    for i, j in PAIRS:
        weight = x[i] * x[j] * p[i][j]
        a[i, j] = weight
        cosine = z[i][0] * z[j][0] + z[i][1] * z[j][1]
        H[i, j] -= weight * cosine
        H[j, i] -= weight * cosine
        H[i, i] += weight * cosine
        H[j, j] += weight * cosine
    sn = sum(a[i, j] * mp.sin(h * (u[i] - u[j])) for i, j in ADJ)
    opp = sum(a[i, j] for i, j in OPPOSITE)
    opp_cos = sum(a[i, j] * mp.cos(h * (u[i] - u[j])) for i, j in OPPOSITE)
    e = sum(a[i, j] * (u[i] - u[j]) ** 2 for i, j in INTERNAL)
    B = mp.matrix([[int(SHEETS[i] == leaf) for leaf in range(4)] for i in range(7)])
    R = B.T * H * B
    trace = sum(R[i, i] for i in range(4))
    Ump = mp.matrix([[int(v) for v in U.row(i)] for i in range(7)])
    Zmp = mp.matrix([[num(str(v)) for v in Z.row(i)] for i in range(7)])
    Ch = Ump.T * H * Zmp / h
    Jh = Zmp.T * H * Zmp
    Jo = mp.diag([a[i, j] for i, j in INTERNAL])
    J = mp.diag([x[i] * x[j] for i, j in INTERNAL])
    Chat = mp.matrix(3)
    for i, j in ADJ:
        for alpha in range(3):
            for beta in range(3):
                Chat[alpha, beta] += a[i, j] * (u[i] - u[j]) * (Ump[i, alpha] - Ump[j, alpha]) * (Zmp[i, beta] - Zmp[j, beta])
    tolerance = mp.mpf('1e-100')
    checks = {}

    def upper(name, value, bound):
        assert value <= bound + tolerance, (name, mp.nstr(value, 50), mp.nstr(bound, 50))
        checks[name] = {'value': mp.nstr(value, 28), 'bound': mp.nstr(bound, 28)}

    upper('S_lower', -sn, mp.mpf(0))
    upper('S_upper', sn, mp.mpf(7) / 3 * h * h)
    upper('opposite_total', opp, mp.mpf(4) / 3 * h * h)
    upper('leaf_trace', trace, mp.mpf(14) / 3 * h * h)
    assert abs(trace - 2 * sn + 2 * opp_cos) < tolerance
    cuts = [sum(a[i, j] * (u[i] - u[j]) for i, j in ADJ if SHEETS[i] == leaf) for leaf in range(4)]
    upper('four_cut_residuals', max(map(abs, cuts)), mp.mpf(14) / 3 * h + mp.mpf(2) / 3 * h * h)
    upper('rescaled_S_error', abs(sn / h ** 2 - e), mp.mpf(4) / 3 * h + mp.mpf(20) / 3 * h * h)
    upper('cross_block_error', max(abs(Ch[i, j] - Chat[i, j]) for i in range(3) for j in range(3)), mp.mpf(4) / 3 * h + h * h / 3)
    upper('internal_block_error', max(abs(Jh[i, j] - Jo[i, j]) for i in range(3) for j in range(3)), h / 4 + mp.mpf(5) / 6 * h * h)
    assert all(J[i, i] > 0 for i in range(3))
    variations = []
    for alpha in range(2):
        correction = -J ** -1 * Chat[alpha, :].T
        v = Ump[:, alpha] + h * Zmp * correction
        full_value = (v.T * H * v)[0] / h ** 2
        relaxed = sn / h ** 2 + 2 * (Ch * correction)[alpha] + (correction.T * Jh * correction)[0]
        upper('variation_nonnegative_' + str(alpha), -full_value, mp.mpf(0))
        upper('opposites_omitted_above_' + str(alpha), full_value, relaxed)
        variations.append({'alpha': alpha + 1, 'actual_scaled_energy': mp.nstr(full_value, 28),
                           'opposites_omitted_upper': mp.nstr(relaxed, 28)})
    return {'h': mp.nstr(h, 28), 'max_abs_u': mp.nstr(max(map(abs, u)), 5),
            'nonzero_opposite_links': sum(bool(a[i, j]) for i, j in OPPOSITE),
            'positive_internal_coefficients': [bool(Jo[i, i] > 0) for i in range(3)],
            'zero_internal_splits': [bool(u[2 * i] == u[2 * i + 1]) for i in range(3)],
            'checks': checks, 'variations': variations,
            'evidence': '120-digit numerical evaluation; not rigorous interval acceptance'}


def main():
    exact = symbolic_checks()
    mp.mp.dps = 120
    source_data = ROOT / 'profile_upper_mass_flow_checks.json'
    data = json.loads(source_data.read_text(encoding='utf-8'))
    assert data['all_controls_passed']
    cases = []
    for index, example in enumerate(data['valid_rational_examples']):
        for scale in (F(1), F(1, 2)):
            row = copy.deepcopy(example['finite_witness'])
            row['P'] = [[str(F(v) * scale) for v in line] for line in row['P']]
            certificate = strict_check(row)
            assert certificate['exact_equilibrium'] and certificate['strict_transverse_stability']
            cases.append({'name': f'preserved_witness_{index + 1}_density_scale_{scale}',
                          'exact_equilibrium_before_hessian': True,
                          'exact_psd_evidence': 'Strict rational gauge LDL from existing verifier',
                          'control_only_not_new_connectivity_record': True,
                          'evaluation': numerical_bridge(row)})
    opposite_source = ROOT / 'one_opposite_link_data.json'
    opposite_data = json.loads(opposite_source.read_text(encoding='utf-8'))
    opposite_row = {key: opposite_data['geometry'][key] for key in ('x', 'z')}
    opposite_row['P'] = opposite_data['lower_witness']['P']
    for scale in (F(1), F(1, 2)):
        row = copy.deepcopy(opposite_row)
        row['P'] = [[str(F(v) * scale) for v in line] for line in row['P']]
        certificate = strict_check(row)
        assert certificate['exact_equilibrium'] and certificate['strict_transverse_stability']
        evaluation = numerical_bridge(row)
        assert evaluation['nonzero_opposite_links'] == 1
        cases.append({'name': f'preserved_opposite_witness_density_scale_{scale}',
                      'exact_equilibrium_before_hessian': True,
                      'exact_psd_evidence': 'Strict rational gauge LDL from existing verifier',
                      'control_only_not_new_connectivity_record': True,
                      'evaluation': evaluation})
    broken = copy.deepcopy(opposite_row)
    broken['P'][0][2] = broken['P'][2][0] = str(F(broken['P'][0][2]) * F(99, 100))
    try:
        strict_check(broken)
    except AssertionError as error:
        assert str(error) == 'equilibrium', 'The control must fail before stability classification.'
    else:
        raise AssertionError('Broken equilibrium was accepted.')
    degenerate_cases = [
        ('all_internal_edges_zero', (0, 0, 0), (-1, F(1, 2), F(1, 4), F(1, 4), F(-1, 2), 0, 0)),
        ('one_singular_internal_block', (0, 1, 1), (-1, F(1, 2), F(1, 4), F(1, 4), F(-1, 2), F(-1, 2), 0)),
        ('all_internal_splits_zero', (1, 1, 1), (-1, -1, F(1, 4), F(1, 4), F(-1, 2), F(-1, 2), 0)),
    ]
    for name, beta, offsets in degenerate_cases:
        row = degenerate_row(beta, offsets)
        certificate = block_psd_check(row)
        cases.append({'name': name, 'exact_equilibrium_before_hessian': True,
                      'exact_psd_evidence': certificate,
                      'control_only_below_relevant_degree': True,
                      'evaluation': numerical_bridge(row)})
    source_names = ['auditoria_paso_variacional.md', 'cota_perfil_general.md',
                    'cota_flujos_06934.md', 'cota_minimos_locales_06934.md',
                    'profile_upper_mass_flow_checks.json', 'one_opposite_link_data.json', 'verify_rational_template.py',
                    'profile_upper_certificate_06934-v1.json']
    digest = lambda file: hashlib.sha256(file.read_bytes()).hexdigest()
    report = {'symbolic_exact_checks': exact, 'finite_controls_passed': len(cases),
              'strict_controls': 8, 'degenerate_psd_controls': 3,
              'broken_equilibrium_rejected_before_stability': True,
              'precision_decimal_digits': mp.mp.dps, 'controls': cases,
              'inequalities_proved_by_written_argument_not_numeric_sampling': True,
              'full_continuous_reduction_machine_verified': False,
              'tree_reexecuted': False, 'tree_reconstructed': False,
              'independent_human_review': False,
              'source_sha256': {name: digest(ROOT / name) for name in source_names},
              'verifier_source_sha256': digest(Path(__file__)),
              'scope': 'Signs, factors and finite numerical controls of the written variational bridge. No derivative assumption, no inverse of the original internal block. Does not prove flow positivity, a nonzero limiting variational vector, novelty or the complete asymptotic theorem.'}
    (ROOT / 'variational_bridge_verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'exact_edge_identities': len(exact['edge_residual_identities']),
                      'strict_finite_controls': 8, 'degenerate_psd_controls': 3,
                      'high_precision_checks_passed': True}))


if __name__ == '__main__':
    main()
