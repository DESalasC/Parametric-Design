#!/usr/bin/env python3
"""
OPTIMIZADOR_ADYACENCIA_v01.py - Optimización de Colocación Espacial y Análisis de Adyacencias
GH Python Script para Grasshopper (GH Player compatible)

ENTRADAS (via Grasshopper):
  - programa_espacial_json: JSON con requerimientos de programa (output de DEMANDA_MOTOR_v01.py o PROGRAMA_AREAS_v01.py)
  - restricciones_territoriales_json: JSON de restricciones territoriales (output de VALIDADOR_CRUZADO_v01.py)
  - poligono_lote: Polígono del lote como lista de puntos [[x1,y1], [x2,y2], ...] (opcional, para contextualización)
  - restricciones_altura: Límites de altura por zona (opcional)
  - factores_ponderacion: Pesos para diferentes criterios de optimización (accesibilidad, vistas, etc.)
  - numero_pisos_objetivo: Número objetivo de pisos para el desarrollo

SALIDAS:
  - distribucion_espacial_optima.json: JSON con la distribución óptima de usos por zona y piso
  - matriz_adyacencia_evaluada.json: Evaluación de cumplimiento de la matriz de adyacencias deseada
  - metricas_espaciales.json: Métricas de calidad del diseño (compactibilidad, accesibilidad, etc.)
  - reporte_optimizacion.txt: Reporte legible del proceso de optimización y recomendaciones
"""

import json
import math
import itertools
import random
from typing import Dict, List, Tuple, Any, Optional, Set
from collections import defaultdict

# Try to import Rhino-specific modules, provide fallbacks for testing
try:
    import rhinoscriptsyntax as rs
    RHINO_AVAILABLE = True
except ImportError:
    RHINO_AVAILABLE = False
    # Mock functions for testing/non-Rhino environments
    class MockRs:
        @staticmethod
        def AreaPolygon(points):
            return 0.0 if len(points) < 3 else 1000.0  # Área aproximada

        @staticmethod
        def Distance(point1, point2):
            return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

        @staticmethod
        def PointInPlanarClosedCurve(point, polygon):
            return 1  # Simplified: assume inside

        @staticmethod
        def CurveLength(curve):
            return 0.0

        @staticmethod
        def BoundingBox(objects):
            return [[0,0,0], [100,100,0]]  # Bounding box ficticio

    rs = MockRs()

# ============================================================
# CONFIGURACIÓN DE PARÁMETROS DE OPTIMIZACIÓN
# ============================================================

# Pesos predeterminados para la función objetivo de optimización
PESOS_OPTIMIZACION_DEFAULT = {
    "adyacencia": 0.35,      # Cumplimiento de preferencias de adyacencia
    "compactibilidad": 0.25,  # Compactibilidad del volumen construido
    "accesibilidad": 0.20,    - # Accesibilidad desde vías principales
    "views": 0.10,            # Calidad de vistas (simplificado)
    "servicios": 0.10         # Proximidad a servicios y transporte
}

# Matriz de afinidad predeterminada (valores de 0.0 a 1.0)
# Valores cercanos a 1.0 indican fuerte preferencia de estar juntos
# Valores cercanos a 0.0 indican preferencia de separación
# Valores cercanos a 0.5 indican neutralidad
MATRIZ_AFINIDAD_DEFAULT = {
    # Filas: uso actual, Columnas: uso adyacente
    ("residencial", "residencial"): 0.8,   # Los residenciales prefieren estar cerca de otros residenciales
    ("residencial", "comercio"): 0.6,      # Los residentes como tener comercios cercanos (pero no demasiado)
    ("residencial", "oficinas"): 0.4,      # Preferencia mixta
    ("residencial", "salud"): 0.3,         # Preferencia de estar razonablemente cerca de salud
    ("residencial", "educacion"): 0.7,     # Familias quieren estar cerca de escuelas
    ("residencial", "parque"): 0.9,        # Alta preferencia por zonas verdes
    ("residencial", "estacionamiento"): 0.2, # Preferencia de estar lejos de estacionamientos (ruido, olores)
    ("residencial", "industrial"): 0.1,    - # Fuerte preferencia de separación

    ("comercio", "residencial"): 0.6,      # Simétrico
    ("comercio", "comercio"): 0.7,         # Los comercios se benefician de aglomeración
    ("comercio", "oficinas"): 0.8,         - # Sinergia fuertes entre oficinas y retail
    ("comercio", "salud"): 0.5,            # Relación neutra-positiva
    ("comercio", "educacion"): 0.4,        # Poco beneficio de estar cerca de escuelas
    ("comercio", "parque"): 0.6,           # Parques atraen flujo peatonal beneficioso
    ("comercio", "estacionamiento"): 0.9,  # Muy importante para el comercio
    ("comercio", "industrial"): 0.2,       # Preferencia de separación

    ("oficinas", "residencial"): 0.4,
    ("oficinas", "comercio"): 0.8,
    ("oficinas", "oficinas"): 0.9,         # Las oficinas se benefician mucho de estar juntas
    ("oficinas", "salud"): 0.6,
    ("oficinas", "educacion"): 0.5,
    ("oficinas", "parque"): 0.4,
    ("oficinas", "estacionamiento"): 0.8,
    ("oficinas", "industrial"): 0.3,

    ("salud", "residencial"): 0.3,
    ("salud", "comercio"): 0.5,
    ("salud", "oficinas"): 0.6,
    ("salud", "salud"): 0.8,               # Servicios de salud se benefician de cercanía (shared equipment, etc)
    ("salud", "educacion"): 0.7,           # Cerca de universidades médicas es beneficioso
    ("salud", "parque"): 0.5,              # Espacios verdes beneficiosos para recuperación
    ("salud", "estacionamiento"): 0.7,
    ("salud", "industrial"): 0.2,

    ("educacion", "residencial"): 0.7,
    ("educacion", "comercio"): 0.4,
    ("educacion", "oficinas"): 0.5,
    ("educacion", "salud"): 0.7,
    ("educacion", "educacion"): 0.8,
    ("educacion", "parque"): 0.6,
    ("educacion", "estacionamiento"): 0.5,
    ("educacion", "industrial"): 0.2,

    ("parque", "residencial"): 0.9,
    ("parque", "comercio"): 0.6,
    ("parque", "oficinas"): 0.4,
    ("parque", "salud"): 0.5,
    ("parque", "educacion"): 0.6,
    ("parque", "parque"): 0.7,
    ("parque", "estacionamiento"): 0.3,
    ("parque", "industrial"): 0.1,

    ("estacionamiento", "residencial"): 0.2,
    ("estacionamiento", "comercio"): 0.9,
    ("estacionamiento", "oficinas"): 0.8,
    ("estacionamiento", "salud"): 0.7,
    ("estacionamiento", "educacion"): 0.5,
    ("parque", "estacionamiento"): 0.3,
    ("estacionamiento", "estacionamiento"): 0.6,
    ("estacionamiento", "industrial"): 0.5, # Los industriales necesitan mucho estacionamiento

    ("industrial", "residencial"): 0.1,
    ("industrial", "comercio"): 0.2,
    ("industrial", "oficinas"): 0.3,
    ("industrial", "salud"): 0.2,
    ("industrial", "educacion"): 0.2,
    ("industrial", "parque"): 0.1,
    ("industrial", "estacionamiento"): 0.5,
    ("industrial", "industrial"): 0.7,      # Las industrias pueden aglomerarse para compartir infraestructura
}

# Penalti por violar restricciones de altura o usos prohibidos
PENALIZACION_VIOLACION_RESTRICCION = 1.0

# Bonus por uso eficiente de terreno (construir hasta el límite permitido)
BONO_APROVECHAMIENTO_TERRENO = 0.2

# ============================================================
# FUNCIONES AUXILIARES DE GEOMETRÍA Y UTILIDADES
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

def calcular_area_poligono(puntos):
    """
    Calcula el área de un polígono dado por lista de puntos [x,y]
    Usa la fórmula del shoelace
    """
    if len(puntos) < 3:
        return 0.0

    area = 0.0
    j = len(puntos) - 1
    for i in range(len(puntos)):
        xi, yi = puntos[i]
        xj, yj = puntos[j]
        area += xi * yj - xj * yi
        j = i
    return abs(area) / 2.0

def punto_dentro_poligono(punto, poligono):
    """
    Determina si un punto está dentro de un polígono usando algoritmo de ray casting
    """
    if len(poligono) < 3:
        return True  # Asumir dentro si el polígono no es válido

    x, y = punto
    dentro = False
    j = len(poligono) - 1

    for i in range(len(poligono)):
        xi, yi = poligono[i]
        xj, yj = poligono[j]

        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            dentro = not dentro
        j = i

    return dentro

def distancia_punto_a_segmento(px, py, x1, y1, x2, y2):
    """
    Calcula la distancia mínima de un punto (px,py) a un segmento de línea (x1,y1)-(x2,y2)
    """
    # Vector del segmento
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        # El segmento es un punto
        return math.sqrt((px - x1)**2 + (py - y1)**2)

    # Proyección del punto sobre la línea
    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
    t = max(0, min(1, t))  # Clamp to segment

    # Punto más cercano en el segmento
    closest_x = x1 + t * dx
    closest_y = y1 + t * dy

    return math.sqrt((px - closest_x)**2 + (py - closest_y)**2)

def distancia_punto_a_poligono(punto, poligono):
    """
    Calcula la distancia mínima de un punto a un polígono (0 si está dentro)
    """
    if punto_dentro_poligono(punto, poligono):
        return 0.0

    min_dist = float('inf')
    for i in range(len(poligono)):
        x1, y1 = poligono[i]
        x2, y2 = poligono[(i + 1) % len(poligono)]
        dist = distancia_punto_a_segmento(punto[0], punto[1], x1, y1, x2, y2)
        min_dist = min(min_dist, dist)

    return min_dist

# ============================================================
# FUNCIONES DE OPTIMIZACIÓN
# ============================================================

def calcular_puntuacion_adyacencia(asignacion_zonas, matriz_afinidad, pesos=None):
    """
    Calcula la puntuación de adyacencia basada en qué tipos de uso están adyacentes
    """
    if pesos is None:
        pesos = PESOS_OPTIMIZACION_DEFAULT

    peso_adyacencia = pesos.get("adyacencia", 0.35)
    if peso_adyacencia == 0:
        return 1.0  # Si no importa la adyacencia, puntuación perfecta

    puntuacion_total = 0.0
    total_adyacencias_evaluadas = 0

    # Para cada par de zonas que comparten frontera
    for zona_id, datos_zona in asignacion_zonas.items():
        uso_zona = datos_zona.get("uso", "desconocido")
        zonas_adyacentes = datos_zona.get("adyacentes", [])

        for vecino_id in zonas_adyacentes:
            if vecino_id in asignacion_zonas:
                uso_vecino = asignacion_zonas[vecino_id].get("uso", "desconocido")

                # Buscar afinidad en ambas direcciones (promedio para simmetrizar)
                afinidad_directa = matriz_afinidad.get((uso_zona, uso_vecino), 0.5)
                afinidad_inversa = matriz_afinidad.get((uso_vecino, uso_zona), 0.5)
                afinidad_promedio = (afinidad_directa + afinidad_inversa) / 2.0

                puntuacion_total += afinidad_promedio
                total_adyacencias_evaluadas += 1

    if total_adyacencias_evaluadas == 0:
        return 1.0  # No hay adyacencias para evaluar

    puntuacion_promedio = puntuacion_total / total_adyacencias_evaluadas
    return puntuacion_promedio  # Ya está en escala 0-1

def calcular_puntuacion_compactibilidad(asignacion_zonas, area_total_disponible):
    """
    Calcula qué tan compacto es el layout (menos superficie de perímetro expuesto)
    """
    peso_compactibilidad = PESOS_OPTIMIZACION_DEFAULT.get("compactibilidad", 0.25)
    if peso_compactibilidad == 0:
        return 1.0

    # Simplificación: medir la relación entre el área construida y el perímetro total
    # Un círculo tendría la mejor relación área/perímetro

    area_construida_total = 0.0
    perimetro_expuesto_total = 0.0

    for zona_id, datos_zona in asignacion_zonas.items():
        area_zona = datos_zona.get("area_asignada", 0.0)
        perimetro_zona = datos_zona.get("perimetro_calculado", 0.0)

        area_construida_total += area_zona
        perimetro_expuesto_total += perimetro_zona

    if area_construida_total == 0:
        return 0.0

    # Índex de compactización: 4π * Área / Perímetro^2 (1.0 para círculo perfecto)
    if perimetro_expuesto_total > 0:
        compacidad = (4 * math.pi * area_construida_total) / (perimetro_expuesto_total ** 2)
        # Normalizar a 0-1 donde 1 es perfectamente compacto
        # Un cuadrado tiene compacidad ≈ 0.785
        compacidad_normalizada = min(1.0, compacidad / 0.785)
    else:
        compacidad_normalizada = 0.0

    return compacidad_normalizada

def calcular_puntuacion_accesibilidad(asignacion_zonas, poligono_lote, puntos_acceso=None):
    """
    Calcula la accesibilidad promedio de las zonas desde puntos de acceso (calles, transporte)
    """
    peso_accesibilidad = PESOS_OPTIMIZACION_DEFAULT.get("accesibilidad", 0.20)
    if peso_accesibilidad == 0:
        return 1.0

    if puntos_acceso is None:
        # Si no se especifican puntos de acceso, usar puntos medios de cada lado del lote
        # Esto es una simplificación
        if len(poligono_lote) >= 4:
            # Tomar puntos a lo largo del perímetro como acceso simulado
            puntos_acceso = []
            for i in range(0, len(poligono_lote), max(1, len(poligono_lote)//4)):
                puntos_acceso.append(poligono_lote[i])
        else:
            # Por defecto, considerar todo el perímetro como accesible
            puntos_acceso = poligono_lote

    distancia_total_ponderada = 0.0
    peso_total_area = 0.0

    for zona_id, datos_zona in asignacion_zonas.items():
        area_zona = datos_zona.get("area_asignada", 0.0)
        if area_zona <= 0:
            continue

        # Simplificación: usar el centroide de la zona como representación
        # En una implementación real, se haría integrado sobre el área
        centroide_zona = datos_zona.get("centroide", [0, 0])

        # Encontrar distancia mínima a cualquier punto de acceso
        distancia_minima = float('inf')
        for punto_acceso in puntos_acceso:
            dist = math.sqrt((centroide_zona[0] - punto_acceso[0])**2 +
                           (centroide_zona[1] - punto_acceso[1])**2)
            distancia_minima = min(distancia_minima, dist)

        # Normalizar distancia: asumir que la distancia máxima razonable es la diagonal del lote
        if len(poligono_lote) > 0:
            xs = [p[0] for p in poligono_lote]
            ys = [p[1] for p in poligono_lote]
            ancho_max = max(xs) - min(xs) if xs else 100
            alto_max = max(ys) - min(ys) if ys else 100
            distancia_maxima = math.sqrt(ancho_max**2 + alto_max**2)
        else:
            distancia_maxima = 100.0  # Valor por defecto

        if distancia_maxima > 0:
            # Accesibilidad = 1 - (distancia_normalizada), acotada entre 0 y 1
            distancia_normalizada = min(1.0, distancia_minima / distancia_maxima)
            accesibilidad = max(0.0, 1.0 - distancia_normalizada)
        else:
            accesibilidad = 1.0

        # Ponderar por área (zonas más grandes tienen más peso en la evaluación)
        distancia_total_ponderada += accesibilidad * area_zona
        peso_total_area += area_zona

    if peso_total_area == 0:
        return 0.0

    accesibilidad_promedio = distancia_total_ponderada / peso_total_area
    return accesibilidad_promedio

def calcular_puntuacion_vistas(asignacion_zonas, orientaciones_preferidas=None):
    """
    Calcula la calidad de vistas basada en la orientación de las fachadas
    (Simplificado - en realtà requeriría análisis de terreno y obstáculos)
    """
    peso_vistas = PESOS_OPTIMIZACION_DEFAULT.get("views", 0.10)
    if peso_vistas == 0:
        return 1.0

    if orientaciones_preferidas is None:
        # Por defecto, asumir que todas las orientaciones son igualmente buenas
        orientaciones_preferidas = {
            "residencial": {"N": 0.8, "S": 0.9, "E": 0.7, "W": 0.7},  # Prefiere sur (luz) y norte (vistas)
            "comercio": {"N": 0.6, "S": 0.8, "E": 0.7, "W": 0.7},    # Bueno en todas, ligeramente prefiera sur
            "oficinas": {"N": 0.9, "S": 0.6, "E": 0.8, "W": 0.8},    # Prefiere norte (luz indirecta) y este/oeste
            "salud": {"N": 0.8, "S": 0.7, "E": 0.7, "W": 0.7},     # Similar a residencial
        }

    puntuacion_total = 0.0
    total_fachadas_evaluadas = 0

    for zona_id, datos_zona in asignacion_zonas.items():
        uso_zona = datos_zona.get("uso", "residencial")  # Valor por defecto
        orientacion_principal = datos_zona.get("orientacion_principal", "N")  # Norte por defecto

        # Obtener puntuación de preferencia para esta orientación y uso
        preferencias_uso = orientaciones_preferidas.get(uso_zona, {"N": 0.5, "S": 0.5, "E": 0.5, "W": 0.5})
        puntuacion_orientacion = preferencias_uso.get(orientacion_principal, 0.5)

        # Ponderar por área de fachada (simplificado: usar área de la zona)
        area_zona = datos_zona.get("area_asignada", 1.0)
        puntuacion_total += puntuacion_orientacion * area_zona
        total_fachadas_evaluadas += area_zona

    if total_fachadas_evaluadas == 0:
        return 0.5  # Neutral si no hay datos

    return puntuacion_total / total_fachadas_evaluadas

def calcular_puntuacion_servicios(asignacion_zonas, ubicaciones_servicios=None):
    """
    Calcula la proximidad a servicios esenciales y transporte
    """
    peso_servicios = PESOS_OPTIMIZACION_DEFAULT.get("servicios", 0.10)
    if peso_servicios == 0:
        return 1.0

    if ubicaciones_servicios is None:
        # Definir servicios típicos y sus ubicaciones relativas (normalizadas 0-1)
        # En una implementación real, vendrían de análisis de GIS
        ancho_lote_estimado = 100.0  # Valor por defecto
        alto_lote_estimado = 100.0

        # Esquinas y centros de lados como ubicaciones de servicios típicas
        ubicaciones_servicios = {
            "transporte_publico": [(0, 50), (100, 50)],  # Puntos medios de los lados este y oeste
            "escuelas": [(25, 0), (75, 100)],            # Esquinas norte y sur
            "centros_comerciales": [(50, 100), (50, 0)], # Puntos medios norte y sur
            "parques": [(25, 25), (75, 75)]              # Esquinas opuestas
        }

    puntuacion_total = 0.0
    peso_total_servicios = 0.0

    # Pesos relativo por tipo de servicio
    pesos_servicios = {
        "transporte_publico": 0.4,
        "escuelas": 0.3,
        "centros_comerciales": 0.2,
        "parques": 0.1
    }

    for tipo_servicio, puntos in ubicaciones_servicios.items():
        peso_servicio = pesos_servicios.get(tipo_servicio, 0.1)

        distancia_minima_ponderada = 0.0
        peso_area_total = 0.0

        for zona_id, datos_zona in asignacion_zonas.items():
            area_zona = datos_zona.get("area_asignada", 0.0)
            if area_zona <= 0:
                continue

            centroide_zona = datos_zona.get("centroide", [50, 50])  # Centro por defecto

            # Encontrar distancia mínima a este tipo de servicio
            distancia_minima = float('inf')
            for punto_servicio in puntos:
                dist = math.sqrt((centroide_zona[0] - punto_servicio[0])**2 +
                               (centroide_zona[1] - punto_servicio[1])**2)
                distancia_minima = min(distancia_minima, dist)

            # Normalizar distancia (asumiendo diagonal del lote como máximo)
            distancia_maxima = math.sqrt(ancho_lote_estimado**2 + alto_lote_estimado**2)
            if distancia_maxima > 0:
                distancia_normalizada = min(1.0, distancia_minima / distancia_maxima)
                proximidad = max(0.0, 1.0 - distancia_normalizada)  # Cerca = buena puntuación
            else:
                proximidad = 0.5

            distancia_minima_ponderada += proximidad * area_zona
            peso_area_total += area_zona

        if peso_area_total > 0:
            proximidad_promedio = distancia_minima_ponderada / peso_area_total
            puntuacion_total += proximidad_promedio * peso_servicio
            peso_total_servicios += peso_servicio

    if peso_total_servicios == 0:
        return 0.5

    return puntuacion_total / peso_total_servicios

def funcion_objetivo(asignacion_zonas, parametros_entorno, pesos=None, matriz_afinidad=None):
    """
    Función objetivo compuesta que combina todos los criterios de optimización
    """
    if pesos is None:
        pesos = PESOS_OPTIMIZACION_DEFAULT
    if matriz_afinidad is None:
        matriz_afinidad = MATRIZ_AFINIDAD_DEFAULT

    # Calcular cada componente
    score_adyacencia = calcular_puntuacion_adyacencia(asignacion_zonas, matriz_afinidad, pesos)
    score_compactibilidad = calcular_puntuacion_compactibilidad(asignacion_zonas,
                                                              parametros_entorno.get("area_total_disponible", 1000))
    score_accesibilidad = calcular_puntuacion_accesibilidad(asignacion_zonas,
                                                          parametros_entorno.get("poligono_lote", []),
                                                          parametros_entorno.get("puntos_acceso"))
    score_vistas = calcular_puntuacion_vistas(asignacion_zonas,
                                            parametros_entorno.get("orientaciones_preferidas"))
    score_servicios = calcular_puntuacion_servicios(asignacion_zonas,
                                                  parametros_entorno.get("ubicaciones_servicios"))

    # Aplicar pesos
    puntuacion_total = (
        pesos.get("adyacencia", 0.35) * score_adyacencia +
        pesos.get("compactibilidad", 0.25) * score_compactibilidad +
        pesos.get("accesibilidad", 0.20) * score_accesibilidad +
        pesos.get("views", 0.10) * score_vistas +
        pesos.get("servicios", 0.10) * score_servicios
    )

    # Penalizaciones por violar restricciones
    penalizacion_total = 0.0
    for zona_id, datos_zona in asignacion_zonas.items():
        # Verificar altura máxima
        altura_asignada = datos_zona.get("altura", 0)
        altura_maxima_permitida = parametros_entorno.get("altura_maxima_por_zona", {}).get(zona_id, float('inf'))
        if altura_asignada > altura_maxima_permitida:
            penalizacion_total += (altura_asignada - altura_maxima_permitida) / altura_maxima_permitida * 0.5

        # Verificar usos prohibidos (simplificado)
        uso_asignado = datos_zona.get("uso", "")
        usos_prohibidos = parametros_entorno.get("usos_prohibidos_por_zona", {}).get(zona_id, set())
        if uso_asignado in usos_prohibidos:
            penalizacion_total += PENALIZACION_VIOLACION_RESTRICCION

    # Aplicar penalización (máximo 1.0 para no entrar en negativo)
    puntuacion_final = max(0.0, puntuacion_total - min(1.0, penalizacion_total))

    # Bonus por buen aprovechamiento de terreno
    area_utilizada = sum(z.get("area_asignada", 0) for z in asignacion_zonas.values())
    area_disponible = parametros_entorno.get("area_total_disponible", 1000)
    if area_disponible > 0:
        proporcion_utilizada = min(1.0, area_utilizada / area_disponible)
        if proporcion_utilizada > 0.8:  # Bonus si usa más del 80% del terreno
            puntuacion_final = min(1.0, puntuacion_final + BONO_APROVECHAMIENTO_TERRENO * (proporcion_utilizada - 0.8) * 5)

    return puntuacion_final

def generar_vecinos_aleatorios(asignacion_actual, tipos_disponibles, zona_seleccionada=None):
    """
    Genera una solución vecina haciendo cambios aleatorios en la asignación
    """
    if not asignacion_actual:
        return {}

    nueva_asignacion = {k: v.copy() for k, v in asignacion_actual.items()}

    # Elegir una zona al azar para modificar (o la especificada)
    if zona_seleccionada is None and asignacion_actual:
        zona_seleccionada = random.choice(list(asignacion_actual.keys()))

    if zona_seleccionada in nueva_asignacion:
        # Opción 1: Cambiar el uso de la zona
        if random.random() < 0.7 and tipos_disponibles:  # 70% probabilidad de cambiar uso
            uso_actual = nueva_asignacion[zona_seleccionada].get("uso", "residencial")
            tipos_disponibles_filtrados = [t for t in tipos_disponibles if t != uso_actual]
            if tipos_disponibles_filtrados:
                nuevo_uso = random.choice(tipos_disponibles_filtrados)
                nueva_asignacion[zona_seleccionada]["uso"] = nuevo_uso

        # Opción 2: Cambiar el área asignada (manteniendo total constante)
        if random.random() < 0.3 and len(asignacion_actual) > 1:  # 30% probabilidad de redistribuir area
            zona_donante = zona_seleccionada
            zona_receptora = random.choice([z for z in asignacion_actual.keys() if z != zona_donante])

            area_movible = nueva_asignacion[zona_donante].get("area_asignada", 0) * 0.1  # Mover hasta 10%
            area_movible = min(area_movible, nueva_asignacion[zona_donante].get("area_asignada", 0) - 10)  # Dejar mínimo

            if area_movible > 0:
                nueva_asignacion[zona_donante]["area_asignada"] -= area_movible
                nueva_asignacion[zona_receptora]["area_asignada"] = nueva_asignacion[zona_receptora].get("area_asignada", 0) + area_movible

    return nueva_asignacion

def optimizar_asignacion_espacial(zonas_iniciales, tipos_disponibles, parametros_entorno,
                                pesos=None, matriz_afinidad=None, iteraciones=1000):
    """
    Optimiza la asignación de usos a zonas usando búsqueda local simple (Hill Climbing con reinicios)
    """
    if pesos is None:
        pesos = PESOS_OPTIMIZACION_DEFAULT
    if matriz_afinidad is None:
        matriz_afinidad = MATRIZ_AFINIDAD_DEFAULT

    # Solución inicial
    mejor_solucion = {k: v.copy() for k, v in zonas_iniciales.items()}
    mejor_puntuacion = funcion_objetivo(mejor_solucion, parametros_entorno, pesos, matriz_afinidad)

    print(f"Puntuación inicial: {mejor_puntuacion:.4f}")

    # Algoritmo de ascenso de colina con reinicios aleatorios
    for reinicio in range(5):  # 5 reinicios
        solucion_actual = {k: v.copy() for k, v in zonas_iniciales.items()}

        # Aleatorizar solución inicial en cada reinicio
        if reinicio > 0:
            # Reasignar usos aleatoriamente manteniendo áreas
            for zona_id in solucion_actual:
                if random.random() < 0.3 and tipos_disponibles:  # 30% de probabilidad de cambiar uso
                    uso_actual = solucion_actual[zona_id].get("uso", "residencial")
                    tipos_disponibles_filtrados = [t for t in tipos_disponibles if t != uso_actual]
                    if tipos_disponibles_filtrados:
                        nuevo_uso = random.choice(tipos_disponibles_filtrados)
                        solucion_actual[zona_id]["uso"] = nuevo_uso

        puntuacion_actual = funcion_objetivo(solucion_actual, parametros_entorno, pesos, matriz_afinidad)

        # Búsqueda local
        for iteracion in range(iteraciones // 5):  # Distribuir iterations entre reinicios
            vecino = generar_vecinos_aleatorios(solucion_actual, tipos_disponibles)
            puntuacion_vecino = funcion_objetivo(vecino, parametros_entorno, pesos, matriz_afinidad)

            if puntuacion_vecino > puntuacion_actual:
                solucion_actual = vecino
                puntuacion_actual = puntuacion_vecino

                # Actualizar mejor solución global
                if puntuacion_actual > mejor_puntuacion:
                    mejor_solucion = {k: v.copy() for k, v in solucion_actual.items()}
                    mejor_puntuacion = puntuacion_actual
                    print(f"Nueva mejor puntuación: {mejor_puntuacion:.4f} (reinicio {reinicio}, iter {iteracion})")

    print(f"Optimización completada. Mejor puntuación: {mejor_puntuacion:.4f}")
    return mejor_solucion, mejor_puntuacion

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():
    """
    Función principal que procesa las entradas y genera la optimización espacial
    """

    if not RHINO_AVAILABLE:
        print("ADVERTENCIA: Rhino/Grasshopper no disponible. Ejecutando en modo de prueba.")

    print("=== OPTIMIZADOR_ADYACENCIA - Optimización de Colocación Espacial ===")

    # Parsear entradas JSON si es necesario
    programa_espacial_dict = safe_json_parse(programa_espacial_json)
    restricciones_dict = safe_json_parse(restricciones_territoriales_json)
    factores_ponderacion_dict = safe_json_parse(factores_ponderacion) if 'factores_ponderacion' in locals() else {}

    # Extraer información básica
    area_total_disponible = 1000.0  # Valor por defecto
    if programa_espacial_dict:
        # Intentar obtener área del programa espacial
        area_total_disponible = programa_espacial_dict.get("area_total_construida", {}).get("area_neta_total_m2", 1000.0)
    elif restricciones_dict:
        # Intentar obtener de restricciones territoriales
        area_total_disponible = restricciones_dict.get("area_total_construida", {}).get("area_neta_total_m2", 1000.0)

    print(f"Área total disponible: {area_total_disponible:.2f} m2")

    # Extraer polígono del lote si se proporciona
    poligono_lote = []
    if 'poligono_lote' in locals() and poligono_lote:
        if isinstance(poligono_lote, str):
            try:
                poligono_lote = json.loads(poligono_lote)
            except:
                poligono_lote = []
        # Asegurar que es una lista de listas/lista de tuplas
        if isinstance(poligono_lote, list) and len(poligono_lote) > 0:
            if isinstance(poligono_lote[0], (list, tuple)) and len(poligono_lote[0]) >= 2:
                poligono_lote = [[float(p[0]), float(p[1])] for p in poligono_lote]

    print(f"Polígono del lote: {len(poligono_lote)} vértices")

    # Determinar número objetivo de pisos
    numero_pisos_objetivo = 5  # Valor por defecto
    if 'numero_pisos_objetivo' in locals():
        numero_pisos_objetivo = safe_int(numero_pisos_objetivo, 5)
    elif programa_espacial_dict:
        numero_pisos_objetivo = programa_espacial_dict.get("area_total_construida", {}).get("numero_pisos", 5)
    elif restricciones_dict:
        numero_pisos_objetivo = restricciones_dict.get("area_total_construida", {}).get("numero_pisos", 5)

    print(f"Número objetivo de pisos: {numero_pisos_objetivo}")

    # Definir tipos de uso disponibles (basado en lo común en desarrollos urbanos)
    tipos_disponibles = ["residencial", "comercio", "oficinas", "salud", "educacion", "parque", "estacionamiento"]

    # Filtrar por uso principal si se especifica restricción fuerte
    uso_principal_esperado = None
    if programa_espacial_dict:
        uso_principal_esperado = programa_espacial_dict.get("uso_principal_suelo")
    elif restricciones_dict:
        uso_principal_esperado = restricciones_dict.get("uso_principal_suelo")
    elif 'uso_principal_suelo' in locals():
        uso_principal_esperado = uso_principal_suelo

    if uso_principal_esperado and uso_principal_esperado in tipos_disponibles:
        # Enfocar principalmente en el uso permitido, pero permitir complementarios
        tipos_enfoque = [uso_principal_esperado]
        # Agregar usos comúnmente compatibles
        compatibles = {
            "residencial": ["comercio", "parque"],
            "comercio": ["residencial", "oficinas", "estacionamiento"],
            "oficinas": ["comercio", "residencial", "estacionamiento"],
            "salud": ["residencial", "parque"],
            "educacion": ["residencial", "parque"],
            "parque": ["residencial", "comercio", "salud", "educacion"],
            "estacionamiento": ["comercio", "oficinas", "residencial"]
        }
        if uso_principal_esperado in compatibles:
            tipos_enfoque.extend(compatibles[uso_principal_esperado])
        # Eliminar duplicados manteniendo orden
        tipos_disponibles = []
        for t in tipos_enfoque:
            if t not in tipos_disponibles:
                tipos_disponibles.append(t)

    print(f"Tipos de uso considerados: {tipos_disponibles}")

    # ============================================================
    # GENERAR ESTADO INICIAL DE ZONAS
    # ============================================================

    # Estrategia: dividir el área disponible en zonas iniciales
    # Para simplicidad, crear un número razonable de zonas basado en el área y altura

    area_por_zona_objetivo = area_total_disponible / max(1, numero_pisos_objetivo * 4)  # ~4 zonas por piso
    zonas_iniciales = {}

    # Distribuir en una cuadrícula aproximada
    if len(poligono_lote) >= 3:
        # Calcular bounding box del polígono
        xs = [p[0] for p in poligono_lote]
        ys = [p[1] for p in poligono_lote]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        ancho_lote = max_x - min_x
        alto_lote = max_y - min_y

        # Determinar número de divisiones
        divs_x = max(1, int(round(math.sqrt(area_total_disponible / area_por_zona_objetivo))))
        divs_y = max(1, int(round(area_total_disponible / (area_por_zona_objetivo * divs_x))))

        dx = ancho_lote / divs_x if divs_x > 0 else ancho_lote
        dy = alto_lote / divs_y if divs_y > 0 else alto_lote

        zona_id = 0
        for i in range(divs_x):
            for j in range(divs_y):
                if zona_id >= 20:  # Límite razonable de zonas
                    break

                # Calcular centro de la celda
                centro_x = min_x + (i + 0.5) * dx
                centro_y = min_y + (j + 0.5) * dy

                # Área de la celda
                area_celda = dx * dy

                zonas_iniciales[f"zona_{zona_id}"] = {
                    "uso": "residencial",  # Valor por defecto
                    "area_asignada": area_celda,
                    "centroide": [centro_x, centro_y],
                    "perimetro_calculado": 2 * (dx + dy),  # Aproximación para rectángulo
                    "altura": 1  # Altura inicial por piso (se ajustará después)
                }
                zona_id += 1
    else:
        # Fallback: crear zonas simples basadas en cuenta
        num_zonas = max(4, min(16, int(area_total_disponible / 50)))  # Entre 4 y 16 zonas
        area_por_zona = area_total_disponible / num_zonas

        for i in range(num_zonas):
            zonas_iniciales[f"zona_{i}"] = {
                "uso": "residencial",
                "area_asignada": area_por_zona,
                "centroide": [50 + i*10, 50],  # Distribuir en línea x
                "perimetro_calculado": 4 * math.sqrt(area_por_zona),  # Asumiendo cuadrado aproximado
                "altura": 1
            }

    print(f"Zonas iniciales creadas: {len(zonas_iniciales)}")

    # ============================================================
    # CONFIGURAR PARÁMETROS DE ENTORNO PARA LA OPTIMIZACIÓN
    # ============================================================

    parametros_entorno = {
        "area_total_disponible": area_total_disponible,
        "poligono_lote": poligono_lote,
        "puntos_acceso": [],  # Se calcularán si no se proporcionan
        "altura_maxima_por_zona": {},
        "usos_prohibidos_por_zona": {},
        "orientaciones_preferidas": None,
        "ubicaciones_servicios": None
    }

    # Configurar puntos de acceso (simplificado: medio de cada lado del bounding box)
    if len(poligono_lote) >= 3:
        xs = [p[0] for p in poligono_lote]
        ys = [p[1] for p in poligono_lote]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        # Puntos medios de cada lado como acceso típico (calles)
        parametros_entorno["puntos_acceso"] = [
            [(min_x + max_x) / 2, min_y],  # Centro del lado sur
            [(min_x + max_x) / 2, max_y],  # Centro del lado norte
            [min_x, (min_y + max_y) / 2],  # Centro del lado oeste
            [max_x, (min_y + max_y) / 2]   # Centro del lado este
        ]
    else:
        # Puntos de acceso por defecto si no hay polígono
        parametros_entorno["puntos_acceso"] = [[0, 50], [100, 50], [50, 0], [50, 100]]

    # Configurar alturas máximas por zona (desde restricciones)
    if restricciones_dict:
        # Extraer información de altura si está disponible
        altura_maxima_global = restricciones_dict.get("area_total_construida", {}).get("altura_maxima", 15.0)  # metros
        altura_piso_tipica = 3.0  # metros por piso
        pisos_maximos = int(altura_maxima_global / altura_piso_tipica) if altura_piso_tipica > 0 else numero_pisos_objetivo

        # Aplicar la misma altura máxima a todas las zonas (simplificación)
        for zona_id in zonas_iniciales:
            parametros_entorno["altura_maxima_por_zona"][zona_id] = float(pisos_maximos)
    else:
        # Altura máxima por defecto
        altura_por_defecto = numero_pisos_objetivo * 3  # 3m por piso
        for zona_id in zonas_iniciales:
            parametros_entorno["altura_maxima_por_zona"][zona_id] = float(altura_por_defecto)

    # Configurar usos prohibidos (por ahora, ninguno por defecto)
    # En una implementación real, vendría de análisis de zonificación y restricciones

    # Configurar pesos de optimización (sobrescribir con los proporcionados si existen)
    pesos_optimizacion = PESOS_OPTIMIZACION_DEFAULT.copy()
    if factores_ponderacion_dict:
        for key, value in factores_ponderacion_dict.items():
            if key in pesos_optimizacion:
                pesos_optimizacion[key] = float(value)

    print(f"Pesos de optimización: {pesos_optimizacion}")

    # ============================================================
    # EJECUTAR OPTIMIZACIÓN
    # ============================================================

    print("\nIniciando optimización...")

    # Usar la matriz de afinidad por defecto (podría personalizarse basado en inputs)
    matriz_afinidad_usar = MATRIZ_AFINIDAD_DEFAULT

    # Ejecutar algoritmo de optimización
    asignacion_optima, puntuacion_optima = optimizar_asignacion_espacial(
        zonas_iniciales,
        tipos_disponibles,
        parametros_entorno,
        pesos=pesos_optimizacion,
        matriz_afinidad=matriz_afinidad_usar,
        iteraciones=500  # Número razonable para demo
    )

    # ============================================================
    # POST-PROCESAMIENTO: DISTRIBUIR ALTURAS POR PISO
    # ============================================================

    # Distribuir la altura total disponible entre las zonas basado en algún criterio
    # Por ahora, asignación uniforme simplificada
    altura_total_disponible = numero_pisos_objetivo * 3.0  # metros

    for zona_id, datos_zona in asignacion_optima.items():
        # Asignar altura basada en área (zonas más grandes pueden tener más altura)
        area_zona = datos_zona.get("area_asignada", 0)
        area_total = sum(z.get("area_asignada", 0) for z in asignacion_optima.values())

        if area_total > 0:
            fraccion_area = area_zona / area_total
            altura_asignada = altura_total_disponible * (0.5 + 0.5 * fraccion_area)  # Entre 50% y 100% de altura promedio
        else:
            altura_asignada = altura_total_disponible / len(asignacion_optima) if asignacion_optima else 0

        # Limitar por altura máxima permitida
        altura_maxima = parametros_entorno["altura_maxima_por_zona"].get(zona_id, float('inf'))
        altura_asignada = min(altura_asignada, altura_maxima)

        # Convertir a número de pisos (redondear hacia abajo)
        pisos_asignados = max(1, int(altura_asignada / 3.0))  # Mínimo 1 piso
        datos_zona["pisos"] = pisos_asignados
        datos_zona["altura_actual"] = pisos_asignados * 3.0

    # ============================================================
    # GENERAR RESULTADOS DETALLADOS
    # ============================================================

    # Calcular puntuaciones detalladas para reporte
    puntuaciones_detalladas = {
        "adyacencia": calcular_puntuacion_adyacencia(asignacion_optima, matriz_afinidad_usar),
        "compactibilidad": calcular_puntuacion_compactibilidad(asignacion_optima, area_total_disponible),
        "accesibilidad": calcular_puntuacion_accesibilidad(asignacion_optima, poligono_lote, parametros_entorno["puntos_acceso"]),
        "vistas": calcular_puntuacion_vistas(asignacion_optima),
        "servicios": calcular_puntuacion_servicios(asignacion_optima)
    }

    # Preparar resultado de distribución espacial óptima
    resultado_distribucion = {
        "metadata": {
            "version": "1.0.0",
            "fecha_optimizacion": datetime.now().isoformat(),
            "algoritmo": "Hill Climbing with Random Restarts",
            "iteraciones_totales": 500,
            "zonas_optimizadas": len(asignacion_optima),
            "tipos_uso_considerados": tipos_disponibles,
            "area_total_disponible_m2": area_total_disponible,
            "numero_pisos_objetivo": numero_pisos_objetivo
        },
        "parametros_optimizacion": {
            "pesos_utilizados": pesos_optimizacion,
            "pesos_predeterminados": PESOS_OPTIMIZACION_DEFAULT,
            "matriz_afinidad_utilizada": "predeterminada (personalizable)"
        },
        "distribucion_optima": {
            "zonas": {},
            "resumen_por_uso": {},
            "estadisticas_globales": {}
        },
        "puntuaciones_detalladas": puntuaciones_detalladas,
        "puntuacion_global": puntuacion_optima
    }

    # Llenar detalles de zonas
    area_total_asignada = 0.0
    volumen_total_construido = 0.0
    conteo_por_uso = defaultdict(int)
    area_por_uso = defaultdict(float)
    volumen_por_uso = defaultdict(float)

    for zona_id, datos_zona in asignacion_optima.items():
        uso_zona = datos_zona.get("uso", "desconocido")
        area_zona = datos_zona.get("area_asignada", 0.0)
        pisos_zona = datos_zona.get("pisos", 1)
        altura_zona = datos_zona.get("altura_actual", pisos_zona * 3.0)
        volumen_zona = area_zona * altura_zona

        # Información de la zona
        resultado_distribucion["distribucion_optima"]["zonas"][zona_id] = {
            "uso": uso_zona,
            "area_asignada_m2": area_zona,
            "pisos": pisos_zona,
            "altura_m": altura_zona,
            "volumen_m3": volumen_zona,
            "centroide": datos_zona.get("centroide", [0, 0]),
            "adyacentes": datos_zona.get("adyacentes", []),
            "perimetro_m": datos_zona.get("perimetro_calculado", 0.0)
        }

        # Acumular para estadísticas
        area_total_asignada += area_zona
        volumen_total_construido += volumen_zona
        conteo_por_uso[uso_zona] += 1
        area_por_uso[uso_zona] += area_zona
        volumen_por_uso[uso_zona] += volumen_zona

    # Resumen por uso
    for uso in tipos_disponibles:
        if conteo_por_uso[uso] > 0:
            resultado_distribucion["distribucion_optima"]["resumen_por_uso"][uso] = {
                "zonas_count": conteo_por_uso[uso],
                "area_total_m2": area_por_uso[uso],
                "volumen_total_m3": volumen_por_uso[uso],
                "porcentaje_area_total": (area_por_uso[uso] / area_total_asignada * 100) if area_total_asignada > 0 else 0,
                "altura_promedio_m": (sum(
                    z.get("altura_actual", 0) for z in asignacion_optima.values()
                    if z.get("uso") == uso
                ) / conteo_por_uso[uso]) if conteo_por_uso[uso] > 0 else 0
            }

    # Estadísticas globales
    resultado_distribucion["distribucion_optima"]["estadisticas_globales"] = {
        "area_total_asignada_m2": area_total_asignada,
        "area_total_disponible_m2": area_total_disponible,
        "porcentaje_aprovechamiento": (area_total_asignada / area_total_disponible * 100) if area_total_disponible > 0 else 0,
        "volumen_total_construido_m3": volumen_total_construido,
        "indice_construccion": volumen_total_construido / (area_total_disponible * (numero_pisos_objetivo * 3.0)) if area_total_disponible > 0 and numero_pisos_objetivo > 0 else 0,
        "altura_promedio_ponderada": (sum(
            z.get("altura_actual", 0) * z.get("area_asignada", 0)
            for z in asignacion_optima.values()
        ) / area_total_asignada) if area_total_asignada > 0 else 0,
        "distribución_uso": dict(conteo_por_uso)
    }

    # Evaluar cumplimiento de matriz de adyacencia
    matriz_evaluacion = {
        "adyacencias_ideales": [],
        "adyacencias_actuales": [],
        "cumplimiento_por_par": {},
        "puntuacion_adyacencia": puntuaciones_detalladas["adyacencia"]
    }

    # Analizar adyacencias actuales vs ideales
    for zona_id, datos_zona in asignacion_optima.items():
        uso_zona = datos_zona.get("uso", "desconocido")
        zonas_adyacentes = datos_zona.get("adyacentes", [])

        for vecino_id in zonas_adyacentes:
            if vecino_id in asignacion_optima:
                uso_vecino = asignacion_optima[vecino_id].get("uso", "desconocido")
                par_ordenado = tuple(sorted([uso_zona, uso_vecino]))

                afinidad_ideal = matriz_afinidad_usar.get((uso_zona, uso_vecino), 0.5)
                afinidad_ideal_inversa = matriz_afinidad_usar.get((uso_vecino, uso_zona), 0.5)
                afinidad_ideal_promedio = (afinidad_ideal + afinidad_ideal_inversa) / 2.0

                clave_par = f"{uso_zona}-{uso_vecino}"
                if clave_par not in matriz_evaluacion["cumplimiento_por_par"]:
                    matriz_evaluacion["cumplimiento_por_par"][clave_par] = {
                        "adyacencias_contadas": 0,
                        "suma_afinidad_actual": 0.0,
                        "afinidad_ideal_promedio": afinidad_ideal_promedio
                    }

                matriz_evaluacion["cumplimiento_por_par"][clave_par]["adyacencias_contadas"] += 1
                matriz_evaluacion["cumplimiento_por_par"][clave_par]["suma_afinidad_actual"] += 1.0  # Asumiendo que si están adyacentes, cumplimiento = 1

                # Registrar para reporte (evitar duplicados)
                par_desc = f"{uso_zona} ↔ {uso_vecino}"
                if par_desc not in [item["descripcion"] for item in matriz_evaluacion["adyacencias_actuales"]]:
                    matriz_evaluacion["adyacencias_actuales"].append({
                        "tipo1": uso_zona,
                        "tipo2": uso_vecino,
                        "descripcion": par_desc,
                        "afinidad_ideal": afinidad_ideal_promedio,
                        "estado": "adyacente"
                    })

    # Calcular promedios de cumplimiento
    for par_key, datos in matriz_evaluacion["cumplimiento_por_par"].items():
        if datos["adyacencias_contadas"] > 0:
            cumplimiento_promedio = datos["suma_afinidad_actual"] / datos["adyacencias_contadas"]
            datos["cumplimiento_relativo"] = cumplimiento_promedio / datos["afinidad_ideal_promedio"] if datos["afinidad_ideal_promedio"] > 0 else 0
            # Ideal sería 1.0 (cumplimos exactamente lo ideal), > 1.0 significa superamos lo ideal

    # Generar reporte legible
    reporte_lineas = [
        "=" * 70,
        "OPTIMIZACIÓN DE COLOCACIÓN ESPACIAL - INFORME DE RESULTADOS",
        "=" * 70,
        f"Fecha de optimización: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Algoritmo utilizado: Hill Climbing with Random Restarts",
        f"Iteraciones totales: 500",
        "",
        "PARÁMETROS DE ENTRADA:",
        f"  Área total disponible: {area_total_disponible:.2f} m²",
        f"  Número objetivo de pisos: {numero_pisos_objetivo}",
        f"  Volumen teórico máximo: {area_total_disponible * (numero_pisos_objetivo * 3.0):.2f} m³",
        f"  Polígono de lote: {len(poligono_lote)} vértices" if len(poligono_lote) > 0 else "  Polígono de lote: No proporcionado (usando coordenadas genéricas)",
        f"  Puntos de acceso considerados: {len(parametros_entorno['puntos_acceso'])}",
        f"  Tipos de uso evaluados: {', '.join(tipos_disponibles)}",
        "",
        "PESOS DE OPTIMIZACIÓN UTILIZADOS:",
    ]

    for peso_where

    descripcion_peso = {
        "adyacencia": "Cumplimiento de preferencias de adyacencia entre usos",
        "compactibilidad": "Compactibilidad del volumen construido (relativa al perímetro)",
        "accesibilidad": "Accesibilidad desde vías principales y transporte",
        "vistas": "Calidad de vistas y orientación de fachadas",
        "servicios": "Proximidad a servicios esenciales (escuelas, comercios, parques)"
    }

    for peso, valor in pesos_optimizacion.items():
        desc = descripcion_peso.get(peso, "Factor de optimización")
        reporte_lineas.append(f"  {peso.capitalize():12} : {valor:.2f} ({desc})")

    reporte_lineas.extend([
        "",
        "RESULTADOS DE LA OPTIMIZACIÓN:",
        f"  Puntuación global obtenida: {puntuacion_optima:.4f} (0.0-1.0)",
        "",
        "DESGLOSE DE PUNTUACIONES POR CRITERIO:",
    ])

    for criterio, puntuacion in puntuaciones_detalladas.items():
        nombre_criterio = criterio.capitalize()
        if criterio == "adyacencia":
            nombre_criterio = "Adyacencia"
        elif criterio == "compactibilidad":
            nombre_criterio = "Compactibilidad"
        elif criterio == "accesibilidad":
            nombre_criterio = "Accesibilidad"
        elif criterio == "vistas":
            nombre_criterio = "Vistas"
        elif criterio == "servicios":
            nombre_criterio = "Servicios"
        porcentaje = puntuacion * 100
        estado = "EXCELENTE" if porcentaje >= 85 else "BUENO" if porcentaje >= 70 else "ACEPTABLE" if porcentaje >= 50 else "INSUFICIENTE"
        reporte_lineas.append(f"  {nombre_criterio:12} : {porcentaje:5.1f}% [{estado}]")

    reporte_lineas.extend([
        "",
        "DISTRIBUCIÓN OPTIMIZADA POR USO:",
    ])

    for uso, resumen in resultado_distribucion["distribucion_optima"]["resumen_por_uso"].items():
        porcentaje_area = resumen["porcentaje_area_total"]
        barra_progreso = "█" * int(porcentaje_area / 5) + "░" * (20 - int(porcentaje_area / 5))
        rango_altura = f"{resumen.get('altura_promedio_m', 0):.1f}m"
        num_zonas = resumen["zonas_count"]
        area_total = resumen["area_total_m2"]
        linea = f"  {uso.upper():12} : {num_zonas:2d} zonas | {area_total:6.1f} m² ({porcentaje_area:5.1f}%) | Altura prom: {rango_altura:>6} | {barra_progreso}"
        reporte_lineas.append(linea)

    reporte_lineas.extend([
        "",
        "ESTADÍSTICAS GLOBALES DEL DISEÑO:",
        f"  Área total asignada: {area_total_asignada:.2f} m²",
        f"  Área total disponible: {area_total_disponible:.2f} m²",
        f"  Porcentaje de aprovechamiento: {resultado_distribucion['distribucion_optima']['estadisticas_globales']['porcentaje_aprovechamiento']:.1f}%",
        f"  Volumen total construido: {volumen_total_construido:.2f} m³",
        f"  Índice de construcción (volumen/volumen teórico): {resultado_distribucion['distribucion_optima']['estadisticas_globales']['indice_construccion']:.3f}",
        f"  Altura promedio ponderada: {resultado_distribucion['distribucion_optima']['estadisticas_globales']['altura_promedio_ponderada']:.1f} m",
        f"  Número promedio de zonas por uso: {sum(conteo_por_uso.values())/len([u for u in conteo_por_uso if conteo_por_uso[u]>0]) if len([u for u in conteo_por_uso if conteo_por_uso[u]>0]) > 0 else 0:.1f}",
        "",
        "ANÁLISIS DE ADYACENCIAS:",
        f"  Puntuación de cumplimiento de adyacencias: {puntuaciones_detalladas['adyacencia']*100:.1f}%",
    ])

    # Mostrar algunos pares de adyacencia clave
    pares_mostrados = 0
    for par_key, datos in matriz_evaluacion["cumplimiento_por_par"].items():
        if pares_mostrados >= 5:  # Limitar salida
            break
        if datos["adyacencias_contadas"] > 0:
            cumplimiento_rel = datos.get("cumplimiento_relativo", 0)
            porcentaje_cumplimiento = min(100, cumplimiento_rel * 100)
            estado = "✓ CUMPLE" if porcentaje_cumplimiento >= 80 else "△ PARCIAL" if porcentaje_cumplimiento >= 50 else "✗ DEFICIENTE"
            tipos = par_key.split("-")
            if len(tipos) == 2:
                reporte_lineas.append(f"  {tipos[0].upper():10} ↔ {tipos[1].upper():10} : {porcentaje_cumplimiento:5.1f}% {estado}")
                pares_mostrados += 1

    if pares_mostrados == 0:
        # Mostrar algunas adyacencias encontradas de todas formas
        adyac_mostradas = 0
        for adyac in matriz_evaluacion["adyacencias_actuales"][:5]:
            if adyac_mostradas < 5:
                afin = adyac["afinidad_ideal"]
                estado = "✓ ALINEADO" if afin >= 0.7 else "△ NEUTRAL" if afin >= 0.4 else "✗ CONTRAINDICADO"
                reporte_lineas.append(f"  {adyac['tipo1'].upper():10} ↔ {adyac['tipo2'].upper():10} : afinidad ideal {afin:.2f} [{estado}]")
                adyac_mostradas += 1

    reporte_lineas.extend([
        "",
        "RECOMENDACIONES DE IMPLEMENTACIÓN:",
    ])

    # Generar recomendaciones basado en resultados
    if puntuacion_optima >= 0.8:
        reco_general = "EL DISEÑO OBTENIDO ES EXCELENTE - Implementar con mínima ajustes"
    elif puntuacion_optima >= 0.65:
        reco_general = "EL DISEÑO OBTENIDO ES BUENO - Considerar pequeños ajustes para mejorar áreas específicas"
    elif puntuacion_optima >= 0.5:
        reco_general = "EL DISEÑO OBTENIDO ES ACEPTABLE - Revisar parcialmente la configuración de uso y ubicación"
    else:
        reco_general = "EL DISEÑO NECESITA MEJORAS SIGNIFICATIVAS - Considerar redefinir restricciones o pesos de optimización"

    reporte_lineas.append(f"  Calidad general: {reco_general}")

    # Recomendaciones específicas por criterio bajo
    if puntuaciones_detalladas["adyacencia"] < 0.6:
        rec_adyac = "Revisar la ubicación de usos incompatibles (ej. industrial cerca de residencial)"
        if puntuaciones_detalladas["adyacencia"] < 0.4:
            rec_adyac = "FUERTE recomendación: Separar usos conflictivos según matriz de afinidad"
        reporte_lineas.append(f"  Adyacencia: {rec_adyac}")

    if puntuaciones_detalladas["accesibilidad"] < 0.6:
        rec_acce = "Mejorar la ubicación de usos críticos cerca de puntos de acceso (transporte, vías principales)"
        if puntuaciones_detalladas["accesibilidad"] < 0.4:
            rec_acce = "FUERTE recomendación: Reubicar usos de alta generación de tráfico cerca de accesos principales"
        reporte_lineas.append(f"  Accesibilidad: {rec_acce}")

    if puntuaciones_detalladas["servicios"] < 0.6:
        rec_serv = "Considerar la proximity a servicios como escuelas, parques y transporte público"
        if puntuaciones_detalladas["servicios"] < 0.4:
            rec_serv = "FUERTE recomendación: Asegurar acceso caminable a servicios básicos para usos residenciales"
        reporte_lineas.append(f"  Servicios: {rec_serv}")

    if porcentaje_aprovech := resultado_distribucion['distribucion_optima']['estadisticas_globales']['porcentaje_aprovechamiento']:
        if porcentaje_aprovech < 70:
            rec_aprov = "Aumentar la densidad de construcción para mejor aprovechamiento del terreno"
            if porcentaje_aprovech < 50:
                rec_aprov = "FUERTE recomendación: El diseño está subutilizando significativamente el terreno disponible"
            reporte_lineas.append(f"  Aprovechamiento de terreno: {rec_aprov}")
        elif porcentaje_aprovech > 95:
            rec_aprov = "Verificar regulaciones de retiros y espacios públicos - posible sobreaprovechamiento"
            reporte_lineas.append(f"  Aprovechamiento de terreno: {rec_aprov}")

    if puntuaciones_detalladas["compactibilidad"] < 0.5:
        rec_compact = "Considerar formas más compactas para reducir costo de infraestructura y mejorar eficiencia energética"
        if puntuaciones_detalladas["compactibilidad"] < 0.3:
            rec_compact = "FUERTE recomendación: Evitar diseños dispersos o en forma de lanza que aumentan costos de servicios"
        reporte_lineas.append(f"  Compactibilidad: {rec_compact}")

    # Resumen final
    area_utilizada_pct = resultado_distribucion['distribucion_optima']['estadisticas_globales']['porcentaje_aprovechamiento']
    aprovechamiento_adecuado = 60 <= area_utilizada_pct <= 90  # Rango razonable

    viabilidad_general = (
        puntuacion_optima >= 0.6 and
        aprovechamiento_adecuado and
        puntuaciones_detalladas["adyacencia"] >= 0.5
    )

    recomendacion_final = "PROCEDER CON EL DESARROLLO" if viabilidad_general else "REVISAR Y AJUSTAR ANTES DE PROCEDER"

    if puntuacion_optima >= 0.8:
        recomendacion_final = "APROBAR DISEÑO - EXCELENTE CUMPLIMIENTO DE OBJETIVOS"
    elif puntuacion_optima < 0.4:
        recomendacion_final = "REDISEÑAR NECESARIO - BAJA CUMPLIMIENTO DE OBJETIVOS"

    reporte_lineas.extend([
        "",
        "CONCLUSIÓN Y RECOMENDACIÓN FINAL:",
        f"  {recomendacion_final}",
        f"  Puntuación global: {puntuacion_optima:.3f}/1.000",
        f"  Aprovechamiento de terreno: {area_utilizada_pct:.1f}% ({'ADECUADO' if aprovechamiento_adecuado else 'FUERA DE RANGO ÓPTIMO'})",
        f"  Cumplimiento de adyacencias: {puntuaciones_detalladas['adyacencia']*100:.1f}% ({'ACEPTABLE' if puntuaciones_detalladas['adyacencia'] >= 0.6 else 'REQUIERE ATENCIÓN'})",
        "",
        "PRÓXIMOS PASOS SUGERIDOS:",
        "  1. Validar resultados con estudios de impacto de tráfico y medioambient",
        "  2. Detallar estándares de construcción por zona de uso",
        "  3. Elaborar planos de distribución detallados por piso",
        "  4. Realizar estudio de viabilidad económica basado en la distribución óptima",
        "  5. Consultar con la comunidad y stakeholders relevantes",
        "",
        "=" * 70
    ])

    reporte_texto = "\n".join(reporte_lineas)

    # Preparar métricas espaciales para salida JSON
    metricas_espaciales = {
        "metadata": {
            "version": "1.0.0",
            "fecha_calculo": datetime.now().isoformat(),
            "descripcion": "Métricas de calidad del diseño espacial optimizado"
        },
        "metricas_principales": {
            "puntuacion_global": puntuacion_optima,
            "aprovechamiento_terreno_pct": area_utilizada_pct,
            "indice_construccion": resultado_distribucion['distribucion_optima']['estadisticas_globales']['indice_construccion'],
            "altura_promedio_ponderada_m": resultado_distribucion['distribucion_optima']['estadisticas_globales']['altura_promedio_ponderada'],
            "densidad_poblacional_estimada": None  # Requeriría supuestos de ocupación
        },
        "metricas_por_criterio": {
            "adyacencia": puntuaciones_detalladas["adyacencia"],
            "compactibilidad": puntuaciones_detalladas["compactibilidad"],
            "accesibilidad": puntuaciones_detalladas["accesibilidad"],
            "vistas": puntuaciones_detalladas["vistas"],
            "servicios": puntuaciones_detalladas["servicios"]
        },
        "distribucion_uso": resultado_distribucion['distribucion_optima']['estadisticas_globales']['distribución_uso'],
        "eficiencia_espacial": {
            "relacion_perimetro_area": (sum(z.get("perimetro_calculado", 0) for z in asignacion_optima.values()) /
                                      (2 * math.sqrt(area_total_asignada * 3.14159)) if area_total_asignada > 0 else 0),
            "compactibilidad_relativa": puntuaciones_detalladas["compactibilidad"],
            "indice_forma": 4 * 3.14159 * area_total_asignada / (sum(z.get("perimetro_calculado", 0) for z in asignacion_optima.values()) ** 2) if sum(z.get("perimetro_calculado", 0) for z in asignacion_optima.values()) > 0 else 0
        }
    }

    # Evaluación de adyacencia detallada
    evaluacion_adyacencia = {
        "metadata": {
            "version": "1.0.0",
            "fecha_evaluacion": datetime.now().isoformat(),
            "descripcion": "Evaluación detallada del cumplimiento de preferencias de adyacencia"
        },
        "matriz_evaluacion": matriz_evaluacion,
        "resumen_cumplimiento": {
            "puntaje_promedio": puntuaciones_detalladas["adyacencia"],
            "interpretacion": "EXCELENTE" if puntuaciones_detalladas["adyacencia"] >= 0.85 else
                            "BUENO" if puntuaciones_detalladas["adyacencia"] >= 0.7 else
                            "ACEPTABLE" if puntuaciones_detalladas["adyacencia"] >= 0.5 else
                            "INSUFICIENTE"
        }
    }

    # Convertir resultados a JSON para salida
    distribucion_json = json.dumps(resultado_distribucion, indent=2, ensure_ascii=False)
    metricas_json = json.dumps(metricas_espaciales, indent=2, ensure_ascii=False)
    adyacencia_json = json.dumps(evaluacion_adyacencia, indent=2, ensure_ascii=False)

    print("\n=== RESUMEN DE EJECUCIÓN ===")
    print(f"Optimización completada para {len(asignacion_optima)} zonas")
    print(f"Puntuación global: {puntuacion_optima:.4f}")
    print(f"Aprovechamiento de terreno: {area_utilizada_pct:.1f}%")
    print(f"Volumen construido: {volumen_total_construido:.2f} m³")

    # Guardar resultados en archivos
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    distribucion_path = os.path.join(output_dir, "distribucion_espacial_optima.json")
    with open(distribucion_path, 'w', encoding='utf-8') as f:
        f.write(distribucion_json)

    metricas_path = os.path.join(output_dir, "metricas_espaciales.json")
    with open(metricas_path, 'w', encoding='utf-8') as f:
        f.write(metricas_json)

    adyacencia_path = os.path.join(output_dir, "matriz_adyacencia_evaluada.json")
    with open(adyacencia_path, 'w', encoding='utf-8') as f:
        f.write(adyacencia_json)

    reporte_path = os.path.join(output_dir, "reporte_optimizacion.txt")
    with open(reporte_path, 'w', encoding='utf-8') as f:
        f.write(reporte_texto)

    print(f"\nArchivos guardados en: {output_dir}")
    print(f"  - distribucion_espacial_optima.json")
    print(f"  - metricas_espaciales.json")
    print(f"  - matriz_adyacencia_evaluada.json")
    print(f"  - reporte_optimizacion.txt")

    # Salidas para Grasshopper
    return distribucion_json, adyacencia_json, metricas_json, reporte_texto

# Ejecutar si se ejecuta como script principal
if __name__ == "__main__":
    try:
        dist_result, adyac_result, metrica_result, reporte_result = main()
    except Exception as e:
        print(f"Error en OPTIMIZADOR_ADYACENCIA: {str(e)}")
        import traceback
        traceback.print_exc()
        # Devolver error en formato JSON para Grasshopper
        error_result = {
            "error": str(e),
            "mensaje": "Error en la optimización de colocación espacial"
        }
        dist_result = json.dumps(error_result, indent=2, ensure_ascii=False)
        adyac_result = json.dumps(error_result, indent=2, ensure_ascii=False)
        metrica_result = json.dumps(error_result, indent=2, ensure_ascii=False)
        reporte_result = f"ERROR: {str(e)}"

    # Para Grasshopper, necesitamos asignar los resultados a variables de salida
    # En GH Python Script, esto se hace automáticamente al retornar o asignar a variables
    # Asumiendo que las salidas se llaman "distribucion_json", "adyacencia_json", "metricas_json", "reporte_texto"
    distribucion_json = dist_result
    adyacencia_json = adyac_result
    metricas_json = metrica_result
    reporte_texto = reporte_result