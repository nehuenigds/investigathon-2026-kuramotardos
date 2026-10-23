"""Compile a poster candidate in system TEMP, without publishing it.

Run with Python -B and a --temp-parent created from PowerShell GetTempPath().
Compiler files and all preview images stay outside the vault and Drive.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
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
    parser.add_argument('--source', default='main-asintotica-v1.tex')
    args = parser.parse_args()
    parent = Path(args.temp_parent).resolve()
    vault = ROOT.parents[4]
    assert parent.is_dir() and not parent.is_relative_to(vault)
    assert not parent.is_symlink() and 'drive' not in str(parent).lower()
    source = ROOT / args.source
    assert source.resolve().is_relative_to(ROOT) and source.is_file()
    job = parent / 'poster'
    job.mkdir(exist_ok=False)
    shutil.copy2(source, job / 'main.tex')
    compiler = Path.home() / 'AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe'
    poppler = RUNTIME / 'native/poppler/Library/bin/pdftoppm.exe'
    assert compiler.is_file() and poppler.is_file()
    env = dict(os.environ, TEXMFOUTPUT=str(job), PYTHONDONTWRITEBYTECODE='1')
    runs = []
    for number in (1, 2):
        start = time.monotonic()
        proc = subprocess.run(
            [str(compiler), '--disable-installer', '-no-shell-escape',
             '-interaction=nonstopmode', '-halt-on-error',
             f'-output-directory={job}', 'main.tex'], cwd=job, env=env,
            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=180)
        (job / f'compiler-{number}.txt').write_text(proc.stdout + '\n' + proc.stderr, encoding='utf-8')
        assert proc.returncode == 0, proc.stdout[-5000:]
        runs.append({'pass': number, 'exit_code': proc.returncode,
                     'seconds': time.monotonic() - start})
    pdf = job / 'main.pdf'
    reader = PdfReader(pdf)
    log = (job / 'main.log').read_text(encoding='utf-8', errors='replace')
    text = '\n'.join(p.extract_text() or '' for p in reader.pages)
    normalized = text.replace(',', '.').replace(' ', '')
    assert len(reader.pages) == 1, len(reader.pages)
    page = reader.pages[0]
    width, height = map(float, (page.mediabox.width, page.mediabox.height))
    assert abs(width * 25.4 / 72 - 841) < .02
    assert abs(height * 25.4 / 72 - 594) < .02
    assert 'Los Kuramotardos' in text
    assert '0.6934' in normalized
    assert '7.756' in normalized and '15.511' in normalized
    assert 'Codex' in text and 'revisión' in text
    assert not re.search(r'Overfull \\[hv]box|undefined|Missing character', log, re.I), log[-3000:]
    render = subprocess.run([str(poppler), '-r', '90', '-singlefile', '-png',
                             str(pdf), str(job / 'poster')],
                            capture_output=True, text=True, timeout=180)
    assert render.returncode == 0, render.stderr
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    receipt = {
        'source_sha256': sha(source), 'pdf_sha256': sha(pdf), 'pages': 1,
        'size_mm': [width * 25.4 / 72, height * 25.4 / 72],
        'team_name': 'Los Kuramotardos', 'affiliation_supplied': False,
        'compiler_runs': runs,
        'column_heights_pt': re.findall(r'POSTER-COLUMN-([ABC])-HEIGHT=([0-9.]+)pt', log),
        'overfull_boxes': False, 'unresolved_references': False,
        'candidate_path': str(pdf), 'render_path': str(job / 'poster.png'),
        'render_sha256': sha(job / 'poster.png'),
        'visual_review': 'Pending; candidate not published.',
        'human_mathematical_review': False, 'novelty_verified': False,
        'submitted': False,
    }
    (job / 'candidate_validation.json').write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False))


if __name__ == '__main__':
    main()
