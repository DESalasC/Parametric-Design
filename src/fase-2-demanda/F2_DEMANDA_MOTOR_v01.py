#!/usr/bin/env python3
"""
DEMANDA_MOTOR_v01.py - Modelos de Viabilidad Comercial y Análisis de Mercado
GH Python Script para Grasshopper (GH Player compatible)

ENTRADAS (via Grasshopper):
  - restricciones_territoriales_json: JSON de restricciones territoriales (output de VALIDADOR_CRUZADO_v01.py)
  - datos_demograficos: JSON con datos poblacionales y socioeconómicos del área
  - indicadores_economicos: JSON con indicadores macroeconómicos locales y nacionales
  - tendencia_market: JSON con tendencias de mercado inmobiliario y comercial
  - uso_principal_suelo: Uso principal del suelo según POT (residencial, comercio, salud, oficinas, mixto)
  - horizonte_analisis: Horizonte de análisis en años (default: 10)

SALIDAS:
  - demanda_proyectada.json: JSON con proyección de demanda por tipo de uso y segmento
  - indicadores_viabilidad.json: JSON con indicadores clave de viabilidad financiera y de mercado
  - reporte_mercado.txt: Reporte legible con análisis de demanda y recomendaciones
"""

import json
import math
import os
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple, Optional

# Try to import Rhino-specific modules, provide fallbacks for testing
try:
    import rhinoscriptsyntax as rs
    RHINO_AVAILABLE = True
except ImportError:
    RHINO_AVAILABLE = False
    # Mock functions for testing/non-Rhino environments
    class MockRs:
        @staticmethod
        def Area(geometry):
            return 0.0

        @staticmethod
        def Distance(point1, point2):
            return 0.0

    rs = MockRs()

# ============================================================
# CONFIGURACIÓN DE PARÁMETROS DE MODELO (basado en building economics y market analysis)
# ============================================================

# Tasas de crecimiento poblacional anual por estrato (Colombia/DANE tasas típicas)
CRECIMIENTO_POBLA = {
    "bajo": 0.015,      # 1.5% anual
    "medio": 0.022,     # 2.2% anual
    "alto": 0.018,      # 1.8% anual
    "total": 0.019      # 1.9% promedio nacional
}

# Elasticidad ingreso-ingresión por tipo de uso (respuesta de demanda al cambio de ingresos)
ELASTICIDAD_INGRESO = {
    "residencial": 0.8,   # Menos elástico (necesidad básica)
    "oficinas": 1.2,      # Más elástico (sensible a ciclos económicos)
    "comercio": 1.0,      # Unitario elástico
    "salud": 0.6,         # Menos elástico (servicio esencial)
    "hoteleria": 1.5      # Muy elástico (turismo y ocio)
}

# Tasa de vacancia estructural por tipo de inmueble (porcentaje)
TASA_VACANZA_ESTRUCTURAL = {
    "residencial": 5.0,   # 5% vacío estructural
    "oficinas": 10.0,     # 10% en oficinas (más cíclico)
    "comercio": 8.0,      # 8% en retail
    "salud": 3.0,         # 3% en salud (menos vacante)
    "hoteleria": 25.0     # 25% en hoteles (altamente estacional)
}

# Reasonable absorption rates (mesees para absorber nueva oferta)
TASA_ABSORPCION_MENSUAL = {
    "residencial": 8.0,   # 8 unidades/mes por proyecto
    "oficinas": 1500.0,   # 1500 m²/mes
    "comercio": 800.0,    # 800 m²/mes
    "salud": 500.0,       # 500 m²/mes
    "hoteleria": 30.0     # 30 habitaciones/mes
}

# Precios base de referencia (USD/m² o USD/unidad) en Bogotá 2024
PRECIOS_REFERENCIA = {
    "residencial_venta": 2200,     # USD/m² venta
    "residencial_arriendo": 12,    # USD/m²/mes arriendo
    "oficinas_venta": 2500,        # USD/m² venta
    "oficinas_arriendo": 18,       # USD/m²/mes arriendo
    "comercio_venta": 3000,        # USD/m² venta
    "comercio_arriendo": 25,       # USD/m²/mes arriendo
    "hoteleria_llave": 180000      # USD/llave (habitación)
}

# Tasas de capitalización (cap rates) para valorización
TASA_CAPITALIZACION = {
    "residencial": 0.05,   # 5% cap rate
    "oficinas": 0.07,      # 7%
    "comercio": 0.06,      # 6%
    "salud": 0.055,        # 5.5%
    "hoteleria": 0.09      # 9% (mayor riesgo)
}

# Costos de operación y mantenimiento anual (% del valor de propiedad)
COSTOS_O_M_ANUALES = {
    "residencial": 0.015,  # 1.5% del valor
    "oficinas": 0.025,     # 2.5%
    "comercio": 0.02,      # 2.0%
    "salud": 0.03,         # 3.0%
    "hoteleria": 0.04      # 4.0%
}

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

def calculate_cagr(initial_value, final_value, years):
    """
    Calculate Compound Annual Growth Rate (CAGR)
    CAGR = (Ending Value / Beginning Value)^(1/n) - 1
    """
    if initial_value <= 0 or years <= 0:
        return 0.0
    return (final_value / initial_value) ** (1/years) - 1

def project_demand(base_demand, growth_rate, years):
    """
    Project future demand using compound growth
    Future Value = Present Value * (1 + r)^n
    """
    if years < 0:
        return base_demand
    return base_demand * ((1 + growth_rate) ** years)

def calculate_net_present_value(cash_flows, discount_rate):
    """
    Calculate Net Present Value (NPV) of cash flows
    NPV = Σ [CF_t / (1 + r)^t] for t=0 to n
    """
    npv = 0.0
    for t, cf in enumerate(cash_flows):
        npv += cf / ((1 + discount_rate) ** t)
    return npv

def calculate_internal_rate_of_return(cash_flows, guess=0.1, max_iterations=100, tolerance=1e-6):
    """
    Calculate Internal Rate of Return (IRR) using Newton-Raphson method
    """
    if len(cash_flows) < 2:
        return 0.0

    rate = guess
    for _ in range(max_iterations):
        npv = 0.0
        dnpv = 0.0

        for t, cf in enumerate(cash_flows):
            factor = (1 + rate) ** t
            npv += cf / factor
            if t > 0:
                dnpv -= t * cf / (factor * (1 + rate))

        if abs(npv) < tolerance:
            break

        if dnpv == 0:
            break

        rate -= npv / dnpv

    return rate

# ============================================================
# MODELOS DE DEMANDA
# ============================================================

def model_demographic_growth(poblacion_base, edad_estructurada, crecimiento_anual, anos_proyeccion):
    """
    Modelo de crecimiento poblacional por estructura etaria
    """
    poblacion_proyectada = {}
    for segmento, poblacion in poblacion_base.items():
        crecimiento_seg = crecimiento_anual.get(segmento, crecimiento_anual.get("total", 0.019))
        poblacion_proyectada[segmento] = project_demand(poblacion, crecimiento_seg, anos_proyeccion)

    return poblacion_proyectada

def model_housing_demand(poblacion_objetivo, tasa_formacion_hogares, ingreso_medio, elasticidad_ingreso):
    """
    Modelo de demanda habitacional basado en formación de hogares y capacidad de pago
    """
    # Hogares potenciales = población objetivo * tasa de formación de hogares
    hogares_potenciales = poblacion_objetivo * tasa_formacion_hogares

    # Ajuste por capacidad de ingreso (simplificado)
    factor_ingreso = 1 + (ingreso_medio - 1000) * 0.0001 * elasticidad_ingreso  # Línea base 1000 USD/mes
    factor_ingreso = max(0.5, min(2.0, factor_ingreso))  # Limitar entre 0.5 y 2.0

    demanda_ajustada = hogares_potenciales * factor_ingreso

    return max(0, demanda_ajustada)

def model_commercial_demand(poblacion_servicio, ingreso_per_capita, densidad_comercial_base, elasticidad_ingreso):
    """
    Modelo de demanda comercial basado en población de servicio y poder adquisitivo
    """
    # Poder adquisitivo total de la población de servicio
    poder_adquisitivo_total = poblacion_servicio * ingreso_per_capita

    # Demanda base de espacio comercial (m² per cápita ajustado por ingreso)
    m2_per_capita_base = densidad_comercial_base  # m² comercial per cápita base
    ajuste_ingreso = 1 + (ingreso_per_capita - 500) * 0.0002 * elasticidad_ingreso  # Base 500 USD/mes
    ajuste_ingreso = max(0.3, min(3.0, ajuste_ingreso))

    demanda_m2 = poder_adquisitivo_total * m2_per_capita_base * ajuste_ingreso / 1000  # Convertir a miles de m2

    return max(0, demanda_m2)

def model_office_demand(poblacion_activa, tasa_participacion_laboral, oficina_por_trabajador, crecimiento_teletrabajo):
    """
    Modelo de demanda de oficinas basado en población activa y tendencia al teletrabajo
    """
    trabajadores_oficina = poblacion_activa * tasa_participacion_laboral * (1 - crecimiento_teletrabajo)
    demanda_m2 = trabajadores_oficina * oficina_por_trabajador

    return max(0, demanda_m2)

def model_healthcare_demand(poblacion_total, tasa_usuarios_salud, m2_por_usuario, factor_envejecimiento):
    """
    Modelo de demanda de infraestructura de salud
    """
    usuarios_salud = poblacion_total * tasa_usuarios_salud
    # Ajuste por factor de envejecimiento (mayor demanda de salud en人口老龄化)
    demanda_m2 = usuarios_salud * m2_por_usuario * (1 + factor_envejecimiento)

    return max(0, demanda_m2)

# ============================================================
# ANÁLISIS DE VIABILIDAD
# ============================================================

def calculate_financial_metrics(inversion_inicial, flujos_efectivo, tasa_descuento, años_proyeccion):
    """
    Calcular métricas financieras clave: VAN, TIR, Payback Period, Beneficio/Costo
    """
    # Asegurar que tenemos flujos para todos los años
    flujos_completos = list(flujos_efectivo) + [0] * max(0, años_proyeccion - len(flujos_efectivo))
    flujos_completos = flujos_completos[:años_proyeccion]

    # VAN (Net Present Value)
    van = calculate_net_present_value([-inversion_inicial] + flujos_completos, tasa_descuento)

    # TIR (Internal Rate of Return)
    tir = calculate_internal_rate_of_return([-inversion_inicial] + flujos_completos)

    # Payback Period (simple)
    flujo_acumulado = -inversion_inicial
    payback_period = años_proyeccion  # Valor por defecto si no se recupera
    for año, flujo in enumerate(flujos_completos):
        flujo_acumulado += flujo
        if flujo_acumulado >= 0:
            # Interpolar para mayor precisión
            if año > 0:
                flujo_anterior = flujo_acumulado - flujo
                if flujo != 0:
                    fraccion = -flujo_anterior / flujo
                    payback_period = año - 1 + fraccion
                else:
                    payback_period = año
            else:
                payback_period = 0
            break

    # Beneficio/Costo Ratio
    valor_actual_beneficios = calculate_net_present_value(flujos_completos, tasa_descuento)
    valor_actual_costos = inversion_inicial  # Simplificado: asumimos inversión inicial como costo
    bc_ratio = valor_actual_beneficios / valor_actual_costos if valor_actual_costos > 0 else 0

    return {
        "valor_actual_neto": van,
        "tasa_interna_retorno": tir,
        "periodo_recuperacion": payback_period,
        "indice_beneficio_costo": bc_ratio,
        "flujo_efectivo_acumulado": flujo_acumulado
    }

def calculate_land_residual_value(ventas_brutas_anuales, Gastos_O_M_anuales, tasa_capitalizacion, vida_remedio):
    """
    Calcular el valor residual del suelo usando enfoque de capitalización de renta neta
    Valor del suelo = (Ingreso neto operativo) / Tasa de capitalización
    """
    ingreso_neto_operativo = ventas_brutas_anuales - Gastos_O_M_anuales
    if tasa_capitalizacion > 0:
        valor_suelo = ingreso_neto_operativo / tasa_capitalizacion
    else:
        valor_suelo = 0

    return max(0, valor_suelo)

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():
    """
    Función principal que procesa las entradas y genera el análisis de demanda
    """

    if not RHINO_AVAILABLE:
        print("ADVERTENCIA: Rhino/Grasshopper no disponible. Ejecutando en modo de prueba.")

    print("=== DEMANDA_MOTOR - Modelos de Viabilidad Comercial ===")

    # Parsear entradas JSON si es necesario
    restricciones_dict = safe_json_parse(restricciones_territoriales_json)
    demografia_dict = safe_json_parse(datos_demograficos)
    economia_dict = safe_json_parse(indicadores_economicos)
    mercado_dict = safe_json_parse(tendencia_market)

    # Extraer parámetros de restricciones territoriales (si están disponibles)
    area_neta_disponible = restricciones_dict.get("area_total_construida", {}).get("area_neta_total_m2", 1000)
    altura_maxima_pisos = restricciones_dict.get("area_total_construida", {}).get("numero_pisos", 5)
    uso_principal = restricciones_dict.get("informacion_base", {}).get("uso_principal_suelo", uso_principal_suelo)

    print(f"Área neta disponible: {area_neta_disponible:.2f} m2")
    print(f"Altura máxima (pisos): {altura_maxima_pisos}")
    print(f"Uso principal del suelo: {uso_principal}")
    print(f"Horizonte de análisis: {horizonte_analisis} años")

    # Extraer datos demográficos
    poblacion_total = safe_float(demografia_dict.get("poblacion_total", 50000))
    poblacion_por_estrato = {
        "bajo": safe_float(demografia_dict.get("poblacion_bajo", poblacion_total * 0.4)),
        "medio": safe_float(demografia_dict.get("poblacion_medio", poblacion_total * 0.4)),
        "alto": safe_float(demografia_dict.get("poblacion_alto", poblacion_total * 0.2))
    }
    ingreso_per_capita = safe_float(demografia_dict.get("ingreso_per_capita_mensual", 800))  # USD/mes
    tasa_urbanizacion = safe_float(demografia_dict.get("tasa_urbanizacion", 0.75))

    # Extraer datos económicos
    crecimiento_pib_anual = safe_float(economia_dict.get("crecimiento_pib_anual", 0.03))
    inflation_anual = safe_float(economia_dict.get("inflacion_anual", 0.035))
    tasa_descuento = safe_float(economia_dict.get("tasa_descuento", 0.10))  # WACC típico

    # Extraer tendencias de mercado
    crecimiento_alquiler_anual = safe_float(mercado_dict.get("crecimiento_alquiler_anual", 0.04))
    crecimiento_precio_venta_anual = safe_float(mercado_dict.get("crecimiento_precio_venta_anual", 0.05))
    variacion_inventario = safe_float(mercado_dict.get("variacion_inventario_anual", 0.02))  # % cambio en inventario

    # ============================================================
    # PROYECCIÓN DE DEMOGRAFÍA Y ECONOMÍA
    # ============================================================

    # Proyección poblacional
    poblacion_proyectada = model_demographic_growth(
        poblacion_por_estrato,
        poblacion_por_estrato,  # Estructura inicial (simplificado)
        CRECIMIENTO_POBLA,
        horizonte_analisis
    )

    poblacion_futuro_total = sum(poblacion_proyectada.values())
    print(f"Población proyectada en {horizonte_analisis} años: {poblacion_futuro_total:,.0f}")

    # Proyección de ingreso per capita (ajustado por crecimiento económico y inflación real)
    crecimiento_ingreso_real = crecimiento_pib_anual - inflation_anual  # Crecimiento real del ingreso
    ingreso_futuro = project_demand(ingreso_per_capita, crecimiento_ingreso_real, horizonte_analisis)
    print(f"Ingreso per capita proyectado: ${ingreso_futuro:.2f}/mes")

    # ============================================================
    # MODELOS DE DEMANDA POR TIPO DE USO
    # ============================================================

    # Parámetros específicos por tipo (basados en estándares internacionales ajustados a contexto local)
    parametros_tipo = {
        "residencial": {
            "tasa_formacion_hogares": 0.35,          # 35% de población forms households
            "m2_por_vivienda": 80,                   # Promedio m² por unidad habitacional
            "vacancia_estructural": TASA_VACANZA_ESTRUCTURAL["residencial"],
            "absorcion_mensual": TASA_ABSORPCION_MENSUAL["residencial"],
            "precio_referencia": PRECIOS_REFERENCIA["residencial_venta"],
            "alquiler_referencia": PRECIOS_REFERENCIA["residencial_arriendo"],
            "cap_rate": TASA_CAPITALIZACION["residencial"],
            "costo_o_m": COSTOS_O_M_ANUALES["residencial"]
        },
        "oficinas": {
            "tasa_participacion_laboral": 0.55,      # 55% población en edad laboral participa
            "m2_por_trabajador": 15,                 # m² por trabajador de oficina
            "crecimiento_teletrabajo": 0.15,         # 15% reducción esperada por teletrabajo
            "vacancia_estructural": TASA_VACANZA_ESTRUCTURAL["oficinas"],
            "absorcion_mensual": TASA_ABSORPCION_MENSUAL["oficinas"],
            "precio_referencia": PRECIOS_REFERENCIA["oficinas_venta"],
            "alquiler_referencia": PRECIOS_REFERENCIA["oficinas_arriendo"],
            "cap_rate": TASA_CAPITALIZACION["oficinas"],
            "costo_o_m": COSTOS_O_M_ANUALES["oficinas"]
        },
        "comercio": {
            "indice_comercial_base": 0.0015,         # 1.5 m² comercial per cápita base
            "vacancia_estructural": TASA_VACANZA_ESTRUCTURAL["comercio"],
            "absorcion_mensual": TASA_ABSORPCION_MENSUAL["comercio"],
            "precio_referencia": PRECIOS_REFERENCIA["comercio_venta"],
            "alquiler_referencia": PRECIOS_REFERENCIA["comercio_arriendo"],
            "cap_rate": TASA_CAPITALIZACION["comercio"],
            "costo_o_m": COSTOS_O_M_ANUALES["comercio"]
        },
        "salud": {
            "tasa_usuarios_salud": 0.15,             # 15% de población usa servicios de salud mensualmente
            "m2_por_usuario": 2.5,                   # m² de instalación por usuario
            "factor_envejecimiento": 0.002 * poblacion_proyectada.get("alto", 0) / poblacion_futuro_total,  # Ajuste por envejecimiento
            "vacancia_estructural": TASA_VACANZA_ESTRUCTURAL["salud"],
            "absorcion_mensual": TEA_ABSORPCION_MENSUAL["salud"],
            "precio_referencia": 0,                  # No se vende generalmente
            "alquiler_referencia": 0,                # Se mide en términos de servicios
            "cap_rate": TASA_CAPITALIZACION["salud"],
            "costo_o_m": COSTOS_O_M_ANUALES["salud"]
        }
    }

    # Calcular demanda proyectada por tipo de uso
    demanda_proyectada = {}

    # Demanda residencial
    if uso_principal in ["residencial", "mixto"] or "residencial" in [uso_principal]:  # Simplificado
        parametros = parametros_tipo["residencial"]
        demanda_hogares = model_housing_demand(
            poblacion_futuro_total,
            parametros["tasa_formacion_hogares"],
            ingreso_futuro,
            ELASTICIDAD_INGRESO["residencial"]
        )
        demanda_m2_residencial = demanda_hogares * parametros["m2_por_vivienda"]
        demanda_proyectada["residencial"] = {
            "demanda_unidades": demanda_hogares,
            "demanda_m2": demanda_m2_residencial,
            "valor_mercado_usd": demanda_m2_residencial * parametros["precio_referencia"],
            "valor_alquiler_anual_usd": demanda_m2_residencial * parametros["alquiler_referencia"] * 12,
            "vacancia_estructural_pct": parametros["vacancia_estructural"],
            "absorcion_mensual_unidades": parametros["absorcion_mensual"]
        }

    # Demanda de oficinas
    if uso_principal in ["oficinas", "mixto"]:
        parametros = parametros_tipo["oficinas"]
        # Población activa estimada (60% de total en edad laboral, 65% de esa población activa)
        poblacion_activa = poblacion_futuro_total * 0.60 * 0.65
        demanda_m2_oficinas = model_office_demand(
            poblacion_activa,
            parametros["tasa_participacion_laboral"],
            parametros["m2_por_trabajador"],
            parametros["crecimiento_teletrabajo"]
        )
        demanda_puestos_oficinas = demanda_m2_oficinas / parametros["m2_por_trabajador"]
        demanda_proyectada["oficinas"] = {
            "demanda_m2": demanda_m2_oficinas,
            "demanda_puestos": demanda_puestos_oficinas,
            "valor_mercado_usd": demanda_m2_oficinas * parametros["precio_referencia"],
            "valor_alquiler_anual_usd": demanda_m2_oficinas * parametros["alquiler_referencia"] * 12,
            "vacancia_estructural_pct": parametros["vacancia_estructural"],
            "absorcion_mensual_m2": parametros["absorcion_mensual"]
        }

    # Demanda comercial
    if uso_principal in ["comercio", "mixto"]:
        parametros = parametros_tipo["comercio"]
        # Población de servicio: residentes + fuerza laboral diaria estimada
        poblacion_servicio = poblacion_futuro_total * (1 + 0.3)  # +30% por trabajadores que vienen de fuera
        demanda_m2_comercio = model_commercial_demand(
            poblacion_servicio,
            ingreso_futuro,
            parametros["indice_comercial_base"],
            ELASTICIDAD_INGRESO["comercio"]
        )
        demanda_proyectada["comercio"] = {
            "demanda_m2": demanda_m2_comercio,
            "valor_mercado_usd": demanda_m2_comercio * parametros["precio_referencia"],
            "valor_alquiler_anual_usd": demanda_m2_comercio * parametros["alquiler_referencia"] * 12,
            "vacancia_estructural_pct": parametros["vacancia_estructural"],
            "absorcion_mensual_m2": parametros["absorcion_mensual"]
        }

    # Demanda de salud
    if uso_principal in ["salud", "mixto"]:
        parametros = parametros_tipo["salud"]
        demanda_m2_salud = model_healthcare_demand(
            poblacion_futuro_total,
            parametros["tasa_usuarios_salud"],
            parametros["m2_por_usuario"],
            parametros["factor_envejecimiento"]
        )
        demanda_unidades_salud = demanda_m2_salud / parametros["m2_por_usuario"]  # Número de usuarios equivalentes
        demanda_proyectada["salud"] = {
            "demanda_m2": demanda_m2_salud,
            "demanda_usuarios_equivalentes": demanda_unidades_salud,
            "valor_equipamiento_usd": demanda_m2_salud * 800,  # Estimado de equipamiento por m2
            "vacancia_estructural_pct": parametros["vacancia_estructural"],
            "absorcion_mensual_m2": parametros["absorcion_mensual"]
        }

    # ============================================================
    # ANÁLISIS DE VIABILIDAD FINANCIERA
    # ============================================================

    indicadores_viabilidad = {}

    # Para cada tipo de uso con demanda significativa, calcular viabilidad
    for tipo, demanda in demanda_proyectada.items():
        if tipo in parametros_tipo and demanda.get("demanda_m2", 0) > 0:
            parametros = parametros_tipo[tipo]

            # Simplificación: corriente de caja anual estimada
            # Ingresos = Alquiler anual - Gastos O&M
            ingreso_anual = demanda.get("valor_alquiler_anual_usd", 0)
            area_total = demanda.get("demanda_m2", 0)
            costo_anual_om = area_total * parametros["costo_o_m"] * 1000  # Asumiendo valor de propiedad ~1000x alquiler mensual
            flujo_neto_anual = ingreso_anual - costo_anual_om

            # Flujo de caja proyectado (asumiendo crecimiento estable)
            flujos_anuales = []
            for año in range(1, int(horizonte_analisis) + 1):
                factor_crecimiento = (1 + crecimiento_ingreso_real) ** año
                flujo_ajustado = flujo_neto_anual * factor_crecimiento
                flujos_anuales.append(flujo_ajustado)

            # Inversión inicial estimada (costo de construcción)
            costo_construccion_m2 = 1200  # USD/m2 estimado de construcción
            inversion_inicial = area_total * costo_construccion_m2

            # Calcular métricas financieras
            metricas = calculate_financial_metrics(
                inversion_inicial,
                flujos_anuales,
                tasa_descuento,
                int(horizonte_analisis)
            )

            # Valor residual del suelo (approximado)
            valor_suelo = calculate_land_residual_value(
                ingreso_anual,
                costo_anual_om,
                parametros["cap_rate"],
                int(horizonte_analisis)
            )

            indicadores_viabilidad[tipo] = {
                "inversion_inicial_usd": inversion_inicial,
                "valor_suelo_estimado_usd": valor_suelo,
                "flujo_neto_anual_actual_usd": flujo_neto_anual,
                "metricas_financieras": metricas,
                "ratio_loan_to_value": min(0.7, inversion_inicial / (valor_suelo + inversion_inicial * 0.3)) if (valor_suelo + inversion_inicial * 0.3) > 0 else 0.7,
                "periodo_recuperacion_ajustado": metricas["periodo_recuperacion"],
                "rentabilidad_esperada": metricas["tasa_interna_retorno"]
            }

    # ============================================================
    # GENERACIÓN DE RESULTADOS
    # ============================================================

    # Preparar resultado de demanda proyectada
    resultado_demanda = {
        "metadata": {
            "version": "1.0.0",
            "fecha_analisis": datetime.now().isoformat(),
            "horizonte_analisis_anos": horizonte_analisis,
            "poblacion_base": poblacion_total,
            "poblacion_proyectada": poblacion_futuro_total,
            "ingreso_per_capita_base": ingreso_per_capita,
            "ingreso_per_capita_proyectado": ingreso_futuro,
            "uso_principal_suelo": uso_principal,
            "area_neta_disponible_m2": area_neta_disponible
        },
        "demanda_por_tipo": demanda_proyectada,
        "supuestos_modelo": {
            "crecimiento_poblacional_anual": CRECIMIENTO_POBLA,
            "elasticidad_ingreso": ELASTICIDAD_INGRESO,
            "tasa_vacancia_estructural": TASA_VACANZA_ESTRUCTURAL,
            "tasas_absorcion_mensual": TASA_ABSORPCION_MENSUAL,
            "precios_referencia": PRECIOS_REFERENCIA,
            "tasas_capitalizacion": TASA_CAPITALIZACION,
            "costos_o_m_anuales": COSTOS_O_M_ANUALES
        }
    }

    # Preparar indicadores de viabilidad
    resultado_viabilidad = {
        "metadata": {
            "version": "1.0.0",
            "fecha_analisis": datetime.now().isoformat(),
            "tasa_descuento_utilizada": tasa_descuento,
            "horizonte_analisis_anos": horizonte_analisis
        },
        "viabilidad_por_tipo": indicadores_viabilidad,
        "resumen_ejecutivo": {
            "total_inversion_estimada_usd": sum(
                inv.get("inversion_inicial_usd", 0)
                for inv in indicadores_viabilidad.values()
            ),
            "valor_suelo_total_estimado_usd": sum(
                inv.get("valor_suelo_estimado_usd", 0)
                for inv in indicadores_viabilidad.values()
            ),
            "tipo_mas_viable": max(
                indicadores_viabilidad.keys(),
                key=lambda k: indicadores_viabilidad[k].get("metricas_financieras", {}).get("valor_actual_neto", -999999)
            ) if indicadores_viabilidad else "ninguno",
            "tir_promedio_ponderado": sum(
                inv.get("metricas_financieras", {}).get("tasa_interna_retorno", 0) *
                inv.get("inversion_inicial_usd", 0)
                for inv in indicadores_viabilidad.values()
            ) / max(sum(inv.get("inversion_inicial_usd", 0) for inv in indicadores_viabilidad.values()), 1)
        }
    }

    # Generar reporte legible
    reporte_lineas = [
        "=" * 60,
        "ANÁLISIS DE DEMANDA Y VIABILIDAD COMERCIAL",
        "=" * 60,
        f"Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Horizonte de análisis: {horizonte_analisis} años",
        f"Ubicación: Bogotá D.C. (supuesto)",
        f"Uso principal del suelo según POT: {uso_principal}",
        "",
        "DATOS DE BASE:",
        f"  Población actual: {poblacion_total:,.0f} habitantes",
        f"  Ingreso per capita mensual: ${ingreso_per_capita:.2f} USD",
        f"  Área neta disponible: {area_neta_disponible:.2f} m²",
        "",
        "PROYECCIONES DEMGRÁFICAS:",
        f"  Población proyectada ({horizonte_analisis} años): {poblacion_futuro_total:,.0f} habitantes",
        f"  Crecimiento poblacional acumulado: {((poblacion_futuro_total/poblacion_total)-1)*100:.1f}%",
        f"  Ingreso per capita proyectado: ${ingreso_futuro:.2f} USD/mes",
        "",
        "DEMANDA PROYECTADA POR TIPO DE USO:",
    ]

    for tipo, demanda in demanda_proyectada.items():
        if demanda.get("demanda_m2", 0) > 0 or demanda.get("demanda_unidades", 0) > 0:
            reporte_lineas.append(f"  {tipo.upper()}:")
            if "demanda_unidades" in demanda:
                reporte_lineas.append(f"    - Unidades: {demanda['demanda_unidades']:,.0f}")
            if "demanda_m2" in demanda:
                reporte_lineas.append(f"    - Área: {demanda['demanda_m2']:,.2f} m²")
            if "valor_mercado_usd" in demanda:
                valor = demanda["valor_mercado_usd"]
                if valor > 0:
                    reporte_lineas.append(f"    - Valor de mercado: ${valor:,.0f} USD")
            if "valor_alquiler_anual_usd" in demanda:
                valor = demanda["valor_alquiler_anual_usd"]
                if valor > 0:
                    reporte_lineas.append(f"    - Valor de alquiler anual: ${valor:,.0f} USD/año")

    reporte_lineas.extend([
        "",
        "INDICADORES DE VIABILIDAD FINANCIERA:",
    ])

    for tipo, indicadores in indicadores_viabilidad.items():
        met = indicadores.get("metricas_financieras", {})
        if met:
            reporte_lineas.append(f"  {tipo.upper()}:")
            reporte_lineas.append(f"    - Inversión inicial: ${indicadores.get('inversion_inicial_usd', 0):,.0f} USD")
            reporte_lineas.append(f"    - VAN: ${met.get('valor_actual_neto', 0):,.0f} USD")
            tir_pct = met.get('tasa_interna_retorno', 0) * 100
            reporte_lineas.append(f"    - TIR: {tir_pct:.1f}%")
            pp = met.get('periodo_recuperacion', 0)
            if pp < 50:  # Razonable
                reporte_lineas.append(f"    - Payback: {pp:.1f} años")
            else:
                reporte_lineas.append(f"    - Payback: >{horizonte_analisis} años (no recuperable en horizonte)")
            bc = met.get('indice_beneficio_costo', 0)
            if bc > 0:
                reporte_lineas.append(f"    - B/C Ratio: {bc:.2f}")
            else:
                reporte_lineas.append(f"    - B/C Ratio: No viable (beneficios < costos)")

    reporte_lineas.extend([
        "",
        "RECOMENDACIONES:",
    ])

    # Generar recomendaciones basado en análisis
    tipos_viales = []
    for tipo, indicadores in indicadores_viabilidad.items():
        met = indicadores.get("metricas_financieras", {})
        van = met.get("valor_actual_neto", 0)
        tir = met.get("tasa_interna_retorno", 0)
        bc = met.get("indice_beneficio_costo", 0)

        if van > 0 and tir > 0.08 and bc > 1.0:  # Umbrales razonables
            tipos_viales.append(tipo)

    if tipos_viales:
        recomendacion = f"Priorizar desarrollo de: {', '.join([t.upper() for t in tipos_viales])}"
        if len(tipos_viales) > 1:
            recomendacion += " (desarrollo mixto recomendado)"
        else:
            recomendacion += f" como uso dominante"
    else:
        recomendacion = "Reconsiderar escala o esperar mejores condiciones de mercado"

    reporte_lineas.append(f"  {recomendacion}")
    reporte_lineas.extend([
        "",
        "FACTORES DE RIESGO A CONSIDERAR:",
        "  - Variabilidad en tasas de interés de financiamiento",
        "  - Cambios en regulación de uso de suelo",
        "  - Fluctuaciones en el poder adquisitivo local",
        "  - Competencia de proyectos vecinos",
        "  - Riesgos de construcción y aprobaciones",
        "",
        "=" * 60
    ])

    reporte_texto = "\n".join(reporte_lineas)

    # Convertir resultados a JSON para salida
    demanda_json = json.dumps(resultado_demanda, indent=2, ensure_ascii=False)
    viabilidad_json = json.dumps(resultado_viabilidad, indent=2, ensure_ascii=False)

    print("\n=== RESUMEN DE EJECUCIÓN ===")
    print(f"Análisis completado para {len(demanda_proyectada)} tipos de uso")
    print(f"Horizonte: {horizonte_analisis} años")
    print(f"Población proyectada: {poblacion_futuro_total:,.0f}")

    # Guardar resultados en archivos
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    demanda_path = os.path.join(output_dir, "demanda_proyectada.json")
    with open(demanda_path, 'w', encoding='utf-8') as f:
        f.write(demanda_json)

    viabilidad_path = os.path.join(output_dir, "indicadores_viabilidad.json")
    with open(viabilidad_path, 'w', encoding='utf-8') as f:
        f.write(viabilidad_json)

    reporte_path = os.path.join(output_dir, "reporte_mercado.txt")
    with open(reporte_path, 'w', encoding='utf-8') as f:
        f.write(reporte_texto)

    print(f"\nArchivos guardados en: {output_dir}")
    print(f"  - demanda_proyectada.json")
    print(f"  - indicadores_viabilidad.json")
    print(f"  - reporte_mercado.txt")

    # Salidas para Grasshopper
    return demanda_json, viabilidad_json, reporte_texto

# Ejecutar si se ejecuta como script principal
if __name__ == "__main__":
    try:
        demanda_result, viabilidad_result, reporte_result = main()
    except Exception as e:
        print(f"Error en DEMANDA_MOTOR: {str(e)}")
        import traceback
        traceback.print_exc()
        # Devolver error en formato JSON para Grasshopper
        error_result = {
            "error": str(e),
            "mensaje": "Error en el cálculo de demanda y viabilidad"
        }
        demanda_result = json.dumps(error_result, indent=2, ensure_ascii=False)
        viabilidad_result = json.dumps(error_result, indent=2, ensure_ascii=False)
        reporte_result = f"ERROR: {str(e)}"

    # Para Grasshopper, necesitamos asignar los resultados a variables de salida
    # En GH Python Script, esto se hace automáticamente al retornar o asignar a variables
    # Asumiendo que las salidas se llaman "demanda_json", "viabilidad_json", "reporte_texto"
    demanda_json = demanda_result
    viabilidad_json = viabilidad_result
    reporte_texto = reporte_result