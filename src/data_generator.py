import json
import random
from pathlib import Path

# Dossier courant du script
current_dir = Path(__file__).parent

# Chemin du fichier de sortie (relatif au script)
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

print(f"✅ Fichier généré : {output_path}")
