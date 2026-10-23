"""Controls for the graph existence certificate and the averaging identities."""
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
import hashlib,json
from verify_simple_graph_separation import build_plan,verify,load,SHEETS

ROOT=Path(__file__).resolve().parent

def graph_quantities(labels,edges,z):
    n=len(labels);R=[F(0) for _ in labels]
    H=[[F(0) for _ in labels] for _ in labels]
    degrees=[0]*n
    for u,v in edges:
        i,j=labels[u],labels[v]
        C=sum(z[i][k]*z[j][k] for k in range(2))
        S=z[i][1]*z[j][0]-z[i][0]*z[j][1]
        R[u]+=S;R[v]-=S
        H[u][u]+=C;H[v][v]+=C;H[u][v]-=C;H[v][u]-=C
        degrees[u]+=1;degrees[v]+=1
    return R,H,degrees

def averaging_control():
    z=[[F(v) for v in a] for a in load('one_opposite_link_data.json')['geometry']['z']]
    labels=[i for i in range(7) for _ in range(2)];n=len(labels)
    edges={(u,v) for u in range(n) for v in range(u+1,n) if SHEETS[labels[u]]==SHEETS[labels[v]]}
    edges.update([(0,4),(1,5),(4,8),(5,9),(13,0),(13,1)])
    edges={tuple(sorted(e)) for e in edges}
    R,H,degrees=graph_quantities(labels,edges,z)
    blocks=[[v for v in range(n) if labels[v]==i] for i in range(7)]
    counts=[[sum(tuple(sorted((u,v))) in edges for u in blocks[i] for v in blocks[j])
             if i!=j else 0 for j in range(7)] for i in range(7)]
    P=[[F(counts[i][j],4) if i!=j else F(1) for j in range(7)] for i in range(7)]
    x=[F(1,7)]*7
    small_R=[sum(x[j]*P[i][j]*(z[i][1]*z[j][0]-z[i][0]*z[j][1]) for j in range(7)) for i in range(7)]
    assert all(small_R[i]==sum(R[v] for v in blocks[i])/(2*n) for i in range(7)),'aggregated balance identity'
    small_H=[[-x[i]*x[j]*P[i][j]*sum(z[i][k]*z[j][k] for k in range(2)) if i!=j else F(0)
              for j in range(7)] for i in range(7)]
    for i in range(7):small_H[i][i]=-sum(small_H[i])
    assert all(sum(H[u][v] for u in blocks[i] for v in blocks[j])==n*n*small_H[i][j]
               for i in range(7) for j in range(7)),'aggregated Hessian identity'
    d=[sum(P[i][j]*x[j] for j in range(7)) for i in range(7)]
    assert all(d[i]==(F(sum(degrees[v] for v in blocks[i]),2)+1)/n for i in range(7)),'average degree plus one'
    assert min(d)>F(min(degrees)+1,n),'non-equitable strict inequality control'
    assert degrees[12]!=degrees[13] and any(R),'non-equilibrium non-equitable toy'
    return {'test':'averaging of a non-equitable 14-vertex graph','passed':True,
            'toy_is_equilibrium':False,'purpose':'Only algebraic identities; no stability or target-connectivity claim.'},labels,edges,z

def completion_control(labels,edges,z):
    removed={(2*i,2*i+1) for i in range(7)}
    before_edges=edges-removed
    before_R,before_H,_=graph_quantities(labels,before_edges,z)
    after_R,after_H,_=graph_quantities(labels,edges,z)
    assert before_R==after_R,'equal-phase edge addition preserves gradient'
    L=[[0]*len(labels) for _ in labels]
    for u,v in removed:
        assert labels[u]==labels[v]
        L[u][u]+=1;L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
    assert all(after_H[u][v]-before_H[u][v]==L[u][v] for u in range(len(labels)) for v in range(len(labels))),'completion Laplacian sum of rank-one squares'
    return {'test':'equal-phase clique completion identity','passed':True,
            'purpose':'Gradient unchanged and Hessian difference equals an explicit sum of PSD edge Laplacians.'}

def main():
    plan=build_plan();report=verify(plan)
    results=[{'test':'exact graph existence and comparison certificate','passed':report['passed']}]
    avg,labels,edges,z=averaging_control();results.extend([avg,completion_control(labels,edges,z)])
    bad_degree=deepcopy(plan);bad_degree['cases']['one_opposite']['completed_minimum_degree']=str(int(bad_degree['cases']['one_opposite']['completed_minimum_degree'])+1)
    bad_normalization=deepcopy(plan)
    bad_normalization['cases']['one_opposite']['normalizations']['proposal']=bad_normalization['cases']['one_opposite']['normalizations']['delta_over_n']
    bad_order=deepcopy(plan);bad_order['n']=str(int(bad_order['n'])+1)
    bad_diagonal=deepcopy(plan);bad_diagonal['cases']['one_opposite']['diagonal_thinned_template']['P'][0][0]='1'
    bad_support=deepcopy(plan);bad_support['cases']['restricted']['diagonal_thinned_template']['P'][0][1]='0'
    for name,data,reason in [
        ('off-by-one minimum degree',bad_degree,'declared minimum degree'),
        ('confused connectivity normalizations',bad_normalization,'normalization conversion'),
        ('wrong graph order',bad_order,'graph order'),
        ('missing diagonal slack',bad_diagonal,'only diagonal thinning'),
        ('changed fixed leaf edge',bad_support,'only diagonal thinning')]:
        try:verify(data)
        except AssertionError as exc:
            assert reason in str(exc),(name,str(exc))
            results.append({'test':name,'passed':True,'rejected_because':str(exc)})
        else:raise AssertionError('Invalid graph plan accepted: '+name)
    output={'passed':all(v['passed'] for v in results),'checks':results,
            'boundary':'Arithmetic and general aggregation/completion identities checked. Target graphs are existential via the cited lemma; no target edges or shifts generated.',
            'source_sha256':{file:hashlib.sha256((ROOT/file).read_bytes()).hexdigest() for file in ['verify_simple_graph_separation.py','simple_graph_separation_checks.py']}}
    (ROOT/'simple_graph_separation_checks.json').write_text(json.dumps(output,indent=2),encoding='utf-8',newline='\n')
    print(json.dumps({'passed':output['passed'],'checks':len(results)},indent=2))

if __name__=='__main__':main()
