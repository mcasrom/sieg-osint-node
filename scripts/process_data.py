import json

with open("../outputs/json/latest.json") as f:
    data = json.load(f)

# Lógica simple (luego metes IA/NLP aquí)
if data["ipc"] > 4:
    data["ipc_trend"] = "ALTO"
else:
    data["ipc_trend"] = "NORMAL"

with open("../outputs/json/processed.json", "w") as f:
    json.dump(data, f, indent=2)

print("Data processed")
