# -*- coding: utf-8 -*-
# ============================================================================
# F0_LOAD_PROYECTO_v01.py — carga proyecto.json y expone variables del canvas
# ============================================================================
# Propósito: leer un proyecto.json (orquestador) y exponer las variables de
#   decisión como salidas, para reemplazar los ~12 inputs sueltos del canvas.
#   Con un único cableado el canvas se recalcula por clic o vía Tapir desde
#   ArchiCAD: basta re-escribir el proyecto.json y disparar la solución.
#
# Normativa aplicable: ninguna (script de orquestación del canvas; no calcula
#   retiros, GFA ni normativa).
#
# Historial de versiones:
#   v01 (2026-08-18) — carga inicial del proyecto.json + salidas tipadas.
#   v01.1 (2026-08-18) — normaliza tipo_bonificacion al vocabulario NORMATIVA;
#       resuelve empate_posterior_pisos desde empate_posterior_m (m -> pisos);
#       expone antejardin_m y voladizo_frontal_m como overrides numericos.
#   v01.2 (2026-08-18) — empate_posterior_pisos y _m son independientes
#       (edificio vecino existente, sin relacion con floor_height_user); se
#       elimina la conversion m -> pisos; 'Servicios' -> 'EQUIPAMIENTO'; nueva
#       salida derivada empate_posterior_entrepiso_m (m / pisos).
#
# Entradas:
#   ruta_json    : str (Item) — ruta absoluta al proyecto.json
#   caso_default : str (Item) — caso por defecto si el json no trae 'caso'
#
# Salidas:
#   chip, tipologia, piso_adicional, tipo_bonificacion, floor_height_user,
#   antejardin_decision, antejardin_m, voladizo_frontal_m,
#   empate_posterior_pisos, empate_posterior_m, empate_posterior_entrepiso_m,
#   tratamiento, caso, alineacion_nucleo, usos (list), modos (list),
#   escenarios (list), vecinos_por_lado_json (str), ok (bool), log (str)
#
# Funciones internas:
#   _val(d, k, default) — devuelve d[k] o default si falta o es None
# ============================================================================

import json
import os


def _val(d, k, default):
    v = d.get(k) if isinstance(d, dict) else None
    return default if v is None else v


def _a_normativa_vecinos(clasificacion):
    """Port de vecinos_por_lado.a_normativa_vecinos_por_lado (sin shapely).
    Respeta frente_override, confirmacion, 'corresponde' y vecinos_manuales.
    Devuelve {str(seg_id): [altura_m, ...]} solo para lados 'predio'."""
    result = {}
    lados = clasificacion.get("lados", []) if isinstance(clasificacion, dict) else []
    for lado in lados:
        if not isinstance(lado, dict):
            continue
        frente = lado.get("frente_override") or lado.get("frente")
        if frente != "predio":
            continue
        if lado.get("confirmacion") == "no_es_predio":
            continue
        altura_por_chip = {}
        for v in lado.get("vecinos", []):
            if not isinstance(v, dict):
                continue
            if v.get("corresponde") is False:
                continue
            h = v.get("altura_m")
            if h is None:
                continue
            try:
                altura_por_chip[v.get("chip")] = float(h)
            except Exception:
                pass
        manuales = []
        for v in lado.get("vecinos_manuales", []):
            if not isinstance(v, dict):
                continue
            h = v.get("altura_m")
            if h is None:
                continue
            try:
                manuales.append(float(h))
            except Exception:
                pass
        if not altura_por_chip and not manuales:
            continue
        seg_vec = lado.get("segmentos_vecinos", {}) or {}
        segmentos = lado.get("segmentos", [])
        for seg_id in segmentos:
            chips = seg_vec.get(str(seg_id), [])
            alturas = [altura_por_chip[c] for c in chips if c in altura_por_chip]
            if segmentos and seg_id == segmentos[0]:
                alturas.extend(manuales)
            if alturas:
                result[str(seg_id)] = alturas
    return result


ruta_json = globals().get("ruta_json") or ""
caso_default = globals().get("caso_default") or "A"

proyecto = {}
ok = False
log = ""
if ruta_json and os.path.exists(ruta_json):
    try:
        with open(ruta_json, "r", encoding="utf-8") as f:
            proyecto = json.load(f)
        if not isinstance(proyecto, dict):
            proyecto = {}
        ok = True
        log = "OK: proyecto cargado desde %s" % ruta_json
    except Exception as e:
        log = "ERROR al leer %s: %s" % (ruta_json, e)
else:
    log = "ERROR: ruta no valida: %s" % ruta_json

variables = proyecto.get("variables") if isinstance(proyecto.get("variables"), dict) else {}

chip = _val(proyecto, "chip", "")
tipologia = _val(variables, "tipologia", "Continua")
piso_adicional = bool(_val(variables, "piso_adicional", False))
tipo_bonificacion = _val(variables, "tipo_bonificacion", "Ninguno")
floor_height_user = _val(variables, "floor_height_user", 3.0)
antejardin_decision = _val(variables, "antejardin_decision", "Según reglamentación")
empate_posterior_pisos = _val(variables, "empate_posterior_pisos", 0)
empate_posterior_m = _val(variables, "empate_posterior_m", None)
tratamiento = _val(variables, "tratamiento", "Consolidación")
caso = _val(variables, "caso", _val(proyecto, "caso", caso_default))
alineacion_nucleo = _val(variables, "alineacion_nucleo", 1)

usos = proyecto.get("usos") or []
modos = proyecto.get("modos") or []
escenarios = proyecto.get("escenarios") or []

if not isinstance(usos, list):
    usos = []
if not isinstance(modos, list):
    modos = []
if not isinstance(escenarios, list):
    escenarios = []


# ---- v01.1: normalizacion hacia el vocabulario de F1_ETAPA2_NORMATIVA ----
_BONIF_MAP = {"Ninguno": "NINGUNO", "Servicios": "EQUIPAMIENTO", "VIS": "VIS"}
_tb = str(tipo_bonificacion).strip() if tipo_bonificacion else ""
if _tb in _BONIF_MAP:
    tipo_bonificacion = _BONIF_MAP[_tb]
elif _tb:
    tipo_bonificacion = _tb.upper()
else:
    tipo_bonificacion = "NINGUNO"

antejardin_m = _val(variables, "antejardin_m", 0.0)
try:
    antejardin_m = float(antejardin_m) if antejardin_m is not None else 0.0
except Exception:
    antejardin_m = 0.0

voladizo_frontal_m = _val(variables, "voladizo_frontal_m", 0.0)
try:
    voladizo_frontal_m = float(voladizo_frontal_m) if voladizo_frontal_m is not None else 0.0
except Exception:
    voladizo_frontal_m = 0.0

# empate_posterior: pisos y metros son INDEPENDIENTES (edificio vecino
# existente, sin relacion con floor_height_user del proyecto actual).
# Pueden darse uno, otro o ambos; NO se convierten entre si.
empate_posterior_entrepiso_m = 0.0
try:
    _n = int(empate_posterior_pisos) if empate_posterior_pisos is not None else 0
except Exception:
    _n = 0
try:
    _h = float(empate_posterior_m) if empate_posterior_m is not None else 0.0
except Exception:
    _h = 0.0
if _n > 0 and _h > 0:
    empate_posterior_entrepiso_m = _h / float(_n)

# ---- v01.3: vecinos por lado -> vecinos_por_lado_json (NORMATIVA_v08) ----
# proyecto.json['vecinos_por_lado'] lo escribe el formulario (orquestador);
# aqui se convierte a {id_lado: [altura_m, ...]} para empate lateral.
vecinos_por_lado_json = ""
_vpl = proyecto.get("vecinos_por_lado")
if isinstance(_vpl, dict):
    try:
        _m = _a_normativa_vecinos(_vpl)
        if _m:
            vecinos_por_lado_json = json.dumps(_m)
    except Exception as e:
        log += " | vecinos_por_lado_json: %s" % e
