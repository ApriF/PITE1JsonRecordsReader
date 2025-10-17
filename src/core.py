
from typing import Iterable
from statistics import mean


def filtrer(records: Iterable[dict], threshold: float) -> list[dict]:
    """Ne garde que les valeurs status='ok' et value >= threshold."""
    out: list[dict] = []
    for r in records:
        if not isinstance(r, dict):
            continue
        status = r.get("status", r.get("STATUS", "")).lower()
        if status == "ok":
            val = r.get("value", 0)
            try:
                val = float(val)
            except (TypeError, ValueError):
                continue
            if val >= threshold:
                out.append({"status": "ok", "value": val})
    return out


def compute_stats(records: list[dict]) -> dict[str, float]:
    """Calcule les stats (count, sum, average) à partir du dictionnnaire précédent."""
    values = [r["value"] for r in records if "value" in r]
    if not values:
        return {"count": 0, "sum": 0.0, "avg": 0.0}
    return {
        "count": len(values),
        "sum": sum(values),
        "avg": mean(values),
    }


def main(records: list[dict], threshold: float = 0) -> dict[str, float]:
    filtered = filtrer(records, threshold)
    return compute_stats(filtered)
