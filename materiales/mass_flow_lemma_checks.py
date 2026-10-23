"""Check the new necessary inequality on existing strict rational fixtures."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from general_quarter_profile import EDGES,SHEETS,analyze
from verify_rational_template import check
from profile_upper_mass_flow_interval import impossible
from verify_mass_flow_relaxation import verify

ROOT=Path(__file__).resolve().parent


def controls():
    source=ROOT/'general_quarter_profile_checks.json'
    examples=json.loads(source.read_text(encoding='utf-8'))['examples']
    rows=[]
    for example in examples:
        profile=example['profile']
        leading=analyze(profile,strict=True)
        # The finite verifier checks exact equilibrium before positive gauge LDL.
        certificate=check(example['finite_witness'])
        m=list(map(F,profile['masses']));a=list(map(F,profile['adjacent_conductances']))
        out=[sum(v for v,(tail,head) in zip(a,EDGES) if tail==i) for i in range(7)]
        incoming=[sum(v for v,(tail,head) in zip(a,EDGES) if head==i) for i in range(7)]
        assert out==incoming
        masses=[sum(v for v,sheet in zip(m,SHEETS) if sheet==i) for i in range(4)]
        total=out[0]+out[1]
        assert all(sum(out[j] for j in range(7) if SHEETS[j]==i)==total for i in range(4))
        chi=[out[2*i]*out[2*i+1]/(total*m[2*i]*m[2*i+1]) for i in range(3)]
        checks=[]
        for i,neighbors in enumerate(((1,3),(0,2),(1,3))):
            t0=out[2*i]/m[2*i];t1=out[2*i+1]/m[2*i+1]
            for neighbor in neighbors:
                bound=masses[neighbor]
                assert t0<=bound and t1<=bound
                left=bound*total-t0*t1*masses[i]
                right=m[2*i]*t0*(bound-t1)+m[2*i+1]*t1*(bound-t0)
                assert left==right and right>=0
                assert chi[i]*masses[i]<=bound
                checks.append(str(left/total))
        if leading['mu']>F(2,3):
            assert impossible([(v,v) for v in chi],leading['mu']) is None
        rows.append({'leading_mu':str(leading['mu']),'finite_mu':certificate['mu'],
                     'chi':list(map(str,chi)),'six_inequality_margins':checks,
                     'equilibrium_then_strict_stability_reverified':True})
    return {'all_passed':True,'strict_finite_examples':rows,'inequalities_checked':6*len(rows),
            'outer_relaxation_witness':verify(),
            'fixture_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'scope':'Exact fixture controls and one projected rational witness. The written algebra proves the inequality universally. No new Kuramoto record or independent human review.'}


if __name__=='__main__':
    result=controls();result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (ROOT/'mass_flow_lemma_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'all_passed':True,'strict_finite_examples':len(result['strict_finite_examples']),
                      'inequalities_checked':result['inequalities_checked']}))
