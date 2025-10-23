# io.py
import json
import argparse
from pathlib import Path
from datetime import datetime
from core import main


# ---------- CONFIGURATION ---------- #

def load_config(config_path: Path | None = None) -> dict:
    """Charge la configuration par défaut ou depuis un fichier JSON."""
    default_config = {
        "data_path": Path(__file__).parent / "sample_100.json",
        "threshold": 50.0
    }

    if config_path and config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                file_config = json.load(f)
            default_config.update(file_config)
        except Exception as e:
            print(f"⚠️ Impossible de charger la config depuis {config_path}: {e}")
    return default_config


# ---------- FONCTIONS MÉTIER ---------- #

def read_json_file(file_path: Path) -> list[dict]:
    """Lit un fichier JSON et renvoie les enregistrements."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier {file_path}: {e}")
        return []


def print_summary(stats: dict):
    """Affiche les statistiques formatées."""
    stamp = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
    print(f"[{stamp}] ok={stats['count']} total_value={stats['sum']} avg={stats['avg']:.2f}")


def main_io(data_path: Path, threshold: float):
    """Lit, traite et affiche les résultats."""
    data = read_json_file(data_path)
    if not data:
        print(f"⚠️ Aucun enregistrement trouvé dans {data_path}")
        return
    stats = main(data, threshold)
    print_summary(stats)


# ---------- CLI (interface ligne de commande) ---------- #

def parse_args() -> argparse.Namespace:
    """Parse les arguments CLI."""
    parser = argparse.ArgumentParser(description="Analyse de fichiers JSON")
    parser.add_argument("--file", type=Path, help="Chemin du fichier JSON à traiter")
    parser.add_argument("--thres", type=float, help="Seuil minimal pour filtrer les valeurs")
    parser.add_argument("--config", type=Path, help="Chemin d’un fichier de configuration JSON")
    return parser.parse_args()


def main_cli():
    """Point d’entrée CLI : lit la config + les arguments utilisateur."""
    args = parse_args()
    config = load_config(args.config)

    # Remplace la config par les arguments s’ils sont présents
    if args.file:
        config["data_path"] = args.file
    if args.thres is not None:
        config["threshold"] = args.thres

    main_io(config["data_path"], config["threshold"])


if __name__ == "__main__":
    main_cli()
