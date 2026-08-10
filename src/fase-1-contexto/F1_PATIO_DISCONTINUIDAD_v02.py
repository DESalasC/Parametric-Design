#! /usr/bin/env python3
"""
================================================================================
F1_PATIO_DISCONTINUIDAD_v02.py — Patios desde vértices del lote (Discontinuity)
GH Python Script para Grasshopper (IronPython 2.7 compatible)

PROPÓSITO:
  Usa los vértices del lote (Discontinuity) + clasificación de lados del JSON
  para detectar vértices donde convergen DOS bordes "Lateral" → patio.

  La clasificación Frontal/Lateral viene del backend, calculada por adyacencia
  real con vecinos (sin líneas artificiales):
    - Frontal: borde del lote SIN vecino colindante → da a vía/espacio público
    - Lateral: borde del lote CON vecino colindante → da a predio vecino

  Reemplaza: LADOS_CONFIGURAR + PATIO_VECINO + PATIO_ESQUINA

ENTRADAS:
  lot_vertices  (Point3d[]) — Vértices del lote desde Discontinuity
  json_path     (String)    — Ruta al JSON de caché del lote

SALIDAS:
  patios_curves   (Curve[])   — Rectángulos de patio
  patio_vertices  (int[])     — Índices de vértices con patio
  patio_count     (int)       — Número de patios generados
  sides_table     (String)    — Clasificación de bordes (JSON)
  mensaje         (String)    — Diagnóstico
================================================================================
"""

import Rhino.Geometry as rg
import json
import os
import math

# ── Config ──
RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}
ALTURA_ENTREPISO = 3.0
PATIO_MINIMO_M = 3.0

# ── Helpers ──

def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]

def point_in_lot(pt, vertices):
    """Ray casting — ¿está el punto dentro del polígono?"""
    n = len(vertices)
    if n < 3: return False
    count = 0
    px, py = pt.X, pt.Y
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        if ((v1.Y > py) != (v2.Y > py)):
            x_int = v1.X + (py - v1.Y) * (v2.X - v1.X) / (v2.Y - v1.Y)
            if px < x_int: count += 1
    return (count % 2) == 1

def build_patio_at_vertex(corner_pt, edge1_vec, edge2_vec, size, lot_vertices):
    """
    Construye rectángulo de patio anclado en corner_pt, con bordes alineados
    a edge1_vec y edge2_vec, proyectado hacia el interior del lote.
    """
    e1 = rg.Vector3d(edge1_vec.X, edge1_vec.Y, 0)
    e2 = rg.Vector3d(edge2_vec.X, edge2_vec.Y, 0)
    if e1.Length < 0.001 or e2.Length < 0.001: return None
    e1.Unitize()
    e2.Unitize()
    
    signs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    best = None
    best_count = -1
    
    for sx, sy in signs:
        s1 = rg.Point3d(corner_pt.X + e1.X * size * sx, corner_pt.Y + e1.Y * size * sx, 0)
        s2 = rg.Point3d(corner_pt.X + e2.X * size * sy, corner_pt.Y + e2.Y * size * sy, 0)
        diag = rg.Point3d(s1.X + e2.X * size * sy, s1.Y + e2.Y * size * sy, 0)
        
        pts = [corner_pt, s1, diag, s2]
        inside = sum(1 for p in pts if point_in_lot(p, lot_vertices))
        if inside > best_count:
            best_count = inside
            best = pts
    
    if best_count < 4 or best is None:
        return None
    
    closed = best + [best[0]]
    return rg.PolylineCurve(closed)


# ── MAIN ──

raw_verts = globals().get("lot_vertices", [])
raw_json  = globals().get("json_path", None)

lot_pts = safe_list(raw_verts)
json_path = str(raw_json).strip("[]'\" ") if raw_json else ""

n = len(lot_pts)
if n < 3:
    patios_curves   = []
    patio_vertices  = []
    patio_count     = 0
    sides_table     = "[]"
    mensaje = "ERROR: Solo {} vertices. Se necesitan >= 3.".format(n)
    print(mensaje)
else:
    # ── 1. Leer clasificación de lados del JSON ──
    edge_class = {}
    sides_table = "[]"
    building_floors = 4
    rango_edif = "3"
    
    if json_path and os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                jdata = json.load(f)
            
            lados = jdata.get("lados", [])
            if lados:
                for lado in lados:
                    idx = lado.get("lado_idx", -1)
                    cls = lado.get("clasificacion", "Lateral")
                    edge_class[idx] = cls
            
            sides_table = json.dumps(lados)
            
            # Pisos/altura desde POT
            pd = jdata.get("pot_data", {})
            rango_edif = str(pd.get("rango_edificabilidad", "3"))
        except Exception as e:
            print("Error leyendo JSON: " + str(e))
    else:
        print("ADVERTENCIA: JSON no encontrado en: " + json_path)
    
    building_floors = RANGO_PISOS.get(rango_edif, 5)
    
    # ── 2. Calcular tamaño del patio ──
    altura_total = building_floors * ALTURA_ENTREPISO
    patio_size = max(PATIO_MINIMO_M, altura_total * 0.25)
    patio_size = round(patio_size * 2) / 2
    
    print("=== PATIO_DISCONTINUIDAD v02 ===")
    print("Clasificacion desde JSON: " + json.dumps({k: edge_class.get(k, "?") for k in range(n)}))
    print("Altura: {:.1f}m ({} pisos, rango {}) | Patio: {:.1f}x{:.1f}m".format(
        altura_total, building_floors, rango_edif, patio_size, patio_size))
    
    # ── 3. Encontrar vértices con DOS bordes Lateral ──
    patios_curves = []
    patio_vertices = []
    
    for i in range(n):
        v_curr = lot_pts[i]
        edge_prev_idx = (i - 1 + n) % n  # borde que llega al vértice
        edge_next_idx = i                 # borde que sale del vértice
        
        cls_prev = edge_class.get(edge_prev_idx, "Lateral")
        cls_next = edge_class.get(edge_next_idx, "Lateral")
        
        is_candidate = (cls_prev == "Lateral" and cls_next == "Lateral")
        
        if not is_candidate:
            print("  Vertice {}: {}+{} -> NO patio".format(i, cls_prev, cls_next))
            continue
        
        print("  Vertice {}: {}+{} -> CANDIDATO patio".format(i, cls_prev, cls_next))
        
        v_prev = lot_pts[edge_prev_idx]
        v_next = lot_pts[(i + 1) % n]
        
        edge_to_prev = rg.Vector3d(v_prev.X - v_curr.X, v_prev.Y - v_curr.Y, 0)
        edge_to_next = rg.Vector3d(v_next.X - v_curr.X, v_next.Y - v_curr.Y, 0)
        
        patio_crv = build_patio_at_vertex(v_curr, edge_to_prev, edge_to_next,
                                          patio_size, lot_pts)
        if patio_crv:
            patios_curves.append(patio_crv)
            patio_vertices.append(i)
            print("    Patio {:.1f}x{:.1f}m generado".format(patio_size, patio_size))
        else:
            print("    Patio NO cabe en el lote (angulo muy agudo o espacio insuficiente)")
    
    patio_count = len(patios_curves)
    n_front = sum(1 for i in range(n) if edge_class.get(i, "?") == "Frontal")
    n_lat  = sum(1 for i in range(n) if edge_class.get(i, "?") == "Lateral")
    mensaje = "Frentes:{} Laterales:{} | Patios:{} de {} vertices | Tamano:{:.1f}m".format(
        n_front, n_lat, patio_count, n, patio_size)
    print(mensaje)
    print("=== FIN ===")
