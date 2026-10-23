"""Freeze the expanded report, proofs and authorized exports; replay in TEMP.

Only validated final ZIP and receipt are saved in the notebook. This builder
never reads raw conversation sessions or expands a visible-history cutoff.
"""
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime, timezone
import argparse
import ast
import hashlib
import json
import os
import subprocess
import sys
import time
from bootstrap import DEPS
from verify_review_package import verify_archive, verify_folder, safe_name

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'paquete-revision-asintotica-ampliada-equipo-v2.zip'
RECEIPT = ROOT / 'expanded_team_package_validation.json'
EXTRA = [
    'revision_asintotica_ampliada_equipo.md', 'primera-lectura-cota-06934.md', 'checkpoint.md',
    'guion-checkpoint-equipo.md', 'guion-checkpoint-equipo-separacion-v1.md', 'revision_bibliografica.md',
    'profile_upper_mass_flow_kit_validation.json', 'kit-cota-flujos-06934-v1.zip',
    'obstruccion_patron_finito.md', 'separacion_grafos_simples.md', 'patron_principal_limite.md',
    'perfil_general_cuatro_hojas.md', 'enlaces_opuestos_limite.md', 'certificados_racionales.md',
    'informe/main.tex', 'informe/output/pdf/informe-kuramoto.pdf', 'informe/validacion.json',
    'informe/build_report.py', 'informe/main-minimos-locales-v2.tex',
    'informe/output/pdf/informe-minimos-locales-v2.pdf', 'informe/validacion-minimos-locales-v2.json',
    'informe/build_local_minima_report.py',
    'cota_minimos_locales_06934.md', 'auditoria_paso_variacional.md', 'auditoria_flujos_centros.md',
    'verify_quarter_turn_local_minima.py', 'quarter_turn_local_minima_verification.json',
    'verify_variational_bridge.py', 'variational_bridge_verification.json',
    'verify_flow_centers.py', 'flow_centers_verification.json',
    'fixed_geometry_005_data.json', 'fixed_geometry_005_tight_data.json',
    'all_density_005_data.json', 'one_opposite_link_data.json',
    'verify_fixed_geometry.py', 'fixed_geometry_checks.py', 'fixed_geometry_checks.json',
    'verify_pattern_obstruction.py', 'pattern_obstruction_certificate.json',
    'verify_simple_graph_separation.py', 'simple_graph_separation_checks.py',
    'simple_graph_separation_plan.json', 'simple_graph_separation_certificate.json',
    'simple_graph_separation_checks.json',
    'exposicion/charla-asintotica.json', 'exposicion/populate_asymptotic_deck.mjs',
    'exposicion/charla_asintotica_validation.json', 'exposicion/guion-15-minutos.md',
    'exposicion/notas_defensa.md', 'exposicion/notas_defensa-complementos-v1.md',
    'exposicion/assets/portada-conceptual.png', 'exposicion/visual_asset.md',
    'exposicion/poster/main.tex', 'exposicion/poster/main-asintotica-v1.tex',
    'exposicion/poster/build_poster.py', 'exposicion/poster/validacion.json',
    'exposicion/poster/output/pdf/poster-kuramoto.pdf',
    'exportar_historial_visible_v3.py', 'verificar_historial_visible_v3.py', 'test_historial_visible_v3.py',
    'verify_review_package.py', 'build_expanded_team_package.py',
]
TRACES = ('chat-visible-20261022-v1', 'preparacion-visible-20261022-v1')
TRACE_FILES = {'mensajes.jsonl', 'transcripcion.md', 'cobertura.json', 'MANIFEST.json'}
MATH = [
    ('verify_profile_upper_mass_flow.py', True), ('profile_upper_mass_flow_checks.py', True),
    ('mass_flow_lemma_checks.py', True), ('verify_covariance_reduction.py', False),
    ('verify_global_optimum.py', False), ('verify_quarter_turn_local_minima.py', False),
    ('verify_variational_bridge.py', False), ('verify_flow_centers.py', False),
    ('fixed_geometry_checks.py', True), ('verify_pattern_obstruction.py', True),
    ('verify_simple_graph_separation.py', True), ('simple_graph_separation_checks.py', True),
]
PRESERVE = [
    'paquete-revision-asintotica-equipo-v1.zip', 'paquete-revision-perfil-equipo-v1.zip',
    'paquete-revision-grafos-equipo-v1.zip', 'kit-cota-flujos-06934-v1.zip',
    'informe/main.tex', 'informe/output/pdf/informe-kuramoto.pdf',
    'informe/output/pdf/informe-minimos-locales-v2.pdf',
    'exposicion/output/charla-kuramoto-v12.pptx',
    'exposicion/poster/output/pdf/poster-kuramoto.pdf', 'exposicion/charla-asintotica.json',
]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def current_hash(name):
    return sha((ROOT / name).read_bytes())


def collect():
    payload, source_files = {}, {}

    def add(name, source=None):
        safe_name(name)
        file = source or ROOT / name
        assert file.is_file() and not file.is_symlink(), name
        raw = file.read_bytes()
        assert name not in payload or payload[name] == raw, 'Conflicting versions: ' + name
        payload[name] = raw
        source_files[str(file.resolve())] = sha(raw)

    kit_receipt = json.loads((ROOT / 'profile_upper_mass_flow_kit_validation.json').read_text(encoding='utf-8'))
    kit = ROOT / 'kit-cota-flujos-06934-v1.zip'
    assert sha(kit.read_bytes()) == kit_receipt['sha256'] and kit_receipt['all_passed']
    with ZipFile(kit) as archive:
        manifest = json.loads(archive.read('MANIFEST.json'))
        for name, entry in manifest['files'].items():
            assert sha(archive.read(name)) == entry['sha256']
            if name != 'README.md':
                add(name)
                assert payload[name] == archive.read(name), 'Mathematical kit changed: ' + name
    for name in EXTRA:
        add(name)
    add('Bitácora.md', ROOT.parent / 'Bitácora.md')
    for trace in TRACES:
        folder = ROOT / 'trazabilidad' / trace
        assert {file.name for file in folder.iterdir()} == TRACE_FILES
        for filename in sorted(TRACE_FILES):
            add('trazabilidad/' + trace + '/' + filename)
    payload['LEEME.md'] = payload['revision_asintotica_ampliada_equipo.md']

    # Verify the project baseline without putting its broader attachment and
    # inline-explanation inventory in this selected review package.
    baseline = json.loads((ROOT / 'asymptotic_delivery_audit.json').read_text(encoding='utf-8'))
    assert all(current_hash(name) == expected for name, expected in baseline['source_sha256'].items())
    for name, expected in baseline['source_sha256'].items():
        if name in payload:
            assert sha(payload[name]) == expected, name
    # Local import closure: external scientific libraries are declared separately.
    for name, raw in list(payload.items()):
        if not name.endswith('.py'):
            continue
        tree = ast.parse(raw.decode('utf-8-sig'), filename=name)
        for node in ast.walk(tree):
            modules = ([alias.name for alias in node.names] if isinstance(node, ast.Import)
                       else [node.module] if isinstance(node, ast.ImportFrom) and node.module else [])
            for module in modules:
                local = module.split('.')[0] + '.py'
                if (ROOT / local).is_file():
                    assert local in payload, f'Missing local import {local} from {name}'
    for name in ('quarter_turn_local_minima_verification.json', 'variational_bridge_verification.json',
                 'flow_centers_verification.json'):
        for source, expected in json.loads(payload[name])['source_sha256'].items():
            assert source in payload and sha(payload[source]) == expected, (name, source)
    expanded = json.loads(payload['informe/validacion-minimos-locales-v2.json'])
    assert expanded['pages'] == 5 and expanded['independent_human_review'] is False
    assert sha(payload['informe/output/pdf/informe-minimos-locales-v2.pdf']) == expanded['pdf_sha256']
    assert sha(payload['informe/main-minimos-locales-v2.tex']) == expanded['source_sha256']
    assert sha(payload['informe/build_local_minima_report.py']) == expanded['build_source_sha256']
    for name, expected in expanded['mathematical_source_sha256'].items():
        assert name in payload and sha(payload[name]) == expected
    assert {name for name in payload if name.endswith('.jsonl')} == {
        'trazabilidad/' + trace + '/mensajes.jsonl' for trace in TRACES}
    assert not any(PurePosixPath(name).suffix in ('.log', '.aux', '.pyc') for name in payload)
    return payload, source_files, kit_receipt, baseline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--temp-parent', type=Path, required=True)
    parser.add_argument('--preflight-only', action='store_true')
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError('Run without -O: assertions are required.')
    parent = args.temp_parent.resolve()
    assert parent.is_dir() and not parent.is_symlink()
    assert not parent.is_relative_to(Path.home() / 'W') and 'drive' not in str(parent).lower()
    assert not OUT.exists() and not RECEIPT.exists(), 'Never overwrite a frozen package or receipt'
    payload, source_files, kit_receipt, baseline = collect()
    if args.preflight_only:
        print(json.dumps({'preflight_passed': True, 'payload_files': len(payload),
                          'project_bindings_checked': len(baseline['source_sha256']),
                          'math_commands': len(MATH), 'total_commands': 16}))
        return
    job = parent / 'expanded-review-package'
    job.mkdir(exist_ok=False)
    assert job.resolve().is_relative_to(parent) and not job.is_symlink()
    preserved = {name: current_hash(name) for name in PRESERVE}
    manifest = {
        'version': 2, 'created_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Expanded 3467/5000 local-minimum report, written audits, finite complement, graph existence certificates, strict presentation sources and already authorized visible messages. Selected report reproduction, not the complete notebook or full AI history.',
        'mathematical_kit_sha256': kit_receipt['sha256'],
        'visible_messages_only': True, 'private_raw_logs_included': False,
        'presentation': {'artifactRef': baseline['artifactRef'], 'stateVersion': baseline['live_state_version'],
                         'hypothesis': 'Preserved strict version', 'new_export_included': False},
        'files': {name: {'bytes': len(raw), 'sha256': sha(raw)} for name, raw in sorted(payload.items())},
    }
    payload['MANIFEST.json'] = json.dumps(manifest, indent=2, ensure_ascii=False).encode('utf-8') + b'\n'
    candidate = job / 'candidate.zip'
    with ZipFile(candidate, 'x', compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, raw in sorted(payload.items()):
            archive.writestr(name, raw)
    verify_archive(candidate)
    isolated = job / 'replay'
    isolated.mkdir(exist_ok=False)
    with ZipFile(candidate) as archive:
        for name in archive.namelist():
            safe_name(name)
            assert (isolated / name).resolve().is_relative_to(isolated)
        archive.extractall(isolated)
    verify_folder(isolated)
    commands = [('verify_review_package.py', ['--folder', '.'], True)]
    commands += [(name, [], standard) for name, standard in MATH]
    commands += [('verificar_historial_visible_v3.py', ['--folder', 'trazabilidad/' + trace], True) for trace in TRACES]
    commands += [('test_historial_visible_v3.py', ['--temp-parent', str(parent)], True)]
    assert len(commands) == 16
    runs = []
    for index, (name, arguments, standard) in enumerate(commands, 1):
        environment = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1')
        environment.pop('PYTHONPATH', None)
        if not standard:
            environment['PYTHONPATH'] = str(DEPS)
        command = [sys.executable, '-B', '-X', 'utf8', *(['-S'] if standard else []), name, *arguments]
        started = time.monotonic()
        result = subprocess.run(command, cwd=isolated, env=environment, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=300)
        (job / f'check-{index}.stdout').write_text(result.stdout, encoding='utf-8')
        (job / f'check-{index}.stderr').write_text(result.stderr, encoding='utf-8')
        assert result.returncode == 0, (name, result.stdout[-2500:], result.stderr[-2500:])
        runs.append({'script': name, 'arguments': arguments, 'standard_library_only': standard,
                     'exit_code': result.returncode, 'seconds': time.monotonic() - started,
                     'stdout_sha256': sha(result.stdout.encode()), 'stderr_sha256': sha(result.stderr.encode())})
        print(f'{index}/16 {name} passed', flush=True)
    verify_folder(isolated)
    assert all(sha(Path(name).read_bytes()) == expected for name, expected in source_files.items())
    assert preserved == {name: current_hash(name) for name in PRESERVE}
    with OUT.open('xb') as stream:
        stream.write(candidate.read_bytes())
    assert sha(OUT.read_bytes()) == sha(candidate.read_bytes())
    verify_archive(OUT)
    receipt = {
        'archive': OUT.name, 'bytes': OUT.stat().st_size, 'sha256': sha(OUT.read_bytes()),
        'members': len(payload), 'payload_files': len(manifest['files']),
        'all_checks_passed': True, 'commands_passed': len(runs), 'runs': runs,
        'isolated_payload_unchanged': True, 'sources_unchanged_during_build': True,
        'project_bindings_checked_before_build': len(baseline['source_sha256']),
        'previous_artifacts_unchanged': preserved, 'temporary_parent': str(parent),
        'symbolic_dependencies': 'Existing external cache; five scientific commands use SymPy/mpmath. No fresh installation tested.',
        'math_tree_replayed': True, 'tree_builder_reexecuted': False,
        'search_reexecuted': False, 'existence_graph_plan_recomputed': True, 'media_rebuilt': False,
        'histories': {'messages': [159, 20], 'user_authorized_visible_messages_only': True,
                      'cutoffs_extended': False, 'current_packaging_turn_covered': False, 'other_chats_covered': False},
        'expanded_review_report_pages': 5, 'talk_and_poster_keep_strict_hypothesis': True,
        'team_proof_reviewed': False, 'independent_human_review': False,
        'rehearsed': False, 'submitted': False, 'goal_won_verified': False,
        'builder_sha256': sha(Path(__file__).read_bytes()),
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({name: receipt[name] for name in
                      ('archive', 'bytes', 'sha256', 'members', 'commands_passed', 'isolated_payload_unchanged')}))


if __name__ == '__main__':
    main()
