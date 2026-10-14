"""
================================================================================
F1_ETAPA1_CONTEXTO_v02.py — Etapa 1: Datos en bruto → Geometria + Capas
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Etapa 1 del pipeline v26. Lee el JSON de contexto v6 y entrega TODA la
  geometria en bruto organizada por CAPA DESTINO, lista para enviar a
  ArchiCAD via Tapir.

  El flujo posterior es MANUAL en ArchiCAD: se clasifican los poligonos
  (vias, andenes, zonas verdes, predios vecinos) en los layers creados,
  y se construyen los Morphs de volumetrias vecinas.

CAMBIOS v02.3 (2026-10-13):
  - Z_BASE CORRECTO (Mínimo Z válido del terreno): prioridad min_z válido malla
    terreno (punto más bajo lote) -> promedio vecinos N/S -> ancla SE -> 0.0.
  - Geometría en LOCAL Z: todas las salidas (lote, vecinos, vías, EP, topografía)
    usan Z_local = Z_absoluto - Z_base. SE corner = (0,0,0). Terreno empieza en ~0.
  - Coherencia total con F1_CONTEXTO50_BUILD v01.3 y F3_VOLUM_GENERADOR v08.1.

CAMBIOS v02.2 (2026-10-13):
  - Se corrigió el origen Z (dz) para tomar el punto más bajo de la malla de terreno
    (min_z) cuando está disponible. Si existen vecinos al norte y al sur del lote,
    se toma la media de sus cotas Z promedio (más cercana en cada dirección) para
    definir dz, asegurando mejor alineación con el contexto urbano. Se mantiene dx, dy
    del vértice SE del lote.

CAMBIOS v02.1 (2026-10-13):
  - Se corrigió el origen Z (dz) para tomar el punto más bajo de la malla de terreno
    (min_z) cuando está disponible, asegurando que el sistema de coordenadas locales
    tenga Z=0 en el terreno y evitando valores negativos. Se mantuvo dx, dy del
    vértice SE del lote.

CAMBIOS v02 (2026-08-15):
  GARANTIA DEL LAYER DEL LOTE: el layer "00-00-10_Lote_proyecto" queda
  asegurado en layers_json con merge defensivo (si faltara en la lista
  estandar se re-inserta como primer elemento) y se expone la salida
  booleana layer_lote_ok. Responde a la solicitud del usuario: el layer
  del lote debe estar incluido en el script de arranque.

  DERIVACION REGLAMENTARIA (ampliado 2026-08-15): nuevas salidas
  ancho_via_oficial_m, tipologia_oficial y reglamentacion_json para que
  F1_ETAPA2_NORMATIVA_v05 pueda sacar tipologia/ancho_via_m/antejardin_m
  directamente de la reglamentacion cuando las entradas del operador son
  nulas o 0. Nota: la fuente POT actual (fetch-urban-context-v6) trae
  ancho: null en las vias y NO trae tipologia ni antejardin (mapas
  CU-5.4.2-33 y CU-5.5, raster) -> las salidas quedan vacias/0 hasta que
  la fuente los provea; NORMATIVA_v05 avisa y usa los defaults.

ENTRADAS:
  json_path (String) — Ruta al <CHIP>-contexto.json

SALIDAS (agrupadas por capa destino):
  LOTE:        lot_curve (Curve) + lot_area (Number)
  VECINOS:     vecinos_curves (Curve[]) — capa "predios vecinos"
  VIAS:        vias_oficiales (Curve[]) — capa 00-20-20_Elementos_entorno_urbano
  ESPACIOS:    espacios_publicos (Curve[]) — capa 70-50-10_Zonas_verdes_publicas
  TOPO:        topo_mesh (Mesh) — capa 10-20-10_Topografia
  NORMATIVA:   altura_max_pot, tratamiento, rango_edificabilidad,
               sector_normativo, upz, io_normativo
  ORIGEN:      origen_x, origen_y (SIRGAS del anclaje SE)
  REGLAMENTO:  ancho_via_oficial_m (Number), tipologia_oficial (String),
               reglamentacion_json (String — pot_data + derivados para
               NORMATIVA_v05)
  LAYERS:      layers_json (String) — lista de capas a crear en ArchiCAD
               layer_lote_ok (Boolean) — True si 00-00-10_Lote_proyecto existe
  MENSAJE:     mensaje (String)

CAPAS ARCHICAD (creadas via Tapir):
  00-00-10_Lote_proyecto
  00-20-20_Elementos_entorno_urbano   (vias)
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


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def to_float_safe(val, default=0.0):
    if val is None: return default
    try: return float(val)
    except: return default


def polyline_from_coords(coords, dx, dy, dz):
    """Convierte [[x,y,z],...] en PolylineCurve con offset. Z ya en local (Z_abs - dz)."""
    if not coords or len(coords) < 3:
        return None
    poly = rg.Polyline()
    for c in coords:
        poly.Add(c[0] - dx, c[1] - dy, c[2] - dz)
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def build_terrain_mesh(mesh_points, dx, dy, dz):
    """Malla de terreno por interpolacion IDW sobre grilla ~5m. Z ya en local."""
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
    """v02: asegura que 00-00-10_Lote_proyecto este en la lista (primer item).

    Retorna (layers_ok, bool). El layer es el primero de la norma del
    proyecto; si falta (p.ej. lista editada manualmente), se re-inserta.
    """
    LOTE = {"nombre": "00-00-10_Lote_proyecto", "color": 1, "visible": True}
    for layer in layers:
        nombre = str(layer.get("nombre", "")).strip()
        if nombre == LOTE["nombre"]:
            return layers, True
    layers.insert(0, dict(LOTE))
    return layers, True


# ==============================================================================
# MAIN
# ==============================================================================

json_path_raw = globals().get("json_path", None)
json_path = str(unwrap(json_path_raw)).strip("[]'\" ") if json_path_raw else ""

# Inicializar salidas
lot_curve = None
lot_area = 0.0
vecinos_curves = []
vias_oficiales = []
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

if not json_path or not os.path.exists(json_path):
    mensaje = "ETAPA1 | ERROR: No se encontro el JSON: {}".format(json_path)
else:
    try:
        # Función para leer JSON soportando rutas y contenidos con tildes y eñes en IronPython
        def leer_json_seguro(ruta):
            """Lee archivos JSON soportando rutas y contenidos con tildes y eñes en IronPython."""
            if not ruta or not System.IO.File.Exists(str(ruta)):
                raise Exception("El archivo no existe en la ruta especificada: {}".format(ruta))

            # 1. Intento con UTF-8
            try:
                contenido = System.IO.File.ReadAllText(str(ruta), System.Text.Encoding.UTF8)
                return json.loads(contenido)
            except Exception as e_utf8:
                # 2. Fallback a codificación por defecto de Windows (CP1252 / Latin-1)
                try:
                    contenido = System.IO.File.ReadAllText(str(ruta), System.Text.Encoding.Default)
                    return json.loads(contenido)
                except Exception as e_default:
                    raise Exception("Error al decodificar el archivo: {} | {}".format(e_utf8, e_default))

        # Uso principal:
        data = leer_json_seguro(json_path)

        # --- TOPOGRAFIA ---
        topo = data.get("topografia", {})
        mesh_points = topo.get("malla_terreno", [])

        # Compute min_z from mesh_points if available (ignore near-zero values)
        if mesh_points:
            mesh_zs = [p["z_local"] for p in mesh_points]
            # Filter out near-zero values (likely invalid/placeholder points)
            valid_zs = [z for z in mesh_zs if abs(z) > 0.001]
            if valid_zs:
                min_z = min(valid_zs)
            else:
                min_z = 0.0
        else:
            min_z = 0.0

        # --- Anclaje: vertice SE del lote (min Y, max X) ---
        lote_verts = data.get("lote_objetivo", {}).get("vertices_3d_local", [])
        if lote_verts and len(lote_verts) >= 3:
            anchor = lote_verts[0]
            for v in lote_verts:
                if v[1] < anchor[1] - 0.01 or (abs(v[1] - anchor[1]) < 0.01 and v[0] > anchor[0]):
                    anchor = v
            dx, dy = anchor[0], anchor[1]
            lot_y = anchor[1]
            # Anchor Z is the REAL terrain elevation at SE corner (from MDT)
            anchor_z = anchor[2]
        else:
            dx, dy = 0.0, 0.0
            lot_y = 0.0
            anchor_z = None

        # --- CALCULO DE Z DESDE VECINOS NORTE/SUR ---
        vecinos_z_norte = None
        vecinos_z_sur = None
        veclist = data.get("vecinos", [])
        if veclist and lot_y is not None:
            norte_candidates = []  # (distance, z)
            sur_candidates = []    # (distance, z)
            for vecino in veclist:
                v_verts = vecino.get("vertices_3d_local", [])
                if v_verts and len(v_verts) >= 3:
                    v_y_sum = sum(v[1] for v in v_verts)
                    v_z_sum = sum(v[2] for v in v_verts)
                    v_count = len(v_verts)
                    v_y_avg = v_y_sum / v_count
                    v_z_avg = v_z_sum / v_count
                    
                    # Only consider neighbors with valid Z (not 0.0)
                    if abs(v_z_avg) > 0.001:
                        if v_y_avg > lot_y:  # norte
                            dist = v_y_avg - lot_y
                            norte_candidates.append((dist, v_z_avg))
                        elif v_y_avg < lot_y:  # sur
                            dist = lot_y - v_y_avg
                            sur_candidates.append((dist, v_z_avg))
            
            # Take closest in each direction
            if norte_candidates:
                norte_candidates.sort(key=lambda x: x[0])
                vecinos_z_norte = norte_candidates[0][1]
            if sur_candidates:
                sur_candidates.sort(key=lambda x: x[0])
                vecinos_z_sur = sur_candidates[0][1]

        # Determine dz = Z_base: priority order
        # 1. Valid terrain mesh min_z (lowest point of lot terrain) - PRIMARY
        # 2. Neighbor average if both available and valid (urban alignment fallback)
        # 3. SE corner anchor Z (real MDT at lot corner) - fallback
        # 4. 0.0 as last resort
        if min_z is not None and min_z > 0.0:
            dz = min_z
        elif vecinos_z_norte is not None and vecinos_z_sur is not None:
            dz = (vecinos_z_norte + vecinos_z_sur) / 2.0
        elif anchor_z is not None:
            dz = anchor_z
        else:
            dz = 0.0

        meta = data.get("metadata", {})
        origen_sirgas = meta.get("origen_sirgas", {})
        origen_x = origen_sirgas.get("x", 0.0)
        origen_y = origen_sirgas.get("y", 0.0)

        # --- LOTE ---
        lot_curve = polyline_from_coords(lote_verts, dx, dy, dz)
        lot_area = to_float_safe(data.get("lote_objetivo", {}).get("area_m2"), 0.0)

        # --- VECINOS ---
        vecinos_curves = []
        for v in data.get("vecinos", []):
            crv = polyline_from_coords(v.get("vertices_3d_local", []), dx, dy, dz)
            if crv:
                vecinos_curves.append(crv)

        # --- VIAS ---
        vias_oficiales = []
        for via in data.get("vias_oficiales", []):
            coords = via.get("coordenadas_local", [])
            if len(coords) >= 2:
                poly = rg.Polyline()
                for c in coords:
                    poly.Add(c[0] - dx, c[1] - dy, c[2] - dz)
                vias_oficiales.append(rg.PolylineCurve(poly))

        # --- ESPACIOS PUBLICOS ---
        espacios_publicos = []
        for ep in data.get("espacios_publicos", []):
            coords = ep.get("coordenadas_local", [])
            crv = polyline_from_coords(coords, dx, dy, dz)
            if crv:
                espacios_publicos.append(crv)

        # --- TOPOGRAFIA (continued) ---
        topo_mesh = build_terrain_mesh(mesh_points, dx, dy, dz) if mesh_points else None

        # --- NORMATIVA ---
        pd = data.get("pot_data", {})
        altura_max_pot = to_float_safe(pd.get("altura_maxima_m"), 11.4)
        tratamiento = str(pd.get("tratamiento", "Consolidacion"))
        rango_edificabilidad = str(pd.get("rango_edificabilidad", "3"))
        sector_normativo = str(pd.get("sector_normativo", ""))
        upz = str(pd.get("upz", "N/A"))
        io_normativo = to_float_safe(pd.get("io_maximo"), 0.70)

        # --- REGLAMENTACION JSON (para NORMATIVA_v05) ---
        # Deriva de la reglamentacion lo que la fuente POT provea:
        # hoy ancho: null y sin tipologia/antejardin (mapas raster).
        anchos = [to_float_safe(v.get("ancho"), 0.0)
                  for v in data.get("vias_oficiales", [])]
        anchos = [a for a in anchos if a > 0]
        ancho_via_oficial_m = min(anchos) if anchos else 0.0
        tipologia_oficial = str(pd.get("tipologia", "") or "").strip()
        antejardin_oficial = to_float_safe(pd.get("antejardin_m"), 0.0)
        reglamentacion_json = json.dumps({
            "pot_data": {
                "tratamiento": tratamiento,
                "rango_edificabilidad": rango_edificabilidad,
                "upz": upz,
                "sector_normativo": sector_normativo,
                "altura_maxima_m": altura_max_pot,
                "io_maximo": io_normativo,
                "tipologia": tipologia_oficial,
                "ancho_via_m": ancho_via_oficial_m,
                "antejardin_m": antejardin_oficial,
            }
        })

        # --- LAYERS JSON (para Tapir) — v02: garantizar layer del lote ---
        LAYERS_ARCHICAD, layer_lote_ok = garantizar_layer_lote(LAYERS_ARCHICAD)
        layers_json = json.dumps(LAYERS_ARCHICAD)

        chip = meta.get("chip", "DESCONOCIDO")
        mensaje = "ETAPA1 v02 | CHIP: {} | Area: {:.1f}m2 | Vecinos: {} | Vias: {} | EP: {} | Origen: ({:.1f}, {:.1f}) | Lote_layer: {} | Reg: ancho_via={} tipologia={}".format(
            chip, lot_area, len(vecinos_curves), len(vias_oficiales),
            len(espacios_publicos), dx, dy,
            "OK" if layer_lote_ok else "FALTA",
            ancho_via_oficial_m or "sin dato",
            tipologia_oficial or "sin dato")

    except Exception as e:
        mensaje = "ETAPA1 | ERROR al leer JSON: {}".format(str(e))