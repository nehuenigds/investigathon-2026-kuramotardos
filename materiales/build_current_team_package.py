"""Freeze the current live-deck source and poster with unchanged v2 math.

Preserves prior packages and authorized message cutoffs. All candidate archives,
extractions and diagnostic files stay in an explicitly supplied system TEMP.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime, timezone
import argparse
import hashlib
import json
import subprocess
import sys
import time
from io import BytesIO
from pypdf import PdfReader
import build_expanded_team_package as previous
from verify_review_package import verify_archive, verify_folder, safe_name

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'paquete-revision-asintotica-actual-equipo-v3.zip'
RECEIPT = ROOT / 'current_team_package_validation.json'
V2 = ROOT / 'paquete-revision-asintotica-ampliada-equipo-v2.zip'
EXTRA = [
    'revision_asintotica_actual_equipo.md', 'build_current_team_package.py',
    'expanded_team_package_validation.json',
    'exposicion/charla-minimos-locales-v2.json',
    'exposicion/populate_local_minima_deck.mjs',
    'exposicion/validate_local_minima_talk.mjs',
    'exposicion/guion-15-minutos-minimos-locales-v2.md',
    'exposicion/charla_minimos_locales_validation.json',
    'exposicion/charla-asintotica-estado4.zip',
    'exposicion/charla-minimos-locales-estado6.zip',
    'exposicion/charla_native_source_validation.json',
    'exposicion/poster/main-minimos-locales-v2.tex',
    'exposicion/poster/output/pdf/poster-minimos-locales-v2.pdf',
    'exposicion/poster/validacion-minimos-locales-v2.json',
]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def check_media(payload):
    live = json.loads(payload['exposicion/charla_minimos_locales_validation.json'])
    native = json.loads(payload['exposicion/charla_native_source_validation.json'])
    assert live['stateVersion'] == native['stateVersion'] == 6
    assert live['slides'] == 15 and live['targetSeconds'] == 900
    for name, expected in live['source_sha256'].items():
        assert sha(payload['exposicion/' + name]) == expected, name
    assert sha(payload['exposicion/charla_minimos_locales_validation.json']) == native['live_visual_review_reference_sha256']
    raw = payload['exposicion/' + native['source_archive']]
    assert sha(raw) == native['archive_sha256']
    with ZipFile(BytesIO(raw)) as archive:
        assert archive.namelist() == [native['member']]
        document = archive.read(native['member'])
        assert sha(document) == native['uncompressed_sha256']
        assert len(document) == native['uncompressed_bytes']
        assert len(json.loads(document)['slides']) == 15
    old = live['previousNativeSource']
    raw = payload['exposicion/' + old['archive']]
    assert sha(raw) == old['archive_sha256']
    with ZipFile(BytesIO(raw)) as archive:
        assert archive.namelist() == [old['member']]
        assert sha(archive.read(old['member'])) == old['uncompressed_sha256']
    poster = json.loads(payload['exposicion/poster/validacion-minimos-locales-v2.json'])
    assert poster['actual_local_minimum_hypothesis'] and poster['visual_review']['completed']
    assert sha(payload[poster['final_source']]) == poster['source_sha256']
    assert sha(payload[poster['final_pdf']]) == poster['pdf_sha256']
    assert sha(payload['exposicion/poster/build_poster.py']) == poster['build_source_sha256']
    for receipt in (live, poster):
        for name, expected in receipt['mathematical_source_sha256'].items():
            assert sha(payload[name]) == expected, name
    pages = {}
    for path, count in [
        ('informe/output/pdf/informe-minimos-locales-v2.pdf', 5),
        ('informe/output/pdf/informe-kuramoto.pdf', 4),
        ('exposicion/poster/output/pdf/poster-minimos-locales-v2.pdf', 1),
        ('exposicion/poster/output/pdf/poster-kuramoto.pdf', 1),
    ]:
        reader = PdfReader(BytesIO(payload[path]))
        assert len(reader.pages) == count
        pages[path] = len(reader.pages)
    return {'current_talk_state': 6, 'talk_slides': 15,
            'native_sources': [4, 6], 'pdf_pages': pages,
            'new_pptx_or_talk_pdf': False, 'powerpoint_opened': False,
            'all_source_hashes_match': True}


def collect():
    payload, source_files, kit_receipt, baseline = previous.collect()
    prior_receipt = json.loads((ROOT / 'expanded_team_package_validation.json').read_text(encoding='utf-8'))
    assert sha(V2.read_bytes()) == prior_receipt['sha256']
    assert prior_receipt['all_checks_passed'] and prior_receipt['commands_passed'] == 16
    assert all(run['exit_code'] == 0 for run in prior_receipt['runs'])
    verify_archive(V2)
    with ZipFile(V2) as archive:
        manifest = json.loads(archive.read('MANIFEST.json'))
        assert set(payload) == set(manifest['files'])
        changed = sorted(name for name in payload if payload[name] != archive.read(name))
        assert changed == ['Bitácora.md', 'checkpoint.md', 'exposicion/notas_defensa.md'], changed
    for name in EXTRA:
        safe_name(name)
        file = ROOT / name
        assert file.is_file() and not file.is_symlink()
        assert name not in payload
        raw = file.read_bytes()
        payload[name] = raw
        source_files[str(file.resolve())] = sha(raw)
    payload['LEEME.md'] = payload['revision_asintotica_actual_equipo.md']
    media = check_media(payload)
    return payload, source_files, baseline, prior_receipt, changed, media


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--temp-parent', required=True, type=Path)
    parser.add_argument('--preflight-only', action='store_true')
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError('Run without -O: assertions are required.')
    parent = args.temp_parent.resolve()
    assert parent.is_dir() and not parent.is_symlink()
    assert not parent.is_relative_to(Path.home() / 'W') and 'drive' not in str(parent).lower()
    assert not OUT.exists() and not RECEIPT.exists(), 'Never overwrite a frozen package'
    payload, sources, baseline, prior, changes, media = collect()
    if args.preflight_only:
        print(json.dumps({'preflight_passed': True, 'payload_files': len(payload),
                          'prior_payload_differences': changes, 'media': media}, ensure_ascii=False))
        return
    job = parent / 'current-review-package'
    job.mkdir(exist_ok=False)
    assert job.resolve().is_relative_to(parent) and not job.is_symlink()
    preserve_names = previous.PRESERVE + [V2.name, 'expanded_team_package_validation.json',
        'exposicion/charla-minimos-locales-v2.json',
        'exposicion/poster/output/pdf/poster-minimos-locales-v2.pdf']
    preserved = {name: sha((ROOT / name).read_bytes()) for name in preserve_names}
    manifest = {
        'version': 2, 'package_revision': 3,
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Current expanded review report, live native deck source, poster, unchanged v2 mathematics and already authorized visible messages. Selected local review materials; not a competition submission.',
        'previous_reproduction_archive': V2.name,
        'previous_reproduction_archive_sha256': prior['sha256'],
        'math_replayed_this_build': False,
        'prior_reproduced_math_bytes_unchanged': True,
        'prior_payload_differences': changes,
        'visible_messages_only': True, 'private_raw_logs_included': False,
        'presentation': {'artifactRef': baseline['artifactRef'], 'stateVersion': 6,
                         'hypothesis': 'Actual local minimum, possibly degenerate',
                         'native_source_included': True, 'pptx_or_pdf_export_included': False},
        'files': {name: {'bytes': len(raw), 'sha256': sha(raw)} for name, raw in sorted(payload.items())},
    }
    payload['MANIFEST.json'] = json.dumps(manifest, ensure_ascii=False, indent=2).encode() + b'\n'
    candidate = job / 'candidate.zip'
    with ZipFile(candidate, 'x', ZIP_DEFLATED, compresslevel=9) as archive:
        for name, raw in sorted(payload.items()):
            archive.writestr(name, raw)
    verify_archive(candidate)
    isolated = job / 'isolated'
    isolated.mkdir(exist_ok=False)
    with ZipFile(candidate) as archive:
        for name in archive.namelist():
            safe_name(name)
            assert (isolated / name).resolve().is_relative_to(isolated)
        archive.extractall(isolated)
    before = verify_folder(isolated)
    started = time.monotonic()
    result = subprocess.run([sys.executable, '-B', '-S', '-X', 'utf8',
        'verify_review_package.py', '--folder', '.'], cwd=isolated,
        capture_output=True, text=True, encoding='utf-8', timeout=120)
    (job / 'integrity.stdout').write_text(result.stdout, encoding='utf-8')
    (job / 'integrity.stderr').write_text(result.stderr, encoding='utf-8')
    assert result.returncode == 0, (result.stdout, result.stderr)
    run = {'script': 'verify_review_package.py', 'arguments': ['--folder', '.'],
           'standard_library_only': True, 'exit_code': 0,
           'seconds': time.monotonic() - started,
           'stdout_sha256': sha(result.stdout.encode()), 'stderr_sha256': sha(result.stderr.encode())}
    after = verify_folder(isolated)
    assert before == after
    assert all(sha(Path(name).read_bytes()) == expected for name, expected in sources.items())
    assert all(sha((ROOT / name).read_bytes()) == expected for name, expected in preserved.items())
    assert payload['LEEME.md'] == payload['revision_asintotica_actual_equipo.md']
    with OUT.open('xb') as stream:
        stream.write(candidate.read_bytes())
    assert OUT.read_bytes() == candidate.read_bytes()
    verify_archive(OUT)
    receipt = {
        'archive': OUT.name, 'bytes': OUT.stat().st_size, 'sha256': sha(OUT.read_bytes()),
        'members': len(payload), 'payload_files': len(manifest['files']),
        'all_checks_passed': True, 'fresh_isolated_commands_passed': 1, 'runs': [run],
        'isolated_payload_unchanged': True, 'source_files_unchanged': True,
        'project_bindings_checked_before_build': len(baseline['source_sha256']),
        'prior_reproduction_archive_sha256': prior['sha256'],
        'prior_reproduction_commands': 16, 'prior_mathematical_commands': 12,
        'prior_payload_changes': changes, 'reproduced_math_bytes_unchanged': True,
        'math_replayed_this_build': False, 'tree_builder_reexecuted': False,
        'search_reexecuted': False, 'media_rebuilt': False, 'media': media,
        'previous_artifacts_unchanged': preserved, 'temporary_parent': str(parent),
        'visible_messages': [159, 20], 'histories_cutoffs_extended': False,
        'private_raw_sessions_or_tool_records_included': False,
        'current_packaging_turn_in_histories': False,
        'team_proof_reviewed': False, 'independent_human_review': False,
        'novelty_verified': False, 'rehearsed': False,
        'submitted': False, 'goal_won_verified': False,
        'builder_sha256': sha(Path(__file__).read_bytes()),
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: receipt[key] for key in ['archive', 'bytes', 'sha256',
        'members', 'fresh_isolated_commands_passed', 'reproduced_math_bytes_unchanged']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
