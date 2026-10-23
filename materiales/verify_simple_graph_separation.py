"""Exact existence certificate for the finite simple-graph separation.

This is an application of O'Keeffe v1 Lemma 2 followed by completion of
equal-phase clusters. No shift sets or graph edges are selected or enumerated.
The universal competing-class bound uses the averaging lemma proved in
separacion_grafos_simples.md, and does not require equitable partitions.
"""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
from copy import deepcopy
import hashlib,json,argparse
from verify_rational_template import check as strict_check
from verify_fixed_geometry import check as dual_check

ROOT=Path(__file__).resolve().parent
SHEETS=[0,0,1,1,2,2,3]
SOURCES={'restricted':'fixed_geometry_005_tight_data.json',
         'one_opposite':'one_opposite_link_data.json'}

def load(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))
def digest(name):return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
def bare(row):return {key:deepcopy(row[key]) for key in ['x','z','P']}

def source_rows():return {label:bare(load(name)['lower_witness']) for label,name in SOURCES.items()}

def build_plan():
    rows=source_rows()
    D=lcm(2,*[F(v).denominator for row in rows.values() for v in row['x']],
          *[F(v).denominator for row in rows.values() for a in row['P'] for v in a])
    n=D*D
    plan={'D':str(D),'n':str(n),'cases':{},
          'graph_edges_enumerated':False,'shift_sets_selected':False,
          'method':'Existence from O Keeffe v1 Lemma 2, then add missing edges within each equal-phase cluster.'}
    for name,row in rows.items():
        x=list(map(F,row['x']));P=[[F(v) for v in a] for a in row['P']]
        mu=min(sum(P[i][j]*x[j] for j in range(7)) for i in range(7))
        thinned=bare(row)
        for i in range(7):thinned['P'][i][i]=str(1-F(1,D))
        thinned['realization_denominator']=str(D)
        delta=n*mu-1
        assert delta.denominator==1
        plan['cases'][name]={'diagonal_thinned_template':thinned,
                             'completed_minimum_degree':str(delta.numerator),
                             'normalizations':{'delta_over_n':str(delta/n),
                                               'proposal':str((delta+1)/n),
                                               'delta_over_n_minus_1':str(delta/(n-1))}}
    return plan

def verify(plan):
    rows=source_rows();a,b=rows.values()
    assert a['x']==b['x'] and a['z']==b['z'],'same masses and phases'
    assert len(set(tuple(p) for p in a['z']))==7,'distinct source phases'
    D=int(plan['D']);n=int(plan['n'])
    assert D>=2 and D%2==0,'even realization denominator'
    assert n==D*D,'graph order'
    assert set(plan['cases'])==set(rows),'case labels'
    assert plan['graph_edges_enumerated'] is False and plan['shift_sets_selected'] is False,'existence claim boundary'
    x=list(map(F,a['x']))
    assert sum(x)==1 and all(v>0 for v in x),'masses'
    assert all((v*D).denominator==1 for v in x),'mass denominator'
    sizes=[int(v*n) for v in x]
    assert sum(sizes)==n and all(F(s,n)==v for s,v in zip(sizes,x)),'integer cluster sizes'
    upper=F(dual_check(load(SOURCES['restricted']))['exact_upper'])
    # For every competing simple graph, (delta+1)/n <= U by averaging.
    upper_degree=(n*upper-1).__floor__()
    upper_proposal=F(upper_degree+1,n)
    upper_paper=F(upper_degree,n-1)
    outputs={}
    for name,original in rows.items():
        original_report=strict_check(original)
        P=[[F(v) for v in row] for row in original['P']]
        assert all((v*D).denominator==1 for row in P for v in row),'density denominator'
        for i in range(7):
            for j in range(7):
                if SHEETS[i]==SHEETS[j]:assert P[i][j]==1,'complete leaf pattern'
                if (SHEETS[i]-SHEETS[j])%4==2:
                    expected=name=='one_opposite' and {i,j}=={1,4}
                    assert (P[i][j]>0)==expected,'opposite support'
        case=plan['cases'][name];thin=case['diagonal_thinned_template']
        assert thin['x']==original['x'] and thin['z']==original['z'],'unchanged realization geometry'
        assert int(thin['realization_denominator'])==D,'declared realization denominator'
        for i in range(7):
            for j in range(7):
                assert F(thin['P'][i][j])==(1-F(1,D) if i==j else P[i][j]),'only diagonal thinning'
        exact=strict_check(thin)
        assert exact['realization']['condition_checked_exactly'],'realization condition'
        assert int(exact['realization']['n'])==n,'common realized order'
        # Lemma 2 makes every cluster block regular. Completion adds X_i-1
        # neighbors to each vertex in cluster i, and only equal-phase edges.
        additions=[int(v*D)-1 for v in x]
        assert all(v>=0 for v in additions),'nonnegative clique completion'
        before=[n*F(v) for v in exact['degrees']]
        after=[before[i]+additions[i] for i in range(7)]
        wanted=[n*F(v)-1 for v in original_report['degrees']]
        assert all(v.denominator==1 for v in before+after),'integer realized degrees'
        assert after==wanted,'clique completion degree identity'
        delta=min(after).numerator
        assert delta==int(case['completed_minimum_degree']),'declared minimum degree'
        assert 0<=delta<n,'simple graph degree range'
        norms={'delta_over_n':F(delta,n),'proposal':F(delta+1,n),
               'delta_over_n_minus_1':F(delta,n-1)}
        assert {k:F(v) for k,v in case['normalizations'].items()}==norms,'normalization conversion'
        assert norms['proposal']==F(original_report['mu']),'proposal equals original template degree'
        assert norms['delta_over_n']==norms['proposal']-F(1,n),'self exclusion correction'
        outputs[name]={'completed_minimum_degree':str(delta),
                       'vertices_per_cluster':[str(v) for v in sizes],
                       'added_neighbors_per_vertex_by_cluster':[str(v) for v in additions],
                       'degrees_after_completion':[str(v.numerator) for v in after],
                       'normalizations':{k:str(v) for k,v in norms.items()},
                       'realization_condition':exact['realization'],
                       'stability':'Strict by the cited realization lemma; added edges join identical phases and add a PSD Laplacian, preserving equilibrium and transverse strictness.'}
    delta_plus=int(outputs['one_opposite']['completed_minimum_degree'])
    gap=F(delta_plus-upper_degree,n)
    paper_gap=F(delta_plus-upper_degree,n-1)
    assert int(outputs['restricted']['completed_minimum_degree'])<=upper_degree,'restricted witness below class upper'
    assert gap>F(199,10**9) and paper_gap>F(199,10**9),'simple graph class separation'
    assert F(outputs['one_opposite']['normalizations']['proposal'])<F(6929,10000),'no record claim'
    return {'passed':True,'model':'Homogeneous Kuramoto on simple undirected graphs, no self-loops.',
            'existence_only':True,'graph_edges_enumerated':False,'shift_sets_selected':False,
            'graph_order':str(n),'graph_order_digits':len(str(n)),'common_denominator':str(D),
            'same_masses_phases_and_order':True,'cases':outputs,
            'restricted_class':'All graphs of this order with the stated seven phase classes and masses, complete within each leaf, opposite leaves unlinked, equilibrium and full Hessian PSD. Arbitrary adjacent blocks; no equitable-partition assumption.',
            'template_upper':str(upper),'restricted_integer_degree_upper':str(upper_degree),
            'restricted_proposal_upper':str(upper_proposal),
            'restricted_paper_upper':str(upper_paper),
            'proposal_and_delta_over_n_gap_lower':str(gap),
            'paper_gap_lower':str(paper_gap),'gap_approx':float(gap),
            'source_sha256':{file:digest(file) for file in SOURCES.values()},
            'checker_dependencies_sha256':{file:digest(file) for file in ['verify_rational_template.py','verify_fixed_geometry.py']},
            'proof_dependency':'separacion_grafos_simples.md: averaging plus clique completion; graph existence from O Keeffe v1 Lemma 2.',
            'limitations':'No new general connectivity bound, no selected shift sets or explicit edge list, no independent review or confirmed novelty.'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--plan');args=parser.parse_args()
    plan=load(args.plan) if args.plan else build_plan()
    report=verify(plan);report['verifier_sha256']=digest(Path(__file__).name)
    (ROOT/'simple_graph_separation_plan.json').write_text(json.dumps(plan,indent=2),encoding='utf-8',newline='\n')
    (ROOT/'simple_graph_separation_certificate.json').write_text(json.dumps(report,indent=2),encoding='utf-8',newline='\n')
    print(json.dumps({k:report[k] for k in ['passed','graph_order_digits','gap_approx','existence_only']},indent=2))

if __name__=='__main__':main()
