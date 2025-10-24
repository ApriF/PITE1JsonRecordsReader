# tests/conftest.py
import sys
from pathlib import Path

# Ajoute le dossier src/ au PYTHONPATH si absent
root = Path(__file__).resolve().parents[1]
src_path = root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))
