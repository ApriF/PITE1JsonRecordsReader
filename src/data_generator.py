import json
import random
from pathlib import Path

# Génération d'un fichier JSON contenant 100 valeurs aléatoires
# Dossier du script 
current_dir = Path(__file__).parent

output_path = current_dir / "sample_100.json"

records = []
for i in range(100):
    status = random.choice(["ok", "bad", "error", "OK", "Bad"])
    val_type = random.choice(["int", "float", "str", "none"])
    if val_type == "int":
        value = random.randint(0, 100)
    elif val_type == "float":
        value = round(random.uniform(0, 100), 2)
    elif val_type == "str":
        value = str(random.randint(0, 100))
    else:
        value = None
    records.append({"status": status, "value": value})


with open(output_path, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)

