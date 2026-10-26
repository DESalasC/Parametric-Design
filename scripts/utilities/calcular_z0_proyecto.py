# -*- coding: utf-8 -*-
"""Calcula el datum Z0 del proyecto (marco de calculo) segun la regla ADR-024.

Modos:
  min_lote           punto mas bajo del predio (vertice de menor Z del lote).
  centro_lindero_via centro del lindero del lote contra la via (arista del lote
                     mas cercana a una via; Z en el punto medio de esa arista).
  manual             valor local definido por el operador (o absoluto con --absoluto).

El resultado se escribe en `data/pot-cache/<CHIP>-z0.json` y es la fuente unica
para F1/F2/F3. El marco ArchiCAD se normaliza aparte: GF = 0 (ver ADR-024).

Uso:
  python scripts/utilities/calcular_z0_proyecto.py --chip AAA0030JKOE --modo min_lote
  python scripts/utilities/calcular_z0_proyecto.py --chip AAA0030JKOE --modo centro_lindero_via
  python scripts/utilities/calcular_z0_proyecto.py --chip AAA0030JKOE --modo manual --valor 0.0
"""
from __future__ import print_function

import argparse
import io
import json
import math
import os
import sys
import time

from shapely.geometry import LineString, Point

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def leer(path):
    with io.open(path, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def anillo(vertices):
    pts = [(float(v[0]), float(v[1]), float(v[2])) for v in (vertices or [])]
    if len(pts) >= 2 and abs(pts[0][0] - pts[-1][0]) < 1e-9 and abs(pts[0][1] - pts[-1][1]) < 1e-9:
        pts.pop()
    return pts


def z0_min_lote(vertices):
    """Vertice de menor Z del lote. Devuelve (z0_m, fuente)."""
    pts = anillo(vertices)
    if not pts:
        raise ValueError("lote sin vertices")
    v = min(pts, key=lambda p: p[2])
    return v[2], {"vertice": [round(v[0], 3), round(v[1], 3), round(v[2], 3)],
                  "n_vertices": len(pts)}


def z0_centro_lindero_via(vertices, vias):
    """Z en el punto medio de la arista del lote mas cercana a una via."""
    pts = anillo(vertices)
    if len(pts) < 2:
        raise ValueError("lote sin aristas")
    lineas = []
    for via in vias or []:
        coords = [(float(p[0]), float(p[1])) for p in (via.get("coordenadas_local") or [])]
        if len(coords) >= 2:
            lineas.append((via.get("nombre") or "", LineString(coords)))
    if not lineas:
        raise ValueError("sin vias para centro_lindero_via")

    mejor = None
    for i in range(len(pts)):
        a, b = pts[i], pts[(i + 1) % len(pts)]
        mid = Point((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)
        for nombre, linea in lineas:
            d = linea.distance(mid)
            if mejor is None or d < mejor[0]:
                mejor = (d, i, nombre, mid, a, b)
    if mejor is None:
        raise ValueError("no se pudo medir distancia a vias")
    d, i, nombre, mid, a, b = mejor
    z = (a[2] + b[2]) / 2.0
    return z, {"lado": i, "via": nombre, "dist_via_m": round(d, 2),
               "midpoint": [round(mid.x, 3), round(mid.y, 3)],
               "z_extremos": [round(a[2], 3), round(b[2], 3)], "n_vertices": len(pts)}


def z0_manual(valor, origen_z, absoluto=False):
    z0 = float(valor) - float(origen_z) if absoluto else float(valor)
    return z0, {"valor_entrada_m": float(valor), "absoluto": bool(absoluto)}


def main():
    ap = argparse.ArgumentParser(description="Datum Z0 del proyecto (ADR-024)")
    ap.add_argument("--chip", required=True)
    ap.add_argument("--modo", required=True, choices=("min_lote", "centro_lindero_via", "manual"))
    ap.add_argument("--valor", type=float, default=None, help="Z local para modo manual")
    ap.add_argument("--absoluto", action="store_true", help="--valor esta en Z absoluto")
    ap.add_argument("--contexto", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    chip = args.chip.strip().upper()
    ruta = args.contexto or os.path.join(ROOT, "data", "pot-cache", chip + "-contexto.json")
    if not os.path.isfile(ruta):
        print("[ERROR] No existe", ruta)
        return 2
    d = leer(ruta)
    meta = d.get("metadata") or {}
    origen_z = float((meta.get("origen_sirgas") or {}).get("z") or 0.0)
    lote = (d.get("lote_objetivo") or {}).get("vertices_3d_local") or []
    if len(lote) < 3:
        print("[ERROR] lote_objetivo sin vertices")
        return 2

    try:
        if args.modo == "min_lote":
            z0, fuente = z0_min_lote(lote)
        elif args.modo == "centro_lindero_via":
            z0, fuente = z0_centro_lindero_via(lote, d.get("vias_oficiales"))
        else:
            if args.valor is None:
                print("[ERROR] --modo manual requiere --valor")
                return 2
            z0, fuente = z0_manual(args.valor, origen_z, args.absoluto)
    except Exception as e:
        print("[ERROR]", e)
        return 2

    salida = {
        "schema": "f1_z0_datum_v01",
        "chip": chip,
        "modo": args.modo,
        "z0_m": round(z0, 4),
        "z0_abs_m": round(origen_z + z0, 4),
        "origen_z_m": round(origen_z, 4),
        "fuente": fuente,
        "fecha": time.strftime("%Y-%m-%d %H:%M"),
        "nota": ("Marco de calculo: Z_modelo = Z_abs - z0_m. "
                 "ArchiCAD se normaliza aparte con GF = 0 (ADR-024)."),
    }
    print(json.dumps(salida, ensure_ascii=False, indent=2))
    if args.dry_run:
        print("[dry-run] no se escribe")
        return 0
    destino = args.out or os.path.join(ROOT, "data", "pot-cache", chip + "-z0.json")
    with io.open(destino, "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, indent=2)
    print("escrito:", destino)
    return 0


if __name__ == "__main__":
    sys.exit(main())
