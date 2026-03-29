import json
from datetime import datetime
import random

# Simulación de datos (luego conectas APIs reales)
data = {
    "timestamp": datetime.utcnow().isoformat(),
    "ipc": round(random.uniform(2.0, 5.0), 2),
    "energia": round(random.uniform(50, 150), 2),
    "alert_level": random.choice(["LOW", "MEDIUM", "HIGH"])
}

with open("../outputs/json/latest.json", "w") as f:
    json.dump(data, f, indent=2)

print("Data fetched")
