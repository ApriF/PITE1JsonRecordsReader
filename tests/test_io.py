import json
import tempfile
from pathlib import Path
from src import io


def test_read_json_file(tmp_path):
    """Test a valid JSON file"""
    data = [{"status": "ok", "value": 10}]
    test_file = tmp_path / "data.json"
    test_file.write_text(json.dumps(data), encoding="utf-8")

    res = io.read_json_file(test_file)
    assert isinstance(res, list)
    assert res[0]["status"] == "ok"


def test_read_json_file_invalid(tmp_path):
    """Test a bad file"""
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{invalid json", encoding="utf-8")

    res = io.read_json_file(bad_file)
    assert res == []  # doit retourner une liste vide


def test_print_summary(capsys):
    """Checks the file format of the output"""
    stats = {"count": 3, "sum": 60, "avg": 20.0}
    io.print_summary(stats)
    captured = capsys.readouterr().out
    assert "ok=" in captured
    assert "total_value=" in captured
    assert "avg=" in captured


def test_main_io(monkeypatch, tmp_path, capsys):
    """Test d'intégration : lecture + stats simulées."""
    # Crée un fichier temporaire
    data = [{"status": "ok", "value": 10}]
    file = tmp_path / "data.json"
    file.write_text(json.dumps(data), encoding="utf-8")

    # Simule core.main pour ne pas dépendre de la logique métier
    def fake_main(data, threshold):
        return {"count": 1, "sum": 10.0, "avg": 10.0}

    monkeypatch.setattr(io, "main", fake_main)
    io.main_io(file, 0)

    captured = capsys.readouterr().out
    assert "ok=" in captured
