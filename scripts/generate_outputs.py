import json
from datetime import datetime

with open("../outputs/json/processed.json") as f:
    data = json.load(f)

html = f"""
<html>
<head>
<title>SIEG OSINT</title>
<meta charset="utf-8">
</head>
<body>

<h1>Radar OSINT</h1>
<p>Última actualización: {data['timestamp']}</p>

<h2>Indicadores</h2>
<ul>
<li>IPC: {data['ipc']} ({data['ipc_trend']})</li>
<li>Energía: {data['energia']}</li>
<li>Alerta: {data['alert_level']}</li>
</ul>

</body>
</html>
"""

with open("../outputs/html/index.html", "w") as f:
    f.write(html)

print("HTML generado")
