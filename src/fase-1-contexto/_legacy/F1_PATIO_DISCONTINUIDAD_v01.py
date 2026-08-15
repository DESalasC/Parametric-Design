#! /usr/bin/env python3
"""
================================================================================
F1_PATIO_DISCONTINUIDAD_v01.py — Patios desde vértices del lote (Discontinuity)
GH Python Script para Grasshopper (IronPython 2.7 compatible)

PROPÓSITO:
  Usa los vértices del lote (de Discontinuity) + curvas de vías para:
  1. Clasificar cada borde del lote como "Frontal" o "Lateral"
  2. Detectar vértices donde convergen DOS bordes "Lateral" → candidato a patio
  3. Generar rectángulo de patio alineado con los bordes del lote
  4. Verificar que el patio quepa dentro del lote

  Reemplaza: LADOS_CONFIGURAR + PATIO_VECINO + PATIO_ESQUINA

ENTRADAS:
  lot_vertices  (Point3d[]) — Vértices del lote desde Discontinuity
  street_curves (Curve[])   — Curvas de vías cercanas
  json_path     (String)    — Ruta al JSON de caché del lote (para altura/pisos)

SALIDAS:
  patios_curves   (Curve[])  — Lista de curvas de patio
  patio_vertices  (int[])    — Índices de vértices con patio
  patio_count     (int)      — Número de patios generados
  sides_table_json (String)  — Clasificación de bordes (Frontal/Lateral)
  mensaje         (String)   — Diagnóstico
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
TOLERANCIA_COLINEAL = 0.05  # 5cm — ángulos menores se consideran colineales

# ── Helpers ──

def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]

def verts_from_points(pts):
    """Convierte lista de Point3d a lista de (x,y,z). Filtra None."""
    return [(p.X, p.Y, p.Z) for p in pts if p is not None]

def edge_midpoint(v1, v2):
    return rg.Point3d((v1.X + v2.X)/2, (v1.Y + v2.Y)/2, 0)

def distance_to_streets(point, street_curves):
    """Distancia mínima desde un punto a cualquier curva de vía."""
    min_d = float('inf')
    for crv in street_curves:
        if crv is None: continue
        try:
            success, t = crv.ClosestPoint(point)
            if success:
                pt = crv.PointAt(t)
                d = point.DistanceTo(pt)
                if d < min_d: min_d = d
        except:
            continue
    return min_d

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
    edge1_vec/edge2_vec son vectores DESDE corner_pt hacia los otros vértices.
    """
    e1 = rg.Vector3d(edge1_vec.X, edge1_vec.Y, 0)
    e2 = rg.Vector3d(edge2_vec.X, edge2_vec.Y, 0)
    if e1.Length < 0.001 or e2.Length < 0.001: return None
    e1.Unitize()
    e2.Unitize()
    
    # Probar 4 combinaciones de signos: hacia adentro del lote
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

raw_verts   = globals().get("lot_vertices", [])
raw_streets = globals().get("street_curves", [])
raw_json    = globals().get("json_path", None)

lot_pts = safe_list(raw_verts)
streets = safe_list(raw_streets)
json_path = str(raw_json).strip("[]'\" ") if raw_json else ""

# Filtro None
streets = [s for s in streets if s is not None]

n = len(lot_pts)
if n < 3:
    patios_curves   = []
    patio_vertices  = []
    patio_count     = 0
    sides_table_json = "[]"
    mensaje = f"ERROR: Solo {n} vertices. Se necesitan >= 3."
    print(mensaje)
else:
    # ── 1. Clasificar bordes ──
    edge_dists = []
    for i in range(n):
        v1 = lot_pts[i]
        v2 = lot_pts[(i + 1) % n]
        mid = edge_midpoint(v1, v2)
        d = distance_to_streets(mid, streets)
        edge_dists.append((i, d, mid))
    
    # Umbral adaptativo
    distances = [d for _, d, _ in edge_dists]
    min_d = min(distances)
    max_d = max(distances)
    threshold = min_d + max(3.0, (max_d - min_d) * 0.15)
    
    print("=== PATIO_DISCONTINUIDAD v01 ===")
    print(f"Distancias a vias: min={min_d:.1f}m max={max_d:.1f}m umbral={threshold:.1f}m")
    
    sides_table = []
    edge_class = {}  # edge_idx -> "Frontal"|"Lateral"
    
    for idx, dist, mid in edge_dists:
        is_front = dist <= threshold
        cls = "Frontal" if is_front else "Lateral"
        edge_class[idx] = cls
        sides_table.append({
            "side_index": idx,
            "classification": cls,
            "dist_to_street_m": round(dist, 2)
        })
        print(f"  Borde {idx}: dist={dist:.1f}m -> {cls}")
    
    sides_table_json = json.dumps(sides_table)
    
    # ── 2. Altura/pisos desde JSON ──
    building_floors = 4
    rango_edif = "3"
    if json_path and os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                jdata = json.load(f)
            pd = jdata.get("pot_data", {})
            rango_edif = str(pd.get("rango_edificabilidad", "3"))
        except: pass
    building_floors = RANGO_PISOS.get(rango_edif, 5)
    
    # Tamaño del patio
    altura_total = building_floors * ALTURA_ENTREPISO
    patio_size = max(PATIO_MINIMO_M, altura_total * 0.25)
    patio_size = round(patio_size * 2) / 2  # redondear a 0.5m
    print(f"Altura: {altura_total:.1f}m ({building_floors} pisos, rango {rango_edif}) | Patio: {patio_size:.1f}x{patio_size:.1f}m")
    
    # ── 3. Encontrar vértices candidatos a patio ──
    patios_curves = []
    patio_vertices = []
    
    for i in range(n):
        v_curr = lot_pts[i]
        edge_prev_idx = (i - 1 + n) % n  # borde que LLEGA al vértice i
        edge_next_idx = i                 # borde que SALE del vértice i
        
        cls_prev = edge_class.get(edge_prev_idx, "Lateral")
        cls_next = edge_class.get(edge_next_idx, "Lateral")
        
        is_candidate = (cls_prev == "Lateral" and cls_next == "Lateral")
        
        if not is_candidate:
            print(f"  Vértice {i}: {cls_prev}+{cls_next} -> NO patio")
            continue
        
        print(f"  Vértice {i}: {cls_prev}+{cls_next} -> CANDIDATO patio")
        
        # Vectores de los bordes desde el vértice hacia adentro
        v_prev = lot_pts[edge_prev_idx]  # vértice ANTERIOR
        v_next = lot_pts[(i + 1) % n]    # vértice SIGUIENTE
        
        # Vector a lo largo del borde DESDE el vértice actual hacia el anterior
        # (invertido porque el borde VA hacia el vértice, no desde él)
        edge_to_prev = rg.Vector3d(v_prev.X - v_curr.X, v_prev.Y - v_curr.Y, 0)
        edge_to_next = rg.Vector3d(v_next.X - v_curr.X, v_next.Y - v_curr.Y, 0)
        
        patio_crv = build_patio_at_vertex(v_curr, edge_to_prev, edge_to_next,
                                          patio_size, lot_pts)
        if patio_crv:
            patios_curves.append(patio_crv)
            patio_vertices.append(i)
            print(f"    Patio {patio_size:.1f}x{patio_size:.1f}m generado")
        else:
            print(f"    Patio NO cabe en el lote (ángulo muy agudo o espacio insuficiente)")
    
    patio_count = len(patios_curves)
    n_front = sum(1 for v in edge_class.values() if v == "Frontal")
    n_lat = sum(1 for v in edge_class.values() if v == "Lateral")
    mensaje = f"Frentes:{n_front} Laterales:{n_lat} | Patios:{patio_count} de {n} vertices | Tamaño:{patio_size:.1f}m"
    print(mensaje)
    print("=== FIN ===")
