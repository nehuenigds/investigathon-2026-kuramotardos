"""Build or verify the messages-only addendum; never copy raw chat logs."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
import stat
import subprocess
import sys
import time
from verificar_historial_visible_v3 import verify
from exportar_historial_visible_v3 import PROFILES

ROOT = Path(__file__).resolve().parent
TRACES = ['trazabilidad/chat-visible-20261023-v1',
          'trazabilidad/preparacion-visible-20261022-v1']
PARTS = ['mensajes.jsonl', 'transcripcion.md', 'cobertura.json', 'MANIFEST.json']
SUPPORT = ['exportar_historial_visible_v3.py', 'verificar_historial_visible_v3.py',
           'test_historial_visible_v3.py', 'adenda_historial_visible.py',
           'adenda_historial_visible.md']
OUT = ROOT / 'adenda-historial-visible-20261023-v1.zip'
RECEIPT = ROOT / 'visible_history_addendum_validation.json'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def verify_archive(path):
    expected = {folder + '/' + name for folder in TRACES for name in PARTS}
    expected.update(SUPPORT + ['LEEME.md', 'MANIFEST.json'])
    with ZipFile(path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names)) and set(names) == expected
        assert archive.testzip() is None
        for info in archive.infolist():
            assert not info.is_dir() and not stat.S_ISLNK(info.external_attr >> 16)
        manifest = json.loads(archive.read('MANIFEST.json'))
        assert manifest['format'] == 'messages-only-addendum-v1'
        assert manifest['visible_messages_only'] and not manifest['raw_sessions_included']
        assert set(manifest['files']) == expected - {'MANIFEST.json'}
        for name, entry in manifest['files'].items():
            raw = archive.read(name)
            assert len(raw) == entry['bytes'] and sha(raw) == entry['sha256'], name
        assert archive.read('LEEME.md') == archive.read('adenda_historial_visible.md')
        counts = []
        for folder in TRACES:
            inner = json.loads(archive.read(folder + '/MANIFEST.json'))
            assert set(inner['files']) == set(PARTS) - {'MANIFEST.json'}
            for name, entry in inner['files'].items():
                raw = archive.read(folder + '/' + name)
                assert len(raw) == entry['bytes'] and sha(raw) == entry['sha256']
            coverage = json.loads(archive.read(folder + '/cobertura.json'))
            assert coverage['version'] == 3 and not coverage['unsupported_visible_blocks']
            assert coverage['thread_id'] == PROFILES[coverage['profile']][0]
            for key in ['tool_inputs_included', 'tool_output_bodies_included',
                        'tool_indices_included', 'project_context_included',
                        'reasoning_included', 'configuration_included',
                        'raw_session_copied', 'automatic_continuations_included',
                        'other_chats_covered', 'current_active_turn_covered']:
                assert coverage[key] is False, key
            assert coverage['exporter_sha256'] == sha(archive.read('exportar_historial_visible_v3.py'))
            messages = [json.loads(line) for line in archive.read(folder + '/mensajes.jsonl').splitlines()]
            assert messages[0]['role'] == 'user'
            assert messages[-1]['role'] == 'assistant' and messages[-1]['phase'] in ('final', 'final_answer')
            for message in messages:
                assert message['role'] in ('user', 'assistant')
                assert message['phase'] in (('user',) if message['role'] == 'user'
                                           else ('commentary', 'final', 'final_answer'))
                assert '<codex_internal_context' not in message['text']
            assert len(messages) == sum(coverage['counts'].values())
            counts.append(len(messages))
        assert counts == [217, 20]
    return {'integrity_passed': True, 'messages': counts,
            'members': len(names), 'scope': 'Messages-only bytes and schema; not complete raw history or event compliance.'}


def build(parent):
    assert parent.is_dir() and not parent.is_symlink()
    assert not parent.is_relative_to(Path.home() / 'W') and 'drive' not in str(parent).lower()
    assert not OUT.exists() and not RECEIPT.exists()
    baseline = json.loads((ROOT / 'asymptotic_delivery_audit.json').read_text(encoding='utf-8'))
    assert all(sha((ROOT / name).read_bytes()) == expected for name, expected in baseline['source_sha256'].items())
    sources = {}
    payload = {}
    for folder in TRACES:
        verify(ROOT / folder, local_sources=True)
    for name in [folder + '/' + part for folder in TRACES for part in PARTS] + SUPPORT:
        file = ROOT / name
        assert file.is_file() and not file.is_symlink()
        payload[name] = file.read_bytes()
        sources[name] = sha(payload[name])
    payload['LEEME.md'] = payload['adenda_historial_visible.md']
    previous_receipt = json.loads((ROOT / 'current_team_package_validation.json').read_text(encoding='utf-8'))
    package = ROOT / previous_receipt['archive']
    assert sha(package.read_bytes()) == previous_receipt['sha256']
    with ZipFile(package) as archive:
        old = [json.loads(line) for line in archive.read('trazabilidad/chat-visible-20261022-v1/mensajes.jsonl').splitlines()]
        new = [json.loads(line) for line in payload[TRACES[0] + '/mensajes.jsonl'].splitlines()]
        assert len(old) == 159 and len(new) == 217 and new[:len(old)] == old
        for part in PARTS:
            name = TRACES[1] + '/' + part
            assert payload[name] == archive.read(name)
        for name in SUPPORT[:3]:
            assert payload[name] == archive.read(name)
    job = parent / 'visible-history-addendum'
    job.mkdir(exist_ok=False)
    assert job.resolve().is_relative_to(parent) and not job.is_symlink()
    manifest = {'format': 'messages-only-addendum-v1',
                'created_utc': datetime.now(timezone.utc).isoformat(),
                'visible_messages_only': True, 'raw_sessions_included': False,
                'previous_package_sha256': previous_receipt['sha256'],
                'previous_main_messages': 159, 'new_main_messages': 217,
                'new_messages': 58, 'preparation_messages_unchanged': 20,
                'files': {name: {'bytes': len(raw), 'sha256': sha(raw)} for name, raw in sorted(payload.items())}}
    payload['MANIFEST.json'] = json.dumps(manifest, ensure_ascii=False, indent=2).encode() + b'\n'
    candidate = job / 'candidate.zip'
    with ZipFile(candidate, 'x', ZIP_DEFLATED, compresslevel=9) as archive:
        for name, raw in sorted(payload.items()):
            archive.writestr(name, raw)
    verify_archive(candidate)
    isolated = job / 'isolated'
    isolated.mkdir(exist_ok=False)
    with ZipFile(candidate) as archive:
        archive.extractall(isolated)
    commands = [('adenda_historial_visible.py', ['--verify-archive', str(candidate)]),
                *[('verificar_historial_visible_v3.py', ['--folder', folder]) for folder in TRACES],
                ('test_historial_visible_v3.py', ['--temp-parent', str(parent)])]
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1')
    environment.pop('PYTHONPATH', None)
    runs = []
    for index, (script, arguments) in enumerate(commands, 1):
        started = time.monotonic()
        result = subprocess.run([sys.executable, '-B', '-S', '-X', 'utf8', script, *arguments],
            cwd=isolated, env=environment, capture_output=True, text=True, encoding='utf-8', timeout=120)
        (job / f'check-{index}.stdout').write_text(result.stdout, encoding='utf-8')
        (job / f'check-{index}.stderr').write_text(result.stderr, encoding='utf-8')
        assert result.returncode == 0, (script, result.stdout, result.stderr)
        runs.append({'script': script, 'arguments': arguments, 'exit_code': 0,
                     'seconds': time.monotonic() - started,
                     'stdout_sha256': sha(result.stdout.encode()), 'stderr_sha256': sha(result.stderr.encode())})
    isolated_names = {p.relative_to(isolated).as_posix() for p in isolated.rglob('*') if p.is_file()}
    assert isolated_names == set(payload)
    assert all((isolated / name).read_bytes() == raw for name, raw in payload.items())
    assert all(sha((ROOT / name).read_bytes()) == expected for name, expected in sources.items())
    assert sha(package.read_bytes()) == previous_receipt['sha256']
    with OUT.open('xb') as stream:
        stream.write(candidate.read_bytes())
    assert OUT.read_bytes() == candidate.read_bytes()
    verify_archive(OUT)
    receipt = {'archive': OUT.name, 'bytes': OUT.stat().st_size, 'sha256': sha(OUT.read_bytes()),
               'members': len(payload), 'all_checks_passed': True, 'isolated_commands_passed': len(runs),
               'runs': runs, 'privacy_filter_tests_passed': 8, 'local_source_replays_passed': 2,
               'messages': [217, 20], 'previous_main_prefix_preserved': True, 'additional_main_messages': 58,
               'preparation_export_unchanged': True, 'previous_package_unchanged': previous_receipt['sha256'],
               'source_sha256': sources, 'isolated_payload_unchanged': True,
               'temporary_parent': str(parent), 'raw_sessions_or_tool_records_included': False,
               'current_active_turn_covered': False, 'other_chats_covered': False,
               'human_review': False, 'submitted': False, 'goal_won_verified': False}
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return {key: receipt[key] for key in ['archive', 'bytes', 'sha256', 'members', 'messages', 'isolated_commands_passed']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--verify-archive', type=Path)
    group.add_argument('--build-temp-parent', type=Path)
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError('Run without -O: assertions are required.')
    result = verify_archive(args.verify_archive) if args.verify_archive else build(args.build_temp_parent.resolve())
    print(json.dumps(result, ensure_ascii=False))
