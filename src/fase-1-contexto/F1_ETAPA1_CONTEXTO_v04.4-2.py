"""
================================================================================
F1_ETAPA1_CONTEXTO_v04.4.1.py — Etapa 1: Datos en bruto → Geometria + Capas
Correccion v04.4.1: bytes legacy a Unicode explicito y diagnostico por etapa
con traceback. Sin cambios de entradas/salidas; pendiente prueba IronPython.
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

CAMBIO v04.4 PROPUESTA (no validada en Rhino):
  Texto Unicode compatible con IronPython; conserva pot_data completo y
  distingue antejardin ausente de cero. Areas viales por offsets y cierres
  RhinoCommon; sin ancho/buffer valido entrega SOLO eje, nunca falsa area.
  El ancho global de vias del contexto es referencia, no ancho del frente.

PROPOSITO:
  Etapa 1 del pipeline v26. Lee el JSON de contexto v6 y entrega TODA la
  geometria en bruto organizada por CAPA DESTINO, lista para enviar a
  ArchiCAD via Tapir.

  El flujo posterior es MANUAL en ArchiCAD: se clasifican los poligonos
  (vias, andenes, zonas verdes, predios vecinos) en los layers creados,
  y se construyen los Morphs de volumetrias vecinas.

CAMBIOS v04.1 (2026-09-21):
  GARANTIA DEL LAYER DEL LOTE: el layer "00-00-10_Lote_proyecto" queda
  asegurado en layers_json con merge defensivo (si faltara en la lista
  estandar se re-inserta como primer elemento) y se expone la salida
  booleana layer_lote_ok.

  DERIVACION REGLAMENTARIA (ampliado 2026-08-15): nuevas salidas
  ancho_via_oficial_m, tipologia_oficial y reglamentacion_json para que
  F1_ETAPA2_NORMATIVA_v05 pueda sacar tipologia/ancho_via_m/antejardin_m
  directamente de la reglamentacion cuando las entradas del operador son
  nulas o 0. Nota: la fuente POT actual (fetch-urban-context-v6) trae
  ancho: null en las vias y NO trae tipologia ni antejardin (mapas
  CU-5.4.2-33 y CU-5.5, raster) -> las salidas quedan vacias/0 hasta que
  la fuente los provea; NORMATIVA_v05 avisa y usa los defaults.

  COMPATIBILIDAD ARCHICAD: Curvas 2D en lugar de PolylineCurve para mejor
  compatibilidad con ArchiCAD Tapir.

CAMBIO v04.2 (2026-09-28, noche):
  APLANADO A PLANO HORIZONTAL (Z=0 del marco local): las curvas de salida
  (lot_curve, vecinos_curves, vias_oficiales, ejes_vias_curves,
  espacios_publicos) se emiten con Z constante para cumplir el requisito de
  la Live Connection Grasshopper-ArchiCAD (Invalid Curve value. It must be
  in a horizontal plane): los nodos 2D Polyline / Mesh exigen curva cerrada
  y en plano horizontal. Con lotes inclinados (z por vertice) la curva no
  era horizontal y el nodo rechazaba. El relieve del terreno se conserva
  aparte en topo_mesh (que NO se aplana).

CAMBIO v04.3 (2026-09-29):
  LECTOR CANONICO DE JSON: lectura por bytes con cascada utf-8 estricto (con
  o sin BOM) -> cp1252 -> latin-1, con AVISO ruidoso si no fue utf-8 y error
  explicito (hex de cabecera) si todo falla. Motivo: error UnicodeDecodeError
  ('unknown' codec / byte 0xF3, posicion 11) observado en corrida real del
  canvas; mecanismo reproducido bajo IronPython el 2026-09-29 (decodificacion
  UTF-8 estricta de contenido cp1252). Salidas SIN cambios respecto a v04.2.

ENTRADAS:
  json_path (String) — Ruta al <CHIP>-contexto.json

SALIDAS (agrupadas por capa destino):
  LOTE:        lot_curve (Curve) + lot_area (Number)
  VECINOS:     vecinos_curves (Curve[]) — capa "predios vecinos"
  VIAS:        vias_oficiales (Curve[]) — capa 00-20-20_Elementos_entorno_urbano (áreas de vía)
  EJES_VIAS:   ejes_vias_curves (Curve[]) — capa 00-20-30_Ejes_vias (ejes de vía)
  ESPACIOS:    espacios_publicos (Curve[]) — capa 70-50-10_Zonas_verdes_publicas
  TOPO:        topo_mesh (Mesh) — capa 10-20-10_Topografia
  NORMATIVA:   altura_max_pot, tratamiento, rango_edificabilidad,
               sector_normativo, upz, io_normativo
  REGLAMENTO:  ancho_via_oficial_m (Number), tipologia_oficial (String),
               reglamentacion_json (String — pot_data + derivados para
               NORMATIVA_v05)
  LAYERS:      layers_json (String) — lista de capas a crear en ArchiCAD
               layer_lote_ok (Boolean) — True si 00-00-10_Lote_proyecto existe
  MENSAJE:     mensaje (String)

CAPAS ARCHICAD (creadas via Tapir):
  00-00-10_Lote_proyecto
  00-20-20_Elementos_entorno_urbano   (áreas de vía)
  00-20-30_Ejes_vias                  (ejes de vía)
  70-50-10_Zonas_verdes_publicas      (parques/plazas)
  70-30-20_Andenes_preexistentes
  10-20-10_Topografia
  70-20-30_Volumetrias_vecinas        (Morphs manuales)
  00-10-20_Elementos_referencia
  00-20-20_Foto_Aerea_Referencia
================================================================================
"""


import Rhino.Geometry as rg
import json
import io
import os
import math
import System.IO
import System.Text
import traceback


try:
    text_type = unicode
except NameError:
    text_type = str


def texto(val):
    """Decodifica bytes explicitamente; no usa el codec implicito de IronPython."""
    if val is None:
        return u""
    if isinstance(val, text_type):
        return val
    if isinstance(val, bytes):
        for enc in ("utf-8-sig", "cp1252", "latin-1"):
            try:
                return val.decode(enc)
            except UnicodeError:
                pass
    return text_type(val)


def area_vial_desde_eje(eje, ancho):
    """Franja aproximada XY por offsets; no sustituye poligono oficial.
    Rechaza offsets fragmentados/autointersectantes; no genera eje como area.
    """
    curvas = []
    for signo in (1.0, -1.0):
        offsets = eje.Offset(rg.Plane.WorldXY, signo * ancho / 2.0,
                             0.01, rg.CurveOffsetCornerStyle.Sharp)
        if not offsets or len(offsets) != 1:
            return None
        curvas.append(offsets[0])
    a, b = curvas
    cap_fin = rg.LineCurve(a.PointAtEnd, b.PointAtEnd)
    cap_inicio = rg.LineCurve(b.PointAtStart, a.PointAtStart)
    joined = rg.Curve.JoinCurves([a, cap_fin, b, cap_inicio], 0.01)
    if not joined or len(joined) != 1 or not joined[0].IsClosed:
        return None
    result = joined[0]
    events = rg.Intersect.Intersection.CurveSelf(result, 0.01)
    if events and events.Count > 0:
        return None
    props = rg.AreaMassProperties.Compute(result)
    return result if props and props.Area > 0.01 else None


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def to_float_safe(val, default=0.0):
    if val is None: return default
    try: return float(val)
    except: return default


def polyline_from_coords(coords, dx, dy, dz):
    """Convierte [[x,y,z],...] en PolylineCurve con offset."""
    if not coords or len(coords) < 3:
        return None
    poly = rg.Polyline()
    for c in coords:
        poly.Add(c[0] - dx, c[1] - dy, 0.0)  # v04.2: plano horizontal (Live Connection)
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def polyline_to_nurbs(poly_curve):
    """Convierte una PolylineCurve a NurbsCurve para mejor compatibilidad con ArchiCAD."""
    if poly_curve is None:
        return None
    if isinstance(poly_curve, rg.PolylineCurve):
        return poly_curve.ToNurbsCurve()
    return poly_curve


def build_terrain_mesh(mesh_points, dx, dy, dz):
    """Malla de terreno por interpolacion IDW sobre grilla ~5m."""
    if not mesh_points or len(mesh_points) < 3:
        return None

    pts = []
    for p in mesh_points:
        pts.append((p["x_local"] - dx, p["y_local"] - dy, p["z_local"] - dz))

    min_x = min(p[0] for p in pts)
    max_x = max(p[0] for p in pts)
    min_y = min(p[1] for p in pts)
    max_y = max(p[1] for p in pts)

    res = 5.0
    cols = max(2, int((max_x - min_x) / res) + 1)
    rows = max(2, int((max_y - min_y) / res) + 1)

    mesh = rg.Mesh()
    grid_pts = []
    for r in range(rows):
        for c in range(cols):
            gx = min_x + c * (max_x - min_x) / max(1, cols - 1)
            gy = min_y + r * (max_y - min_y) / max(1, rows - 1)
            gz = 0.0
            total_w = 0.0
            for px, py, pz in pts:
                dist = math.sqrt((gx - px) ** 2 + (gy - py) ** 2)
                if dist < 0.01:
                    gz = pz
                    total_w = 1.0
                    break
                w = 1.0 / max(0.1, dist * dist)
                gz += pz * w
                total_w += w
            if total_w > 0:
                gz /= total_w
            idx = mesh.Vertices.Add(gx, gy, gz)
            grid_pts.append(idx)

    for r in range(rows - 1):
        for c in range(cols - 1):
            a = grid_pts[r * cols + c]
            b = grid_pts[r * cols + c + 1]
            cc = grid_pts[(r + 1) * cols + c]
            d = grid_pts[(r + 1) * cols + c + 1]
            mesh.Faces.AddFace(a, b, d)
            mesh.Faces.AddFace(a, d, cc)

    mesh.Normals.ComputeNormals()
    mesh.Compact()
    return mesh


def garantizar_layer_lote(layers):
    """v04: asegura que 00-00-10_Lote_proyecto este en la lista (primer item).

    Retorna (layers_ok, bool). El layer es el primero de la norma del
    proyecto; si falta (p.ej. lista editada manualmente), se re-inserta.
    """
    LOTE = {"nombre": "00-00-10_Lote_proyecto", "color": 1, "visible": True}
    for layer in layers:
        nombre = texto(layer.get("nombre", "")).strip()
        if nombre == LOTE["nombre"]:
            return layers, True
    layers.insert(0, dict(LOTE))
    return layers, True


def _quitar_bom(t):
    """v04.3: quita BOM utf-8 (U+FEFF) o su lectura literal en cp1252/latin-1."""
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
#   fue utf-8; error explicito con hex de cabecera si todo falla. Política de
#   proyecto: los escritores nuevos emiten UTF-8 explicito / ASCII-safe.
# ============================================================================
def _leer_json_canonico(ruta, etiqueta="contexto"):
    ruta_s = texto(ruta)
    if not ruta or not System.IO.File.Exists(ruta_s):
        raise Exception("El archivo no existe en la ruta especificada: {}".format(ruta))
    bruto = System.IO.File.ReadAllBytes(ruta_s)
    err_utf8 = ""
    err_cp1252 = ""
    # 1) UTF-8 estricto (tolera BOM)
    try:
        contenido = _quitar_bom(System.Text.UTF8Encoding(False, True).GetString(bruto))
        return json.loads(contenido)
    except Exception as e_utf8:
        err_utf8 = texto(e_utf8)
    # 2) CP1252 (legacy Windows; 0xF3 -> 'o' con tilde)
    try:
        contenido = _quitar_bom(System.Text.Encoding.GetEncoding(1252).GetString(bruto))
        data = json.loads(contenido)
        print("[AVISO ENCODING] {}: leido como cp1252 (no utf-8); normalizar el archivo: {}".format(etiqueta, ruta_s))
        return data
    except Exception as e_cp1252:
        err_cp1252 = texto(e_cp1252)
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
        raise Exception(u"No se pudo decodificar {} ({}). Primeros bytes: [{}]. utf8={} | cp1252={} | latin1={}".format(
            etiqueta, ruta_s, " ".join(cab), err_utf8, err_cp1252, texto(e_latin1)))


def leer_json_seguro(ruta):
    """Compat v04.3: wrapper del lector canonico (nombre historico)."""
    return _leer_json_canonico(ruta, "contexto")


# ==============================================================================
# MAIN
# ==============================================================================

json_path_raw = globals().get("json_path", None)
json_path = texto(unwrap(json_path_raw)).strip(u"[]'\" ") if json_path_raw else u""

# Inicializar salidas
lot_curve = None
lot_area = 0.0
vecinos_curves = []
vias_oficiales = []  # Áreas de vía (para capa 00-20-20_Elementos_entorno_urbano)
ejes_vias_curves = []  # Ejes de vía (para capa 00-20-30_Ejes_vias)
espacios_publicos = []
topo_mesh = None
altura_max_pot = 11.4
tratamiento = "Consolidacion"
rango_edificabilidad = "3"
sector_normativo = ""
upz = "N/A"
io_normativo = 0.70
origen_x = 0.0
origen_y = 0.0
layers_json = ""
layer_lote_ok = False
ancho_via_oficial_m = 0.0
tipologia_oficial = ""
reglamentacion_json = ""
avisos = []

LAYERS_ARCHICAD = [
    {"nombre": "00-00-10_Lote_proyecto", "color": 1, "visible": True},
    {"nombre": "00-20-20_Elementos_entorno_urbano", "color": 2, "visible": True},
    {"nombre": "00-20-30_Ejes_vias", "color": 8, "visible": True},
    {"nombre": "70-50-10_Zonas_verdes_publicas", "color": 3, "visible": True},
    {"nombre": "70-30-20_Andenes_preexistentes", "color": 4, "visible": True},
    {"nombre": "10-20-10_Topografia", "color": 5, "visible": True},
    {"nombre": "70-20-20_Perimetros_vecinos", "color": 9, "visible": True},
    {"nombre": "70-20-30_Volumetrias_vecinas", "color": 6, "visible": True},
    {"nombre": "00-10-20_Elementos_referencia", "color": 7, "visible": True},
    {"nombre": "00-20-20_Foto_Aerea_Referencia", "color": 5, "visible": True},
]

etapa_actual = "ruta"
if not json_path or not os.path.exists(json_path):
    mensaje = "ETAPA1 | ERROR: No se encontro el JSON: {}".format(json_path)
else:
    try:
        # Uso principal de la función segura:
        etapa_actual = "lectura/decodificacion JSON"
        data = leer_json_seguro(json_path)
        if not isinstance(data, dict):
            raise ValueError("La raiz del JSON debe ser un objeto")
        etapa_actual = "geometria y anclaje"

        # --- Anclaje: vertice SE del lote (min Y, max X) ---
        lote_verts = data.get("lote_objetivo", {}).get("vertices_3d_local", [])
        if lote_verts and len(lote_verts) >= 3:
            anchor = lote_verts[0]
            for v in lote_verts:
                if v[1] < anchor[1] - 0.01 or (abs(v[1] - anchor[1]) < 0.01 and v[0] > anchor[0]):
                    anchor = v
            dx, dy, dz = anchor[0], anchor[1], anchor[2]
        else:
            dx, dy, dz = 0.0, 0.0, 0.0

        meta = data.get("metadata", {})
        origen_sirgas = meta.get("origen_sirgas", {})
        origen_x = origen_sirgas.get("x", 0.0)
        origen_y = origen_sirgas.get("y", 0.0)

        # --- LOTE ---
        lot_curve_raw = polyline_from_coords(lote_verts, dx, dy, dz)
        lot_curve = polyline_to_nurbs(lot_curve_raw)  # Convert to NURBS for better ArchiCAD compatibility
        lot_area = to_float_safe(data.get("lote_objetivo", {}).get("area_m2"), 0.0)

        # --- VECINOS ---
        vecinos_curves = []
        for v in data.get("vecinos", []):
            crv_raw = polyline_from_coords(v.get("vertices_3d_local", []), dx, dy, dz)
            crv = polyline_to_nurbs(crv_raw)  # Convert to NURBS for better ArchiCAD compatibility
            if crv:
                vecinos_curves.append(crv)

        # --- VIAS (Ejes de vía y áreas de vía) ---
        ejes_vias_curves = []
        vias_oficiales_buffered = []

        for via in data.get("vias_oficiales", []):
            coords = via.get("coordenadas_local", [])
            ancho_via = to_float_safe(via.get("ancho"), 0.0)

            if len(coords) >= 2:
                # Crear la polilínea central (eje de vía)
                poly = rg.Polyline()
                for c in coords:
                    poly.Add(c[0] - dx, c[1] - dy, 0.0)  # v04.2: plano horizontal (Live Connection)
                poly_curve = rg.PolylineCurve(poly)
                nurbs_curve = polyline_to_nurbs(poly_curve)  # Convert to NURBS for better ArchiCAD compatibility
                ejes_vias_curves.append(nurbs_curve)

                if ancho_via > 0:
                    try:
                        area_vial = area_vial_desde_eje(poly_curve, ancho_via)
                        if area_vial is not None:
                            vias_oficiales_buffered.append(area_vial)
                        else:
                            avisos.append(u"area vial aproximada rechazada; eje conservado")
                    except Exception as e:
                        avisos.append(u"offset vial fallido: {}".format(texto(e)))
                else:
                    avisos.append(u"via sin ancho: solo eje, sin area vial")

        vias_oficiales = vias_oficiales_buffered

        # --- ESPACIOS PUBLICOS ---
        espacios_publicos = []
        for ep in data.get("espacios_publicos", []):
            coords = ep.get("coordenadas_local", [])
            crv_raw = polyline_from_coords(coords, dx, dy, dz)
            crv = polyline_to_nurbs(crv_raw)  # Convert to NURBS for better ArchiCAD compatibility
            if crv:
                espacios_publicos.append(crv)

        # --- TOPOGRAFIA ---
        topo = data.get("topografia", {})
        mesh_points = topo.get("malla_terreno", [])
        topo_mesh = build_terrain_mesh(mesh_points, dx, dy, dz) if mesh_points else None

        # --- NORMATIVA ---
        etapa_actual = "datos normativos"
        pd = data.get("pot_data", {})
        if not isinstance(pd, dict):
            raise ValueError("pot_data debe ser un objeto")
        altura_max_pot = to_float_safe(pd.get("altura_maxima_m"), 11.4)
        tratamiento = texto(pd.get("tratamiento", "Consolidacion"))
        rango_edificabilidad = texto(pd.get("rango_edificabilidad", "3"))
        sector_normativo = texto(pd.get("sector_normativo", ""))
        upz = texto(pd.get("upz", "N/A"))
        io_normativo = to_float_safe(pd.get("io_maximo"), 0.70)

        # --- REGLAMENTACION JSON (para NORMATIVA_v05) ---
        # Deriva de la reglamentacion lo que la fuente POT provea:
        # hoy ancho: null y sin tipologia/antejardin (mapas raster).
        anchos = [to_float_safe(v.get("ancho"), 0.0)
                  for v in data.get("vias_oficiales", [])]
        anchos = [a for a in anchos if a > 0]
        ancho_via_oficial_m = min(anchos) if anchos else 0.0
        tipologia_oficial = texto(pd.get("tipologia", "") or "").strip()
        # Conservar pisos totales, fuentes, aprobaciones y campos desconocidos.
        # No inventar antejardin cero ni ancho de frente a partir de vias lejanas.
        etapa_actual = "serializacion reglamentacion"
        reglamento = dict(pd)
        reglamentacion_json = json.dumps({
            "pot_data": reglamento,
            "metadata": {"chip": meta.get("chip"),
                         "fuente_contexto": json_path,
                         "anclaje_local": [dx, dy, dz]},
        }, ensure_ascii=True)

        # --- LAYERS JSON (para Tapir) — v04: garantizar layer del lote ---
        etapa_actual = "layers"
        LAYERS_ARCHICAD, layer_lote_ok = garantizar_layer_lote(LAYERS_ARCHICAD)
        layers_json = json.dumps(LAYERS_ARCHICAD)

        etapa_actual = "mensaje final"
        chip = texto(meta.get("chip", "DESCONOCIDO"))
        mensaje = u"ETAPA1 v04.4.1 | CHIP: {} | Area: {:.1f}m2 | Vecinos: {} | Vias: {} | EP: {} | Origen: ({:.1f}, {:.1f}) | Lote_layer: {} | Reg: ancho_via={} tipologia={}".format(
            chip, lot_area, len(vecinos_curves), len(vias_oficiales),
            len(espacios_publicos), dx, dy,
            "OK" if layer_lote_ok else "FALTA",
            ancho_via_oficial_m or "sin dato",
            tipologia_oficial or "sin dato")
        if avisos:
            mensaje += u" | AVISOS: " + u"; ".join(sorted(set(avisos)))

    except Exception as e:
        # Mensaje de error más detallado para debug
        error_type = type(e).__name__
        error_msg = texto(e)
        mensaje = u"ETAPA1 v04.4.1 | ERROR en {}: [{}] {} | json_path='{}' | file_exists={}".format(
            etapa_actual, error_type, error_msg, json_path, os.path.exists(json_path) if json_path else False)
        try:
            mensaje += u" | TRACE: " + texto(traceback.format_exc()).replace(u"\n", u" / ")
        except Exception:
            pass