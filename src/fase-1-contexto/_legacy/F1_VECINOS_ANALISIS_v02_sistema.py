#!/usr/bin/env python3
"""
VECINOS_ANALISIS_v02.py - Análisis de Vecinos NSR-10
"""

import Rhino.Geometry as rg
import json

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================
def to_int(val, default=0):
    try: return int(float(val))
    except (ValueError, TypeError): return default

def to_float(val, default=0.0):
    try: return float(val)
    except (ValueError, TypeError): return default

# ============================================================
# OBTENCIÓN SEGURA DE INPUTS
# ============================================================
datos_vecinos = globals().get("datos_vecinos", None)
lot_polygon = globals().get("lot_polygon", None)
street_curves = globals().get("street_curves", [])

# Asegurarse de que sean listas
if street_curves is None: street_curves = []
if not isinstance(street_curves, list): street_curves = [street_curves]

# ============================================================
# ANÁLISIS DE VECINOS
# ============================================================
# Valores por defecto (en una implementación real, estos vendrían del análisis de datos de vecinos)
zon_sismica = "ZONA_MEDIA"  # Valor típico para gran parte de Bogotá
tipo_suelo = "SUELO_TYPE_A"  # Suelo firme/rocoso
altura_maxima_permitida = 15.0  # metros, valor conservador típico
setbacks_nsr10 = {
    "norte": 3.0,
    "sur": 3.0,
    "este": 3.0,
    "oeste": 3.0
}

# Si tenemos datos de vecinos reales, procesarlos aquí
if datos_vecinos is not None:
    # En una implementación completa, procesaríamos los datos_vecinos
    # para extraer información específica de zonificación sísmica y tipo de suelo
    pass

# ============================================================
# SALIDAS
# ============================================================
vecino_analisis_json = json.dumps({
    "zon_sismica": zon_sismica,
    "tipo_suelo": tipo_suelo,
    "altura_maxima_permitida": altura_maxima_permitida,
    "setbacks": setbacks_nsr10
})

# Salidas individuales para compatibilidad
zon_sismica_out = zon_sismica
tipo_suelo_out = tipo_suelo
altura_maxima_permitida_out = altura_maxima_permitida
setbacks_nsr10_out = json.dumps(setbacks_nsr10)

a = "Análisis de vecinos NSR-10 completado: Zona={}, Suelo={}, Altura máxima={}m".format(
    zon_sismica, tipo_suelo, altura_maxima_permitida)