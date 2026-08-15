# -*- coding: utf-8 -*-
"""Inventario de equipamientos de salud alrededor de AAA0127AZPA (El Prado, Suba)
usando la capa oficial de instituciones prestadoras de salud (Datos Abiertos Bogota)."""
import io
import json
import math

from pyproj import Transformer

SRC = "data/transporte/ips_bogota.geojson"
ORIGEN = (102233.2065, 112615.234)  # ESRI:102233, origen SIRGAS del lote (contexto F1)

with io.open(SRC, encoding="utf-8") as f:
    g = json.load(f)

t = Transformer.from_crs("EPSG:4326", "ESRI:102233", always_xy=True)

# Campos disponibles en la primera feature
feat0 = g["features"][0]
print("CAMPOS:", sorted(feat0["properties"].keys()))
print("total features:", len(g["features"]))

rows = []
for feat in g["features"]:
    p = feat["properties"]
    geom = feat.get("geometry") or {}
    coords = geom.get("coordinates")
    if not coords:
        continue
    x, y = t.transform(coords[0], coords[1])
    d = math.hypot(x - ORIGEN[0], y - ORIGEN[1])
    rows.append((d, p))

rows.sort(key=lambda r: r[0])

for radio in (200, 500, 1000):
    dentro = [r for r in rows if r[0] <= radio]
    print(f"\n=== RADIO {radio} m: {len(dentro)} IPS ===")

print("\n=== DETALLE < 500 m ===")
for d, p in rows:
    if d <= 500:
        nombre = p.get("NOMBRE") or p.get("nombre") or p.get("RAZON_SOCIAL") or "?"
        tipo = p.get("TIPO") or p.get("tipo") or p.get("CLASIFICACION") or p.get("NIVEL") or "?"
        direc = p.get("DIRECCION") or p.get("direccion") or p.get("SEDE") or "?"
        print(f"  {d:6.0f} m | {tipo} | {nombre} | {direc}")
