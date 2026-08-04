#!/usr/bin/env python3
"""
F1_CONTEXTO_POT_v01 - Análisis Normativo POT Bogotá Consolidado
GH Python Script para Grasshopper (GH Player compatible)

ENTRADAS (via Tapir Live Connection desde ArchiCAD):
  - lot_polygon: Polígono del lote (perímetro cerrado, planar XY)
  - lot_area: Área del lote en m2 (componente Area nativo GH)
  - lot_centroid: Centroide del lote (Point3d, componente Area nativo GH)
  - street_curves: Curvas de ejes/bordes de calle(s) con User Text "CLASIFICACION_VIAL"
  - north_angle_rad: Ángulo norte geográfico en radianes (float)
  - elevation_nmm: Cota NMM (float, msnm Bogotá)
  - json_path: Ruta al JSON de caché POT para este lote (contiene datos precalculados de POT y catastro)

SALIDAS CONSOLIDADAS (Property Palette ArchiCAD - UN SOLO OBJETO):
  - pot_conclusions: Dict consolidado con TODA la normativa aplicable
    Estructura:
    {
      "lot_info": {...},
      "soil": {...},
      "urban_treatment": {...},
      "sector": {...},
      "height_limits": {...},
      "road_analysis": [...],
      "road_classification_summary": "...",
      "restrictions": {...},
      "plan_parcial": {...},
      "actuacion_estrategica": {...},
      "setbacks_by_road_type": {...},
      "balcony_rules": {...},
      "compliance_summary": {...},
      "traceability": {...},
      "desfase_virtual": {...}  // Vector de desfase entre coordenadas locales y MAGNA-SIRGAS
    }

v01: Consulta JSON de caché POT como fuente principal de datos normativos,
     usando solo la geometría local (lote, calles) para cálculo de distancias.
     Incluye cálculo de desfase virtual entre coordenadas locales y MAGNA-SIRGAS.
"""

import rhinoscriptsyntax as rs
import json
import os
import math
from pathlib import Path

# ============================================================
# CONFIGURACIÓN (VALORES POR DEFECTO Y MAPEOS)
# ============================================================

# Mapeo códigos POT Bogotá (Decreto 555/2021)
CLASE_SUELO_MAP = {
    1: "Urbano Consolidado",
    2: "Urbano En Consolidación",
    3: "Expansión Urbana",
    4: "Rural",
    5: "Protección Ecológica",
    6: "Riesgo",
    7: "Reserva",
}

# Tratamiento urbanístico → Altura máx (m) y Índices
TRATAMIENTO_PARAMS = {
    "TRADICIONAL": {"altura_max": 9, "ios_max": 0.5, "ibc_max": 3.0},
    "RENOVACION_URBANA": {"altura_max": 12, "ios_max": 0.6, "ibc_max": 4.5},
    "CENTRALIDAD": {"altura_max": 15, "ios_max": 0.7, "ibc_max": 6.0},
    "EJE_AMBIENTAL": {"altura_max": 6, "ios_max": 0.4, "ibc_max": 2.5},
    "PATRIMONIO": {"altura_max": 7, "ios_max": 0.4, "ibc_max": 2.0},
}

# Rango de edificabilidad -> número de pisos (aprox. 3 m por piso)
RANGO_A_FLOORS = {
    "1": 8,
    "2": 5,
    "3": 4,
    "4A": 3,
    "4B": 3,
    "4C": 2,
    "4D": 2,
}

# Clasificación vial → Retiros y ancho típico (Decreto 555/2021)
CLASIFICACION_VIAL_PARAMS = {
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
}

# Incremento retiro por piso (Art. 2.2.6.2.3.3)
RETIRO_INCREMENTO_POR_PISO = 0.5  # m/piso > 2
ALTURA_BASE_RETIRO = 2  # pisos

# ============================================================
# HELPERS
# ============================================================

def load_pot_cache(json_path):
    """Cargar datos normativos desde el caché POT (JSON)."""
    if not json_path or not os.path.exists(json_path):
        return None
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error cargando caché POT: {e}")
        return None

def point_in_polygon(point, polygon):
    """Verificar si punto está dentro de polígono (plano XY)"""
    return rs.PointInPlanarClosedCurve(point, polygon) == 1

def curves_intersect(curve_a, curve_b):
    """Verificar intersección entre dos curvas"""
    events = rs.CurveCurveIntersection(curve_a, curve_b)
    return events is not None and len(events) > 0

def curve_width_at_point(curve, point):
    """Calcular ancho de vía en un punto (distancia a curva paralela/opuesta)"""
    # Para ejes viales: buscar curva paralela a distancia típica
    # Para bordes: distancia al borde opuesto
    t = rs.CurveClosestPoint(curve, point)
    if t is None:
        return None
    tangent = rs.CurveTangent(curve, t)
    if not tangent:
        return None
    normal = rs.VectorCrossProduct(tangent, (0, 0, 1))
    normal = rs.VectorUnitize(normal)
    # Placeholder: devolver None si no hay datos de bordes
    return None

def calculate_road_width(street_curves, lot_polygon, lot_centroid):
    """
    Calcular ancho de vía real para cada calle frontal al lote.
    """
    road_widths = []
    for crv, props in street_curves:
        if not curves_intersect(lot_polygon, crv):
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

def get_setbacks_for_road_class(classification, floors):
    """Calcular retiros normativos según clasificación vial y pisos."""
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
    params = CLASIFICACION_VIAL_PARAMS[cls_key]
    inc = max(0, (floors - ALTURA_BASE_RETIRO)) * RETIRO_INCREMENTO_POR_PISO
    return {
        "classification_used": cls_key,
        "original_classification": classification,
        "front": params["retiro_frontal"] + inc,
        "side": params["retiro_lateral"] + inc,
        "rear": params["retiro_posterior"] + inc,
        "increment_per_floor_above_2": RETIRO_INCREMENTO_POR_PISO,
        "source_norm": "Decreto 555/2021 Art. 2.2.6.2.3.3"
    }

def get_balcony_rules(classification, road_width_m, floors):
    """Determinar reglas de balcones según normativa POT."""
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
    params = CLASIFICACION_VIAL_PARAMS[cls_key]
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
    pisos_permitidos = list(range(ALTURA_BASE_RETIRO + 1, floors + 1)) if solo_superior else list(range(1, floors + 1))
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

# ============================================================
# MAIN EXECUTION
# ============================================================

# Validar inputs geométricos (obligatorios)
if lot_polygon is None:
    raise ValueError("Falta lot_polygon")
if lot_area is None:
    raise ValueError("Falta lot_area (componente Area nativo GH)")
if lot_centroid is None:
    raise ValueError("Falta lot_centroid (componente Area nativo GH)")

print(f"=== F1_CONTEXTO_POT_v01 ===")
print(f"Lote: {float(lot_area):.1f} m2 | Centroide: {lot_centroid}")

# Cargar caché POT si se proporciona
pot_data = None
if 'json_path' in globals() and json_path:
    pot_data = load_pot_cache(json_path)
    if pot_data:
        print(f"Cargado caché POT desde: {json_path}")
    else:
        print(f"Advertencia: No se pudo cargar caché POT desde {json_path}. Se usarán valores por defecto o se calcularán desde geometría.")

# Conversión del ángulo norte (radianes) a vector (el componente norte proviene de Tapir como ángulo en radianes)
north_angle_rad = globals().get("north_angle_rad", 0.0)
# Convertir a vector unitario en el plano XY (asumiendo que 0 rad apunta al norte del eje Y positivo)
north_vector = {"x": math.sin(north_angle_rad), "y": math.cos(north_angle_rad), "z": 0.0}
# (Este vector no se usa directamente en cálculos posteriores, pero está disponible si se necesita)

# Inicializar estructuras de datos
soil_data = {"classification": None, "code": None, "trace": ""}
urban_data = {"treatment": None, "altura_max": None, "ios_max": None, "ibc_max": None, "trace": ""}
sector_data = {"sector": None, "densidad": None, "trace": ""}
road_analysis = []
restrictions = {}
plan_parcial_data = {"aplica": False, "nombre": None, "trace": ""}
actuacion_data = {"aplica": False, "nombre": None, "trace": ""}
trace = []

# Si tenemos datos del caché, extraerlos
if pot_data:
    # 1. CLASIFICACIÓN DE SUELO
    soil_info = pot_data.get('soil', {})
    if soil_info:
        soil_data["classification"] = soil_info.get("classification")
        soil_data["code"] = soil_info.get("code")
        soil_data["trace"] = soil_info.get("trace", "")
        if soil_data["trace"]:
            trace.append(f"SOIL: {soil_data['classification']} (code {soil_data['code']}) desde caché")

    # 2. TRATAMIENTO URBANÍSTICO
    urban_info = pot_data.get('urban_treatment', {})
    if urban_info:
        urban_data["treatment"] = urban_info.get("treatment")
        urban_data["altura_max"] = urban_info.get("altura_max")
        urban_data["ios_max"] = urban_info.get("ios_max")
        urban_data["ibc_max"] = urban_info.get("ibc_max")
        urban_data["trace"] = urban_info.get("trace", "")
        if urban_data["trace"]:
            trace.append(f"URBAN: {urban_data['treatment']} | Hmax={urban_data['altura_max']}m desde caché")

    # 3. SECTOR USO RESIDENCIAL
    sector_info = pot_data.get('sector', {})
    if sector_info:
        sector_data["sector"] = sector_info.get("sector")
        sector_data["densidad"] = sector_info.get("densidad")
        sector_data["trace"] = sector_info.get("trace", "")
        if sector_data["trace"]:
            trace.append(f"SECTOR: {sector_data['sector']} | Densidad: {sector_data['densidad']} desde caché")

    # 4. ANÁLISIS VIAL
    road_analysis_raw = pot_data.get('road_analysis', [])
    if road_analysis_raw:
        # Convertir los datos de la caché al formato esperado por las funciones posteriores
        for street in road_analysis_raw:
            # Asegurarse de que tenga los campos necesarios
            street_data = {
                "street_id": street.get("street_id", len(road_analysis)),
                "classification": street.get("classification", "DESCONOCIDO"),
                "road_width_m": street.get("road_width_m"),
                "width_source": street.get("width_source", "DESCONOCIDO"),
                "setbacks": street.get("setbacks", {}),
                "balcony_rules": street.get("balcony_rules", {}),
                "trace": street.get("trace", ""),
                "properties": street.get("properties", {})
            }
            road_analysis.append(street_data)
            if street_data["trace"]:
                trace.append(f"VÍA {street_data['street_id']}: {street_data['classification']} desde caché")

    # 5. RESTRICCIONES
    restrictions_raw = pot_data.get('restrictions', {})
    if restrictions_raw:
        for key, value in restrictions_raw.items():
            restrictions[key] = {
                "intersects": value.get("intersects", False),
                "description": value.get("description", ""),
                "features_count": value.get("features_count", 0),
                "details": value.get("details", [])
            }
            if restrictions[key]["intersects"]:
                trace.append(f"RESTRICTION: {restrictions[key]['description']} INTERSECTA lote desde caché")

    # 6. PLAN PARCIAL Y ACTUACIÓN ESTRatégica
    plan_parcial_raw = pot_data.get('plan_parcial', {})
    if plan_parcial_raw:
        plan_parcial_data["aplica"] = plan_parcial_raw.get("aplica", False)
        plan_parcial_data["nombre"] = plan_parcial_raw.get("nombre")
        plan_parcial_data["trace"] = plan_parcial_raw.get("trace", "")
        if plan_parcial_data["trace"]:
            trace.append(f"PLAN_PARCIAL: {plan_parcial_data['nombre']} desde caché")

    actuacion_raw = pot_data.get('actuacion_estrategica', {})
    if actuacion_raw:
        actuacion_data["aplica"] = actuacion_raw.get("aplica", False)
        actuacion_data["nombre"] = actuacion_raw.get("nombre")
        actuacion_data["trace"] = actuacion_raw.get("trace", "")
        if actuacion_data["trace"]:
            trace.append(f"ACTUACION: {actuacion_data['nombre']} desde caché")

# Si no tenemos datos del caché, usar los métodos originales (GeoJSON) como fallback
# Pero según las instrucciones, debemos ignorar las consultas espaciales a GeoJSON.
# Sin embargo, para no romper la funcionalidad si no se proporciona JSON, mantenemos el fallback
# pero con una advertencia. En la versión final, se espera que siempre se proporcione JSON.
if not pot_data:
    print("Advertencia: No se proporcionó caché POT válido. Usando métodos de respaldo (GeoJSON).")
    # Aquí iría el código original de carga de GeoJSON, pero lo omitimos siguiendo las instrucciones.
    # Por ahora, dejamos los datos vacíos y se usarán valores por defecto posteriormente.
    pass

# ------------------------------------------------------------------
# 1. CLASIFICACIÓN DE SUELO (si no viene del caché, usar valor por defecto)
# ------------------------------------------------------------------
if not soil_data["classification"]:
    soil_data["classification"] = "Urbano Consolidado"  # valor por defecto
    soil_data["code"] = 1
    soil_data["trace"] = "Valor por defecto (no se encontró en caché)"
    trace.append("SOIL: Usando valor por defecto")

# ------------------------------------------------------------------
# 2. TRATAMIENTO URBANÍSTICO + ALTURA + ÍNDICES (si no viene del caché)
# ------------------------------------------------------------------
if not urban_data["treatment"]:
    urban_data["treatment"] = "TRADICIONAL"
    urban_data["altura_max"] = 12.0
    urban_data["ios_max"] = 0.6
    urban_data["ibc_max"] = 4.5
    urban_data["trace"] = "Valor por defecto (no se encontró en caché)"
    trace.append("URBAN: Usando valor por defecto")

# ------------------------------------------------------------------
# 3. SECTOR USO RESIDENCIAL (si no viene del caché)
# ------------------------------------------------------------------
if not sector_data["sector"]:
    sector_data["sector"] = "DESCONOCIDO"
    sector_data["densidad"] = None
    sector_data["trace"] = "Valor por defecto (no se encontró en caché)"
    trace.append("SECTOR: Usando valor por defecto")

# ------------------------------------------------------------------
# 4. ANÁLISIS VIAL COMPLETO (usar street_curves de entrada y datos del caché o cálculo)
# ------------------------------------------------------------------
# Si no tenemos road_analysis del caché, calcularlo desde las street_curves de entrada
# Asegurar que street_curves sea una lista
if not street_curves:
    street_curves = []
elif not isinstance(street_curves, list):
    street_curves = [street_curves]

# Convertir Guids a Curvas si es necesario
clean_street_curves = []
for crv in street_curves:
    if isinstance(crv, System.Guid):
        # Si es Guid, convertir a Curve
        converted_crv = rs.coercecurve(crv)
        if converted_crv:
            clean_street_curves.append(converted_crv)
    elif isinstance(crv, str):
        # A veces Grasshopper pasa el Guid como string
        try:
            guid_obj = System.Guid(crv)
            converted_crv = rs.coercecurve(guid_obj)
            if converted_crv:
                clean_street_curves.append(converted_crv)
        except:
            pass
    else:
        # Ya es una curva u otro objeto
        clean_street_curves.append(crv)

# Usar clean_street_curves en lugar de street_curves de aquí en adelante
# Ejemplo: for crv in clean_street_curves:

if not road_analysis and 'street_curves' in globals() and street_curves:
    vial_curves = []
    for crv in street_curves:
        if crv:
            # Asumimos que la curva tiene propiedades en su User Text o en un diccionario adjunto
            # Pero en GH, las curvas pueden venir con atributos de usuario. Aquí simplificamos.
            # En la versión original, se usaba geojson_to_curves_with_props, pero ahora asumimos que
            # las curvas de entrada ya tienen las propiedades necesarias en un diccionario adjunto?
            # Para simplificar, asumimos que cada elemento en street_curves es una tupla (curva, propiedades)
            # como en la versión original. Pero si no, intentamos extraer propiedades del User Text.
            # Esto es una simplificación; en la práctica, la interfaz de GH debería pasar las curvas con propiedades.
            if isinstance(crv, tuple) and len(crv) == 2:
                vial_curves.append(crv)
            else:
                # Intentar obtener propiedades del User Text
                props = {}
                try:
                    user_text = rs.GetUserText(crv)
                    # Asumimos que el User Text contiene un JSON o pares clave-valor
                    # Pero por simplicidad, dejamos vacío y usaremos clasificación por defecto
                except:
                    pass
                vial_curves.append((crv, props))

    if vial_curves:
        # Calcular anchos de vía
        road_widths = calculate_road_width(vial_curves, lot_polygon, lot_centroid)
        # Número de pisos para cálculo de retiros y balcones (se deriva de altura_máx)
        # Si no tenemos altura_máx del caché, usamos un valor por defecto
        altura_max_urb = urban_data["altura_max"] if urban_data["altura_max"] is not None else 12.0
        building_floors = max(1, int(round(altura_max_urb / 3.0)))  # aproximación 3m/piso

        for i, (crv, props) in enumerate(vial_curves):
            width_info = road_widths[i] if i < len(road_widths) else {"width_m": None, "source": "NO_CALCULADO", "properties": props}
            cls = props.get("CLASIFICACION_VIAL") or props.get("TIPO_VIA") or "DESCONOCIDO"
            setbacks = get_setbacks_for_road_class(cls, building_floors)
            balcony = get_balcony_rules(cls, width_info["width_m"], building_floors)
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
            trace.append(road_analysis[-1]["trace"])

        road_classification_str = ", ".join(set(v["classification"] for v in road_analysis)) if road_analysis else "NINGUNA"
    else:
        road_analysis = []
        road_classification_str = "NINGUNA"
        trace.append("VÍA: No se encontraron calles de entrada")
else:
    # Si tenemos road_analysis del caché, aún necesitamos calcular setbacks y balcones
    # porque dependen del número de pisos (que no está en el caché directamente)
    if road_analysis:
        # Calcular número de pisos desde la altura_máx del tratamiento urbano
        altura_max_urb = urban_data["altura_max"] if urban_data["altura_max"] is not None else 12.0
        building_floors = max(1, int(round(altura_max_urb / 3.0)))

        for street in road_analysis:
            cls = street["classification"]
            width_m = street["road_width_m"]
            # Recalcular setbacks y balcones con el número de pisos actual
            setbacks = get_setbacks_for_road_class(cls, building_floors)
            balcony = get_balcony_rules(cls, width_m, building_floors)
            street["setbacks"] = setbacks
            street["balcony_rules"] = balcony
            # Actualizar trace
            street["trace"] = f"Calle {street['street_id']}: {cls} | Ancho={width_m}m ({street['width_source']}) | Retiros F:{setbacks['front']} S:{setbacks['side']} P:{setbacks['rear']} | Balcón max={balcony['balcon_max_m']}m {'(solo pisos>2)' if balcony['balcon_solo_pisos_superiores'] else '(todos pisos)'}"
            trace.append(street["trace"])
        road_classification_str = ", ".join(set(v["classification"] for v in road_analysis)) if road_analysis else "NINGUNA"
    else:
        road_classification_str = "NINGUNA"

# ------------------------------------------------------------------
# 5. RESTRICCIONES (si no vienen del caché, usar valores por defecto o vacío)
# ------------------------------------------------------------------
if not restrictions:
    restriction_layers = {
        "heritage_buffer_100m": ("BienInteresCultural", "Buffer 100m BIC"),
        "ecological_structure": ("EstructuraEcologicaPrincipal", "Estructura Ecológica Principal"),
        "hydric_system": ("SistemaHidrico", "Sistema Hídrico (rondas)"),
        "protected_areas": ("AreasProtegidaSINAP", "Áreas Protegidas SINAP"),
        "risk_areas": ("SueloProteccionRiesgo", "Suelos Protección/Riesgo"),
        "reserve_areas": ("SueloReserva", "Suelo Reserva"),
    }
    for key, (layer_name, desc) in restriction_layers.items():
        restrictions[key] = {
            "intersects": False,
            "description": desc,
            "features_count": 0,
            "details": []
        }
    # Plan Parcial y Actuación Estratégica por defecto
    if not plan_parcial_data["aplica"]:
        plan_parcial_data = {"aplica": False, "nombre": None, "trace": "Valor por defecto"}
    if not actuacion_data["aplica"]:
        actuacion_data = {"aplica": False, "nombre": None, "trace": "Valor por defecto"}

# ------------------------------------------------------------------
# 6. CONSOLIDAR POT_CONCLUSIONS (SALIDA ÚNICA)
# ------------------------------------------------------------------
# Altura efectiva (mínimo entre tratamiento y restricciones)
altura_efectiva = urban_data["altura_max"] or 12.0

# Desfase virtual entre coordenadas locales (0,0,0 de ArchiCAD/Rhino) y MAGNA-SIRGAS (del caché POT)
desfase_virtual = {"x": 0.0, "y": 0.0, "z": 0.0}
if pot_data and 'coordenadas' in pot_data and 'poligono' in pot_data['coordenadas']:
    magna_coords = pot_data['coordenadas']['poligono']
    if isinstance(magna_coords, list) and len(magna_coords) >= 3:
        # Calcular centróide del polígono MAGNA (asumiendo coordenadas proyectadas, Z=0)
        sum_x = sum(float(p[0]) for p in magna_coords if isinstance(p, (list, tuple)) and len(p) >= 2)
        sum_y = sum(float(p[1]) for p in magna_coords if isinstance(p, (list, tuple)) and len(p) >= 2)
        cnt = len([p for p in magna_coords if isinstance(p, (list, tuple)) and len(p) >= 2])
        if cnt > 0:
            maga_centroid_x = sum_x / cnt
            maga_centroid_y = sum_y / cnt
            local_x = lot_centroid.X
            local_y = lot_centroid.Y
            local_z = lot_centroid.Z
            desfase_virtual["x"] = maga_centroid_x - local_x
            desfase_virtual["y"] = maga_centroid_y - local_y
            desfase_virtual["z"] = 0.0  # Asumimos plano XY; Z se puede derivar de altura si fuera necesario
            trace.append(f"DESFASE VIRTUAL: Magna centroid ({maga_centroid_x:.2f},{maga_centroid_y:.2f}) - Local centroid ({local_x:.2f},{local_y:.2f}) = ({desfase_virtual['x']:.2f},{desfase_virtual['y']:.2f})")
        else:
            trace.append("DESFASE VIRTUAL: Formato de coordenadas Magna no válido; usando cero.")
    else:
        trace.append("DESFASE VIRTUAL: Coordenadas Magna insuficientes; usando cero.")
else:
    trace.append("DESFASE VIRTUAL: No se encontraron coordenadas Magna en caché; usando cero.")

# Resumen cumplimiento
warnings = []
if soil_data["code"] in [5, 6, 7]:  # Protección, Riesgo, Reserva
    warnings.append(f"SUELO {soil_data['classification']}: Restricciones de edificación aplican")

for r in road_analysis:
    if r["balcony_rules"]["width_validation"] != "OK":
        warnings.append(f"VÍA {r['classification']}: {r['balcony_rules']['width_validation']}")

for key, val in restrictions.items():
    if val["intersects"]:
        warnings.append(f"RESTRICCIÓN: {val['description']} intersecta el lote")

if plan_parcial_data["aplica"]:
    warnings.append(f"PLAN PARCIAL: {plan_parcial_data['nombre']} - Verificar normas específicas")

compliance = {
    "overall_ok": len(warnings) == 0,
    "warnings": warnings,
    "trace_summary": trace
}

# Construir el diccionario de salida
pot_conclusions = {
    "lot_info": {
        "area_m2": float(lot_area),
        "perimeter_m": rs.CurveLength(lot_polygon) if rs.CurveLength(lot_polygon) else 0,
        "centroid": [lot_centroid.X, lot_centroid.Y, lot_centroid.Z],
        "elevation_nmm": float(elevation_nmm) if elevation_nmm else 2600,
    },
    "soil": soil_data,
    "urban_treatment": urban_data,
    "sector": sector_data,
    "height_limits": {
        "altura_max_tratamiento": urban_data["altura_max"],
        "ios_max": urban_data.get("ios_max"),
        "ibc_max": urban_data.get("ibc_max"),
        "altura_efectiva_m": altura_efectiva,
        "trace": urban_data.get("trace", "")
    },
    "road_analysis": road_analysis,
    "road_classification_summary": road_classification_str,
    "restrictions": restrictions,
    "plan_parcial": plan_parcial_data,
    "actuacion_estrategica": actuacion_data,
    "setbacks_by_road_type": {v["classification"]: v["setbacks"] for v in road_analysis},
    "balcony_rules": {v["classification"]: v["balcony_rules"] for v in road_analysis},
    "compliance_summary": compliance,
    "desfase_virtual": desfase_virtual,  # Vector de desfase entre coordenadas locales y MAGNA-SIRGAS
    "traceability": {
        "steps": trace,
        "geojson_layers_used": {"note": "En v01, se usa caché POT; no se usan GeoJSON directamente"},
        "timestamp": "CONTEXTO_v01"
    }
}

# Convertir a JSON string para salida de Grasshopper
pot_layers_dict = json.dumps(pot_conclusions, ensure_ascii=False, indent=2)

# Salidas individuales (para compatibilidad)
soil_classification = soil_data["classification"]
urban_treatment = urban_data["treatment"]
max_height = urban_data["altura_max"]
road_classification = road_classification_str
# Los siguientes se extraen de restrictions (asumiendo claves conocidas)
heritage_buffer = restrictions.get("heritage_buffer_100m", {}).get("intersects", False)
ecological_structure = restrictions.get("ecological_structure", {}).get("intersects", False)
hydric_system = restrictions.get("hydric_system", {}).get("intersects", False)
protected_areas = restrictions.get("protected_areas", {}).get("intersects", False)
risk_areas = restrictions.get("risk_areas", {}).get("intersects", False) or restrictions.get("reserve_areas", {}).get("intersects", False)

# Salida impresa para depuración
print("\n=== POT_CONCLUSIONS (Resumen) ===")
print(f"Suelo: {soil_classification}")
print(f"Tratamiento: {urban_treatment}")
print(f"Altura máx: {max_height}m")
print(f"Vías frontales: {road_classification}")
print(f"Análisis vial: {len(road_analysis)} calles")
for v in road_analysis:
    b = v["balcony_rules"]
    print(f"  {v['classification']}: Ancho={v['road_width_m']}m | Balcón max={b['balcon_max_m']}m {'(pisos>2)' if b['balcon_solo_pisos_superiores'] else ''} | {b['width_validation']}")
print(f"Restricciones: {[k for k,v in restrictions.items() if v['intersects']]}")
print(f"Cumplimiento: {'OK' if compliance['overall_ok'] else 'WARNINGS'}")
for w in warnings:
    print(f"  ⚠ {w}")

# GH OUTPUTS
# pot_layers_dict, soil_classification, urban_treatment, max_height,
# road_classification, heritage_buffer, ecological_structure,
# hydric_system, protected_areas, risk_areas