# -*- coding: utf-8 -*-
"""inventario_salud_lote.py — Inventario de equipamientos de salud alrededor de un lote.

Usa la capa oficial de instituciones prestadoras de salud de Bogota (Datos Abiertos,
resource ips.geojson, descargada a data/transporte/) y el origen SIRGAS del contexto F1
(data/pot-cache/<CHIP>-contexto.json) para contar y listar IPS en radios 200/500/1000 m.

USO:  python scripts/utilities/inventario_salud_lote.py <CHIP>
SALIDA: exports/alcance/<CHIP>-salud.json
"""
import io
import json
import math
import os
import sys

from pyproj import Transformer

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, "..", ".."))
SRC_IPS = os.path.join(ROOT, "data", "transporte", "ips_bogota.geojson")

RADIOS = (200, 500, 1000)


def cargar_origen(chip):
    ruta = os.path.join(ROOT, "data", "pot-cache", f"{chip}-contexto.json")
    with io.open(ruta, encoding="utf-8") as f:
        ctx = json.load(f)
    o = ctx["metadata"]["origen_sirgas"]
    return o["x"], o["y"]


def main():
    chip = sys.argv[1] if len(sys.argv) > 1 else "AAA0127AZPA"
    ox, oy = cargar_origen(chip)
    with io.open(SRC_IPS, encoding="utf-8") as f:
        g = json.load(f)
    t = Transformer.from_crs("EPSG:4326", "ESRI:102233", always_xy=True)

    rows = []
    for feat in g["features"]:
        p = feat["properties"]
        coords = (feat.get("geometry") or {}).get("coordinates")
        if not coords:
            continue
        x, y = t.transform(coords[0], coords[1])
        d = math.hypot(x - ox, y - oy)
        rows.append({"distancia_m": round(d, 1),
                     "nombre": p.get("nombre") or "?",
                     "direccion": p.get("direccion") or "?",
                     "nivel": p.get("nivel") or "?",
                     "naturaleza": p.get("naturaleza") or "?",
                     "clase_pres": p.get("clase_pres") or "?",
                     "clase_pers": p.get("clase_pers") or "?",
                     "barrio": p.get("barrio") or "?"})
    rows.sort(key=lambda r: r["distancia_m"])

    salida = {
        "chip": chip,
        "origen_sirgas": {"crs": "ESRI:102233", "x": ox, "y": oy},
        "capa": "instituciones-prestadoras-de-salud-bogota (Datos Abiertos Bogota, ips.geojson)",
        "fecha": "2026-08-14",
        "total_ips_ciudad": len(rows),
        "radios": {str(r): [x for x in rows if x["distancia_m"] <= r] for r in RADIOS},
        "resumen": {str(r): len([x for x in rows if x["distancia_m"] <= r]) for r in RADIOS},
        "detalle_500m": [x for x in rows if x["distancia_m"] <= 500],
    }
    out = os.path.join(ROOT, "exports", "alcance", f"{chip}-salud.json")
    with io.open(out, "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, indent=2)
    print(f"OK {out}")
    print("Resumen:", salida["resumen"])


if __name__ == "__main__":
    main()
