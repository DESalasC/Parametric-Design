# -*- coding: utf-8 -*-
"""Clasificación de predios inmediatamente vecinos por LADO (nomenclatura cardinal).

Convierte un <CHIP>-contexto.json en un <CHIP>-vecinos-por-lado.json que agrupa,
para cada lado del lote, los predios vecinos COLINDANTES (los que comparten
lindero con el lote), asignándoles nomenclatura cardinal:

    Lado Norte / Oriente / Sur / Occidente  (por el azimut de la normal saliente)
    Sub-segmentos: Norte1, Norte2, ... / Oriente1, Oriente2, ...

Esto resuelve el caso de un lote (p. ej. La Candelaria) donde por un mismo lado
hay DOS o MÁS lotes colindantes, cada uno con una altura distinta. El operador
identifica cada lado/sub-segmento y asigna los valores correspondientes.

Los segmentos consecutivos del polígono con el MISMO cardinal se FUSIONAN en un
único lado (los polígonos SIG suelen traer vértices colineales que partirían un
mismo lado real en varios). El campo "segmentos" conserva los índices originales
para poder mapear a sides_table_json (F1_ETAPA2_LADOS) y a vecinos_por_lado_json
(F1_ETAPA2_NORMATIVA_v08, que usa id_lado = índice de segmento).

Convenciones:
  - Coordenadas locales = SIRGAS trasladadas SIN rotación: +X = Este, +Y = Norte.
    Azimut desde el norte, sentido horario.
  - Un vecino de esquina puede colindar con DOS lados: aparece en ambos con
    nombre distinto (p. ej. "Norte2" y "Oriente1").

Dependencias: shapely (disponible en el .venv del proyecto). Herramienta de
PREPARACIÓN de datos (no GHPython; no aplican restricciones IronPython).

CLI:
  python vecinos_por_lado.py <CHIP|ruta.json> [--out ruta_salida.json]
"""

from __future__ import annotations

import argparse
import io
import json
import math
import os
import sys
from typing import Dict, List, Optional, Tuple

from shapely.geometry import LineString, Point, Polygon

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
POT_CACHE = os.path.join(ROOT, "data", "pot-cache")

TOL_COLINDANCIA_M = 0.15
N_SAMPLES = 40
MIN_FRACCION = 0.25

CARDINAL_BANDS = [
    ("Norte", 315.0, 45.0),      # cruza el 0
    ("Oriente", 45.0, 135.0),
    ("Sur", 135.0, 225.0),
    ("Occidente", 225.0, 315.0),
]


def azimut(vx: float, vy: float) -> float:
    """Azimut (0..360, desde el norte, sentido horario) del vector (vx, vy)."""
    if vx == 0.0 and vy == 0.0:
        return 0.0
    return math.degrees(math.atan2(vx, vy)) % 360.0


def cardinal(az: float) -> str:
    """Nombre cardinal de un azimut (0..360)."""
    for name, lo, hi in CARDINAL_BANDS:
        if lo <= hi:
            if lo <= az < hi:
                return name
        else:  # banda que cruza 0 (Norte)
            if az >= lo or az < hi:
                return name
    return "Norte"


def _normal_saliente(p1: Tuple[float, float], p2: Tuple[float, float],
                     centroid: Tuple[float, float]) -> Tuple[float, float]:
    """Normal unitaria que apunta hacia AFUERA del lote, para el lado p1->p2."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    n1 = (-dy, dx)
    n2 = (dy, -dx)
    mx = (p1[0] + p2[0]) / 2.0
    my = (p1[1] + p2[1]) / 2.0
    vx = mx - centroid[0]
    vy = my - centroid[1]
    d1 = vx * n1[0] + vy * n1[1]
    d2 = vx * n2[0] + vy * n2[1]
    return n1 if d1 >= d2 else n2


def _fraccion_colindancia(side_line: LineString, poly: Polygon,
                          tol_m: float = TOL_COLINDANCIA_M,
                          n_samples: int = N_SAMPLES) -> float:
    """Fracción (0..1) del lado que está a <= tol_m del polígono vecino."""
    if side_line.is_empty or poly.is_empty:
        return 0.0
    hits = 0
    for k in range(n_samples + 1):
        t = k / float(n_samples)
        pt = side_line.interpolate(t, normalized=True)
        if poly.distance(pt) <= tol_m:
            hits += 1
    return hits / float(n_samples + 1)


def _posicion_media(side_line: LineString, poly: Polygon) -> float:
    """Posición (0..1) del vecino a lo largo del lado, para ordenar sub-segmentos."""
    if poly.is_empty:
        return 0.0
    c = poly.centroid
    return side_line.project(Point(c.x, c.y), normalized=True)


def _agrupar_por_cardinal(segments: List[Dict]) -> Dict[str, List[Dict]]:
    """Agrupa TODOS los segmentos por cardinal, preservando el orden de frontera."""
    grupos: Dict[str, List[Dict]] = {}
    for seg in segments:
        grupos.setdefault(seg["cardinal"], []).append(seg)
    return grupos


def clasificar_vecinos_por_lado(contexto: Dict, tol_m: float = TOL_COLINDANCIA_M,
                                n_samples: int = N_SAMPLES,
                                min_frac: float = MIN_FRACCION) -> Dict:
    """Clasifica los vecinos colindantes por lado (fusionando cardinales) y asigna nomenclatura."""
    meta = contexto.get("metadata", {})
    chip = meta.get("chip", "")
    crs = meta.get("origen_sirgas", {}).get("crs", "")
    azimuth = meta.get("azimuth_norte_grados", 0.0)

    lote = contexto.get("lote_objetivo", {}).get("vertices_3d_local", [])
    pts = [(float(x), float(y)) for x, y, _z in lote]
    if len(pts) < 3:
        return {"chip": chip, "error": "lote sin vértices suficientes", "lados": []}
    if pts[0] != pts[-1]:
        pts.append(pts[0])
    n = len(pts) - 1

    lot_poly = Polygon(pts)
    if not lot_poly.is_valid:
        lot_poly = lot_poly.buffer(0)
    centroid = (lot_poly.centroid.x, lot_poly.centroid.y)

    # segmentos del lote
    segments: List[Dict] = []
    for i in range(n):
        p1 = pts[i]
        p2 = pts[i + 1]
        line = LineString([p1, p2])
        nx, ny = _normal_saliente(p1, p2, centroid)
        az = azimut(nx, ny)
        segments.append({
            "id": i,
            "cardinal": cardinal(az),
            "azimut_grados": az,
            "line": line,
            "longitud_m": line.length,
        })

    # vecinos colindantes por SEGMENTO (para luego consolidar por lado fusionado)
    vecinos: List[Tuple[str, Polygon]] = []
    for v in contexto.get("vecinos", []):
        vpts = [(float(x), float(y)) for x, y, _z in v.get("vertices_3d_local", [])]
        if len(vpts) < 3:
            continue
        poly = Polygon(vpts)
        if not poly.is_valid:
            poly = poly.buffer(0)
        if poly.is_empty:
            continue
        vecinos.append((v.get("chip", ""), poly))

    lados_out: List[Dict] = []
    total_colindantes = 0
    order = {"Norte": 0, "Oriente": 1, "Sur": 2, "Occidente": 3}
    por_cardinal = _agrupar_por_cardinal(segments)
    for card in sorted(por_cardinal.keys(), key=lambda c: order.get(c, 9)):
        grupo = por_cardinal[card]
        # vecinos colindantes con este lado (dedupe por chip) + posición para ordenar
        colindantes: Dict[str, Dict] = {}
        for seg in grupo:
            for chip_v, poly in vecinos:
                frac = _fraccion_colindancia(seg["line"], poly, tol_m, n_samples)
                if frac >= min_frac:
                    t = _posicion_media(seg["line"], poly)
                    shared = round(frac * seg["longitud_m"], 2)
                    if chip_v not in colindantes:
                        colindantes[chip_v] = {"chip": chip_v, "seg_min": seg["id"], "t": t,
                                               "longitud_colindancia_m": shared}
                    else:
                        # acumula longitud y usa el segmento más temprano para ordenar
                        colindantes[chip_v]["longitud_colindancia_m"] = round(
                            colindantes[chip_v]["longitud_colindancia_m"] + shared, 2)
                        if seg["id"] < colindantes[chip_v]["seg_min"]:
                            colindantes[chip_v]["seg_min"] = seg["id"]
                            colindantes[chip_v]["t"] = t

        ordenados = sorted(colindantes.values(), key=lambda vv: (vv["seg_min"], vv["t"]))
        vecinos_out = []
        for k, vv in enumerate(ordenados, start=1):
            vecinos_out.append({
                "chip": vv["chip"],
                "nombre": "%s%d" % (grupo[0]["cardinal"], k),
                "longitud_colindancia_m": vv["longitud_colindancia_m"],
                "altura_m": None,   # lo completa el operador
                "pisos": None,      # lo completa el operador
            })
        total_colindantes += len(vecinos_out)
        lados_out.append({
            "cardinal": grupo[0]["cardinal"],
            "azimut_grados": round(grupo[0]["azimut_grados"], 1),
            "segmentos": [g["id"] for g in grupo],
            "longitud_m": round(sum(g["longitud_m"] for g in grupo), 2),
            "n_vecinos": len(vecinos_out),
            "vecinos": vecinos_out,
        })

    return {
        "chip": chip,
        "crs": crs,
        "azimuth_norte_grados": azimuth,
        "n_lados": len(lados_out),
        "n_vecinos_colindantes": total_colindantes,
        "lados": lados_out,
    }


def _load_contexto(chip_or_path: str) -> Tuple[str, Dict]:
    if chip_or_path.lower().endswith(".json") and os.path.exists(chip_or_path):
        path = chip_or_path
        data = json.loads(io.open(path, "r", encoding="utf-8").read())
        chip = data.get("metadata", {}).get("chip", os.path.splitext(os.path.basename(path))[0])
        return chip, data
    chip = chip_or_path
    path = os.path.join(POT_CACHE, "%s-contexto.json" % chip)
    if not os.path.exists(path):
        raise FileNotFoundError("no existe contexto para %s (%s)" % (chip, path))
    return chip, json.loads(io.open(path, "r", encoding="utf-8").read())


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Clasifica vecinos colindantes por lado (nomenclatura cardinal).")
    ap.add_argument("chip_or_json", help="CHIP o ruta al <CHIP>-contexto.json")
    ap.add_argument("--out", help="ruta de salida (default: data/pot-cache/<CHIP>-vecinos-por-lado.json)")
    args = ap.parse_args(argv)

    chip, data = _load_contexto(args.chip_or_json)
    result = clasificar_vecinos_por_lado(data)

    out = args.out or os.path.join(POT_CACHE, "%s-vecinos-por-lado.json" % chip)
    io.open(out, "w", encoding="utf-8").write(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    )
    print("OK -> %s (%d lados, %d vecinos colindantes)" % (
        out, result.get("n_lados", 0), result.get("n_vecinos_colindantes", 0)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
