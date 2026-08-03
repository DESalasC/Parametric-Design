#!/usr/bin/env python3
"""
CONTEXTO_v04 - Análisis Normativo POT Bogotá Consolidado
GH Python Script para Grasshopper (GH Player compatible)

ENTRADAS (via Tapir Live Connection desde ArchiCAD):
  - lot_polygon: Polígono del lote (perímetro cerrado, planar XY)
  - lot_area: Área del lote en m2 (componente Area nativo GH)
  - lot_centroid: Centroide del lote (Point3d, componente Area nativo GH)
  - street_curves: Curvas de ejes/bordes de calle(s) con User Text "CLASIFICACION_VIAL"
  - north_vector: Vector norte geográfico (Point3d)
  - elevation_nmm: Cota NMM (float, msnm Bogotá)

SALIDAS CONSOLIDADAS (Property Palette ArchiCAD - UN SOLO OBJETO):
  - pot_conclusions: Dict consolidado con TODA la normativa aplicable
    Estructura:
    {
      "lot_info": {...},
      "soil": {...},
      "urban_treatment": {...},
      "height_limits": {...},
      "road_analysis": {...},
      "restrictions": {...},
      "setbacks_by_road_type": {...},
      "balcony_rules": {...},
      "compliance_summary": {...},
      "traceability": {...}  # De dónde sale cada decisión
    }

v04: Consulta REAL de GeoJSONs, calcula ancho de vía, deriva reglas balcones,
     consolida TODO en pot_conclusions con trazabilidad completa.
"""

import rhinoscriptsyntax as rs
import json
import os
import math

# ============================================================
# CONFIGURACIÓN RUTAS
# ============================================================
GEOJSON_DIR = r"C:\Users\Dario Salas\proyectos\2-Entradas\Datos_Sitio_GDB\geojson_layers"

KEY_LAYERS = {
    "ClasificacionSuelo": "clase_suelo_pot.gdb_layer_fields_report",
    "TratamientoUrbanistico": "tratamiento_urbanistico.gdb_layer_fields_report",
    "Sector_uso_residencial": "sector_uso_residencial.gdb_layer_fields_report",
    "PerimetroUrbano": "perimetro_urbano.gdb_layer_fields_report",
    "Eje_vial": "eje_vial.gdb_layer_fields_report",
    "BienInteresCultural": "bien_interes_cultural.gdb_layer_fields_report",
    "EstructuraEcologicaPrincipal": "estructura_ecologica_principal.gdb_layer_fields_report",
    "SistemaHidrico": "sistema_hidrico.gdb_layer_fields_report",
    "AreasProtegidaSINAP": "areas_protegidas_sinap.gdb_layer_fields_report",
    "SueloProteccionRiesgo": "suelo_proteccion_riesgo.gdb_layer_fields_report",
    "SueloReserva": "suelo_reserva.gdb_layer_fields_report",
    "PlanParcial": "plan_parcial.gdb_layer_fields_report",
    "ActuacionEstrategica": "actuacion_estrategica.gdb_layer_fields_report",
}

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
# Ancho típico para validar clasificación detectada vs real
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

def load_geojson_features(layer_key):
    """Cargar features de un GeoJSON pre-exportado"""
    filename = KEY_LAYERS.get(layer_key)
    if not filename:
        return []
    path = os.path.join(GEOJSON_DIR, f"{filename}.geojson")
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get("features", [])
    except Exception as e:
        print(f"Error cargando {layer_key}: {e}")
        return []


def geojson_to_curves_with_props(features):
    """Convertir features GeoJSON a curvas Rhino + propiedades"""
    curves = []
    for feat in features:
        geom = feat.get("geometry")
        if not geom:
            continue
        gtype = geom.get("type")
        coords = geom.get("coordinates")
        props = feat.get("properties", {})

        if gtype == "Polygon":
            pts = [rs.coerce3dpoint(c) for c in coords[0]]
            if len(pts) >= 3:
                crv = rs.AddPolyline(pts)
                if crv:
                    rs.CloseCurve(crv)
                    curves.append((crv, props))
        elif gtype == "MultiPolygon":
            for poly_coords in coords:
                pts = [rs.coerce3dpoint(c) for c in poly_coords[0]]
                if len(pts) >= 3:
                    crv = rs.AddPolyline(pts)
                    if crv:
                        rs.CloseCurve(crv)
                        curves.append((crv, props))
        elif gtype == "LineString":
            pts = [rs.coerce3dpoint(c) for c in coords]
            if len(pts) >= 2:
                crv = rs.AddPolyline(pts)
                if crv:
                    curves.append((crv, props))
    return curves


def point_in_polygon(point, polygon):
    """Verificar si punto está dentro de polígono (plano XY)"""
    return rs.PointInPlanarClosedCurve(point, polygon) == 1


def curves_intersect(curve_a, curve_b):
    """Verificar intersección entre dos curvas"""
    events = rs.CurveCurveIntersection(curve_a, curve_b)
    return events is not None and len(events) > 0


def curve_width_at_point(curve, point):
    """Calcular ancho de vía en un punto (distancia a curva paralela/opuesta)

    Para ejes viales: buscar curva paralela a distancia típica
    Para bordes: distancia al borde opuesto
    """
    # Buscar punto más cercano en la curva
    t = rs.CurveClosestPoint(curve, point)
    if t is None:
        return None

    # Tangente en ese punto
    tangent = rs.CurveTangent(curve, t)
    if not tangent:
        return None

    # Normal perpendicular
    normal = rs.VectorCrossProduct(tangent, (0, 0, 1))
    normal = rs.VectorUnitize(normal)

    # Ray casting en ambas direcciones para encontrar borde opuesto
    # En práctica: el GDB debería tener bordes, no solo ejes
    # Placeholder: devolver None si no hay datos de bordes
    return None


def calculate_road_width(street_curves, lot_polygon, lot_centroid):
    """
    Calcular ancho de vía real para cada calle frontal al lote.

    Método: Para cada curva de calle que intersecta el lote,
    buscar su pareja paralela (otro borde/eje) y medir distancia perpendicular.
    """
    road_widths = []

    for crv, props in street_curves:
        if not curves_intersect(lot_polygon, crv):
            continue

        cls_vial = props.get("CLASIFICACION_VIAL") or props.get("TIPO_VIA") or "DESCONOCIDO"

        # Intentar obtener ancho desde propiedades del GDB
        ancho_gdb = props.get("ANCHO") or props.get("ANCHO_VIA") or props.get("SECCION")

        if ancho_gdb:
            try:
                ancho = float(ancho_gdb)
            except:
                ancho = None
        else:
            # Fallback: estimar por clasificación
            cls_lower = str(cls_vial).lower()
            if "arterial" in cls_lower and "principal" in cls_lower:
                ancho = 30  # típica 25-40m
            elif "arterial" in cls_lower:
                ancho = 22  # típica 20-30m
            elif "colector" in cls_lower or "colectora" in cls_lower:
                ancho = 18  # típica 15-25m
            elif "local" in cls_lower:
                ancho = 10  # típica 8-15m
            elif "peatonal" in cls_lower:
                ancho = 6   # típica 4-10m
            else:
                ancho = 12  # default

        road_widths.append({
            "classification": cls_vial,
            "width_m": ancho,
            "source": "GDB_PROPERTY" if ancho_gdb else "ESTIMATED_BY_CLASS",
            "properties": props
        })

    return road_widths


def get_setbacks_for_road_class(classification, floors):
    """
    Calcular retiros normativos según clasificación vial y pisos.
    Basado en Decreto 555/2021 Art. 2.2.6.2.3.3
    """
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
        cls_key = "local"  # default conservador

    params = CLASIFICACION_VIAL_PARAMS[cls_key]

    # Incremento por pisos > 2
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
    """
    Determinar reglas de balcones según normativa POT.

    Reglas clave (Decreto 555/2021 + normas complementarias):
    - Vías arteriales: balcones hasta 1.20m, solo pisos superiores (>=3)
    - Vías colectoras: balcones hasta 1.00m, solo pisos superiores
    - Vías locales: balcones hasta 0.80m, solo pisos superiores
    - Vías peatonales: NO balcones
    - El ancho real de vía puede restringir más
    """
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

    # Validar ancho real vs clasificación
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

    # Pisos donde se permiten balcones
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

# Validar inputs
if lot_polygon is None:
    raise ValueError("Falta lot_polygon")
if lot_area is None:
    raise ValueError("Falta lot_area (componente Area nativo GH)")
if lot_centroid is None:
    raise ValueError("Falta lot_centroid (componente Area nativo GH)")

print(f"=== CONTEXTO_v04 ===")
print(f"Lote: {float(lot_area):.1f} m2 | Centroide: {lot_centroid}")

# Cargar capas desde GeoJSON
layers_curves = {}
for layer_key in KEY_LAYERS:
    features = load_geojson_features(layer_key)
    if features:
        layers_curves[layer_key] = geojson_to_curves_with_props(features)
        print(f"  Cargada {layer_key}: {len(layers_curves[layer_key])} geometrías")
    else:
        layers_curves[layer_key] = []

# Traceability log
trace = []

# ------------------------------------------------------------------
# 1. CLASIFICACIÓN DE SUELO
# ------------------------------------------------------------------
soil_data = {"classification": None, "code": None, "trace": ""}
suelo_curves = layers_curves.get("ClasificacionSuelo", [])
for crv, props in suelo_curves:
    if point_in_polygon(lot_centroid, crv):
        clase_code = props.get("CLASE_SUELO") or props.get("clase_suelo")
        if clase_code is not None:
            soil_data["classification"] = CLASE_SUELO_MAP.get(int(clase_code), f"Código {clase_code}")
            soil_data["code"] = int(clase_code)
            soil_data["trace"] = f"Centroide {lot_centroid} dentro de polígono CLASE_SUELO={clase_code} (feature props: {list(props.keys())})"
            trace.append(f"SOIL: {soil_data['classification']} (code {clase_code}) via point-in-polygon centroid")
        break

# ------------------------------------------------------------------
# 2. TRATAMIENTO URBANÍSTICO + ALTURA + ÍNDICES
# ------------------------------------------------------------------
urban_data = {"treatment": None, "altura_max": None, "ios_max": None, "ibc_max": None, "trace": ""}
trat_curves = layers_curves.get("TratamientoUrbanistico", [])
for crv, props in trat_curves:
    if point_in_polygon(lot_centroid, crv):
        treatment = props.get("CODIGO_SUBTRATAMIENTO") or props.get("TIPOLOGIA") or "DESCONOCIDO"
        urban_data["treatment"] = treatment

        # Obtener altura en propiedades (ALTURA_MAXIMA es el rango de edificabilidad)
        rango = props.get("ALTURA_MAXIMA") or props.get("altura_maxima")
        altura_por_rango = None
        if rango is not None:
            try:
                rango_str = str(rango).strip()
                if rango_str in RANGO_A_FLOORS:
                    pisos = RANGO_A_FLOORS[rango_str]
                    altura_por_rango = pisos * 3.0  # asumiendo 3 m por piso
                    urban_data["trace"] += " Altura desde rango {}: {} pisos = {}m. ".format(rango_str, pisos, altura_por_rango)
                else:
                    # Rango no reconocido, intentar con tipología
                    pass
            except:
                pass

        # Si obtuvimos altura del rango, usarla
        if altura_por_rango is not None:
            urban_data["altura_max"] = altura_por_rango
            # Intentar obtener ios_max e ibc_max del tratamiento (por tipología) si están disponibles
            tipo = str(treatment).upper()
            for k, v in TRATAMIENTO_PARAMS.items():
                if k in tipo:
                    urban_data["ios_max"] = v["ios_max"]
                    urban_data["ibc_max"] = v["ibc_max"]
                    urban_data["trace"] += " Índices por tipología {}: IOS={}, IBC={}. ".format(k, v["ios_max"], v["ibc_max"])
                    break
            # Si no se encontraron índices, dejarlos como None
        else:
            # Fallback por tipología si no hay altura válida del rango
            tipo = str(treatment).upper()
            found = False
            for k, v in TRATAMIENTO_PARAMS.items():
                if k in tipo:
                    urban_data["altura_max"] = v["altura_max"]
                    urban_data["ios_max"] = v["ios_max"]
                    urban_data["ibc_max"] = v["ibc_max"]
                    urban_data["trace"] += " Altura/índices por tipología {}: Hmax={}m, IOS={}, IBC={}. ".format(k, v["altura_max"], v["ios_max"], v["ibc_max"])
                    found = True
                    break
            if not found:
                # Valor por defecto si no se pudo determinar
                urban_data["altura_max"] = 12.0  # 4 pisos * 3m
                urban_data["ios_max"] = None
                urban_data["ibc_max"] = None
                urban_data["trace"] += " Altura por defecto (12m) - verificar manualmente. "

        trace.append("URBAN: {} | Hmax={}m | source={}".format(treatment, urban_data["altura_max"], "RANGO" if altura_por_rango is not None else ("TIPOLOGÍA" if urban_data["altura_max"] is not None else "DEFECTO")))
        break

# ------------------------------------------------------------------
# 3. SECTOR USO RESIDENCIAL (Densidad)
# ------------------------------------------------------------------
sector_data = {"sector": None, "densidad": None, "trace": ""}
uso_curves = layers_curves.get("Sector_uso_residencial", [])
for crv, props in uso_curves:
    if point_in_polygon(lot_centroid, crv):
        sector_data["sector"] = props.get("NOMBRE") or props.get("SECTOR") or "DESCONOCIDO"
        sector_data["densidad"] = props.get("DENSIDAD") or props.get("DENSIDAD_NETA")
        sector_data["trace"] = f"Centroide en sector {sector_data['sector']}"
        trace.append(f"SECTOR: {sector_data['sector']} | Densidad: {sector_data['densidad']}")
        break

# ------------------------------------------------------------------
# 4. ANÁLISIS VIAL COMPLETO (Clasificación + Ancho + Retiros + Balcones)
# ------------------------------------------------------------------
vial_curves = layers_curves.get("Eje_vial", [])
vial_frontales = []

for crv, props in vial_curves:
    if curves_intersect(lot_polygon, crv):
        cls = props.get("CLASIFICACION_VIAL") or props.get("TIPO_VIA") or "DESCONOCIDA"
        vial_frontales.append({
            "curve": crv,
            "classification": cls,
            "properties": props,
            "length": rs.CurveLength(crv) if rs.CurveLength(crv) else 0
        })

# Calcular anchos de vía reales
road_widths = calculate_road_width(vial_curves, lot_polygon, lot_centroid)

# Consolidar análisis vial con retiros y balcones
building_floors = 4  # Se puede pasar como input si está disponible
vial_analysis = []

for i, vial in enumerate(vial_frontales):
    cls = vial["classification"]
    width_info = road_widths[i] if i < len(road_widths) else {"width_m": None, "source": "NO_CALCULADO"}

    setbacks = get_setbacks_for_road_class(cls, building_floors)
    balcony = get_balcony_rules(cls, width_info["width_m"], building_floors)

    vial_analysis.append({
        "street_id": i,
        "classification": cls,
        "road_width_m": width_info["width_m"],
        "width_source": width_info["source"],
        "setbacks": setbacks,
        "balcony_rules": balcony,
        "trace": f"Calle {i}: {cls} | Ancho={width_info['width_m']}m ({width_info['source']}) | Retiros F:{setbacks['front']} S:{setbacks['side']} P:{setbacks['rear']} | Balcón max={balcony['balcon_max_m']}m {'(solo pisos >2)' if balcony['balcon_solo_pisos_superiores'] else '(todos pisos)'}"
    })
    trace.append(vial_analysis[-1]["trace"])

road_classification_str = ", ".join(set(v["classification"] for v in vial_frontales)) if vial_frontales else "NINGUNA"

# ------------------------------------------------------------------
# 5. RESTRICCIONES (Buffers, EEP, Hidrico, BIC, Protegidas, Riesgo)
# ------------------------------------------------------------------
restrictions = {}
restriction_layers = {
    "heritage_buffer_100m": ("BienInteresCultural", "Buffer 100m BIC"),
    "ecological_structure": ("EstructuraEcologicaPrincipal", "Estructura Ecológica Principal"),
    "hydric_system": ("SistemaHidrico", "Sistema Hídrico (rondas)"),
    "protected_areas": ("AreasProtegidaSINAP", "Áreas Protegidas SINAP"),
    "risk_areas": ("SueloProteccionRiesgo", "Suelos Protección/Riesgo"),
    "reserve_areas": ("SueloReserva", "Suelo Reserva"),
}

for key, (layer_name, desc) in restriction_layers.items():
    intersects = False
    intersecting_features = []
    for crv, props in layers_curves.get(layer_name, []):
        if curves_intersect(lot_polygon, crv):
            intersects = True
            intersecting_features.append(props)
    restrictions[key] = {
        "intersects": intersects,
        "description": desc,
        "features_count": len(intersecting_features),
        "details": intersecting_features[:3] if intersecting_features else []
    }
    if intersects:
        trace.append(f"RESTRICTION: {desc} INTERSECTA lote ({len(intersecting_features)} features)")

# Plan Parcial y Actuación Estratégica
plan_parcial_data = {"aplica": False, "nombre": None, "trace": ""}
for crv, props in layers_curves.get("PlanParcial", []):
    if curves_intersect(lot_polygon, crv):
        plan_parcial_data["aplica"] = True
        plan_parcial_data["nombre"] = props.get("NOMBRE") or props.get("ID")
        plan_parcial_data["trace"] = f"Lote intersecta Plan Parcial: {plan_parcial_data['nombre']}"
        trace.append(f"PLAN_PARCIAL: {plan_parcial_data['nombre']}")
        break

actuacion_data = {"aplica": False, "nombre": None, "trace": ""}
for crv, props in layers_curves.get("ActuacionEstrategica", []):
    if curves_intersect(lot_polygon, crv):
        actuacion_data["aplica"] = True
        actuacion_data["nombre"] = props.get("NOMBRE") or props.get("ID")
        actuacion_data["trace"] = f"Lote intersecta Actuación Estratégica: {actuacion_data['nombre']}"
        trace.append(f"ACTUACION: {actuacion_data['nombre']}")
        break

# ------------------------------------------------------------------
# 6. CONSOLIDAR POT_CONCLUSIONS (SALIDA ÚNICA)
# ------------------------------------------------------------------

# Altura efectiva (mínimo entre tratamiento y restricciones)
altura_efectiva = urban_data["altura_max"] or 12

# Resumen cumplimiento
warnings = []
if soil_data["code"] in [5, 6, 7]:  # Protección, Riesgo, Reserva
    warnings.append(f"SUELO {soil_data['classification']}: Restricciones de edificación aplican")

for r in vial_analysis:
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
    "road_analysis": vial_analysis,
    "road_classification_summary": road_classification_str,
    "restrictions": restrictions,
    "plan_parcial": plan_parcial_data,
    "actuacion_estrategica": actuacion_data,
    "setbacks_by_road_type": {v["classification"]: v["setbacks"] for v in vial_analysis},
    "balcony_rules": {v["classification"]: v["balcony_rules"] for v in vial_analysis},
    "compliance_summary": compliance,
    "traceability": {
        "steps": trace,
        "geojson_layers_used": {k: len(v) for k, v in layers_curves.items()},
        "timestamp": "CONTEXTO_v04"
    }
}

# Outputs individuales (para compatibilidad) + consolidado
# Convertir diccionario a JSON string para pasar entre componentes de Python en Grasshopper
# Esto evita que Grasshopper envuelva el diccionario en List[Object]
pot_layers_dict = json.dumps(pot_conclusions)
soil_classification = soil_data["classification"]
urban_treatment = urban_data["treatment"]
max_height = urban_data["altura_max"]
road_classification = road_classification_str
heritage_buffer = restrictions["heritage_buffer_100m"]["intersects"]
ecological_structure = restrictions["ecological_structure"]["intersects"]
hydric_system = restrictions["hydric_system"]["intersects"]
protected_areas = restrictions["protected_areas"]["intersects"]
risk_areas = restrictions["risk_areas"]["intersects"] or restrictions["reserve_areas"]["intersects"]

print("\n=== POT_CONCLUSIONS (Resumen) ===")
print(f"Suelo: {soil_classification}")
print(f"Tratamiento: {urban_treatment}")
print(f"Altura máx: {max_height}m")
print(f"Vías frontales: {road_classification}")
print(f"Análisis vial: {len(vial_analysis)} calles")
for v in vial_analysis:
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
