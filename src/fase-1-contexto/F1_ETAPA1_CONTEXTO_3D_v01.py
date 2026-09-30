"""
================================================================================
F1_ETAPA1_CONTEXTO_3D_v01.py — Contexto 3D drapeado (ramas para el canvas v12)
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Rama 3D ADITIVA del contexto (no reemplaza a F1_ETAPA1_CONTEXTO_v04.x): lee
  el mismo JSON de contexto y produce las representaciones necesarias para que
  los perimetros (lote, vecinos, vias, espacios publicos) sean VISIBLES Y
  UTILIZABLES EN 3D dentro de ArchiCAD, via los nodos de la Live Connection:
    - bandas drapeadas (Mesh)  -> nodo "Morph Solid"  (cinta con cuerpo)
    - curvas drapeadas (Curve) -> nodo "Morph Curve"  (linea 3D no solida)
    - topo_pts + topo_boundary -> nodo "Mesh"         (malla de terreno)
  La cota de cada punto se interpola del MDT (malla_terreno del JSON, IDW),
  en el MISMO marco local del canvas que F1_ETAPA1_CONTEXTO (anclaje vertice
  SE del lote; regla del proyecto).

  Origen: funciones de bandas probadas en F1_ETAPA1_CONTEXTO_v05 (offline
  6/6, 2026-09-29). Esta version: contrato SLIM solo-3D + LECTOR CANONICO de
  codificacion + salidas adicionales (curvas 3D, terreno).

POLITICA DE CODIFICACION (v2026-09-29, LECTOR CANONICO):
  - Lectura: bytes -> utf-8 estricto (con/sin BOM) -> cp1252 -> latin-1,
    con AVISO RUIDOSO si no fue utf-8 y error explicito (hex de cabecera) si
    todo falla. Regla de proyecto: los escritores nuevos emiten UTF-8
    explicito / ASCII-safe; nunca defaults ANSI.

CAMBIOS:
  v01 (2026-09-29): creacion. Deriva de F1_ETAPA1_CONTEXTO_v05 (bandas) +
    lector canonico + curvas 3D drapeadas (nodos "Morph Curve") + terreno
    (topo_pts/topo_boundary para el nodo "Mesh") + toggles de visibilidad
    (mostrar_curvas / mostrar_cintas). Referencia LC verificada (2026-09-29):
    la Live Connection NO tiene nodo "3D Polyline"; si "Morph Curve".

ENTRADAS:
  json_path (String)        — Ruta al <CHIP>-contexto.json (mismo panel que
                              alimenta a F1_ETAPA1_CONTEXTO_v04.x)
  mostrar_curvas (Boolean)  — si False, curvas_* salen vacias (toggle canvas)
  mostrar_cintas (Boolean)  — si False, bandas_* salen vacias (toggle canvas)

SALIDAS:
  bandas_lote      (Mesh)    — cinta del perimetro del lote sobre el MDT
  bandas_vecinos   (Mesh[])  — cintas de perimetros de vecinos
  bandas_vias      (Mesh[])  — cintas de ejes/areas de via (abiertas)
  bandas_ep        (Mesh[])  — cintas de espacios publicos
  bandas_todas     (Mesh[])  — concatenacion lista para un unico Morph Solid
  curvas_lote      (Curve)   — polilinea 3D del lote drapeada (cerrada)
  curvas_vecinos   (Curve[]) — polilineas 3D de vecinos (cerradas)
  curvas_vias      (Curve[]) — polilineas 3D de vias (abiertas)
  curvas_ep        (Curve[]) — polilineas 3D de espacios publicos (cerradas)
  topo_pts         (Point3d[]) — puntos del MDT en marco canvas (node Mesh)
  topo_boundary    (Curve)   — contorno rectangular horizontal del area MDT
  mensaje          (String)  — diagnostico

CONEXIONES (canvas v12):
  json_path      <- mismo File Path que #21 (data/pot-cache/CHIP-contexto.json)
  mostrar_*      <- Boolean Toggles del canvas
  bandas_todas   -> Morph Solid (bandas)      curvas_lote    -> Morph Curve 1
  curvas_vecinos -> Morph Curve 2             (env) banda_3d -> Morph Solid
  topo_pts/topo_boundary -> nodo Mesh         (malla de terreno)
================================================================================
"""

import Rhino.Geometry as rg
import json
import io
import os
import math
import System.IO
import System.Text

ANCHO_BANDA_M = 0.5   # ancho de la cinta [m]
PROF_BANDA_M = 0.5    # profundidad de la cinta bajo la cota [m]


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


def _quitar_bom(t):
    if not t:
        return t
    if t[0] == u"\uFEFF":
        return t[1:]
    if t[:3] == u"\u00EF\u00BB\u00BF":
        return t[3:]
    return t


# ============================================================================
# LECTOR CANONICO DE JSON (v2026-09-29)
#   utf-8 estricto (con/sin BOM) -> cp1252 -> latin-1. AVISO ruidoso si no
#   fue utf-8; error explicito con hex de cabecera si todo falla.
# ============================================================================
def _leer_json_canonico(ruta, etiqueta="contexto"):
    ruta_s = str(ruta)
    if not ruta or not System.IO.File.Exists(ruta_s):
        raise Exception("El archivo no existe en la ruta especificada: {}".format(ruta))
    bruto = System.IO.File.ReadAllBytes(ruta_s)
    err_utf8 = ""
    err_cp1252 = ""
    # 1) UTF-8 estricto
    try:
        contenido = _quitar_bom(System.Text.UTF8Encoding(False, True).GetString(bruto))
        return json.loads(contenido)
    except Exception as e_utf8:
        err_utf8 = str(e_utf8)
    # 2) CP1252 (legacy Windows; 0xF3 -> 'o' con tilde)
    try:
        contenido = _quitar_bom(System.Text.Encoding.GetEncoding(1252).GetString(bruto))
        data = json.loads(contenido)
        print("[AVISO ENCODING] {}: leido como cp1252 (no utf-8); normalizar el archivo: {}".format(etiqueta, ruta_s))
        return data
    except Exception as e_cp1252:
        err_cp1252 = str(e_cp1252)
    # 3) Latin-1 (ultimo recurso; byte a byte nunca falla)
    try:
        contenido = _quitar_bom(System.Text.Encoding.GetEncoding(28591).GetString(bruto))
        data = json.loads(contenido)
        print("[AVISO ENCODING] {}: leido como latin-1 (ultimo recurso): {}".format(etiqueta, ruta_s))
        return data
    except Exception as e_latin1:
        cab = []
        for i in range(min(24, len(bruto))):
            cab.append("%02X" % (bruto[i] if isinstance(bruto[i], int) else ord(bruto[i])))
        raise Exception("No se pudo decodificar {} ({}). Primeros bytes: [{}]. utf8={} | cp1252={} | latin1={}".format(
            etiqueta, ruta_s, " ".join(cab), err_utf8, err_cp1252, str(e_latin1)))


def _idw_z(gx, gy, pts):
    """Cota IDW (misma interpolacion del MDT usada por ETAPA1 v05)."""
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


def banda_drapeada(coords, dx, dy, dz, pts_mdt, ancho=ANCHO_BANDA_M, prof=PROF_BANDA_M, cerrada=True):
    """Cinta 3D solida que sigue el MDT a lo largo de una polilinea."""
    if not coords or len(coords) < 2 or not pts_mdt:
        return None
    p = [(c[0] - dx, c[1] - dy) for c in coords]
    if cerrada and p[0] != p[-1]:
        p.append(p[0])
    n = len(p)
    left = []
    right = []
    for i in range(n):
        i0 = i - 1 if i > 0 else (n - 2 if cerrada else 0)
        i1 = i + 1 if i < n - 1 else (1 if cerrada else n - 1)
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
    seg = n if cerrada else n - 1
    for i in range(seg):
        j = (i + 1) % n
        m.Faces.AddFace(zl[i], zr[i], zr[j], zl[j])
        m.Faces.AddFace(zlb[i], zlb[j], zrb[j], zrb[i])
        m.Faces.AddFace(zl[i], zlb[i], zlb[j], zl[j])
        m.Faces.AddFace(zr[i], zr[j], zrb[j], zrb[i])
    if not cerrada:
        m.Faces.AddFace(zl[0], zr[0], zrb[0], zlb[0])
        m.Faces.AddFace(zl[n - 1], zr[n - 1], zrb[n - 1], zlb[n - 1])
    m.Normals.ComputeNormals()
    m.Compact()
    return m


def curva_drapeada(coords, dx, dy, dz, pts_mdt, cerrada=True):
    """v01: polilinea 3D (z = IDW del MDT por vertice) para nodos Morph Curve."""
    if not coords or len(coords) < 2 or not pts_mdt:
        return None
    p = [(c[0] - dx, c[1] - dy) for c in coords]
    if cerrada and p[0] != p[-1]:
        p.append(p[0])
    poly = rg.Polyline()
    for (px, py) in p:
        poly.Add(px, py, _idw_z(px, py, pts_mdt))
    if not poly.IsClosed and cerrada:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def bandas_por_categoria(listas_coords, dx, dy, dz, pts_mdt, cerrada=True):
    out = []
    for coords in listas_coords:
        b = banda_drapeada(coords, dx, dy, dz, pts_mdt, cerrada=cerrada)
        if b is not None:
            out.append(b)
    return out


def curvas_por_categoria(listas_coords, dx, dy, dz, pts_mdt, cerrada=True):
    out = []
    for coords in listas_coords:
        c = curva_drapeada(coords, dx, dy, dz, pts_mdt, cerrada=cerrada)
        if c is not None:
            out.append(c)
    return out


def _rectangulo_horizontal(x0, y0, x1, y1, z=0.0):
    """v01: contorno rectangular cerrado y horizontal (boundary del nodo Mesh)."""
    poly = rg.Polyline()
    poly.Add(x0, y0, z)
    poly.Add(x1, y0, z)
    poly.Add(x1, y1, z)
    poly.Add(x0, y1, z)
    poly.Add(x0, y0, z)
    return rg.PolylineCurve(poly)


# ==============================================================================
# MAIN
# ==============================================================================

json_path_raw = globals().get("json_path", None)
json_path = str(unwrap(json_path_raw)).strip("[]'\" ") if json_path_raw else ""
mostrar_curvas = parse_bool(globals().get("mostrar_curvas", None), True)
mostrar_cintas = parse_bool(globals().get("mostrar_cintas", None), True)

# Inicializar salidas
bandas_lote = None
bandas_vecinos = []
bandas_vias = []
bandas_ep = []
bandas_todas = []
curvas_lote = []
curvas_vecinos = []
curvas_vias = []
curvas_ep = []
topo_pts = []
topo_boundary = None
mensaje = ""

if not json_path or not os.path.exists(json_path):
    mensaje = "ETAPA1-3D v01 | ERROR: No se encontro el JSON: {}".format(json_path)
else:
    try:
        data = _leer_json_canonico(json_path, "contexto-3d")

        # --- Anclaje: vertice SE del lote (regla ETAPA1) ---
        lote_verts = data.get("lote_objetivo", {}).get("vertices_3d_local", [])
        if lote_verts and len(lote_verts) >= 3:
            anchor = lote_verts[0]
            for v in lote_verts:
                if v[1] < anchor[1] - 0.01 or (abs(v[1] - anchor[1]) < 0.01 and v[0] > anchor[0]):
                    anchor = v
            dx, dy, dz = anchor[0], anchor[1], anchor[2]
        else:
            dx, dy, dz = 0.0, 0.0, 0.0

        # --- MDT en marco canvas ---
        topo = data.get("topografia", {})
        mesh_points = topo.get("malla_terreno", [])
        pts_mdt = []
        for mp in mesh_points:
            pts_mdt.append((mp["x_local"] - dx, mp["y_local"] - dy, mp["z_local"] - dz))

        if pts_mdt:
            # terreno para el nodo Mesh de la Live Connection
            for (px, py, pz) in pts_mdt:
                topo_pts.append(rg.Point3d(px, py, pz))
            xs = [p[0] for p in pts_mdt]
            ys = [p[1] for p in pts_mdt]
            topo_boundary = _rectangulo_horizontal(min(xs), min(ys), max(xs), max(ys), 0.0)

            # --- 3D: curvas drapeadas (Morph Curve) ---
            if mostrar_curvas:
                if lote_verts:
                    c = curva_drapeada(lote_verts, dx, dy, dz, pts_mdt, cerrada=True)
                    if c is not None:
                        curvas_lote = [c]
                curvas_vecinos = curvas_por_categoria(
                    [v.get("vertices_3d_local", []) for v in data.get("vecinos", [])],
                    dx, dy, dz, pts_mdt, cerrada=True)
                curvas_vias = curvas_por_categoria(
                    [v.get("coordenadas_local", []) for v in data.get("vias_oficiales", [])],
                    dx, dy, dz, pts_mdt, cerrada=False)
                curvas_ep = curvas_por_categoria(
                    [e.get("coordenadas_local", []) for e in data.get("espacios_publicos", [])],
                    dx, dy, dz, pts_mdt, cerrada=True)

            # --- 3D: bandas drapeadas (Morph Solid) ---
            if mostrar_cintas:
                if lote_verts:
                    bandas_lote = banda_drapeada(lote_verts, dx, dy, dz, pts_mdt, cerrada=True)
                bandas_vecinos = bandas_por_categoria(
                    [v.get("vertices_3d_local", []) for v in data.get("vecinos", [])],
                    dx, dy, dz, pts_mdt, cerrada=True)
                bandas_vias = bandas_por_categoria(
                    [v.get("coordenadas_local", []) for v in data.get("vias_oficiales", [])],
                    dx, dy, dz, pts_mdt, cerrada=False)
                bandas_ep = bandas_por_categoria(
                    [e.get("coordenadas_local", []) for e in data.get("espacios_publicos", [])],
                    dx, dy, dz, pts_mdt, cerrada=True)
                if bandas_lote is not None:
                    bandas_todas.append(bandas_lote)
                bandas_todas = bandas_todas + bandas_vecinos + bandas_vias + bandas_ep
        else:
            mensaje = "ETAPA1-3D v01 | AVISO: JSON sin malla de terreno (no hay drapeo 3D)"

        chip = data.get("metadata", {}).get("chip", "DESCONOCIDO")
        mensaje = ("ETAPA1-3D v01 | CHIP: {} | curvas: {} (lote {} / vec {} / vias {} / ep {}) | "
                   "cintas: {} (lote {} / vec {} / vias {} / ep {}) | MDT pts: {} | anclaje: ({:.1f}, {:.1f})").format(
            chip,
            "ON" if mostrar_curvas else "OFF", 1 if curvas_lote else 0, len(curvas_vecinos), len(curvas_vias), len(curvas_ep),
            "ON" if mostrar_cintas else "OFF", 1 if bandas_lote is not None else 0, len(bandas_vecinos), len(bandas_vias), len(bandas_ep),
            len(pts_mdt), dx, dy)

    except Exception as e:
        error_type = type(e).__name__
        mensaje = "ETAPA1-3D v01 | ERROR al leer JSON: [{}] {} | json_path='{}' | file_exists={}".format(
            error_type, str(e), json_path, os.path.exists(json_path) if json_path else False)
