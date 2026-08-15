import json
import urllib.request
from System.Collections.Generic import List

names = List[str]()
is_hidden = List[bool]()
colors = List[int]()
status = "Listo para procesar"

if json_text:
    try:
        data = json.loads(str(json_text))
        for item in data:
            names.Add(str(item.get("nombre", "")))
            is_hidden.Add(not bool(item.get("visible", True)))
            colors.Add(int(item.get("color", 1)))
        status = f"JSON procesado: {names.Count} capas parsed."
        if execute:
            url = "http://127.0.0.1:61321"
            payload = {
                "command": "CreateLayers",
                "parameters": {
                    "layers": [
                        {"name": n, "isHidden": h, "isLocked": False}
                        for n, h in zip(names, is_hidden)
                    ]
                }
            }
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                status = f"Respuesta ArchiCAD: {res_data}"
    except Exception as e:
        status = f"Error: {str(e)}"
