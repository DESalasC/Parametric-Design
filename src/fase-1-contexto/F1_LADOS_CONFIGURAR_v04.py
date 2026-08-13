#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CONFIGURAR_v04.py — Clasificacion de lados del lote.
Proyecto: DisenoParametrico / Fase 1 — Contexto y Normativa
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Clasifica cada lado del poligono del lote como "Frontal" (colinda con via) o
  "Lateral" (colinda con vecino), midiendo la distancia de cada lado a las
  curvas de calle (street_curves). Los lados mas cercanos a vias son Frontales.

  NO requiere centroid como input externo — lo calcula internamente.

ENTRADAS (Inputs de Grasshopper):
  ┌──────────────────┬──────────┬──────────────────────────────────────────────┐
  │ Nombre           │ Tipo     │ Descripcion                                  │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ lot_polygon      │ Curve    │ Poligono del lote. Item Access.              │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ lot_segments     │ Line[]   │ Segmentos del lote (Explode). List Access.   │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ lot_midpoints    │ Point[]  │ Puntos medios de cada segmento. List Access. │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ street_curves    │ Curve[]  │ Curvas de vias cercanas. List Access.        │
  └──────────────────┴──────────┴──────────────────────────────────────────────┘

SALIDAS (Outputs de Grasshopper):
  ┌──────────────────┬──────────┬──────────────────────────────────────────────┐
  │ Nombre           │ Tipo     │ Descripcion                                  │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ sides_table_json │ String   │ JSON array con clasificacion de cada lado.   │
  │                  │          │ Array de objetos: {side_index, classification,│
  │                  │          │  setback_m, road_type, ...}                  │
  └──────────────────┴──────────┴──────────────────────────────────────────────┘

VERSIONES:
  v03 — Requeria centroid, pot_conclusions, floors_per_tower como inputs.
  v04 — Eliminados inputs redundantes. centroid calculado internamente.
        Salida simplificada: solo sides_table_json (lo demas no se usaba).
================================================================================
"""

import Rhino.Geometry as rg
import json
import math


def to_int_safe(val, default=0):
    if val is None: return default
    try:
        v = int(float(val))
        return v
    except: return default


def to_float_safe(val, default=0.0):
    if val is None: return default
    try: return float(val)
    except: return default


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon   = globals().get("lot_polygon", None)
lot_segments  = globals().get("lot_segments", [])
lot_midpoints = globals().get("lot_midpoints", [])
# Accept either "street_curves" (from upstream) or "public_space_curve" (from F1_CONTEXTO_POT)
street_curves = globals().get("street_curves", [])
if not street_curves:
    street_curves = globals().get("public_space_curve", [])

# Normalizar listas - asegurar que sean listas
if lot_segments is None:
    lot_segments = []
if not isinstance(lot_segments, list):
    lot_segments = [lot_segments]
if lot_midpoints is None:
    lot_midpoints = []
if not isinstance(lot_midpoints, list):
    lot_midpoints = [lot_midpoints]
if street_curves is None:
    street_curves = []
if not isinstance(street_curves, list):
    street_curves = [street_curves]

# Filtrar Nones y validar que sean objetos de curva válidos
lot_segments  = [s for s in lot_segments if s is not None and hasattr(s, 'From') and hasattr(s, 'To')]
lot_midpoints = [p for p in lot_midpoints if p is not None]
# Filtrar solo objetos de curva válidos para street_curves que tengan los métodos necesarios
valid_street_curves = []
for c in street_curves:
    if c is not None and hasattr(c, 'ClosestPoint') and hasattr(c, 'PointAt'):
        valid_street_curves.append(c)
street_curves = valid_street_curves

# DEBUG: Información de entrada
print("LADOS_CONFIGURAR v04 DEBUG: lot_polygon={}, lot_segments={}, lot_midpoints={}, street_curves={}".format(
    lot_polygon is not None,
    len(lot_segments) if lot_segments else 0,
    len(lot_midpoints) if lot_midpoints else 0,
    len(street_curves) if street_curves else 0))

if lot_polygon is None or len(lot_segments) == 0:
    sides_table_json = json.dumps([])
    print("ERROR: Falta lot_polygon o lot_segments.")
else:
    # --- 1. CALCULAR DISTANCIA DE CADA SEGMENTO A LA CALLE MAS CERCANA ---
    segment_data = []

    if len(street_curves) == 0:
        print("ADVERTENCIA: No hay street_curves válidas para comparar. Todas las clasificaciones serán Lateral.")
        # Si no hay calles, todo es vecino por defecto
        for i in range(len(lot_segments)):
            segment_data.append({
                "idx": i,
                "dist": 999.0,  # Distancia grande para activar la advertencia de coordenadas
                "street_idx": -1
            })
    else:
        for i, seg in enumerate(lot_segments):
            # Punto medio
            if i < len(lot_midpoints):
                mid = lot_midpoints[i]
            else:
                # Fallback: punto medio del segmento
                mid = rg.Point3d((seg.From.X + seg.To.X) / 2,
                                 (seg.From.Y + seg.To.Y) / 2, 0)

            min_dist = float('inf')
            closest_idx = -1

            for j, crv in enumerate(street_curves):
                try:
                    success, t = crv.ClosestPoint(mid)
                    if success:
                        pt_on_crv = crv.PointAt(t)
                        dist = mid.DistanceTo(pt_on_crv)
                        if dist < min_dist:
                            min_dist = dist
                            closest_idx = j
                except Exception as e:
                    print("  ERROR calculando distancia a street curve {}: {}".format(j, str(e)))
                    continue

            segment_data.append({
                "idx": i,
                "dist": min_dist,
                "street_idx": closest_idx
            })

            # DEBUG: Para los primeros pocos segmentos, mostrar distancia
            if i < 3:
                print("  Segmento {}: distancia mínima a calle = {:.2f}m".format(i, min_dist))

    # --- 2. CLASIFICAR ---
    if len(segment_data) == 0:
        sides_table = []
    else:
        min_dist_overall = min(d["dist"] for d in segment_data)
        print("LADOS_CONFIGURAR v04 DEBUG: Distancia mínima general a calles = {:.2f}m".format(min_dist_overall))

        # Si la distancia minima es > 50m, las calles estan en otro sistema
        # de coordenadas. Advertir y clasificar todo como Lateral (vecino).
        if min_dist_overall > 50.0:
            sides_table = []
            for d in segment_data:
                sides_table.append({
                    "side_index": d["idx"],
                    "classification": "Lateral",
                    "setback_m": 0.0,
                    "road_type": "Vecino",
                    "dist_to_street_m": round(d["dist"], 2)
                })
            print("ADVERTENCIA: street_curves a {:.1f}m del lote. "
                  "¿Estan en el mismo sistema de coordenadas? "
                  "Clasificando todos los lados como Lateral (vecino).".format(min_dist_overall))
        else:
            # Clasificación normal: los lados más cercanos a las calles son Frontales
            sides_table = []
            for d in segment_data:
                # Es frontal si su distancia es igual al mínimo (con tolerancia para errores de punto flotante)
                is_frontal = abs(d["dist"] - min_dist_overall) < 0.01  # 1cm de tolerancia
                sides_table.append({
                    "side_index": d["idx"],
                    "classification": "Frontal" if is_frontal else "Lateral",
                    "setback_m": 0.0,  # Se calculará en F1_NORMATIVA_APLICAR
                    "road_type": "Via" if is_frontal else "Vecino",
                    "dist_to_street_m": round(d["dist"], 2)
                })

    # --- 3. SALIDA ---
    sides_table_json = json.dumps(sides_table)

    n_fronts = sum(1 for s in sides_table if s["classification"] == "Frontal")
    n_laterals = sum(1 for s in sides_table if s["classification"] == "Lateral")
    print("LADOS_CONFIGURAR v04: {} lados ({} Frontales, {} Laterales)".format(
        len(sides_table), n_fronts, n_laterals))
