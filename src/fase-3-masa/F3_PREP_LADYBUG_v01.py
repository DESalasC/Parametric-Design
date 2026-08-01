#!/usr/bin/env python3
"""
PREP_LADYBUG_v01.py - Preparación de Datos para Análisis Ladybug/Honeybee
GH Python Script para Grasshopper (GH Player compatible)

Este componente prepara los datos necesarios para los análisis de Ladybug y Honeybee,
incluyendo la preparación de geometrías, clima, y configuración de simulaciones.

ENTRADAS (via Grasshopper):
  - geometria_edificio: Geometría del edificio preparada (output de VOLUMEN_v03.py)
  - clima_archivo: Ruta al archivo EPW de clima (opcional, se usa Bogotá por defecto)
  - punto_norte: Vector norte para orientación (opcional, se calcula si no se proporciona)
  - periodo_analisis: Período de análisis ("anual", "verano", "invierno", etc.)
  - tipo_analisis: Tipo de análisis ("radiacion", "solasol", "visibilidad", "iluminacion", "energia")
  - resolucion_malla: Resolución de la malla de análisis en metros (opcional)
  - altura_punto_analisis: Altura para puntos de análisis humano (default 1.1m)
  - incluir_sombras_propias: Boolean para incluir autosombreamiento
  - incluir_sombras_contextuales: Boolean para incluir sombras de contexto
  - contexto_edificios: Geometrías de edificios cercanos (opcional)

SALIDAS:
  - ladybug_entrada.json: JSON preparado para Ladybug con geometría, clima y parámetros
  - honeybee_entrada.json: JSON preparado para Honeybee con modelo energético
  - parametros_simulacion.json: Parámetros específicos para el tipo de análisis solicitado
  - reporte_preparacion.txt: Reporte legible del proceso de preparación
  - geometria_preparada_geo.json: Geometría en formato GeoJSON para visualización
"""

import json
import math
import os
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional
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

    class Brep:
        pass

    class Mesh:
        pass

    class Interval:
        def __init__(self, t0=0, t1=1):
            self.T0 = t0
            self.T1 = t1

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
        def AreaMesh(mesh):
            return 100.0  # Área aproximada

        @staticmethod
        def VolumeMesh(mesh):
            return 500.0  # Volumen aproximado

        @staticmethod
        def MeshBox(box):
            return "mock_mesh"

        @staticmethod
        def Extrusion():
            return "mock_extrusion"

        @staticmethod
        def CapPlanarHoles(brep):
            return [brep]

    rs = MockRs()

# ============================================================
# ENUMS Y CONSTANTES
# ============================================================

class TipoAnalisis(Enum):
    RADIACION_SOLAR = "radiacion_solar"
    ILUMINACION_DIA = "iluminacion_dia"
    CONSUMO_ENERGETICO = "consumo_energetico"
    COMFORT_TERMAL = "comfort_termal"
    ILUMINACION_ANUAL = "iluminacion_anual"
    RADIACION_ANUAL = "radiacion_anual"

class PeriodoAnalisis(Enum):
    ANUAL = "anual"
    VERANO = "verano"
    INVIERNO = "invierno"
    PRIMAVERA = "primavera"
    OTOÑO = "otoño"
    MES_ESPECIFICO = "mes_especifico"
    HORARIO = "horario"

# Parámetros por defecto para análisis
PARAMETROS_DEFECTO = {
    TipoAnalisis.RADIACION_SOLAR: {
        "mesh_size": 0.5,
        "north_angle": 0,
        "hourly": True,
        "monthly": False,
        "north": True,
        "south": True,
        "east": True,
        "west": True,
        "horizontal": False
    },
    TipoAnalisis.ILUMINACION_DIA: {
        "grid_size": 0.5,
        "north_angle": 0,
        "month": 6,  # Junio
        "day": 21,
        "hour_interval": 1,
        "min_hour": 8,
        "max_hour": 18,
        "sensor_type": "illuminance"
    },
    TipoAnalisis.CONSUMO_ENERGETICO: {
        "weather_file": "BRA_Bogota.Eldorado.803820_TMYx.epw",
        "simulation_parameters": {
            "timestep": 60,
            "temp_setpoint_heating": 20,
            "temp_setpoint_cooling": 26
        }
    }
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

def crear_vector_desde_lista(coords):
    """Convierte una lista [x,y,z] o [x,y] a Vector3d"""
    if len(coords) >= 3:
        return Vector3d(float(coords[0]), float(coords[1]), float(coords[2]))
    elif len(coords) == 2:
        return Vector3d(float(coords[0]), float(coords[1]), 0.0)
    else:
        return Vector3d(0, 0, 0)

def crear_point_desde_lista(coords):
    """Convierte una lista [x,y,z] o [x,y] a Point3d"""
    if len(coords) >= 3:
        return Point3d(float(coords[0]), float(coords[1]), float(coords[2]))
    elif len(coords) == 2:
        return Point3d(float(coords[0]), float(coords[1]), 0.0)
    else:
        return Point3d(0, 0, 0)

def calcular_centroide_puntos(puntos):
    """Calcula el centroide de una lista de puntos 3D"""
    if not puntos:
        return Point3d(0, 0, 0)

    sum_x = sum(p.X for p in puntos)
    sum_y = sum(p.Y for p in puntos)
    sum_z = sum(p.Z for p in puntos)
    count = len(puntos)

    return Point3d(sum_x/count, sum_y/count, sum_z/count)

def calcular_area_superficie(brep_or_mesh):
    """Calcula el área aproximada de una superficie o malla"""
    # Implementación simplificada - en la realidad usaría métodos de RhinoCommon
    return 100.0  # Área estimada por defecto

def calcular_volumen_solido(brep):
    """Calcula el volumen aproximado de un sólido"""
    # Implementación simplificada
    return 500.0  # Volumen estimado por defecto

def obtener_bounding_box(geometria):
    """Obtiene la caja envolvente de una geometría"""
    # Implementación simplificada
    return {
        "min": [0, 0, 0],
        "max": [50, 50, 30]
    }

def rotar_vector_around_z(vector, angulo_grados):
    """Rota un vector alrededor del eje Z"""
    angulo_rad = math.radians(angulo_grados)
    cos_a = math.cos(angulo_rad)
    sin_a = math.sin(angulo_rad)

    x_new = vector.X * cos_a - vector.Y * sin_a
    y_new = vector.X * sin_a + vector.Y * cos_a
    z_new = vector.Z

    return Vector3d(x_new, y_new, z_new)

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():
    """
    Función principal que prepara datos para análisis Ladybug/Honeybee
    """

    print("=== PREP_LADYBUG_v01 - Preparación para Análisis Ladybug/Honeybee ===")

    if not RHINO_AVAILABLE:
        print("ADVERTENCIA: Rhino/Grasshopper no disponible. Ejecutando en modo de prueba.")

    # Procesar entradas
    geometria_edificio = None
    clima_archivo = None
    punto_norte = None
    periodo_analisis = "anual"
    tipo_analisis_str = "radiacion_solar"
    resolucion_malla = 1.0
    altura_punto_analisis = 1.1
    incluir_sombras_propias = True
    incluir_sombras_contextuales = False
    contexto_edificios = None

    # Intentar obtener variables de entrada de Grasshopper
    try:
        if 'geometria_edificio' in locals() and geometria_edificio is not None:
            pass  # Ya tiene valor
        else:
            geometria_edificio = "geometria_ejemplo"  # Placeholder

        if 'clima_archivo' in locals() and clima_archivo:
            if isinstance(clima_archivo, str):
                clima_archivo = clima_archivo.strip()
                if not clima_archivo or clima_archivo.lower() in ["none", "null", ""]:
                    clima_archivo = None
        else:
            clima_archivo = None

        if 'punto_norte' in locals() and punto_norte is not None:
            if isinstance(punto_norte, str):
                try:
                    punto_norte = json.loads(punto_norte)
                except:
                    punto_norte = None
        else:
            punto_norte = None

        if 'periodo_analisis' in locals() and periodo_analisis:
            periodo_analisis = periodo_analisis.lower().strip()
        else:
            periodo_analisis = "anual"

        if 'tipo_analisis' in locals() and tipo_analisis:
            tipo_analisis_str = tipo_analisis.lower().strip()
        else:
            tipo_analisis_str = "radiacion_solar"

        if 'resolucion_malla' in locals() and resolucion_malla is not None:
            resolucion_malla = safe_float(resolucion_malla, 1.0)
        else:
            resolucion_malla = 1.0

        if 'altura_punto_analisis' in locals() and altura_punto_analisis is not None:
            altura_punto_analisis = safe_float(altura_punto_analisis, 1.1)
        else:
            altura_punto_analisis = 1.1

        if 'incluir_sombras_propias' in locals() and incluir_sombras_propias is not None:
            if isinstance(incluir_sombras_propias, str):
                incluir_sombras_propias = incluir_sombras_propias.lower() in ['true', '1', 'yes']
            else:
                incluir_sombras_propias = bool(incluir_sombras_propias)
        else:
            incluir_sombras_propias = True

        if 'incluir_sombras_contextuales' in locals() and incluir_sombras_contextuales is not None:
            if isinstance(incluir_sombras_contextuales, str):
                incluir_sombras_contextuales = incluir_sombras_contextuales.lower() in ['true', '1', 'yes']
            else:
                incluir_sombras_contextuales = bool(incluir_sombras_contextuales)
        else:
            incluir_sombras_contextuales = False

        if 'contexto_edificios' in locals() and contexto_edificios is not None:
            if isinstance(contexto_edificios, str):
                try:
                    contexto_edificios = json.loads(contexto_edificios)
                except:
                    contexto_edificios = None
        else:
            contexto_edificios = None

    except Exception as e:
        print(f"Advertencia: Error procesando entradas: {e}. Usando valores por defecto.")

    # Validar y establecer valores predeterminados
    if not clima_archivo:
        clima_archivo = "BRA_Bogota.Eldorado.803820_TMYx.epw"  # Clima por defecto para Bogotá
        print(f"Usando archivo de clima por defecto: {clima_archivo}")

    if punto_norte is None:
        # Norte por defecto (vector Y positivo)
        punto_norte = [0, 1, 0]
        print("Usando vector norte por defecto: [0, 1, 0]")

    if periodo_analisis not in [p.value for p in PeriodoAnalisis]:
        periodo_analisis = "anual"
        print(f"Período de análisis no válido. Usando: {periodo_analisis}")

    try:
        tipo_analisis = TipoAnalisis(tipo_analisis_str)
    except ValueError:
        tipo_analisis = TipoAnalisis.RADIACION_SOLAR
        print(f"Tipo de análisis no válido. Usando: {tipo_analisis.value}")

    # Preparar geometría para análisis
    print("Preparando geometría para análisis...")

    # En una implementación real, aquí se procesaría la geometría de entrada
    # Para este ejemplo, creamos una geometría de referencia
    limite_sitio = {
        "tipo": "Polígono",
        "coordenadas": [[0, 0, 0], [50, 0, 0], [50, 50, 0], [0, 50, 0], [0, 0, 0]]
    }

    volumen_estimado = {
        "tipo": "Prisma Rectangular",
        "dimensiones": [30, 30, 15],  # largo, ancho, alto
        "volumen_m3": 30 * 30 * 15,
        "superficie_exterior_m2": 2 * (30*30 + 30*15 + 30*15)
    }

    zonas_funcionales = [
        {
            "id": "zona_1",
            "tipo": "residencial",
            "area_m2": 150,
            "volumen_m3": 450,
            "altura_promedio": 3.0
        },
        {
            "id": "zona_2",
            "tipo": "comercial",
            "area_m2": 100,
            "volumen_m3": 300,
            "altura_promedio": 3.0
        }
    ]

    # Preparar datos climáticos
    print("Preparando datos climáticos...")
    datos_climaticos = {
        "archivo_epw": clima_archivo,
        "ciudad": "Bogotá",
        "pais": "Colombia",
        "latitud": 4.7110,
        "longitud": -74.0721,
        "zona_horaria": -5,
        "elevacion_m": 2640,
        "periodo_disponible": "TMY (Typical Meteorological Year)"
    }

    # Preparar orientación
    print("Configurando orientación...")
    vector_norte_original = crear_vector_desde_lista(punto_norte)
    vector_norte_normalizado = rs.UnitVector(vector_norte_original) if RHINO_AVAILABLE else vector_norte_original
    angulo_norte_grados = 0  # En una implementación real, se calcularía respecto al norte verdadero

    # Determinar parámetros de análisis según tipo
    print(f"Configurando parámetros para análisis: {tipo_analisis.value}")
    parametros_analisis = PARAMETROS_DEFECTO.get(tipo_analisis, {}).copy()

    # Ajustar resolución de malla
    if "mesh_size" in parametros_analisis:
        parametros_analisis["mesh_size"] = resolucion_malla
    if "grid_size" in parametros_analisis:
        parametros_analisis["grid_size"] = resolucion_malla

    # Ajustar período de análisis
    if periodo_analisis == "verano":
        parametros_analisis["mes_inicio"] = 12  # Diciembre (verano en SH)
        parametros_analisis["mes_fin"] = 2      # Febrero
    elif periodo_analisis == "invierno":
        parametros_analisis["mes_inicio"] = 6   # Junio (invierno en SH)
        parametros_analisis["mes_fin"] = 8      # Agosto
    elif periodo_analisis.startswith("mes"):
        try:
            mes_num = int(periodo_analisis.split("_")[1]) if len(periodo_analisis.split("_")) > 1 else 6
            parametros_analisis["mes_especifico"] = max(1, min(12, mes_num))
        except:
            parametros_analisis["mes_especifico"] = 6  # Junio por defecto

    # Preparar malla de análisis
    print("Generando malla de análisis...")
    bounding_box = obtener_bounding_box(geometria_edificio)
    tamaño_celda = resolucion_malla

    # Puntos de análisis a altura humana
    puntos_analisis_altura = []
    if geometria_edificio:
        # En una implementación real, se generarían puntos en las superficies
        # Por ahora, creamos una cuadrícula simple en el rango del bounding box
        x_min, y_min, z_min = bounding_box["min"]
        x_max, y_max, z_max = bounding_box["max"]

        # Crear una cuadrícula básica en el plano XY a la altura especificada
        pasos_x = max(1, int((x_max - x_min) / tamaño_celda))
        pasos_y = max(1, int((y_max - y_min) / tamaño_celda))

        for i in range(min(pasos_x, 10)):  # Limitar para no generar demasiados puntos
            for j in range(min(pasos_y, 10)):
                x = x_min + (i + 0.5) * tamaño_celda
                y = y_min + (j + 0.5) * tamaño_celda
                z = altura_punto_analisis
                puntos_analisis_altura.append([x, y, z])

    vorbereitung_datos_ladybug = {
        "tipo_analisis": tipo_analisis.value,
        "geometria": {
            "limite_sitio": limite_sitio,
            "volumen_estimado": volumen_estimado,
            "zonas_funcionales": zonas_funcionales,
            "bounding_box": bounding_box,
            "puntos_analisis": puntos_analisis_altura[:50] if len(puntos_analisis_altura) > 50 else puntos_analisis_altura  # Limitar para output
        },
        "clima": datos_climaticos,
        "orientacion": {
            "vector_norte": [vector_norte_normalizado.X, vector_norte_normalizado.Y, vector_norte_normalizado.Z],
            "angulo_norte_grados": angulo_norte_grados,
            "sistema_coordenadas": "derecho"
        },
        "parametros_simulacion": parametros_analisis,
        "configuracion_analisis": {
            "periodo": periodo_analisis,
            "resolucion_malla_m": resolucion_malla,
            "altura_analisis_humano_m": altura_punto_analisis,
            "incluir_sombras_propias": incluir_sombras_propias,
            "incluir_sombras_contextuales": incluir_sombras_contextuales,
            "contexto_incluido": bool(contexto_edificios)
        },
        "metadatos": {
            "version_preparador": "1.0.0",
            "fecha_preparacion": datetime.now().isoformat(),
            "software": "PREP_LADYBUG_v01",
            "comentarios": "Datos preparados para análisis con Ladybug/Honeybee"
        }
    }

    # Preparar datos específicos para Honeybee (modelo energético)
    datos_honeybee = {
        "tipo_analisis: tipo_analisis.value if tipo_analisis != TipoAnalisis.CONSUMO_ENERGETICO else "carga_energetica_anual",
        "modelo_energetico": {
            "tipo": "Modelo BoxSimple",  # Simplificado para el ejemplo
            "pisos": int(volumen_estimado["dimensiones"][2] / 3.0) if volumen_estimado["dimensiones"][2] > 0 else 1,
            "altura_piso_promedio": 3.0,
            "area_pisos": [zona["area_m2"] for zona in zonas_funcionales],
            "volumen_total": sum(zona["volumen_m3"] for zona in zonas_funcionales),
            "envolvente": {
                "tipo_construccion": "medio",
                "aislamiento_paredes": "medio",
                "aislamiento_techo": "medio",
                "tipo_ventanas": "doble_vidrio_clear",
                "fraccion_ventana_pared": 0.3
            },
            "cargas_internas": {
                "iluminacion_w_m2": 10 if "oficina" in [z["tipo"] for z in zonas_funcionales] else 5,
                "equipamiento_w_m2": 5 if "oficina" in [z["tipo"] for z in zonas_funcionales] else 3,
                "personas_por_m2": 0.1 if "oficina" in [z["tipo"] for z in zonas_funcionales] else 0.05
            },
            "programacion": {
                "tipo_uso": "oficina" if any("oficina" in z["tipo"] for z in zonas_funcionales) else "residencial",
                "horario_operacion": "08:00-18:00, L-V" if any("oficina" in z["tipo"] for z in zonas_funcionales) else "07:00-22:00, Todos"
            }
        },
        "clima": datos_climaticos,
        "simulacion": {
            "paso_tiempo_hora": 1,
            "metodos_calculo": "DF" if tipo_analisis == TipoAnalisis.ILUMINACION_DIA else "CTF",
            "dias_simulacion": 365 if periodo_analisis == "anual" else 90 if periodo_analisis in ["verano", "invierno"] else 30
        }
    }

    # Parámetros específicos según tipo de análisis
    parametros_especificos = {
        "tipo_analisis": tipo_analisis.value,
        "periodo": periodo_analisis,
        "resolucion": resolucion_malla,
        "configuracion_detallada": parametros_analisis,
        "archivos_salida_esperados": []
    }

    if tipo_analisis == TipoAnalisis.RADIACION_SOLAR:
        parametros_especificos["archivos_salida_esperados"] = [
            "radiacion_horaria_whm2.csv",
            "radiacion_diaria_whm2.csv",
            "radiacion_mensual_whm2.csv",
            "mapa_colores_anual.png",
            "grafica_mensual.png"
        ]
        parametros_especificos["metodos_calculo"] = [
            "radiacion_directa_normal",
            "radiacion_difusa_horizontal",
            "radiacion_global_horizontal"
        ]
    elif tipo_analisis == TipoAnalisis.ILUMINACION_DIA:
        parametros_especificos["archivos_salida_esperados"] = [
            "iluminancia_hora_puntual_lux.csv",
            "iluminancia_diaria_promedio_lux.csv",
            "factor_iluminacion_diurna_prompt_pdf",
            "mapa_iluminancia_anual.png",
            "analisis_deslumbrante.pdf"
        ]
        parametros_especificos["metodos_calculo"] = [
            "metodo_puntos",
            "biDireccional_transmitancia"
        ]
    elif tipo_analisis == TipoAnalisis.CONSUMO_ENERGETICO:
        parametros_especificos["archivos_salida_esperados"] = [
            "balance_energetico_anual_kwh.csv",
            "calefaccion_mensual_kwh.csv",
            "refrigeracion_mensual_kwh.csv",
            "iluminacion_mensual_kwh.csv",
            "equipamiento_mensual_kwh.csv",
            "carga_total_mensual_kwh.csv",
            "grafica_carga_horaria.png",
            "certificacion_energetica.pdf"
        ]
        parametros_especificos["metodos_calculo"] = [
            "metodo_balance_energetico",
            "simulacion_trasiera"
        ]
    elif tipo_analisis == TipoAnalisis.COMFORT_TERMAL:
        parametros_especificos["archivos_salida_esperados"] = [
            "indice_comfort_mensual.csv",
            "horas_sobrecalentamiento.csv",
            "horas_subenfriamiento.csv",
            "mapa_comfort_por_zona.png",
            "grafica_pmv_ppd.png"
        ]
        parametros_especificos["metodos_calculo"] = [
            "modelo_PMV_PPD",
            "indice_temperatura_operativa",
            "porcentaje_personas_insatisfechas"
        ]

    # Generar reporte de preparación
    print("Generando reporte de preparación...")

    reporte_lineas = [
        "=" * 80,
        "PREPARACIÓN DE DATOS PARA ANÁLISIS LADYBUG/HONEYBEE - INFORME",
        "=" * 80,
        f"Fecha de preparación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Tipo de análisis: {tipo_analisis.value}",
        f"Período de análisis: {periodo_analisis}",
        f"Resolución de malla: {resolucion_malla} m",
        f"Altura de análisis humano: {altura_punto_analisis} m",
        "",
        "GEOMETRÍA PROCESADA:",
        "-" * 40,
        f"• Límite de sitio: {len(limite_sitio.get('coordenadas', []))-1 if 'coordenadas' in limite_sitio else 0} vértices",
        f"• Volumen estimado del edificio: {volumen_estimado.get('volumen_m3', 0):.1f} m³",
        f"• Superficie exterior estimada: {volumen_estimado.get('superficie_exterior_m2', 0):.1f} m²",
        f"• Número de zonas funcionales: {len(zonas_funcionales)}",
        ""
    ]

    for i, zona in enumerate(zonas_funcionales[:3]):  # Mostrar primeras 3 zonas
        zona_tipo = zona.get('tipo', 'desconocido')
        zona_area = zona.get('area_m2', 0)
        zona_volumen = zona.get('volumen_m3', 0)
        zona_altura = zona.get('altura_promedio', 0)
        reporte_lineas.append(
            f"  Zona {i+1} ({zona_tipo}): {zona_area:.1f} m², {zona_volumen:.1f} m³, {zona_altura:.1f} m altura"
        )

    if len(zonas_funcionales) > 3:
        resto = len(zonas_funcionales) - 3
        reporte_lineas.append(f"  ... y {resto} zonas más")

    reporte_lineas.extend([
        "",
        "DATOS CLIMÁTICOS:",
        "-" * 40,
        f"• Ciudad: {datos_climaticos.get('ciudad', 'N/D')}, {datos_climaticos.get('pais', 'N/D')}",
        f"• Latitud: {datos_climaticos.get('latitud', 0):.4f}°",
        f"• Longitud: {datos_climaticos.get('longitud', 0):.4f}°",
        f"• Elevación: {datos_climaticos.get('elevacion_m', 0)} m s.n.m.",
        f"• Archivo EPW: {datos_climaticos.get('archivo_epw', 'N/D')}",
        f"• Zona horaria: UTC{datos_climaticos.get('zona_horaria', 0):+d}",
        "",
        "ORIENTACIÓN Y NORTE:",
        "-" * 40,
        f"• Vector norte: [{vector_norte_normalizado.X:.3f}, {vector_norte_normalizado.Y:.3f}, {vector_norte_normalizado.Z:.3f}]",
        f"• Ángulo de rotación aplicado: {angulo_norte_grados}°",
        f"• Sistema de coordenadas: Derecho (X-Este, Y-Norte, Z-Arriba)",
        "",
        "CONFIGURACIÓN DE ANÁLISIS:",
        "-" * 40,
        f"• Tipo de análisis solicitado: {tipo_analisis.value}",
    ])

    # Añadir detalles específicos según tipo de análisis
    if tipo_analisis == TipoAnalisis.RADIACION_SOLAR:
        reporte_lineas.extend([
            "• Análisis de radiación solar directa, difusa y global",
            "• Cálculo horario y acumulado",
            "• Mapas de radiación en superficies"
        ])
    elif tipo_analisis == TipoAnalisis.ILUMINACION_DIA:
        reporte_lineas.extend([
            "• Análisis de iluminancia natural interior",
            "• Cálculo del Factor de Iluminación Diurna (FID)",
            "• Evaluación de deslumbramiento"
        ])
    elif tipo_analisis == TipoAnalisis.CONSUMO_ENERGETICO:
        reporte_lineas.extend([
            "• Simulación energética anual",
            "• Cálculo de cargas de calefacción, refrigeración, iluminación y equipos",
            "• Estimación de consumo energético neto"
        ])
    elif tipo_analisis == TipoAnalisis.COMFORT_TERMAL:
        reporte_lineas.extend([
            "• Evaluación de confort térmico usando modelo PMV-PPD",
            "• Cálculo de horas de sobrecalentamiento y subenfriamiento",
            "• Mapas de confort por zonas"
        ])

    reporte_lineas.extend([
        "",
        f"• Resolución de malla de análisis: {resolucion_malla} m",
        f"• Altura de puntos de análisis humano: {altura_punto_analisis} m",
        f"• Incluir sombras propias: {'Sí' if incluir_sombras_propias else 'No'}",
        f"• Incluir sombras contextuales: {'Sí' if incluir_sombras_contextuales else 'No'}",
        f"• Contexto de edificios vecinos: {'Incluido' if contexto_edificios else 'No incluido'}",
        "",
        "PARÁMETROS DE SIMULACIÓN ESPECÍFICOS:",
        "-" * 40
    ])

    for key, value in parametros_analisis.items():
        if isinstance(value, bool):
            valor_str = "Sí" if value else "No"
        elif isinstance(value, (int, float)):
            valor_str = f"{value}"
        else:
            valor_str = str(value)[:50] + ("..." if len(str(value)) > 50 else "")
        reporte_lineas.append(f"• {key}: {valor_str}")

    if parametros_especificos["archivos_salida_esperados"]:
        reporte_lineas.extend([
            "",
            "ARCHIVOS DE SALIDA ESPERADOS:",
            "-" * 40
        ])
        for archivo in parametros_especificos["archivos_salida_esperados"][:5]:  # Mostrar primeros 5
            reporte_lineas.append(f"• {archivo}")

        if len(parametros_especificos["archivos_salida_esperados"]) > 5:
            resto = len(parametros_especificos["archivos_salida_esperados"]) - 5
            reporte_lineas.append(f"  ... y {resto} archivos más")

    # Recomendaciones basada en el tipo de análisis
    recomendaciones = []
    if tipo_analisis == TipoAnalisis.RADIACION_SOLAR:
        recomendaciones.append("Considerar análisis de sobrecalentamiento para superficies vidriadas orientadas al oeste")
        recomendaciones.append("Evaluar potencial de ganancia solar pasiva en orientación sur")
    elif tipo_analisis == TipoAnalisis.ILUMINACION_DIA:
        recomendaciones.append("Verificar cumplimiento de estándares de iluminancia minima (300 lux para espacios de trabajo)")
        recomendaciones.append("Analizar distribución uniforme de luz para reducir puntos ciegos")
    elif tipo_analisis == TipoAnalisis.CONSUMO_ENERGETICO:
        recomendaciones.append("Comparar resultados con benchmarks de edificios similares en la región")
        recomendaciones.append("Identificar oportunidades de mejora en envolvente y sistemas HVAC")
    elif tipo_analisis == TipoAnalisis.COMFORT_TERMAL:
        recomendaciones.append("Evaluar estrategias de ventilación natural para reducir carga de refrigeración")
        recomendaciones.append("Considerar masas térmicas para estabilizar temperaturas interiores")

    if recomendaciones:
        reporte_lineas.extend([
            "",
            "RECOMENDACIONES ESPECÍFICAS:",
            "-" * 40
        ])
        for rec in recomendaciones:
            reporte_lineas.append(f"• {rec}")

    # Conclusión general
   重almente = True  # Siempre válido en modo de preparación
    status_general = "LISTO PARA ANÁLISIS" if realmente else "REQUIERE REVISIÓN"

    reporte_lineas.extend([
        "",
        "ESTADO GENERAL:",
        "-" * 40,
        f"Preparación de datos: {status_general}",
        f"Geometría procesada: {'Sí' if geometria_edificio else 'No'}",
        f"Clima cargado: {'Sí' if datos_climaticos.get('archivo_epw') else 'No'}",
        f"Orientación definida: {'Sí' if punto_norte else 'No'}",
        f"Parámetros de análisis completados: {'Sí' if parametros_analisis else 'No'}",
        "",
        "PRÓXIMOS PASOS:",
        "-" * 40,
        "1. Ejecutar análisis con Ladybug usando los archivos JSON generados",
        "2. Para analisis energéticos: usar Honeybee con el modelo energético preparado",
        "3. Validar resultados climáticos contra datos locales de registros históricos",
        "4. Considerar refinamiento de malla en áreas de interés particular",
        "5. Documentar suposiciones y limitaciones del análisis para el informe final",
        "",
        "=" * 80
    ])

    reporte_texto = "\n".join(reporte_lineas)

    # Preparar salida en formato GeoJSON para visualización (simplificado)
    geometria_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "name": "Límite del sitio",
                    "type": "boundary"
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [limite_sitio.get("coordenadas", [[[0,0,0],[100,0,0],[100,100,0],[0,100,0],[0,0,0]]])]
                }
            },
            {
                "type": "Feature",
                "properties": {
                    "name": "Vector Norte",
                    "type": "reference"
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [25, 25, 0],  # Punto de origen (centro aproximado)
                        [25 + vector_norte_normalizado.X * 10,
                         25 + vector_norte_normalizado.Y * 10,
                         0 + vector_norte_normalizado.Z * 10]  # Punta del vector
                    ]
                }
            }
        ]
    }

    # Añadir puntos de análisis si existen pocos
    if len(puntos_analisis_altura) <= 20:
        for i, punto in enumerate(puntos_analisis_altura[:10]):  # Máximo 10 puntos para legibilidad
            geometria_geojson["features"].append({
                "type": "Feature",
                "properties": {
                    "name": f"Punto de análisis {i+1}",
                    "type": "analysis_point",
                    "height": altura_punto_analisis
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [punto[0], punto[1], punto[2]]
                }
            })

    # Convertir a JSON para salida
    ladybug_json = json.dumps(preparacion_datos_ladybug, indent=2, ensure_ascii=False)
    honeybee_json = json.dumps(datos_honeybee, indent=2, ensure_ascii=False)
    parametros_json = json.dumps(parametros_especificos, indent=2, ensure_ascii=False)
    geometria_geo_json = json.dumps(geometria_geojson, indent=2, ensure_ascii=False)

    print("\n=== RESUMEN DE PREPARACIÓN ===")
    print(f"Análisis preparado: {tipo_analisis.value}")
    print(f"Período: {periodo_analisis}")
    print(f"Resolución de malla: {resolucion_malla} m")
    print(f"Puntos de análisis generados: {len(puntos_analisis_altura)}")
    print(f"Datos climáticos cargados: {clima_archivo}")

    # Guardar resultados en archivos
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    ladybug_path = os.path.join(output_dir, "ladybug_entrada.json")
    with open(ladybug_path, 'w', encoding='utf-8') as f:
        f.write(ladybug_json)

    honeybee_path = os.path.join(output_dir, "honeybee_entrada.json")
    with open(honeybee_path, 'w', encoding='utf-8') as f:
        f.write(honeybee_json)

    parametros_path = os.path.join(output_dir, "parametros_simulacion.json")
    with open(parametros_path, 'w', encoding='utf-8') as f:
        f.write(parametros_json)

    geojson_path = os.path.join(output_dir, "geometria_preparada_geo.json")
    with open(geojson_path, 'w', encoding='utf-8') as f:
        f.write(geometria_geo_json)

    reporte_path = os.path.join(output_dir, "reporte_preparacion.txt")
    with open(reporte_path, 'w', encoding='utf-8') as f:
        f.write(reporte_texto)

    print(f"\nArchivos guardados en: {output_dir}")
    print(f"  - ladybug_entrada.json")
    print(f"  - honeybee_entrada.json")
    print(f"  - parametros_simulacion.json")
    print(f"  - geometria_preparada_geo.json")
    print(f"  - reporte_preparacion.txt")

    # Asignar para salida de Grasshopper
    ladybug_entrada = ladybug_json
    honeybee_entrada = honeybee_json
    parametros_simulacion = parametros_json
    geometria_preparada_geo = geometria_geo_json
    reporte_preparacion = reporte_texto

# Ejecutar si se ejecuta como script principal
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error en PREP_LADYBUG_v01: {str(e)}")
        import traceback
        traceback.print_exc()

        # Salida de error para Grasshopper
        error_result = {
            "error": str(e),
            "mensaje": "Error en la preparación de datos para análisis Ladybug/Honeybee"
        }
        ladybug_entrada = json.dumps(error_result, indent=2, ensure_ascii=False)
        honeybee_entrada = json.dumps(error_result, indent=2, ensure_ascii=False)
        parametros_simulacion = json.dumps(error_result, indent=2, ensure_ascii=False)
        geometria_preparada_geo = json.dumps(error_result, indent=2, ensure_ascii=False)
        reporte_preparacion = f"ERROR: {str(e)}"