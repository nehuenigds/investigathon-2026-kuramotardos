"""Portable schema/integrity checks and optional read-only local source replay."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
from exportar_historial_visible_v3 import PROFILES, extract, jsonl, records, snapshot

ROOT = Path(__file__).resolve().parent
FILES = {'mensajes.jsonl', 'transcripcion.md', 'cobertura.json'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def verify(folder, local_sources=False):
    assert folder.is_dir() and not folder.is_symlink()
    manifest = json.loads((folder / 'MANIFEST.json').read_text(encoding='utf-8'))
    assert set(manifest['files']) == FILES
    assert {p.name for p in folder.iterdir()} == FILES | {'MANIFEST.json'}
    for name, info in manifest['files'].items():
        p = folder / name
        assert p.is_file() and not p.is_symlink()
        raw = p.read_bytes()
        assert len(raw) == info['bytes'] and sha(raw) == info['sha256'], name
    load = lambda name: [json.loads(s) for s in (folder / name).read_text(encoding='utf-8').splitlines()]
    messages = load('mensajes.jsonl')
    c = json.loads((folder / 'cobertura.json').read_text(encoding='utf-8'))
    assert c['version'] == 3 and not c['unsupported_visible_blocks']
    for key in ('tool_inputs_included', 'tool_output_bodies_included', 'reasoning_included',
                'configuration_included', 'raw_session_copied', 'automatic_continuations_included',
                'other_chats_covered', 'current_active_turn_covered', 'tool_indices_included', 'project_context_included'):
        assert c[key] is False, key
    assert c['thread_id'] == PROFILES[c['profile']][0]
    for m in messages:
        assert set(m) == {'source_line', 'timestamp_utc', 'source_item_id', 'role', 'phase', 'revision', 'text'}
        assert m['role'] in ('user', 'assistant')
        assert m['phase'] in (('user',) if m['role'] == 'user' else ('commentary', 'final', 'final_answer'))
        assert '<codex_internal_context' not in m['text']
    assert c['counts']['user_messages'] == sum(m['role'] == 'user' for m in messages)
    assert c['counts']['assistant_commentary'] == sum(m['phase'] == 'commentary' for m in messages)
    assert c['counts']['assistant_final'] == sum(m['phase'] in ('final', 'final_answer') for m in messages)
    assert messages and messages[0]['role'] == 'user'
    assert messages[-1]['role'] == 'assistant' and messages[-1]['phase'] in ('final', 'final_answer')
    assert c['exporter_sha256'] == sha((ROOT / 'exportar_historial_visible_v3.py').read_bytes())
    if local_sources:
        thread, source = PROFILES[c['profile']]
        assert source.is_file(), 'Original local source unavailable; portable integrity checks do not need it'
        b = snapshot(source, thread, c['cutoff_bytes'])
        assert all(c[k] == v for k, v in b.items())
        data = extract(records(source, c['cutoff_bytes']))
        assert not data['unsupported_visible_blocks']
        for name, key in [('mensajes.jsonl', 'messages')]:
            assert jsonl(data[key]) == (folder / name).read_bytes(), name
    return {'export': folder.name, 'cutoff_utc': c['completed_through_utc'],
            'messages': len(messages), 'tool_indices_included': False,
            'schema_and_integrity_passed': True, 'local_source_replayed': local_sources,
            'raw_complete_history': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=Path, required=True)
    parser.add_argument('--local-sources', action='store_true')
    args = parser.parse_args()
    print(json.dumps(verify(args.folder.resolve(), args.local_sources), ensure_ascii=False, indent=2))
