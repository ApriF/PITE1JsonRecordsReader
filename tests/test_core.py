import pytest
from src.core import filtrer, compute_stats, main


@pytest.fixture
def sample_records():
    return [
        {"status": "ok", "value": 10},
        {"status": "OK", "value": "20"},
        {"status": "bad", "value": 30},
        {"STATUS": "ok", "value": 5},
        {"status": "ok", "value": None},
        {"status": "ok", "value": "abc"},  # invalide
    ]


def test_filtrer_threshold(sample_records):
    res = filtrer(sample_records, threshold=10)
    assert len(res) == 2
    assert all(r["status"] == "ok" for r in res)
    assert {r["value"] for r in res} == {10.0, 20.0}


def test_filtrer_empty_list():
    assert filtrer([], 10) == []


def test_compute_stats():
    data = [{"value": 10}, {"value": 20}, {"value": 30}]
    stats = compute_stats(data)
    assert stats["count"] == 3
    assert stats["sum"] == 60
    assert stats["avg"] == pytest.approx(20.0)


def test_compute_stats_empty():
    assert compute_stats([]) == {"count": 0, "sum": 0.0, "avg": 0.0}


def test_main_integration(sample_records):
    stats = main(sample_records, 10)
    assert stats["count"] == 2
    assert stats["sum"] == 30
    assert stats["avg"] == pytest.approx(15.0)
