"""Compile the expanded review report; all intermediate output stays in TEMP.

Creates a candidate and validation record, never replaces a reviewed PDF.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import time
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
RUNTIME = Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--temp-parent', required=True)
    args = parser.parse_args()
    parent = Path(args.temp_parent).resolve()
    vault = ROOT.parents[3]
    assert parent.is_dir() and not parent.is_relative_to(vault) and not parent.is_symlink()
    assert 'drive' not in str(parent).lower()
    job = parent / 'report-local-minima'
    job.mkdir(exist_ok=False)
    assert job.resolve().is_relative_to(parent) and not job.is_symlink()
    source = ROOT / 'main-minimos-locales-v2.tex'
    shutil.copy2(source, job / 'main.tex')
    compiler = Path.home() / 'AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe'
    poppler = RUNTIME / 'native/poppler/Library/bin/pdftoppm.exe'
    assert compiler.is_file() and poppler.is_file()
    environment = dict(os.environ, TEXMFOUTPUT=str(job), PYTHONDONTWRITEBYTECODE='1')
    runs = []
    for number in (1, 2):
        started = time.monotonic()
        result = subprocess.run([
            str(compiler), '--disable-installer', '-no-shell-escape', '-interaction=nonstopmode',
            '-halt-on-error', f'-output-directory={job}', 'main.tex'],
            cwd=job, env=environment, capture_output=True, text=True,
            encoding='utf-8', errors='replace', timeout=180)
        (job / f'compiler-{number}.txt').write_text(result.stdout + '\n' + result.stderr, encoding='utf-8')
        assert result.returncode == 0, (number, result.stdout[-4000:], result.stderr[-1000:])
        runs.append({'pass': number, 'exit_code': result.returncode, 'seconds': time.monotonic() - started})
    pdf = job / 'main.pdf'
    reader = PdfReader(pdf)
    log = (job / 'main.log').read_text(encoding='utf-8', errors='replace')
    unresolved = bool(re.search(r'undefined|Rerun to get cross-references right', log, re.I))
    overfull = bool(re.search(r'Overfull \\[hv]box', log))
    render = subprocess.run([str(poppler), '-r', '120', '-png', str(pdf), str(job / 'page')],
                            capture_output=True, text=True, timeout=180)
    assert render.returncode == 0, (render.stdout, render.stderr)
    images = sorted(job.glob('page-*.png'))
    assert len(images) == len(reader.pages)
    texts = [page.extract_text() or '' for page in reader.pages]
    text = '\n'.join(texts)
    normalized = text.replace(',', '.')
    compact = re.sub(r'\s+', '', normalized)
    required = ['Los Kuramotardos', 'mínimo local real', '0.6934', '1.99',
                'Lepsveridze', 'Zhang', '159', '20 mensajes', 'Declaración de IA',
                'verify_flow_centers.py', 'verify_variational_bridge.py']
    assert all(re.sub(r'\s+', '', value) in compact for value in required), [value for value in required if re.sub(r'\s+', '', value) not in compact]
    digest = lambda file: hashlib.sha256(file.read_bytes()).hexdigest()
    report = {'source_sha256': digest(source), 'pdf_sha256': digest(pdf),
              'pages': len(reader.pages), 'max_pages': 5, 'within_page_limit': len(reader.pages) <= 5,
              'unresolved_references': unresolved, 'overfull_boxes': overfull,
              'compiler_runs': runs, 'page_characters': list(map(len, texts)),
              'required_content_present': True, 'candidate_path': str(pdf),
              'render_paths': list(map(str, images)),
              'page_render_sha256': {str(i): digest(image) for i, image in enumerate(images, 1)},
              'build_source_sha256': digest(Path(__file__)),
              'visual_review': 'Pending; candidate not copied to the vault.',
              'independent_human_review': False, 'submitted': False,
              'status': 'Expanded local-minimum theorem; draft for team review, not a competition submission.'}
    (job / 'candidate_validation.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()
