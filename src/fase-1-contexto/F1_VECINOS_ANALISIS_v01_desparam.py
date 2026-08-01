#!/usr/bin/env python3
"""
ANALISIS_VECINOS.py - Analiza construcciones vecinas y aplica separación sísmica NSR-10
Componente GHPython para Grasshopper (Rhino 7+)

ENTRADAS:
  - lot_polygon: Curve cerrado en plano XY (polígono del lote)
  - neighbor_breps: Lista de Breps (cada uno representa una construcción vecina)
  - my_building_total_height: float, altura total estimada del proyecto en metros
  - pot_setbacks: Lista de floats, aislamientos urbanísticos mínimos del POT por lado del lote

SALIDAS:
  - updated_sides_table: JSON string con tabla de lados actualizada
  - neighbor_footprints: Lista de Curves (huellas proyectadas de los vecinos)
  - neighbor_heights: Lista de números (alturas de los vecinos)
"""

import json
import math

# Intentar usar rhinoscriptsyntax (disponible en GHPython)
try:
    import rhinoscriptsyntax as rs
except ImportError:
    # Fallback mínimo para pruebas externas (no se espera llegar aquí en GH)
    rs = None

def safe_float(val, default=0.0):
    try:
        return float(val)
    except:
        return default

def main():
    global updated_sides_table, neighbor_footprints, neighbor_heights
    # Validar entradas
    if lot_polygon is None:
        raise ValueError("lot_polygon es requerido")
    if not isinstance(neighbor_breps, list):
        neighbor_breps = [] if neighbor_breps is None else [neighbor_breps]
    if my_building_total_height is None:
        my_building_total_height = 0.0
    if pot_setbacks is None:
        pot_setbacks = []
    # Asegurar que pot_sebs sea lista de floats
    pot_setbacks = [safe_float(x) for x in pot_setbacks]

    my_height = safe_float(my_building_total_height)

    # Preparar salidas
    updated_sides = []      # lista de diccionarios que se convertirán a JSON
    neighbor_footprints = [] # lista de Curves
    neighbor_heights = []   # lista de floats (alturas)

    # --- 1. Procesar cada vecino: obtener altura y huella proyectada ---
    for i, brep in enumerate(neighbor_breps):
        if brep is None:
            continue
        # Bounding box del brep (lista de 8 puntos)
        bbox = rs.BoundingBox(brep)
        if not bbox or len(bbox) < 8:
            # Si falla, saltar este vecino
            continue
        # Extraer coordenadas Z para altura
        z_vals = [pt[2] for pt in bbox]
        height = max(z_vals) - min(z_vals)  # altura total
        neighbor_heights.append(height)

        # Huella proyectada: rectángulo en XY usando minX, maxX, minY, maxY a Z=0
        xs = [pt[0] for pt in bbox]
        ys = [pt[1] for pt in bbox]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        # Puntos del rectángulo (cerrado)
        pts = [
            (minx, miny, 0.0),
            (maxx, miny, 0.0),
            (maxx, maxy, 0.0),
            (minx, maxy, 0.0),
            (minx, miny, 0.0)
        ]
        footprint = rs.AddPolyline(pts)
        if footprint:
            neighbor_footprints.append(footprint)
        else:
            # Si falla la creación, usar curva nula pero aún así registrar altura
            neighbor_footprints.append(None)

    # --- 2. Obtener lados del lote (explodir polígono en segmentos) ---
    lot_side_curves = rs.ExplodeCurves(lot_polygon)
    if not lot_side_curves:
        lot_side_curves = []  # evitar errores

    # --- 3. Para cada lado, calcular separación sísmica si hay vecino adyacente ---
    tolerance = 0.01  # metros, considerar adyacente si distancia <= tolerance
    for side_idx, side_crv in enumerate(lot_side_curves):
        if side_crv is None:
            continue
        # Setback base del POT (si existe)
        pot_setback = pot_setbacks[side_idx] if side_idx < len(pot_setbacks) else 0.0
        # Inicializar valores
        final_setback = pot_setback
        adj_neighbor_height = 0.0
        nsr_sep = 0.0

        # Verificar adyacencia con cada huella de vecino
        for n_idx, footprint in enumerate(neighbor_footprints):
            if footprint is None:
                continue
            # Distancia mínima entre la curva del lado y la huella
            dist = rs.CurveDistance(side_crv, footprint)
            if dist <= tolerance:
                # Vecino adyacente
                vecino_height = neighbor_heights[n_idx] if n_idx < len(neighbor_heights) else 0.0
                # Fórmula NSR-10 simplificada: S = 0.007 * (h_edu + h_vecino) / 1.5
                nsr_sep = 0.007 * (my_height + vecino_height) / 1.5
                # El setback definitivo es el máximo entre POT y NSR
                final_setback = max(pot_setback, nsr_sep)
                adj_neighbor_height = vecino_height
                # No break; queremos el máximo entre múltiples vecinos adyacentes (si los hubiera)
                # Pero como usamos max con pot_setback y cada nsr_sep, podemos seguir checking

        # Guardar resultados para este lado
        side_data = {
            "side_index": side_idx,
            "setback_m": round(final_setback, 3),
            "neighbor_height_m": round(adj_neighbor_height, 3),
            "pot_setback_m": round(pot_setback, 3),
            "nsr_separation_m": round(nsr_sep, 3) if adj_neighbor_height > 0 else 0.0
        }
        updated_sides.append(side_data)

    # Convertir lista de lados a JSON string
    updated_sides_table = json.dumps(updated_sides, ensure_ascii=False, indent=2)

    # Salidas del componente ya están en las variables:
    # updated_sides_table, neighbor_footprints, neighbor_heights
    # (así que no necesitamos hacer nada más)

# --- Ejecución principal ---
try:
    main()
except Exception as e:
    # En caso de error, producir salida vacía pero informativa
    updated_sides_table = json.dumps({"error": str(e)}, ensure_ascii=False)
    neighbor_footprints = []
    neighbor_heights = []