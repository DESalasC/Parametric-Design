# -*- coding: utf-8 -*-
"""F1_FRONTAL_NIVEL_v01.py - Vista FRONTAL del lote desde la calle y nivel 0,00.

Que resuelve
------------
El orquestador ya tenia un "alzado sobre la via" estatico. Esta utilidad produce
el payload que alimenta la vista FRONTAL interactiva del formulario web:

  * perfil del lindero frontal y de la franja de calle (cotas locales y MSNM),
  * curvas de nivel del terreno proyectadas sobre el plano de fachada (MSNM),
  * silueta del terreno detras del frente,
  * volumenes de los vecinos inmediatos con su altura en metros y su cota MSNM,
  * perimetro del lote proyectado, con el MISMO color por lado de la planta,
  * niveles de las esquinas del poligono,
  * puntos marcados en planta (maximo 5), proyectados a la fachada con su
    linea vertical de altura maxima reglamentaria,
  * datum vigente (nivel 0,00) y su posicion sobre el frente,
  * banda de altura permitida medida SOBRE EL TERRENO (no sobre el 0,00).

Entradas (CLI)
--------------
--chip        CHIP del predio (obligatorio).
--lado        lado_id de <CHIP>-vecinos-por-lado.json. Si se omite se elige el
              lado clasificado como 'via' (calle frontal) y, si hay varios, el de
              la calle de acceso de bloques.json.
--ancho-via   metros hacia la calle para muestrear la franja de via (3.0).
--mdt         'malla' (IDW de la malla ETAPA1, sin red) o 'rest' (MDT Catastro).
--json        imprime el payload completo.
--salida      ruta del JSON de salida (opcional).

Salidas (payload)
-----------------
frente{...}, lindero[], calle[], esquinas[], curvas[], silueta[], vecinos[],
lados[], altura{}, datum{}, banda{}, puntos[], plano{}, avisos[].

Conexiones
----------
* servidor.py  -> GET /api/frontal?chip=...&lado=...&mdt=...
* index.html / frontal.js -> dibuja la vista y fija el 0,00 (POST /api/z0).

Ultimos tres cambios
--------------------
1. 2026-11-01 v01: creacion. Proyeccion "desde la calle" con espejo automatico,
   curvas de nivel MSNM por marching squares y banda de altura sobre terreno.
2. 2026-11-01 v01.1: puntos P1..P5 persistidos en <CHIP>-frontal.json, con altura
   reglamentaria editable por punto.
3. 2026-11-01 v01.2: seleccion del lado frontal por clasificacion 'via' y
   respaldo por calle de acceso / arista mas cercana a via.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import io
import json
import math
import os
import sys
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
POT_CACHE = os.path.join(RAIZ, "data", "pot-cache")
POT_BOGOTA = os.path.join(RAIZ, "data", "pot-bogota")
MAX_PUNTOS = 5
EPS = 1e-6

PALETA_FRENTE = {"via": "#2563eb", "via_no_frontal": "#60a5fa", "predio": "#d97706",
                 "espacio_publico": "#16a34a", "libre": "#9ca3af",
                 "indefinido": "#9ca3af"}
ETIQUETA_FRENTE = {"via": "via (frontal)", "via_no_frontal": "via (no frontal)",
                   "predio": "predio / vecino", "espacio_publico": "espacio publico",
                   "libre": "libre", "indefinido": "indefinido"}
COLOR_PUNTO = ["#b42318", "#6d28d9", "#0e7490", "#b45309", "#4d7c0f"]
COL_CALLE = "#1f6feb"
COL_TERRENO = "#2da44e"
COL_DATUM = "#b8860b"
COL_BANDA = "#6b7280"


# --------------------------------------------------------------------------- io
def _cargar_modulo(ruta: str, nombre: str):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    if spec is None or spec.loader is None:
        raise RuntimeError("no se pudo cargar %s" % ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_ALZADO = None


def _alzado():
    """Utilidades compartidas del alzado (IDW, MDT REST, lectura JSON)."""
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


def ruta_contexto50(chip: str) -> Optional[str]:
    for nombre in (chip + "-contexto50.json", "contexto50-actual.json"):
        p = os.path.join(POT_CACHE, nombre)
        if os.path.isfile(p):
            return p
    return None


def ruta_vecinos_por_lado(chip: str) -> Optional[str]:
    ov = os.path.join(POT_CACHE, chip + "-vecinos-por-lado-override.json")
    auto = os.path.join(POT_CACHE, chip + "-vecinos-por-lado.json")
    if os.path.isfile(ov):
        return ov
    return auto if os.path.isfile(auto) else None


def ruta_z0(chip: str) -> str:
    return os.path.join(POT_CACHE, chip + "-z0.json")


def ruta_puntos(chip: str) -> str:
    return os.path.join(POT_CACHE, chip + "-frontal.json")


def ruta_mdt_frontal(chip: str) -> str:
    return os.path.join(POT_CACHE, chip + "-frontal-mdt.json")


def ruta_bloques(chip: str) -> Optional[str]:
    for p in (os.path.join(RAIZ, "src", "fase-3-masa", "casos", chip, "bloques.json"),
              os.path.join(POT_CACHE, chip + "-bloques.json")):
        if os.path.isfile(p):
            return p
    return None


def leer_puntos(chip: str) -> Dict[str, Any]:
    """Puntos guardados del frontal (P1..P5) y alturas por punto."""
    d = _json(ruta_puntos(chip), {}) or {}
    pts: List[Dict[str, Any]] = []
    for p in (d.get("puntos") or [])[:MAX_PUNTOS]:
        try:
            pts.append({"id": str(p.get("id") or ""), "x": float(p["x"]), "y": float(p["y"])})
        except Exception:
            continue
    alturas: Dict[str, float] = {}
    for k, v in (d.get("alturas") or {}).items():
        try:
            alturas[str(k)] = float(v)
        except Exception:
            continue
    return {"puntos": pts, "alturas": alturas}


def guardar_puntos(chip: str, puntos: Sequence[Dict[str, Any]],
                   alturas: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
    """Persiste hasta MAX_PUNTOS puntos dentro del lote; devuelve el estado."""
    ctx = _json(ruta_contexto(chip)) or {}
    lote = []
    for v in (ctx.get("lote_objetivo", {}) or {}).get("vertices_3d_local") or []:
        lote.append([float(v[0]), float(v[1])])
    limpios: List[Dict[str, Any]] = []
    vistos = set()
    descartados = 0
    for p in list(puntos):
        try:
            pid = str(p.get("id") or "").strip().upper()
            x = float(p["x"])
            y = float(p["y"])
        except Exception:
            descartados += 1
            continue
        if pid not in ("P1", "P2", "P3", "P4", "P5") or pid in vistos:
            descartados += 1
            continue
        if lote and not _punto_en_poligono(x, y, lote):
            descartados += 1
            continue
        if len(limpios) >= MAX_PUNTOS:
            descartados += 1
            continue
        vistos.add(pid)
        limpios.append({"id": pid, "x": round(x, 4), "y": round(y, 4)})
    alts: Dict[str, float] = {}
    for k, v in (alturas or {}).items():
        if k in vistos:
            try:
                alts[k] = round(float(v), 3)
            except Exception:
                pass
    datos = {"schema": "f1_frontal_puntos_v01", "chip": chip, "max": MAX_PUNTOS,
             "puntos": limpios, "alturas": alts, "descartados": descartados,
             "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
    with io.open(ruta_puntos(chip), "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    return datos


# --------------------------------------------------------------------- geometria
def _sub(a: Sequence[float], b: Sequence[float]) -> Tuple[float, float]:
    return (float(a[0]) - float(b[0]), float(a[1]) - float(b[1]))


def _norm(v: Sequence[float]) -> float:
    return math.hypot(float(v[0]), float(v[1]))


def _unit(v: Sequence[float]) -> Tuple[float, float]:
    n = _norm(v)
    return (float(v[0]) / n, float(v[1]) / n) if n > 1e-9 else (0.0, 0.0)


def _dot(a: Sequence[float], b: Sequence[float]) -> float:
    return float(a[0]) * float(b[0]) + float(a[1]) * float(b[1])


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


def _lados_lote(chip: str, lote: List[List[float]]) -> List[Dict[str, Any]]:
    """Lados agrupados del predio (los mismos de la planta del orquestador)."""
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
            "frente_auto": lado.get("frente"),
            "frente_override": lado.get("frente_override"),
            "color": PALETA_FRENTE.get(frente, "#9ca3af"),
            "etiqueta": ETIQUETA_FRENTE.get(frente, frente),
            "longitud_m": round(largo, 2),
            "segmentos": segs,
            "polyline": [[round(float(p[0]), 3), round(float(p[1]), 3), round(float(p[2]), 3)]
                         for p in poly],
            "vecinos": lado.get("vecinos") or [],
        })
    if lados:
        return lados

    # Respaldo: una arista por lado (predio sin cuadro de lados guardado).
    for i in range(n):
        a, b = lote[i], lote[(i + 1) % n]
        largo = math.hypot(b[0] - a[0], b[1] - a[1])
        if largo < 0.5:
            continue
        lados.append({"lado_id": i, "cardinal": None, "cardinal_label": "arista %d" % i,
                      "frente": "indefinido", "frente_auto": None, "frente_override": None,
                      "color": PALETA_FRENTE["indefinido"], "etiqueta": "indefinido",
                      "longitud_m": round(largo, 2), "segmentos": [i],
                      "polyline": [[a[0], a[1], a[2]], [b[0], b[1], b[2]]], "vecinos": []})
    return lados


def _dist_a_vias(punto: Sequence[float], ctx: Dict[str, Any]) -> float:
    mejor = 1e9
    for v in ctx.get("vias_oficiales") or []:
        pts = v.get("coordenadas_local") or []
        for k in range(len(pts) - 1):
            d = _dist_punto_seg(punto, pts[k], pts[k + 1])
            if d < mejor:
                mejor = d
    return mejor


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


def _marco(lote: List[List[float]], p0: Sequence[float], p1: Sequence[float]):
    """Eje del frente, normal exterior y espejo para verlo DESDE LA CALLE."""
    eje = _unit(_sub(p1, p0))
    normal = (-eje[1], eje[0])
    cx = sum(float(v[0]) for v in lote) / len(lote)
    cy = sum(float(v[1]) for v in lote) / len(lote)
    mid = ((float(p0[0]) + float(p1[0])) / 2.0, (float(p0[1]) + float(p1[1])) / 2.0)
    if _dot(normal, _sub(mid, (cx, cy))) < 0:
        normal = (-normal[0], -normal[1])
    # "derecha" del observador parado en la calle mirando al lote
    derecha = (-normal[1], normal[0])
    espejo = _dot(eje, derecha) < 0
    return eje, normal, espejo


def _interp(puntos: List[Dict[str, Any]], campo: str, xf: float) -> Optional[float]:
    """Interpola linealmente un campo del perfil (ordenado por xf)."""
    seq = [p for p in puntos if p.get(campo) is not None]
    if not seq:
        return None
    if xf <= seq[0]["xf"]:
        return float(seq[0][campo])
    if xf >= seq[-1]["xf"]:
        return float(seq[-1][campo])
    for a, b in zip(seq, seq[1:]):
        if a["xf"] <= xf <= b["xf"]:
            dd = (b["xf"] - a["xf"]) or EPS
            t = (xf - a["xf"]) / dd
            return float(a[campo]) + t * (float(b[campo]) - float(a[campo]))
    return float(seq[-1][campo])


# ----------------------------------------------------------------------- curvas
def _contornos(malla: List[Sequence[float]], lote_xy: List[Sequence[float]],
               proj: Callable[[Sequence[float]], float], z_ref: float,
               paso: float = 0.5, paso_grid: float = 1.25) -> List[Dict[str, Any]]:
    """Curvas de nivel del terreno proyectadas a la fachada (MSNM).

    Marching squares sobre una grilla IDW del lote; para cada cota se devuelven
    los tramos horizontales [x0, x1] (metros sobre el frente) donde el terreno
    alcanza esa cota. En una elevacion las curvas de nivel son horizontales.
    """
    if not malla or len(lote_xy) < 3:
        return []
    alz = _alzado()
    xs = [float(p[0]) for p in lote_xy]
    ys = [float(p[1]) for p in lote_xy]
    xmin, xmax = min(xs) - 0.5, max(xs) + 0.5
    ymin, ymax = min(ys) - 0.5, max(ys) + 0.5
    nx = max(3, int(math.ceil((xmax - xmin) / paso_grid)) + 1)
    ny = max(3, int(math.ceil((ymax - ymin) / paso_grid)) + 1)
    gx = [xmin + i * (xmax - xmin) / (nx - 1) for i in range(nx)]
    gy = [ymin + j * (ymax - ymin) / (ny - 1) for j in range(ny)]
    grid: List[List[Optional[float]]] = []
    zmin, zmax = 1e18, -1e18
    for y in gy:
        fila: List[Optional[float]] = []
        for x in gx:
            z, _ = alz.idw(malla, x, y)
            if z is None:
                fila.append(None)
            else:
                z = float(z)
                zmin = min(zmin, z)
                zmax = max(zmax, z)
                fila.append(z)
        grid.append(fila)
    if zmin > zmax:
        return []

    nivel0 = math.ceil((zmin + z_ref) / paso) * paso
    nivel1 = math.floor((zmax + z_ref) / paso) * paso
    niveles: List[float] = []
    n = int(round((nivel1 - nivel0) / paso)) + 1
    for i in range(max(0, n)):
        niveles.append(round(nivel0 + i * paso, 3))
    if len(niveles) > 90:
        niveles = niveles[:: max(1, len(niveles) // 90)]

    def cruce(pa: Tuple[float, float], va: float,
              pb: Tuple[float, float], vb: float, z: float) -> Optional[Tuple[float, float]]:
        if (va - z) * (vb - z) > 0:
            return None
        if abs(vb - va) < 1e-12:
            return pa
        t = (z - va) / (vb - va)
        return (pa[0] + t * (pb[0] - pa[0]), pa[1] + t * (pb[1] - pa[1]))

    salida: List[Dict[str, Any]] = []
    for nivel_msnm in niveles:
        z = nivel_msnm - z_ref
        tramos: List[Tuple[float, float]] = []
        for j in range(ny - 1):
            for i in range(nx - 1):
                v00, v10 = grid[j][i], grid[j][i + 1]
                v01, v11 = grid[j + 1][i], grid[j + 1][i + 1]
                if v00 is None or v10 is None or v01 is None or v11 is None:
                    continue
                vals = [v00, v10, v11, v01]
                if min(vals) > z or max(vals) < z:
                    continue
                p00 = (gx[i], gy[j])
                p10 = (gx[i + 1], gy[j])
                p11 = (gx[i + 1], gy[j + 1])
                p01 = (gx[i], gy[j + 1])
                pts: List[Tuple[float, float]] = []
                for pa, va, pb, vb in ((p00, v00, p10, v10), (p10, v10, p11, v11),
                                       (p11, v11, p01, v01), (p01, v01, p00, v00)):
                    q = cruce(pa, va, pb, vb, z)
                    if q is not None:
                        pts.append(q)
                # quitar duplicados (vertices exactos)
                uniq: List[Tuple[float, float]] = []
                for q in pts:
                    if not any(abs(q[0] - r[0]) < 1e-6 and abs(q[1] - r[1]) < 1e-6 for r in uniq):
                        uniq.append(q)
                if len(uniq) < 2:
                    continue
                if len(uniq) == 2:
                    pares = [(uniq[0], uniq[1])]
                elif len(uniq) == 3:
                    pares = [(uniq[0], uniq[1]), (uniq[1], uniq[2])]
                else:
                    # silla: emparejar los dos puntos mas cercanos entre si
                    d01 = math.hypot(uniq[0][0] - uniq[1][0], uniq[0][1] - uniq[1][1])
                    d02 = math.hypot(uniq[0][0] - uniq[2][0], uniq[0][1] - uniq[2][1])
                    d03 = math.hypot(uniq[0][0] - uniq[3][0], uniq[0][1] - uniq[3][1])
                    if d01 <= min(d02, d03):
                        pares = [(uniq[0], uniq[1]), (uniq[2], uniq[3])]
                    elif d02 <= d03:
                        pares = [(uniq[0], uniq[2]), (uniq[1], uniq[3])]
                    else:
                        pares = [(uniq[0], uniq[3]), (uniq[1], uniq[2])]
                for a, b in pares:
                    mx, my = (a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0
                    if _punto_en_poligono(mx, my, lote_xy):
                        tramos.append((proj(a), proj(b)))
        if not tramos:
            continue
        tramos.sort()
        unidos: List[List[float]] = []
        for a, b in tramos:
            a, b = min(a, b), max(a, b)
            if unidos and a - unidos[-1][1] <= 2.0:
                unidos[-1][1] = max(unidos[-1][1], b)
            else:
                unidos.append([a, b])
        unidos = [[a, b] for a, b in unidos if (b - a) >= 0.8][:5]
        if not unidos:
            continue
        salida.append({"msnm": round(nivel_msnm, 2), "z": round(z, 3),
                       "tramos": [[round(a, 2), round(b, 2)] for a, b in unidos],
                       "mayor": abs(nivel_msnm - round(nivel_msnm)) < 1e-6})
    return salida


# ----------------------------------------------------------------------- vecinos
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


def _vecinos(c50: Optional[Dict[str, Any]], ctx: Dict[str, Any], lote_xy: List[Sequence[float]],
             proj: Callable[[Sequence[float]], float],
             prof: Callable[[Sequence[float]], float],
             profundidad: float, largo_frente: float,
             color_izq: str, color_der: str) -> Tuple[List[Dict[str, Any]], int]:
    """Volumenes de vecinos en marco ETAPA1, con rol y color del lado."""
    if not c50:
        return [], 0
    alz = _alzado()
    meta50 = c50.get("metadata") or {}
    ancla = meta50.get("ancla_canvas_local") or {}
    ax = float(ancla.get("x", 0.0))
    ay = float(ancla.get("y", 0.0))
    desp = alz._desplazamiento_z(ctx, meta50)
    out: List[Dict[str, Any]] = []
    sin_dato = 0
    for e in c50.get("edificios") or []:
        zb = e.get("z_base_m")
        h = e.get("altura_m")
        if zb is None or not h:
            sin_dato += 1
            continue
        ring = (e.get("anillos") or [e.get("vertices")])[0] or []
        if len(ring) < 3:
            sin_dato += 1
            continue
        ring_c = [(float(p[0]) + ax, float(p[1]) + ay) for p in ring]
        dentro = sum(1 for p in ring_c if _punto_en_poligono(p[0], p[1], lote_xy))
        if dentro * 2 >= len(ring_c):
            continue  # construccion del propio predio
        xfv = [proj(p) for p in ring_c]
        profs = [prof(p) for p in ring_c]
        prof_m = sum(profs) / len(profs)
        if prof_m > 25.0 or prof_m < -(profundidad + 15.0):
            continue
        x0, x1 = min(xfv), max(xfv)
        # solo vecinos inmediatos: tocando el lote o al frente, cruzando la calle
        dist = _dist_anillo_lote(ring_c, lote_xy)
        if not (dist <= 4.0 or (0.0 < prof_m <= 15.0 and x1 >= -2.0
                                and x0 <= largo_frente + 2.0)):
            continue
        rol = "fondo"
        if x1 <= 1.0 and abs(prof_m) <= 15.0:
            rol = "lateral_izq"
        elif x0 >= largo_frente - 1.0 and abs(prof_m) <= 15.0:
            rol = "lateral_der"
        elif prof_m > 1.0:
            rol = "frente"
        color = "#94a3b8"
        if rol == "lateral_izq":
            color = color_izq
        elif rol == "lateral_der":
            color = color_der
        out.append({"id": e.get("id"), "rol": rol, "color": color,
                    "x0": round(x0, 2), "x1": round(x1, 2), "prof": round(prof_m, 2),
                    "z_base": round(float(zb) - desp, 3),
                    "h": round(float(h), 2),
                    "z_top": round(float(zb) - desp + float(h), 3),
                    "anillo": [[round(p[0], 2), round(p[1], 2)] for p in ring_c]})
    out.sort(key=lambda v: -v["prof"])
    return out, sin_dato


# ---------------------------------------------------------------------- principal
def construir(chip: str, lado_id: Optional[int] = None, ancho_via: float = 3.0,
              mdt: str = "malla", n_lindero: int = 25) -> Dict[str, Any]:
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
    alz = _alzado()

    lados = _lados_lote(chip, lote)
    frente, origen_frente = _elegir_frente(chip, lados, ctx, lado_id)
    p0 = frente["polyline"][0]
    p1 = frente["polyline"][-1]
    eje, normal, espejo = _marco(lote, p0, p1)
    L = math.hypot(p1[0] - p0[0], p1[1] - p0[1])

    def proj(p: Sequence[float]) -> float:
        d = _dot(_sub(p, p0), eje)
        return (L - d) if espejo else d

    def prof(p: Sequence[float]) -> float:
        return _dot(_sub(p, p0), normal)

    # desviacion del lindero real respecto de la cuerda
    desvio = max((abs(_dot(_sub(v, p0), normal)) for v in frente["polyline"]), default=0.0)

    # -------- muestreo del lindero y de la franja de calle
    lindero: List[Dict[str, Any]] = []
    calle: List[Dict[str, Any]] = []
    for k in range(n_lindero):
        t = k / float(n_lindero - 1)
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        z, dentro = alz.idw(malla, x, y)
        lindero.append({"t": t, "x": x, "y": y, "z": z, "estimado": not dentro,
                        "fuente": "malla ETAPA1", "xf": proj((x, y))})
        xv = x + normal[0] * ancho_via
        yv = y + normal[1] * ancho_via
        zv, dentro_v = alz.idw(malla, xv, yv)
        fallback = False
        if zv is None:
            zv, fallback = z, True
        calle.append({"t": t, "x": xv, "y": yv, "z": zv,
                      "estimado": (not dentro_v) or fallback,
                      "fuente": "malla ETAPA1", "xf": proj((xv, yv))})

    mdt_metodo = "IDW malla ETAPA1 (%d puntos)" % len(malla)
    cache_mdt = _json(ruta_mdt_frontal(chip), {}) or {}
    cache_ok = (cache_mdt.get("lado_id") == frente["lado_id"]
                and cache_mdt.get("n") == n_lindero
                and len(cache_mdt.get("z_lindero") or []) == n_lindero
                and len(cache_mdt.get("z_calle") or []) == n_lindero)
    if mdt == "rest":
        planos = [(p["x"], p["y"]) for p in lindero] + [(p["x"], p["y"]) for p in calle]
        zs_rest, ok_rest = alz._rest_terreno(planos, ctx)
        if ok_rest:
            n = len(lindero)
            for k, p in enumerate(lindero):
                zr = zs_rest[k]
                if zr is not None:
                    p["z"], p["estimado"], p["fuente"] = zr, False, "MDT REST"
            for k, p in enumerate(calle):
                zr = zs_rest[n + k]
                if zr is not None:
                    p["z"], p["estimado"], p["fuente"] = zr, False, "MDT REST"
            mdt_metodo = "MDT Catastro REST (puntos reales)"
            try:
                with io.open(ruta_mdt_frontal(chip), "w", encoding="utf-8") as f:
                    json.dump({"chip": chip, "lado_id": frente["lado_id"], "n": n_lindero,
                               "z_lindero": [p["z"] for p in lindero],
                               "z_calle": [p["z"] for p in calle],
                               "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")},
                              f, ensure_ascii=False, indent=1)
            except Exception:
                pass
        elif cache_ok:
            for k, p in enumerate(lindero):
                p["z"], p["estimado"], p["fuente"] = cache_mdt["z_lindero"][k], False, "MDT cache"
            for k, p in enumerate(calle):
                p["z"], p["estimado"], p["fuente"] = cache_mdt["z_calle"][k], False, "MDT cache"
            mdt_metodo = "MDT Catastro en cache (%s; REST no disponible)" % cache_mdt.get("fecha", "-")
        else:
            mdt_metodo = "IDW malla ETAPA1 (REST no disponible)"
    elif cache_ok:
        for k, p in enumerate(lindero):
            p["z"], p["estimado"], p["fuente"] = cache_mdt["z_lindero"][k], False, "MDT cache"
        for k, p in enumerate(calle):
            p["z"], p["estimado"], p["fuente"] = cache_mdt["z_calle"][k], False, "MDT cache"
        mdt_metodo = "MDT Catastro en cache (%s) + malla ETAPA1" % cache_mdt.get("fecha", "-")

    for p in lindero + calle:
        p["z"] = round(float(p["z"]), 3) if p.get("z") is not None else None
        p["msnm"] = round(float(p["z"]) + z_ref, 2) if p.get("z") is not None else None
    lindero.sort(key=lambda p: p["xf"])
    calle.sort(key=lambda p: p["xf"])

    z_lote = [v[2] for v in lote]
    z_lindero = [p["z"] for p in lindero if p["z"] is not None]
    z_calle = [p["z"] for p in calle if p["z"] is not None]
    avisos: List[str] = []
    if desvio > 0.75:
        avisos.append("El lindero frontal no es recto (desvio %.2f m): el perfil se muestrea "
                      "sobre la cuerda entre sus extremos." % desvio)
    estimados = sum(1 for p in lindero + calle if p.get("estimado"))
    if estimados:
        avisos.append("%d de %d puntos de muestreo quedan fuera de la malla ETAPA1: su cota "
                      "es extrapolada (use 'Actualizar cotas MDT' para leer Catastro)."
                      % (estimados, len(lindero) + len(calle)))

    # -------- lados proyectados (perimetro con los colores de la planta)
    for l in lados:
        pts = l["polyline"]
        xfv = [proj(q) for q in pts]
        l["x0"] = round(min(xfv), 2)
        l["x1"] = round(max(xfv), 2)
        l["polyline_xz"] = [[round(proj(q), 2), round(float(q[2]), 2)] for q in pts]

    def _color_extremo(xext: float) -> str:
        """Color del lado que toca el extremo del frente (0 o L)."""
        for l in lados:
            if l["x0"] - 0.25 <= xext <= l["x1"] + 0.25:
                return l["color"]
        if not lados:
            return "#9ca3af"
        c = min(lados, key=lambda l: min(abs(l["x0"] - xext), abs(l["x1"] - xext)))
        return c["color"]

    color_izq = _color_extremo(0.0)
    color_der = _color_extremo(L)

    # -------- rango horizontal de la vista (todo el predio proyectado)
    xf_lote = [proj(v) for v in lote]
    x_min, x_max = min(xf_lote), max(xf_lote)

    # -------- esquinas principales (extremos de los lados agrupados)
    esquinas: List[Dict[str, Any]] = []
    vistos = set()
    for l in lados:
        for q in (l["polyline"][0], l["polyline"][-1]):
            clave = (round(q[0], 2), round(q[1], 2))
            if clave in vistos:
                continue
            vistos.add(clave)
            xq, yq, zq = float(q[0]), float(q[1]), float(q[2])
            xfq = proj((xq, yq))
            rol = "izq" if xfq <= x_min + 1.0 else ("der" if xfq >= x_max - 1.0 else "fondo")
            esquinas.append({"x": round(xq, 2), "y": round(yq, 2), "z": round(zq, 3),
                             "msnm": round(zq + z_ref, 2), "xf": round(xfq, 2),
                             "prof": round(prof((xq, yq)), 2), "rol": rol,
                             "lado_id": l["lado_id"]})
    esquinas.sort(key=lambda e: e["xf"])

    # -------- curvas de nivel, silueta y vecinos
    curvas = _contornos(malla, [[v[0], v[1]] for v in lote], proj, z_ref)
    profundidad = max([-prof(v) for v in lote] + [5.0])
    silueta: List[Dict[str, Any]] = []
    paso_bin = max(1.0, (x_max - x_min) / 60.0)
    bins: Dict[int, List[float]] = {}
    nx = max(3, int((max(v[0] for v in lote) - min(v[0] for v in lote)) / 1.5) + 1)
    ny = max(3, int((max(v[1] for v in lote) - min(v[1] for v in lote)) / 1.5) + 1)
    for iy in range(ny):
        yy = min(v[1] for v in lote) + iy * (max(v[1] for v in lote) - min(v[1] for v in lote)) / (ny - 1)
        for ix in range(nx):
            xx = min(v[0] for v in lote) + ix * (max(v[0] for v in lote) - min(v[0] for v in lote)) / (nx - 1)
            if not _punto_en_poligono(xx, yy, lote):
                continue
            zz, _ = alz.idw(malla, xx, yy)
            if zz is None:
                continue
            ib = int((proj((xx, yy)) - x_min) / paso_bin)
            bins.setdefault(ib, []).append(float(zz))
    for ib in sorted(bins):
        zs = bins[ib]
        silueta.append({"xf": round(x_min + (ib + 0.5) * paso_bin, 2),
                        "z_base": round(min(zs), 3), "z_top": round(max(zs), 3)})

    c50 = _json(ruta_contexto50(chip), {}) or {}
    vecinos, n_sin_altura = _vecinos(c50, ctx, [[v[0], v[1]] for v in lote], proj, prof,
                                     profundidad, L, color_izq, color_der)

    # -------- altura reglamentaria (override del operador > geobase)
    pot = ctx.get("pot_data") or {}
    norma_ov = ((_json(os.path.join(POT_BOGOTA, "norma-override.json"), {}) or {})
                .get("lotes") or {}).get(chip) or {}
    h_norma = norma_ov.get("altura_maxima_m") or pot.get("altura_maxima_m") or 0.0
    h_fuente = (norma_ov.get("altura_maxima_fuente") or norma_ov.get("fuente")
                or pot.get("altura_maxima_fuente") or pot.get("fuente_norma") or "POT")
    altura = {"h_m": round(float(h_norma), 3),
              "fuente": h_fuente,
              "referencia_m": norma_ov.get("altura_maxima_m_referencia_pzcb")
              or pot.get("altura_maxima_m_referencia_pzcb"),
              "upz": pot.get("upz"), "tratamiento": pot.get("tratamiento"),
              "tipologia": pot.get("tipologia"), "pisos": norma_ov.get("altura_maxima_pisos")
              or pot.get("altura_maxima_pisos")}

    # -------- datum y banda sobre el terreno
    z0d = _json(ruta_z0(chip), {}) or {}
    z0_m = z0d.get("z0_m")
    modo = z0d.get("modo") or "min_lote"
    if z0_m is None:
        z0_m = min(z_lote) if z_lote else 0.0
    present = z0d.get("presentacion") or {}
    xf_datum = present.get("x_frente_m")
    punto_datum = present.get("punto_id")
    if xf_datum is None:
        xf_datum = L / 2.0
    xf_datum = min(max(float(xf_datum), 0.0), L)
    z_terreno_datum = _interp(lindero, "z", xf_datum)
    if z_terreno_datum is None:
        z_terreno_datum = float(z0_m)
    banda = {"base_z": round(float(z_terreno_datum), 3),
             "base_msnm": round(float(z_terreno_datum) + z_ref, 2),
             "top_z": round(float(z_terreno_datum) + float(h_norma), 3),
             "top_msnm": round(float(z_terreno_datum) + float(h_norma) + z_ref, 2),
             "h_m": round(float(h_norma), 3),
             "x_frente_m": round(xf_datum, 2),
             "delta_vs_z0_m": round(float(z_terreno_datum) - float(z0_m), 3),
             "regla": "altura permitida medida sobre el nivel del terreno"}

    # -------- puntos marcados en planta
    guardados = leer_puntos(chip)
    puntos: List[Dict[str, Any]] = []
    for k, p in enumerate(guardados["puntos"]):
        z, dentro = alz.idw(malla, p["x"], p["y"])
        h_p = float(guardados["alturas"].get(p["id"], h_norma))
        xf_p = proj((p["x"], p["y"]))
        puntos.append({
            "id": p["id"],
            "color": (COLOR_PUNTO[(int(p["id"][1:]) - 1) % len(COLOR_PUNTO)]
                      if p["id"][1:].isdigit() else COLOR_PUNTO[k % len(COLOR_PUNTO)]),
            "x": round(p["x"], 3), "y": round(p["y"], 3),
            "xf": round(xf_p, 2), "prof": round(prof((p["x"], p["y"])), 2),
            "dentro": bool(dentro), "z": round(float(z), 3) if z is not None else None,
            "msnm": round(float(z) + z_ref, 2) if z is not None else None,
            "h_m": round(h_p, 3), "h_manual": p["id"] in guardados["alturas"],
            "z_top": round(float(z) + h_p, 3) if z is not None else None,
            "msnm_top": round(float(z) + h_p + z_ref, 2) if z is not None else None})
    if punto_datum:
        for p in puntos:
            if p["id"] == punto_datum:
                xf_datum = p["xf"]
                if p["z"] is not None:
                    z_terreno_datum = p["z"]
                    banda.update({"base_z": round(float(p["z"]), 3),
                                  "base_msnm": round(float(p["msnm"]), 2),
                                  "top_z": round(float(p["z"]) + float(h_norma), 3),
                                  "top_msnm": round(float(p["msnm"]) + float(h_norma), 2),
                                  "x_frente_m": round(p["xf"], 2),
                                  "delta_vs_z0_m": round(float(p["z"]) - float(z0_m), 3)})

    for p in puntos:
        x_min = min(x_min, p["xf"])
        x_max = max(x_max, p["xf"])
    x_rango = [round(x_min - 5.0, 2), round(x_max + 5.0, 2)]

    # -------- plano en miniatura
    plano = {
        "lote": [[round(v[0], 2), round(v[1], 2)] for v in lote],
        "bbox": [round(min(v[0] for v in lote), 2), round(min(v[1] for v in lote), 2),
                 round(max(v[0] for v in lote), 2), round(max(v[1] for v in lote), 2)],
        "lados": [{"lado_id": l["lado_id"], "color": l["color"], "etiqueta": l["etiqueta"],
                   "nombre": l["cardinal_label"] or l["cardinal"],
                   "polyline": [[p[0], p[1]] for p in l["polyline"]],
                   "es_frente": l["lado_id"] == frente["lado_id"]} for l in lados],
        "vecinos": [{"id": v["id"], "color": v["color"], "anillo": v["anillo"],
                     "rol": v["rol"]} for v in vecinos],
        "frente": {"p0": [p0[0], p0[1]], "p1": [p1[0], p1[1]],
                   "normal": [normal[0], normal[1]],
                   "color": frente["color"], "largo_m": round(L, 2)},
    }

    return {
        "chip": chip,
        "generado": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "marco": "canvas (z_local = Z_abs - z_ref; msnm = z_local + z_ref)",
        "frente": {"lado_id": frente["lado_id"],
                   "cardinal": frente.get("cardinal"),
                   "etiqueta": frente.get("cardinal_label") or frente.get("cardinal"),
                   "origen": origen_frente if lado_id is None else "seleccion del operador",
                   "frente_tipo": frente["frente"],
                   "color": frente["color"],
                   "p0": [round(p0[0], 3), round(p0[1], 3)],
                   "p1": [round(p1[0], 3), round(p1[1], 3)],
                   "eje_x": [round(eje[0], 6), round(eje[1], 6)],
                   "normal": [round(normal[0], 6), round(normal[1], 6)],
                   "espejo": bool(espejo),
                   "largo_m": round(L, 2),
                   "desvio_lindero_m": round(desvio, 2),
                   "via_cercana": ((_json(ruta_bloques(chip), {}) or {}).get("orientacion")
                                   or {}).get("calle_acceso", {}).get("via_cercana_nombre")},
        "msnm": {"z_ref_m": round(z_ref, 3), "regla": "msnm = z_local + origen_sirgas.z"},
        "lindero": lindero,
        "calle": calle,
        "perfil": {"z_min": min(z_lindero) if z_lindero else None,
                   "z_max": max(z_lindero) if z_lindero else None,
                   "desnivel_m": round(max(z_lindero) - min(z_lindero), 2) if z_lindero else None,
                   "calle_min": min(z_calle) if z_calle else None,
                   "calle_max": max(z_calle) if z_calle else None},
        "esquinas": esquinas,
        "curvas": curvas,
        "silueta": silueta,
        "vecinos": vecinos,
        "vecinos_sin_altura": n_sin_altura,
        "lados": lados,
        "altura": altura,
        "datum": {"z0_m": round(float(z0_m), 3), "z0_msnm": round(float(z0_m) + z_ref, 2),
                  "modo": modo, "origen": z0d.get("origen"),
                  "x_frente_m": round(xf_datum, 2), "punto_id": punto_datum},
        "banda": banda,
        "puntos": puntos,
        "max_puntos": MAX_PUNTOS,
        "plano": plano,
        "lote_min_z": round(min(z_lote), 3),
        "lote_max_z": round(max(z_lote), 3),
        "x_rango": x_rango,
        "lote_x": [round(min(xf_lote), 2), round(max(xf_lote), 2)],
        "mdt": {"metodo": mdt_metodo, "puntos": len(malla)},
        "fuentes": {"lados": os.path.basename(ruta_vecinos_por_lado(chip) or "") or "derivados",
                    "vecinos": os.path.basename(ruta_contexto50(chip) or "") or "sin contexto50",
                    "norma": h_fuente},
        "avisos": avisos,
    }


# --------------------------------------------------------------------------- CLI
def main() -> int:
    ap = argparse.ArgumentParser(description="Vista frontal del lote desde la calle")
    ap.add_argument("--chip", required=True)
    ap.add_argument("--lado", type=int, default=None)
    ap.add_argument("--ancho-via", type=float, default=3.0)
    ap.add_argument("--mdt", choices=("malla", "rest"), default="malla")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--salida", default=None)
    args = ap.parse_args()

    datos = construir(args.chip, lado_id=args.lado, ancho_via=args.ancho_via, mdt=args.mdt)
    if args.salida:
        with io.open(args.salida, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)
    if args.json:
        print(json.dumps(datos, ensure_ascii=False))
    else:
        fr = datos["frente"]
        print("Frontal %s | lado %s (%s) | %.2f m | %s"
              % (datos["chip"], fr["lado_id"], fr["etiqueta"], fr["largo_m"], fr["origen"]))
        print("  lindero %.2f a %.2f msnm | calle %.2f a %.2f msnm"
              % (datos["perfil"]["z_min"] + datos["msnm"]["z_ref_m"],
                 datos["perfil"]["z_max"] + datos["msnm"]["z_ref_m"],
                 datos["perfil"]["calle_min"] + datos["msnm"]["z_ref_m"],
                 datos["perfil"]["calle_max"] + datos["msnm"]["z_ref_m"]))
        print("  curvas: %d niveles | vecinos: %d | esquinas: %d | puntos: %d"
              % (len(datos["curvas"]), len(datos["vecinos"]), len(datos["esquinas"]),
                 len(datos["puntos"])))
        print("  datum 0,00 = %.2f msnm (%s) | banda terreno %.2f-%.2f msnm"
              % (datos["datum"]["z0_msnm"], datos["datum"]["modo"],
                 datos["banda"]["base_msnm"], datos["banda"]["top_msnm"]))
        for a in datos["avisos"]:
            print("  aviso: %s" % a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
