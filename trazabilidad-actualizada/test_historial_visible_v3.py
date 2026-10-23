"""Disclosure-boundary and immutable-prefix controls; fixtures stay outside W."""
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import json
import unittest
from exportar_historial_visible_v3 import canonical, extract, snapshot

PARENT = None


def item(kind, **fields):
    return {'type': 'event_msg', 'timestamp': 'fixture',
            'payload': {'type': 'item_completed', 'item': {'type': kind, **fields}}}


class VisibleExportTests(unittest.TestCase):
    def test_internal_content_never_exported(self):
        fixture = [item('UserMessage', id='u', content=[{'type': 'text', 'text': 'human request'}]),
                   item('AgentMessage', id='a', phase='commentary', content=[{'type': 'Text', 'text': 'visible answer'}]),
                   item('AgentMessage', id='b', phase='analysis', content=[{'type': 'Text', 'text': 'EXCLUDED_CANARY'}]),
                   item('Reasoning', text='EXCLUDED_CANARY'),
                   item('ContextCompaction', summary='EXCLUDED_CANARY'),
                   {'type': 'session_meta', 'payload': {'instructions': 'EXCLUDED_CANARY'}},
                   {'type': 'response_item', 'payload': {'type': 'message', 'role': 'developer',
                     'content': [{'text': 'EXCLUDED_CANARY'}]}}]
        result = extract(enumerate(fixture, 1))
        self.assertEqual([m['text'] for m in result['messages']], ['human request', 'visible answer'])
        self.assertNotIn(b'EXCLUDED_CANARY', canonical(result))

    def test_automatic_continuations_excluded_even_as_user(self):
        fixture = [item('UserMessage', id='u', content=[{'type': 'text',
                    'text': '<codex_internal_context>EXCLUDED_CANARY</codex_internal_context>'}])]
        result = extract(enumerate(fixture, 1))
        self.assertFalse(result['messages'])
        self.assertNotIn(b'EXCLUDED_CANARY', canonical(result))

    def test_neither_tool_inputs_nor_outputs_exported(self):
        fixture = [item('CommandExecution', id='c', command=['EXCLUDED_CANARY'],
                        aggregated_output='EXCLUDED_CANARY', status='completed', exit_code=0),
                   item('McpToolCall', id='m', server='fixture', tool='read',
                        arguments={'text': 'EXCLUDED_CANARY'}, result={'body': 'EXCLUDED_CANARY'}),
                   {'type': 'response_item', 'payload': {'type': 'custom_tool_call', 'name': 'exec',
                       'call_id': 'a', 'input': 'EXCLUDED_CANARY'}},
                   {'type': 'response_item', 'payload': {'type': 'custom_tool_call_output',
                       'call_id': 'a', 'output': 'EXCLUDED_CANARY'}}]
        result = extract(enumerate(fixture, 1))
        self.assertNotIn(b'EXCLUDED_CANARY', canonical(result))
        self.assertNotIn('calls', result)
        self.assertNotIn('outputs', result)

    def test_project_context_excluded(self):
        text = '# AGENTS.md instructions\n<INSTRUCTIONS>user rule</INSTRUCTIONS>\n<environment_context>EXCLUDED_CANARY</environment_context>'
        fixture = [{'type': 'response_item', 'payload': {'type': 'message', 'role': 'user',
                     'content': [{'text': text}]}}, item('UserMessage', id='u', content=[{'type': 'text', 'text': text}])]
        result = extract(enumerate(fixture, 1))
        self.assertNotIn('contexts', result)
        self.assertNotIn(b'EXCLUDED_CANARY', canonical(result))
        self.assertFalse(result['messages'])

    def test_duplicates_removed_revisions_preserved(self):
        def answer(text):
            return item('AgentMessage', id='a', phase='final_answer', content=[{'type': 'Text', 'text': text}])
        result = extract(enumerate([answer('first'), answer('first'), answer('revised')], 1))
        self.assertEqual([m['revision'] for m in result['messages']], [1, 2])
        self.assertEqual([m['text'] for m in result['messages']], ['first', 'revised'])

    def test_nontext_visible_blocks_flagged_without_body(self):
        fixture = [item('AgentMessage', id='a', phase='final_answer', content=[{'type': 'Image', 'data': 'EXCLUDED_CANARY'}])]
        result = extract(enumerate(fixture, 1))
        self.assertEqual(result['unsupported_visible_blocks'], {'Image': 1})
        self.assertNotIn(b'EXCLUDED_CANARY', canonical(result))

    def test_form_retains_only_visible_question_and_answer(self):
        text = '<send_user_message_question_reply>' + json.dumps([
            {'questionItemId': 'EXCLUDED_CANARY', 'question': 'Visible question?', 'answer': 'Visible answer'}
        ]) + '</send_user_message_question_reply>'
        fixture = [item('UserMessage', id='u', content=[{'type': 'text', 'text': text}])]
        result = extract(enumerate(fixture, 1))
        self.assertEqual(result['messages'][0]['text'], 'Pregunta: Visible question?\n\nRespuesta: Visible answer')
        self.assertNotIn(b'EXCLUDED_CANARY', canonical(result))

    def test_boundary_stops_at_completed_turn(self):
        fixture = [{'type': 'session_meta', 'payload': {'id': 'fixture-thread'}},
                   {'type': 'event_msg', 'timestamp': 'complete', 'payload': {'type': 'task_complete'}},
                   item('AgentMessage', id='a', phase='commentary', content=[{'type': 'Text', 'text': 'active'}])]
        with TemporaryDirectory(prefix='history-fixture-', dir=PARENT) as folder:
            source = Path(folder) / 'fixture.jsonl'
            source.write_bytes(b''.join(canonical(r) + b'\n' for r in fixture))
            boundary = snapshot(source, 'fixture-thread')
            self.assertEqual(boundary['source_lines'], 2)
            self.assertEqual(boundary, snapshot(source, 'fixture-thread', boundary['cutoff_bytes']))
            with self.assertRaisesRegex(AssertionError, 'completed turn'):
                snapshot(source, 'fixture-thread', source.stat().st_size)
            with self.assertRaisesRegex(AssertionError, 'Unrelated'):
                snapshot(source, 'another-thread')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--temp-parent', type=Path, required=True)
    args = parser.parse_args()
    PARENT = args.temp_parent.resolve()
    assert PARENT.is_dir() and not PARENT.is_symlink()
    assert not PARENT.is_relative_to(Path.home() / 'W')
    assert 'drive' not in str(PARENT).lower()
    unittest.main(argv=['visible-export-controls'], verbosity=1)
