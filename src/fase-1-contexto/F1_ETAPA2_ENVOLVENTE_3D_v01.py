"""
================================================================================
F1_ETAPA2_ENVOLVENTE_3D_v01.py — Envolvente en 3D (curva + banda + volumen)
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Toma la `envelope_curve` de F1_ETAPA2_NORMATIVA_v08 (huella envolvente del
  predio) y la altura total, y produce representaciones 3D para la Live
  Connection (canvas v12):
    - curva_3d    (Curve)  -> nodo "Morph Curve" (perimetro 3D drapeado al MDT)
    - banda_3d    (Mesh)   -> nodo "Morph Solid" (cinta drapeada)
    - volumen_3d  (Mesh)   -> nodo "Morph Solid" (prisma extruido; util para
                              movimiento de tierra / prefactibilidad, pedido
                              del operador 2026-09-29)
  La cota se interpola del MDT (IDW sobre `topo_pts`, salida del componente
  F1_ETAPA1_CONTEXTO_3D_v01). El prisma se levanta desde la cota minima
  drapeada de la envolvente hasta `altura_total`.

POLITICA DE CODIFICACION (2026-09-29): lectura por cascada sobre bytes
  (utf-8 estricto -> cp1252 -> latin-1) — este componente no lee archivos,
  pero mantiene la convencion de avisos ruidosos (sin fallback silencioso).

CAMBIOS:
  v01 (2026-09-29): creacion (sustituye el plan "NORMATIVA v08.1": se prefirio
    un componente dedicado para no tocar el contrato validado de NORMATIVA v08).
    Muestreo de la envolvente con rg.Curve.DivideByCount (N=64) drapeado por
    IDW; banda reutiliza el patron de F1_ETAPA1_CONTEXTO_v05; prisma por malla
    construida a mano (sin rg.Extrusion) + tapas.

ENTRADAS:
  envelope_curve (Curve)     — salida de F1_ETAPA2_NORMATIVA_v08 (envelope)
  altura_total   (Number)    — altura total [m] (salida de NORMATIVA v08)
  topo_pts       (Point3d[]) — puntos del MDT en marco canvas (ETAPA1_3D)
  mostrar_curva   (Boolean)  — gate de la curva 3D
  mostrar_banda   (Boolean)  — gate de la cinta 3D
  mostrar_volumen (Boolean)  — gate del prisma (default OFF en el canvas)

SALIDAS:
  curva_3d   (Curve)  — perimetro drapeado (cerrado)
  banda_3d   (Mesh)   — cinta drapeada
  volumen_3d (Mesh)   — prisma (base = min cota drapeada; tope = base + altura)
  mensaje    (String) — diagnostico

CONEXIONES (canvas v12):
  envelope_curve <- #113 NORMATIVA.envelope_curve
  altura_total   <- #113 NORMATIVA.altura_total
  topo_pts       <- F1_ETAPA1_CONTEXTO_3D_v01.topo_pts
  mostrar_*      <- Boolean Toggles del canvas
  curva_3d -> Morph Curve 3 | banda_3d -> Morph Solid (bandas) |
  volumen_3d -> Morph Solid (volumen)
================================================================================
"""

import Rhino.Geometry as rg
import json
import io
import os
import math

N_MUESTREO = 64       # puntos de muestreo de la envolvente
ANCHO_BANDA_M = 0.6   # cinta de la envolvente (un poco mas ancha que las de contexto)
PROF_BANDA_M = 0.6


# ------------------------------------------------------------------ utilidades
def unwrap(val):
    if val is None:
        return None
    if isinstance(val, list):
        return val[0] if len(val) > 0 else None
    return val


def parse_bool(val, default=True):
    val = unwrap(val)
    if val is None:
        return default
    if isinstance(val, bool):
        return val
    s = str(val).strip().lower()
    return s in ("true", "1", "verdadero", "yes", "si")


def to_float_safe(val, default=0.0):
    if val is None:
        return default
    try:
        return float(val)
    except:
        return default


def _idw_z(gx, gy, pts):
    gz = 0.0
    total_w = 0.0
    for px, py, pz in pts:
        dist = math.sqrt((gx - px) ** 2 + (gy - py) ** 2)
        if dist < 0.01:
            return pz
        w = 1.0 / max(0.1, dist * dist)
        gz += pz * w
        total_w += w
    return gz / total_w if total_w > 0 else 0.0


def _puntos_de_curva(crv, n=N_MUESTREO):
    """Muestrea una curva cerrada/abierta con DivideByCount + PointAt."""
    pts = []
    if crv is None:
        return pts
    try:
        tt = rg.Curve.DivideByCount(crv, n, True)
        for t in tt:
            pts.append(crv.PointAt(t))
    except Exception:
        # fallback: propiedades de PolylineCurve
        try:
            poly = crv.Polyline
            for p in poly:
                pts.append(p)
        except Exception:
            pass
    return pts


def _pts_a_tuplas(pts):
    out = []
    for p in pts:
        out.append((p.X, p.Y))
    return out


def banda_drapeada(p_xy, pts_mdt, ancho=ANCHO_BANDA_M, prof=PROF_BANDA_M):
    """Cinta 3D que sigue el MDT (mismo patron de ETAPA1 v05)."""
    if not p_xy or len(p_xy) < 2 or not pts_mdt:
        return None
    p = list(p_xy)
    if p[0] != p[-1]:
        p.append(p[0])
    n = len(p)
    left = []
    right = []
    for i in range(n):
        i0 = i - 1 if i > 0 else (n - 2)
        i1 = i + 1 if i < n - 1 else (1)
        tx = p[i1][0] - p[i0][0]
        ty = p[i1][1] - p[i0][1]
        L = math.sqrt(tx * tx + ty * ty)
        if L < 1e-9:
            tx, ty, L = 1.0, 0.0, 1.0
        nx, ny = -ty / L, tx / L
        left.append((p[i][0] + nx * ancho / 2.0, p[i][1] + ny * ancho / 2.0))
        right.append((p[i][0] - nx * ancho / 2.0, p[i][1] - ny * ancho / 2.0))
    m = rg.Mesh()
    zl = []
    zr = []
    zlb = []
    zrb = []
    for i in range(n):
        z = _idw_z(p[i][0], p[i][1], pts_mdt)
        zl.append(m.Vertices.Add(left[i][0], left[i][1], z))
        zr.append(m.Vertices.Add(right[i][0], right[i][1], z))
        zlb.append(m.Vertices.Add(left[i][0], left[i][1], z - prof))
        zrb.append(m.Vertices.Add(right[i][0], right[i][1], z - prof))
    seg = n
    for i in range(seg):
        j = (i + 1) % n
        m.Faces.AddFace(zl[i], zr[i], zr[j], zl[j])
        m.Faces.AddFace(zlb[i], zlb[j], zrb[j], zrb[i])
        m.Faces.AddFace(zl[i], zlb[i], zlb[j], zl[j])
        m.Faces.AddFace(zr[i], zr[j], zrb[j], zrb[i])
    m.Normals.ComputeNormals()
    m.Compact()
    return m


def curva_drapeada(p_xy, pts_mdt):
    if not p_xy or len(p_xy) < 2 or not pts_mdt:
        return None
    p = list(p_xy)
    if p[0] != p[-1]:
        p.append(p[0])
    poly = rg.Polyline()
    for (px, py) in p:
        poly.Add(px, py, _idw_z(px, py, pts_mdt))
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def prisma_desde_poligono(p_xy, z_base, altura):
    """v01: prisma por malla (paredes + tapa superior + base) sin rg.Extrusion."""
    if not p_xy or len(p_xy) < 3 or altura <= 0:
        return None
    p = list(p_xy)
    if p[0] == p[-1]:
        p.pop()
    n = len(p)
    m = rg.Mesh()
    bot = []
    top = []
    for (px, py) in p:
        bot.append(m.Vertices.Add(px, py, z_base))
        top.append(m.Vertices.Add(px, py, z_base + altura))
    for i in range(n):
        j = (i + 1) % n
        m.Faces.AddFace(bot[i], bot[j], top[j], top[i])
    # tapas (abanico desde el primer vertice)
    for i in range(1, n - 1):
        m.Faces.AddFace(bot[0], bot[i + 1], bot[i])
        m.Faces.AddFace(top[0], top[i], top[i + 1])
    m.Normals.ComputeNormals()
    m.Compact()
    return m


# ==============================================================================
# MAIN
# ==============================================================================

envelope_curve = unwrap(globals().get("envelope_curve", None))
altura_total = to_float_safe(unwrap(globals().get("altura_total", None)), 0.0)
topo_pts_raw = globals().get("topo_pts", None)
mostrar_curva = parse_bool(globals().get("mostrar_curva", None), True)
mostrar_banda = parse_bool(globals().get("mostrar_banda", None), True)
mostrar_volumen = parse_bool(globals().get("mostrar_volumen", None), False)

curva_3d = None
banda_3d = None
volumen_3d = None
mensaje = ""

pts_mdt = []
if isinstance(topo_pts_raw, list):
    for p in topo_pts_raw:
        try:
            pts_mdt.append((p.X, p.Y, p.Z))
        except Exception:
            pass

if envelope_curve is None:
    mensaje = "ENVOLVENTE-3D v01 | AVISO: sin envelope_curve (NORMATIVA no valida?)"
elif not pts_mdt:
    mensaje = "ENVOLVENTE-3D v01 | AVISO: sin topo_pts (revisar ETAPA1_3D)"
else:
    try:
        muestras = _puntos_de_curva(envelope_curve)
        p_xy = _pts_a_tuplas(muestras)
        if len(p_xy) < 3:
            mensaje = "ENVOLVENTE-3D v01 | AVISO: no se pudo muestrear la envolvente"
        else:
            if mostrar_curva:
                curva_3d = curva_drapeada(p_xy, pts_mdt)
            if mostrar_banda:
                banda_3d = banda_drapeada(p_xy, pts_mdt)
            if mostrar_volumen and altura_total > 0:
                zs = [_idw_z(px, py, pts_mdt) for (px, py) in p_xy]
                z_base = min(zs) if zs else 0.0
                volumen_3d = prisma_desde_poligono(p_xy, z_base, altura_total)
            mensaje = ("ENVOLVENTE-3D v01 | muestras: {} | base: {:.2f} | altura: {:.2f} | "
                       "curva: {} | banda: {} | volumen: {}").format(
                len(p_xy),
                min([_idw_z(px, py, pts_mdt) for (px, py) in p_xy]) if p_xy else 0.0,
                altura_total,
                "ON" if curva_3d is not None else "OFF",
                "ON" if banda_3d is not None else "OFF",
                "ON" if volumen_3d is not None else "OFF")
    except Exception as e:
        mensaje = "ENVOLVENTE-3D v01 | ERROR: [{}] {}".format(type(e).__name__, str(e))
