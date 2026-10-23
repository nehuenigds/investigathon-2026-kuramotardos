"""Read-only portable integrity check for the expanded team review package."""
from pathlib import Path, PurePosixPath
from zipfile import ZipFile
import argparse
import hashlib
import json
import stat

VISIBLE_TRACES = {
    'trazabilidad/chat-visible-20261022-v1/mensajes.jsonl',
    'trazabilidad/preparacion-visible-20261022-v1/mensajes.jsonl',
}


def safe_name(name):
    parts = PurePosixPath(name)
    assert name and not parts.is_absolute() and '..' not in parts.parts
    assert ':' not in name and '\\' not in name and parts.as_posix() == name


def verify_bytes(manifest, names, read):
    assert manifest['version'] == 2
    assert manifest['visible_messages_only'] is True
    assert manifest['private_raw_logs_included'] is False
    files = manifest['files']
    assert set(names) == set(files) | {'MANIFEST.json'}, 'Manifest/member mismatch'
    assert {name for name in names if name.endswith('.jsonl')} == VISIBLE_TRACES, 'Unexpected message files'
    for name, expected in files.items():
        safe_name(name)
        raw = read(name)
        assert len(raw) == expected['bytes'], 'Size mismatch: ' + name
        assert hashlib.sha256(raw).hexdigest() == expected['sha256'], 'Hash mismatch: ' + name
    return {'integrity_passed': True, 'payload_files': len(files),
            'visible_trace_files': 2,
            'scope': 'Bytes agree with this manifest; not an author signature, mathematical review or proof of complete chat coverage.'}


def verify_archive(path):
    with ZipFile(path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names)), 'Duplicate members'
        for info in archive.infolist():
            safe_name(info.filename)
            assert not info.is_dir() and not stat.S_ISLNK(info.external_attr >> 16)
        assert archive.testzip() is None
        manifest = json.loads(archive.read('MANIFEST.json'))
        return verify_bytes(manifest, names, archive.read)


def verify_folder(path):
    root = path.resolve()
    names = []
    for file in root.rglob('*'):
        assert not file.is_symlink(), 'Symlink in package'
        if file.is_file():
            assert file.resolve().is_relative_to(root)
            names.append(file.relative_to(root).as_posix())
    manifest = json.loads((root / 'MANIFEST.json').read_text(encoding='utf-8'))
    return verify_bytes(manifest, names, lambda name: (root / name).read_bytes())


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--archive', type=Path)
    group.add_argument('--folder', type=Path)
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError('Run without -O: assertions are required.')
    result = verify_archive(args.archive) if args.archive else verify_folder(args.folder)
    print(json.dumps(result))


if __name__ == '__main__':
    main()
