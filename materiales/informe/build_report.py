"""Compile and rasterize the saved report outside the vault for visual review.

Does not publish a candidate or replace the final PDF. Keep only source and the
reviewed final document in the vault; all compiler output remains under TEMP.
"""
from pathlib import Path
import argparse,hashlib,json,os,re,shutil,subprocess,time
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent
RUNTIME=Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies'


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--temp-parent',required=True)
    parser.add_argument('--resume-first-pass',action='store_true')
    args=parser.parse_args();parent=Path(args.temp_parent).resolve();vault=ROOT.parents[3]
    assert parent.is_dir() and not parent.is_relative_to(vault) and not parent.is_symlink()
    assert 'drive' not in str(parent).lower()
    job=parent/'report'
    if not args.resume_first_pass:job.mkdir(exist_ok=False)
    assert job.resolve().is_relative_to(parent) and not job.is_symlink()
    source=ROOT/'main.tex'
    if args.resume_first_pass:
        assert source.read_bytes()==(job/'main.tex').read_bytes()
        assert (job/'main.pdf').is_file() and 'Output written on' in (job/'main.log').read_text(errors='replace')
    else:shutil.copy2(source,job/'main.tex')
    compiler=Path.home()/'AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe'
    poppler=RUNTIME/'native/poppler/Library/bin/pdftoppm.exe'
    assert compiler.is_file() and poppler.is_file()
    env=dict(os.environ);env['TEXMFOUTPUT']=str(job);env['PYTHONDONTWRITEBYTECODE']='1'
    runs=([{'pass':1,'successful_compiler_log_reused_after_wrapper_timeout':True}]
          if args.resume_first_pass else [])
    for number in ((2,) if args.resume_first_pass else (1,2)):
        started=time.monotonic()
        run=subprocess.run([str(compiler),'--disable-installer','-no-shell-escape','-interaction=nonstopmode',
                            '-halt-on-error',f'-output-directory={job}','main.tex'],cwd=job,env=env,
                           capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
        (job/f'compiler-{number}.txt').write_text(run.stdout+'\n'+run.stderr,encoding='utf-8')
        assert run.returncode==0,(number,run.stdout[-5000:],run.stderr[-1000:])
        runs.append({'pass':number,'exit_code':run.returncode,'seconds':time.monotonic()-started})
    pdf=job/'main.pdf';reader=PdfReader(pdf);log=(job/'main.log').read_text(encoding='utf-8',errors='replace')
    unresolved=bool(re.search(r'undefined|Rerun to get cross-references right',log,re.I))
    overfull=bool(re.search(r'Overfull \\[hv]box',log))
    run=subprocess.run([str(poppler),'-r','120','-png',str(pdf),str(job/'page')],capture_output=True,text=True,timeout=180)
    assert run.returncode==0,(run.stdout,run.stderr)
    images=sorted(job.glob('page-*.png'));assert len(images)==len(reader.pages)
    texts=[page.extract_text() or '' for page in reader.pages]
    text='\n'.join(texts)
    normalized=text.replace(',','.')
    assert '0.6934' in normalized and '1.99' in normalized
    sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    report={'source_sha256':sha(source),'pdf_sha256':sha(pdf),'pages':len(reader.pages),'max_pages':5,
            'unresolved_references':unresolved,'overfull_boxes':overfull,'compiler_runs':runs,
            'page_characters':[len(t) for t in texts],
            'render_sha256':{str(i):sha(p) for i,p in enumerate(images,1)},
            'candidate_path':str(pdf),'render_paths':list(map(str,images)),
            'visual_review':'Pending; candidate not published.',
            'ai_declaration_present':'Declaración de IA' in text,
            'status':'Draft pending independent mathematical and bibliographic review; not submitted'}
    (job/'candidate_validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))


if __name__=='__main__':main()
