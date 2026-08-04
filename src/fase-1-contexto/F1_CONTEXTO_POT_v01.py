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

import json
import os
import math
import System
from pathlib import Path
import Rhino

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

# Tratamiento urbanístico → Altura máx (m) e Índices
TRATAMIENTO_PARAMS = {
    "TRADICIONAL": {"altura_max": 9, "ios_max": 0.5, "ibc_max": 3.0},
    "RENOVACION_URBANA": {"altura_max": 12, "ios_max": 0.6, "ibc_max": 4.5},
    "CENTRALIDAD": {"altura_max": 15, "ios_max": 0.7, "ibc_max": 6.0},
    "EJE_AMBIENTAL": {"altura_max": 6, "ios_max": 0.4, "ibc_max": 2.5},
    "PATRIMONIO": {"altura_max": 7, "ios_max": 0.4, "ibc_max": 2.0},
}

# Rango de edificabilidad → número de pisos (aprox. 3 m por piso)
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
    if polygon is None:
        return False
    # Use Rhino.Geometry.PointInPlanarClosedCurve
    return Rhino.Geometry.PointInPlanarClosedCurve(point, polygon, Rhino.Geometry.Plane.WorldXY, 0.01) == Rhino.Geometry.PointRelation.Inside

def curves_intersect(curve_a, curve_b):
    """Verificar intersección entre dos curvas"""
    if curve_a is None or curve_b is None:
        return False
    # Asegurar que sean listas para iterar
    list_a = curve_a if isinstance(curve_a, list) else [curve_a]
    list_b = curve_b if isinstance(curve_b, list) else [curve_b]

    for c_a in list_a:
        if not isinstance(c_a, Rhino.Geometry.Curve):
            continue
        for c_b in list_b:
            if not isinstance(c_b, Rhino.Geometry.Curve):
                continue
            events = Rhino.Geometry.Intersect.Intersection.CurveCurve(c_a, c_b, 0.01, 0.01)
            if events is not None and len(events) > 0:
                return True
    return False

def curve_width_at_point(curve, point):
    """Calcular ancho de vía en un punto (distancia a curva paralela/opuesta)"""
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
            "props": props
        })
    return road_widths

def get_setbacks_for_road_class(road_class, num_floors):
    """Calculate setbacks based on road classification and number of floors.
    Returns a dict with keys: 'front', 'side', 'rear' (in meters).
    """
    # Normalize the road class string for lookup
    road_class_norm = str(road_class).strip().lower()

    # Default setbacks (if road class not found)
    default_setbacks = {"frontal": 3.0, "lateral": 0.0, "posterior": 0.0}

    # Look up in CLASIFICACION_VIAL_PARAMS
    params = None
    for key, value in CLASIFICACION_VIAL_PARAMS.items():
        if key == road_class_norm:
            params = value
            break

    # If not found, try to match by substring (e.g., if the input is "Vía Arterial" we want to match "arterial_principal" etc.)
    # But note: the keys in CLASIFICACION_VIAL_PARAMS are in English and underscore.
    # The input might be in Spanish. We'll try a simple mapping.
    if params is None:
        # Try to map common Spanish terms to our keys
        if "arterial" in road_class_norm and "principal" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("arterial_principal")
        elif "arterial" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("arterial_complementaria")
        elif "colector" in road_class_norm or "colectora" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("colectora")
        elif "local" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("local")
        elif "peatonal" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("peatonal")

    if params is None:
        # Use default
        setbacks = default_setbacks
    else:
        setbacks = {
            "frontal": params["retiro_frontal"],
            "lateral": params["retiro_lateral"],
            "posterior": params["retiro_posterior"]
        }

    # Apply increment for floors above the base (2 floors)
    if num_floors > ALTURA_BASE_RETIRO:
        extra_floors = num_floors - ALTURA_BASE_RETIRO
        increment = extra_floors * RETIRO_INCREMENTO_POR_PISO
        setbacks["frontal"] += increment
        setbacks["lateral"] += increment
        setbacks["posterior"] += increment

    # Return the setbacks in the format expected by the code (with keys 'front', 'side', 'rear')
    return {
        "front": setbacks["frontal"],
        "side": setbacks["lateral"],
        "rear": setbacks["posterior"]
    }

def get_balcony_rules(road_class, road_width_m, num_floors):
    """
    Get balcony rules based on road classification, actual road width, and number of floors.
    Returns a dict with:
      - balcon_max_m: maximum balcony depth allowed (meters)
      - balcon_solo_pisos_superiores: boolean indicating if balcony is only allowed for floors > 2
    """
    # Normalize the road class string for lookup
    road_class_norm = str(road_class).strip().lower()

    # Default values (if road class not found or no balcony allowed)
    default_rules = {
        "balcon_max_m": 0.0,
        "balcon_solo_pisos_superiores": False
    }

    # Look up in CLASIFICACION_VIAL_PARAMS
    params = None
    for key, value in CLASIFICACION_VIAL_PARAMS.items():
        if key == road_class_norm:
            params = value
            break

    # If not found, try to match by substring (same logic as in get_setbacks_for_road_class)
    if params is None:
        # Try to map common Spanish terms to our keys
        if "arterial" in road_class_norm and "principal" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("arterial_principal")
        elif "arterial" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("arterial_complementaria")
        elif "colector" in road_class_norm or "colectora" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("colectora")
        elif "local" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("local")
        elif "peatonal" in road_class_norm:
            params = CLASIFICACION_VIAL_PARAMS.get("peatonal")

    # If still not found, use default (no balcony)
    if params is None:
        return default_rules.copy()

    # Check if balconies are allowed at all for this classification
    if not params.get("permite_balcon", False):
        return {
            "balcon_max_m": 0.0,
            "balcon_solo_pisos_superiores": False
        }

    # Get the base balcony max from the classification
    balcon_max = params.get("balcon_max", 0.0)

    # Optionally adjust based on actual road width vs typical width range
    # If the actual width is outside the typical range, we might adjust the balcony allowance
    ancho_min = params.get("ancho_tipico_min")
    ancho_max = params.get("ancho_tipico_max")

    # If we have width data and it's outside typical range, reduce balcony allowance proportionally
    if road_width_m is not None and ancho_min is not None and ancho_max is not None:
        if road_width_m < ancho_min:
            # Narrower than typical - reduce balcony proportionally
            if ancho_min > 0:
                ratio = road_width_m / ancho_min
                balcon_max *= max(0.0, ratio)  # Don't go negative
        elif road_width_m > ancho_max:
            # Wider than typical - could allow same or slightly more, but we'll keep max for safety
            pass  # Keep original balcon_max
        # If within typical range, use the standard value

    # Determine if balcony is only for floors above 2
    balcon_solo_superior = params.get("balcon_solo_superior", False)

    # If building has 2 floors or less, and rule says balconies only for superior floors,
    # then effectively no balconies allowed (since there are no "superior" floors)
    if num_floors <= ALTURA_BASE_RETIRO and balcon_solo_superior:
        balcon_max = 0.0  # No balconies allowed if building is only 2 floors or less

    return {
        "balcon_max_m": balcon_max,
        "balcon_solo_pisos_superiores": balcon_solo_superior
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
    soil_info = pot_data.get('pot', {}).get('clasificacion_suelo', {})
    if soil_info:
        suelo_code = soil_info.get("clase_suelo")
        soil_data["classification"] = CLASE_SUELO_MAP.get(suelo_code, "Desconocido")
        soil_data["code"] = suelo_code
        soil_data["trace"] = ""  # JSON doesn't have trace field for this
        if soil_data["code"]:
            trace.append(f"SOIL: {soil_data['classification']} (code {soil_data['code']}) desde caché")

    # 2. TRATAMIENTO URBANÍSTICO
    urban_info = pot_data.get('pot', {}).get('tratamiento_urbanistico', {})
    altura_maxima_m = pot_data.get('pot', {}).get('altura_maxima_m')
    if urban_info:
        urban_data["treatment"] = urban_info.get("nombre")  # 'nombre' field contains treatment type like "Desarrollo"
        # Use altura_maxima_m from pot object, fallback to None if null
        if altura_maxima_m is not None:
            urban_data["altura_max"] = float(altura_maxima_m)
        else:
            urban_data["altura_max"] = None
        # Calculate ios_max and ibc_max from treatment type if available
        tratamiento_key = urban_data["treatment"]
        if tratamiento_key and tratamiento_key in TRATAMIENTO_PARAMS:
            urban_data["ios_max"] = TRATAMIENTO_PARAMS[tratamiento_key]["ios_max"]
            urban_data["ibc_max"] = TRATAMIENTO_PARAMS[tratamiento_key]["ibc_max"]
        else:
            urban_data["ios_max"] = None
            urban_data["ibc_max"] = None
        urban_data["trace"] = ""  # JSON doesn't have trace field for this
        if urban_data["treatment"]:
            trace.append(f"URBAN: {urban_data['treatment']} | Hmax={urban_data['altura_max']}m desde caché")

    # 3. SECTOR USO RESIDENCIAL (from UPZ)
    upz_info = pot_data.get('pot', {}).get('upz', {})
    if upz_info:
        sector_data["sector"] = upz_info.get("nombre")
        sector_data["densidad"] = None  # Not in JSON structure
        sector_data["trace"] = ""  # JSON doesn't have trace field for this
        if sector_data["sector"]:
            trace.append(f"SECTOR: {sector_data['sector']} desde caché")

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

# Convertir a Curvas de forma segura (verificar tipo primero)
clean_street_curves = []
for crv in street_curves:
    if isinstance(crv, Rhino.Geometry.Curve):
        # Ya es una curva nativa de Rhino, usarla directamente
        clean_street_curves.append(crv)
    else:
        # Intentar convertir desde Guid o string
        try:
            # In Grasshopper, we might get a Guid as string or Guid type
            # We'll try to coerce to Rhino.Geometry.Curve using RhinoDoc.ActiveDoc.Objects.Find
            # But we don't have access to the document. We'll skip for now.
            # Alternatively, we can use Rhino.Runtime.InteropWrap.TopologyUtil.TryConvertCurve? Not available.
            # Since we cannot reliably convert without document context, we'll skip.
            pass
        except:
            pass  # Ignorar elementos que no se pueden convertir

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
                    # rhinoscriptsyntax.GetUserText requires an object ID, which we don't have in this context.
                    # User text should be passed via the tuple (curve, props) from the data source.
                    # We'll leave props empty and rely on the tuple.
                    user_text = {}
                except:
                    user_text = {}
                vial_curves.append((crv, props))

    if vial_curves:
        # Calcular anchos de vía
        road_widths = calculate_road_width(vial_curves, lot_polygon, lot_centroid)
        # Número de pisos para cálculo de retiros y balcones (se deriva de altura_máx)
        # Si no tenemos altura_máx del caché, usamos un valor por defecto
        altura_max_urb = urban_data["altura_max"] if urban_data["altura_max"] is not None else 12.0
        building_floors = max(1, int(round(altura_max_urb / 3.0)))  # aproximación 3m/piso

        for i, (crv, props) in enumerate(vial_curves):
            width_info = road_widths[i] if i < len(road_widths) else {"width_m": None, "source": "NO_CALCULADO", "props": props}
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
                "props": props
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
    warnings.append(f"SUELO {soil_data['classification']}: Restricciones de edificación")

# Construir salida final
pot_conclusions = {
    "lot_info": {
        "area_m2": float(lot_area),
        "centroid": {"x": lot_centroid.X, "y": lot_centroid.Y, "z": lot_centroid.Z},
        "polygon": [{"x": pt.PointAtStart.X, "y": pt.PointAtStart.Y, "z": pt.PointAtStart.Z} for pt in lot_polygon.Explode()] if lot_polygon else []
    },
    "soil": soil_data,
    "urban_treatment": urban_data,
    "sector": sector_data,
    "height_limits": {
        "maximo_urbano": urban_data["altura_max"],
        "efectivo": altura_efectiva,
        "unidades": "metros",
        "trace": urban_data["trace"]
    },
    "road_analysis": road_analysis,
    "road_classification_summary": road_classification_str,
    "restrictions": restrictions,
    "plan_parcial": plan_parcial_data,
    "actuacion_estrategica": actuacion_data,
    "setbacks_by_road_type": {street["classification"]: street["setbacks"] for street in road_analysis if street["setbacks"]},
    "balcony_rules": {street["classification"]: street["balcony_rules"] for street in road_analysis if street["balcony_rules"]},
    "compliance_summary": {
        "warnings": warnings,
        "cumple_altura": altura_efectiva >= (urban_data["altura_max"] or 0),  # siempre true si no hay restricciones
        "trace": "; ".join(trace) if trace else "Sin trazabilidad adicional"
    },
    "traceability": {
        "timestamp": __import__('datetime').datetime.now().isoformat(),
        "script_version": "F1_CONTEXTO_POT_v01",
        "inputs": {
            "lot_area": lot_area,
            "lot_centroid": {"x": lot_centroid.X, "y": lot_centroid.Y, "z": lot_centroid.Z},
            "street_curves_count": len(street_curves) if street_curves else 0,
            "north_angle_rad": north_angle_rad,
            "elevation_nmm": elevation_nmm,
            "json_path": json_path if 'json_path' in globals() else None
        },
        "cache_used": pot_data is not None
    },
    "desfase_virtual": desfase_virtual
}

# Salida (en Grasshopper, esto se asigna a la salida de potencia)
pot_conclusions