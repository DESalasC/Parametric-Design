#!/usr/bin/env python3
"""
CONTEXTO_v09 - Análisis Normativo POT Bogotá Consolidado
CORRECCIÓN: Desplazamiento virtual de la geometría local al sistema MAGNA-SIRGAS.
TRAZABILIDAD: Anotaciones normativas Decreto 555 de 2021 (POT Bogotá).
"""

import Rhino
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

# ------------------------------------------------------------
# MARCO NORMATIVO POT BOGOTÁ (Decreto 555 de 2021)
# ------------------------------------------------------------
CLASE_SUELO_MAP = {
    1: "Urbano Consolidado", 2: "Urbano En Consolidación", 3: "Expansión Urbana",
    4: "Rural", 5: "Protección Ecológica", 6: "Riesgo", 7: "Reserva",
}

TRATAMIENTO_PARAMS = {
    "TRADICIONAL": {"altura_max": 9, "ios_max": 0.5, "ibc_max": 3.0},
    "RENOVACION_URBANA": {"altura_max": 12, "ios_max": 0.6, "ibc_max": 4.5},
    "CENTRALIDAD": {"altura_max": 15, "ios_max": 0.7, "ibc_max": 6.0},
    "EJE_AMBIENTAL": {"altura_max": 6, "ios_max": 0.4, "ibc_max": 2.5},
    "PATRIMONIO": {"altura_max": 7, "ios_max": 0.4, "ibc_max": 2.0},
}

CLASIFICACION_VIAL_PARAMS = {
    "arterial_principal": {"retiro_frontal": 5.0, "retiro_lateral": 3.0, "retiro_posterior": 3.0, "ancho_tipico_min": 25, "ancho_tipico_max": 40, "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
    "arterial_complementaria": {"retiro_frontal": 4.0, "retiro_lateral": 3.0, "retiro_posterior": 3.0, "ancho_tipico_min": 20, "ancho_tipico_max": 30, "permite_balcon": True, "balcon_max": 1.2, "balcon_solo_superior": False},
    "colectora": {"retiro_frontal": 3.0, "retiro_lateral": 2.5, "retiro_posterior": 3.0, "ancho_tipico_min": 15, "ancho_tipico_max": 25, "permite_balcon": True, "balcon_max": 1.0, "balcon_solo_superior": True},
    "local": {"retiro_frontal": 3.0, "retiro_lateral": 2.0, "retiro_posterior": 2.5, "ancho_tipico_min": 8, "ancho_tipico_max": 15, "permite_balcon": True, "balcon_max": 0.8, "balcon_solo_superior": True},
    "peatonal": {"retiro_frontal": 2.0, "retiro_lateral": 1.5, "retiro_posterior": 2.0, "ancho_tipico_min": 4, "ancho_tipico_max": 10, "permite_balcon": False, "balcon_max": 0.0, "balcon_solo_superior": False},
}

RETIRO_INCREMENTO_POR_PISO = 0.5  # m/piso
ALTURA_BASE_RETIRO = 2  # pisos

# ============================================================
# HELPERS
# ============================================================

def load_geojson_features(layer_key):
    filename = KEY_LAYERS.get(layer_key)
    if not filename: return []
    path = os.path.join(GEOJSON_DIR, f"{filename}.geojson")
    if not os.path.exists(path): return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get("features", [])
    except: return []

def geojson_to_curves_with_props(features):
    curves = []
    for feat in features:
        geom = feat.get("geometry")
        if not geom: continue
        gtype = geom.get("type")
        coords = geom.get("coordinates")
        props = feat.get("properties", {})
        if gtype in ["Polygon", "MultiPolygon"]:
            polys = coords if gtype == "MultiPolygon" else [coords]
            for poly_coords in polys:
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
                if crv: curves.append((crv, props))
    return curves

def point_in_polygon(point, polygon):
    return rs.PointInPlanarClosedCurve(point, polygon) == 1

def curves_are_close(curve_a, curve_b, tolerance=5.0):
    crv_a = rs.coercecurve(curve_a)
    crv_b = rs.coercecurve(curve_b)
    if not crv_a or not crv_b: return False
    success, pt_a, pt_b = crv_a.ClosestPoints(crv_b)
    if success and pt_a and pt_b:
        return pt_a.DistanceTo(pt_b) <= tolerance
    return False

def get_setbacks_for_road_class(classification, floors):
    cls_lower = str(classification).lower()
    if "arterial" in cls_lower and "principal" in cls_lower: cls_key = "arterial_principal"
    elif "arterial" in cls_lower: cls_key = "arterial_complementaria"
    elif "colector" in cls_lower or "colectora" in cls_lower: cls_key = "colectora"
    elif "local" in cls_lower: cls_key = "local"
    elif "peatonal" in cls_lower: cls_key = "peatonal"
    else: cls_key = "local"

    params = CLASIFICACION_VIAL_PARAMS[cls_key]
    inc = max(0, (floors - ALTURA_BASE_RETIRO)) * RETIRO_INCREMENTO_POR_PISO
    return {
        "classification_used": cls_key, "original_classification": classification,
        "front": params["retiro_frontal"] + inc, "side": params["retiro_lateral"] + inc,
        "rear": params["retiro_posterior"] + inc, "source_norm": "Decreto 555/2021 Art. 2.2.6.2.3.3"
    }

# ============================================================
# MAIN EXECUTION
# ============================================================

pot_layers_dict = "{}"
soil_classification = None
urban_treatment = None
max_height = None
road_classification = "NINGUNA"
heritage_buffer = False
ecological_structure = False
hydric_system = False
protected_areas = False
risk_areas = False

try:
    if lot_polygon is None: raise ValueError("Falta lot_polygon")

    # Cargar capas
    layers_curves = {}
    for layer_key in KEY_LAYERS:
        features = load_geojson_features(layer_key)
        if features:
            layers_curves[layer_key] = geojson_to_curves_with_props(features)

    trace = []

    # --- DESPLAZAMIENTO VIRTUAL MAGNA-SIRGAS ---
    # lot_polygon y lot_centroid están cerca de 0,0,0 (ArchiCAD)
    # magna_eastings y magna_northings son las coordenadas reales en el mundo (ej: 1'000.000)
    
    check_point = None
    virtual_lot_polygon = lot_polygon # Por defecto es el mismo
    
    try:
        e = float(magna_eastings)
        n = float(magna_northings)
        if e > 10000 and n > 10000:
            # Crear punto MAGNA
            check_point = Rhino.Geometry.Point3d(e, n, 0)
            trace.append(f"Coordenada MAGNA recibida: E={e}, N={n}")
            
            # Calcular vector de desfase (MAGNA - Local)
            offset_x = e - lot_centroid.X
            offset_y = n - lot_centroid.Y
            offset_vec = Rhino.Geometry.Vector3d(offset_x, offset_y, 0)
            
            # Mover virtualmente el polígono del lote a coordenadas MAGNA
            virtual_lot_polygon = rs.CopyObject(lot_polygon, offset_vec)
            trace.append("Lote desplazado virtualmente para cálculos GIS.")
    except:
        pass

    # Si por algún motivo no llegaron coordenadas MAGNA, usar el centroide tal cual
    if check_point is None:
        check_point = lot_centroid
        virtual_lot_polygon = lot_polygon
        trace.append("Usando coordenadas locales (0,0,0) para GIS. Puede fallar si el POT está en MAGNA.")

    # 1. CLASIFICACIÓN DE SUELO (Usa el punto MAGNA)
    soil_data = {"classification": None, "code": None, "trace": ""}
    suelo_curves = layers_curves.get("ClasificacionSuelo", [])
    for crv, props in suelo_curves:
        if point_in_polygon(check_point, crv):
            clase_code = props.get("CLASE_SUELO") or props.get("clase_suelo")
            if clase_code is not None:
                soil_data["classification"] = CLASE_SUELO_MAP.get(int(clase_code), f"Código {clase_code}")
                soil_data["code"] = int(clase_code)
                trace.append(f"SOIL: {soil_data['classification']}")
            break

    # 2. TRATAMIENTO URBANÍSTICO (Usa el punto MAGNA)
    urban_data = {"treatment": None, "altura_max": None, "ios_max": None, "ibc_max": None, "trace": ""}
    trat_curves = layers_curves.get("TratamientoUrbanistico", [])
    for crv, props in trat_curves:
        if point_in_polygon(check_point, crv):
            treatment = props.get("CODIGO_SUBTRATAMIENTO") or props.get("TIPOLOGIA") or "DESCONOCIDO"
            urban_data["treatment"] = treatment
            tipo = str(treatment).upper()
            for k, v in TRATAMIENTO_PARAMS.items():
                if k in tipo:
                    urban_data["altura_max"] = v["altura_max"]
                    urban_data["ios_max"] = v["ios_max"]
                    urban_data["ibc_max"] = v["ibc_max"]
                    break
            trace.append(f"URBAN: {treatment} | Hmax={urban_data['altura_max']}m")
            break

    # 3. ANÁLISIS VIAL (Usa el lote desplazado virtualmente a MAGNA)
    vial_curves = layers_curves.get("Eje_vial", [])
    vial_frontales = []
    for crv, props in vial_curves:
        if curves_are_close(virtual_lot_polygon, crv, tolerance=5.0):
            cls = props.get("CLASIFICACION_VIAL") or props.get("TIPO_VIA") or "DESCONOCIDA"
            vial_frontales.append({"classification": cls})
            trace.append(f"Vía frontal detectada (vía virtual): {cls}")

    building_floors = 4
    vial_analysis = []
    for vial in vial_frontales:
        setbacks = get_setbacks_for_road_class(vial["classification"], building_floors)
        vial_analysis.append({"classification": vial["classification"], "setbacks": setbacks})

    road_classification_str = ", ".join(set(v["classification"] for v in vial_frontales)) if vial_frontales else "NINGUNA"

    # 4. RESTRICCIONES (Usa el lote desplazado virtualmente)
    restrictions = {}
    for key, (layer_name, desc) in {
        "heritage_buffer_100m": ("BienInteresCultural", "Buffer 100m BIC"),
        "ecological_structure": ("EstructuraEcologicaPrincipal", "Estructura Ecológica Principal"),
        "hydric_system": ("SistemaHidrico", "Sistema Hídrico (rondas)"),
        "protected_areas": ("AreasProtegidaSINAP", "Áreas Protegidas SINAP"),
        "risk_areas": ("SueloProteccionRiesgo", "Suelos Protección/Riesgo"),
    }.items():
        intersects = False
        for crv, props in layers_curves.get(layer_name, []):
            if curves_are_close(virtual_lot_polygon, crv, tolerance=0.1):
                intersects = True
                break
        restrictions[key] = {"intersects": intersects, "description": desc}

    # Limpiar geometría temporal del documento de Rhino (para no ensuciar el modelo)
    if virtual_lot_polygon != lot_polygon:
        rs.DeleteObject(virtual_lot_polygon)

    altura_efectiva = urban_data["altura_max"] or 12
    pot_conclusions = {
        "lot_info": {"centroid_magna": [check_point.X, check_point.Y, check_point.Z]},
        "soil": soil_data,
        "urban_treatment": urban_data,
        "height_limits": {"altura_efectiva_m": altura_efectiva},
        "road_analysis": vial_analysis,
        "road_classification_summary": road_classification_str,
        "restrictions": restrictions,
        "traceability": {"steps": trace}
    }

    pot_layers_dict = json.dumps(pot_conclusions)
    soil_classification = soil_data["classification"]
    urban_treatment = urban_data["treatment"]
    max_height = urban_data["altura_max"]
    road_classification = road_classification_str
    heritage_buffer = restrictions["heritage_buffer_100m"]["intersects"]
    ecological_structure = restrictions["ecological_structure"]["intersects"]
    hydric_system = restrictions["hydric_system"]["intersects"]
    protected_areas = restrictions["protected_areas"]["intersects"]
    risk_areas = restrictions["risk_areas"]["intersects"]

    print("=== CONTEXTO_v09 EJECUTADO OK ===")
    if soil_classification: print(f"Suelo: {soil_classification}")
    if road_classification != "NINGUNA": print(f"Calles: {road_classification}")

except Exception as e:
    print(f"ERROR FATAL CONTEXTO: {str(e)}")