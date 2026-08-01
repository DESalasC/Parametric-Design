#! /usr/bin/env python3
"""
VALIDADOR_CRUZADO_v01.py - Verificación de consistencia normativa (POT vs NSR-10)
GH Python Script para Grasshopper (GH Player compatible)

ENTRADAS:
  - pot_conclusions: JSON del análisis POT (de POT_CONTO_v04.py o LADOS_CONFIGURAR_v03.py)
  - vecino_analisis: JSON del análisis NSR-10 (de VECINOS_ANALISIS_v02.py - opcional, se simula si no existe)
  - lote_id: Identificador único del lote (opcional)

SALIDAS:
  - restricciones_territoriales_json: JSON estructurado con análisis POT, NSR-10 y conflictos detectados
  - resumen_validacion: Texto legible con resumen de validación cruzada
  - estado_validacion: "VALIDO", "ADVERTENCIA" o "ERROR" según severidad de conflictos
"""

import rhinoscriptsyntax as rs
import json
import math
from typing import Dict, Any, List, Tuple, Optional

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def safe_json_parse(data):
    """Parse JSON string or dict safely"""
    if not data:
        return {}
    if isinstance(data, str):
        try:
            return json.loads(data)
        except:
            return {}
    return data if isinstance(data, dict) else {}

def safe_float(value, default=0.0):
    """Convert to float safely"""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def safe_int(value, default=0):
    """Convert to int safely"""
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return default

def validate_setback_consistency(pot_setbacks: Dict[str, float],
                               nsr10_setbacks: Dict[str, float]) -> List[Dict]:
    """
    Valida consistencia entre退让距离 de POT y NSR-10
    Devuelve lista de conflictos encontrados
    """
    conflicts = []
    directions = ["norte", "sur", "este", "oeste"]

    for direction in directions:
        pot_val = pot_setbacks.get(direction, 0.0)
        nsr10_val = nsr10_setbacks.get(direction, 0.0)

        if pot_val > 0 and nsr10_val > 0:
            # Ambos existen, verificar que el más restrictivo se aplique
            min_required = max(pot_val, nsr10_val)  # El más restrictivo es el mayor valor
            if abs(pot_val - nsr10_val) > 0.1:  # Diferencia significativa
                conflicts.append({
                    "type": f"setback_conflict_{direction}",
                    "direction": direction,
                    "pot_value": pot_val,
                    "nsr10_value": nsr10_val,
                    "applied_value": min_required,
                    "severity": "warning",
                    "description": f"Conflicto de退让距离 en {direction}: POT={pot_val}m, NSR-10={nsr10_val}m. Se aplica el más restrictivo: {min_required}m",
                    "suggested_resolution": f"使用退让距离 {min_required}m para cumple con ambas normas"
                })

    return conflicts

def validate_height_consistency(pot_max_height: float,
                              nsr10_max_height: float,
                              num_floors: int,
                              floor_height: float = 3.0) -> List[Dict]:
    """
    Valida consistencia entre altura máxima de POT y NSR-10
    """
    conflicts = []

    # Altura máxima permitida por POT
    pot_height_limit = pot_max_height

    # Altura máxima permitida por NSR-10 (basada en zona sismica y tipo de suelo)
    nsr10_height_limit = nsr10_max_height

    # Altura actual propuesta
    proposed_height = num_floors * floor_height

    # Verificar contra POT
    if proposed_height > pot_height_limit + 0.1:  # Tolerancia de 10cm
        conflicts.append({
            "type": "height_exceeds_pot",
            "pot_limit": pot_height_limit,
            "nsr10_limit": nsr10_limit,
            "proposed_height": proposed_height,
            "severity": "error",
            "description": f"Altura propuesta ({proposed_height:.1f}m) excede límite POT ({pot_height_limit:.1f}m)",
            "suggested_resolution": f"Reducir a {pot_height_limit:.1f}m o {int(pot_height_limit/floor_height)} pisos"
        })

    # Verificar contra NSR-10
    if proposed_height > nsr10_height_limit + 0.1:
        conflicts.append({
            "type": "height_exceeds_nsr10",
            "pot_limit": pot_height_limit,
            "nsr10_limit": nsr10_limit,
            "proposed_height": proposed_height,
            "severity": "error",
            "description": f"Altura propuesta ({proposed_height:.1f}m) excede límite NSR-10 ({nsr10_height_limit:.1f}m)",
            "suggested_resolution": f"Reducir a {nsr10_height_limit:.1f}m o {int(nsr10_height_limit/floor_height)} pisos"
        })

    return conflicts

def determine_overall_status(conflicts: List[Dict]) -> str:
    """
    Determina el estado general basado en la severidad de los conflictos
    """
    if not conflicts:
        return "VALIDO"

    has_error = any(c.get("severity") == "error" for c in conflicts)
    has_warning = any(c.get("severity") == "warning" for c in conflicts)

    if has_error:
        return "ERROR"
    elif has_warning:
        return "ADVERTENCIA"
    else:
        return "VALIDO"

# ============================================================
# OBTENCIÓN SEGURA DE INPUTS
# ============================================================

# Inputs from Grasshopper/Tapir
pot_connections_input = globals().get("pot_conclusions", None)
vecino_analisis_input = globals().get("vecino_analisis", None)
lote_id_input = globals().get("lote_id", "LOTE_DESCONOCIDO")

# Parse inputs
pot_data = safe_json_parse(pot_connections_input)
vecino_data = safe_json_parse(vecino_analisis_input) if vecino_analisis_input else {}

# Validar entradas críticas
if not pot_data:
    raise ValueError("Falta pot_connections. Asegúrese de conectar la salida de POT_CONTEXTO_v04.py")

# ============================================================
# EXTRACCIÓN DE DATOS RELEVANTES
# ============================================================

# Extraer datos de POT
pot_lote_info = pot_data.get("lot_info", {})
pot_soil = pot_data.get("soil", {})
pot_urban = pot_data.get("urban_treatment", {})
pot_height_limits = pot_data.get("height_limits", {})
pot_road_analysis = pot_data.get("road_analysis", [])
pot_restrictions = pot_data.get("restrictions", {})
pot_setbacks_by_road = pot_data.get("setbacks_by_road_type", {})
pot_balcony_rules = pot_data.get("balcony_rules", {})

# Valores específicos de POT
pot_max_height = safe_float(pot_height_limits.get("altura_efectiva_m", pot_height_limits.get("altura_maxima", 0)))
pot_urban_treatment = pot_urban.get("tratamiento", pot_urban.get("zone", "NO_ESPECIFICADO"))
pot_soil_type = pot_soil.get("clase_suelo", pot_soil.get("tipo_suelo", "DESCONOCIDO"))

# Intentar obtener退让距离 desde diferentes posiciones posibles en la estructura POT
pot_setbacks = {}
if isinstance(pot_setbacks_by_road, dict):
    # Formato: {"Arterial_Principal": 5.0, "Colectora": 4.0, ...}
    # Necesitamos mapearlo a direcciones - simplificación: usar valores promedio o específicos si hay mapeo de dirección
    if "setbacks" in pot_data and isinstance(pot_data["setbacks"], dict):
        pot_setbacks = pot_data["setbacks"]
    else:
        # Estimación básica: si solo tenemos tipos de vía, asignar un valor promedio
        if pot_setbacks_by_road:
            avg_setback = sum(float(v) for v in pot_setbacks_by_road.values() if isinstance(v, (int, float))) / len([v for v in pot_setbacks_by_road.values() if isinstance(v, (int, float))])
            # Asignar el mismo valor a todas las direcciones como aproximación
            for direction in ["norte", "sur", "este", "oeste"]:
                pot_setbacks[direction] = avg_setback
        else:
            # Valor por defecto
            for direction in ["norte", "sur", "este", "oeste"]:
                pot_setbacks[direction] = 3.0  # Valor típico de退让距离
else:
    # Valor por defecto
    for direction in ["norte", "sur", "este", "oeste"]:
        pot_setbacks[direction] = 3.0

# Extraer datos de NSR-10 (si están disponibles) o simular
nsr10_data_available = bool(vecino_data and isinstance(vecino_data, dict) and len(vecino_data) > 0)

if nsr10_data_available:
    # Datos reales de NSR-10 (cuando VECINOS_ANALISIS_v02.py esté implementado)
    nsr10_separations = vecino_data.get("separations", {})
    nsr10_building_height = safe_float(vecino_data.get("building_height", 0))
    nsr10_seismic_zone = vecino_data.get("seismic_zone", "DESCONOCIDO")
    nsr10_soil_type = vecino_data.get("soil_type", "DESCONOCIDO")

    # Normalizar claves de direcciones a minúsculas
    nsr10_setbacks = {}
    for key, value in nsr10_separations.items():
        key_lower = str(key).lower()
        if key_lower in ["norte", "sur", "este", "oeste", "north", "south", "east", "west"]:
            # Mapear nombres en inglés a español si es necesario
            spanish_key = {
                "north": "norte",
                "south": "sur",
                "east": "este",
                "west": "oeste"
            }.get(key_lower, key_lower)
            nsr10_setbacks[spanish_key] = safe_float(value)
else:
    # Simular datos de NSR-10 cuando no estén disponibles (modo de desarrollo)
    # En una implementación real, estos vendrían de VECINOS_ANALISIS_v02.py
    nsr10_data_available = False

    # Valores típicos de NSR-10 para Bogotá (zona de amenaza media, suelo tipo normale)
    nsr10_seismic_zone = "ZONA_MEDIA"  # Valor típico para gran parte de Bogotá
    nsr10_soil_type = "SUELO_TYPE_A"   # Suelo firme/rocoso

    # Retiros típicos de NSR-10 (estos son ejemplos, deberían venir del análisis real)
    # NSR-10 suele tener requerimientos de separación basados en altura y uso
    altura_referencia = max(pot_max_height, 12.0)  # Usar altura de POT o 12m como referencia
    base_separation = 1.5  # Valor base de separación en metros

    # Ajuste simple basado en altura (en realidad NSR-10 es más complejo)
    height_factor = min(altura_referencia / 10.0, 3.0)  # Factor de ajuste por altura
    calculated_separation = base_separation + (height_factor * 0.5)

    # Aplicar a todas las direcciones (en una implementación real, variarían por orientación y Topografía)
    nsr10_setbacks = {
        "norte": calculated_separation,
        "sur": calculated_separation,
        "este": calculated_separation,
        "oeste": calculated_separation
    }

    # Altura máxima según NSR-10 (simplificado)
    # En realidad depende del tipo de suelo, zona sísmica, sistema estructural, etc.
    nsr10_building_height = min(18.0, altura_referencia * 1.2)  # Ejemplo conservativo

# ============================================================
# VALIDACIÓN CRUZADA
# ============================================================

# Validar退让距离
setback_conflicts = validate_setback_consistency(pot_setbacks, nsr10_setbacks)

# Validar altura
num_floors_pot = safe_int(pot_data.get("num_floors", pot_data.get("pisos", 0)))
if num_floors_pot == 0 and pot_max_height > 0:
    # Calcular número de pisos desde altura si no se proporciona directamente
    num_floors_pot = max(1, int(pot_max_height / 3.0))  # Asumiendo 3m por piso

height_conflicts = validate_height_consistency(
    pot_max_height=pot_max_height,
    nsr10_max_height=nsr10_building_height,
    num_floors=num_floors_pot,
    floor_height=3.0
)

# Combinar todos los conflictos
all_conflicts = setback_conflicts + height_conflicts

# Determinar estado general
estado_validacion = determine_overall_status(all_conflicts)

# ============================================================
# CONSTRUCCIÓN DE SALIDA
# ============================================================

# Construir el JSON de restricciones territoriales siguiendo el estándar
restricciones_territoriales = {
    "metadata": {
        "version": "1.0.0",
        "timestamp": rs.DateTime.Now().ToString("yyyy-MM-ddTHH:mm:ssZ"),
        "source_layer": "1",
        "validation_component": "VALIDADOR_CRUZADO_v01.py",
        "lote_id": str(lote_id_input),
        "nsr10_data_source": "REAL" if nsr10_data_available else "SIMULADO"
    },
    "data": {
        "lote_id": str(lote_id_input),
        "pot_analysis": {
            "soil_classification": pot_soil_type,
            "urban_treatment": pot_urban_treatment,
            "max_height": pot_max_height,
            "road_classification": pot_urban_treatment,  # Simplificación
            "setbacks": pot_setbacks,
            "num_floors": num_floors_pot,
            "floor_height_assumed": 3.0
        },
        "nsr10_analysis": {
            "separations": nsr10_setbacks,
            "building_height": nsr10_building_height,
            "seismic_zone": nsr10_seismic_zone,
            "soil_type": nsr10_soil_type,
            "data_source": "REAL" if nsr10_data_available else "SIMULADO"
        },
        "conflicts": all_conflicts
    },
    "validations": {
        "passed": estado_validacion == "VALIDO",
        "warnings": [c for c in all_conflicts if c.get("severity") == "warning"],
        "errors": [c for c in all_conflicts if c.get("severity") == "error"],
        "overall_status": estado_validacion
    }
}

# Convertir a string JSON para salida de Grasshopper
restricciones_territoriales_json = json.dumps(restricciones_territoriales, indent=2, ensure_ascii=False)

# Generar resumen legible
resumen_lineas = [
    f"=== VALIDACIÓN CRUZADA POT vs NSR-10 ===",
    f"Lote ID: {lote_id_input}",
    f"Estado de Validación: {estado_validacion}",
    f"Datos NSR-10: {'REALES (de VECINOS_ANALISIS_v02.py)' if nsr10_data_available else 'SIMULADOS (modo desarrollo)'}",
    f"",
    f"ANÁLISIS POT:",
    f"  - Suelo: {pot_soil_type}",
    f"  - Tratamiento Urbano: {pot_urban_treatment}",
    f"  - Altura Máxima: {pot_max_height:.1f}m",
    f"  - Número de Pisos: {num_floors_pot}",
    f"  - Retiros: {json.dumps({k: f'{v:.1f}m' for k, v in pot_setbacks.items()})}",
    f"",
    f"ANÁLISIS NSR-10:",
    f"  - Zona Sísmica: {nsr10_seismic_zone}",
    f"  - Tipo de Suelo: {nsr10_soil_type}",
    f"  - Altura Máxima Permitida: {nsr10_building_height:.1f}m",
    f"  - Retiros: {json.dumps({k: f'{v:.1f}m' for k, v in nsr10_setbacks.items()})}",
    f"",
    f"RESULTADO DE VALIDACIÓN:",
]

if not all_conflicts:
    resumen_lineas.append("  ✓ NO SE DETECTARON CONFLICTOS - Las normas POT y NSR-10 son consistentes")
else:
    resumen_lineas.append(f"  ⚠ SE DETECTARON {len(all_conflicts)} PROBLEMA(S):")
    for i, conflict in enumerate(all_conflicts, 1):
        severity_symbol = "✗" if conflict["severity"] == "error" else "⚠"
        resumen_lineas.append(f"    {i}. {severity_symbol} [{conflict['severity'].upper()}] {conflict['description']}")
        if "suggested_resolution" in conflict:
            resumen_lineas.append(f"      → Sugerencia: {conflict['suggested_resolution']}")

resumen_lineas.extend([
    f"",
    f"RECOMENDACIÓN FINAL:",
    f"  Estado: {estado_validacion}",
    f"  Acción requerida: {'Ninguna - diseño conforme a normativas' if estado_validacion == 'VALIDO' else 'Revisar y ajustar diseño según los conflictos identificados'}"
])

resumen_validacion = "\n".join(resumen_lineas)

# ============================================================
# SALIDAS
# ============================================================

# Salida principal: JSON con restricciones territoriales
restricciones_territoriales_output = restricciones_territoriales_json

# Salidas auxiliares
resumen_validacion_output = resumen_validacion
estado_validacion_output = estado_validacion

# Para depuración en Grasshopper
print(f"VALIDADOR_CRUZADO_v01.py completado - Estado: {estado_validacion}")
if all_conflicts:
    print(f"  Detectados {len(all_conflicts)} conflictos")
else:
    print("  No se detectaron conflictos")