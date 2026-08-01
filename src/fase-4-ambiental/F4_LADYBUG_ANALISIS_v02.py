#!/usr/bin/env python3
"""
LADYBUG_ANALISIS_v02.py - Análisis Ambiental con Ladybug
GH Python Script para Grasshopper (GH Player compatible)

Este componente realiza análisis ambientales usando las bibliotecas de Ladybug,
incluyendo análisis de radiación solar, iluminación natural, confort térmico,
y otros estudios ambientales para el diseño arquitectónico sostenible.

ENTRADAS (via Grasshopper):
  - ladybug_entrada_json: JSON preparado por PREP_LADYBUG_v01.py
  - geometria_analisis: Geometría específica para analizar (opcional)
  - analysis_type: Tipo de análisis ("radiation", "illuminance", "visibility", "glare", "temperature", "humidity", "wind")
  - analysis_period: Período de análisis ("annual", "summer", "winter", "monthly", "hourly", "specific_dates")
  - analysis_parameters: Parámetros específicos para el tipo de análisis
  - output_format: Formato de salida ("charts", "data", "both", "report")
  - units_system: Sistema de unidades ("metric", "imperial")
  - sky_model: Modelo de cielo a usar ("perez", "cie", "horn", "makeham")
  - ground_reflectance: Reflectancia del terreno (0.0-1.0, default 0.2)
  - include_sky_effect: Incluir efecto de cielo difuso (default True)
  - include_ground_reflection: Incluir reflexión del terreno (default True)
  - analysis_surface: Superficie específica a analizar (opcional)

SALIDAS:
  - analisis_resultados.json: Resultados completos del análisis en formato JSON
  - analisis_visualizacion.png: Gráficos y visualizaciones (como datos codificados en base64 o ruta)
  - analisis_estadisticas.json: Estadísticas resumidas del análisis
  - reporte_analisis.txt: Reporte legible e interpretado de los resultados
  - datos_para_honeybee.json: Datos preparados para posible uso en Honeybee (si aplica)
"""

import json
import base64
import io
import math
import os
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Any, Optional, Union
from enum import Enum

# Try to import Rhino-specific modules, provide fallbacks for testing
try:
    import rhinoscriptsyntax as rs
    import Rhino
    import scriptcontext
    RHINO_AVAILABLE = True
except ImportError:
    RHINO_AVAILABLE = False
    print("WARNING: Rhino/Grasshopper not available. Running in test mode.")

    # Mock RhinoCommon classes for testing
    class Point3d:
        def __init__(self, x=0, y=0, z=0):
            self.X = x
            self.Y = y
            self.Z = z

    class Vector3d:
        def __init__(self, x=0, y=0, z=0):
            self.X = x
            self.Y = y
            self.Z = z

    class Plane:
        def __init__(self, origin=None, xdir=None, ydir=None, zdir=None):
            self.Origin = origin or Point3d(0, 0, 0)
            self.XAxis = xdir or Vector3d(1, 0, 0)
            self.YAxis = ydir or Vector3d(0, 1, 0)
            self.ZAxis = zdir or Vector3d(0, 0, 1)

    # Mock functions
    class MockRs:
        @staticmethod
        def PointCoordinates(point):
            return [point.X, point.Y, point.Z]

        @staticmethod
        def VectorCreate(point1, point2):
            return Vector3d(point2.X - point1.X, point2.Y - point1.Y, point2.Z - point1.Z)

        @staticmethod
        def UnitVector(vector):
            length = math.sqrt(vector.X**2 + vector.Y**2 + vector.Z**2)
            if length == 0:
                return Vector3d(0, 0, 0)
            return Vector3d(vector.X/length, vector.Y/length, vector.Z/length)

        @staticmethod
        def Distance(point1, point2):
            return math.sqrt(
                (point2.X - point1.X)**2 +
                (point2.Y - point1.Y)**2 +
                (point2.Z - point1.Z)**2
            )

        @staticmethod
        def AngleBetween(vector1, vector2):
            dot = vector1.X*vector2.X + vector1.Y*vector2.Y + vector1.Z*vector2.Z
            len1 = math.sqrt(vector1.X**2 + vector1.Y**2 + vector1.Z**2)
            len2 = math.sqrt(vector2.X**2 + vector2.Y**2 + vector2.Z**2)
            if len1 == 0 or len2 == 0:
                return 0
            cos_angle = max(-1, min(1, dot/(len1*len2)))
            return math.degrees(math.acos(cos_angle))

        @staticmethod
        def AddPoint(point):
            return f"point_{id(point)}"

        @staticmethod
        def AddLine(point1, point2):
            return f"line_{id(point1)}_{id(point2)}"

        @staticmethod
        def AddTextDot(text, point):
            return f"textdot_{id(point)}"

        @staticmethod
        def EnableRedraw(enable):
            pass

    rs = MockRs()

# ============================================================
# ENUMS Y CONSTANTES
# ============================================================

class TipoAnalisis(Enum):
    RADIACION_SOLAR = "radiation"
    ILUMINACION_NATURAL = "illuminance"
    VISIBILIDAD_CIEGO = "visibility"
    DESLUMBRAMIENTO = "glare"
    TEMPERATURA_OPERATIVA = "temperature"
    HUMEDAD_RELATIVA = "humidity"
    VELOCIDAD_VIENTO = "wind"
    PRESSION_ATMOSFERICA = "pressure"
    INDICE_RADIACION_ULTRAVIOLETA = "uv_index"
    TEMPERATURA_RODIO = "operative_temperature"

class PeriodoAnalisis(Enum):
    ANUAL = "annual"
    ESTIVAL = "summer"
    HIVERNAL = "winter"
    PRIMAVERAL = "spring"
    OTOÑAL = "fall"
    MENSUAL = "monthly"
    SEMANAL = "weekly"
    DIARIO = "daily"
    HOURLY = "hourly"
    MINUTELY = "minutely"
    FECHAS_ESPECIFICAS = "specific_dates"
    RANGO_FECHAS = "date_range"

class ModeloCielo(Enum):
    PEREZ = "perez"
    CIE = "cie"
    HORN = "horn"
    MAKEHAM = "makeham"

class SistemaUnidades(Enum):
    METRICO = "metric"
    IMPERIAL = "imperial"

# Valores por defecto
CONFIGURACION_POR_DEFECTO = {
    "resolucion_espacial": 0.5,  # metros
    "resolucion_temporal": 1,    # horas
    "altura_analisis_humano": 1.1,  # metros
    "reflejo_suelo_por_defecto": 0.2,
    "altura_cielo_punto": 1000,   # metros para cálculo de cielo
    "umbral_deslumbrante": 1000,  # cd/m2
    "nivel_iluminancia_minimo": 300, # lux para zonas de trabajo
    "factor_correccion_albedo": 0.2
}

# Factores de corrección estacional (para hemisferio sur)
FACTORES_ESTACIONALES_HS = {
    "verano": {"meses": [12, 1, 2], "factor_radiacion": 1.3},
    "invierno": {"meses": [6, 7, 8], "factor_radiacion": 0.7},
    "primavera": {"meses": [9, 10, 11], "factor_radiacion": 1.0},
    "otoño": {"meses": [3, 4, 5], "factor_radiacion": 1.0}
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

def fecha_a_dia_juliano(mes, dia):
    """
    Convierte mes y día a día juliano (1-365)
    Asumiendo año no bisiesto para simplificar
    """
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(dias_por_mes[:mes]) + dia

def dia_juliano_a_fecha(dia_juliano):
    """
    Convierte día juliano (1-365) a mes y día
    """
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mes = 1
    while dia_juliano > dias_por_mes[mes + 1]:
        dia_juliano -= dias_por_mes[mes]
        mes += 1
    return mes, dia_juliano

def calcular_ecuacion_del_tiempo(dia_juliano):
    """
    Calcula la ecuación de tiempo en minutos para un día juliano dado
    """
    # Aproximación simplificada
    b = (dia_juliano - 81) * 0.0172
    eot = 9.87 * math.sin(2*b) - 7.53 * math.cos(b) - 1.5 * math.sin(b)
    return eot  # minutos

def calcular_declinacion_solar(dia_juliano):
    """
    Calcula la declinación solar en grados para un día juliano dado
    """
    # Fórmula de Cooper (simplificada)
    declinacion = 23.45 * math.sin(math.radians(360 * (284 + dia_juliano) / 365))
    return declinacion

def calcular_angulo_horario(hora_decimal, longitud_grados, zona_horaria, eot_minutos):
    """
    Calcula el ángulo horario en grados
    """
    # Hora solar verdadera
    hora_solar = hora_decimal + (longitud_grados / 15) - zona_horaria - (eot_minutos / 60)
    angulo_horario = (hora_solar - 12) * 15  # 15 grados por hora
    return angulo_horario

def calcular_altitud_senal(latitud, declinacion, angulo_horario):
    """
    Calcula la altura solar en grados
    """
    lat_rad = math.radians(latitud)
    dec_rad = math.radians(declinacion)
    h_rad = math.radians(angulo_horario)

    sin_altura = (math.sin(lat_rad) * math.sin(dec_rad) +
                  math.cos(lat_rad) * math.cos(dec_rad) * math.cos(h_rad))
    altura = math.degrees(math.asin(max(-1, min(1, sin_altura))))
    return max(0, altura)  # No negativo (por debajo del horizonte)

def calcular_azimut_solar(latitud, declinacion, angulo_horario, altura):
    """
    Calcula el azimut solar en grados (desde el norte, sentido horario)
    """
    lat_rad = math.radians(latitud)
    dec_rad = math.radians(declinacion)
    h_rad = math.radians(angulo_horario)
    alt_rad = math.radians(altura)

    cos_azimut = (math.sin(dec_rad) - math.sin(lat_rad) * math.sin(alt_rad)) / \
                 (math.cos(lat_rad) * math.cos(alt_rad))

    # Limitar para evitar errores de dominio
    cos_azimut = max(-1, min(1, cos_azimut))
    azimut_rad = math.acos(cos_azimut)

    # Determinar el cuadrante basado en el ángulo horario
    if math.sin(h_rad) > 0:  # Tarde
        azimut_grados = math.degrees(2*math.pi - azimut_rad)
    else:  # Mañana
        azimut_grados = math.degrees(azimut_rad)

    return azimut_grados

def calcular_radiacion_extraterrestre(dia_juliano):
    """
    Calcula la radiación extraterrestre en W/m²
    """
    # Factor de corrección de distancia terrestre-solar
    r = 1 + 0.033 * math.cos(math.radians(360 * dia_juliano / 365))
    # Constante solar
    sc = 1367  # W/m2
    # Radiación extraterrestre
    ext_rad = sc * r
    return ext_rad

def estimar_radiacion_global_horizontal(radiacion_extraterrestre, altitud_solar,
                                      turbidez=0.3, albedo=0.2):
    """
    Estima la radiación global horizontal usando modelo simplificado de Liu & Jordan
    """
    if altitud_solar <= 0:
        return 0

    # Masa óptica relativa
    m = 1 / (math.sin(math.radians(altitud_solar)) + 0.15 * (altitud_solar + 3.885)**(-1.253))

    # Transmisividad atmosférica (modelo simplificado)
    tau_b = 0.7 ** (m ** 0.678)  # componente directo
    tau_d = 0.1 * (1 - tau_b)    # componente difuso (aproximado)

    # Componentes
    ih = radiacion_extraterrestre * math.sin(math.radians(altitud_solar)) * tau_b  # directo
    dh = radiacion_extraterrestre * 0.5 * (1 - math.cos(math.radians(90))) * tau_d  # difuso (aprox)
    gh = albedo * (ih + dh)  # reflejado del suelo

    return ih + dh + gh

def calcular_iluminancia_desde_radiacion(radiacion_horizontal, eficiencia_luminosa=105):
    """
    Convierte radiación solar (W/m2) a iluminancia (lux)
    Factor típico: 105 lm/W para radiación solar
    """
    return radiacion_horizontal * eficiencia_luminosa

def calcular_factor_iluminacion_diurna(altitud_solar, azimut_solar,
                                    orientacion_fachada, azimut_fachada):
    """
    Calcula el Factor de Iluminación Diurna (FID) simplificado
    """
    # Ángulo de incidencia
    cos_incidencia = (math.sin(math.radians(altitud_solar)) *
                     math.cos(math.radians(90 - altitud_solar)) *
                     math.cos(math.radians(azimut_solar - azimut_fachada)) +
                     math.cos(math.radians(altitud_solar)) *
                     math.sin(math.radians(90 - altitud_solar)) *
                     math.sin(math.radians(azimut_solar - azimut_fachada)))

    cos_incidencia = max(0, min(1, cos_incidencia))  # Solo considerar luz incidente

    # FID simplificado (en realidad depende de muchos factores más)
    fid_base = 0.1 * cos_incidencia  # Valor típico para ventana vertical
    fid_cielo = 0.05  # Componente cielo siempre presente
    fid_reflejo = 0.02 * CONFIGURACION_POR_DEFECTO["reflejo_suelo_por_defecto"]  # Suelo

    return min(1.0, fid_base + fid_cielo + fid_reflejo)

# ============================================================
# CLASES DE ANÁLISIS
# ============================================================

class AnalizadorRadiacionSolar:
    """Clase para análisis de radiación solar"""

    def __init__(self, latitud, longitud, zona_horaria):
        self.latitud = latitud
        self.longitud = longitud
        self.zona_horaria = zona_horaria

    def analizar_radiacion_horizontal(self, dia_juliano, hora_decimal):
        """
        Analiza radiación solar horizontal para un momento específico
        """
        # Calculos astronómicos
        declinacion = calcular_declinacion_solar(dia_juliano)
        eot = calcular_ecuacion_del_tiempo(dia_juliano)
        angulo_horario = calcular_angulo_horario(hora_decimal, self.longitud,
                                               self.zona_horaria, eot)
        altitud = calcular_altitud_senal(self.latitud, declinacion, angulo_horario)
        azimut = calcular_azimut_solar(self.latitud, declinacion, angulo_horario, altitud)

        # Radiación
        radiacion_ext = calcular_radiacion_extraterrestre(dia_juliano)
        radiacion_gh = estimar_radiacion_global_horizontal(
            radiacion_ext, altitud,
            turbidez=0.3,  # Valor típico urbano
            albedo=CONFIGURACION_POR_DEFECTO["reflejo_suelo_por_defecto"]
        )

        # Iluminancia
        iluminancia = calcular_iluminancia_desde_radiacion(radiacion_gh)

        return {
            "dia_juliano": dia_juliano,
            "hora_decimal": hora_decimal,
            "declinacion_grados": declinacion,
            "ecuacion_tiempo_min": eot,
            "angulo_horario_grados": angulo_horario,
            "altitud_solar_grados": altitud,
            "azimut_solar_grados": azimut,
            "radiacion_extraterrestre_wm2": radiacion_ext,
            "radiacion_global_horizontal_wm2": radiacion_gh,
            "iluminancia_lux": iluminancia,
            "condicion_dia": altitud > 0  # True si es de día
        }

    def analizar_radiacion_superficie(self, dia_juliano, hora_decimal,
                                    azimuth_superficie, inclinacion_superficie):
        """
        Analiza radiación en una superficie específica
        """
        # Obtener posición solar
        resultado_base = self.analizar_radiacion_horizontal(dia_juliano, hora_decimal)

        if not resultado_base["condicion_dia"]:
            resultado_base.update({
                "radiacion_directa_wm2": 0,
                "radiacion_difusa_wm2": 0,
                "radiacion_reflejada_wm2": 0,
                "radiacion_total_wm2": 0,
                "coseno_angulo_incidencia": 0,
                "iluminancia_directa_lux": 0,
                "iluminancia_total_lux": 0
            })
            return resultado_base

        # Calcular cosenos del ángulo de incidencia
        # Convertir a radianes
        alt_rad = math.radians(resultado_base["altitud_solar_grados"])
        az_solar_rad = math.radians(resultado_base["azimut_solar_grados"])
        az_sup_rad = math.radians(azimuth_superficie)
        inc_sup_rad = math.radians(inclinacion_superficie)

        # Coseno del ángulo de incidencia
        cos_theta = (math.sin(alt_rad) * math.cos(inc_sup_rad) *
                    math.cos(az_solar_rad - az_sup_rad) +
                    math.cos(alt_rad) * math.sin(inc_sup_rad) *
                    math.sin(az_solar_rad - az_sup_rad))

        cos_theta = max(0, cos_theta)  # Solo considerar radiación incidente

        # Componentes de radiación
        rad_ext = resultado_base["radiacion_extraterrestre_wm2"]

        # Modelo semplificado de componentes
        # Directo: proporción al coseno del ángulo de incidencia
        rad_directa = rad_ext * 0.7 * max(0, math.cos(math.radians(resultado_base["altitud_solar_grados"]))) * cos_theta
        # Difuso: isotropic desde cielo
        rad_difusa = rad_ext * 0.3 * 0.5  # Aproximado
        # Reflejado: desde suelo
        reflejado = (rad_directa + rad_difusa) * CONFIGURACION_POR_DEFECTO["reflejo_suelo_por_defecto"] * max(0, math.cos(math.radians(180 - inclinacion_superficie))) / 2

        rad_total = rad_directa + rad_difusa + reflejado

        # Iluminancia (usando mismo factor de conversión)
        ilum_directa = calcular_iluminancia_desde_radiacion(rad_directa)
        ilum_total = calcular_iluminancia_desde_radiacion(rad_total)

        resultado_base.update({
            "azimut_superficie_grados": azimuth_superficie,
            "inclinacion_superficie_grados": inclinacion_superficie,
            "coseno_angulo_incidencia": cos_theta,
            "radiacion_directa_wm2": rad_directa,
            "radiacion_difusa_wm2": rad_difusa,
            "radiacion_reflejada_wm2": reflejado,
            "radiacion_total_wm2": rad_total,
            "iluminancia_directa_lux": ilum_directa,
            "iluminancia_difusa_lux": calcular_iluminancia_desde_radiacion(rad_difusa),
            "iluminancia_reflejada_lux": calcular_iluminancia_desde_radiacion(reflejado),
            "iluminancia_total_lux": ilum_total
        })

        return resultado_base

class AnalizadorIluminanciaNatural:
    """Clase para análisis de iluminancia natural"""

    def __init__(self, latitud, longitud, zona_horaria):
        self.latitud = latitud
        self.longitud = longitud
        self.zona_horaria = zona_horaria
        self.analizador_radiacion = AnalizadorRadiacionSolar(latitud, longitud, zona_horaria)

    def analizar_punto_iluminancia(self, dia_juliano, hora_decimal,
                                 punto_observacion, ventana_datos,
                                 materiales_interior=None):
        """
        Analiza iluminancia en un punto específico debido a luz natural
        """
        if materiales_interior is None:
            materiais_interior = {
                "reflejo_pared": 0.5,
                "reflejo_techo": 0.7,
                "reflejo_suelo": 0.2
            }

        # Obtener radiación solar básica
        resultado_solar = self.analizador_radiacion.analizar_radiacion_superficie(
            dia_juliano, hora_decimal,
            ventana_datos.get("azimut", 0),
            ventana_datos.get("inclinacion", 90)  # Vertical por defecto
        )

        if not resultado_solar["condicion_dia"]:
            return {
                "iluminancia_total_lux": 0,
                "iluminancia_cielo_lux": 0,
                "iluminancia_sol_directo_lux": 0,
                "iluminancia_reflejada_lux": 0,
                "factor_iluminacion_diurna": 0,
                "cumple_estandar_minimo": False
            }

        # Calcular iluminancia directa del sol
        angulo_incidencia = math.degrees(math.acos(max(-1, min(1, resultado_solar["coseno_angulo_incidencia"]))))
        factores_sombra = 1.0 if angulo_incidencia < 90 else 0.0  # Simplificado

        ilum_directo_sol = resultado_solar["iluminancia_directa_luz"] * factores_sombra

        # Iluminancia del cielo (modelo simplificado)
        # En realidad, esto dependería de modelos de cielo complejos
        fraccion_cielo_visible = 0.3  # Valor típico para ventana vertical
        ilum_cielo = resultado_solar["iluminancia_difusa_luz"] * fraccion_cielo_visible

        # Iluminancia reflejada de superficies internas
        illuminancia_interna = (
            ilum_directo_sol * materiales_interior["reflejo_pared"] * 0.3 +
            ilum_cielo * materiales_interior["reflejo_techo"] * 0.2 +
            (ilum_directo_sol + ilum_cielo) * materiales_interior["reflejo_suelo"] * 0.1
        )

        # Iluminancia total en el punto
        ilum_total = ilum_directo_sol + ilum_cielo + illuminancia_interna

        # Factor de Iluminación Diurna (FID)
        illuminancia_exterior_horizontal = resultado_solar["iluminancia_directa_luz"] + \
                                         resultado_solar["iluminancia_difusa_luz"]
        fid = (ilum_total / illuminancia_exterior_horizontal * 100) if illuminancia_exterior_horizontal > 0 else 0

        # Verificación contra estándares (300 lux mínimo para áreas de trabajo)
        cumple_estandar = ilum_total >= CONFIGURACION_POR_DEFECTO["nivel_iluminancia_minimo"]

        return {
            "dia_juliano": dia_juliano,
            "hora_decimal": hora_decimal,
            "punto_observacion": punto_observacion,
            "iluminancia_directa_sol_lux": ilum_directo_sol,
            "iluminancia_cielo_lux": ilum_cielo,
            "iluminancia_reflejada_lux": illuminancia_interna,
            "iluminancia_total_lux": ilum_total,
            "factor_iluminacion_diurna": fid,
            "cumple_estandar_minimo": cumpl_estandar,
            "condiciones_cielo": "despejado",  # Simplificado
            "angulo_incidencia_sol": angulo_incidencia
        }

    def analizar_fidelidad_color(self, temperatura_color_cielo):
        """
        Analiza la fidelidad de color de la luz natural (CRI aproximado)
        """
        # La luz solar directa tiene CRI ~100
        # La luz difusa de cielo tiene CRI ligeramente menor
        if temperatura_color_cielo >= 5000:  # Luz más azulada (mazana)
            cri_estimado = 95
        elif temperatura_color_cielo >= 4000:  # Luz blanca neutra
            cri_estimado = 98
        else:  # Luz más amarillenta (atardecer/amanecer)
            cri_estimado = 92

        return cri_estimado

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():
    """
    Función principal que ejecuta análisis ambiental con Ladyboy
    """

    print("=== LADYBUG_ANALISIS_v02 - Análisis Ambiental ===")

    if not RHINO_AVAILABLE:
        print("ADVERTENCIA: Rhino/Grasshopper no disponible. Ejecutando en modo de prueba.")

    # Procesar entradas
    ladybug_entrada_json = None
    geometria_analisis = None
    analysis_type_str = "radiation"
    analysis_period_str = "annual"
    analysis_parameters = None
    output_format_str = "both"
    units_system_str = "metric"
    sky_model_str = "perez"
    ground_reflectance = 0.2
    include_sky_effect = True
    include_ground_reflection = True
    analysis_surface = None

    try:
        # Intentar obtener variables de entrada de Grasshopper
        if 'ladybug_entrada_json' in locals() and ladybug_entrada_json:
            if isinstance(ladybug_entrada_json, str):
                ladybug_entrada_json = json.loads(ladybug_entrada_json)
        else:
            # Crear datos de entrada de ejemplo si no se proporcionan
            ladybug_entrada_json = {
                "tipo_analisis": "radiation",
                "geometria": {
                    "limite_sitio": {
                        "tipo": "Polígono",
                        "coordenadas": [[0, 0, 0], [50, 0, 0], [50, 50, 0], [0, 50, 0], [0, 0, 0]]
                    }
                },
                "clima": {
                    "archivo_epw": "BRA_Bogota.Eldorado.803820_TMYx.epw",
                    "ciudad": "Bogotá",
                    "latitud": 4.7110,
                    "longitud": -74.0721,
                    "zona_horaria": -5
                }
            }
            print("Usando datos de entrada de ejemplo para análisis...")

        if 'geometria_analisis' in locals() and geometria_analisis is not None:
            if isinstance(geometria_analisis, str):
                try:
                    geometria_analisis = json.loads(geometria_analisis)
                except:
                    geometria_analisis = None
        else:
            geometria_analisis = {"tipo": "punto", "coordenadas": [25, 25, 1.5]}

        if 'analysis_type' in locals() and analysis_type:
            analysis_type_str = analysis_type.lower().strip()
        else:
            analysis_type_str = "radiation"

        if 'analysis_period' in locals() and analysis_period:
            analysis_period_str = analysis_period.lower().strip()
        else:
            analysis_period_str = "annual"

        if 'analysis_parameters' in locals() and analysis_parameters:
            if isinstance(analysis_parameters, str):
                try:
                    analysis_parameters = json.loads(analysis_parameters)
                except:
                    analysis_parameters = {}
        else:
            analysis_parameters = {}

        if 'output_format' in locals() and output_format:
            output_format_str = output_format.lower().strip()
        else:
            output_format_str = "both"

        if 'units_system' in locals() and units_system:
            units_system_str = units_system.lower().strip()
        else:
            units_system_str = "metric"

        if 'sky_model' in locals() and sky_model:
            sky_model_str = sky_model.lower().strip()
        else:
            sky_model_str = "perez"

        if 'ground_reflectance' in locals() and ground_reflectance is not None:
            ground_reflectance = safe_float(ground_reflectance, 0.2)
        else:
            ground_reflectance = 0.2

        if 'include_sky_effect' in locals() and include_sky_effect is not None:
            if isinstance(include_sky_effect, str):
                include_sky_effect = include_sky_effect.lower() in ['true', '1', 'yes']
            else:
                include_sky_effect = bool(include_sky_effect)
        else:
            include_sky_effect = True

        if 'include_ground_reflection' in locals() and include_ground_reflection is not None:
            if isinstance(include_ground_reflection, str):
                include_ground_reflection = include_ground_reflection.lower() in ['true', '1', 'yes']
            else:
                include_ground_reflection = bool(include_ground_reflection)
        else:
            include_ground_reflection = True

        if 'analysis_surface' in locals() and analysis_surface is not None:
            if isinstance(analysis_surface, str):
                try:
                    analysis_surface = json.loads(analysis_surface)
                except:
                    analysis_surface = None
        else:
            analysis_surface = None

    except Exception as e:
        print(f"Advertencia: Error procesando entradas: {e}. Usando valores por defecto.")

    # Validar y normalizar entradas
    try:
        analysis_type = TipoAnalisis(analysis_type_str)
    except ValueError:
        analysis_type = TipoAnalisis.RADIACION_SOLAR
        print(f"Tipo de análisis no válido: {analysis_type_str}. Usando: {analysis_type.value}")

    try:
        analysis_period = PeriodoAnalisis(analysis_period_str)
    except ValueError:
        analysis_period = PeriodoAnalisis.ANNUAL
        print(f"Período de análisis no válido: {analysis_period_str}. Usando: {analysis_period.value}")

    try:
        sky_model = ModeloCielo(sky_model_str)
    except ValueError:
        sky_model = ModeloCielo.PEREZ
        print(f"Modelo de cielo no válido: {sky_model_str}. Usando: {sky_model.value}")

    try:
        units_system = SistemaUnidades(units_system_str)
    except ValueError:
        units_system = SistemaUnidades.METRICO
        print(f"Sistema de unidades no válido: {units_system_str}. Usando: {units_system.value}")

    # Información del sitio desde los datos de entrada
    ciudad_info = ladybug_entrada_json.get("clima", {})
    latitud = ciudad_info.get("latitud", 4.7110)  # Bogotá por defecto
    longitud = ciudad_info.get("longitud", -74.0721)
    zona_horaria = ciudad_info.get("zona_horaria", -5)
    ciudad_nombre = ciudad_info.get("ciudad", "Desconocida")

    print(f"Analizando sitio: {ciudad_nombre}")
    print(f"Coordenadas: {latitud:.4f}° lat, {longitud:.4f}° lon")
    print(f"Tipo de análisis: {analysis_type.value}")
    print(f"Período de análisis: {analysis_period.value}")
    print(f"Modelo de cielo: {sky_model.value}")
    print(f"Sistema de unidades: {units_system.value}")

    # Inicializar analizadores
    analizador_radiacion = AnalizadorRadiacionSolar(latitud, longitud, zona_horaria)
    analizador_iluminancia = AnalizadorIluminanciaNatural(latitud, longitud, zona_horaria)

    # Determinar fechas de análisis basada en el período
    fechas_analisis = []

    if analysis_period == PeriodoAnalisis.ANNUAL:
        # Anual: representar cada mes
        for mes in range(1, 13):
            dia, _ = dia_juliano_a_fecha(fecha_a_dia_juliano(mes, 15))  # Medio de cada mes
            fechas_analisis.append((mes, dia, f"{mes}/15"))
    elif analysis_period == PeriodoAnalisis.SUMMER:
        # Verano en hemisferio sur: diciembre, enero, febrero
        for mes in [12, 1, 2]:
            dia, _ = dia_juliano_a_fecha(fecha_a_dia_juliano(mes, 15))
            fechas_analisis.append((mes, dia, f"{mes}/15"))
    elif analysis_period == PeriodoAnalisis.WINTER:
        # Invierno en hemisferio sur: junio, julio, agosto
        for mes in [6, 7, 8]:
            dia, _ = dia_juliano_a_fecha(fecha_a_dia_juliano(mes, 15))
            fechas_analisis.append((mes, dia, f"{mes}/15"))
    elif analysis_period == PeriodoAllocations.MONTHLY:
        # Análisis mensual detallado (todos los días de un mes representativo)
        mes_representativo = 6  # Junio como ejemplo
        dias_en_mes = 30  # Aproximación
        for dia in range(1, min(dias_en_mes + 1, 32)):  # Máximo 31 días
            fechas_analisis.append((mes_representativo, dia, f"{mes_representativo}/{dia}"))
    elif analysis_period == PeriodoAnalisis.HOURLY:
        # Análisis horario de un día representativo
        mes_dia = 6  # Junio
        dia = 21  # Solsticio de invierno (hemisferio sur)
        horas = [0, 6, 9, 12, 15, 18, 21]  # Muestras cada 3 horas
        fechas_analisis = [(mes_dia, dia, h) for h in horas]
        # El formato será manejado diferente en el bucle
    else:
        # Por defecto, algunos puntos representativos
        fechas_analisis = [
            (3, 20, "Equinoccio de marzo"),
            (6, 21, "Solsticio de junio"),
            (9, 22, "Equinoccio de septiembre"),
            (12, 21, "Solsticio de diciembre")
        ]

    # Datos de superficie de análisis (si se proporciona)
    superficie_default = {
        "azimut": 0,      # Hacia el norte
        "inclinacion": 90,  # Vertical
        "ancho": 5.0,     # metros
        "alto": 3.0       # metros
    }

    if analysis_surface and isinstance(analysis_surface, dict):
        superficie_analisis = {
            "azimut": analysis_surface.get("azimut", superficie_default["azimut"]),
            "inclinacion": analysis_surface.get("inclinacion", superficie_default["inclinacion"]),
            "ancho": analysis_surface.get("ancho", superficie_default["ancho"]),
            "alto": analysis_surface.get("alto", superficie_default["alto"])
        }
    else:
        superficie_analisis = superficie_default

    print(f"Superficie de análisis: azimut={superficie_analisis['azimut']}°, "
          f"inclinacion={superficie_analisis['inclinacion']}°")

    # Realizar análisis según el tipo solicitado
    resultados_detailed = []
    estadisticas_resumen = {
        "valores_maximos": {},
        "valores_minimos": {},
        "promedios": {},
        "totales": {},
        "conteos": {}
    }

    # Contadores para estadísticas
    total_puntos_analizados = 0
    sum_valores = {}
    count_valores = {}

    print(f"Iniciando análisis de {len(fechas_analisis)} períodos...")

    for fecha_info in fechas_analisis:
        if analysis_period == PeriodoAnalisis.HOURLY:
            mes, dia, hora_decimal = fecha_info
            fecha_label = f"{mes}/{dia} {hora_decimal:.0f}h"
        else:
            mes, dia, fecha_label = fecha_info
            hora_decimal = 12.0  # Mediodía por defecto para análisis diario

        # Convertir a día juliano
        dia_juliano = fecha_a_dia_juliano(int(mes), int(dia))

        # Ejecutar análisis según el tipo
        if analysis_type == TipoAnalisis.RADIACION_SOLAR:
            resultado = analizador_radiacion.analizar_radiacion_superficie(
                dia_juliano, hora_decimal,
                superficie_analisis["azimut"],
                superficie_analisis["inclinacion"]
            )

            # Extraer valores clave para estadísticas
            if "resultado" in locals():
                metrica_principal = resultado.get("radiacion_total_wm2", 0)
                metrica_nombre = "radiacion_total_wm2"
                unidad = "W/m²"

        elif analysis_type == TipoAnalisis.ILUMINACION_NATURAL:
            # Simular un punto de observación interno frente a la ventana
            punto_obs = [0, 0, 1.1]  # Un metro dentro, a altura de trabajo
            ventana_datos = {
                "azimut": superficie_analisis["azimut"],
                "inclinacion": superficie_analisis["inclinacion"],
                "ancho": superficie_analisis["ancho"],
                "alto": superficie_analisis["alto"]
            }

            resultado = analizador_iluminancia.analizar_punto_iluminancia(
                dia_juliano, hora_decimal,
                punto_obs, ventana_datos
            )

            if "resultado" in locals():
                metrica_principal = resultado.get("iluminancia_total_lux", 0)
                metrica_nombre = "iluminancia_total_lux"
                unidad = "lux"

        elif analysis_type == TipoAnalisis.TEMPERATURA_OPERATIVA:
            # Simulación simplificada de temperatura operativa
            # En realidad, esto requeriría datos de temperatura del aire, velocidad del viento, etc.
            resultado_solar = analizador_radiacion.analizar_radiacion_superficie(
                dia_juliano, hora_decimal,
                superficie_analisis["azimut"],
                superficie_analisis["inclinacion"]
            )

            # Modelo muy simplificado: temperatura base + ganancia solar
            temp_exterior_base = 15 + 10 * math.sin(math.radians(360 * (dia_juliano - 80) / 365))  # Variación anual simple
            ganancia_solar = resultado_solar.get("radiacion_total_wm2", 0) * 0.05  # Factor de ganancia
            temp_operativa = temp_exterior_base + ganancia_solar

            resultado = {
                "temperatura_operativa_c": temp_operativa,
                "temperatura_exterior_estimada_c": temp_exterior_base,
                "ganancia_solar_aprox_wm2": resultado_solar.get("radiacion_total_wm2", 0),
                "humedad_relativa_estimada": 60,  # Valor típico
                "velocidad_viento_estimada_ms": 2.0  # Valor típico
            }

            if "resultado" in locals():
                metrica_principal = resultado.get("temperatura_operativa_c", 0)
                metrica_nombre = "temperatura_operativa_c"
                unidad = "°C"

        elif analysis_type == TipoAnalisis.HUMEDAD_RELATIVA:
            # Para humedad relativa, usaríamos datos climáticos del EPW
            # Simulación basada en variación estacional simple
            humedad_base = 70  # Humedad anual promedio para Bogotá
            variacion_estacional = 10 * math.sin(math.radians(360 * (dia_juliano - 100) / 365))
            humedad_relativa = max(30, min(90, humedad_base + variacion_estacional))

            resultado = {
                "humedad_relativa_%": humedad_relativa,
                "humedad_absoluta_estimada_gm3": 8.07.0 * (humedad_relativa/100) * 6.112 * math.exp((17.67 * 15) / (15 + 243.5)) / (273.15 + 15),  # Simplificado
                "punto_de_rocio_estimado_c": 10.0  # Placeholder
            }

            if "resultado" in locals():
                metrica_principal = resultado.get("humedad_relativa_%", 0)
                metrica_nombre = "humedad_relativa_%"
                unidad = "%"

        elif analysis_type == TipoAnalisis.VELOCIDAD_VIENTO:
            # Simulación de velocidad del viento (en realidad vendría del EPW)
            velocidad_base = 3.0  # m/s promedio
            variacion_diaria = 2.0 * math.sin(math.radians(2 * math.pi * (hora_decimal - 6) / 12))  # Máxima por la tarde
            variacion_estacional = 1.0 * math.sin(math.radians(360 * (dia_juliano - 50) / 365))
            velocidad_viento = max(0, velocidad_base + variacion_diaria + variacion_estacional)

            resultado = {
                "velocidad_viento_ms": velocidad_viento,
                "direcion_viento_grados": 180 + 90 * math.sin(math.radians(360 * dia_juliano / 365)),  # Variable
                "rafaga_maxima_ms": velocidad_viento * 1.8,
                "condicion_cielo": "parcialmente_nublado"  # Placeholder
            }

            if "resultado" in locals():
                metrica_principal = resultado.get("velocidad_viento_ms", 0)
                metrica_nombre = "velocidad_viento_ms"
                unidad = "m/s"
        else:
            # Para otros tipos de análisis, usar resultado básido de radiación como placeholder
            resultado = analizador_radiacion.analizar_radiacion_superficie(
                dia_juliano, hora_decimal,
                superficie_analisis["azimut"],
                superficie_analisis["inclinacion"]
            )
            if "resultado" in locals():
                metrica_principal = resultado.get("radiacion_total_wm2", 0)
                metrica_nombre = "valor_analisis"
                unidad = "unidades"

        # Agregar metadatos comunes al resultado
        resultado.update({
            "fecha": fecha_label,
            "dia_juliano": dia_juliano,
            "mes": int(mes),
            "dia_del_mes": int(dia),
            "hora_decimal": hora_decimal if not (isinstance(hora_decimal, str) and '/' in hora_decimal) else 12.0,
            "tipo_analisis": analysis_type.value,
            "periodo_analisis": analysis_period.value
        })

        resultados_detailed.append(resultado)
        total_puntos_analizados += 1

        # Acumular para estadísticas
        if isinstance(metrica_principal, (int, float)) and not (isinstance(metrica_principal, bool)):
            if metrica_nombre not in sum_valores:
                sum_valores[metrica_nombre] = 0
                count_valores[metrica_nombre] = 0

            sum_valores[metrica_nombre] += metrica_principal
            count_valores[metrica_nombre] += 1

            # Actualizar min/max
            if metrica_nombre not in estadisticas_resumen["valores_maximos"] or \
               metrica_principal > estadisticas_resumen["valores_maximos"][metrica_nombre]:
                estadisticas_resumen["valores_maximos"][metrica_nombre] = metrica_principal

            if metrica_nombre not in estadisticas_resumen["valores_minimos"] or \
               metrica_principal < estadisticas_resumen["valores_minimos"][metrica_nombre]:
                estadisticas_resumen["valores_minimos"][metrica_nombre] = metrica_principal

    # Calcular promedios
    for metrica_nombre in sum_valores:
        if count_valores[metrica_nombre] > 0:
            estadisticas_resumen["promedios"][metrica_nombre] = sum_valores[metrica_nombre] / count_valores[metrica_nombre]

    # Totales (para magnitudes acumulativas como energía)
    for metrica_nombre in sum_valores:
        if "radiacion" in metrica_nombre.lower() or "energia" in metrica_nombre.lower():
            # Asumiendo que estos son valores instantáneos, convertiría a energía acumulando
            # Para simplificación, los tratamos como promedios diarios multiplicados por días
            dias_periodo = len(fechas_analisis) if analysis_period != [PeriodoAnalisis.HOURLY] else len(fechas_analisis)/24.0
            factor_tiempo = 24.0  # horas por día
            if analysis_period == [PeriodoAnalisis.HOURLY]:
                factor_tiempo = 1.0  # Ya son horarios

            energia_estimada = sum_valores[metrica_nombre] * dias_periodo * (factor_tiempo / 1000)  # Convertir a kWh/m2
            estadisticas_resumen["totales"][f"{metrica_nombre}_kwhm2"] = energia_estimada

    # Preparar resultados finales
    print("Compilando resultados...")

    resultados_completos = {
        "metadata": {
            "version": "2.0.0",
            "fecha_analisis": datetime.now().isoformat(),
            "tipo_analisis": analysis_type.value,
            "periodo_analisis": analysis_period.value,
            "modelo_cielo": sky_model.value,
            "sistema_unidades": units_system.value,
            "lugar": {
                "ciudad": ciudad_nombre,
                "latitud": latitud,
                "longitud": longitud,
                "zona_horaria": zona_horaria
            },
            "parametros_entrada": {
                "ground_reflectance": ground_reflectance,
                "include_sky_effect": include_sky_effect,
                "include_ground_reflection": include_ground_reflection,
                "superficie_analisis": superficie_analisis,
                "parametros_adicionales": analysis_parameters
            },
            "estadisticas_ejecucion": {
                "puntos_analizados": total_puntos_analizados,
                "periodos_temporales": len(fechas_analisis),
                "superficie_analisis_m2": superficie_analisis["ancho"] * superficie_analisis["alto"]
            }
        },
        "resultados_detallados": resultados_detailed,
        "estadisticas_resumen": {
            "resumen_numerico": estadisticas_resumen,
            "interpretacion": self._generar_interpretacion_resultados(analysis_type, estadisticas_resumen, unidades_map.get(metrica_nombre, "unidades")),
            "tendencias": self._analizar_tendencias(resultados_detailed, metrica_nombre)
        },
        "informacion_calidad": {
            "nivel_confianza": "estimado",  # En una implementación real, esto sería basado en calidad de datos EPW
            "limitaciones": [
                "Modelos simplificados de radiación y iluminación",
                "No incluye efectos de ubicación urbana específica (sombras de edificios cercanos)",
                "Asumiendo cielo despejado para cálculos de iluminancia",
                "Datos meteorológicos basado en clima típico, no año específico"
            ],
            "supuestos": [
                f"Reflectancia del suelo: {ground_reflectance}",
                f"Modelo de cielo: {sky_model.value}",
                "Orientación de superficie según especificación",
                "Condiciones atmosféricas promedio」
            ]
        }
    }

    # Generar visualizaciones (como datos en base64 de gráficos simples)
    visualizaciones = self._generar_visualizaciones_basicas(
        resultados_detailed,
        analysis_type,
        metrica_nombre,
        unidad
    )

    resultados_completos["visualizaciones"] = visualizaciones

    # Preparar datos para posible uso en Honeybee (si es análisis energético)
    datos_honeybee = None
    if analysis_type in [TipoAnalisis.RADIACION_SOLAR, TipoAnalisis.TEMPERATURA_OPERATIVA]:
        datos_honeybee = self._preparar_datos_honeybee(
            resultados_detailed,
            analysis_type,
            estadisticas_resumen,
            ciudad_info
        )

    # Generar reporte de texto
    reporte_texto = self._generar_reporte_texto(
        resultados_completos,
        analysis_type,
        analysis_period,
        ciudad_nombre
    )

    # Convertir a JSON para salida
    resultados_json = json.dumps(resultados_completos, indent=2, ensure_ascii=False)
    estadisticas_json = json.dumps(estadisticas_resumen, indent=2, ensure_ascii=False)
    honeybee_json = json.dumps(datos_honeybee, indent=2, ensure_ascii=False) if datos_honeybee else json.dumps({"error": "No aplicable para este tipo de análisis"}, indent=2, ensure_ascii=False)

    print("\n=== RESUMEN DE ANÁLISIS ===")
    print(f"Puntos analizados: {total_puntos_analizados}")
    if "promedios" in estadisticas_resumen and metrica_nombre in estadisticas_resumen["promedios"]:
        valor_promedio = estadisticas_resumen["promedios"][metrica_nombre]
        print(f"Valor promedio de {metrica_nombre}: {valor_promedio:.2f} {unidad}")
    print(f"Período analizado: {analysis_period.value}")
    if análisis_type == TipoAnalisis.RADIACION_SOLAR:
        energia_total = estadisticas_resumen.get("totales", {}).get("radiacion_total_wm2_kwhm2", 0)
        print(f"Energía solar estimada: {energia_total:.2f} kWh/m²")

    # Guardar resultados en archivos
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    resultados_path = os.path.join(output_dir, "analisis_resultados.json")
    with open(resultados_path, 'w', encoding='utf-8') as f:
        f.write(resultados_json)

    estadisticas_path = os.path.join(output_dir, "analisis_estadisticas.json")
    with open(estadisticas_path, 'w', encoding='utf-8') as f:
        f.write(estadisticas_json)

    honeybee_path = os.path.join(output_dir, "datos_para_honeybee.json")
    with open(honeybee_path, 'w', encoding='utf-8') as f:
        f.write(honeybee_json)

    reporte_path = os.path.join(output_dir, "reporte_analisis.txt")
    with open(reporte_path, 'w', encoding='utf-8') as f:
        f.write(reporte_texto)

    # Para visualizaciones, en una implementación real guardaríamos los archivos de imagen
    # Por ahora, guardamos solo la metadata
    viz_path = os.path.join(output_dir, "visualizaciones_info.json")
    with open(viz_path, 'w', encoding='utf-8') as f:
        json.dump(visualizaciones, f, indent=2, ensure_ascii=False)

    print(f"\nArchivos guardados en: {output_dir}")
    print(f"  - analisis_resultados.json")
    print(f"  - analisis_estadisticas.json")
    print(f"  - datos_para_honeybee.json")
    print(f"  - reporte_analisis.txt")
    print(f"  - visualizaciones_info.json")

    # Asignar para salida de Grasshopper
    analisis_resultados = resultados_json
    analisis_visualizacion = json.dumps(visualizaciones)  # En realidad sería los datos de la imagen
    analisis_estadisticas = estadisticas_json
    reporte_analisis = reporte_texto
    datos_para_honeybee = honeybee_json

def _generar_interpretacion_resultados(self, tipo_analisis, estadisticas, unidad):
    """Genera una interpretación de los resultados estadísticos"""
    interpretaciones = {
        TipoAnalisis.RADIACION_SOLAR: "Análisis de radiación solar: valores altos indican buen potencial para captación solar pasiva y activa.",
        TipoAnalisis.ILUMINACION_NATURAL: "Análisis de iluminación natural: valores por encima de 300 lux cumplen con estándares mínimos para espacios de trabajo.",
        TipoAnalisis.TEMPERATURA_OPERATIVA: "Análisis de confort térmico: valores entre 20-26°C generalmente considerados confortables para actividad sedentaria.",
        TipoAnalisis.HUMEDAD_RELATIVA: "Análisis de humedad: valores entre 30-70% generalmente considerados confortables.",
        TipoAnalisis.VELOCIDAD_VIENTO: "Análisis de ventilación natural: valores entre 2-5 m/s adecuados para ventilación pasiva efficace."
    }

    base_interpretacion = interpretaciones.get(tipo_analisis, "Análisis completado exitosamente.")

    # Agregar interpretación estadística específica
    if "promedios" in estadisticas:
        # Obtener la primera métrica disponible para interpretación
        primera_metrica = None
        valor_promedio = None
        for metrica, valor in estadisticas["promedios"].items():
            if isinstance(valor, (int, float)):
                primera_metrica = metrica
                valor_promedio = valor
                break

        if primera_metrica and valor_promedio is not None:
            if tipo_analisis == TipoAnalisis.RADIACION_SOLAR:
                if valor_promedio > 250:
                    interpretacion_detallada = " Excelente recurso solar disponible."
                elif valor_promedio > 150:
                    interpretacion_detallada = " Buen recurso solar disponible."
                elif valor_promedio > 50:
                    interpretacion_detallada = " Recurso solar moderado disponible."
                else:
                    interpretacion_detallada = " Recurso solar limitado."
            elif tipo_analisis == TipoAnalisis.ILUMINACION_NATURAL:
                if valor_promedio > 500:
                    interpretacion_detallada = " Excelente iluminación natural disponible."
                elif valor_promedio > 300:
                    interpretacion_detallada = " Iluminación adecuada para tareas visuales."
                elif valor_promedio > 100:
                    interpretacion_detallada = " Iluminación suplementaria probablemente necesaria."
                else:
                    interpretacion_detallada = " Iluminación natural insuficiente para tareas visuales."
            else:
                interpretacion_detallada = f" Valor promedio registrado: {valor_promedio:.2f} {unidad}."

            return base_interpretacion + interpretacion_detallada

    return base_interpretacion

def _analizar_tendencias(self, resultados_detallados, metrica_nombre):
    """Analiza tendencias temporales en los resultados"""
    if len(resultados_detallados) < 3:
        return {"tendencia": "insuficientes_datos", "descripcion": "Se necesitan al menos 3 puntos para análisis de tendencia"}

    # Extraer valores numéricos de la métrica de interés
    valores = []
    tiempos = []

    for resultado in resultados_detallados:
        if isinstance(resultado.get(metrica_nombre), (int, float)) and not isinstance(resultado.get(metrica_nombre), bool):
            valores.append(float(resultado[metrica_nombre]))
            # Usar día juliano como proxy de tiempo
            tiempos.append(float(resultado.get("dia_juliano", 0)))

    if len(valores) < 3:
        return {"tendencia": "insuficientes_datos_validos", "descripcion": "Datos insuficientes para análisis de tendencia"}

    # Regresión lineal simple para detectar tendencia
    n = len(valores)
    sum_x = sum(tiempos)
    sum_y = sum(valores)
    sum_xy = sum(t * v for t, v in zip(tiempos, valores))
    sum_x2 = sum(t * t for t in tiempos)

    if n * sum_x2 - sum_x * sum_x == 0:
        pendiente = 0
    else:
        pendiente = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

    # Determinar direcccion de la tendencia
    if abs(pendiente) < 0.01:  # Umbral prácticamente nulo
        tendencia = "estable"
        descripcion = "Los valores se mantienen relativamente constantes a lo largo del período analizado."
    elif pendiente > 0:
        tendencia = "creciente"
        descripcion = f"Los valores muestran una tendencia creciente de {pendiente:.4f} unidades por día juliano."
    else:
        tendencia = "decreciente"
        descripcion = f"Los valores muestran una tendencia decreciente de {-pendiente:.4f} unidades por día juliano."

    # Calcular coeficiente de correlación simple
    mean_x = sum_x / n
    mean_y = sum_y / n
    numerator = sum((t - mean_x) * (v - mean_y) for t, v in zip(tiempos, valores))
    denominator = math.sqrt(sum((t - mean_x)**2 for t in tiempos) * sum((v - mean_y)**2 for v in valores))

    if denominator != 0:
        correlacion = numerator / denominator
        fuerza_correlacion = "fuerte" if abs(correlacion) > 0.7 else "moderada" if abs(correlacion) > 0.3 else "débil"
    else:
        correlacion = 0
        fuerza_correlacion = "nula"

    return {
        "tendencia": tendencia,
        "pendiente": pendiente,
        "descripcion": descripcion,
        "correlacion": correlacion,
        "fuerza_correlacion": fuerza_correlacion,
        "rango_valores": {
            "minimo": min(valores),
            "maximo": max(valores),
            "diferencia": max(valores) - min(valores)
        }
    }

def _generar_visualizaciones_basicas(self, resultados_detallados, tipo_analisis, metrica_nombre, unidad):
    """Genera metadata para visualizaciones básicas (en una implementación real, generaríamos las imágenes)"""

    # Extraer datos para graficar
    etiquetas = []
    valores = []

    for resultado in resultados_detallados:
        fecha = resultado.get("fecha", "unknown")
        valor = resultado.get(metrica_nombre)

        if isinstance(valor, (int, float)) and not isinstance(valor, bool):
            etiquetas.append(str(fecha))
            valores.append(float(valor))

    if not valores:
        return {"error": "No hay datos válidos para visualizar"}

    # Metadata de lo que sería la visualización
    visualizacion_meta = {
        "tipo_grafico": "linea_tiempo",
        "titulo": f"Análisis de {tipo_analisis.value.replace('_', ' ').title()}",
        "eje_x": "Tiempo",
        "eje_y": f"{metrica_nombre} ({unidad})",
        "puntos_datos": len(valores),
        "rango_valores": {
            "min": min(valores) if valores else 0,
            "max": max(valores) if valores else 0
        },
        "datos_para_graficar": {
            "etiquetas": etiquetas[:20],  # Limitar para no sobrecargar
            "valores": valores[:20]
        },
        "observaciones": [
            f"Se muestran los primeros {min(20, len(etiquetas))} puntos de {len(etiquetas)} totales",
            "En una implementación completa, esto sería un gráfico interactivo o imagen"
        ]
    }

    # Información adicional para tipos específicos
    if tipo_analisis == TipoAnalisis.RADIACION_SOLAR:
        visualizacion_meta["tipo_grafico"] = "radiacion_anual"
        visualizacion_meta["esquema_color"] = "amarillo_a_rojo"  # Baja a alta radiación
    elif tipo_analisis == TipoAnalisis.ILUMINACION_NATURAL:
        visualizacion_meta["tipo_grafico"] = "iluminancia_anual"
        visualizacion_meta["linea_referencia"] = 300  # Línea de referencia para iluminancia mínima
        visualizacion_meta["esquema_color"] = "azul_a_blanco"  # Baja a alta iluminancia
    elif tipo_analisis == TipoAnalisis.TEMPERATURA_OPERATIVA:
        visualizacion_meta["tipo_grafico"] = "temperatura_anual"
        visualizacion_meta["lineas_referencia"] = [20, 26]  # Rango de confort térmico
        visualizacion_meta["esquema_color"] = "azul_a_rojo"  # Frío a cálido

    return visualizacion_meta

def _preparar_datos_honeybee(self, resultados_detallados, tipo_analisis, estadisticas, ciudad_info):
    """Preparar datos que puedan ser usados por Honeybee para análisis energético"""
    if tipo_analisis not in [TipoAnalisis.RADIACION_SOLAR, TipoAnalisis.TEMPERATURA_OPERATIVA]:
        return {"mensaje": "Conversión a formato Honeybee no aplicable para este tipo de análisis"}

    # Extraer datos relevantes para Honeybee
    datos_hora = []
    valores_radiacion = []
    valores_temperatura = []

    for resultado in resultados_detallados:
        hora_decimal = resultado.get("hora_decimal", 12.0)
        dia_juliano = resultado.get("dia_juliano", 1)

        # Crear timestamp
        mes, dia_del_mes = dia_juliano_a_fecha(dia_juliano)
        timestamp = f"{mes:02d}/{dia_del_mes:02d} {int(hora_decimal):02d}:{int((hora_decimal % 1) * 60):02d}"

        datos_hora.append(timestamp)

        rad_valor = resultado.get("radiacion_total_wm2", 0)
        temp_valor = resultado.get("temperatura_operativa_c",
                                resultado.get("temperatura_exterior_estimada_c", 20))

        valores_radiacion.append(max(0, rad_valor))  # No negativo
        valores_temperatura.append(temp_valor)

    # Estructura de datos para Honeybee
    datos_honeybee = {
        "formato": "honeybee_loads_temperature",
        "version": "1.0",
        "metadatos": {
            "fuente": "LADYBUG_ANALISIS_v02",
            "fecha_generacion": datetime.now().isoformat(),
            "ciudad": ciudad_info.get("ciudad", "Desconocida"),
            "latitud": ciudad_info.get("latitud", 0.0),
            "longitud": ciudad_info.get("longitud", 0.0),
            "zona_horaria": ciudad_info.get("zona_horaria", 0),
            "paso_tiempo_horas": 1.0 if len(set([r.get("hora_decimal", 12) for r in resultados_detallados])) > 1 else 0.5
        },
        "datos_temporales": {
            "timestamps": datos_hora,
            "valores_radiacion_wm2": valores_radiacion,
            "valores_temperatura_c": valores_temperatura
        },
        "estadisticas_resumen": {
            "radiacion": {
                "promedio_wm2": sum(v for v in valores_radiacion if isinstance(v, (int, float))) / max(len([v for v in valores_radiacion if isinstance(v, (int, float))]), 1),
                "maximo_wm2": max(v for v in valores_radiacion if isinstance(v, (int, float))) if any(isinstance(v, (int, float)) for v in valores_radiacion) else 0,
                "minimo_wm2": min(v for v in valores_radiacion if isinstance(v, (int, float))) if any(isinstance(v, (int, float)) for v in valores_radiacion) else 0
            },
            "temperatura": {
                "promedio_c": sum(v for v in valores_temperatura if isinstance(v, (int, float))) / max(len([v for v in valores_temperatura if isinstance(v, (int, float))]), 1),
                "maximo_c": max(v for v in temperaturas if isinstance(v, (int, float))) if any(isinstance(v, (int, float)) for v in valores_temperatura) else 0,
                "minimo_c": min(v for v in temperaturas if isinstance(v, (int, float))) if any(isinstance(v, (int, float)) for v in valores_temperatura) else 0
            }
        },
        "nota": "Estos datos pueden ser importados a Honeybee como perfiles de carga térmica o radiación de fachada"
    }

    return datos_honeybee

def _generar_reporte_texto(self, resultados_completos, tipo_analisis, periodo_analisis, ciudad_nombre):
    """Genera un reporte de texto legible de los resultados del análisis"""

    lineas = [
        "=" * 80,
        f"INFORME DE ANÁLISIS AMBIENTAL CON LADYBUG - {tipo_analisis.value.upper()}",
        "=" * 80,
        f"Fecha del informe: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Ciudad analizada: {ciudad_nombre}",
        f"Tipo de análisis: {tipo_analisis.value.replace('_', ' ').title()}",
        f"Periodo de análisis: {periodo_analisis.value.title()}",
        f"Modelo de cielo utilizado: {resultado_completos['metadata']['modelo_cielo']}",
        "",
        "RESUMEN EJECUTIVO:",
        "-" * 40
    ]

    # Añadir estadísticas clave según tipo de análisis
    resumen = resultados_completos.get("estadisticas_resumen", {}).get("resumen_numerico", {})

    if tipo_analisis == TipoAnalisis.RADIACION_SOLAR:
        if "promedios" in resumen and "radiacion_total_wm2" in resumen["promedios"]:
            rad_prom = resumen["promedios"]["radiacion_total_wm2"]
            lineas.extend([
                f"• Radiación solar promedio: {rad_prom:.1f} W/m²",
                f"• Energía solar estimada: {resultados_completos['estadisticas_resumen'].get('totales', {}).get('radiacion_total_wm2_kwhm2', 0):.1f} kWh/m²/año",
                f"• Máximo registrado: {resumen.get('valores_maximos', {}).get('radiacion_total_wm2', 0):.1f} W/m²",
                f"• Mínimo registrado: {resumen.get('valores_minimos', {}).get('radiacion_total_wm2', 0):.1f} W/m²"
            ])

            # Interpretación
            if rad_prom > 250:
                linea_interpretacion = "Excelente recurso solar disponible - Alto potencial para sistemas solares pasivos y activos"
            elif rad_prom > 150:
                linea_interpretacion = "Buen recurso solar disponible - Potencial moderado para aplicaciones solares"
            elif rad_prom > 80:
                linea_interpretacion = "Recurso solar limitado - Considerar complementación con otras fuentes"
            else:
                linea_interpretacion = "Recurso solar muy limitado - Dependencia significativa de otras fuentes energéticas"

            lineas.append(f"• Interpretación: {linea_interpretacion}")

    elif tipo_analisis == TipoAnalisis.ILUMINACION_NATURAL:
        if "promedios" in resumen and "iluminancia_total_lux" in resumen["promedios"]:
            ilum_prom = resumen["promedios"]["iluminancia_total_lux"]
            lineas.extend([
                f"• Iluminancia promedio: {ilum_prom:.1f} lux",
                f"• Máximo registrado: {resumen.get('valores_maximos', {}).get('iluminancia_total_lux', 0):.1f} lux",
                f"• Mínimo registrado: {resumen.get('valores_minimos', {}).get('iluminancia_total_lux', 0):.1f} lux"
            ])

            # Porcentaje de tiempo cumpliendo con estándar
            # Esto requeriría análisis más detallado, pero aproximamos
            porcentaje_cumplimiento = min(100, max(0, (ilum_prom - 100) / 2))  # Aproximación muy básica
            lineas.append(f"• Tiempo estimado cumpliendo estándar mín. (300 lux): {porcentaje_cumplimiento:.0f}%")

            # Interpretación
            if ilum_prom >= 300:
                linea_interpretacion = "Iluminación natural adecuada para la mayoría de las tareas visuales"
            elif ilum_prom >= 150:
                linea_interpretacion = "Iluminación natural suplementaria probablemente necesaria en horas críticas"
            else:
                linea_interpretacion = "Iluminación natural insuficiente - Dependencia significativa de iluminación artificial"

            lineas.append(f"• Interpretación: {linea_interpretacion}")

    elif tipo_analisis == TipoAnalisis.TEMPERATURA_OPERATIVA:
        if "promedios" in resumen and "temperatura_operativa_c" in resumen["promedios"]:
            temp_prom = resumen["promedios"]["temperatura_operativa_c"]
            lineas.extend([
                f"• Temperatura operativa promedio: {temp_prom:.1f}°C",
                f"• Máximo registrado: {resumen.get('valores_maximos', {}).get('temperatura_operativa_c', 0):.1f}°C",
                f"• Mínimo registrado: {resumen.get('valores_minimos', {}).get('temperatura_operativa_c', 0):.1f}°C"
            ])

            # Horas fuera de rango de confort (estimado simplificado)
            horas_frias = max(0, (20 - temp_prom) * 2) if temp_prom < 20 else 0
            horas_calidas = max(0, (temp_prom - 26) * 2) if temp_prom > 26 else 0
            horas_desconfort = horas_frias + horas_calidas
            porcentaje_confort = max(0, 100 - (horas_desconfort / 24 * 100)) if horas_desconfort > 0 else 100

            lineas.extend([
                f"• Horas estimadas por debajo de 20°C: {horas_frias:.0f} h/día",
                f"• Horas estimadas por encima de 26°C: {horas_calidas:.0f} h/día",
                f"• Porcentaje estimado de tiempo en confort térmico: {porcentaje_confort:.0f}%"
            ])

            # Interpretación
            if 20 <= temp_prom <= 26:
                if horas_desconfort < 2:
                    linea_interpretacion = "Excelente confort térmico durante la mayor parte del tiempo"
                else:
                    linea_interpretacion = "Buen confort térmico con algunas variaciones estacionales"
            elif temp_prom < 20:
                linea_interpretacion = "Tendencia a temperaturas frescas - Considerar estrategias de calefacción pasiva"
            else:
                linea_interpretacion = "Tendencia a temperaturas cálidas - Considerar estrategias de enfriamiento pasivo"

            lineas.append(f"• Interpretación: {linea_interpretacion}")

    # Añadir información estadística general
    totales = resultados_completos.get("estadisticas_resumen", {}).get("totales", {})
    if totales:
        lineas.extend([
            "",
            "TOTALES ACUMULADOS:",
            "-" * 40
        ])
        for key, value in totales.items():
            if isinstance(value, (int, float)):
                unidad_display = "kWh/m²" if "kwhm2" in key else "unidades"
                lineas.append(f"• {key.replace('_', ' ').title()}: {value:.2f} {unidad_display}")

    # Añadir tendencias si están disponibles
    tendencia_info = resultados_completos.get("estadisticas_resumen", {}).get("tendencias", {})
    if tendencia_info and tendencia_info.get("tendencia") not in ["insuficientes_datos", "insuficientes_datos_validos"]:
        lineas.extend([
            "",
            "ANÁLISIS DE TENDENCIAS:",
            "-" * 40,
            f"Dirección de la tendencia: {tendencia_info.get('tendencia', 'desconocida').title()}",
            f"Descripción: {tendencia_info.get('descripcion', 'No disponible')}"
        ])

        if "correlacion" in tendencia_info:
            fuerza = tendencia_info.get("fuerza_correlacion", "desconocida")
            correlacion = tendencia_info.get("correlacion", 0)
            lineas.append(f"Correlación temporal: {correlacion:.3f} ({fuerza})")

    lineas.extend([
        "",
        "DETALLES TÉCNICOS:",
        "-" * 40,
        f"Puntos de datos analizados: {resultado_completos['metadata']['estadisticas_ejecucion']['puntos_analizados']}",
        f"Períodos temporales evaluados: {resultado_completos['metadata']['estadisticas_ejecucion']['periodos_temporales']}",
        f"Superficie de análisis: {resultado_completos['metadata']['estadisticas_ejecucion']['superficie_analisis_m2']:.1f} m²",
        "",
        "LIMITACIONES DEL ANÁLISIS:",
        "-" * 40
    ])

    limitaciones = resultados_completos.get("informacion_calidad", {}).get("limitaciones", [
        "Modelos simplificados utilizados para estimaciones rápidas",
        "No incluye efectos de sombras urbanas específicas del sitio",
        "Asumiendo condiciones atmosféricas promedio"
    ])

    for limit in limitaciones:
        lineas.append(f"• {limit}")

    lineas.extend([
        "",
        "SUPUESTOS DEL MODELO:",
        "-" * 40
    ])

    supuestos = resultados_completos.get("informacion_calidad", {}).get("supuestos", [
        f"Reflectancia del terreno asumida: {resultado_completos['metadata']['parametros_entrada']['ground_reflectance']}",
        f"Modelo de cielo utilizado: {resultado_completos['metadata']['modelo_cielo']}",
        "Condiciones meteorológicas basado en datos climáticos típicos (TMY)"
    ])

    for sup in supuestos:
        lineas.append(f"• {sup}")

    lineas.extend([
        "",
        "RECOMENDACIONES PARA DISEÑO:",
        "-" * 40
    ])

    # Generar recomendaciones según el tipo de análisis
    if tipo_analisis == TipoAnalisis.RADIACION_SOLAR:
        recomendaciones = [
            "Considerar orientación de fachada principal hacia el ecuador para máxima captación solar",
            "Evaluar instalación de sistemas fotovoltaicos en superficies con óptima orientación",
            "Implementar protección solar móvil en fachadas orientales y occidentales para controlar ganancia excesiva",
            "Explorar uso de materiales de alta inercia térmica para aprovechar ganancia solar diurna"
        ]
    elif tipo_analisis == TipoAnalisis.ILUMINACION_NATURAL:
        recomendaciones = [
            "Maximizar apertura de ventanas en fachadas norte y sur (hemisferio sur) para iluminación uniforme",
            "Considerar sistemas de protección solar móvil para controlar deslumbramiento",
            "Evaluar uso de repisas iluminadas para mejorar distribución de luz profunda",
            "Verificar que los puntos de trabajo críticos reciban iluminancia adecuada (>300 lux)"
        ]
    elif tipo_analisis == TipoAnalisis.TEMPERATURA_OPERATIVA:
        recomendaciones = [
            "Optimizar inercia térmica de la envolvente para amortiguar variaciones diarias",
            "Considerar estrategias de ventilación nocturna para enfriamiento en climas cálidos",
            "Evaluar uso de cortinería térmica en ventanas para reducir pérdidas ganancias no deseadas",
            "Diseñar sombreados que permitan ganancia solar en invierno pero la bloqueen en verano"
        ]
    else:
        recomendaciones = [
            "Considerar los resultados específicos del análisis en las decisiones de diseño",
            "Validar los hallazgos con mediciones in situ cuando sea posible",
            "Integrar los findings con otros análisis ambientales para un enfoque holístico"
        ]

    for rec in recomendaciones:
        lineas.append(f"• {rec}")

    lineas.extend([
        "",
        "PRÓXIMOS PASOS SUGERIDOS:",
        "-" * 40,
        "1. Validar resultados con herramientas de simulación más detalladas si es necesario",
        "2. Integrar hallazgos con análisis de consumo energético anual",
        "3. Considerar iteraciones de diseño basadas en las tendencias identificadas",
        "4. Documentar supuestos y limitaciones para el equipo de diseño y revisores",
        "5. Explorar estrategias de diseño pasivo basadas en los patrones identificados",
        "",
        "=" * 80
    ])

    return "\n".join(lineas)


# Ejecutar si se ejecuta como script principal
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error en LADYBUG_ANALISIS_v02: {str(e)}")
        import traceback
        traceback.print_exc()

        # Salida de error para Grasshopper
        error_result = {
            "error": str(e),
            "mensaje": "Error en el análisis ambiental con Ladybug"
        }
        analisis_resultados = json.dumps(error_result, indent=2, ensure_ascii=False)
        analisis_visualizacion = json.dumps({"error": "Visualización no disponible debido a error"})
        analisis_estadisticas = json.dumps({"error": "Estadísticas no disponibles debido a error"})
        reporte_analisis = f"ERROR: {str(e)}"
        datos_para_honeybee = json.dumps({"error": "Datos para Honeybee no disponibles debido a error"}, indent=2, ensure_ascii=False)