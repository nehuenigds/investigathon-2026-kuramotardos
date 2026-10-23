from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parent
_cache_base = (
    Path.home() / 'AppData' / 'Local'
    if sys.platform == 'win32'
    else Path(os.environ.get('XDG_CACHE_HOME', str(Path.home() / '.cache')))
)
DEPS = Path(os.environ.get(
    'CODEX_W_KURAMOTO_DEPS',
    str(_cache_base / 'Codex' / 'work-cache' / 'W' / 'kuramoto' / 'deps'),
)).expanduser()
sys.path.insert(0, str(DEPS))

