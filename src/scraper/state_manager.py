import json
from pathlib import Path
from ..utils.config import STATE_FILE


class StateManager:
def __init__(self, path=STATE_FILE):
self.path = Path(path)
if not self.path.exists():
self._write({})


def _read(self):
with self.path.open('r') as f:
return json.load(f)


def _write(self, obj):
with self.path.open('w') as f:
json.dump(obj, f, indent=2)


def get(self, project):
data = self._read()
return data.get(project, {'startAt': 0})


def set(self, project, state):
data = self._read()
data[project] = state
self._write(data)
