#! /usr/bin/env python3
"""
================================================================================
F1_PATIO_ESQUINA_v03.py — Patio de aislamiento para lote de esquina.
Proyecto: DiseñoParametrico / Fase 1 — Contexto y Normativa
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPÓSITO:
  En lotes de esquina, la normativa POT/NSR-10 exige un patio de aislamiento
  en la esquina INTERIOR (diagonalmente opuesta al cruce de las vías). Este
  patio garantiza ventilación e iluminación natural al propio edificio y a los
  predios vecinos del interior de la manzana.

  La esquina interior es la opuesta a donde convergen dos calles. El patio se
  ubica en esa esquina, con sus bordes alineados a los linderos del lote,
  proyectándose hacia el interior.

NORMATIVA APLICABLE:
  - Decreto 555/2021, Art. 281 y ficha reglamentaria UPZ El Prado
  - Lotes < 500 m² con tipología Continua: patio fijo de 3.0m × 3.0m
  - Regla general: patio_min = max(3.0, altura_total × 0.25) metros por lado

VERSIONES:
  v01 — Primera implementación. Detección de frentes por sides_table_json,
         cálculo de esquina interior, rectángulo con inward_dir.
  v02 — Eliminado input building_floors (causaba ciclo circular 119→161→119).
         Pisos leídos directamente del JSON de regulación. Rectángulo alineado
         con bordes del lote (edge1, edge2). sides_table_json acepta List Access.
  v03 — Geometría simplificada radicalmente: rectángulo alineado con bordes del
         lote en la esquina interior, proyectado hacia adentro con verificación
         de inclusión. Sin líneas extendidas ni intersecciones infinitas.
         Documentación completa de entradas/salidas/funciones.

ENTRADAS (Inputs de Grasshopper):
  ┌──────────────────┬──────────┬──────────────────────────────────────────────┐
  │ Nombre           │ Tipo     │ Descripción                                  │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ lot_polygon      │ Curve    │ Polígono cerrado del perímetro del lote.     │
  │                  │          │ Item Access. Proviene de F1_CONTEXTO_POT.    │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ sides_table_json │ String   │ JSON con clasificación de cada lado del      │
  │                  │          │ lote (Frontal/Lateral/Posterior). List Acc.  │
  │                  │          │ Proviene de F1_LADOS_CONFIGURAR.             │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ json_path        │ String   │ Ruta absoluta al archivo JSON de caché del   │
  │                  │          │ lote (AAA0127AZPA-contexto.json). De aquí se │
  │                  │          │ lee rango_edificabilidad para calcular pisos.│
  └──────────────────┴──────────┴──────────────────────────────────────────────┘

SALIDAS (Outputs de Grasshopper):
  ┌──────────────────┬──────────┬──────────────────────────────────────────────┐
  │ Nombre           │ Tipo     │ Descripción                                  │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ patio_curve      │ Curve    │ Polilínea cerrada del rectángulo de patio.  │
  │                  │          │ None si el lote no es de esquina (< 2        │
  │                  │          │ frentes) o si hay error. Se usa para boolean │
  │                  │          │ difference con la huella en NORMATIVA.       │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ patio_vertex_idx │ int      │ Índice del vértice interior donde se ubica   │
  │                  │          │ el patio (0-based). -1 si no aplica.         │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ patio_size_m     │ float    │ Longitud del lado del patio en metros.       │
  │                  │          │ 0.0 si no aplica.                            │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ mensaje          │ String   │ Diagnóstico detallado de la operación.       │
  └──────────────────┴──────────┴──────────────────────────────────────────────┘

FUNCIONES INTERNAS:
  ┌─────────────────────────┬──────────────────────────────────────────────────┐
  │ Nombre                  │ Descripción                                      │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ parse_json_safe(data)   │ Convierte string/dict/list a dict de forma       │
  │                         │ segura, sin lanzar excepciones.                  │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ to_int_safe(val, def)   │ Convierte a int con fallback. Valores ≤ 0        │
  │                         │ retornan el default.                             │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ get_vertices(curve)     │ Extrae lista de Point3d únicos de una            │
  │                         │ PolylineCurve cerrada (sin duplicar cierre).     │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ find_street_corner(     │ Busca el vértice donde convergen dos frentes     │
  │   front_indices,        │ adyacentes. Retorna (street_corner_idx,          │
  │   n_verts)              │ interior_corner_idx). Si no hay dos frentes      │
  │                         │ adyacentes, usa heurísticas de fallback.         │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ point_in_lot(pt,        │ Ray casting para determinar si un punto está     │
  │   vertices)             │ dentro del polígono del lote.                    │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ build_patio_rect(       │ Construye el rectángulo del patio: una esquina   │
  │   corner, edge1, edge2, │ en el vértice interior, los bordes alineados con │
  │   size, vertices)       │ los linderos del lote, proyectado hacia adentro. │
  │                         │ Verifica que las 4 esquinas estén dentro.        │
  └─────────────────────────┴──────────────────────────────────────────────────┘
================================================================================
"""

import Rhino.Geometry as rg
import json
import os


# ==============================================================================
# FUNCIONES AUXILIARES
# ==============================================================================

def parse_json_safe(data):
    """
    Convierte cualquier entrada (string JSON, dict, list) a un dict de forma
    segura. IronPython 2.7 compatible.
    
    Args:
        data: String JSON, dict, list, o None.
    
    Returns:
        dict: Datos parseados, o dict vacío si la entrada es inválida.
    """
    if data is None:
        return {}
    if isinstance(data, str):
        try:
            return json.loads(data)
        except:
            return {}
    if isinstance(data, (dict, list)):
        return data
    return {}


def to_int_safe(val, default=4):
    """
    Convierte un valor a entero con fallback seguro.
    Valores ≤ 0 retornan el default.
    
    Args:
        val: Valor a convertir (int, float, str, None).
        default: Valor por defecto si la conversión falla o es ≤ 0.
    
    Returns:
        int: Valor convertido o default.
    """
    if val is None:
        return default
    try:
        v = int(float(val))
        if v <= 0:
            return default
        return v
    except (ValueError, TypeError):
        return default


def get_vertices(curve):
    """
    Extrae los vértices únicos de una PolylineCurve cerrada.
    Si la curva está cerrada (primer vértice = último), omite la duplicación.
    
    Args:
        curve: rg.Curve (PolylineCurve cerrada).
    
    Returns:
        list[rg.Point3d]: Lista de vértices únicos.
    """
    if curve is None:
        return []
    success, poly = curve.TryGetPolyline()
    if not success or poly is None:
        return []
    c = poly.Count
    if c >= 2 and poly[0].DistanceTo(poly[c - 1]) < 0.001:
        return [poly[i] for i in range(c - 1)]
    return [poly[i] for i in range(c)]


def point_in_lot(pt, vertices):
    """
    Determina si un punto está dentro del polígono del lote usando ray casting.
    IronPython 2.7 compatible (sin shapely).
    
    Args:
        pt: rg.Point3d a verificar.
        vertices: list[rg.Point3d] del perímetro del lote.
    
    Returns:
        bool: True si el punto está dentro del polígono.
    """
    n = len(vertices)
    if n < 3:
        return False
    
    count = 0
    px, py = pt.X, pt.Y
    
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        y1, y2 = v1.Y, v2.Y
        
        # El rayo horizontal desde (px, py) hacia la derecha
        if ((y1 > py) != (y2 > py)):
            x1, x2 = v1.X, v2.X
            x_int = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if px < x_int:
                count += 1
    
    return (count % 2) == 1


def find_street_corner(front_indices, n_verts):
    """
    Encuentra la esquina de calles (donde convergen dos frentes adyacentes)
    y la esquina interior opuesta (donde se ubica el patio).
    
    Estrategia:
      1. Buscar dos frentes adyacentes (diferencia = 1 o n-1).
      2. El vértice entre ellos es la street_corner.
      3. La esquina interior es street_corner + n//2 (diagonalmente opuesta).
      4. Fallback: si no hay frentes adyacentes, usar el primer frente y
         asumir que la esquina está en front+1.
    
    Args:
        front_indices: list[int] — índices de lados clasificados como "Frontal".
        n_verts: int — número de vértices del polígono del lote.
    
    Returns:
        tuple: (street_corner_idx, interior_corner_idx) o (None, None) si falla.
    """
    if len(front_indices) < 2:
        return None, None
    
    sorted_fr = sorted(front_indices)
    street_corner = None
    
    # Buscar pares adyacentes
    for i in range(len(sorted_fr)):
        a = sorted_fr[i]
        b = sorted_fr[(i + 1) % len(sorted_fr)]
        diff = abs(a - b)
        
        if diff == 1:
            street_corner = b  # vértice compartido: final del segmento a
            break
        elif diff == n_verts - 1:
            street_corner = 0  # wrap-around: segmentos 0 y n-1
            break
    
    if street_corner is None:
        # Fallback: usar el vértice después del primer frente
        street_corner = (sorted_fr[0] + 1) % n_verts
    
    interior_corner = (street_corner + n_verts // 2) % n_verts
    
    return street_corner, interior_corner


def build_patio_rect(corner_vertex, edge1, edge2, size, vertices):
    """
    Construye un rectángulo de patio en la esquina interior del lote.
    
    El rectángulo tiene:
      - Una esquina anclada en corner_vertex (el vértice interior).
      - Dos bordes alineados con edge1 y edge2 (los linderos del lote).
      - Proyección hacia el interior del lote.
      - Verificación de que las 4 esquinas están dentro del polígono.
    
    Args:
        corner_vertex: rg.Point3d — vértice interior donde anclar el patio.
        edge1: rg.Vector3d — dirección del primer borde del lote (hacia afuera
               desde corner_vertex).
        edge2: rg.Vector3d — dirección del segundo borde del lote.
        size: float — longitud del lado del patio en metros.
        vertices: list[rg.Point3d] — vértices del lote para verificación de
                  inclusión.
    
    Returns:
        rg.PolylineCurve o None: Curva cerrada del rectángulo de patio,
        o None si el rectángulo no cabe dentro del lote.
    """
    # Normalizar vectores
    e1 = rg.Vector3d(edge1.X, edge1.Y, 0)
    e2 = rg.Vector3d(edge2.X, edge2.Y, 0)
    
    if e1.Length < 0.001 or e2.Length < 0.001:
        return None
    
    e1.Unitize()
    e2.Unitize()
    
    # Determinar hacia dónde queda el interior del lote.
    # Probamos las 4 combinaciones de signos (±e1, ±e2) y elegimos
    # la que maximiza el número de esquinas dentro del lote.
    
    signs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    best_count = -1
    best_pts = None
    
    for sx, sy in signs:
        s1 = rg.Vector3d(sx * e1.X, sx * e1.Y, 0)
        s2 = rg.Vector3d(sy * e2.X, sy * e2.Y, 0)
        
        p0 = rg.Point3d(corner_vertex.X, corner_vertex.Y, 0)
        p1 = rg.Point3d(p0.X + s1.X * size, p0.Y + s1.Y * size, 0)
        p2 = rg.Point3d(p1.X + s2.X * size, p1.Y + s2.Y * size, 0)
        p3 = rg.Point3d(p0.X + s2.X * size, p0.Y + s2.Y * size, 0)
        
        test_pts = [p0, p1, p2, p3]
        inside_count = sum(1 for p in test_pts if point_in_lot(p, vertices))
        
        if inside_count > best_count:
            best_count = inside_count
            best_pts = [p0, p1, p2, p3]
    
    if best_count < 4:
        # El patio no cabe completamente dentro del lote con esta orientación.
        # Intentar reducirlo o usar solo la esquina.
        return None
    
    pts = best_pts + [best_pts[0]]  # cerrar polilínea
    return rg.PolylineCurve(pts)


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

# --- 1. LECTURA DE ENTRADAS ---
lot_polygon_raw = globals().get("lot_polygon", None)
sides_table_raw = globals().get("sides_table_json", None)
json_path_raw   = globals().get("json_path", None)

# Unwrap si GH envía lista unitaria (Item Access residual)
if isinstance(lot_polygon_raw, list) and len(lot_polygon_raw) == 1:
    lot_polygon_raw = lot_polygon_raw[0]

lot_polygon = lot_polygon_raw
json_path   = str(json_path_raw).strip("[]'\" ") if json_path_raw else ""

# Validación temprana
if lot_polygon is None:
    patio_curve      = None
    patio_vertex_idx = -1
    patio_size_m     = 0.0
    mensaje          = "ERROR: lot_polygon es None. Verifique conexión."
    print(mensaje)
    # GH outputs implícitos: patio_curve, patio_vertex_idx, patio_size_m, mensaje
else:
    # --- 2. PISOS DESDE LA REGULACIÓN (sin input externo, evita ciclo) ---
    building_floors = 4   # default conservador
    rango_edif      = "3"
    
    if json_path and os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                jdata = json.load(f)
            pd = jdata.get("pot_data", {})
            rango_edif = str(pd.get("rango_edificabilidad", "3"))
        except:
            pass
    
    RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}
    building_floors = RANGO_PISOS.get(rango_edif, 5)
    
    # --- 3. CLASIFICACIÓN DE LADOS ---
    sides_data = parse_json_safe(sides_table_raw)
    sides_list = []
    
    if isinstance(sides_data, list):
        # List Access: lista de dicts o strings JSON por lado
        for item in sides_data:
            if isinstance(item, dict):
                sides_list.append(item)
            elif isinstance(item, str):
                try:
                    d = json.loads(item)
                    if isinstance(d, dict):
                        sides_list.append(d)
                except:
                    pass
    elif isinstance(sides_data, dict):
        inner = sides_data.get("sides", sides_data.get("lados", []))
        if isinstance(inner, list):
            sides_list = inner
    
    # --- 4. IDENTIFICAR FRENTES ---
    front_indices = []
    for side in sides_list:
        if isinstance(side, dict):
            cls = str(side.get("classification", "")).strip().lower()
            if cls == "frontal":
                idx = to_int_safe(side.get("side_index", -1))
                if idx >= 0:
                    front_indices.append(idx)
    
    vertices = get_vertices(lot_polygon)
    n_verts  = len(vertices)
    
    # --- 5. DECISIÓN: ¿APLICA PATIO DE ESQUINA? ---
    if len(front_indices) < 2:
        patio_curve      = None
        patio_vertex_idx = -1
        patio_size_m     = 0.0
        mensaje = "No aplica patio: {} frente(s) detectado(s) de {} lados.".format(
            len(front_indices), n_verts)
        print(mensaje)
    
    elif n_verts < 4:
        patio_curve      = None
        patio_vertex_idx = -1
        patio_size_m     = 0.0
        mensaje = "ERROR: lote con {} vértices (< 4).".format(n_verts)
        print(mensaje)
    
    else:
        # --- 6. LOCALIZAR ESQUINAS ---
        street_corner, interior_corner = find_street_corner(front_indices, n_verts)
        
        if street_corner is None:
            patio_curve      = None
            patio_vertex_idx = -1
            patio_size_m     = 0.0
            mensaje = "ERROR: no se pudo identificar esquina de calles. Frentes: {}".format(
                front_indices)
            print(mensaje)
        else:
            # --- 7. TAMAÑO DEL PATIO ---
            try:
                amp = rg.AreaMassProperties.Compute(lot_polygon)
                lot_area = amp.Area if amp else 315.0
            except:
                lot_area = 315.0
            
            if lot_area < 500.0 and building_floors <= 5:
                patio_size_m = 3.0
            else:
                altura_total = building_floors * 3.0
                patio_size_m = max(3.0, altura_total * 0.25)
                patio_size_m = round(patio_size_m * 2.0) / 2.0  # redondear a 0.5m
            
            # --- 8. CONSTRUIR GEOMETRÍA DEL PATIO ---
            v_int  = vertices[interior_corner]
            v_prev = vertices[(interior_corner - 1 + n_verts) % n_verts]
            v_next = vertices[(interior_corner + 1) % n_verts]
            
            # Vectores de los bordes del lote hacia afuera desde la esquina interior
            edge_to_prev = rg.Vector3d(v_prev.X - v_int.X, v_prev.Y - v_int.Y, 0)
            edge_to_next = rg.Vector3d(v_next.X - v_int.X, v_next.Y - v_int.Y, 0)
            
            patio_curve = build_patio_rect(v_int, edge_to_prev, edge_to_next,
                                           patio_size_m, vertices)
            
            patio_vertex_idx = interior_corner
            
            if patio_curve is None:
                mensaje = (
                    "ADVERTENCIA: El patio de {:.1f}x{:.1f}m no cabe completamente "
                    "en el lote en el vértice interior v{}. "
                    "Esquina calles: v{}. Frentes: {}. "
                    "Posible causa: ángulo muy agudo en la esquina interior o "
                    "clasificación de frentes incorrecta."
                ).format(patio_size_m, patio_size_m, interior_corner,
                         street_corner, front_indices)
            else:
                mensaje = (
                    "Patio {:.1f}x{:.1f}m generado en vértice interior v{} "
                    "(esquina calles: v{}, {} frentes, {} pisos norma, rango {})."
                ).format(patio_size_m, patio_size_m, interior_corner,
                         street_corner, len(front_indices), building_floors, rango_edif)
            
            print(mensaje)

# ==============================================================================
# OUTPUTS: patio_curve, patio_vertex_idx, patio_size_m, mensaje
# ==============================================================================
