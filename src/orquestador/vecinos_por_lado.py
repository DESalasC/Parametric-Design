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
MIN_EP_OVERLAP_M2 = 5.0       # 2026-09-28: overlap maximo lote-EP para que el EP cuente como frente
TOL_COLINEAR_GRADOS = 10.0   # aristas consecutivas colineales se funden en un lado

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


def _agrupar_lados(segments: List[Dict]) -> List[List[Dict]]:
    """Agrupa aristas consecutivas y colineales en lados (corridas de aristas).

    Reemplaza el agrupamiento por cardinal: dos tramos del mismo cardinal pero
    NO adyacentes quedan en lados separados (p. ej. Norte-1 y Norte-2).
    """
    if not segments:
        return []
    m = len(segments)

    def _dir(seg):
        return seg["dir_az"] % 180.0

    def _colineal(a, b):
        d = abs(_dir(a) - _dir(b)) % 180.0
        return min(d, 180.0 - d) <= TOL_COLINEAR_GRADOS

    # rotar para que una corrida no cruce el cierre del poligono
    start = 0
    for i in range(m):
        if not _colineal(segments[i], segments[(i + 1) % m]):
            start = (i + 1) % m
            break
    orden = [segments[(start + k) % m] for k in range(m)]
    grupos: List[List[Dict]] = []
    for seg in orden:
        if grupos and _colineal(grupos[-1][-1], seg):
            grupos[-1].append(seg)
        else:
            grupos.append([seg])
    grupos.sort(key=lambda g: g[0]["id"])
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
        return {"chip": chip, "error": "lote sin v\u00e9rtices suficientes", "lados": []}
    if pts[0] != pts[-1]:
        pts.append(pts[0])
    n = len(pts) - 1

    lot_poly = Polygon(pts)
    if not lot_poly.is_valid:
        lot_poly = lot_poly.buffer(0)
    centroid = (lot_poly.centroid.x, lot_poly.centroid.y)

    # geometr\u00edas de v\u00edas y espacios p\u00fablicos (uni\u00f3n para consulta r\u00e1pida)
    via_geoms: List[LineString] = []
    for v in contexto.get("vias_oficiales", []):
        cl = v.get("coordenadas_local", [])
        if len(cl) >= 2:
            via_geoms.append(LineString([(float(x), float(y)) for x, y, _z in cl]))
    vias = unary_union(via_geoms) if via_geoms else None

    # 2026-09-28: un espacio publico que CUBRE/CRUZA el lote (p. ej. "Parque
    # Pueblo Viejo", estructurante PROPUESTO con fragmentos sobre el predio) no
    # es un "frente" del lote y sesga la clasificacion -> se ignora (overlap).
    ep_polys: List[Polygon] = []
    eps_ignorados: List[str] = []
    for e in contexto.get("espacios_publicos", []):
        p = _poly2d(e.get("coordenadas_local", []))
        if p is None:
            continue
        try:
            if p.intersection(lot_poly).area > MIN_EP_OVERLAP_M2:
                eps_ignorados.append(str(e.get("nombre", "")))
                continue
        except Exception:
            pass
        ep_polys.append(p)
    eps = unary_union(ep_polys) if ep_polys else None

    vecinos: List[Tuple[str, Polygon, Optional[float], Optional[int]]] = []
    for v in contexto.get("vecinos", []):
        p = _poly2d(v.get("vertices_3d_local", []))
        if p is not None:
            vecinos.append((v.get("chip", ""), p, v.get("altura_m"), v.get("pisos")))

    # segmentos del lote + fracciones de contacto + direcci\u00f3n (para colinealidad)
    segments: List[Dict] = []
    for i in range(n):
        p1 = pts[i]
        p2 = pts[i + 1]
        line = LineString([p1, p2])
        nx, ny = _normal_saliente(p1, p2, centroid)
        az = azimut(nx, ny)
        dir_az = azimut(p2[0] - p1[0], p2[1] - p1[1])
        segments.append({
            "id": i,
            "cardinal": cardinal(az),
            "azimut_grados": az,
            "dir_az": dir_az,
            "line": line,
            "longitud_m": line.length,
            "frac_via": _frac_dentro(line, vias, tol_via),
            "frac_ep": _frac_dentro(line, eps, tol_ep),
        })

    lados_out: List[Dict] = []
    colindantes_global: Dict[str, float] = {}
    for grupo in _agrupar_lados(segments):
        card = grupo[0]["cardinal"]
        longitud_total = sum(g["longitud_m"] for g in grupo) or 1.0
        frac_via = sum(g["frac_via"] * g["longitud_m"] for g in grupo) / longitud_total
        frac_ep = sum(g["frac_ep"] * g["longitud_m"] for g in grupo) / longitud_total

        # vecinos colindantes por segmento (dedupe por chip)
        colindantes: Dict[str, Dict] = {}
        seg_vecinos: Dict[int, List[str]] = {}
        for seg in grupo:
            for chip_v, poly, _h, _p in vecinos:
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

        # clasificaci\u00f3n del frente (precedencia: via > espacio_publico > predio > libre)
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
                # Buscar altura/pisos del vecino en los datos de contexto (geobase)
                altura_m = None
                pisos = None
                for vchip, _vpoly, v_altura, v_pisos in vecinos:
                    if vchip == vv["chip"]:
                        altura_m = v_altura
                        pisos = v_pisos
                        break
                vecinos_out.append({
                    "chip": vv["chip"],
                    "nombre": "%s%d" % (card, k),
                    "longitud_colindancia_m": vv["longitud_colindancia_m"],
                    "altura_m": altura_m,
                    "pisos": pisos,
                })
                colindantes_global[vv["chip"]] = colindantes_global.get(vv["chip"], 0.0) + vv["longitud_colindancia_m"]

        lados_out.append({
            "lado_id": grupo[0]["id"],
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

    # cardinal_label desambiguado (Norte, Norte-1, ...) sin romper "cardinal" base
    conteo: Dict[str, int] = {}
    for l in lados_out:
        conteo[l["cardinal"]] = conteo.get(l["cardinal"], 0) + 1
    vistos: Dict[str, int] = {}
    for l in lados_out:
        base = l["cardinal"]
        if conteo[base] > 1:
            vistos[base] = vistos.get(base, 0) + 1
            l["cardinal_label"] = "%s-%d" % (base, vistos[base])
        else:
            l["cardinal_label"] = base

    return {
        "chip": chip,
        "crs": crs,
        "azimuth_norte_grados": azimuth,
        "n_lados": len(lados_out),
        "n_predios_colindantes": len(colindantes_global),
        "eps_ignorados": eps_ignorados,
        "colindantes": [{"chip": cv, "longitud_colindancia_total_m": round(ln, 2)}
                        for cv, ln in sorted(colindantes_global.items())],
        "nota": ("Clasificaci\u00f3n autom\u00e1tica (frente_fuente='auto'). Las v\u00edas provienen de "
                 "vias_oficiales (Eje_vial, INCOMPLETO: calles no digitalizadas pueden quedar "
                 "como 'predio'); algunas zonas verdes est\u00e1n en 'vecinos' y no en "
                 "'espacios_publicos'. El operador debe confirmar/corregir 'frente' por lado "
                 "(frente_override)."),
        "lados": lados_out,
    }


def a_normativa_vecinos_por_lado(clasificacion: Dict) -> Dict:
    """Convierte la clasificación (con confirmación + alturas del operador) al
    formato vecinos_por_lado_json de F1_ETAPA2_NORMATIVA_v08: {id_lado: [altura_m, ...]}.
    Respeta: frente efectivo (override), confirmacion, flag 'corresponde' por vecino
    y vecinos_manuales (asignados al primer segmento del lado)."""
    result: Dict[str, List[float]] = {}
    for lado in clasificacion.get("lados", []):
        if not isinstance(lado, dict):
            continue
        frente = lado.get("frente_override") or lado.get("frente")
        if frente != "predio":
            continue
        if lado.get("confirmacion") == "no_es_predio":
            continue
        altura_por_chip: Dict[str, float] = {}
        for v in lado.get("vecinos", []):
            if not isinstance(v, dict):
                continue
            if v.get("corresponde") is False:
                continue
            h = v.get("altura_m")
            if h is None:
                continue
            try:
                altura_por_chip[v.get("chip")] = float(h)
            except (TypeError, ValueError):
                pass
        manuales: List[float] = []
        for v in lado.get("vecinos_manuales", []):
            if not isinstance(v, dict):
                continue
            h = v.get("altura_m")
            if h is None:
                continue
            try:
                manuales.append(float(h))
            except (TypeError, ValueError):
                pass
        if not altura_por_chip and not manuales:
            continue
        seg_vec = lado.get("segmentos_vecinos", {}) or {}
        segmentos = lado.get("segmentos", [])
        for seg_id in segmentos:
            chips = seg_vec.get(str(seg_id), [])
            alturas = [altura_por_chip[c] for c in chips if c in altura_por_chip]
            if manuales:
                alturas.extend(manuales)
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
