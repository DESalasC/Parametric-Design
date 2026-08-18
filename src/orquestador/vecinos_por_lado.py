# -*- coding: utf-8 -*-
"""Clasificación de predios inmediatamente vecinos por LADO (nomenclatura cardinal).

Convierte un <CHIP>-contexto.json en un <CHIP>-vecinos-por-lado.json que clasifica,
para cada lado del lote, QUÉ enfrenta ese lado:

    - "predio"           : predio(s) vecino(s) colindante(s) — requieren empate/altura
    - "via"              : calle / vía (NO es predio vecino)
    - "espacio_publico"  : zona verde / parque / plaza (NO es predio vecino)
    - "libre"            : sin contacto detectado

Solo los lados "predio" listan vecinos con sub-índice (Norte1, Norte2, ...).

LIMITACIONES CONOCIDAS (documentadas en el campo "nota"):
  - Las vías provienen de `vias_oficiales` (Eje_vial del POT), que está INCOMPLETA
    (muchas calles no digitalizadas). Lados que en realidad dan a vía pueden
    clasificarse como "predio" si su vía no está en el dato.
  - Algunas zonas verdes están capturadas como "vecinos" (predios con CHIP), no en
    `espacios_publicos`; no hay atributo de uso para separarlas automáticamente.

Convenciones:
  - Coordenadas locales = SIRGAS trasladadas SIN rotación: +X = Este, +Y = Norte.
  - Un vecino de esquina puede colindar con DOS lados.

CLI:  python vecinos_por_lado.py <CHIP|ruta.json> [--out ruta_salida.json]
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
from shapely.ops import unary_union

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
POT_CACHE = os.path.join(ROOT, "data", "pot-cache")

TOL_COLINDANCIA_M = 0.15     # vecino colindante (comparte lindero)
N_SAMPLES = 40
MIN_FRACCION_VECINO = 0.25
TOL_VIA_M = 12.0             # centro de la vía puede estar a media calzada + andén
MIN_FRACCION_VIA = 0.40
TOL_EP_M = 1.0
MIN_FRACCION_EP = 0.40

CARDINAL_BANDS = [
    ("Norte", 315.0, 45.0),
    ("Oriente", 45.0, 135.0),
    ("Sur", 135.0, 225.0),
    ("Occidente", 225.0, 315.0),
]


def azimut(vx: float, vy: float) -> float:
    if vx == 0.0 and vy == 0.0:
        return 0.0
    return math.degrees(math.atan2(vx, vy)) % 360.0


def cardinal(az: float) -> str:
    for name, lo, hi in CARDINAL_BANDS:
        if lo <= hi:
            if lo <= az < hi:
                return name
        else:
            if az >= lo or az < hi:
                return name
    return "Norte"


def _normal_saliente(p1, p2, centroid):
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


def _poly2d(points: List) -> Optional[Polygon]:
    pts = [(float(x), float(y)) for x, y, _z in points]
    if len(pts) < 3:
        return None
    p = Polygon(pts)
    if not p.is_valid:
        p = p.buffer(0)
    return p if not p.is_empty else None


def _frac_dentro(line: LineString, geom, tol_m: float, n_samples: int = N_SAMPLES) -> float:
    if geom is None or line.is_empty:
        return 0.0
    hits = 0
    for k in range(n_samples + 1):
        t = k / float(n_samples)
        pt = line.interpolate(t, normalized=True)
        if geom.distance(pt) <= tol_m:
            hits += 1
    return hits / float(n_samples + 1)


def _posicion_media(side_line: LineString, poly: Polygon) -> float:
    if poly.is_empty:
        return 0.0
    c = poly.centroid
    return side_line.project(Point(c.x, c.y), normalized=True)


def _agrupar_por_cardinal(segments: List[Dict]) -> Dict[str, List[Dict]]:
    grupos: Dict[str, List[Dict]] = {}
    for seg in segments:
        grupos.setdefault(seg["cardinal"], []).append(seg)
    return grupos


def clasificar_vecinos_por_lado(contexto: Dict,
                                tol_vecino: float = TOL_COLINDANCIA_M,
                                tol_via: float = TOL_VIA_M,
                                tol_ep: float = TOL_EP_M) -> Dict:
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

    # geometrías de vías y espacios públicos (unión para consulta rápida)
    via_geoms: List[LineString] = []
    for v in contexto.get("vias_oficiales", []):
        cl = v.get("coordenadas_local", [])
        if len(cl) >= 2:
            via_geoms.append(LineString([(float(x), float(y)) for x, y, _z in cl]))
    vias = unary_union(via_geoms) if via_geoms else None

    ep_polys: List[Polygon] = []
    for e in contexto.get("espacios_publicos", []):
        p = _poly2d(e.get("coordenadas_local", []))
        if p is not None:
            ep_polys.append(p)
    eps = unary_union(ep_polys) if ep_polys else None

    vecinos: List[Tuple[str, Polygon]] = []
    for v in contexto.get("vecinos", []):
        p = _poly2d(v.get("vertices_3d_local", []))
        if p is not None:
            vecinos.append((v.get("chip", ""), p))

    # segmentos del lote + fracciones de contacto
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
            "frac_via": _frac_dentro(line, vias, tol_via),
            "frac_ep": _frac_dentro(line, eps, tol_ep),
        })

    lados_out: List[Dict] = []
    total_predios = 0
    order = {"Norte": 0, "Oriente": 1, "Sur": 2, "Occidente": 3}
    for card in sorted(_agrupar_por_cardinal(segments).keys(), key=lambda c: order.get(c, 9)):
        grupo = _agrupar_por_cardinal(segments)[card]
        longitud_total = sum(g["longitud_m"] for g in grupo) or 1.0
        frac_via = sum(g["frac_via"] * g["longitud_m"] for g in grupo) / longitud_total
        frac_ep = sum(g["frac_ep"] * g["longitud_m"] for g in grupo) / longitud_total

        # vecinos colindantes por segmento (dedupe por chip)
        colindantes: Dict[str, Dict] = {}
        seg_vecinos: Dict[int, List[str]] = {}
        for seg in grupo:
            for chip_v, poly in vecinos:
                frac = _frac_dentro(seg["line"], poly, tol_vecino)
                if frac >= MIN_FRACCION_VECINO:
                    seg_vecinos.setdefault(seg["id"], [])
                    if chip_v not in seg_vecinos[seg["id"]]:
                        seg_vecinos[seg["id"]].append(chip_v)
                    t = _posicion_media(seg["line"], poly)
                    shared = round(frac * seg["longitud_m"], 2)
                    if chip_v not in colindantes:
                        colindantes[chip_v] = {"chip": chip_v, "seg_min": seg["id"], "t": t,
                                               "longitud_colindancia_m": shared}
                    else:
                        colindantes[chip_v]["longitud_colindancia_m"] = round(
                            colindantes[chip_v]["longitud_colindancia_m"] + shared, 2)
                        if seg["id"] < colindantes[chip_v]["seg_min"]:
                            colindantes[chip_v]["seg_min"] = seg["id"]
                            colindantes[chip_v]["t"] = t

        # clasificación del frente (precedencia: via > espacio_publico > predio > libre)
        if frac_via >= MIN_FRACCION_VIA:
            frente = "via"
        elif frac_ep >= MIN_FRACCION_EP:
            frente = "espacio_publico"
        elif colindantes:
            frente = "predio"
        else:
            frente = "libre"

        vecinos_out = []
        if frente == "predio":
            ordenados = sorted(colindantes.values(), key=lambda vv: (vv["seg_min"], vv["t"]))
            for k, vv in enumerate(ordenados, start=1):
                vecinos_out.append({
                    "chip": vv["chip"],
                    "nombre": "%s%d" % (card, k),
                    "longitud_colindancia_m": vv["longitud_colindancia_m"],
                    "altura_m": None,
                    "pisos": None,
                })
            total_predios += len(vecinos_out)

        lados_out.append({
            "cardinal": card,
            "frente": frente,
            "frente_fuente": "auto",
            "frente_override": None,
            "azimut_grados": round(grupo[0]["azimut_grados"], 1),
            "segmentos": [g["id"] for g in grupo],
            "segmentos_vecinos": ({str(k): v for k, v in seg_vecinos.items()} if frente == "predio" else {}),
            "longitud_m": round(longitud_total, 2),
            "n_vecinos": len(vecinos_out),
            "vecinos": vecinos_out,
        })

    return {
        "chip": chip,
        "crs": crs,
        "azimuth_norte_grados": azimuth,
        "n_lados": len(lados_out),
        "n_predios_colindantes": total_predios,
        "nota": ("Clasificación automática (frente_fuente='auto'). Las vías provienen de "
                 "vias_oficiales (Eje_vial, INCOMPLETO: calles no digitalizadas pueden quedar "
                 "como 'predio'); algunas zonas verdes están en 'vecinos' y no en "
                 "'espacios_publicos'. El operador debe confirmar/corregir 'frente' por lado "
                 "(frente_override)."),
        "lados": lados_out,
    }


def a_normativa_vecinos_por_lado(clasificacion: Dict) -> Dict:
    """Convierte la clasificación (con alturas ya llenadas por el operador) al
    formato vecinos_por_lado_json de F1_ETAPA2_NORMATIVA_v08: {id_lado: [altura_m, ...]}.
    Solo incluye lados 'predio'; id_lado = índice de segmento del polígono."""
    result: Dict[str, List[float]] = {}
    for lado in clasificacion.get("lados", []):
        if lado.get("frente") != "predio":
            continue
        altura_por_chip: Dict[str, float] = {}
        for v in lado.get("vecinos", []):
            h = v.get("altura_m")
            if h is None:
                continue
            try:
                altura_por_chip[v["chip"]] = float(h)
            except (TypeError, ValueError):
                pass
        if not altura_por_chip:
            continue
        seg_vec = lado.get("segmentos_vecinos", {})
        for seg_id in lado.get("segmentos", []):
            chips = seg_vec.get(str(seg_id), [])
            alturas = [altura_por_chip[c] for c in chips if c in altura_por_chip]
            if alturas:
                result[str(seg_id)] = alturas
    return result


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
    io.open(out, "w", encoding="utf-8").write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print("OK -> %s (%d lados, %d predios colindantes)" % (
        out, result.get("n_lados", 0), result.get("n_predios_colindantes", 0)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
