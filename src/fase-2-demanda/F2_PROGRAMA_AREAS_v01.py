#!/usr/bin/env python3
"""
PROGRAMA_AREAS - Motor de Viabilidad Comercial y Programa de Áreas tipológicamente adaptativo
GH Python Script para Grasshopper (GH Player compatible)

ENTRADAS (via Grasshopper):
  - lot_polygon: Polígono del lote (perímetro cerrado, planar XY)
  - lot_area: Área del lote en m2 (componente Area nativo GH)
  - lot_centroid: Centroide del lote (Point3d, componente Area nativo GH)
  - street_curves: Curvas de ejes/bordes de calle(s) con User Text "CLASIFICACION_VIAL"
  - north_vector: Vector norte geográfico (Point3d)
  - elevation_nmm: Cota NMM (float, msnm Bogotá)
  - pot_conclusions: Diccionario consolidado de normativa POT (output de CONTEXTO_v04.py)
  - configurar_lados_result: JSON con outputs de CONFIGURAR_LADOS_v04.py (perimetro_edificable, altura_maxima_pisos, aislamientos_aplicados, area_neta_por_piso)
  - uso_principal_suelo: Uso principal del suelo según POT (residencial, comercio, salud, oficinas, mixto) - output de Fase 1

SALIDAS:
  - programa_disenoparametrico.json: Archivo JSON con el programa de áreas y análisis de viabilidad comercial
"""

import json
import math
import os

# Try to import Rhino-specific modules, provide fallbacks for testing
try:
    import rhinoscriptsyntax as rs
    RHINO_AVAILABLE = True
except ImportError:
    RHINO_AVAILABLE = False
    # Create mock functions for testing/non-Rhino environments
    class MockRs:
        @staticmethod
        def CurveLength(curve):
            return 0.0 if curve is None else getattr(curve, 'Length', 0.0)

        @staticmethod
        def PointInPlanarClosedCurve(point, polygon):
            return 1  # Mock: assume point is inside polygon

        @staticmethod
        def CurveCurveIntersection(curve_a, curve_b):
            return None  # Mock: no intersection

        @staticmethod
        def CurveClosestPoint(curve, point):
            return 0.0  # Mock: closest point at parameter 0

        @staticmethod
        def CurveTangent(curve, t):
            return (1.0, 0.0, 0.0)  # Mock: unit tangent in X direction

        @staticmethod
        def VectorCrossProduct(v1, v2):
            # Simple cross product mock
            return (-v1[2]*v2[1], v1[2]*v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0])

        @staticmethod
        def VectorUnitize(vector):
            length = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
            if length > 0:
                return (vector[0]/length, vector[1]/length, vector[2]/length)
            return vector

    rs = MockRs()

# ============================================================
# CONFIGURACIÓN ESTÁNDARES POR TIPOLOGÍA (basado en el skill building-programming y building-typology)
# ============================================================

# Ratios Net-to-Gross (NTG) por tipología
NTG_RATIOS = {
    "residencial": 0.78,      # Departamento típico (rango 0.75-0.82)
    "oficinas": 0.82,         # Oficina especulativa (rango 0.80-0.85)
    "comercio": 0.85,         # Retail (rango 0.80-0.88)
    "salud": 0.60,            # Hospital (rango 0.55-0.65)
    "mixto": 0.75             # Promedio ponderado para usos mixtos
}

# Estándares de área neta por unidad/tipo (m² NIA)
AREAS_POR_UNIDAD = {
    "residencial": {
        "estudio": 37,          # NDSS mínimo para 1 persona
        "1habitacion": 50,      # NDSS rango para 1-2 personas
        "2habitaciones": 70,    # NDSS rango para 3-4 personas
        "3habitaciones": 90     # NDSS rango para 4-5 personas
    },
    "oficinas": {
        "open_plan": 10,        # m² por persona (oficina abierta asignada)
        "private_office": 15,   # m² por persona (oficina privada)
        "meeting_room": 2.5,    # m² por persona (salas de reunión)
        "support": 0.15         # Ratio de apoyo (15% del área de trabajo)
    },
    "comercio": {
        "retail_small": 200,    # Tienda conveniencia
        "retail_medium": 1000,  # Supermercado pequeño
        "retail_large": 5000,   # Supermercado grande
        "storage": 0.20         # Ratio de bodega (20% del área de venta)
    },
    "salud": {
        "consulta": 16,         # m² por consulta (clínica)
        "hospitalizacion": 55,  # m² por cama (hospital general)
        "consulta_exterior": 25, # m² por consulta (consultorio exterior)
        "servicios": 0.30       # Ratio de servicios (30% del área clínica)
    }
}

# Distribución típica de unidades por piso para residencial
DISTRIBUCION_RESIDENCIAL = {
    "estudio": 0.40,           # 40% estudios
    "1habitacion": 0.30,       # 30% 1 habitación
    "2habitaciones": 0.20,     # 20% 2 habitaciones
    "3habitaciones": 0.10      # 10% 3 habitaciones
}

# Costos base de construcción (USD/m²) por tipo y calidad
COSTOS_BASE = {
    "residencial": {"economico": 800, "estandar": 1200, "lujo": 2000},
    "oficinas": {"economico": 900, "estandar": 1400, "lujo": 2500},
    "comercio": {"economico": 700, "estandar": 1100, "lujo": 1800},
    "salud": {"economico": 1000, "estandar": 1600, "lujo": 2500},
    "mixto": {"economico": 850, "estandar": 1300, "lujo": 2200}
}

# Factores regionales (ejemplo para Bogotá)
FACTOR_REGIONAL = {
    "bogota": 0.85,      # Factor de costo relativo a EE.UU. promedio
    "colombia": 0.80
}

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def safe_get(dictionary, keys, default=None):
    """Obtener valor de diccionario anidado de forma segura"""
    for key in keys:
        if isinstance(dictionary, dict) and key in dictionary:
            dictionary = dictionary[key]
        else:
            return default
    return dictionary

def parse_json_input(data):
    """Parsear entrada JSON de forma segura"""
    if not data:
        return {}
    if isinstance(data, str):
        try:
            return json.loads(data)
        except:
            return {}
    return data if isinstance(data, dict) else {}

def calculate_ntg_area(net_area, building_type):
    """
    Calcular área bruta a partir del área neta usando ratio NTG
    ntg_ratio = net_area / gross_area
    portanto: gross_area = net_area / ntg_ratio
    """
    ntg_ratio = NTG_RATIOS.get(building_type, 0.75)
    if ntg_ratio > 0:
        return net_area / ntg_ratio
    return 0

def calculate_program_distribution(net_area_per_floor, num_floors, primary_use, complementary_uses=None):
    """
    Calcular distribución del programa por piso basada en tipología

    Args:
        net_area_per_floor: Área neta disponible por piso (m2)
        num_floors: Número total de pisos
        primary_use: Uso principal ('residencial', 'oficinas', 'comercio', 'salud', 'mixto')
        complementary_uses: Lista de usos complementarios permitidos

    Returns:
        dict: Distribución de usos por piso y mix de espacios
    """
    if complementary_uses is None:
        complementary_uses = []

    # Determinar usos efectivos por piso
    effective_uses = [primary_use] + [u for u in complementary_uses if u != primary_use]
    if not effective_uses:
        effective_uses = [primary_use]

    # Para usos mixtos, distribuir por piso
    if len(effective_uses) > 1 and primary_use != "mixto":
        # Estrategia: usos comerciales/comunitarios en planta baja, residencial arriba
        ground_floor_uses = [u for u in effective_uses if u in ['comercio', 'residencial'] and u != 'residencial']
        upper_floor_uses = [u for u in effective_uses if u == 'residencial'] or [primary_use]

        # Si hay usos comerciales, los ponemos en planta baja
        if ground_floor_uses:
            ground_use = ground_floor_uses[0]  # Toma el primero compatible
            upper_use = 'residencial' if 'residencial' in effective_uses else primary_use
        else:
            ground_use = primary_use
            upper_use = primary_use
    else:
        ground_use = primary_use
        upper_use = primary_use

    # Calcular distribución por tipo
    distribution = {}

    if primary_use == "residencial":
        # Distribuir área residencial entre tipos de unidades
        total_area = net_area_per_floor
        for unit_type, percentage in DISTRIBUCION_RESIDENCIAL.items():
            unit_area = AREAS_POR_UNIDAD["residencial"][unit_type]
            units_per_floor = (total_area * percentage) / unit_area
            distribution[unit_type] = {
                "area_por_unidad_m2": unit_area,
                "porcentaje_distribucion": percentage * 100,
                "unidades_por_piso": round(units_per_floor, 1),
                "area_total_por_piso_m2": round(total_area * percentage, 2)
            }

    elif primary_use == "oficinas":
        # Distribución típica de oficina
        trabajo_area = net_area_per_floor * 0.70  # 70% para trabajo
        reunion_area = net_area_per_floor * 0.15  # 15% para reuniones
        soporte_area = net_area_per_floor * 0.15  # 15% para soporte

        distribution = {
            "trabajo": {
                "area_por_puesto_m2": AREAS_POR_UNIDAD["oficinas"]["open_plan"],
                "area_total_por_piso_m2": round(trabajo_area, 2),
                "puestos_estimados": round(trabajo_area / AREAS_POR_UNIDAD["oficinas"]["open_plan"])
            },
            "reuniones": {
                "area_por_puesto_m2": AREAS_POR_UNIDAD["oficinas"]["meeting_room"],
                "area_total_por_piso_m2": round(reunion_area, 2),
                "puestos_estimados": round(reunion_area / AREAS_POR_UNIDAD["oficinas"]["meeting_room"])
            },
            "soporte": {
                "ratio_sobre_trabajo": AREAS_POR_UNIDAD["oficinas"]["support"] * 100,
                "area_total_por_piso_m2": round(soporte_area, 2)
            }
        }

    elif primary_use == "comercio":
        # Distribución típica de retail
        venta_area = net_area_per_floor * 0.80   # 80% para venta
        bodega_area = net_area_per_floor * 0.20  # 20% para bodega

        distribution = {
            "venta": {
                "area_total_por_piso_m2": round(venta_area, 2),
                "tipo_typico": "retail_medium" if venta_area < 1000 else "retail_large"
            },
            "bodega": {
                "ratio_sobre_venta": AREAS_POR_UNIDAD["comercio"]["storage"] * 100,
                "area_total_por_piso_m2": round(bodega_area, 2)
            }
        }

    elif primary_use == "salud":
        # Distribución típica de salud clínica
        consulta_area = net_area_per_floor * 0.60  # 60% para consultas
        servicios_area = net_area_per_floor * 0.40 # 40% para servicios

        distribution = {
            "consulta": {
                "area_por_consulta_m2": AREAS_POR_UNIDAD["salud"]["consulta"],
                "area_total_por_piso_m2": round(consulta_area, 2),
                "consultas_por_piso": round(consulta_area / AREAS_POR_UNIDAD["salud"]["consulta"])
            },
            "servicios": {
                "ratio_sobre_consulta": AREAS_POR_UNIDAD["salud"]["servicios"] * 100,
                "area_total_por_piso_m2": round(servicios_area, 2)
            }
        }

    else:  # mixto o default
        # Distribución genérica
        distribution = {
            "area_general": {
                "area_total_por_piso_m2": round(net_area_per_floor, 2),
                "uso_asignado": primary_use
            }
        }

    return {
        "uso_principal": primary_use,
        "uso_plant_baja": ground_use,
        "uso_pisos_superiores": upper_use if upper_use != ground_use else ground_use,
        "distribucion_por_tipo": distribution,
        "area_neta_por_piso_m2": net_area_per_floor,
        "area_bruta_por_piso_m2": round(calculate_ntg_area(net_area_per_floor, primary_use), 2)
    }

def validate_normative_incentives(pot_conclusions, configurar_lados_result, uso_principal_suelo):
    """
    Validar incentivos normativos según POT

    Returns:
        dict: Información sobre estrategia normativa aplicada
    """
    estrategia = {
        "bonus_floor_aplicado": False,
        "razon_bonus": "",
        "usos_complementarios_permitidos": [],
        "estrategia_aplicada": "",
        "detalles": {}
    }

    # Extraer información relevante
    altura_maxima_pisos = configurar_lados_result.get("altura_maxima_pisos", 0)
    bonus_input = configurar_lados_result.get("bonus_floor_aplicado", False)
    total_floors_effective = configurar_lados_result.get("total_floors_effective", altura_maxima_pisos)

    # Verificar si se aplicó bonus floor
    if total_floors_effective > altura_maxima_pisos:
        estrategia["bonus_floor_aplicado"] = True
        estrategia["bonus_floors_adicionales"] = total_floors_effective - altura_maxima_pisos

        # Determinar razón del bonus
        if uso_principal_suelo == "residencial":
            estrategia["razon_bonus"] = "Piso adicional activado por uso comunal en nivel 1 (POT Art 2.2.6.2.3.5)"
            estrategia["estrategia_aplicada"] = "Planta baja: uso comunal/comercial, Pisos superiores: residencial"
        else:
            estrategia["razon_bonus"] = "Piso adicional aplicado según incentivos de renovación urbana"
            estrategia["estrategia_aplicada"] = "Distribución mezclada según usos permitidos"

    # Determinar usos complementarios permitidos
    usos_complementarios = []

    # Analizar uso principal para determinar compatibles
    compatibilidades = {
        "residencial": ["comercio", "comunidad"],  # Puede tener locales comerciales en PB
        "comercio": ["residencial", "oficinas"],   # Mixed-use típico
        "oficinas": ["comercio", "residencial"],   # Puede tener retail en plazas bajas
        "salud": ["comercio"],                     # Farmacias, tiendas de conveniencia
        "mixto": ["residencial", "comercio", "oficinas"]  # Ya es mixto
    }

    usos_complementarios = compatibilidades.get(uso_principal_suelo, [])

    # Verificar restricciones que podrían limitar usos complementarios
    restrictions = pot_conclusions.get("restrictions", {})
    tiene_restricciones = any(restrictions.get(key, {}).get("intersects", False)
                              for key in ["heritage_buffer_100m", "ecological_structure",
                                        "protected_areas", "risk_areas"])

    if tiene_restricciones:
        # En áreas restringidas, ser más conservador con usos complementarios
        usos_complementarios = [u for u in usos_complementarios if u in ["comercio"]]
        estrategia["nota_restricciones"] = "Se aplicaron limitaciones debido a restricciones territoriales"

    estrategia["usos_complementarios_permitidos"] = usos_complementarios

    # Determinar estrategia final
    if estrategia["bonus_floor_aplicado"] and uso_principal_suelo == "residencial" and "comercio" in usos_complementarios:
        strategy_desc = "Piso adicional activado: Planta baja para uso comercial, {} pisos superiores para residencial".format(
            int(altura_maxima_pisos))
    elif estrategia["bonus_floor_aplicado"]:
        strategy_desc = "Piso adicional aplicado según incentivos de uso del suelo"
    elif usos_complementarios:
        strategy_desc = "Usos mixtos permitidos en misma estratosfía: {}".format(", ".join(usos_complementarios))
    else:
        strategy_desc = "Uso único conforme a zonificación: {}".format(uso_principal_suelo)

    estrategia["estrategia_aplicada"] = strategy_desc
    estrategia["detalles"] = {
        "altura_maxima_pot": altura_maxima_pisos,
        "pisos_totales_efectivos": total_floors_effective,
        "uso_principal_suelo": uso_principal_suelo,
        "restricciones_detectadas": tiene_restricciones
    }

    return estrategia

def calculate_construction_cost(area_bruta_total_m2, building_types_distribution, calidad="estandar", region="bogota"):
    """
    Calcular estimado de costos de construcción

    Args:
        area_bruta_total_m2: Área bruta total construida (m2)
        building_types_distribution: Distribución por tipo de uso
        calidad: Nivel de acabado ('economico', 'estandar', 'lujo')
        region: Región para factor de costo

    Returns:
        dict: Estimado de costos desglosado
    """
    factor_region = FACTOR_REGIONAL.get(region, FACTOR_REGIONAL["bogota"])

    # Calculo ponderado del costo base si hay múltiples usos
    if isinstance(building_types_distribution, dict) and "uso_principal" in building_types_distribution:
        # Uso único o predominante
        primary_use = building_types_distribution["uso_principal"]
        costo_base = COSTOS_BASE.get(primary_use, COSTOS_BASE["mixto"]).get(calidad, COSTOS_BASE["mixto"]["estandar"])
    else:
        # Distribución múltiple - promedio ponderado
        costo_base = COSTOS_BASE["mixto"][calidad]

    costo_ajustado = costo_base * factor_region
    costo_total = area_bruta_total_m2 * costo_ajustado

    # Costos adicionales típicos (porcentaje del costo directo)
    honorarios_pct = 12.0      # Honorarios profesionales
    contingencia_pct = 10.0    # Contingencia técnica

    honorarios = costo_total * (honorarios_pct / 100)
    contingencia = costo_total * (contingencia_pct / 100)
    costo_total_con_gastos = costo_total + honorarios + contingencia

    return {
        "costo_base_usd_m2": round(costo_base, 2),
        "factor_regional": factor_region,
        "costo_ajustado_usd_m2": round(costo_ajustado, 2),
        "area_bruta_total_m2": round(area_bruta_total_m2, 2),
        "costo_directo_usd": round(costo_total, 2),
        "honorarios_profesionales_pct": honorarios_pct,
        "honorarios_profesionales_usd": round(honorarios, 2),
        "contingencia_pct": contingencia_pct,
        "contingencia_usd": round(contingencia, 2),
        "costo_total_estimado_usd": round(costo_total_con_gastos, 2),
        "desglose_por_tipo": building_types_distribution if isinstance(building_types_distribution, dict) else {"uso_predominante": building_types_distribution}
    }

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():
    """
    Función principal que procesa las entradas y genera el programa de áreas
    """

    if not RHINO_AVAILABLE:
        print("ADVERTENCIA: Rhino/Grasshopper no disponible. Ejecutando en modo de prueba.")

    print("=== PROGRAMA_AREAS - Motor de Viabilidad Comercial ===")

    # Parsear entradas JSON si es necesario
    pot_dict = parse_json_input(pot_conclusions)
    config_result = parse_json_input(configurar_lados_result)

    print(f"Procesando lote: {float(lot_area):.1f} m2")
    print(f"Uso principal del suelo: {uso_principal_suelo}")

    # Extraer datos de CONFIGURAR_LADOS
    area_neta_por_piso = config_result.get("area_neta_por_piso", 0)
    altura_maxima_pisos = config_result.get("altura_maxima_pisos", 0)
    perimetro_edificable = config_result.get("perimetro_edificable", 0)

    print(f"Área neta por piso: {area_neta_por_piso:.2f} m2")
    print(f"Altura máxima (pisos): {altura_maxima_pisos}")
    print(f"Perímetro edificable: {perimetro_edificable:.2f} m")

    # Validar incentivos normativos
    estrategia_normativa = validate_normative_incentives(pot_dict, config_result, uso_principal_suelo)
    print(f"Estrategia normativa: {estrategia_normativa['estrategia_aplicada']}")

    # Determinar número efectivo de pisos
    numero_pisos = config_result.get("total_floors_effective", altura_maxima_pisos)
    if numero_pisos <= 0:
        numero_pisos = altura_maxima_pisos  # fallback

    print(f"Número total de pisos a desarrollar: {numero_pisos}")

    # Calcular distribución del programa por piso
    distribucion_piso = calculate_program_distribution(
        area_neta_por_piso,
        numero_pisos,
        uso_principal_suelo
    )

    print(f"Distribución calculada para uso: {distribucion_piso['uso_principal']}")

    # Calcular áreas totales
    area_neta_total = area_neta_por_piso * numero_pisos
    area_bruta_por_piso = distribucion_piso.get('area_bruta_por_piso_m2',
                                                calculate_ntg_area(area_neta_por_piso, uso_principal_suelo))
    area_bruta_total = area_bruta_por_piso * numero_pisos

    print(f"Área neta total: {area_neta_total:.2f} m2")
    print(f"Área bruta por piso: {area_bruta_por_piso:.2f} m2")
    print(f"Área bruta total: {area_bruta_total:.2f} m2")

    # Calcular estimado de costos
    estimacion_costos = calculate_construction_cost(
        area_bruta_total,
        distribucion_piso,
        calidad="estandar",  # Puede parametrizarse
        region="bogota"
    )

    print(f"Costo estimado de construcción: ${estimacion_costos['costo_total_estimado_usd']:,.2f} USD")

    # Preparar información de usos por piso
    usos_por_piso = {}

    # Para cada piso, definir qué usos tiene
    for i in range(int(numero_pisos)):
        piso_num = i + 1
        if piso_num == 1 and estrategia_normativa["bonus_floor_aplicado"] and uso_principal_suelo == "residencial":
            # Planta baja especial para usos comerciales/comunitarios
            uso_piso = distribucion_piso.get('uso_plant_baja', uso_principal_suelo)
            usos_por_piso[f"Piso {piso_num}"] = uso_piso
        elif piso_num == 1:
            # Primera planta normal
            usos_por_piso[f"Piso {piso_num}"] = uso_principal_suelo
        else:
            # Pisos superiores
            usos_por_piso[f"Piso {piso_num}"] = distribucion_piso.get('uso_pisos_superiores', uso_principal_suelo)

    # Preparar mix de espacios (resumen de la distribución)
    mix_espacios = distribucion_piso.get('distribucion_por_tipo', {})

    # Construir resultado final
    resultado = {
        "estrategia_normativa": {
            "aplicada": estrategia_normativa['estrategia_aplicada'],
            "bonus_floor_aplicado": estrategia_normativa['bonus_floor_aplicado'],
            "razon_bonus": estrategia_normativa['razon_bonus'],
            "usos_complementarios_permitidos": estrategia_normativa['usos_complementarios_permitidos'],
            "detalles": estrategia_normativa['detalles']
        },
        "usos_por_piso": usos_por_piso,
        "mix_espacios": mix_espacios,
        "area_total_construida": {
            "area_neta_total_m2": round(area_neta_total, 2),
            "area_bruta_por_piso_m2": round(area_bruta_por_piso, 2),
            "area_bruta_total_m2": round(area_bruta_total, 2),
            "numero_pisos": int(numero_pisos),
            "area_neta_por_piso_m2": round(area_neta_por_piso, 2)
        },
        "estimacion_costos": estimacion_costos,
        "informacion_base": {
            "uso_principal_suelo": uso_principal_suelo,
            "area_neta_por_piso_entrada": round(area_neta_por_piso, 2),
            "altura_maxima_pisos_entrada": altura_maxima_pisos,
            "lote_area_m2": float(lot_area)
        }
    }

    # Convertir a JSON para salida
    resultado_json = json.dumps(resultado, indent=2, ensure_ascii=False)

    print("\n=== RESULTADO GENERADO ===")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

    # También guardar como archivo en el directorio del proyecto
    output_path = os.path.join(os.path.dirname(__file__), "..", "..", "programa_disenoparametrico.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(resultado_json)
    print(f"\nArchivo guardado en: {output_path}")

    # Salidas para Grasshopper
    return resultado_json

# Ejecutar si se ejecuta como script principal
if __name__ == "__main__":
    try:
        result = main()
    except Exception as e:
        print(f"Error en PROGRAMA_AREAS: {str(e)}")
        import traceback
        traceback.print_exc()
        # Devolver error en formato JSON para Grasshopper
        error_result = {
            "error": str(e),
            "mensaje": "Error en el cálculo del programa de áreas"
        }
        result = json.dumps(error_result, indent=2, ensure_ascii=False)

    # Para Grasshopper, necesitamos asignar el resultado a una variable de salida
    # En GH Python Script, esto se hace automáticamente al retornar o asignar a una variable
    # Asumiendo que la salida se llama "resultado_json"
    resultado_json = result