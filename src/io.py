import json
from pathlib import Path
from datetime import datetime
from core import main


data_path = Path(__file__).parent / "sample_100.json"
threshold = 50


def read_json_file(file_path: str) -> list[dict]:
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_summary(stats: dict):
    """Affiche les stats"""
    print(f"ok={stats['count']} total_value={stats['sum']} avg={stats['avg']:.2f}")



def main_io(data_path, threshold):
    data = read_json_file(data_path)
    stats = main(data, threshold)
    print_summary(stats)


if __name__ == "__main__":
    main_io(data_path, threshold)
