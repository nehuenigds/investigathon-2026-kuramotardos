"""Exact controls for principal flow, centers and a nonzero offset direction.

This does not construct or certify finite equilibria for synthetic profiles.
The continuous limiting implication is the written proof in the linked note.
"""
import bootstrap
from bootstrap import ROOT
from pathlib import Path
from fractions import Fraction as F
import copy
import hashlib
import json
import sympy as S
from verify_rational_template import check as finite_check

if not __debug__:
    raise RuntimeError('Run without -O: assertions are required.')

LEAF = (0, 0, 1, 1, 2, 2, 3)
EDGES = ((0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (2, 5),
         (3, 4), (3, 5), (4, 6), (5, 6), (6, 0), (6, 1))


def symbolic_checks():
    total = S.Symbol('T', positive=True)
    fa, fb, fc, ab, bc = S.symbols('fA fB fC edgeAB edgeBC', real=True)
    s = S.symbols('s0:7', real=True)
    conductance = (ab, fa - ab, fb - ab, total - fa - fb + ab,
                   bc, fb - bc, fc - bc, total - fb - fc + bc,
                   fc, total - fc, fa, total - fa)
    outgoing = [sum(a for a, (i, j) in zip(conductance, EDGES) if i == k) for k in range(7)]
    incoming = [sum(a for a, (i, j) in zip(conductance, EDGES) if j == k) for k in range(7)]
    assert all(S.expand(a - b) == 0 for a, b in zip(outgoing, incoming))
    assert [S.expand(v) for v in outgoing] == [fa, total - fa, fb, total - fb, fc, total - fc, total]
    cuts = [sum(a * (s[i] - s[j]) for a, (i, j) in zip(conductance, EDGES) if LEAF[i] == leaf) for leaf in range(4)]
    moments = [sum(outgoing[i] * s[i] for i in range(7) if LEAF[i] == leaf) for leaf in range(4)]
    assert all(S.expand(cuts[i] - moments[i] + moments[(i + 1) % 4]) == 0 for i in range(4))
    assert all(S.diff(cut, parameter) == 0 for cut in cuts for parameter in (ab, bc))
    k = S.symbols('k0:3', real=True)
    reconstructed = []
    for flow, width in zip((fa, fb, fc), k):
        reconstructed.extend((-(1 - flow / total) * width, flow / total * width))
    reconstructed.append(S.Integer(0))
    replace = dict(zip(s, reconstructed))
    assert all(S.expand(moment.subs(replace)) == 0 for moment in moments)
    assert all(S.expand(reconstructed[2 * i + 1] - reconstructed[2 * i] - k[i]) == 0 for i in range(3))
    # T>0 suffices to reconstruct offsets from moments, widths and the anchor.
    # Individual positive margins are additionally needed for chi>0.
    coordinates = S.Matrix(moments[:3] + [s[6]] + [s[2 * i + 1] - s[2 * i] for i in range(3)])
    determinant = S.factor(coordinates.jacobian(s).det())
    assert S.expand(determinant ** 2 - total ** 6) == 0
    jj = S.symbols('J0:3', positive=True)
    original_energy = sum(jj[i] * k[i] ** 2 for i in range(3))
    scaled_energy = sum((jj[i] / total) * k[i] ** 2 for i in range(3))
    assert S.expand(scaled_energy - original_energy / total) == 0
    u = F(3467, 5000)
    assert (2 * u - 1) / 2 == F(967, 5000)
    assert (2 * u - 1) / 8 == F(967, 20000)
    return {'all_assertions_passed': True, 'balanced_transport_node_identities': 7,
            'cut_equals_difference_of_flow_moments': 4,
            'cut_independent_of_transport_covariance': True,
            'offset_reconstruction': True, 'coordinate_map_determinant': str(determinant),
            'energy_scale_identity': True, 'target_constants_exact': True}


def validate_principal(x, a, s, threshold):
    assert len(x) == len(s) == 7 and len(a) == 12, 'dimensions'
    assert all(v > 0 for v in x) and sum(x) == 1, 'positive normalized masses'
    assert all(0 <= value <= x[i] * x[j] for value, (i, j) in zip(a, EDGES)), 'adjacent capacities'
    assert s[6] == 0, 'W anchor'
    assert max(map(abs, s)) == 1, 'offset normalization'
    outgoing = [sum(value for value, (i, j) in zip(a, EDGES) if i == k) for k in range(7)]
    incoming = [sum(value for value, (i, j) in zip(a, EDGES) if j == k) for k in range(7)]
    assert outgoing == incoming, 'principal node balance'
    y = [sum(x[i] for i in range(7) if LEAF[i] == leaf) for leaf in range(4)]
    totals = [sum(outgoing[i] for i in range(7) if LEAF[i] == leaf) for leaf in range(4)]
    assert all(value == totals[0] for value in totals), 'common total flow'
    total = totals[0]
    cuts = [sum(value * (s[i] - s[j]) for value, (i, j) in zip(a, EDGES) if LEAF[i] == leaf) for leaf in range(4)]
    assert cuts == [F(0)] * 4, 'individual principal leaf cuts'
    degree = list(y[LEAF[i]] for i in range(7))
    for value, (i, j) in zip(a, EDGES):
        degree[i] += value / x[i]
        degree[j] += value / x[j]
    assert degree == [y[LEAF[i]] + 2 * outgoing[i] / x[i] for i in range(7)], 'degree identity'
    high_degree = None
    if threshold is not None:
        assert threshold > F(1, 2), 'threshold domain'
        # This check precedes any division by total or any positivity assertion
        # deduced from high degree, including in the zero-flow rejection cases.
        assert min(degree) >= threshold, 'degree threshold'
        for leaf in range(4):
            opposite = (leaf + 2) % 4
            assert all(degree[i] <= 1 - y[leaf] for i in range(7) if LEAF[i] == opposite)
            assert y[leaf] <= 1 - threshold
        c = (2 * threshold - 1) / 2
        margins = [outgoing[i] - c * x[i] for i in range(7)]
        assert min(margins) >= 0
        assert min(outgoing) > 0
        assert total >= c * max(y) >= c / 4 > 0
        assert total * total <= y[0] * y[1] * y[2] * y[3] <= F(1, 256)
        assert total <= F(1, 16)
        high_degree = {'threshold': str(threshold), 'flow_per_mass_lower': str(c),
                       'individual_flow_margins': list(map(str, margins)),
                       'total_flow_lower': str(c / 4), 'total_flow_upper': '1/16'}
    # In the low-degree retained fixture these are checked directly, rather than
    # attributed to a threshold assumption which that fixture does not satisfy.
    assert total > 0 and min(outgoing) > 0, 'positive margins for this control'
    moments = [sum(outgoing[i] * s[i] for i in range(7) if LEAF[i] == leaf) for leaf in range(4)]
    assert all(cuts[i] == moments[i] - moments[(i + 1) % 4] for i in range(4))
    assert moments[3] == total * s[6] == 0
    assert moments == [F(0)] * 4
    fractions = [outgoing[2 * i] / total for i in range(3)]
    widths = [s[2 * i + 1] - s[2 * i] for i in range(3)]
    for i, fraction in enumerate(fractions):
        assert 0 < fraction < 1
        assert s[2 * i] == -(1 - fraction) * widths[i]
        assert s[2 * i + 1] == fraction * widths[i]
    assert 1 <= max(map(abs, widths)) <= 2
    j = [x[2 * i] * x[2 * i + 1] for i in range(3)]
    norm_squared = sum(j[i] * widths[i] ** 2 for i in range(3))
    assert norm_squared >= min(j) > 0
    scaled_norm_squared = sum((j[i] / total) * widths[i] ** 2 for i in range(3))
    assert scaled_norm_squared == norm_squared / total > 0
    chi = [fractions[i] * (1 - fractions[i]) / (j[i] / total) for i in range(3)]
    assert min(chi) > 0
    return {'completed_principal_mu': str(min(degree)), 'total_flow': str(total),
            'individual_flows': list(map(str, outgoing)), 'high_degree_bound': high_degree,
            'zero_adjacent_entries': a.count(F(0)), 'flow_centers': list(map(str, moments)),
            'nonzero_widths': sum(bool(value) for value in widths),
            'max_abs_width': str(max(map(abs, widths))), 'z_norm_squared': str(norm_squared),
            'z_norm_squared_lower': str(min(j)), 'scaled_z_norm_squared': str(scaled_norm_squared),
            'positive_chi': list(map(str, chi)), 'exact_arithmetic': 'fractions only'}


def normalized_profile(profile):
    m = list(map(F, profile['masses']))
    raw_a = list(map(F, profile['adjacent_conductances']))
    offsets = list(map(F, profile['offsets']))
    n = sum(m)
    maximum = max(map(abs, offsets))
    assert maximum > 0
    return ([value / n for value in m], [value / n ** 2 for value in raw_a],
            [value / maximum for value in offsets])


def symmetric_control(mask):
    x = [F(1, 8)] * 6 + [F(1, 4)]
    a = [x[i] * x[j] for i, j in EDGES]
    offsets = [F(0)] * 7
    for i in range(3):
        if mask & (1 << i):
            offsets[2 * i], offsets[2 * i + 1] = F(-1), F(1)
    return x, a, offsets


def sparse_transport_control(mask):
    # Boundary transport of the retained unequal-half family. Only principal
    # balance/cuts/degree are asserted here; no finite stable lift is asserted.
    m = [F(2, 5), F(8, 5), F(8, 5), F(2, 5), F(2, 5), F(8, 5), F(8, 5)]
    raw_a = [F(16, 25), F(0), F(48, 25), F(16, 25),
             F(16, 25), F(48, 25), F(0), F(16, 25),
             F(16, 25), F(64, 25), F(16, 25), F(64, 25)]
    raw_a = [value * F(99, 100) for value in raw_a]
    offsets = []
    for i, fraction in enumerate((F(1, 5), F(4, 5), F(1, 5))):
        width = F(bool(mask & (1 << i)))
        offsets.extend((-(1 - fraction) * width, fraction * width))
    offsets.append(F(0))
    profile = {'masses': list(map(str, m)), 'adjacent_conductances': list(map(str, raw_a)),
               'offsets': list(map(str, offsets))}
    return normalized_profile(profile)


def main():
    exact = symbolic_checks()
    fixture = ROOT / 'general_quarter_profile_checks.json'
    data = json.loads(fixture.read_text(encoding='utf-8'))
    assert data['all_controls_passed']
    retained = []
    for index, example in enumerate(data['examples']):
        # Existing rational coordinates certify an actual finite equilibrium;
        # principal flow identities are checked separately on its limit profile.
        finite = finite_check(example['finite_witness'])
        assert finite['exact_equilibrium'] and finite['strict_transverse_stability']
        x, a, s = normalized_profile(example['profile'])
        mu = F(example['leading_mu'])
        result = validate_principal(x, a, s, mu if mu > F(1, 2) else None)
        assert F(result['completed_principal_mu']) == mu
        retained.append({'fixture_index': index + 1, 'exact_finite_equilibrium_before_ldl': True,
                         'principal_control': result})
    synthetic = []
    for mask in range(1, 8):
        result = validate_principal(*symmetric_control(mask), F(3467, 5000))
        synthetic.append({'kind': 'full principal transport', 'width_support_mask': mask,
                          'finite_equilibrium_or_stability_claimed': False, 'principal_control': result})
    for mask in (1, 3, 7):
        result = validate_principal(*sparse_transport_control(mask), F(2, 3))
        assert result['zero_adjacent_entries'] == 2
        synthetic.append({'kind': 'principal transport with two zero entries', 'width_support_mask': mask,
                          'finite_equilibrium_or_stability_claimed': False, 'principal_control': result})
    rejections = []

    def reject(label, row, reason):
        try:
            validate_principal(*row, F(2, 3))
        except AssertionError as error:
            assert str(error) == reason, (label, str(error))
            rejections.append({'name': label, 'reason': reason})
        else:
            raise AssertionError('Invalid control accepted: ' + label)

    row = copy.deepcopy(symmetric_control(7))
    row[1][0] /= 2
    reject('unbalanced adjacent flow', row, 'principal node balance')
    row = copy.deepcopy(symmetric_control(7))
    row[2][0] += F(1, 8)
    reject('nonzero individual cut', row, 'individual principal leaf cuts')
    row = copy.deepcopy(symmetric_control(7))
    row[2][:] = [F(0)] * 7
    reject('zero normalized offset vector', row, 'offset normalization')
    x, _, _ = symmetric_control(7)
    disconnected = (x, [F(0)] * 12, [F(1), F(1), F(0), F(0), F(0), F(0), F(0)])
    reject('total flow zero at claimed high degree', disconnected, 'degree threshold')
    total = F(1, 64)
    half_zero_a = [F(0), F(0), total / 2, total / 2] + [total / 4] * 4 + [total / 2, total / 2, F(0), total]
    half_zero = (x, half_zero_a, [F(-1)] + [F(0)] * 6)
    reject('one half flow zero at claimed high degree', half_zero, 'degree threshold')
    names = ['auditoria_flujos_centros.md', 'auditoria_paso_variacional.md',
             'cota_perfil_general.md', 'cota_flujos_06934.md',
             'general_quarter_profile_checks.json', 'verify_rational_template.py',
             'profile_upper_certificate_06934-v1.json']
    digest = lambda file: hashlib.sha256(file.read_bytes()).hexdigest()
    report = {'symbolic_checks': exact, 'retained_profiles_with_existing_finite_witnesses': retained,
              'synthetic_partial_condition_controls': synthetic, 'rejections': rejections,
              'retained_finite_equilibria_checked': len(retained),
              'synthetic_principal_controls': len(synthetic), 'rejections_checked': len(rejections),
              'all_rational_controls_passed': True, 'floating_point_used_for_acceptance': False,
              'target_threshold': '3467/5000', 'target_flow_per_mass_lower': '967/5000',
              'target_total_flow_lower': '967/20000', 'universal_total_flow_upper': '1/16',
              'normalization_and_limit_extraction_machine_verified': False,
              'independent_human_review': False, 'tree_reexecuted': False,
              'source_sha256': {name: digest(ROOT / name) for name in names},
              'verifier_source_sha256': digest(Path(__file__)),
              'scope': 'Exact algebra and rational controls of balanced principal flows, cut moments, zero cases and nonzero width direction. Synthetic controls do not claim finite equilibrium or stability and are not verified against all conditions of the asymptotic theorem. Written proof supplies the continuous limiting argument.'}
    (ROOT / 'flow_centers_verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'symbolic_identities_passed': True, 'retained_finite_equilibria': len(retained),
                      'synthetic_principal_controls': len(synthetic), 'rejections': len(rejections),
                      'all_rational_controls_passed': True}))


if __name__ == '__main__':
    main()
