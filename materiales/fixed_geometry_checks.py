"""Replay exact primal/dual evidence and deliberately corrupted certificates."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import json,hashlib
from verify_fixed_geometry import check

ROOT=Path(__file__).resolve().parent


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    rows=[]
    for prefix in ['fixed_geometry_005','fixed_geometry_005_tight','all_density_005','one_opposite_link']:
        path=ROOT/(prefix+'_data.json');data=json.loads(path.read_text(encoding='utf-8'))
        report=check(data)
        unrestricted=data['geometry'].get('density_model')=='all_offdiagonal'
        assert F(report['exact_upper'])<F(688773576 if unrestricted else 688773375,10**9)
        if prefix.endswith('_tight'):
            assert F(report['exact_lower'])>F(68877337398,10**11)
            assert F(report['exact_upper'])<F(68877337417,10**11)
            assert F(report['exact_gap'])<F(1,5*10**9)
            assert F(report['neighborhood']['mass_coordinate_radius'])>=F(1,10**8)
            assert F(report['neighborhood']['exact_upper'])<F(6929,10000)
        rows.append({'name':prefix,'passed':True,'data_sha256':sha(path),
                     'exact_gap':report['exact_gap'],'neighborhood_upper':report['neighborhood']['exact_upper']})
    source=json.loads((ROOT/'fixed_geometry_005_tight_data.json').read_text(encoding='utf-8'))
    for kind,reason in [('PSD','dual PSD: nonpositive pivot'),('weights','degree multipliers'),
                        ('upper','upper bound replay'),('equilibrium','equilibrium'),
                        ('model','density model')]:
        damaged=deepcopy(source)
        if kind=='PSD':damaged['dual']['PSD_multiplier'][0][0]='-1'
        elif kind=='weights':damaged['dual']['degree_weights'][0]='-1'
        elif kind=='upper':damaged['dual']['upper']=str(F(damaged['dual']['upper'])-F(1,10**8))
        elif kind=='model':damaged['geometry']['density_model']='undefined'
        else:
            P=damaged['lower_witness']['P'];P[0][2]=P[2][0]=str(F(P[0][2])-F(1,10**8))
        try:check(damaged)
        except AssertionError as exc:assert str(exc)==reason,(kind,str(exc))
        else:raise AssertionError('Corrupted '+kind+' certificate accepted')
        rows.append({'name':'corrupted_'+kind,'passed':True,'expected_rejection':reason})
    output={'all_passed':True,'checks':rows,'verifier_sha256':sha(ROOT/'verify_fixed_geometry.py'),
            'lower_verifier_sha256':sha(ROOT/'verify_rational_template.py'),
            'runner_sha256':sha(Path(__file__)),'acceptance':'Python standard-library Fractions only'}
    (ROOT/'fixed_geometry_checks.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps({'all_passed':True,'checks':len(rows),'five_corrupted_certificates_rejected':True},indent=2))


if __name__=='__main__':main()
