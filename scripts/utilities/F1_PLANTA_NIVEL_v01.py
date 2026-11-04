# -*- coding: utf-8 -*-
"""
F1_PLANTA_NIVEL_v01.py - Vista EN PLANTA del lote con bloques sobre cotas del MDT.

Que resuelve
------------
Produce el payload que alimenta la vista EN PLANTA interactiva del formulario web
(seccion 4b: asignacion de bloques y alturas). Muestra:

  * perimetro del lote con el MISMO color por lado que la vista frontal
  * vertices del lote con su cota estimada del MDT (z_local + z_ref = MSNM)
  * bloques B1..Bn como poligonos con su ID, color propio, cota z_base y
    z_terreno_medio (cota estimada del terreno bajo cada bloque)
  * franja de calle / vias de acceso
  * marco de coordenadas local (x, y) para leer posiciones
  * datos coherentes con la vista frontal (misma paleta, mismos lados)

Entradas (CLI)
--------------
--chip   CHIP del predio (obligatorio).
--mdt    'malla' (IDW ETAPA1) o 'rest' (MDT Catastro).
--json   imprime el payload completo.
--salida ruta del JSON de salida (opcional).

Salidas (payload)
-----------------
lote{vertices[], lados[]}, bloques[{id, poligono[], z_base_m, z_terreno_medio_m,
                                     pisos, area_m2, ancho_m, color}],
vias[{polyline[], nombre, ancho}], marco{z_ref, origen}, avisos[]
"""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import io
import json
import math
import os
import re
import sys
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
POT_CACHE = os.path.join(RAIZ, "data", "pot-cache")
POT_BOGOTA = os.path.join(RAIZ, "data", "pot-bogota")
EPS = 1e-6

# Misma paleta que F1_FRONTAL_NIVEL_v01 para coherencia visual entre alzado y planta.
PALETA_FRENTE = {"via": "#2563eb", "via_no_frontal": "#60a5fa", "predio": "#d97706",
                 "espacio_publico": "#16a34a", "libre": "#9ca3af", "indefinido": "#9ca3af"}
ETIQUETA_FRENTE = {"via": "via (frontal)", "via_no_frontal": "via (no frontal)",
                   "predio": "predio / vecino", "espacio_publico": "espacio publico",
                   "libre": "libre", "indefinido": "indefinido"}
COL_LOTE = "#d97706"

# Rango valido de altura de entrepiso en Bogota (m).
ENTREPISO_MIN_M = 2.20
ENTREPISO_MAX_M = 3.80
ENTREPISO_DEFECTO_M = 3.00
RUTA_NIVELES_BLOQUE = os.path.join(POT_BOGOTA, "niveles-bloque-override.json")

COL_BLOQUE_BASE = ["#1f6feb", "#0e7490", "#b45309", "#4d7c0f", "#6d28d9", "#b42318",
                   "#16a34a", "#d97706", "#64748b", "#0891b2"]
COL_CALLE = "#1f6feb"
COL_VERTEX = "#b8860b"


def _cargar_modulo(ruta: str, nombre: str):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    if spec is None or spec.loader is None:
        raise RuntimeError("no se pudo cargar %s" % ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_ALZADO = None


def _alzado():
    global _ALZADO
    if _ALZADO is None:
        ruta = os.path.join(RAIZ, "scripts", "utilities", "generar-alzado-via.py")
        _ALZADO = _cargar_modulo(ruta, "generar_alzado_via")
    return _ALZADO


def _json(ruta: Optional[str], defecto: Any = None) -> Any:
    if not ruta:
        return defecto
    try:
        with io.open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return defecto


def ruta_contexto(chip: str) -> str:
    return os.path.join(POT_CACHE, chip + "-contexto.json")


def ruta_vecinos_por_lado(chip: str) -> Optional[str]:
    ov = os.path.join(POT_CACHE, chip + "-vecinos-por-lado-override.json")
    auto = os.path.join(POT_CACHE, chip + "-vecinos-por-lado.json")
    if os.path.isfile(ov):
        return ov
    return auto if os.path.isfile(auto) else None


def ruta_bloques(chip: str) -> Optional[str]:
    for p in (os.path.join(RAIZ, "src", "fase-3-masa", "casos", chip, "bloques.json"),
              os.path.join(POT_CACHE, chip + "-bloques.json")):
        if os.path.isfile(p):
            return p
    return None


def _sub(a: Sequence[float], b: Sequence[float]) -> Tuple[float, float]:
    return (float(a[0]) - float(b[0]), float(a[1]) - float(b[1]))


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return float(a[0]) * float(b[0]) + float(a[1]) * float(b[1])


def _unit(v: Sequence[float]) -> Tuple[float, float]:
    n = math.hypot(float(v[0]), float(v[1]))
    return (float(v[0]) / n, float(v[1]) / n) if n > 1e-9 else (0.0, 0.0)


def _punto_en_poligono(x: float, y: float, ring: Sequence[Sequence[float]]) -> bool:
    dentro = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = float(ring[i][0]), float(ring[i][1])
        xj, yj = float(ring[j][0]), float(ring[j][1])
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) or EPS) + xi):
            dentro = not dentro
        j = i
    return dentro


def _dist_punto_seg(p: Sequence[float], a: Sequence[float], b: Sequence[float]) -> float:
    ax, ay, bx, by = float(a[0]), float(a[1]), float(b[0]), float(b[1])
    vx, vy = bx - ax, by - ay
    l2 = vx * vx + vy * vy
    if l2 <= 1e-12:
        return math.hypot(float(p[0]) - ax, float(p[1]) - ay)
    t = max(0.0, min(1.0, ((float(p[0]) - ax) * vx + (float(p[1]) - ay) * vy) / l2))
    return math.hypot(float(p[0]) - (ax + t * vx), float(p[1]) - (ay + t * vy))


def _dist_anillo_lote(ring: Sequence[Sequence[float]],
                      lote_xy: Sequence[Sequence[float]]) -> float:
    mejor = 1e9
    n = len(lote_xy)
    for p in ring:
        for k in range(n):
            d = _dist_punto_seg(p, lote_xy[k], lote_xy[(k + 1) % n])
            if d < mejor:
                mejor = d
    return mejor


def _lados_lote(chip: str, lote: List[List[float]]) -> List[Dict[str, Any]]:
    """Lados agrupados del predio (los mismos de la vista frontal)."""
    n = len(lote)
    vpl = _json(ruta_vecinos_por_lado(chip), {}) or {}
    lados: List[Dict[str, Any]] = []
    for k, lado in enumerate(vpl.get("lados") or []):
        segs: List[int] = []
        for s in (lado.get("segmentos") or []):
            try:
                segs.append(int(s) % n)
            except Exception:
                continue
        if not segs:
            continue
        poly = [lote[s] for s in segs] + [lote[(segs[-1] + 1) % n]]
        largo = sum(math.hypot(lote[s][0] - lote[(s + 1) % n][0],
                               lote[s][1] - lote[(s + 1) % n][1]) for s in segs)
        frente = (lado.get("frente_override") or lado.get("frente") or "indefinido")
        lados.append({
            "lado_id": int(lado.get("lado_id", k)),
            "cardinal": lado.get("cardinal"),
            "cardinal_label": lado.get("cardinal_label") or lado.get("cardinal"),
            "frente": frente,
            "color": PALETA_FRENTE.get(frente, "#9ca3af"),
            "etiqueta": ETIQUETA_FRENTE.get(frente, frente),
            "longitud_m": round(largo, 2),
            "segmentos": segs,
            "polyline": [[round(float(p[0]), 3), round(float(p[1])), round(float(p[2]), 3)]
                         for p in poly],
            "vecinos": lado.get("vecinos") or [],
        })
    if lados:
        return lados

    # Respaldo: una arista por lado.
    for i in range(n):
        a, b = lote[i], lote[(i + 1) % n]
        largo = math.hypot(b[0] - a[0], b[1] - a[1])
        if largo < 0.5:
            continue
        lados.append({"lado_id": i, "cardinal": None, "cardinal_label": "arista %d" % i,
                      "frente": "indefinido", "color": PALETA_FRENTE["indefinido"],
                      "etiqueta": "indefinido", "longitud_m": round(largo, 2),
                      "segmentos": [i],
                      "polyline": [[a[0], a[1], a[2]], [b[0], b[1], b[2]]], "vecinos": []})
    return lados


def _elegir_frente(chip: str, lados: List[Dict[str, Any]],
                   ctx: Dict[str, Any], lado_id: Optional[int]) -> Tuple[Dict[str, Any], str]:
    """Lado FRONTAL: parametro > calle de acceso > clasificado 'via'."""
    if lado_id is not None:
        for l in lados:
            if int(l["lado_id"]) == int(lado_id):
                return l, "seleccion del operador"
        for l in lados:
            if int(lado_id) in (l.get("segmentos") or []):
                return l, "seleccion del operador (segmento)"

    bloques = _json(ruta_bloques(chip), {}) or {}
    calle = (bloques.get("orientacion") or {}).get("calle_acceso") or {}
    if calle.get("lado_id") is not None:
        for l in lados:
            if int(l["lado_id"]) == int(calle["lado_id"]):
                return l, "calle de acceso del modelado (%s)" % (calle.get("cardinal_label") or "")

    vias = [l for l in lados if l.get("frente") == "via"]
    if len(vias) == 1:
        return vias[0], "clasificacion de la planta (via)"
    if len(vias) > 1:
        def clave(l: Dict[str, Any]):
            pts = l.get("polyline") or []
            mid = pts[len(pts) // 2] if pts else [0, 0]
            return (_dist_a_vias(mid, ctx), -float(l.get("longitud_m") or 0))
        return sorted(vias, key=clave)[0], "clasificacion de la planta (via, la mas cercana al eje)"

    mejor, mejor_d = lados[0], 1e9
    for l in lados:
        pts = l.get("polyline") or []
        mid = pts[len(pts) // 2] if pts else [0, 0]
        d = _dist_a_vias(mid, ctx)
        if d < mejor_d:
            mejor, mejor_d = l, d
    return mejor, "arista mas cercana a una via"


def _dist_a_vias(punto: Sequence[float], ctx: Dict[str, Any]) -> float:
    mejor = 1e9
    for v in ctx.get("vias_oficiales") or []:
        pts = v.get("coordenadas_local") or []
        for k in range(len(pts) - 1):
            d = _dist_punto_seg(punto, pts[k], pts[k + 1])
            if d < mejor:
                mejor = d
    return mejor


def _idw_z(malla: List[Tuple[float, float, float]], x: float, y: float) -> Tuple[Optional[float], bool]:
    """IDW simple sobre malla de terreno. Devuelve (z, dentro)."""
    alz = _alzado()
    try:
        z, dentro = alz.idw(malla, x, y)
        return z, dentro
    except Exception:
        return None, False



def _pisos_de_rango(rango: Any) -> Optional[int]:
    """Extrae el maximo de pisos desde 'rango_edificabilidad' del POT.

    Acepta valores como "4", "1-4", "1 a 4", "4 pisos", "hasta 4".
    Devuelve None si no se puede interpretar.
    """
    if rango is None:
        return None
    txt = str(rango).strip().lower()
    if not txt:
        return None
    nums = re.findall(r"\d+", txt)
    if not nums:
        return None
    try:
        return int(max(int(n) for n in nums))
    except Exception:
        return None


def _norma_chip(ctx: Dict[str, Any]) -> Dict[str, Any]:
    """Tope normativo de edificabilidad del predio (POT)."""
    pot = ctx.get("pot_data") or ctx.get("pot") or {}
    pisos_max = _pisos_de_rango(pot.get("rango_edificabilidad"))
    altura_max = pot.get("altura_maxima_m")
    try:
        altura_max = float(altura_max) if altura_max is not None else None
    except Exception:
        altura_max = None
    return {
        "rango_edificabilidad": pot.get("rango_edificabilidad"),
        "pisos_max": pisos_max,
        "altura_max_m": altura_max,
        "altura_max_pzcb_m": pot.get("altura_maxima_m_referencia_pzcb"),
        "io_maximo": pot.get("io_maximo"),
        "ic_maximo": pot.get("ic_maximo"),
        "tratamiento": pot.get("tratamiento"),
        "upz": pot.get("upz"),
        "fuente": "contexto.pot",
    }



def _niveles_bloque_chip(chip: str) -> Dict[str, Any]:
    """Configuracion de alturas de entrepiso por bloque (override del operador)."""
    data = _json(RUTA_NIVELES_BLOQUE, {}) or {}
    cfg = data.get(chip)
    return cfg if isinstance(cfg, dict) else {}


def _entrepiso_de_bloque(cfg: Dict[str, Any], bloque_id: str) -> Dict[str, Any]:
    """Alturas de entrepiso aplicables a un bloque segun los grupos G1..Gn.

    Devuelve {"alturas": [...], "entrepiso_m": float, "fuente": str}.
    """
    alturas: List[float] = []
    fuente = "sin configuracion (default %.2f m)" % ENTREPISO_DEFECTO_M
    if cfg:
        grupos = cfg.get("grupos") or {}
        por_grupo = cfg.get("alturas_por_grupo") or {}
        for gid, bloques in grupos.items():
            if bloque_id in (bloques or []):
                alturas = [float(a) for a in (por_grupo.get(gid) or []) if a]
                if alturas:
                    fuente = "grupo %s" % gid
                break
        if not alturas and cfg.get("modo") == "iguales":
            for gid, lst in por_grupo.items():
                vals = [float(a) for a in (lst or []) if a]
                if vals:
                    alturas = vals
                    fuente = "grupo %s (modo iguales)" % gid
                    break
    if not alturas:
        return {"alturas": [ENTREPISO_DEFECTO_M], "entrepiso_m": ENTREPISO_DEFECTO_M,
                "fuente": fuente}
    alturas = [min(max(a, ENTREPISO_MIN_M), ENTREPISO_MAX_M) for a in alturas]
    prom = sum(alturas) / len(alturas)
    return {"alturas": alturas, "entrepiso_m": round(prom, 3), "fuente": fuente}


def _color_bloque(idx: int) -> str:
    return COL_BLOQUE_BASE[idx % len(COL_BLOQUE_BASE)]


def construir(chip: str, lado_id: Optional[int] = None, mdt: str = "malla") -> Dict[str, Any]:
    chip = (chip or "").strip().upper()
    ctx = _json(ruta_contexto(chip))
    if not ctx:
        raise SystemExit("No existe %s" % ruta_contexto(chip))

    lote: List[List[float]] = []
    for v in (ctx.get("lote_objetivo", {}) or {}).get("vertices_3d_local") or []:
        p = [float(v[0]), float(v[1])]
        p.append(float(v[2]) if len(v) > 2 else 0.0)
        lote.append(p)
    if len(lote) > 1 and abs(lote[0][0] - lote[-1][0]) < 1e-4 and abs(lote[0][1] - lote[-1][1]) < 1e-4:
        lote = lote[:-1]
    if len(lote) < 3:
        raise SystemExit("Lote sin vertices suficientes")

    malla = [(float(p["x_local"]), float(p["y_local"]), float(p["z_local"]))
             for p in ((ctx.get("topografia") or {}).get("malla_terreno") or [])]
    z_ref = float(((ctx.get("metadata") or {}).get("origen_sirgas") or {}).get("z", 0.0) or 0.0)

    lados = _lados_lote(chip, lote)
    frente, origen_frente = _elegir_frente(chip, lados, ctx, lado_id)
    p0 = frente["polyline"][0]
    p1 = frente["polyline"][-1]
    eje = _unit(_sub(p1, p0))
    normal = (-eje[1], eje[0])

    # --- Vertices del lote con cotas estimadas del MDT ---
    lote_vertices: List[Dict[str, Any]] = []
    for k, v in enumerate(lote):
        z, dentro = _idw_z(malla, float(v[0]), float(v[1]))
        if z is None:
            z = float(v[2]) if len(v) > 2 and v[2] is not None else 0.0
            fuente = "vertice lote (fallback)"
            estimado = True
        else:
            fuente = "IDW malla ETAPA1" if mdt == "malla" else "MDT REST"
            estimado = not dentro
        lote_vertices.append({
            "id": "V%d" % (k + 1),
            "x": round(float(v[0]), 3),
            "y": round(float(v[1]), 3),
            "z": round(float(z), 3),
            "msnm": round(float(z) + z_ref, 2),
            "estimado": estimado,
            "fuente": fuente,
        })

    # --- Lados proyectados con coordenadas y cota media ---
    for l in lados:
        pts = l["polyline"]
        zs = [float(q[2]) for q in pts]
        l["z_min"] = round(min(zs), 2)
        l["z_max"] = round(max(zs), 2)
        l["z_media"] = round(sum(zs) / len(zs), 2)
        l["x_min"] = round(min(float(q[0]) for q in pts), 2)
        l["x_max"] = round(max(float(q[0]) for q in pts), 2)
        l["y_min"] = round(min(float(q[1]) for q in pts), 2)
        l["y_max"] = round(max(float(q[1]) for q in pts), 2)

    # --- Bloques desde bloques.json ---
    bloques_data = _json(ruta_bloques(chip), {}) or {}
    norma = _norma_chip(ctx)
    niveles_cfg = _niveles_bloque_chip(chip)
    bloques_lista: List[Dict[str, Any]] = []
    for idx, b in enumerate((bloques_data.get("bloques") or [])[:20]):
        poligono = b.get("poligono_local") or []
        if len(poligono) < 3:
            continue
        # Cota del terreno bajo el bloque: usar z_terreno_medio o interpolar del MDT
        z_terreno = float(b.get("z_terreno_medio_m") or 0.0)
        z_base = float(b.get("z_base_m") or 0.0)
        if poligono:
            cx = sum(float(p[0]) for p in poligono) / len(poligono)
            cy = sum(float(p[1]) for p in poligono) / len(poligono)
        else:
            cx, cy = 0.0, 0.0
        # Estimar z del terreno en el centroide del poligono si no hay dato
        if z_terreno == 0.0 and poligono:
            zt, _ = _idw_z(malla, cx, cy)
            if zt is not None:
                z_terreno = float(zt)
        _bid = b.get("id") or "B%d" % (idx + 1)
        _ent = _entrepiso_de_bloque(niveles_cfg, _bid)
        # Pisos: prima el rango de edificabilidad (numero de pisos). La altura
        # reglamentaria NO limita pisos: se controla como ADVERTENCIA sobre el MDT.
        _pisos_orig = int(b.get("pisos") or 0)
        _pisos_ef = _pisos_orig
        _pmax = norma.get("pisos_max")
        if _pmax:
            _pisos_ef = min(_pisos_ef, int(_pmax))
        _amax = norma.get("altura_max_m")
        if _pisos_ef < 1:
            _pisos_ef = 1
        # Altura del bloque = pisos efectivos x entrepiso (SIN recortar por altura:
        # el limite de altura es una cota sobre el MDT, no un tope de pisos).
        _alt_bloque = round(_ent["entrepiso_m"] * _pisos_ef, 3)

        # --- Terreno en 3 puntos de la franja: norte, centro y sur ---
        _terr3 = {"norte": None, "centro": None, "sur": None}
        _alt3 = {"norte": None, "centro": None, "sur": None}
        if poligono:
            _p_norte = max(poligono, key=lambda q: float(q[1]))
            _p_sur = min(poligono, key=lambda q: float(q[1]))
            _pts3 = {
                "norte": (float(_p_norte[0]), float(_p_norte[1])),
                "centro": (cx, cy),
                "sur": (float(_p_sur[0]), float(_p_sur[1])),
            }
            # Tope del bloque en MSNM = z_base (local) + altura + z_ref.
            # OJO: z_terreno_medio_m YA viene en MSNM (no sumarle z_ref).
            _z_top_msnm = float(z_base) + _alt_bloque + z_ref
            for _k, (_px, _py) in _pts3.items():
                _zt, _dentro = _idw_z(malla, _px, _py)
                if _zt is None:
                    _zmsnm = round(float(z_terreno), 2)   # ya es MSNM
                else:
                    _zmsnm = round(float(_zt) + z_ref, 2)  # malla local -> MSNM
                _terr3[_k] = _zmsnm
                _alt3[_k] = round(_z_top_msnm - _zmsnm, 2)
        _vals_alt = [v for v in _alt3.values() if v is not None]
        _alt3["max"] = round(max(_vals_alt), 2) if _vals_alt else None
        _alt3["min"] = round(min(_vals_alt), 2) if _vals_alt else None
        _excede_alt = None
        _adv_alt = None
        if _amax and _alt3.get("max") is not None:
            _dif = round(_alt3["max"] - float(_amax), 2)
            _excede_alt = _dif
            if _dif > 0.01:
                _adv_alt = ("ADVERTENCIA: la altura sobre el MDT llega a %.2f m en el punto "
                            "mas alto de la franja; el limite reglamentario es %.2f m "
                            "(excede %.2f m). Reprocesar con menor entrepiso."
                            % (_alt3["max"], float(_amax), _dif))
        bloques_lista.append({
            "id": _bid,
            "orden": int(b.get("orden") or idx + 1),
            "poligono": [[round(float(p[0]), 3), round(float(p[1]), 3)] for p in poligono],
            "area_m2": round(float(b.get("area_lote_m2") or 0.0), 2),
            "ancho_m": round(float(b.get("ancho_m") or 0.0), 2),
            "pisos": int(b.get("pisos") or 0),
            "z_base_m": round(z_base, 3),
            "z_terreno_medio_m": round(z_terreno, 3),
            "z_terreno_msnm": round(z_terreno + z_ref, 2),
            "gfa_objetivo_m2": round(float(b.get("gfa_objetivo_m2") or 0.0), 2),
            "color": _color_bloque(idx),
            "centroide": [round(cx, 2), round(cy, 2)] if poligono else [0, 0],
            "alturas_entrepiso_m": _ent["alturas"],
            "altura_entrepiso_m": _ent["entrepiso_m"],
            "entrepiso_fuente": _ent["fuente"],
            "pisos_efectivos": _pisos_ef,
            "altura_bloque_m": _alt_bloque,
            "terreno_msnm": _terr3,
            "altura_sobre_mdt_m": _alt3,
            "altura_max_sobre_mdt_m": _alt3.get("max"),
            "excede_altura_m": _excede_alt,
            "advertencia_altura": _adv_alt,
            "pisos_norma": norma.get("pisos_max"),
            "excede_pisos": bool(norma.get("pisos_max") is not None
                                 and int(b.get("pisos") or 0) > int(norma["pisos_max"])),
        })

    # --- Vias de acceso ---
    vias: List[Dict[str, Any]] = []
    for v in (ctx.get("vias_oficiales") or [])[:8]:
        coords = v.get("coordenadas_local") or []
        if len(coords) < 2:
            continue
        vias.append({
            "nombre": v.get("nombre") or v.get("codigo") or "via",
            "tipo_via": v.get("tipo_via"),
            "polyline": [[round(float(p[0]), 2), round(float(p[1]), 2)] for p in coords],
        })

    avisos: List[str] = []
    estimados_lote = sum(1 for v in lote_vertices if v.get("estimado"))
    if estimados_lote:
        avisos.append("%d de %d vertices del lote con cota extrapolada (fuera de malla ETAPA1)."
                      % (estimados_lote, len(lote_vertices)))
    if not bloques_lista:
        avisos.append("No se encontro bloques.json para este chip. Generar bloques en la seccion 4b.")

    return {
        "schema": "f1_planta_nivel_v01",
        "chip": chip,
        "generado": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "mdt": mdt,
        "z_ref": round(z_ref, 3),
        "origen_frente": origen_frente,
        "lado_frontal": frente["lado_id"],
        "lote": {
            "vertices": lote_vertices,
            "lados": lados,
            "area_m2": round(
                abs(sum(float(lote[i][0]) * float(lote[(i + 1) % len(lote)][1]) -
                        float(lote[(i + 1) % len(lote)][0]) * float(lote[i][1])
                        for i in range(len(lote))) / 2.0), 2),
        },
        "bloques": bloques_lista,
        "norma": norma,
        "niveles_bloque": niveles_cfg,
        "entrepiso_rango_m": {"min": ENTREPISO_MIN_M, "max": ENTREPISO_MAX_M,
                              "defecto": ENTREPISO_DEFECTO_M},
        "vias": vias,
        "marco": {
            "origen_x": round(float(p0[0]), 2),
            "origen_y": round(float(p0[1]), 2),
            "eje_x": round(eje[0], 4),
            "eje_y": round(eje[1], 4),
            "normal_x": round(normal[0], 4),
            "normal_y": round(normal[1], 4),
        },
        "avisos": avisos,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Vista en planta del lote con bloques y cotas MDT")
    ap.add_argument("--chip", required=True)
    ap.add_argument("--lado", type=int, default=None)
    ap.add_argument("--mdt", default="malla", choices=["malla", "rest"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--salida", default=None)
    args = ap.parse_args()
    try:
        datos = construir(args.chip, args.lado, args.mdt)
    except SystemExit as e:
        print(str(e))
        sys.exit(1)
    if args.json or args.salida:
        txt = json.dumps(datos, ensure_ascii=False, indent=2)
        if args.salida:
            with io.open(args.salida, "w", encoding="utf-8") as f:
                f.write(txt)
            print("Escrito %s" % args.salida)
        else:
            print(txt)
    else:
        print("Planta de %s: %d bloques, %d vertices de lote, z_ref=%s"
              % (args.chip, len(datos["bloques"]), len(datos["lote"]["vertices"]),
                 datos["z_ref"]))


if __name__ == "__main__":
    main()
