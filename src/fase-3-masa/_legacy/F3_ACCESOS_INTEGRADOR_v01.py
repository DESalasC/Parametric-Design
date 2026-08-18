#!/usr/bin/env python3
"""
ACCESOS_INTEGRADOR_v01.py - Integrador de Accesos y Cálculo de Patios
GH Python Script para Grasshopper (GH Player compatible)

ENTRADAS (via Grasshopper):
  - distribucion_espacial_json: JSON con distribución óptima de usos (output de OPTIMIZADOR_ADYACENCIA_v01.py)
  - poligono_lote: Polígono del lote como lista de puntos [[x1,y1], [x2,y2], ...]
  - calles_perimetro: Información de calles perimetrales (opcional)
  - requisitos_patio: Requerimientos mínimos de patios según uso y normativa (opcional)
  - RETIROS_POT: Retiros normativos según POT (opcional)
  - FACTORES_CORRECCION: Factores de ajuste para cálculos de accesibilidad y patios

SALIDAS:
  - accesos_calculados.json: JSON con cálculos de accesibilidad, distancias a vialidad y puntos de acceso
  - patios_calculados.json: JSON con cálculos de áreas de patio requeridas y provistas
  - redes_peatonales.json: Propuesta de red de circulación peatonal interna
  - reporte_accesos_patios.txt: Reporte legible del análisis de accesos y patios
"""

import json
import math
import os
from typing import Dict, List, Tuple, Any, Optional, Set
from collections import defaultdict

# Try to import Rhino-specific modules, provide fallbacks for testing
try:
    import rhinoscriptsyntax as rs
    RHINO_AVAILABLE = True
except ImportError:
    RHINO_ISPONIBLE = False
    # Mock functions for testing/non-Rhino environments
    class MockRs:
        @staticmethod
        def Distance(point1, point2):
            return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

        @staticmethod
        def PointInPlanarClosedCurve(point, polygon):
            return 1  # Simplified: assume inside

        @staticmethod
        def AreaPolygon(points):
            return 0.0 if len(points) < 3 else 1000.0  # Área aproximada

        @staticmethod
        def CurveLength(curve):
            return 0.0

        @staticmethod
        +BoundingBox(objects):
            return [[0,0,0], [100,100,0]]  # Bounding box ficticio

        @staticmethod
        def CurveIntersectCurves(curve1, curve2):
            return []  # No intersections

        @staticmethod
        def OffsetCurve(curve, point, distance, tolerance):
            return None  # Simplified

        @staticmethod
        def OffsetPolyline(points, distance):
            return []  # Simplified

    rs = MockRs()

# ============================================================
# CONFIGURACIÓN DE PARÁMETROS POR DEFECTO
# ============================================================

# Requerimientos mínimos de patio por tipo de uso (m² por m² de construcción)
# Valores típicos basados en normas de habitabilidad y bienestar
REQUISITOS_PATIO_POR_USO = {
    "residencial": {
        "patio_minimo_por_vivienda": 8.0,  # m² por vivienda
        "area_construida_reference": 80.0,  # m² por vivienda de referencia
        "factor_ajuste": 0.10,  # 10% del área construida como patio mínimo
        "patio_absoluto_minimo": 4.0  # m² mínimo absoluto por unidad
    },
    "comercio": {
        "patio_minimo_por_local": 4.0,
        "area_construida_reference": 50.0,
        "factor_ajuste": 0.05,  # 5% del área construida
        "patio_absoluto_minimo": 2.0
    },
    "oficinas": {
        "patio_minimo_por_oficina": 3.0,
        "area_construida_reference": 25.0,
        "factor_ajuste": 0.04,  # 4% del área construida
        "patio_absoluto_minimo": 1.5
    },
    "salud": {
        "patio_minimo_por_cama": 6.0,
        "area_construida_reference": 30.0,
        "factor_ajuste": 0.08,  # 8% del área construida
        "patio_absoluto_minimo": 3.0
    },
    "educacion": {
        "patio_minimo_por_aula": 10.0,
        "area_construida_reference": 60.0,
        "factor_ajuste": 0.12,  # 12% del área construida
        "patio_absoluto_minimo": 5.0
    },
    "parque": {
        "patio_minimo_por_hectarea": 200.0,  # Los parques son esencialmente patios
        "area_construida_reference": 1000.0,
        "factor_ajuste": 0.80,  # 80% del área (máximo espacio verde)
        "patio_absoluto_minimo": 50.0
    },
    "estacionamiento": {
        "patio_minimo_por_plaza": 1.0,
        "area_construida_reference": 12.5,
        "factor_ajuste": 0.02,  # 2% del área construida
        "patio_absoluto_minimo": 0.5
    }
}

# Factores de corrección por accesibilidad (pesos para diferentes tipos de acceso)
FACTORES_ACCESIBILIDAD = {
    "via_principal": 1.0,      # Acceso directo a vía arterial o colectora
    "via_secundaria": 0.7,     # Acceso vía local o secundaria
    "transporte_publico": 0.9, # Proximidad a paradas de transporte
    "peonal": 0.8,             # Acceso principalmente peatonal
    "servicios": 0.6,          # Acceso a servicios básicos
    "verde": 0.5               # Acceso a zonas verdes/parques
}

# Distancias máximas recomendadas para buena accesibilidad (metros)
DISTANCIAS_MAXIMO_ACCESO = {
    "via_principal": 50.0,
    "via_secundaria": 30.0,
    "transporte_publico": 200.0,
    "peonal": 100.0,
    "servicios": 150.0,
    "verde": 100.0
}

# Factores de ponderación para el score final de accesibilidad
PESOS_ACCESIBILIDAD = {
    "via_principal": 0.30,
    "via_secundaria": 0.20,
    "transporte_publico": 0.25,
    "peonal": 0.15,
    "servicios": 0.05,
    "verde": 0.05
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

def punto_medio_segmento(p1, p2):
    """Calcula el punto medio entre dos puntos"""
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

def longitud_poligono(poligono):
    """Calcula la longitud total de un poligono (perímetro)"""
    if len(poligono) < 2:
        return 0.0

    longitud = 0.0
    for i in range(len(poligono)):
        p1 = poligono[i]
        p2 = poligono[(i + 1) % len(poligono)]
        longitud += math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    return longitud

# ============================================================
# FUNCIONES DE CÁLCULO DE ACCESOS
# ============================================================

def calcular_accesibilidad_zona(centroide_zona, poligono_lote, calles_perimetro=None, factores_correccion=None):
    """
    Calcula el score de accesibilidad de una zona basado en su distancia
    a diferentes tipos de acceso
    """
    if factores_correccion is None:
        factores_correccion = FACTORES_ACCESIBILIDAD

    if calles_perimetro is None:
        # Generar calles perimetrales aproximadas desde el polígono del lote
        calles_perimetro = {}
        if len(poligono_lote) >= 3:
            # Simplificado: asumir que cada lado del lote tiene acceso
            # En realidad, vendría de datos GIS
            lados = []
            for i in range(len(poligono_lote)):
                p1 = poligono_lote[i]
                p2 = poligono_lote[(i + 1) % len(poligono_lote)]
                lados.append((p1, p2))

            # Clasificar lados como principales o secundarios (simplificado)
            if len(lados) >= 2:
                # Asumir que los lados más largos son vías principales
                longitudes_lados = []
                for i, (p1, p2) in enumerate(lados):
                    largo = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
                    longitudes_lados.append((largo, i, p1, p2))

                longitudes_lados.sort(reverse=True)  # Ordenar de mayor a menor

                llamadas_principales = []
                llamadas_secundarias = []

                # Los dos más largos son principales, el resto secundarios
                for i, (largo, idx, p1, p2) in enumerate(longitudes_lados):
                    if i < 2 and len(lados) >= 2:
                        llamadas_principales.append((p1, p2))
                    else:
                        llamadas_secundarias.append((p1, p2))

                calles_perimetro["via_principal"] = llamadas_principales
                calles_perimetro["via_secundaria"] = llamadas_secundarias
            else:
                # Pocos lados, tratar todo como secundario
                calles_perimetro["via_secundaria"] = lados
        else:
            # Sin polígono válido, usar valores por defecto
            calles_perimetro = {
                "via_principal": [[[0, 50], [100, 50]]],  # Línea horizontal central
                "via_secundaria": [[[50, 0], [50, 100]]]   # Línea vertical central
            }

    # Calcular distancia mínima a cada tipo de acceso
    puntuaciones_acceso = {}
    detalles_acceso = {}

    for tipo_acceso, peso in PESOS_ACCESIBILIDAD.items():
        factor_correccion = factores_correccion.get(tipo_acceso, 1.0)
        distancia_maxima = DISTANCIAS_MAXIMO_ACCESO.get(tipo_acceso, 100.0)

        distancia_minima = float('inf')
        segmentos_acceso = calles_perimetro.get(tipo_acceso, [])

        # Si no hay segmentos definidos para este tipo, buscar en todos
        if not segmentos_acceso:
            # Combinar todos los segmentos disponibles
            all_segmentos = []
            for tipo_acceso in calles_perimetro:
                all_segmentos.extend(calles_perimetro[tipo_acceso])

            if not all_segmentos and calles_perimetro:
                # Tomar todos los valores del diccionario
                for segmento_list in calles_perimetro.values():
                    all_segmentos.extend(segmento_list)

            segmentos_acceso = all_segmentos

        # Calcular distancia mínima a cualquier segmento de este tipo de acceso
        for segmento in segmentos_acceso:
            if len(segmento) == 2:  # Segmento definido por dos puntos
                p1, p2 = segmento
                dist = distancia_punto_a_segmento(
                    centroide_zona[0], centroide_zona[1],
                    p1[0], p1[1], p2[0], p2[1]
                )
                distancia_minima = min(distancia_minima, dist)

        # Si no se encontraron segmentos, usar distancia al borde del polígono como fallback
        if distancia_minima == float('inf'):
            distancia_minima = distancia_punto_a_poligono(centroide_zona, poligono_lote)

        # Normalizar distancia (0 = perfecto acceso, 1 = acceso pobre)
        if distancia_maxima > 0:
            distancia_normalizada = min(1.0, distancia_minima / distancia_maxima)
            puntuacion_acceso = max(0.0, 1.0 - distancia_normalizada)  # Invertir para que alto = bueno
        else:
            puntuacion_acceso = 1.0  # Si distancia máxima es 0, acceso perfecto

        # Aplicar factor de corrección
        puntuacion_ajustada = min(1.0, puntuacion_acceso * factor_correccion)

        puntuaciones_acceso[tipo_acceso] = puntuacion_ajustada
        detalles_acceso[tipo_acceso] = {
            "distancia_minima_m": distancia_minima if distancia_minima != float('inf') else 0.0,
            "distancia_maxima_recomendada_m": distancia_maxima,
            "distancia_normalizada": distancia_normalizada if distancia_maxima > 0 else 0.0,
            "puntuacion_base": puntuacion_acceso,
            "factor_correccion": factor_correccion,
            "puntuacion_final": puntuacion_ajustada
        }

    # Calcular puntuación ponderada total
    puntuacion_total = sum(
        puntuaciones_acceso[tipo] * PESOS_ACCESIBILIDAD[tipo]
        for tipo in PESOS_ACCESIBILIDAD
    )

    return {
        "puntuacion_accesibilidad": puntuacion_total,
        "puntuaciones_por_tipo": puntuaciones_acceso,
        "detalles_por_tipo": detalles_acceso,
        "centroide_evaluado": centroide_zona,
        "accesibilidad_clasificacion": (
            "EXCELENTE" if puntuacion_total >= 0.85 else
            "BUENO" if puntuacion_total >= 0.70 else
            "ACEPTABLE" if puntuacion_total >= 0.50 else
            "INSUFICIENTE"
        )
    }

def calcular_red_peatonal_optima(zonas, poligono_lote):
    """
    Genera una propuesta básica de red de circulación peatonal interna
    basada en la distribución espacial de zonas
    """
    # Extraer centroides de zonas
    nodos = []
    nodos_info = []

    for zona_id, datos_zona in zonas.items():
        centroide = datos_zona.get("centroide", [0, 0])
        uso = datos_zona.get("uso", "desconocido")
        area = datos_zona.get("area_asignada", 0)

        nodos.append(centroide)
        nodos_info.append({
            "zona_id": zona_id,
            "uso": uso,
            "area_m2": area,
            "centroide": centroide
        })

    # Agregar puntos de acceso al perímetro como nodos adicionales
    if len(poligono_lote) >= 3:
        # Puntos medios de cada lado como accesos peatonales
        for i in range(len(poligono_lote)):
            p1 = poligono_lote[i]
            p2 = poligono_lote[(i + 1) % len(poligono_lote)]
            punto_medio = punto_medio_segmento(p1, p2)
            nodos.append(punto_medio)
            nodos_info.append({
                "tipo": "acceso_perimetro",
                "lado_index": i,
                "punto_inicial": p1,
                "punto_final": p2,
                "centroide": punto_medio
            })

    # Algoritmo simple de MST (Minimum Spanning Tree) para conectar todos los nodos
    # Versión simplificada usando algoritmo de Prim

    if len(nodos) < 2:
        return {
            "nodos": nodos_info,
            "aristas": [],
            "longitud_total_m": 0.0,
            "eficiencia_red": 0.0
        }

    # Iniciar MST desde el primer nodo
    nodos_no_visitados = set(range(len(nodos)))
    nodos_visitados = {0}  # Empezar desde el nodo 0
    nodos_no_visitados.remove(0)

    aristas_mst = []
    longitud_total = 0.0

    while nodos_no_visitados:
        # Encontrar la arista más corta que conecte un nodo visitado con uno no visitado
        mejor_distancia = float('inf')
        mejor_origen = None
        mejor_destino = None

        for origen in nodos_visitados:
            for destino in nodos_no_visitados:
                # Calcular distancia euclidiana
                dx = nodos[destino][0] - nodos[origen][0]
                dy = nodos[destino][1] - nodos[origen][1]
                distancia = math.sqrt(dx*dx + dy*dy)

                if distancia < mejor_distancia:
                    mejor_distancia = distancia
                    mejor_origen = origen
                    mejor_destino = destino

        # Agregar la mejor arista encontrada
        if mejor_origen is not None and mejor_destino is not None:
            aristas_mst.append({
                "desde": mejor_origen,
                "hacia": mejor_destino,
                "distancia_m": mejor_distancia,
                "desde_info": nodos_info[mejor_origen],
                "hacia_info": nodos_info[mejor_destino]
            })

            longitud_total += mejor_distancia
            nodos_visitados.add(mejor_destino)
            nodos_no_visitados.remove(mejor_destino)
        else:
            # No se encontró conexión (no debería pasar en conjunto conexo)
            break

    # Calcular eficiencia de la red (relación con el grafo completo)
    # En un grafo completo, la longitud total sería la suma de todas las aristas posibles
    # Pero usamos una aproximación: razón entre MST y el perímetro conveniente
    perimetro_lote = longitud_poligono(poligono_lote) if len(poligono_lote) >= 3 else 100.0
    eficiencia = min(1.0, perimetro_lote / max(longitud_total, 0.1)) if longitud_total > 0 else 0.0

    return {
        "nodos": nodos_info,
        "aristas": aristas_mst,
        "longitud_total_m": longitud_total,
        "numero_nodos": len(nodos),
        "numero_aristas": len(aristas_mst),
        "eficiencia_red": eficiencia,
        "longitud_promedio_arista": longitud_total / len(aristas_mst) if aristas_mst else 0.0
    }

# ============================================================
# FUNCIONES DE CÁLCULO DE PATIOS
# ============================================================

def calcular_requisitos_patio_zona(datos_zona, requisitos_por_uso=None):
    """
    Calcula el área de patio requerida para una zona específica
    basado en su uso y características
    """
    if requisitos_por_uso is None:
        requisitos_por_uso = REQUISITOS_PATIO_POR_USO

    uso = datos_zona.get("uso", "residencial")
    area_construida = datos_zona.get("area_asignada", 0.0)
    pisos = datos_zona.get("pisos", 1)

    # Si no se especifican pisos, estimar basado en área (asumiendo edificios bajos)
    if pisos == 0 and area_construida > 0:
        # Estimación aproximada: 80 m² por piso promedio
        pisos = max(1, int(area_construida / 80.0))

    area_total_construida = area_construida * pisos

    requerimiento = requisitos_por_uso.get(uso, requisitos_por_uso["residencial"])

    patio_requerido_m2 = 0.0
    detalle_calculo = ""

    if uso == "residencial":
        # Estimar número de viviendas basado en área estándar
        area_por_vivienda = requerimiento.get("area_construida_reference", 80.0)
        num_viviendas = max(1, int(area_total_construida / area_por_vivienda))
        patio_por_vivienda = requerimiento.get("patio_minimo_por_vivienda", 8.0)
        patio_requerido_m2 = num_viviendas * patio_por_vivienda

        # También calcular por porcentaje
        factor_ajuste = requerimiento.get("factor_ajuste", 0.10)
        patio_por_porcentaje = area_total_construida * factor_ajuste

        # Tomar el máximo de ambos métodos para ser conservador
        patio_requerido_m2 = max(patio_requerido_m2, patio_por_porcentaje)
        detalle_calculo = f"{num_viviendas} viviendas × {patio_por_vivienda} m²/vivienda = {num_viviendas * patio_por_vivienda} m² (mínimo por vivienda)"
        detalle_calculo += f" vs {area_total_construida:.1f} m² × {factor_ajuste} = {patio_por_porcentaje:.1f} m² (por porcentaje)"

    elif uso == "comercio":
        area_por_local = requerimiento.get("area_construida_reference", 50.0)
        num_locales = max(1, int(area_total_construida / area_por_local))
        patio_por_local = requerimiento.get("patio_minimo_por_local", 4.0)
        patio_requerido_m2 = num_locales * patio_por_local

        factor_ajuste = requerimiento.get("factor_ajuste", 0.05)
        patio_por_porcentaje = area_total_construida * factor_ajuste
        patio_requerido_m2 = max(patio_requerido_m2, patio_por_porcentaje)
        detalle_calculo = f"{num_locales} locales × {patio_por_local} m²/local = {num_locales * patio_por_local} m²"
        detalle_calculo += f" vs {area_total_construida:.1f} m² × {factor_ajuste} = {patio_por_porcentaje:.1f} m²"

    elif uso == "oficinas":
        area_por_oficina = requerimiento.get("area_construida_reference", 25.0)
        num_oficinas = max(1, int(area_total_construida / area_por_oficina))
        patio_por_oficina = requerimiento.get("patio_minimo_por_oficina", 3.0)
        patio_requerido_m2 = num_oficinas * patio_por_oficina

        factor_ajuste = requerimiento.get("factor_ajuste", 0.04)
        patio_por_porcentaje = area_total_construida * factor_ajuste
        patio_requerido_m2 = max(patio_requerido_m2, patio_por_porcentaje)
        detalle_calculo = f"{num_oficinas} oficinas × {patio_por_oficina} m²/oficina = {num_oficinas * patio_por_oficina} m²"
        detalle_calculo += f" vs {area_total_construida:.1f} m² × {factor_ajuste} = {patio_por_porcentaje:.1f} m²"

    elif uso == "salud":
        # Estimación: 1 cama por 25 m² construidos (varía según tipo de instalación)
        area_por_cama = requerimiento.get("area_construida_reference", 30.0)
        num_camas = max(1, int(area_total_construida / area_por_cama))
        patio_por_cama = requerimiento.get("patio_minimo_por_cama", 6.0)
        patio_requerido_m2 = num_camas * patio_por_cama

        factor_ajuste = requerimiento.get("factor_ajuste", 0.08)
        patio_por_porcentaje = area_total_construida * factor_ajuste
        patio_requerido_m2 = max(patio_requerido_m2, patio_por_porcentaje)
        detalle_calculo = f"{num_camas} camas × {patio_por_cama} m²/cama = {num_camas * patio_por_cama} m²"
        detalle_calculo += f" vs {area_total_construida:.1f} m² × {factor_ajuste} = {patio_por_porcentaje:.1f} m²"

    elif uso == "educacion":
        # Estimación: 1 aula por 50 m² construidos
        area_por_aula = requerimiento.get("area_construida_reference", 60.0)
        num_aulas = max(1, int(area_total_construida / area_por_aula))
        patio_por_aula = requerimiento.get("patio_minimo_por_aula", 10.0)
        patio_requerido_m2 = num_aulas * patio_por_aula

        factor_ajuste = requerimiento.get("factor_ajuste", 0.12)
        patio_por_porcentaje = area_total_construida * factor_ajuste
        patio_requerido_m2 = max(patio_requerido_m2, patio_por_porcentaje)
        detalle_calculo = f"{num_aulas} aulas × {patio_por_aula} m²/aula = {num_aulas * patio_por_aula} m²"
        detalle_calculo += f" vs {area_total_construida:.1f} m² × {factor_ajuste} = {patio_por_porcentaje:.1f} m²"

    elif uso == "parque":
        # Para parques, el "patio" es esencialmente el área verde
        factor_ajuste = requerimiento.get("factor_ajuste", 0.80)
        patio_requerido_m2 = area_total_construida * factor_ajuste
        patio_absoluto = requerimiento.get("patio_absoluto_minimo", 50.0)
        patio_requerido_m2 = max(patio_requerido_m2, patio_absoluto)
        detalle_calculo = f"{area_total_construida:.1f} m² × {factor_ajuste} = {patio_requerido_m2:.1f} m² (mínimo {patio_absoluto} m²)"

    else:  # estacionamiento y otros
        area_por_unidad = requerimiento.get("area_construida_reference", 12.5)
        num_unidades = max(1, int(area_total_construida / area_por_unidad))
        patio_por_unidad = requerimiento.get("patio_minimo_por_plaza", 1.0)
        patio_requerido_m2 = num_unidades * patio_por_unidad

        factor_ajuste = requerimiento.get("factor_ajuste", 0.02)
        patio_por_porcentaje = area_total_construida * factor_ajuste
        patio_requerido_m2 = max(patio_requerido_mado, patio_por_porcentaje)
        detalle_calculo = f"{num_unidades} unidades × {patio_por_unidad} m²/unidad = {num_unidades * patio_por_unidad} m²"
        detalle_calculo += f" vs {area_total_construida:.1f} m² × {factor_ajuste} = {patio_por_porcentaje:.1f} m²"

    # Aplicar mínimo absoluto
    patio_absoluto_minimo = requerimiento.get("patio_absoluto_minimo", 0.0)
    patio_requerido_m2 = max(patio_requerido_m2, patio_absoluto_minimo)

    return {
        "patio_requerido_m2": patio_requerido_m2,
        "area_construida_m2": area_total_construida,
        "pisos_calculados": pisos,
        "detalle_calculo": detalle_calculo,
        "porcentaje_sobre_construido": (patio_requerido_m2 / area_total_construida * 100) if area_total_construida > 0 else 0
    }

def calcular_patios_provistos(zona, poligono_lote):
    """
    Estima el área de patio disponible basado en el espacio no construido
    alrededor de la zona (simplificación)
    """
    # En una implementación real, esto requeriría análisis detallado de
    # polígonos de construcción y cálculo de áreas libres
    # Aquí usamos una aproximación basada en el hecho de que no todo el lote se construye

    area_zona = zona.get("area_asignada", 0.0)

    # Suponemos que un porcentaje del lote total queda como espacio libre
    # Este porcentaje debería venir de los retiros normativos y espacios comunes
    area_total_lote = calcular_area_poligono(poligono_lote) if len(poligono_lote) >= 3 else 1000.0

    if area_total_lote > 0:
        fraccion_construida_total = sum(
            z.get("area_asignada", 0) * z.get("pisos", 1)
            for z in zona.values()
            if isinstance(zona, dict)  # Esto está mal, debería iterar sobre todas las zonas
        ) / (area_total_lote * 3)  # Asumiendo 3 pisos promedio

        # Pero esta función recibe una zona específica, no todas
        # Vamos a simplificar: asumir que hay un factor de retiro promedio
        factor_retiro_promedio = 0.25  # 25% del área de lote como espacio libre no construido
        area_libre_estimada = area_total_lote * factor_retiro_promedio

        # Distribuir proporcionalmente el área libre entre las zonas construidas
        area_construida_total = sum(
            z.get("area_asignada", 0) * z.get("pisos", 1)
            for z in zona.values()
        ) if isinstance(zona, dict) and "area_asignada" in next(iter(zona.values()), {}) else 100.0

        if area_construida_total > 0:
            proporcion_zona = (area_zona * zona.get("pisos", 1)) / area_construida_total
            patio_disponible_estimado = area_libre_estimada * proporcion_zona
        else:
            patio_disponible_estimado = area_libre_estimada / len(zona) if zona else 0.0
    else:
        patio_disponible_estimado = 10.0  # Valor por defecto

    return {
        "patio_disponible_m2": max(0.0, patio_disponible_estimado),
        "metodo_estimacion": "proporcional_a_area_construida_con_factor_retiro_fijo",
        "factor_retiro_asumido": 0.25
    }

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():
    """
    Función principal que procesa las entradas y genera el análisis de accesos y patios
    """

    if not RHINO_AVAILABLE:
        print("ADVERTENCIA: Rhino/Grasshopper no disponible. Ejecutando en modo de prueba.")

    print("=== ACCESOS_INTEGRADOR_v01 - Análisis de Accesos y Patios ===")

    # Parsear entradas JSON
    distribucion_dict = safe_json_parse(distribucion_espacial_json) if 'distribucion_espacial_json' in locals() else {}
    # Si no hay distribución espacial, crear una de ejemplo para testing
    if not distribucion_dict or "distribucion_optima" not in distribucion_dict:
        print("Usando datos de distribución de ejemplo para testing...")
        # Crear distribución de ejemplo basada en lo que normalmente produciría OPTIMIZADOR_ADYACENCIA
        distribucion_dict = {
            "distribucion_optima": {
                "zonas": {
                    "zona_0": {
                        "uso": "residencial",
                        "area_asignada_m2": 150.0,
                        "pisos": 3,
                        "centroide": [25.0, 25.0],
                        "adyacentes": ["zona_1", "zona_2"]
                    },
                    "zona_1": {
                        "uso": "comercio",
                        "area_asignada_m2": 80.0,
                        "pisos": 2,
                        "centroide": [75.0, 25.0],
                        "adyacentes": ["zona_0", "zona_3"]
                    },
                    "zona_2": {
                        "uso": "oficinas",
                        "area_asignada_m2": 120.0,
                        "pisos": 4,
                        "centroide": [25.0, 75.0],
                        "adyacentes": ["zona_0", "zona_3"]
                    },
                    "zona_3": {
                        "uso": "parque",
                        "area_asignada_m2": 200.0,
                        "pisos": 0,
                        "centroide": [75.0, 75.0],
                        "adyacentes": ["zona_1", "zona_2"]
                    }
                }
            }
        }

    # Polígono del lote
    poligono_lote = []
    if 'poligono_lote' in locals() and poligono_lote:
        if isinstance(poligono_lote, str):
            try:
                poligono_lote = json.loads(poligono_lote)
            except:
                poligono_lote = []
        # Asegurar formato correcto
        if isinstance(poligono_lote, list) and len(poligono_lote) > 0:
            if isinstance(poligono_lote[0], (list, tuple)) and len(poligono_lote[0]) >= 2:
                poligono_lote = [[float(p[0]), float(p[1])] for p in poligono_lote]

    # Si no hay polígono, crear uno por defecto
    if not poligono_lote or len(poligono_lote) < 3:
        print("Advertencia: Polígono de lote no válido o no proporcionado. Usando polígono por defecto.")
        poligono_lote = [[0, 0], [100, 0], [100, 100], [0, 100]]  # Cuadrado de 100x100

    print(f"Polígono del lote: {len(poligono_lote)} vértices")
    area_lote = calcular_area_poligono(poligono_lote)
    print(f"Área del lote: {area_lote:.2f} m²")

    # Calles perimetro (opcional, se generará si no se proporciona)
    calles_perimetro = None
    if 'calles_perimetro' in locals() and calles_perimetro:
        if isinstance(calles_perimetro, str):
            try:
                calles_perimetro = json.loads(calles_perimetro)
            except:
                calles_perimetro = None

    # Factores de corrección (opcional)
    factores_correccion = None
    if 'factores_correccion' in locals() and factores_correccion:
        if isinstance(factores_correccion, str):
            try:
                factores_correccion = json.loads(factores_correccion)
            except:
                factores_correccion = None

    # Requisitos de patio (opcional)
    requisitos_patio = None
    if 'requisitos_patio' in locals() and requisitos_patio:
        if isinstance(requisitos_patio, str):
            try:
                requisitos_patio = json.loads(requisitos_patio)
            except:
                requisitos_patio = None

    # ============================================================
    # PROCESAR ZONAS DE LA DISTRIBUCIÓN ESPACIAL
    # ============================================================

    zonas_distribuidas = {}
    if "distribucion_optima" in distribucion_dict and "zonas" in distribucion_dict["distribucion_optima"]:
        zonas_data = distribucion_dict["distribucion_optima"]["zonas"]

        for zona_id, datos_zona in zonas_data.items():
            # Convertir formato de salida a formato interno
            zonas_distribuidas[zona_id] = {
                "uso": datos_zona.get("uso", "residencial"),
                "area_asignada": datos_zona.get("area_asignada_m2", 0.0),
                "pisos": datos_zona.get("pisos", 1),
                "altura_actual": datos_zona.get("altura_m", 0.0),
                "centroide": datos_zona.get("centroide", [0.0, 0.0]),
                "adyacentes": datos_zona.get("adyacentes", []),
                "perimetro_calculado": datos_zona.get("perimetro_m", 0.0)
            }

    if not zonas_distribuidas:
        # Crear zonas de ejemplo si no se pudo extraer
        print("Creando zonas de ejemplo para procesamiento...")
        zonas_distribuidas = {
            "zona_0": {
                "uso": "residencial",
                "area_asignada": 150.0,
                "pisos": 3,
                "altura_actual": 9.0,
                "centroide": [25.0, 25.0],
                "adyacentes": ["zona_1", "zona_2"],
                "perimetro_calculado": 50.0
            },
            "zona_1": {
                "uso": "comercio",
                "area_asignada": 80.0,
                "pisos": 2,
                "altura_actual": 6.0,
                "centroide": [75.0, 25.0],
                "adyacentes": ["zona_0", "zona_3"],
                "perimetro_calculado": 40.0
            },
            "zona_2": {
                "uso": "oficinas",
                "area_asignada": 120.0,
                "pisos": 4,
                "altura_actual": 12.0,
                "centroide": [25.0, 75.0],
                "adyacentes": ["zona_0", "zona_3"],
                "perimetro_calculado": 60.0
            },
            "zona_3": {
                "uso": "parque",
                "area_asignada": 200.0,
                "pisos": 0,
                "altura_actual": 0.0,
                "centroide": [75.0, 75.0],
                "adyacentes": ["zona_1", "zona_2"],
                "perimetro_calculado": 60.0
            }
        }

    print(f"Procesando {len(zonas_distribuidas)} zonas de distribución espacial...")

    # ============================================================
    # CALCULAR ACCESIBILIDAD PARA CADA ZONA
    # ============================================================

    resultados_accesibilidad = {}
    resumen_accesibilidad = {
        "puntuacion_promedio": 0.0,
        "zonas_excelentes": 0,
        "zonas_buenas": 0,
        "zonas_aceptables": 0,
        "zonas_insuficientes": 0,
        "detalles_por_zona": {}
    }

    suma_puntuaciones = 0.0

    for zona_id, datos_zona in zonas_distribuidas.items():
        acceso_result = calcular_accesibilidad_zona(
            datos_zona["centroide"],
            poligono_lote,
            calles_perimetro,
            factores_correccion
        )

        resultados_accesibilidad[zona_id] = acceso_result
        puntuacion = acceso_result["puntuacion_accesibilidad"]
        suma_puntuaciones += puntuacion

        # Clasificar por nivel de accesibilidad
        clasificacion = acceso_result["accesibilidad_clasificacion"]
        if clasificacion == "EXCELENTE":
            resumen_accesibilidad["zonas_excelentes"] += 1
        elif clasificacion == "BUENO":
            resumen_accesibilidad["zonas_buenas"] += 1
        elif clasificacion == "ACEPTABLE":
            resumen_accesibilidad["zonas_aceptables"] += 1
        else:
            resumen_accesibilidad["zonas_insuficientes"] += 1

        resumen_accesibilidad["detalles_por_zona"][zona_id] = {
            "uso": datos_zona["uso"],
            "puntuacion_accesibilidad": puntuacion,
            "clasificacion": clasificacion,
            "distancia_minima_via_principal_m": acceso_result["detalles_por_tipo"].get("via_principal", {}).get("distancia_minima_m", 0.0),
            "distancia_minima_transporte_m": acceso_result["detalles_por_tipo"].get("transporte_publico", {}).get("distancia_minima_m", 0.0)
        }

    resumen_accesibilidad["puntuacion_promedio"] = suma_puntuaciones / len(zonas_distribuidas) if zonas_distribuidas else 0.0

    # ============================================================
    # CALCULAR REQUISITOS Y DISPONIBILIDAD DE PATIOS
    # ============================================================

    resultados_patios = {}
    resumen_patios = {
        "area_patio_requerido_total_m2": 0.0,
        "area_patio_disponible_estimada_total_m2": 0.0,
        "deficit_patio_total_m2": 0.0,
        "superávit_patio_total_m2": 0.0,
        "porcentaje_cumplimiento_promedio": 0.0,
        "zonas_con_deficit": 0,
        "zonas_con_superavit": 0,
        "detalles_por_zona": {}
    }

    total_requerido = 0.0
    total_disponible = 0.0
    suma_porcentaje_cumplimiento = 0.0

    for zona_id, datos_zona in zonas_distribuidas.items():
        # Calcular requerimiento
        requerimiento_result = calcular_requisitos_patio_zona(datos_zona, requisitos_patio)
        requerimiento_m2 = requerimiento_result["patio_requerido_m2"]

        # Calcular disponible (estimado)
        disponible_result = calcular_patios_provistos(datos_zona, poligono_lote)
        disponible_m2 = disponible_result["patio_disponible_m2"]

        # Calcular déficit/superávit
        deficit = max(0.0, requerimiento_m2 - disponible_m2)
        superavit = max(0.0, disponible_m2 - requerimiento_m2)

        # Porcentaje de cumplimiento para esta zona
        porcentaje_cumplimiento = (disponible_m2 / requerimiento_m2 * 100) if requerimiento_m2 > 0 else (100.0 if disponible_mado > 0 else 0.0)

        # Actualizar totales
        total_requerido += requerimiento_m2
        total_disponible += disponible_m2
        suma_porcentaje_cumplimiento += porcentaje_cumplimiento

        if deficit > 0:
            resumen_patios["zonas_con_deficit"] += 1
        if superavit > 0:
            resumen_patios["zonas_con_superavit"] += 1

        resultados_patios[zona_id] = {
            "uso": datos_zona["uso"],
            "area_asignada_m2": datos_zona["area_asignada"],
            "pisos": datos_zona["pisos"],
            "area_construida_m2": requerimiento_result["area_construida_m2"],
            "patio_requerido_m2": requerimiento_m2,
            "patio_disponible_estimado_m2": disponible_m2,
            "deficit_m2": deficit,
            "superavit_m2": superavit,
            "porcentaje_cumplimiento": porcentaje_cumplimiento,
            "detalle_calculo_requerido": requerimiento_result["detalle_calculo"],
            "metodo_disponible": disponible_result["metodo_estimacion"]
        }

        resumen_patios["detalles_por_zona"][zona_id] = {
            "uso": datos_zona["uso"],
            "patio_requerido_m2": requerimiento_m2,
            "patio_disponible_m2": disponible_m2,
            "porcentaje_cumplimiento": porcentaje_cumplimiento,
            "estado": "CUMPLE" if porcentaje_cumplimiento >= 90 else "PARCIAL" if porcentaje_cumplimiento >= 70 else "DEFICIT"
        }

    # Calcular promedios y totales
    resumen_patios["area_patio_requerido_total_m2"] = total_requerido
    resumen_patios["area_patio_disponible_estimada_total_m2"] = total_disponible
    resumen_patios["deficit_patio_total_m2"] = max(0.0, total_requerido - total_disponible)
    resumen_patios["superavit_patio_total_m2"] = max(0.0, total_disponible - total_requerido)
    resumen_patios["porcentaje_cumplimiento_promedio"] = suma_porcentaje_cumplimiento / len(zonas_distribuidas) if zonas_distribuidas else 0.0

    # ============================================================
    # GENERAR RED PEATONAL
    # ============================================================

    red_peatonale = calcular_red_peatonal_optima(zonas_distribuidas, poligono_lote)

    # ============================================================
    # PREPARAR RESULTADOS PARA SALIDA
    # ============================================================

    # Resultado de accesibilidad
    resultado_accesos = {
        "metadata": {
            "version": "1.0.0",
            "fecha_calculo": datetime.now().isoformat(),
            "descripcion": "Análisis de accesibilidad y conexiones a vialidad"
        },
        "parametros_utilizados": {
            "factores_accesibilidad": FACTORES_ACCESIBILIDAD,
            "pesos_accesibilidad": PESOS_ACCESIBILIDAD,
            "distancias_maximos_recomendados": DISTANCIAS_MAXIMO_ACCESO,
            "factores_correccion_aplicados": factores_correccion if factores_correccion else "valores_predeterminados",
            "calles_perimetro_procesadas": bool(calles_perimetro)
        },
        "resumen_general": {
            "puntuacion_promedio_accesibilidad": resumen_accesibilidad["puntuacion_promedio"],
            "zonas_analizadas": len(zonas_distribuidas),
            "distribución_calificaciones": {
                "excelente": resumen_accesibilidad["zonas_excelentes"],
                "bueno": resumen_accesibilidad["zonas_buenas"],
                "aceptable": resumen_accesibilidad["zonas_aceptables"],
                "insuficiente": resumen_accesibilidad["zonas_insuficientes"]
            },
            "accesibilidad_general_clasificacion": (
                "EXCELENTE" if resumen_accesibilidad["puntuacion_promedio"] >= 0.85 else
                "BUENO" if resumen_accesibilidad["puntuacion_promedio"] >= 0.70 else
                "ACEPTABLE" if resumen_accesibilidad["puntuacion_promedio"] >= 0.50 else
                "INSUFICIENTE"
            )
        },
        "detalles_por_zona": resumen_accesibilidad["detalles_por_zona"],
        "recomendaciones_mejora": []
    }

    # Agregar recomendaciones de mejora basado en resultados
    if resumen_accesibilidad["puntuacion_promedio"] < 0.7:
        resultado_accesos["recomendaciones_mejora"].append(
            "Considerar redistribuir usos para mejorar přístos a vías principales y transporte público"
        )

    zonas_bajas_acceso = [
        (zona_id, datos["puntuacion_accesibilidad"])
        for zona_id, datos in resumen_accesibilidad["detalles_por_zona"].items()
        if datos["puntuacion_accesibilidad"] < 0.5
    ]

    if zonas_bajas_acceso:
        zonas_bajas_acceso.sort(key=lambda x: x[1])  # Ordenar por puntuación ascendente
        peor_zona_id, peor_puntuacion = zonas_bajas_acceso[0]
        peor_zona_uso = zonas_distribuidas[peor_zona_id]["uso"]
        resultado_accesos["recomendaciones_mejora"].append(
            f"Revisar ubicación de zona '{peor_zona_id}' ({peor_zona_uso}) - accesibilidad muy baja ({peor_puntuacion:.2f})"
        )

    # Resultado de patios
    resultado_patios = {
        "metadata": {
            "version": "1.0.0",
            "fecha_calculo": datetime.now().isoformat(),
            "descripcion": "Cálculo de requisitos y disponibilidad de áreas de patio"
        },
        "parametros_utilizados": {
            "requisitos_por_uso_base": REQUISITOS_PATIO_POR_USO,
            "requisitos_patio_personalizados": requisitos_patio if requisitos_patio else "valores_predeterminados"
        },
        "resumen_general": {
            "area_patio_requerido_total_m2": resumen_patios["area_patio_requerido_total_m2"],
            "area_patio_disponible_estimada_total_m2": resumen_patios["area_patio_disponible_estimada_total_m2"],
            "deficit_patio_total_m2": resumen_patios["deficit_patio_total_m2"],
            "superavit_patio_total_m2": resumen_patios["superavit_patio_total_m2"],
            "porcentaje_cumplimiento_promedio": resumen_patios["porcentaje_cumplimiento_promedio"],
            "cumplimiento_general": (
                "EXCELENTE" if resumen_patios["porcentaje_cumplimiento_promedio"] >= 95 else
                "BUENO" if resumen_patios["porcentaje_cumplimiento_promedio"] >= 85 else
                "ACEPTABLE" if resumen_patios["porcentaje_cumplimiento_promedio"] >= 70 else
                "INSUFICIENTE"
            ),
            "zonas_analizadas": len(zonas_distribuidas),
            "zonas_con_deficit": resumen_patios["zonas_con_deficit"],
            "zonas_con_superavit": resumen_patios["zonas_con_superavit"]
        },
        "detalles_por_zona": resumen_patios["detalles_por_zona"],
        "recomendaciones": []
    }

    # Agregar recomendaciones de patios
    if resumen_patios["deficit_patio_total_m2"] > 0:
        resultado_patios["recomendaciones"].append(
            f"Déficit total de patio: {resumen_patios['deficit_patio_total_m2']:.1f} m². Considerar aumentar retiros o reducir densidad"
        )

    zonas_con_deficit_severo = [
        (zona_id, datos["porcentaje_cumplimiento"])
        for zona_id, datos in resumen_patios["detalles_por_zona"].items()
        if datos["porcentaje_cumplimiento"] < 50
    ]

    if zonas_con_deficit_severo:
        resultado_patios["recomendaciones"].append(
            f"{len(zonas_con_deficit_severo)} zonas con déficit severo de patio (<50% cumplimiento). Revisar diseño de esas zonas."
        )

    if resumen_patios["porcentaje_cumplimiento_promedio"] >= 90:
        resultado_patios["recomendaciones"].append(
            "Cumplimiento de requisitos de patio adecuado. El diseño proporciona suficientes espacios abiertos."
        )

    # Resultado de red peatonal
    resultado_red_peatonale = {
        "metadata": {
            "version": "1.0.0",
            "fecha_calculo": datetime.now().isoformat(),
            "descripcion": "Propuesta de red de circulación peatonal interna"
        },
        "parametros_utilizados": {
            "metodo_conectividad": "Árbol de Expansión Mínimo (MST) - Algoritmo de Prim",
            "nodos_considerados": "centroides de zonas + accesos perimetrales"
        },
        "estadisticas_red": {
            "total_nodos": red_peatonale["numero_nodos"],
            "total_aristas": red_peatonale["numero_aristas"],
            "longitud_total_m": red_peatonale["longitud_total_m"],
            "longitud_promedio_arista_m": red_peatonale["longitud_promedio_arista"],
            "eficiencia_red": red_peatonale["eficiencia_red"]
        },
        "nodos": red_peatonale["nodos"],
        "conexiones": [
            {
                "desde_zona": arista["desde_info"].get("zona_id", f"nodo_{arista['desde']}"),
                "hacia_zona": arista["hacia_info"].get("zona_id", f"nodo_{arista['hacia']}"),
                "distancia_m": arista["distancia_m"],
                "tipo_conexion": "zonas_adjacentes" if (
                    arista["desde_info"].get("zona_id") in zonas_distribuidas and
                    arista["hacia_info"].get("zona_id") in zonas_distribuidas
                ) else "zona_a_acceso"
            }
            for arista in red_peatonale["aristas"]
        ],
        "analisis_eficiencia": {
            "interpretacion": (
                "RED EFICIENTE" if red_peatonale["eficiencia_red"] >= 0.8 else
                "RED ACEPTABLE" if red_peatonale["eficiencia_red"] >= 0.6 else
                "RED PÉSFICA - CONSIDERAR MEJORAS"
            ),
            "recomendacion": (
                "La red de conexiones peatonales es eficiente para el tamaño del desarrollo."
                if red_peatonale["eficiencia_red"] >= 0.7 else
                "Considerar añadir accesos peatonales directos o reducir la dispersión de zonas."
            )
        }
    }

    # Generar reporte de texto
    reporte_lineas = [
        "=" * 80,
        "ANÁLISIS DE ACCESOS, PATIOS Y RED PEATONAL - INFORME COMPLETO",
        "=" * 80,
        f"Fecha de análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Área total de lote analizada: {area_lote:.2f} m²",
        f"Número de zonas evaluadas: {len(zonas_distribuidas)}",
        "",
        "ANÁLISIS DE ACCESIBILIDAD:",
        "-" * 40,
        f"Puntuación promedio de accesibilidad: {resumen_accesibilidad['puntuacion_promedio']:.3f}/1.000",
        f"Clasificación general: {resultado_accesos['resumen_general']['accesibilidad_general_clasificacion']}",
        f"Distribución por categoría:",
        f"  • Excelente (≥0.85): {resumen_accesibilidad['zonas_excelentes']} zonas",
        f"  • Bueno (0.70-0.84): {resumen_accesibilidad['zonas_buenas']} zonas",
        f"  • Aceptable (0.50-0.69): {resumen_accesibilidad['zonas_aceptables']} zonas",
        f"  • Insuficiente (<0.50): {resumen_accesibilidad['zonas_insuficientes']} zonas",
        ""
    ]

    # Detalle de accesibilidad por zona (primeras 5 para no sobrecargar)
    cuenta_mostradas = 0
    for zona_id, detalles in resumen_accesibilidad["detalles_por_zona"].items():
        if cuenta_mostradas >= 5:
            resto = len(resumen_accesibilidad["detalles_por_zona"]) - 5
            if resto > 0:
                reporte_lineas.append(f"  ... y {resto} zonas más")
            break

        uso = detalles["uso"]
        puntuacion = detalles["puntuacion_accesibilidad"]
        clasificacion = detalles["accesibilidad_clasificacion"]
        dist_via = detalles["distancia_minima_via_principal_m"]
        dist_trans = detalles["distancia_minima_transporte_m"]

        reporte_lineas.append(
            f"  Zona {zona_id} ({uso:12}): {puntuacion:.3f} [{clasificacion}] "
            f"(vía principal: {dist_via:.1f}m, transporte: {dist_trans:.1f}m)"
        )
        cuenta_mostradas += 1

    if resultado_accesos["recomendaciones_mejora"]:
        reporte_lineas.extend([
            "",
            "RECOMENDACIONES DE MEJORA DE ACCESIBILIDAD:",
            "-" * 40
        ])
        for rec in resultado_accesos["recomendaciones_mejora"]:
            reporte_lineas.append(f"  • {rec}")

    reporte_lineas.extend([
        "",
        "ANÁLISIS DE PATIOS Y ESPACIOS ABIERTOS:",
        "-" * 40,
        f"Área total de patio requerida: {resumen_patios['area_patio_requerido_total_m2']:.2f} m²",
        f"Área total de patio disponible (estimada): {resumen_patios['area_patio_disponible_estimada_total_m2']:.2f} m²",
        f"Déficit total de patio: {max(0, resumen_patios['deficit_patio_total_m2']):.2f} m²",
        f"Superávit total de patio: {max(0, resumen_patios['superavit_patio_total_m2']):.2f} m²",
        f"Porcentaje promedio de cumplimiento: {resumen_patios['porcentaje_cumplimiento_promedio']:.1f}%",
        f"Clasificación general de patios: {resultado_patios['resumen_general']['cumplimiento_general']}",
        f"Zonas con déficit: {resumen_patios['zonas_con_deficit']} de {len(zonas_distribuidas)}",
        f"Zonas con superávit: {resumen_patios['zonas_con_superavit']} de {len(zonas_distribuidas)}",
        ""
    ])

    # Detalle de patios por zona (primeras 5)
    cuenta_mostradas = 0
    for zona_id, detalles in resumen_patios["detalles_por_zona"].items():
        if cuenta_mostradas >= 5:
            resto = len(resumen_patios["detalles_por_zona"]) - 5
            if resto > 0:
                reporte_lineas.append(f"  ... y {resto} zonas más")
            break

        uso = detalles["uso"]
        requerido = detalles["patio_requerido_m2"]
        disponible = detalles["patio_disponible_m2"]
        cumplimiento = detalles["porcentaje_cumplimiento"]
        estado = detalles["estado"]

        reporte_lineas.append(
            f"  Zona {zona_id} ({uso:12}): {requerido:.1f}m² req / {disponible:.1f}m² disp "
            f"= {cumplimiento:.1f}% [{estado}]"
        )
        cuenta_mostradas += 1

    if resultado_patios["recomendaciones"]:
        reporte_lineas.extend([
            "",
            "RECOMENDACIONES DE PATIOS:",
            "-" * 40
        ])
        for rec in resultado_patios["recomendaciones"]:
            reporte_lineas.append(f"  • {rec}")

    reporte_lineas.extend([
        "",
        "ANÁLISIS DE RED PEATONAL:",
        "-" * 40,
        f"Nodos en la red (zonas + accesos): {resultado_red_peatonale['estadisticas_red']['total_nodos']}",
        f"Conexiones propuestas: {resultado_red_peatonale['estadisticas_red']['total_aristas']}",
        f"Longitud total de senderos peatonales: {resultado_red_peatonale['estadisticas_red']['longitud_total_m']:.1f} m",
        f"Longitud promedio por conexión: {resultado_red_peatonale['estadisticas_red']['longitud_promedio_arista_m']:.1f} m",
        f"Eficiencia de la red: {resultado_red_peatonale['estadisticas_red']['eficiencia_red']:.3f}",
        f"Interpretación: {resultado_red_peatonale['analisis_eficiencia']['interpretacion']}",
        ""
    ])

    if resultado_red_peatonale["analisis_eficiencia"]["recomendacion"]:
        reporte_lineas.extend([
            "RECOMENDACIONES DE RED PEATONAL:",
            "-" * 40,
            f"  • {resultado_red_peatonale['analisis_eficiencia']['recomendacion']}"
        ])

    # Detalle de algunas conexiones (primeras 3)
    conexiones_mostradas = 0
    max_conexiones_mostrar = min(3, len(resultado_red_peatonale["conexiones"]))
    if resultado_red_peatonale["conexiones"]:
        reporte_lineas.append("  Conexiones principales propuestas:")
        for i in range(min(max_conexiones_mostrar, len(resultado_red_peatonale["conexiones"]))):
            conn = resultado_red_peatonale["conexiones"][i]
            desde = conn["desde_zona"]
            hacia = conn["hacia_zona"]
            dist = conn["distancia_m"]
            tipo = conn["tipo_conexion"]
            reporte_lineas.append(
                f"    {desde} ↔ {haya}: {dist:.1f}m ({tipo})"
            )
            conexiones_mostradas += 1

        total_conexiones = len(resultado_red_peatonale["conexiones"])
        if total_conexiones > max_conexiones_mostrar:
            resto = total_conexiones - max_conexiones_mostrar
            reporte_lineas.append(f"    ... y {resto} conexiones más")

    reporte_lineas.extend([
        "",
        "RESUMEN EJECUTIVO Y RECOMENDACIONES FINALES:",
        "-" * 40,
    ])

    # Determinar viabilidad general
    accesibilidad_aceptable = resumen_accesibilidad["puntuacion_promedio"] >= 0.6
    patios_adecuados = resumen_patios["porcentaje_cumplimiento_promedio"] >= 70
    red_eficiente = resultado_red_peatonale["estadisticas_red"]["eficiencia_red"] >= 0.6

    puntuacion_global = (resumen_accesibilidad["puntuacion_promedio"] * 0.4 +
                        (resumen_patios["porcentaje_cumplimiento_promedio"] / 100.0) * 0.3 +
                        resultado_red_peatonale["estadisticas_red"]["eficiencia_red"] * 0.3)

    if puntuacion_adelante >= 0.8:
        verdict = "EXCELENTE - El diseño cumple favorablemente con los criterios de accesibilidad, patios y conectividad."
    elif puntuacion_adelante >= 0.65:
        verdict = "BUENO - El diseño muestra buenos niveles de cumplimiento con oportunidades de mejora menores."
    elif puntuacion_adelante >= 0.5:
        verdict = "ACEPTABLE - El diseño cumple mínimamente los requisitos, se recomienda revisión y optimización."
    else:
        verdict = "INSUFICIENTE - El diseño requiere mejoras significativas en accesibilidad, provisión de patos o conectividad."

    recom_final = (
        "PROCEDER CON EL DISEÑO ACTUAL - MONITOREAR DURANTE EJECUCIÓN"
        if puntuacion_adelante >= 0.6 else
        "REVISAR Y OPTIMIZAR ANTES DE LA ETAPA DE DISEÑO DETALLADO"
    )

    reporte_lineas.extend([
        f"Puntuación global de desempeño: {puntuacion_adelante:.3f}/1.000",
        f"Veredito técnico: {verdict}",
        f"Recomendación final: {recom_final}",
        "",
        "Desglose de contribuciones al puntaje:",
        f"  • Accesibilidad (40%): {resumen_accesibilidad['puntuacion_promedio']:.3f} × 0.40 = {resumen_accesibilidad['puntuacion_promedio'] * 0.4:.3f}",
        f"  • Patios y espacios abiertos (30%): {resumen_patios['porcentaje_cumplimiento_promedio']/100:.3f} × 0.30 = {(resumen_patios['porcentaje_cumplimiento_promedio']/100)*0.3:.3f}",
        f"  • Red peatonal y conectividad (30%): {resultado_red_peatonale['estadisticas_red']['eficiencia_red']:.3f} × 0.30 = {resultado_red_peatonale['estadisticas_red']['eficiencia_red']*0.3:.3f}",
        "",
        "PRÓXIMOS PASOS RECOMENDADOS:",
        "  1. Validar resultados con estudios de impacto de movilidad específicos al sitio",
        "  2. Realizar análisis de soleamiento y ventilación para espacios de patio",
        "  3. Desarrollar detalles constructivos de accesibilidad universal",
        "  4. Coordinar con autoridades locales de tránsito y planeación para accesos viales",
        "  5. Elaborar planes de señalización y orientación peatonal detallados",
        "",
        "=" * 80
    ])

    reporte_texto = "\n".join(reporte_lineas)

    # Convertir a JSON para salida
    accesos_json = json.dumps(resultado_accesos, indent=2, ensure_ascii=False)
    patios_json = json.dumps(resultado_patios, indent=2, ensure_ascii=False)
    red_json = json.dumps(resultado_red_peatonale, indent=2, ensure_ascii=False)

    print("\n=== RESUMEN DE EJECUCIÓN ===")
    print(f"Análisis completado para {len(zonas_distribuidas)} zonas")
    print(f"Puntuación promedio de accesibilidad: {resumen_accesibilidad['puntuacion_promedio']:.3f}")
    print(f"Porcentaje promedio de cumplimiento de patios: {resumen_patios['porcentaje_cumplimiento_promedio']:.1f}%")
    print(f"Longitud total de red peatonal propuesta: {resultado_red_peatonale['estadisticas_red']['longitud_total_m']:.1f} m")

    # Guardar resultados en archivos
    output_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    accesos_path = os.path.join(output_dir, "accesos_calculados.json")
    with open(accesos_path, 'w', encoding='utf-8') as f:
        f.write(accesos_json)

    patios_path = os.path.join(output_dir, "patios_calculados.json")
    with open(patios_path, 'w', encoding='utf-8') as f:
        f.write(patios_json)

    red_path = os.path.join(output_dir, "redes_peatonales.json")
    with open(red_path, 'w', encoding='utf-8') as f:
        f.write(red_json)

    reporte_path = os.path.join(output_dir, "reporte_accesos_patios.txt")
    with open(reporte_path, 'w', encoding='utf-8') as f:
        f.write(reporte_texto)

    print(f"\nArchivos guardados en: {output_dir}")
    print(f"  - accesos_calculados.json")
    print(f"  - patios_calculados.json")
    print(f"  - redes_peatonales.json")
    print(f"  - reporte_accesos_patios.txt")

    # Asignar valores para salida de Grasshopper
    accesos_calculados = accesos_json
    patios_calculados = patios_json
    redes_peatonales = red_json
    reporte_accesos_patios = reporte_texto

# Ejecutar si se ejecuta como script principal
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error en ACCESOS_INTEGRADOR_v01: {str(e)}")
        import traceback
        traceback.print_exc()

        # Salida de error para Grasshopper
        error_result = {
            "error": str(e),
            "mensaje": "Error en el análisis de accesos y patios"
        }
        accesos_calculados = json.dumps(error_result, indent=2, ensure_ascii=False)
        patios_calculados = json.dumps(error_result, indent=2, ensure_ascii=False)
        redes_peatonales = json.dumps(error_result, indent=2, ensure_ascii=False)
        reporte_accesos_patios = f"ERROR: {str(e)}"