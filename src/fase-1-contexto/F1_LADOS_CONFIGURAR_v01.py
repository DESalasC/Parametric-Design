#! /usr/bin/env python3
"""
CONFIGURAR_LADOS_v04 - Clasificacion automatica de lados del lote
Usa JSON de caché POT para datos normativos y geometría local para cálculos.

ENTRADAS:
  - lot_polygon: Polígono del lote (Curve cerrado en plano XY)
  - lot_segments: Lista de segmentos de línea que representan los lados del lote (Curve)
  - lot_midpoints: Puntos medios de cada segmento (Point3d)
  - street_curves: Curvas de calles (Curve) con atributos de clasificación vial
  - json_path: Ruta al JSON de caché POT para este lote (contiene datos precalculados)
  - floors_per_tower: Número de pisos del edificio nuevo (int)
  - bonus_input: Indicador de aumento de piso (bool)
  - losas_coincide: (Opcional, default False) Indicar si las losas del edificio nuevo y del vecino coinciden

SALIDAS:
  - sides_table_json: JSON string con tabla de lados (clasificación, retiros, balcones, etc.)
  - pot_compliance_json: JSON string con datos de cumplimiento de altura y pisos
  - balcony_rules_summary_json: JSON string con resumen de reglas de balcones
  - resultado_json_string: JSON string solicitado (perimetro_edificable, altura_maxima_pisos, aislamientos_aplicados, area_neta_por_piso)
  - vecino_analisis_json: JSON string simulado para análisis vecinal (si no se tiene el componente VECINOS_ANALISIS)
"""

import json
import math
import os
from pathlib import Path

# Intentar usar rhinoscriptsyntax (disponible en GHPython)
try:
    import Rhino.Geometry as rg
    import rhinoscriptsyntax as rs
except ImportError:
    # Fallback mínimo para pruebas externas (no se espera llegar aquí en GH)
    rg = None
    rs = None

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def to_int(val, default=0):
    try: return int(float(val))
    except (ValueError, TypeError): return default

def to_float(val, default=0.0):
    try: return float(val)
    except (ValueError, TypeError): return default

def get_road_class_by_width(width_m):
    """Clasificación vial basada en ancho de vía (metros)."""
    w = to_float(width_m, 0)
    if w <= 0: return "SIN_DATO"
    if w >= 30: return "Arterial_Principal"
    elif w >= 22: return "Arterial_Complementaria"
    elif w >= 15: return "Colectora"
    elif w >= 11: return "Local"
    else: return "Peatonal"

def parse_json_input(data):
    """Parsear entrada JSON de forma segura."""
    if not data: return {}
    if isinstance(data, str):
        try: return json.loads(data)
        except: return {}
    return data if isinstance(data, dict) else {}

def load_pot_cache(json_path):
    """Cargar datos normativos desde el caché POT (JSON)."""
    if not json_path or not isinstance(json_path, str) or not json_path.strip():
        return None
    path = Path(json_path.strip())
    if not path.exists():
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error leyendo caché POT: {e}")
        return None

# ============================================================
# OBTENCIÓN SEGURA DE INPUTS
# ============================================================

lot_poly = globals().get("lot_polygon", None)
lot_segments = globals().get("lot_segments", [])
lot_midpoints = globals().get("lot_midpoints", [])
street_curves = globals().get("street_curves", [])
pot_connections = globals().get("pot_connections", None)  # Mantener por compatibilidad, pero preferir json_path
floors_per_tower = globals().get("floors_per_tower", 4)
bonus_input = globals().get("bonus_floor", False)
json_path = globals().get("json_path", None)  # Nueva entrada principal
losas_coincide = globals().get("losas_coincide", False)

# Asegurarse de que sean listas
if lot_segments is None: lot_segments = []
if not isinstance(lot_segments, list): lot_segments = [lot_segments]
if lot_midpoints is None: lot_midpoints = []
if not isinstance(lot_midpoints, list): lot_midpoints = [lot_midpoints]
if street_curves is None: street_curves = []
if not isinstance(street_curves, list): street_curves = [street_curves]

bonus_floor = 1 if bonus_input else 0

if lot_poly is None: raise ValueError("Falta lot_polygon")
if not lot_segments: raise ValueError("Falta lot_segments. Conecte el Explode del lote.")

# Cargar caché POT
pot_data = load_pot_cache(json_path) if json_path else None
if pot_data:
    print(f"Cargado caché POT desde: {json_path}")
else:
    print("Advertencia: No se proporcionó caché POT válido. Se usarán valores por defecto o se calcularán desde geometría.")

# ============================================================
# 1. DESERIALIZAR EL POT (si se proporciona)
# ============================================================

# Si se proporciona pot_connections (por compatibilidad), usarlo como fallback
pot_dict = parse_json_input(pot_connections) if pot_connections else {}
if pot_data:
    # Sobrescribir con los datos del caché
    pot_dict = pot_data

# ============================================================
# 2. ALTURA Y PISOS
# ============================================================

height_limits = pot_dict.get("height_limits", {})
max_height_m = to_float(height_limits.get("altura_efectiva_m", 0), 0)
max_floors_pot = to_int(floors_per_tower, 4)  # Entrada de Grasshopper tiene prioridad

# Si no se proporciona floors_per_tower, intentar obtenerlo del caché
if floors_per_tower == 4 and 'floors_per_tower' not in globals():
    # Intentar obtener número de pisos desde altura_máx del tratamiento urbano
    altura_max_trat = height_limits.get("altura_max_tratamiento")
    if altura_max_trat is not None:
        max_floors_pot = max(1, int(round(float(altura_max_trat) / 3.0)))

total_floors = max_floors_pot + bonus_floor

if max_height_m > 0 and total_floors > 0:
    fh = max_height_m / total_floors
else:
    fh = 3.0  # altura típica por piso

# ============================================================
# 3. ANÁLISIS VIAL (usar street_curves de entrada)
# ============================================================

road_analysis = pot_dict.get("road_analysis", [])
if not road_analysis and street_curves:
    # Calcular análisis vial desde las curvas de entrada (similar a F1_CONTEXTO_POT)
    # Convertir street_curves a lista de tuplas (curva, propiedades)
    vial_curves = []
    for crv in street_curves:
        props = {}
        if rs:
            try:
                user_text = rs.GetUserText(crv)
                if user_text:
                    # Intentar parsear como JSON
                    try:
                        props = json.loads(user_text)
                    except:
                        # Si no es JSON, asumir pares clave-valor separados por ;
                        for pair in user_text.split(';'):
                            if '=' in pair:
                                k, v = pair.split('=', 1)
                                props[k.strip()] = v.strip()
            except:
                pass
        vial_curves.append((crves.append((crv, props))

    if vial_curves:
        # Calcular anchos de vía (función de F1_CONTEXTO_POT, adaptada)
        def calculate_road_width_local(street_curves, lot_polygon, lot_centroid):
            road_widths = []
            for crv, props in street_curves:
                if not rs or not rs.CurveCurveIntersection(lot_polygon, crv):
                    continue
                cls_vial = props.get("CLASIFICACION_VIAL") or props.get("TIPO_VIA") or "DESCONOCIDO"
                ancho_gdb = props.get("ANCHO") or props.get("ANCHO_VIA") or props.get("SECCION")
                if ancho_gdb:
                    try:
                        ancho = float(ancho_gdb)
                    except:
                        ancho = None
                else:
                    cls_lower = str(cls_vial).lower()
                    if "arterial" in cls_lower and "principal" in cls_lower:
                        ancho = 30
                    elif "arterial" in cls_lower:
                        ancho = 22
                    elif "colector" in cls_lower or "colectora" in cls_lower:
                        ancho = 18
                    elif "local" in cls_lower:
                        ancho = 10
                    elif "peatonal" in cls_lower:
                        ancho = 6
                    else:
                        ancho = 12
                road_widths.append({
                    "classification": cls_vial,
                    "width_m": ancho,
                    "source": "GDB_PROPERTY" if ancho_gdb else "ESTIMATED_BY_CLASS",
                    "properties": props
                })
            return road_widths

        road_widths = calculate_road_width_local(vial_curves, lot_polygon, lot_centroid)

        # Número de pisos para cálculo de retiros y balcones
        altura_max_urb = height_limits.get("altura_max_tratamiento")
        if altura_max_urb is None:
            altura_max_urb = max_height_m if max_height_m > 0 else 12.0
        building_floors = max(1, int(round(float(altura_max_urb) / 3.0)))

        for i, (crv, props) in enumerate(vial_curves):
            width_info = road_widths[i] if i < len(road_widths) else {"width_m": None, "source": "NO_CALCULADO", "properties": props}
            cls = props.get("CLASIFICACION_VIAL") or props.get("TIPO_VIA") or "DESCONOCIDO"
            # Calcular setbacks y balcones usando funciones de F1_CONTEXTO_POT (adaptadas)
            def get_setbacks_for_road_class_local(classification, floors):
                cls_key = None
                cls_lower = str(classification).lower()
                if "arterial" in cls_lower and "principal" in cls_lower:
                    cls_key = "arterial_principal"
                elif "arterial" in cls_lower:
                    cls_key = "arterial_complementaria"
                elif "colector" in cls_lower or "colectora" in cls_lower:
                    cls_key = "colectora"
                elif "local" in cls_lower:
                    cls_key = "local"
                elif "peatonal" in cls_lower:
                    cls_key = "peatonal"
                else:
                    cls_key = "local"
                # Parámetros hardcodeados (igual que en F1_CONTEXTO_POT)
                params = {
                    "arterial_principal": {"retiro_frontal": 5.0, "retiro_lateral": 3.0, "retiro_posterior": 3.0,
                                           "ancho_tipico_min": 25, "ancho_tipico_max": 40,
                                           "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
                    "arterial_complementaria": {"retiro_frontal": 4.0, "retiro_lateral": 3.0, "retiro_posterior": 3.0,
                                                "ancho_tipico_min": 20, "ancho_tipico_max": 30,
                                                "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
                    "colectora": {"retiro_frontal": 3.0, "retiro_lateral": 2.5, "retiro_posterior": 3.0,
                                  "ancho_tipico_min": 15, "ancho_tipico_max": 25,
                                  "permite_balcon": True, "balcon_max": 1.0, "balcon_solo_superior": True},
                    "local": {"retiro_frontal": 3.0, "retiro_lateral": 2.0, "retiro_posterior": 2.5,
                              "ancho_tipico_min": 8, "ancho_tipico_max": 15,
                              "permite_balcon": True, "balcon_max": 0.8, "balcon_solo_superior": True},
                    "peatonal": {"retiro_frontal": 2.0, "retiro_lateral": 1.5, "retiro_posterior": 2.0,
                                 "ancho_tipico_min": 4, "ancho_tipico_max": 10,
                                 "permite_balcon": False, "balcon_max": 0.0, "balcon_solo_superior": False},
                }[cls_key]
                inc = max(0, (floors - 2)) * 0.5  # RETIRO_INCREMENTO_POR_PISO = 0.5, ALTURA_BASE_RETIRO = 2
                return {
                    "classification_used": cls_key,
                    "original_classification": classification,
                    "front": params["retiro_frontal"] + inc,
                    "side": params["retiro_lateral"] + inc,
                    "rear": params["retiro_posterior"] + inc,
                    "increment_per_floor_above_2": 0.5,
                    "source_norm": "Decreto 555/2021 Art. 2.2.6.2.3.3"
                }

            def get_balcony_rules_local(classification, road_width_m, floors):
                cls_key = None
                cls_lower = str(classification).lower()
                if "arterial" in cls_lower and "principal" in cls_lower:
                    cls_key = "arterial_principal"
                elif "arterial" in cls_lower:
                    cls_key = "arterial_complementaria"
                elif "colector" in cls_lower or "colectora" in cls_lower:
                    cls_key = "colectora"
                elif "local" in cls_lower:
                    cls_key = "local"
                elif "peatonal" in cls_lower:
                    cls_key = "peatonal"
                else:
                    cls_key = "local"
                params = {
                    "arterial_principal": {"ancho_tipico_min": 25, "ancho_tipico_max": 40,
                                           "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
                    "arterial_complementaria": {"ancho_tipico_min": 20, "ancho_tipico_max": 30,
                                                "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
                    "colectora": {"ancho_tipico_min": 15, "ancho_tipico_max": 25,
                                  "permite_balcon": True, "balcon_max": 1.0, "balcon_solo_superior": True},
                    "local": {"ancho_tipico_min": 8, "ancho_tipico_max": 15,
                              "permite_balcon": True, "balcon_max": 0.8, "balcon_solo_superior": True},
                    "peatonal": {"ancho_tipico_min": 4, "ancho_tipico_max": 10,
                                 "permite_balcon": False, "balcon_max": 0.0, "balcon_solo_superior": False},
                }[cls_key]
                ancho_min = params["ancho_tipico_min"]
                ancho_max = params["ancho_tipico_max"]
                width_warning = None
                if road_width_m:
                    if road_width_m < ancho_min:
                        width_warning = f"ANCHO VIA ({road_width_m}m) < MÍNIMO TIPICO {cls_key} ({ancho_min}m) - REVISAR CLASIFICACIÓN"
                    elif road_width_m > ancho_max:
                        width_warning = f"ANCHO VIA ({road_width_m}m) > MÁXIMO TIPICO {cls_key} ({ancho_max}m) - POSIBLE RECLASIFICACIÓN"
                permite_balcon = params["permite_balcon"]
                balcon_max = params["balcon_max"]
                solo_superior = params["balcon_solo_superior"]
                pisos_permitidos = list(range(3, floors + 1)) if solo_superior else list(range(1, floors + 1))
                return {
                    "classification_used": cls_key,
                    "original_classification": classification,
                    "road_width_m": road_width_m,
                    "width_validation": "OK" if not width_warning else width_warning,
                    "permite_balcon": permite_balcon,
                    "balcon_max_m": balcon_max if permite_balcon else 0.0,
                    "balcon_solo_pisos_superiores": solo_superior,
                    "pisos_permitidos_balcon": pisos_permitidos,
                    "norma_ref": "Decreto 555/2021 Art. 2.2.6.2.3.3 + Planes Parciales"
                }

            setbacks = get_setbacks_for_road_class_local(cls, building_floors)
            balcony = get_balcony_rules_local(cls, width_info["width_m"], building_floors)
            road_analysis.append({
                "street_id": i,
                "classification": cls,
                "road_width_m": width_info["width_m"],
                "width_source": width_info["source"],
                "setbacks": setbacks,
                "balcony_rules": balcony,
                "trace": f"Calle {i}: {cls} | Ancho={width_info['width_m']}m ({width_info['source']}) | Retiros F:{setbacks['front']} S:{setbacks['side']} P:{setbacks['rear']} | Balcón max={balcony['balcon_max_m']}m {'(solo pisos>2)' if balcony['balcon_solo_pisos_superiores'] else '(todos pisos)'}",
                "properties": props
            })

        road_classification_str = ", ".join(set(v["classification"] for v in road_analysis)) if road_analysis else "NINGUNA"
    else:
        road_analysis = []
        road_classification_str = "NINGUNA"
else:
    # Si tenemos road_analysis del caché, asegurar que tengan setbacks y balcones calculados con los pisos actuales
    if road_analysis:
        altura_max_urb = height_limits.get("altura_max_tratamiento")
        if altura_max_urb is None:
            altura_max_urb = max_height_m if max_height_m > 0 else 12.0
        building_floors = max(1, int(round(float(altura_max_urb) / 3.0)))
        for street in road_analysis:
            cls = street["classification"]
            width_m = street["road_width_m"]
            # Recalcular setbacks y balcones
            def get_setbacks_for_road_class_local(classification, floors):
                cls_key = None
                cls_lower = str(classification).lower()
                if "arterial" in cls_lower and "principal" in cls_lower:
                    cls_key = "arterial_principal"
                elif "arterial" in cls_lower:
                    cls_key = "arterial_complementaria"
                elif "colector" in cls_lower or "colectora" in cls_lower:
                    cls_key = "colectora"
                elif "local" in cls_lower:
                    cls_key = "local"
                elif "peatonal" in cls_lower:
                    cls_key = "peatonal"
                else:
                    cls_key = "local"
                params = {
                    "arterial_principal": {"retiro_frontal": 5.0, "retiro_lateral": 3.0, "retiro_posterior": 3.0,
                                           "ancho_tipico_min": 25, "ancho_tipico_max": 40,
                                           "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
                    "arterial_complementaria": {"retiro_frontal": 4.0, "retiro_lateral": 3.0, "retiro_posterior": 3.0,
                                                "ancho_tipico_min": 20, "ancho_tipico_max": 30,
                                                "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
                    "colectora": {"retiro_frontal": 3.0, "retiro_lateral": 2.5, "retiro_posterior": 3.0,
                                  "ancho_tipico_min": 15, "ancho_tipico_max": 25,
                                  "permite_balcon": True, "balcon_max": 1.0, "balcon_solo_superior": True},
                    "local": {"retiro_frontal": 3.0, "retiro_lateral": 2.0, "retiro_posterior": 2.5,
                              "ancho_tipico_min": 8, "ancho_tipico_max": 15,
                              "permite_balcon": True, "balcon_max": 0.8, "balcon_solo_superior": True},
                    "peatonal": {"retiro_frontal": 2.0, "retiro_lateral": 1.5, "retiro_posterior": 2.0,
                                 "ancho_tipico_min": 4, "ancho_tipico_max": 10,
                                 "permite_balcon": False, "balcon_max": 0.0, "balcon_solo_superior": False},
                }[cls_key]
                inc = max(0, (floors - 2)) * 0.5
                return {
                    "classification_used": cls_key,
                    "original_classification": classification,
                    "front": params["retiro_frontal"] + inc,
                    "side": params["retiro_lateral"] + inc,
                    "rear": params["retiro_posterior"] + inc,
                    "increment_per_floor_above_2": 0.5,
                    "source_norm": "Decreto 555/2021 Art. 2.2.6.2.3.3"
                }

            def get_balcony_rules_local(classification, road_width_m, floors):
                cls_key = None
                cls_lower = str(classification).lower()
                if "arterial" in cls_lower and "principal" in cls_lower:
                    cls_key = "arterial_principal"
                elif "arterial" in cls_lower:
                    cls_key = "arterial_complementaria"
                elif "colector" in cls_lower or "colectora" in cls_lower:
                    cls_key = "colectora"
                elif "local" in cls_lower:
                    cls_key = "local"
                elif "peatonal" in cls_lower:
                    cls_key = "peatonal"
                else:
                    cls_key = "local"
                params = {
                    "arterial_principal": {"ancho_tipico_min": 25, "ancho_tipico_max": 40,
                                           "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
                    "arterial_complementaria": {"ancho_tipico_min": 20, "ancho_tipico_max": 30,
                                                "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
                    "colectora": {"ancho_tipico_min": 15, "ancho_tipico_max": 25,
                                  "permite_balcon": True, "balcon_max": 1.0, "balcon_solo_superior": True},
                    "local": {"ancho_tipico_min": 8, "ancho_tipico_max": 15,
                              "permite_balcon": True, "balcon_max": 0.8, "balcon_solo_superior": True},
                    "peatonal": {"ancho_tipico_min": 4, "ancho_tipico_max": 10,
                                 "permite_balcon": False, "balcon_max": 0.0, "balcon_solo_superior": False},
                }[cls_key]
                ancho_min = params["ancho_tipico_min"]
                ancho_max = params["ancho_tipico_max"]
                width_warning = None
                if road_width_m:
                    if road_width_m < ancho_min:
                        width_warning = f"ANCHO VIA ({road_width_m}m) < MÍNIMO TIPICO {cls_key} ({ancho_min}m) - REVISAR CLASIFICACIÓN"
                    elif road_width_m > ancho_max:
                        width_warning = f"ANCHO VIA ({road_width_m}m) > MÁXIMO TIPICO {cls_key} ({ancho_max}m) - POSIBLE RECLASIFICACIÓN"
                permite_balcon = params["permite_balcon"]
                balcon_max = params["balcon_max"]
                solo_superior = params["balcon_solo_superior"]
                pisos_permitidos = list(range(3, floors + 1)) if solo_superior else list(range(1, floors + 1))
                return {
                    "classification_used": cls_key,
                    "original_classification": classification,
                    "road_width_m": road_width_m,
                    "width_validation": "OK" if not width_warning else width_warning,
                    "permite_balcon": permite_balcon,
                    "balcon_max_m": balcon_max if permite_balcon else 0.0,
                    "balcon_solo_pisos_superiores": solo_superior,
                    "pisos_permitidos_balcon": pisos_permitidos,
                    "norma_ref": "Decreto 555/2021 Art. 2.2.6.2.3.3 + Planes Parciales"
                }

            setbacks = get_setbacks_for_road_class_local(cls, building_floors)
            balcony = get_balcony_rules_local(cls, width_m, building_floors)
            street["setbacks"] = setbacks
            street["balcony_rules"] = balcony
            street["trace"] = f"Calle {street['street_id']}: {cls} | Ancho={width_m}m ({street['width_source']}) | Retiros F:{setbacks['front']} S:{setbacks['side']} P:{setbacks['rear']} | Balcón max={balcony['balcon_max_m']}m {'(solo pisos>2)' if balcony['balcon_solo_pisos_superiores'] else '(todos pisos)'}"
        road_classification_str = ", ".join(set(v["classification"] for v in road_analysis)) if road_analysis else "NINGUNA"
    else:
        road_classification_str = "NINGUNA"

# ============================================================
# 4. CLASIFICACIÓN ADAPTATIVA DE LADOS
# ============================================================

# Calcular distancia de cada segmento a la calle más cercana
segment_data = []
for i, seg in enumerate(lot_segments):
    if not seg: continue
    if i < len(lot_midpoints):
        mid = lot_midpoints[i]
    else:
        if rs:
            mid = rg.AreaMassProperties.Compute(seg).Centroid
        else:
            mid = None
            continue

    min_dist = float('inf')
    closest_street_idx = -1
    for j, crv in enumerate(street_curves):
        if not crv: continue
        if rs:
            success, t = crv.ClosestPoint(mid)
            if success:
                pt_on_crv = crv.PointAt(t)
                dist = mid.DistanceTo(pt_on_crv)
                if dist < min_dist:
                    min_dist = dist
                    closest_street_idx = j
    else:
        # Sin rs, asumir distancia infinita
        continue

    segment_data.append({
        "idx": i,
        "dist": min_dist,
        "street_idx": closest_street_idx
    })

# Determinar lados frontales, laterales y posteriores
front_indices = []
non_front_indices = []
if segment_data:
    min_dist_overall = min(d["dist"] for d in segment_data)
    front_tolerance = 5.0  # metros
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

# ============================================================
# 5. OBTENER RETIROS DEL CACHÉ POT (si se proporciona)
# ============================================================

# Valores por defecto
frontal_m = 3.0
lateral_izq_m = 3.0
lateral_der_m = 3.0
posterior_m = 3.0

if pot_data:
    retiros = pot_data.get("setbacks_by_road_type", {})  # Estructura: {clasificacion: {front: x, side: y, rear: z}}
    # También podría estar bajo "retiros" directamente
    if not retiros:
        retiros = pot_data.get("retiros", {})
    if retiros:
        # Intentar obtener valores por clasificación de vía frontal
        # Asumimos que la primera calle frontal es representativa
        if front_indices and road_analysis:
            first_front_idx = front_indices[0]
            if first_front_idx < len(road_analysis):
                street_class = road_analysis[first_front_idx]["classification"]
                # Normalizar la clasificación para buscar en el caché
                class_key = None
                class_lower = str(street_class).lower()
                if "arterial" in class_lower and "principal" in class_lower:
                    class_key = "arterial_principal"
                elif "arterial" in class_lower:
                    class_key = "arterial_complementaria"
                elif "colector" in class_lower or "colectora" in class_lower:
                    class_key = "colectora"
                elif "local" in class_lower:
                    class_key = "local"
                elif "peatonal" in class_lower:
                    class_key = "peatonal"
                else:
                    class_key = "local"
                if class_key in retiros:
                    vals = retiros[class_key]
                    frontal_m = to_float(vals.get("frontal_m", frontal_m), frontal_m)
                    lateral_izq_m = to_float(vals.get("lateral_izq_m", lateral_izq_m), lateral_izq_m)
                    lateral_der_m = to_float(vals.get("lateral_der_m", lateral_der_m), lateral_der_m)
                    posterior_m = to_float(vals.get("posterior_m", posterior_m), posterior_m)
                else:
                    # Intentar con la clave tal cual
                    if street_class in retiros:
                        vals = retiros[street_class]
                        frontal_m = to_float(vals.get("frontal_m", frontal_m), frontal_m)
                        lateral_izq_m = to_float(vals.get("lateral_izq_m", lateral_izq_m), lateral_izq_m)
                        lateral_der_m = to_float(vals.get("lateral_der_m", lateral_der_m), lateral_der_m)
                        posterior_m = to_float(vals.get("posterior_m", posterior_m), posterior_m)
            # Si no se encontró por clasificación, usar promedio de los valores disponibles
            if frontal_m == 3.0 and lateral_izq_m == 3.0 and lateral_der_m == 3.0 and posterior_m == 3.0:
                # Calcular promedio de todos los valores en el caché
                fronts = []
                sides = []
                rears = []
                for key, vals in retiros.items():
                    if isinstance(vals, dict):
                        if "frontal_m" in vals:
                            fronts.append(to_float(vals["frontal_m"], 0))
                        if "lateral_izq_m" in vals:
                            sides.append(to_float(vals["lateral_izq_m"], 0))
                        if "lateral_der_m" in vals:
                            sides.append(to_float(vals["lateral_der_m"], 0))
                        if "posterior_m" in vals:
                            rears.append(to_float(vals["posterior_m"], 0))
                if fronts:
                    frontal_m = sum(fronts) / len(fronts)
                if sides:
                    lateral_avg = sum(sides) / len(sides)
                    lateral_izq_m = lateral_der_m = lateral_avg
                if rears:
                    posterior_m = sum(rears) / len(rears)

# ============================================================
# 6. DETERMINAR TIPO LATERAL BASADO EN TRATAMIENTO URBANÍSTICO
# ============================================================

tratamiento_info = pot_dict.get("urban_treatment", {}).get("tratamiento_urbanistico", {})
tratamiento_nombre = str(tratamiento_info.get("nombre", "")).strip().upper()
if "CONSOLIDACION" in tratamiento_nombre or "CONTINUA" in tratamiento_nombre:
    lateral_m = 0.0  # Tipología continua: retiros laterales y posteriores = 0.0m
elif "AISLADA" in tratamiento_nombre:
    lateral_m = (lateral_izq_m + lateral_der_m) / 2.0  # Promedio de laterales
else:
    lateral_m = (lateral_izq_m + lateral_der_m) / 2.0  # Por defecto o desconocido

# ============================================================
# 7. CONSTRUIR LA TABLA DE LADOS
# ============================================================

sides_table = []
for data in segment_data:
    i = data["idx"]
    is_front = i in front_indices
    is_posterior = (i == posterior_idx)

    road_type = "N/A"
    road_width = 0.0
    balcony_allowed = False
    balcony_max_depth = 0.0
    setback = 3.0  # valor por defecto

    if is_front:
        classification = "Frontal"
        street_idx = data["street_idx"]
        if street_idx >= 0 and street_idx < len(road_analysis):
            street_data = road_analysis[street_idx]
            road_width = to_float(street_data.get("road_width_m", 0))
        if road_width == 0:
            road_width = 15.0  # ancho por defecto
        road_type = get_road_class_by_width(road_width)

        # Reglas de balcón y retiro según ancho de vía (compatibilidad)
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

        # Sobrescribir el retiro con el valor del caché (frontal)
        setback = frontal_m

    elif is_posterior:
        classification = "Posterior"
        neighbor_height = 0.0
        setback = posterior_m
    else:
        classification = "Lateral"
        neighbor_height = 0.0
        setback = lateral_m  # promedio de laterales

    sides_table.append({
        "side_index": i,
        "classification": classification,
        "road_type": road_type,
        "road_width_m": round(road_width, 2),
        "setback_m": round(setback, 2),
        "balcony_allowed": balcony_allowed,
        "balcony_max_depth_m": round(balcony_max_depth, 2),
        "neighbor_height_m": 0.0,
        "separation_required_m": round(setback, 2),
        "is_access": is_front
    })

# ============================================================
# 8. CALCULAR SOLICITUD JSON: perímetro_edificable, altura_maxima_pisos, aislamientos_aplicados, área_neta_por_piso
# ============================================================

# 1. Altura máxima en pisos (desde POT)
height_limits = pot_dict.get("height_limits", {})
altura_efectiva_m = to_float(height_limits.get("altura_efectiva_m", 0))
FLOOR_HEIGHT_DEFAULT = 3.0
altura_maxima_pisos = int(altura_efectiva_m / FLOOR_HEIGHT_DEFAULT) if altura_efectiva_m > 0 else 0

# 2. Aislamientos aplicados (de cada lado)
try:
    sides_list = json.loads(json.dumps(sides_table))  # Convertir a lista de dicts
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
if rs and rg and lot_polygon:
    try:
        if lot_polygon.IsClosed:
            # Extraer todos los setbacks para cálculo conservador
            setbacks = [side["setback_m"] for side in sides_table]
            min_setback = min(setbacks) if setbacks else 0.0

            # Offset hacia adentro (negativo) para obtener el área/perímetro edificable
            offset_curves = lot_polygon.Offset(
                rg.Plane.WorldXY,
                -min_setback,
                0.1,
                rg.CurveOffsetCornerStyle.Sharp
            )

            if offset_curves:
                offset_curve = offset_curves[0]
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
            perimetro_edificable = lot_polygon.GetLength() if lot_polygon else 0.0
            area_total = rg.AreaMassProperties.Compute(lot_polygon).Area if lot_polygon else 0.0
            area_neta_por_piso = max(0, area_total - (perimetro_edificable * 3.0))
    except Exception as e:
        print(f"Error en cálculo de perímetro/área edificable: {e}")
        perimetro_edificable = lot_polygon.GetLength() if lot_polygon and rs else 0.0
        try:
            area_total = rg.AreaMassProperties.Compute(lot_polygon).Area if lot_polygon and rg else 0.0
        except:
            area_total = 0.0
        area_neta_por_piso = max(0, area_total - (perimetro_edificable * 3.0))
else:
    # Valores por defecto si no hay polígono válido o sin rs/rg
    perimetro_edificable = 0.0
    area_neta_por_piso = 0.0

# 4. Crear el JSON solicitado
result_json = {
    "perimetro_edificable": round(perimetro_edificable, 2),
    "altura_maxima_pisos": altura_maxima_pisos,
    "aislamientos_aplicados": aislamientos_aplicados,
    "area_neta_por_piso": round(area_neta_por_piso, 2)
}

# Convertir a string JSON para salida de Grasshopper
resultado_json_string = json.dumps(result_json, indent=2, ensure_ascii=False)

# ============================================================
# 9. SALIDAS
# ============================================================

# Cumplimiento de altura y pisos
pot_compliance = {
    "height_max_m": max_height_m,
    "height_max_floors": max_floors_pot,
    "bonus_floor_applied": bonus_floor > 0,
    "total_floors_effective": total_floors,
    "floor_height_m": fh,
    "front_side_indices": front_indices
}
pot_compliance_json = json.dumps(pot_compliance, indent=2, ensure_ascii=False)

# Resumen de reglas de balcones
balcony_rules_summary = {
    "front_has_balcony": any(s["balcony_allowed"] for s in sides_table if s["classification"] == "Frontal"),
    "front_balcony_depth": max([s["balcony_max_depth_m"] for s in sides_table if s["classification"] == "Frontal"] or [0]),
}
balcony_rules_summary_json = json.dumps(balcony_rules_summary, indent=2, ensure_ascii=False)

# Tabla de lados
sides_table_json = json.dumps(sides_table, indent=2, ensure_ascii=False)

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
}, indent=2, ensure_ascii=False)

# Salidas de depuración
print(f"\n=== LADOS CONFIGURADOS ===")
print(f"Lados procesados: {len(sides_table)}")
for side in sides_table:
    print(f"  Lado {side['side_index']}: {side['classification']} | Vía: {side['road_type']} ({side['road_width_m']}m) | Retiro: {side['setback_m']}m | Balcón: {side['balcony_allowed']} (max {side['balcony_max_depth_m']}m)")
print(f"Frentes: {front_indices}")
print(f"Posterior: {posterior_idx}")
print(f"Altura efectiva: {altura_efectiva_m}m → {altura_maxima_pisos} pisos")
print(f"Perímetro edificable: {perimetro_edificable:.2f}m")
print(f"Área neta por piso: {area_neta_por_piso:.2f}m2")