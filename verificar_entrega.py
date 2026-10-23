"""Verify the local delivery without network or third-party packages."""
from pathlib import Path
import hashlib,json,subprocess,sys

if not __debug__:
    raise RuntimeError('Run without -O: assertions are required.')
root=Path(__file__).resolve().parent
manifest=json.loads((root/'MANIFEST.json').read_text(encoding='utf-8'))
assert manifest['format']=='kuramotardos-local-delivery-v2'
actual=set()
for path in root.rglob('*'):
    relative=path.relative_to(root)
    if relative.parts[0]=='.git':
        continue
    assert not path.is_symlink(),'Symlink: '+str(relative)
    if path.is_file():
        actual.add(relative.as_posix())
assert actual==set(manifest['files'])|{'MANIFEST.json'},'File list differs'
for name,entry in manifest['files'].items():
    raw=(root/name).read_bytes()
    assert len(raw)==entry['bytes'] and hashlib.sha256(raw).hexdigest()==entry['sha256'],name
commands=[('materiales','verify_review_package.py',['--folder','.']),
          ('trazabilidad-actualizada','verificar_historial_visible_v3.py',
           ['--folder','trazabilidad/chat-visible-20261023-v1']),
          ('trazabilidad-actualizada','verificar_historial_visible_v3.py',
           ['--folder','trazabilidad/preparacion-visible-20261022-v1'])]
for folder,script,args in commands:
    result=subprocess.run([sys.executable,'-B','-S','-X','utf8',script,*args],
        cwd=root/folder,capture_output=True,text=True,encoding='utf-8',timeout=120)
    assert result.returncode==0,(script,result.stdout,result.stderr)
print(json.dumps({'integrity_passed':True,'payload_files':len(manifest['files']),
    'inner_checks_passed':len(commands),'unique_visible_messages':237,
    'scope':'Integrity of this frozen selection; not human mathematical review or submission.'}))
