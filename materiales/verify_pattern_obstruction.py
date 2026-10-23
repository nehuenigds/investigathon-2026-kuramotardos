"""Exact separation: one opposite link beats every empty-opposite template
at the specified identical masses and rational circle coordinates.
"""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import json,hashlib
from verify_fixed_geometry import check

ROOT=Path(__file__).resolve().parent


def main():
    names=['fixed_geometry_005_tight_data.json','one_opposite_link_data.json']
    restricted,enlarged=[json.loads((ROOT/name).read_text(encoding='utf-8')) for name in names]
    for key in ['x','z','sheets']:
        assert restricted['geometry'][key]==enlarged['geometry'][key],'comparison geometry'
    base=check(restricted);better=check(enlarged)
    sheets=enlarged['geometry']['sheets'];P=[list(map(F,a)) for a in enlarged['lower_witness']['P']]
    for i in range(len(P)):
        for j in range(len(P)):
            if sheets[i]==sheets[j]:assert P[i][j]==1,'same-sheet condition'
            elif (sheets[i]-sheets[j])%4==2:
                assert (P[i][j]>0 if {i,j}=={1,4} else P[i][j]==0),'opposite support'
    improvement=F(better['exact_lower'])-F(base['exact_upper'])
    assert improvement>F(199,10**9)
    assert F(better['exact_lower'])>F(68877357363,10**11)
    assert F(base['exact_upper'])<F(68877337417,10**11)
    assert F(better['exact_upper'])<F(688773576,10**9)
    report={'exact_strict_separation':True,'restricted_exact_upper':base['exact_upper'],
            'one_opposite_exact_lower':better['exact_lower'],'exact_advantage':str(improvement),
            'advantage_approx':float(improvement),'opposite_edge_zero_based':[1,4],
            'opposite_density':str(P[1][4]),'same_sheet_links_complete':True,
            'all_other_opposite_links_absent':True,
            'claim':'At these fixed masses and phases, keeping all opposite densities zero loses connectivity, even after optimizing all adjacent densities.',
            'scope':'Finite weighted templates, not a new bound on general critical connectivity; no contradiction with a result about the zero-splitting limit.',
            'data_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names},
            'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'dual_verifier_sha256':hashlib.sha256((ROOT/'verify_fixed_geometry.py').read_bytes()).hexdigest(),
            'lower_verifier_sha256':hashlib.sha256((ROOT/'verify_rational_template.py').read_bytes()).hexdigest()}
    (ROOT/'pattern_obstruction_certificate.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['exact_strict_separation','advantage_approx','opposite_density','claim','scope']},indent=2))


if __name__=='__main__':main()
