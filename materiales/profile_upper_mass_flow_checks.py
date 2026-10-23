"""Exact controls for the coupled flow/mass certificate."""
from pathlib import Path
from fractions import Fraction as F
import copy,hashlib,json
from verify_profile_upper_mass_flow import replay
from profile_upper_mass_flow_interval import impossible
from general_quarter_profile import unequal_profile,analyze,finite
from verify_rational_template import check

ROOT=Path(__file__).resolve().parent
path=ROOT/'profile_upper_certificate_06934-v1.json'
data=json.loads(path.read_text(encoding='utf-8'));valid=replay(data)
rejections=[]
def reject(name,fn):
    try:fn()
    except (AssertionError,KeyError,TypeError) as error:
        rejections.append({'name':name,'reason':str(error),'exception':type(error).__name__})
    else:raise AssertionError('Corruption accepted: '+name)

bad=copy.deepcopy(data);bad['root'][0][1]='2'
reject('root domain changed',lambda:replay(bad))
bad=copy.deepcopy(data);bad['tree']['left']=None
reject('left branch omitted',lambda:replay(bad))
def find(node,kind):
    if node.get('reason')==kind:return node
    if 'dimension' in node:return find(node['left'],kind) or find(node['right'],kind)
    return None
bad=copy.deepcopy(data);find(bad['tree'],'matrix')['weights'][0]='-1'
reject('negative comparison vector',lambda:replay(bad))
bad=copy.deepcopy(data);find(bad['tree'],'bernstein_matrix')['alpha']='2'
reject('nonconvex combination coefficient',lambda:replay(bad))
bad=copy.deepcopy(data);bad['tree']={'reason':'aggregate_cut'}
reject('false aggregate-cut exclusion at root',lambda:replay(bad))
bad=copy.deepcopy(data);bad['tree']={'reason':'mass_flow_sum'}
reject('false mass-flow exclusion at root',lambda:replay(bad))
assert len(rejections)==6

# Three actual rational templates guard against rejecting admissible profiles.
# They are below the known record and are not the numerical relaxation search.
examples=[]
q=F(3,5);rho=F(99,100);w=F(7,5)
for r in [F(19,20),F(1),F(21,20)]:
    profile=unequal_profile(r,q,w,F(3,5),rho)
    leading=analyze(profile,strict=True)
    chi=[rho*(1+q)/(2*r),rho*r*(1+q)/2,rho*(1+q)/(2*r)]
    assert F(2,3)<leading['mu']<F(3467,5000)
    assert impossible([(v,v) for v in chi],leading['mu']) is None
    witness=finite(profile,F(1,10**6));certificate=check(witness)
    examples.append({'r':str(r),'leading_mu':str(leading['mu']),'chi':list(map(str,chi)),
                     'projection_retained':True,'finite_witness':witness,'finite_certificate':certificate})

reference=json.loads((ROOT/'global_optimum_certificate.json').read_text(encoding='utf-8'))
mu0lo=F(reference['connectivity_interval']['lo']);mu0hi=F(reference['connectivity_interval']['hi'])
upper=F(3467,5000)
gaplo,gaphi=upper-mu0hi,upper-mu0lo
assert F(492,10**6)<gaplo<=gaphi<F(493,10**6)
from verify_mass_flow_relaxation import verify as verify_outer_witness
outer_witness=verify_outer_witness()
report={'all_controls_passed':True,'valid_tree':valid,'corruptions_rejected':rejections,
        'valid_rational_examples':examples,'gap_to_reference_interval':[str(gaplo),str(gaphi)],
        'gap_strictly_below':'493/1000000','outer_relaxation_witness':outer_witness,'reference_sha256':hashlib.sha256((ROOT/'global_optimum_certificate.json').read_bytes()).hexdigest(),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'scope':'Exact coverage replay, six proof-object corruptions rejected, three strict finite witnesses retained. Reference interval is from the previous global algebraic proof. No independent human review.'}
(ROOT/'profile_upper_mass_flow_checks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_controls_passed':True,'corruptions_rejected':len(rejections),
                  'strict_finite_examples_retained':len(examples),'gap_below':.000493}))
