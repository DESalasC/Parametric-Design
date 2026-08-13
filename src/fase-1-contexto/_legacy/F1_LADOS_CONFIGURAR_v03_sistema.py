#! /usr/bin/env python3
"""
CONFIGURAR_LADOS_v03 - Clasificacion automatica de lados del lote
"""

import Rhino.Geometry as rg
import json

# === FUNCIONES AUXILIARES ===
def to_int(val, default=0):
    try: return int(float(val))
    except (ValueError, TypeError): return default

def to_float(val, default=0.0):
    try: return float(val)
    except (ValueError, TypeError): return default

def get_road_class_by_width(width_m):
    w = to_float(width_m, 0)
    if w <= 0: return "SIN_DATO"
    if w >= 30: return "Arterial_Principal"
    elif w >= 22: return "Arterial_Complementaria"
    elif w >= 15: return "Colectora"
    elif w >= 11: return "Local"
    else: return "Peatonal"

def parse_json_input(data):
    if not data: return {}
    if isinstance(data, str):
        try: return json.loads(data)
        except: return {}
    return data if isinstance(data, dict) else {}

# === OBTENCIÓN SEGURA DE INPUTS ===
lot_poly = globals().get("lot_polygon", None)
lot_segments = globals().get("lot_segments", [])
lot_midpoints = globals().get("lot_midpoints", [])
street_curves = globals().get("street_curves", [])
pot_conclusions = globals().get("pot_conclusions", None)
floors_per_tower = globals().get("floors_per_tower", 4)
bonus_input = globals().get("bonus_floor", False)

# Asegurarse de que sean listas
if lot_segments is None: lot_segments = []
if not isinstance(lot_segments, list): lot_segments = [lot_segments]

if lot_midpoints is None: lot_midpoints = []
if not isinstance(lot_midpoints, list): lot_midpoints = [lot_midpoints]

if street_curves is None: street_curves = []
if not isinstance(street_curves, list): street_curves = [street_curves]

bonus_floor = 1 if bonus_input else 0

if lot_poly is None: raise ValueError("Falta lot_polygon")
if not lot_segments: raise ValueError("Falta lot_segments. Asegurate de conectar el Explode del lote.")
if pot_conclusions is None: raise ValueError("Falta pot_conclusions")

# 1. Deserializar el POT
pot_dict = parse_json_input(pot_conclusions)

# 2. Altura y Pisos
height_limits = pot_dict.get("height_limits", {})
max_height_m = to_float(height_limits.get("altura_efectiva_m", 0), 0)
max_floors_pot = to_int(floors_per_tower, 4)

total_floors = max_floors_pot + bonus_floor
if max_height_m > 0 and total_floors > 0:
    fh = max_height_m / total_floors
else:
    fh = 3.0

road_analysis = pot_dict.get("road_analysis", [])

# 3. Calcular distancia de cada segmento a la calle más cercana
segment_data = []
for i, seg in enumerate(lot_segments):
    if not seg: continue
    
    if i < len(lot_midpoints):
        mid = lot_midpoints[i]
    else:
        mid = rg.AreaMassProperties.Compute(seg).Centroid
        
    min_dist = float('inf')
    closest_street_idx = -1
    
    for j, crv in enumerate(street_curves):
        if not crv: continue
        try:
            success, t = crv.ClosestPoint(mid)
            if success:
                pt_on_crv = crv.PointAt(t)
                dist = mid.DistanceTo(pt_on_crv)
                if dist < min_dist:
                    min_dist = dist
                    closest_street_idx = j
        except:
            continue
            
    segment_data.append({
        "idx": i, 
        "dist": min_dist, 
        "street_idx": closest_street_idx
    })

# 4. CLASIFICACIÓN ADAPTATIVA
front_indices = []
non_front_indices = []

if segment_data:
    min_dist_overall = min(d["dist"] for d in segment_data)
    front_tolerance = 5.0 
    
    for d in segment_data:
        if d["dist"] <= min_dist_overall + front_tolerance:
            front_indices.append(d["idx"])
        else:
            non_front_indices.append(d["idx"])

posterior_idx = -1
if non_front_indices:
    non_front_data = [d for d in segment_data if d["idx"] in non_front_indices]
    furthest = max(non_front_data, key=lambda x: x["dist"])
    posterior_idx = furthest["idx"]

# 5. Construir la tabla de lados
sides_table = []
for data in segment_data:
    i = data["idx"]
    is_front = i in front_indices
    is_posterior = (i == posterior_idx)
    
    road_type = "N/A"
    road_width = 0.0
    balcony_allowed = False
    balcony_max_depth = 0.0
    setback = 3.0 
    
    if is_front:
        classification = "Frontal"
        street_idx = data["street_idx"]
        
        if street_idx >= 0 and street_idx < len(road_analysis):
            street_data = road_analysis[street_idx]
            road_width = to_float(street_data.get("road_width_m", 0))
        
        if road_width == 0:
            road_width = 15.0 
            
        road_type = get_road_class_by_width(road_width)
        
        if "Arterial" in road_type or road_width >= 22:
            balcony_allowed = True
            balcony_max_depth = 1.2
            setback = 5.0
        elif "Colectora" in road_type or road_width >= 15:
            balcony_allowed = True
            balcony_max_depth = 1.0
            setback = 4.0
        else:
            balcony_allowed = True
            balcony_max_depth = 0.8
            setback = 3.0
            
    elif is_posterior:
        classification = "Posterior"
        neighbor_height = 0.0
        setback = max(3.0, neighbor_height * 0.5)
    else:
        classification = "Lateral"
        neighbor_height = 0.0
        setback = max(3.0, neighbor_height * 0.5)

    sides_table.append({
        "side_index": i, "classification": classification, "road_type": road_type,
        "road_width_m": road_width, "setback_m": setback, "balcony_allowed": balcony_allowed,
        "balcony_max_depth_m": balcony_max_depth, "neighbor_height_m": 0.0, 
        "separation_required_m": setback, "is_access": is_front
    })
# === CALCULAR SOLICITUD JSON: perímetro_edificable, altura_maxima_pisos, aislamientos_aplicados, área_neta_por_piso ===

# 1. Altura máxima en pisos (desde POT)
height_limits = pot_dict.get("height_limits", {})
altura_efectiva_m = to_float(height_limits.get("altura_efectiva_m", 0))
FLOOR_HEIGHT_DEFAULT = 3.0  # metros por piso
altura_maxima_pisos = int(altura_efectiva_m / FLOOR_HEIGHT_DEFAULT) if altura_efectiva_m > 0 else 0

# 2. Aislamientos aplicados (de cada lado)
try:
    sides_list = json.loads(sides_table)  # lados ya viene como JSON string
    aislamientos_aplicados = []
    for side in sides_list:
        aislamientos_aplicados.append({
            "side_index": side["side_index"],
            "classification": side["classification"],
            "setback_m": side["setback_m"],
            "road_type": side["road_type"]
        })
except:
    aislamientos_aplicados = []

# 3. Perímetro edificable y área neta por piso (usando offset de polígono)
perimetro_edificable = 0.0
area_neta_por_piso = 0.0

try:
    if lot_polygon and hasattr(lot_polygon, 'IsClosed') and lot_polygon.IsClosed:
        # Extraer todos los setbacks para cálculo conservador
        setbacks = [side["setback_m"] for side in json.loads(sides_table)] if 'sides_table' in locals() else [3.0]
        min_setback = min(setbacks) if setbacks else 0.0

        # Offset hacia adentro (negativo) para obtener el área/perímetro edificable
        offset_curves = lot_polygon.Offset(
            rg.Plane.WorldXY,
            -min_setback,
            0.1,
            rg.CurveOffsetCornerStyle.Sharp
        )

        if offset_curves:
            offset_curve = offset_curves[0]  # Tomar la primera curva offset
            if offset_curve.IsClosed:
                perimetro_edificable = offset_curve.GetLength()
                area_mass = rg.AreaMassProperties.Compute(offset_curve)
                area_neta_por_piso = area_mass.Area
            else:
                # Fallback si el offset no resulta en curva cerrada
                perimetro_edificable = lot_polygon.GetLength()
                area_total = rg.AreaMassProperties.Compute(lot_polygon).Area
                perimetro_total = lot_polygon.GetLength()
                area_neta_por_piso = max(0, area_total - (perimetro_total * min_setback))
        else:
            # Fallback si el offset falla
            perimetro_edificable = lot_polygon.GetLength()
            area_total = rg.AreaMassProperties.Compute(lot_polygon).Area
            perimetro_total = lot_polygon.GetLength()
            area_neta_por_piso = max(0, area_total - (perimetro_total * (sum(setbacks)/len(setbacks) if setbacks else 0)))
    else:
        # Valores por defecto si no hay polígono válido
        perimetro_edificable = 0.0
        area_neta_por_piso = 0.0
except Exception as e:
    print(f"Error en cálculo de perímetro/área edificable: {e}")
    perimetro_edificable = lot_polygon.GetLength() if lot_polygon else 0.0
    try:
        area_total = rg.AreaMassProperties.Compute(lot_polygon).Area if lot_polygon else 0.0
    except:
        area_total = 0.0
    area_neta_por_piso = max(0, area_total - (perimetro_edificable * 3.0))  # valor por defecto conservador

# 4. Crear el JSON solicitado
result_json = {
    "perimetro_edificable": round(perimetro_edificable, 2),
    "altura_maxima_pisos": altura_maxima_pisos,
    "aislamientos_aplicados": aislamientos_aplicados,
    "area_neta_por_piso": round(area_neta_por_piso, 2)
}

# Convertir a string JSON para salida de Grasshopper
import json
resultado_json_string = json.dumps(result_json, indent=2, ensure_ascii=False)

Updated Outputs:

Add resultado_json_string as a new output alongside the existing ones:
- sides_table (existing)
- pot_compliance (existing)
- balcony_rules_summary (existing)
- resultado_json (NEW - the requested JSON)

Complementary Improvement to CONTEXTO_v04a.py

To make the height information more directly accessible, consider adding this to the end of CONTEXTO_v04a.py:

# Salida adicional para fácil acceso: altura maxima en pisos
if urban_data["altura_max"]:
    altura_maxima_pisos_pot = int(float(urban_data["altura_max"]) / 3.0)
else:
    altura_maxima_pisos_pot = int((urban_data.get("altura_max") or 12) / 3.0)

This would make the piso calculation directly available as an output.

Expected JSON Output Format:

The proposed solution will generate a JSON like:
{
  "perimetro_edificable": 120.5,
  "altura_maxima_pisos": 8,
  "aislamientos_aplicados": [
    {
      "side_index": 0,
      "classification": "Frontal",
      "setback_m": 5.0,
      "road_type": "Arterial_Principal"
    },
    {
      "side_index": 1,
      "classification": "Lateral",
      "setback_m": 3.0,
      "road_type": "Local"
    }
  ],
  "area_neta_por_piso": 350.25
}

# 6. Salidas
pot_compliance = {
    "height_max_m": max_height_m, "height_max_floors": max_floors_pot,
    "bonus_floor_applied": bonus_floor > 0, "total_floors_effective": total_floors,
    "floor_height_m": fh, "front_side_indices": front_indices
}

balcony_rules_summary = {
    "front_has_balcony": any(s["balcony_allowed"] for s in sides_table if s["classification"] == "Frontal"),
    "front_balcony_depth": max([s["balcony_max_depth_m"] for s in sides_table if s["classification"] == "Frontal"] or [0]),
}

# Convertir a JSON
sides_table_json = json.dumps(sides_table)
pot_compliance_json = json.dumps(pot_compliance)
balcony_rules_summary_json = json.dumps(balcony_rules_summary)
resultado_json_string = json.dumps({
    "perimetro_edificable": round(perimetro_edificable, 2),
    "altura_maxima_pisos": altura_maxima_pisos,
    "aislamientos_aplicados": aislamientos_aplicados,
    "area_neta_por_piso": round(area_neta_por_piso, 2)
})

# Vector de análisis vecinal (simulado si no se tiene el componente VECINOS_ANALISIS_v02.py)
vecino_analisis_json = json.dumps({
    "zon_sismica": "ZONA_MEDIA",
    "tipo_suelo": "SUELO_TYPE_A",
    "altura_maxima_permitida": altura_maxima_pisos * 3.0,  # Convertir pies a metros aproximado
    "setbacks": {
        "norte": 3.0,
        "sur": 3.0,
        "este": 3.0,
        "oeste": 3.0
    }
})

front_str = ", ".join(str(x) for x in front_indices)
a = "Lados: {} | Frentes: [{}] | Posterior: {} | Altura POT: {}m | Pisos: {}+{} | Altura Piso: {:.2f}m".format(
    len(segment_data), front_str, posterior_idx, max_height_m, max_floors_pot, bonus_floor, fh)