#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CONFIGURAR_v07.py — Clasificación mejorada con distancia y alineación
GH Python Script para Grasshopper (IronPython 2.7 compatible)

PROPOSITO:
  Clasifica los lados del lote como "Frontal" (colindan con vía) o "Lateral"
  (colindan con vecino) usando DOS criterios:
  1. Distancia mínima a las calles (como en versiones anteriores)
  2. Alineación angular: el segmento debe approximadamente enfrentar a la vía
     (ángulo < 45° entre el vector lote→segmento y la tangente de la calle)

  Esto resuelve el problema de falsos positivos en lotes con segmentos paralelos
  donde tanto el frente como el reverso podían tener distancias similares a la calle.

ENTRADAS: lot_polygon, lot_segments, lot_midpoints, street_curves
SALIDA: sides_table_json (String)

NORMATIVA APLICABLE:
  - Decreto 555/2021, Art. 2.2.6.2.3.3 (Retiros)
  - Lado frontal = colinda con vía/espacio público → aplica retiro frontal normativo
  - Lado lateral = colinda con predio vecino → aplica aislamiento lateral según tipología

================================================================================
"""

import Rhino
import Rhino.Geometry as rg
import json
import math


def to_int_safe(val, default=0):
    if val is None: return default
    try: return int(float(val))
    except: return default


def safe_angle_between(v1, v2):
    """Calcula el ángulo entre dos vectores de forma segura"""
    try:
        if v1.Length < 1e-9 or v2.Length < 1e-9:
            return 180.0  # ángulo máximo para vectores nulos
        cos_angle = max(-1.0, min(1.0, (v1.X * v2.X + v1.Y * v2.Y + v1.Z * v2.Z) /
                                   (v1.Length * v2.Length)))
        return math.degrees(math.acos(cos_angle))
    except:
        return 180.0


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon   = globals().get("lot_polygon", None)
lot_segments  = globals().get("lot_segments", [])
lot_midpoints = globals().get("lot_midpoints", [])
street_curves = globals().get("street_curves", [])

if lot_segments is None: lot_segments = []
if not isinstance(lot_segments, list): lot_segments = [lot_segments]
if lot_midpoints is None: lot_midpoints = []
if not isinstance(lot_midpoints, list): lot_midpoints = [lot_midpoints]
if street_curves is None: street_curves = []
if not isinstance(street_curves, list): street_curves = [street_curves]

# Filtrar None
lot_segments  = [s for s in lot_segments if s is not None]
lot_midpoints = [p for p in lot_midpoints if p is not None]
street_curves = [c for c in street_curves if c is not None]

# --- DIAGNOSTICO DE COORDENADAS ---
print("=== DIAG LADOS v07 ===")
if len(lot_segments) > 0:
    s0 = lot_segments[0]
    print("Lote seg[0]: From=({:.1f},{:.1f}) To=({:.1f},{:.1f})".format(
        s0.From.X, s0.From.Y, s0.To.X, s0.To.Y))

if len(lot_midpoints) > 0:
    mp0 = lot_midpoints[0]
    print("Lote mid[0]: ({:.1f}, {:.1f})".format(mp0.X, mp0.Y))

print("street_curves count: {}".format(len(street_curves)))
for i, sc in enumerate(street_curves[:3]):  # solo primeros 3
    try:
        bbox = sc.GetBoundingBox(rg.Plane.WorldXY)
        print("  CALLE[{}] bbox: ({:.1f},{:.1f}) -> ({:.1f},{:.1f})".format(
            i, bbox.Min.X, bbox.Min.Y, bbox.Max.X, bbox.Max.Y))
    except:
        print("  CALLE[{}]: sin bbox".format(i))

if lot_polygon is None or len(lot_segments) == 0:
    sides_table_json = json.dumps([])
    print("ERROR: falta geometria")
else:
    segment_data = []

    for i, seg in enumerate(lot_segments):
        if i < len(lot_midpoints):
            mid = lot_midpoints[i]
        else:
            mid = rg.Point3d((seg.From.X + seg.To.X) / 2,
                             (seg.From.Y + seg.To.Y) / 2, 0)

        min_dist = float('inf')
        for j, crv in enumerate(street_curves):
            try:
                if not hasattr(crv, 'ClosestPoint'):
                    continue
                success, t = crv.ClosestPoint(mid)
                if success:
                    pt = crv.PointAt(t)
                    dist = mid.DistanceTo(pt)
                    if dist < min_dist:
                        min_dist = dist
            except:
                continue

        segment_data.append({"idx": i, "dist": min_dist, "midpoint": mid, "segment": seg})

    if len(street_curves) == 0:
        print("ADVERTENCIA: street_curves VACIA. Todo Lateral.")
        sides_table = []
        for d in segment_data:
            sides_table.append({
                "side_index": d["idx"],
                "classification": "Lateral",
                "setback_m": 0.0,
                "road_type": "Vecino",
                "dist_to_street_m": 0.0
            })
    else:
        # Calcular estadísticas de distancia
        dists = [d["dist"] for d in segment_data]
        min_d = min(dists)
        max_d = max(dists)
        lot_width = max_d - min_d

        # Umbral adaptativo: mínimo 3m o 15% del ancho del lote
        adaptive_threshold = min_d + max(3.0, lot_width * 0.15)

        print("Dist a calles: min={:.1f}m max={:.1f}m ancho_lote={:.1f}m umbral={:.1f}m".format(
            min_d, max_d, lot_width, adaptive_threshold))

        # Calcular centroide del lote para referencia angular
        lot_centroid = None
        try:
            if lot_polygon:
                area_prop = rg.AreaMassProperties.Compute(lot_polygon)
                lot_centroid = area_prop.Centroid
        except:
            # Fallback: promedio de los puntos medios
            if lot_midpoints:
                sum_x = sum(p.X for p in lot_midpoints)
                sum_y = sum(p.Y for p in lot_midpoints)
                lot_centroid = rg.Point3d(sum_x/len(lot_midpoints), sum_y/len(lot_midpoints), 0)
            else:
                lot_centroid = rg.Point3d(0, 0, 0)

        print("Centroide lote: ({:.1f}, {:.1f})".format(lot_centroid.X, lot_centroid.Y))

        sides_table = []
        for d in segment_data:
            idx = d["idx"]
            dist = d["dist"]
            mid_pt = d["midpoint"]
            seg = d["segment"]

            # CRITERIO 1: Distancia (umbral adaptativo)
            is_close_enough = dist <= adaptive_threshold

            # CRITERIO 2: Alineación angular (nuevo en v07)
            is_facing_street = False
            if lot_centroid:
                # Vector desde centroide del lote al punto medio del segmento
                vec_to_mid = mid_pt - lot_centroid

                # Encontrar la mejor alineación con cualquier calle cercana
                min_angle = 180.0  # iniciar con valor máximo (mala alineación)
                for crv in street_curves:
                    try:
                        success, t = crv.ClosestPoint(mid_pt)
                        if success:
                            pt_on_crv = crv.PointAt(t)
                            # Vector desde punto en calle hacia el punto medio del segmento
                            # (esto apunta desde calle hacia lote)
                            vec_crv_to_mid = mid_pt - pt_on_crv

                            # Obtener tangente aproximada en la calle
                            success_tan, tan_vec = crv.TangentAt(t)
                            if success_tan and tan_vec.Length > 1e-9:
                                # El vector de la calle que apunta hacia el lote es opuesto a vec_crv_to_mid
                                # Pero para el ángulo, lo que importa es la dirección de la calle misma
                                angle = safe_angle_between(vec_to_mid, tan_vec)
                                # También considerar el ángulo opuesto (180 - angle) por si la tangente está invertida
                                angle = min(angle, 180.0 - angle)
                                min_angle = min(min_angle, angle)
                    except:
                        continue

                # Si el segmento mira aproximadamente hacia la calle (dentro de 45°)
                # O si está mirando exactamente opuesto (135-180°) - esto sería el caso trasero
                # Pero queremos solo los que enfrentan a la calle, así que < 45° o > 135° es trasero
                # En realidad, queremos el ángulo más pequeño entre el vector y la dirección de la calle
                is_facing_street = min_angle < 45.0

            # Clasificación final: debe cumplir AMBOS criterios para ser frontal
            # Si no hay calles o no podemos determinar alineación, caeremos a solo distancia
            if len(street_curves) > 0 and lot_centroid:
                is_front = is_close_enough and is_facing_street
                method = "distancia+alineación"
            else:
                # Fallback al método anterior si no podemos hacer el análisis angular
                is_front = is_close_enough
                method = "solo distancia (fallback)"

            cls = "Frontal" if is_front else "Lateral"
            sb = 3.0 if is_front else 0.0
            road_type = "Calle" if is_front else "Vecino"

            sides_table.append({
                "side_index": idx,
                "classification": cls,
                "setback_m": sb,
                "road_type": road_type,
                "dist_to_street_m": round(dist, 2)
            })

            # Logging detallado para diagnóstico
            print("  Lado {}: dist={:.1f}m (umbral={:.1f}) close={} facing={}° -> {} [{}]".format(
                idx, dist, adaptive_threshold, is_close_enough,
                min_angle if 'min_angle' in locals() else 'N/A', cls, method))

        # Estadísticas finales
        nf = sum(1 for s in sides_table if s["classification"] == "Frontal")
        nl = sum(1 for s in sides_table if s["classification"] == "Lateral")
        print("RESULTADO: {}F {}L de {} lados".format(nf, nl, len(sides_table)))

        # Advertencia si parece que no se clasificó ningún lado frontal
        if nf == 0 and len(street_curves) > 0:
            print("ADVERTENCIA: Ningún lado clasificado como Frontal. Revisar datos de entrada.")

    sides_table_json = json.dumps(sides_table)

print("=== FIN LADOS v07 ===")