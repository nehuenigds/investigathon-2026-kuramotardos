"""Immutable messages-only export of completed visible conversation.

Never copy source logs, reasoning, configuration, compactions, tool arguments,
tool result bodies, tool indices, project context or automatic goal continuations. Restrict sources to the two
identified project chats. Only completed visible conversational items qualify.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
PROFILES = {
    'objetivo': ('01a14d2e-090e-7cd2-9d68-9bb5284f6911', Path.home() /
        '.codex/sessions/2026/10/18/rollout-2026-10-18T01-03-45-01a14d2e-090e-7cd2-9d68-9bb5284f6911.jsonl'),
    'preparacion': ('01a14d0c-ac89-7281-a9a2-f301f5167925', Path.home() /
        '.codex/sessions/2026/10/18/rollout-2026-10-18T00-27-18-01a14d0c-ac89-7281-a9a2-f301f5167925.jsonl'),
}
PHASES = {'commentary', 'final', 'final_answer'}


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def jsonl(rows):
    return b''.join(canonical(row) + b'\n' for row in rows)


def snapshot(source, thread, cutoff=None):
    limit = source.stat().st_size if cutoff is None else cutoff
    assert 0 < limit <= source.stat().st_size, 'Invalid prefix size'
    used = 0
    digest = hashlib.sha256()
    boundary = None
    checked = False
    with source.open('rb') as stream:
        for line in range(1, 10**9):
            if used >= limit:
                break
            raw = stream.readline(limit - used)
            if not raw:
                break
            used += len(raw)
            digest.update(raw)
            try:
                record = json.loads(raw)
            except json.JSONDecodeError:
                assert cutoff is None and used == limit, 'Malformed pinned prefix'
                break
            payload = record.get('payload', {})
            if record.get('type') == 'session_meta':
                assert payload.get('id', payload.get('session_id')) == thread, 'Unrelated chat source'
                checked = True
            if record.get('type') == 'event_msg' and payload.get('type') == 'task_complete':
                boundary = {'cutoff_bytes': used, 'source_lines': line,
                            'source_prefix_sha256': digest.hexdigest(),
                            'completed_through_utc': record.get('timestamp')}
    assert checked and boundary, 'No verified completed turn'
    if cutoff is not None:
        assert boundary['cutoff_bytes'] == cutoff, 'Prefix must end at a completed turn'
    return boundary


def records(source, cutoff):
    with source.open('rb') as stream:
        remaining = cutoff
        line = 0
        while remaining:
            raw = stream.readline(remaining)
            assert raw, 'Short pinned prefix'
            remaining -= len(raw)
            line += 1
            yield line, json.loads(raw)


def extract(rows):
    messages = []
    seen = set()
    revisions = Counter()
    excluded = Counter()
    unsupported = Counter()
    for line, record in rows:
        if record.get('type') != 'event_msg':
            continue
        payload = record.get('payload', {})
        if payload.get('type') != 'item_completed':
            continue
        item = payload.get('item', {})
        kind = item.get('type')
        if kind not in ('UserMessage', 'AgentMessage'):
            continue
        phase = item.get('phase', '')
        if kind == 'AgentMessage' and phase not in PHASES:
            excluded['nonvisible_agent_message'] += 1
            continue
        parts = []
        for block in item.get('content', []):
            if block.get('type') in ('text', 'Text') and isinstance(block.get('text'), str):
                parts.append(block['text'])
            else:
                unsupported[str(block.get('type', 'unknown'))] += 1
        if not parts:
            continue
        text = '\n'.join(parts)
        if '<codex_internal_context' in text or text.startswith('# AGENTS.md instructions'):
            excluded['automatic_or_project_context'] += 1
            continue
        if kind == 'UserMessage':
            text = readable(text)
        ident = str(item.get('id', ''))
        assert ident, 'Missing visible item identifier'
        key = (kind, ident, sha(text.encode('utf-8')))
        if key in seen:
            excluded['duplicate_visible_message'] += 1
            continue
        seen.add(key)
        revisions[(kind, ident)] += 1
        messages.append({'source_line': line, 'timestamp_utc': record.get('timestamp'),
                         'source_item_id': ident, 'role': 'user' if kind == 'UserMessage' else 'assistant',
                         'phase': 'user' if kind == 'UserMessage' else phase,
                         'revision': revisions[(kind, ident)], 'text': text})
    return {'messages': messages, 'excluded_counts': dict(excluded),
            'unsupported_visible_blocks': dict(unsupported)}


def readable(text):
    marker = '<send_user_message_question_reply>'
    if text.startswith(marker):
        rows = json.loads(text.split(marker, 1)[1].split('</send_user_message_question_reply>', 1)[0])
        return '\n\n'.join('Pregunta: ' + row['question'] + '\n\nRespuesta: ' + row['answer'] for row in rows)
    return text


def export(profile, out, cutoff=None):
    thread, source = PROFILES[profile]
    boundary = snapshot(source, thread, cutoff)
    data = extract(records(source, boundary['cutoff_bytes']))
    assert not data['unsupported_visible_blocks'], 'Unsupported visible content; do not claim complete text coverage'
    assert data['messages'] and data['messages'][0]['role'] == 'user'
    if profile == 'objetivo':
        assert data['messages'][0]['text'].strip() == '/goal gana el invetigathon'
    else:
        assert 'preparame un proyecto con todo esto.' in data['messages'][0]['text']
    assert data['messages'][-1]['role'] == 'assistant' and data['messages'][-1]['phase'] in ('final', 'final_answer')
    assert out.resolve().is_relative_to((ROOT / 'trazabilidad').resolve())
    assert not out.exists(), 'Frozen export already exists'
    counts = {'user_messages': sum(m['role'] == 'user' for m in data['messages']),
              'assistant_commentary': sum(m['phase'] == 'commentary' for m in data['messages']),
              'assistant_final': sum(m['phase'] in ('final', 'final_answer') for m in data['messages'])}
    coverage = {'version': 3, 'profile': profile, 'thread_id': thread, **boundary,
                'created_utc': datetime.now(timezone.utc).isoformat(), 'counts': counts,
                'source_basename': source.name, 'exporter_sha256': sha(Path(__file__).read_bytes()),
                'visible_text_coverage': 'All completed visible conversational text in this pinned prefix, excluding identical repeats and automatic/project context. Form replies normalized to visible question and answer; no tool indices.',
                'tool_inputs_included': False, 'tool_output_bodies_included': False,
                'tool_indices_included': False, 'project_context_included': False,
                'reasoning_included': False, 'configuration_included': False,
                'raw_session_copied': False, 'automatic_continuations_included': False,
                'other_chats_covered': False, 'current_active_turn_covered': False,
                'excluded_counts': data['excluded_counts'],
                'unsupported_visible_blocks': data['unsupported_visible_blocks']}
    text = '# Historial visible: ' + profile + '\n\nCorte de turno completo: ' + str(boundary['completed_through_utc'])
    text += '. Texto visible completado; respuestas de formulario legibles. Solo mensajes visibles; sin entradas, resultados o índices de herramientas ni contexto del proyecto.\n\n'
    text += '\n\n'.join('## ' + str(m['timestamp_utc']) + ' — ' + ('Usuario' if m['role'] == 'user' else 'Codex (' + m['phase'] + ')') + '\n\n' + m['text'] for m in data['messages']) + '\n'
    payload = {'mensajes.jsonl': jsonl(data['messages']),
               'transcripcion.md': text.encode('utf-8'), 'cobertura.json': canonical(coverage) + b'\n'}
    # Verify the pinned prefix before committing any durable export files.
    assert snapshot(source, thread, boundary['cutoff_bytes']) == boundary, 'Source prefix changed'
    out.mkdir(parents=True, exist_ok=False)
    for name, raw in payload.items():
        (out / name).write_bytes(raw)
    manifest = {'files': {name: {'bytes': len(raw), 'sha256': sha(raw)} for name, raw in sorted(payload.items())}}
    (out / 'MANIFEST.json').write_bytes(canonical(manifest) + b'\n')
    return coverage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', choices=PROFILES, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--cutoff-bytes', type=int)
    args = parser.parse_args()
    c = export(args.profile, args.out, args.cutoff_bytes)
    print(json.dumps({'cutoff_utc': c['completed_through_utc'], 'counts': c['counts'],
                      'tool_inputs_included': False, 'tool_output_bodies_included': False,
                'tool_indices_included': False, 'project_context_included': False,
                      'raw_session_copied': False}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
