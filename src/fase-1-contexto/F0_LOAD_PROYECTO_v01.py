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
# PROPUESTA v01.6 (pendiente pruebas IronPython): lee el activo de lados
# con CHIP verificado; preserva tramos en clasificacion_lados_json (NUEVA
# salida Item String). No envia IDs crudos a NORMATIVA. Los cardinales
# ambiguos se excluyen del puente legacy; requieren adaptador geometrico.
# Historial de versiones:
#   v01.3 (2026-08-23) — vecinos por lado -> vecinos_por_lado_json
#       (NORMATIVA_v08; respeta frente_override, confirmacion,
#       'corresponde' y vecinos_manuales).
#   v01.4 (2026-08-23) — frente confirmado por cardinal ->
#       frente_override_json (para cablear F0 -> F1_ETAPA2_NORMATIVA_v08;
#       ignora 'indefinido'/'libre').
#   v01.5 (2026-09-29) — LECTOR CANONICO de codificacion (cascada utf-8
#       estricto -> cp1252 -> latin-1, con aviso ruidoso) para proyecto.json.
#
# Ruta recomendada (2026-09-01): conectar ruta_json a data/activo/proyecto.json
#   (espejo que el orquestador reescribe en cada POST /api/proyecto).
# Entradas:
#   ruta_json    : str (Item) — ruta absoluta al proyecto.json
#   caso_default : str (Item) — caso por defecto si el json no trae 'caso'
#
# Salidas:
#   chip, tipologia, piso_adicional, tipo_bonificacion, floor_height_user,
#   antejardin_decision, antejardin_m, voladizo_frontal_m,
#   empate_posterior_pisos, empate_posterior_m, empate_posterior_entrepiso_m,
#   tratamiento, caso, alineacion_nucleo, usos (list), modos (list),
#   escenarios (list), vecinos_por_lado_json (str), frente_override_json (str),
#   ok (bool), log (str)
#
# Funciones internas:
#   _val(d, k, default) — devuelve d[k] o default si falta o es None
# ============================================================================

import json
import os

try:
    import System.IO
    import System.Text
    _TIENE_SYSTEM = True
except ImportError:
    _TIENE_SYSTEM = False


try:
    text_type = unicode
except NameError:
    text_type = str


def _texto(v):
    if v is None:
        return u""
    if isinstance(v, text_type):
        return v
    if isinstance(v, bytes):
        for enc in ("utf-8-sig", "cp1252", "latin-1"):
            try:
                return v.decode(enc)
            except UnicodeError:
                pass
    return text_type(v)


def _ascii_json(v):
    # Evita el encoder de cadenas IronPython; conserva todos los campos.
    def quote(s):
        parts = ['"']
        for c in _texto(s):
            n = ord(c)
            if n == 34:
                parts.append('\\"')
            elif n == 92:
                parts.append('\\\\')
            elif n < 32 or n > 126:
                if n <= 65535:
                    parts.append('\\u%04x' % n)
                else:
                    n -= 65536
                    parts.append('\\u%04x\\u%04x' % (55296 + (n >> 10), 56320 + (n & 1023)))
            else:
                parts.append(chr(n))
        return ''.join(parts) + '"'
    def emit(x):
        if x is None: return 'null'
        if isinstance(x, bool): return 'true' if x else 'false'
        if isinstance(x, dict):
            return '{' + ','.join(quote(k) + ':' + emit(w) for k, w in x.items()) + '}'
        if isinstance(x, (list, tuple)):
            return '[' + ','.join(emit(w) for w in x) + ']'
        if isinstance(x, (text_type, bytes)):
            return quote(x)
        try:
            nums = (int, long, float)
        except NameError:
            nums = (int, float)
        if isinstance(x, nums): return json.dumps(x, allow_nan=False)
        raise TypeError('Tipo JSON no soportado: ' + type(x).__name__)
    result = emit(v)
    json.loads(result)
    return result


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
            if manuales:
                alturas.extend(manuales)
            if alturas:
                result[str(seg_id)] = alturas
    return result


def _quitar_bom(t):
    if not t:
        return t
    if t[0] == u"\uFEFF":
        return t[1:]
    if t[:3] == u"\u00EF\u00BB\u00BF":
        return t[3:]
    return t


def _leer_json_canonico(ruta, etiqueta="json"):
    """LECTOR CANONICO v01.5: utf-8 estricto (con/sin BOM) -> cp1252 -> latin-1.

    Dual: usa System.IO/System.Text cuando corre en IronPython (canvas) y
    open() nativo cuando corre en CPython (tests). Avisos ruidosos; error
    explicito con hex de cabecera si todo falla."""
    ruta_s = _texto(ruta)
    if not ruta or not os.path.exists(ruta_s):
        raise Exception("El archivo no existe en la ruta especificada: {}".format(ruta))
    if _TIENE_SYSTEM:
        bruto = System.IO.File.ReadAllBytes(ruta_s)
    else:
        with open(ruta_s, "rb") as f:
            bruto = f.read()
    err_utf8 = ""
    err_cp1252 = ""
    # 1) UTF-8 estricto (tolera BOM)
    try:
        if _TIENE_SYSTEM:
            contenido = _quitar_bom(System.Text.UTF8Encoding(False, True).GetString(bruto))
        else:
            contenido = _quitar_bom(bruto.decode("utf-8"))
        return json.loads(contenido)
    except Exception as e_utf8:
        err_utf8 = _texto(e_utf8)
    # 2) CP1252 (legacy Windows)
    try:
        if _TIENE_SYSTEM:
            contenido = _quitar_bom(System.Text.Encoding.GetEncoding(1252).GetString(bruto))
        else:
            contenido = _quitar_bom(bruto.decode("cp1252"))
        data = json.loads(contenido)
        print(u"[AVISO ENCODING] {}: CP1252".format(_texto(etiqueta)))
        return data
    except Exception as e_cp1252:
        err_cp1252 = _texto(e_cp1252)
    # 3) Latin-1 (ultimo recurso)
    try:
        if _TIENE_SYSTEM:
            contenido = _quitar_bom(System.Text.Encoding.GetEncoding(28591).GetString(bruto))
        else:
            contenido = _quitar_bom(bruto.decode("latin-1"))
        data = json.loads(contenido)
        print(u"[AVISO ENCODING] {}: Latin-1".format(_texto(etiqueta)))
        return data
    except Exception as e_latin1:
        cab = []
        for i in range(min(24, len(bruto))):
            cab.append("%02X" % (bruto[i] if isinstance(bruto[i], int) else ord(bruto[i])))
        raise Exception("No se pudo decodificar {} ({}). Primeros bytes: [{}]. utf8={} | cp1252={} | latin1={}".format(
            etiqueta, ruta_s, " ".join(cab), err_utf8, err_cp1252, str(e_latin1)))


ruta_json = _texto(globals().get("ruta_json") or "")
caso_default = globals().get("caso_default") or "A"

proyecto = {}
ok = False
log = ""
if ruta_json and os.path.exists(ruta_json):
    try:
        proyecto = _leer_json_canonico(ruta_json, "proyecto.json")
        if not isinstance(proyecto, dict):
            proyecto = {}
        ok = True
        log = u"F0 v01.6 | OK: proyecto cargado desde %s" % ruta_json
    except Exception as e:
        log = u"ERROR al leer %s: %s" % (ruta_json, _texto(e))
else:
    log = u"ERROR: ruta no valida: %s" % ruta_json

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
_tb = _texto(tipo_bonificacion).strip() if tipo_bonificacion else ""
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

# v01.6: fuente activa del Orquestador, con identidad de CHIP obligatoria.
# NUEVA salida clasificacion_lados_json: conectar al futuro adaptador de LADOS,
# NO a vecinos_por_lado_json legacy de NORMATIVA.
clasificacion_lados_json = ""
vecinos_por_lado_json = ""
frente_override_json = ""
_vpl = proyecto.get("vecinos_por_lado")
_root = os.environ.get("DISENO_PARAMETRICO_ROOT", "")
if not _root and ruta_json:
    # Solo derivar raiz de la ruta recomendada data/activo/proyecto.json.
    _dir = os.path.dirname(ruta_json)
    if os.path.basename(_dir).lower() == "activo" and os.path.basename(os.path.dirname(_dir)).lower() == "data":
        _root = os.path.dirname(os.path.dirname(_dir))
_activo = os.path.join(_root, "data", "pot-cache", "CHIP-vecinos-por-lado.json") if _root else ""
if _activo and os.path.isfile(_activo):
    try:
        _vpl = _leer_json_canonico(_activo, "lados activos")
        log += u" | lados: archivo activo"
    except Exception as e:
        _vpl = None
        ok = False
        log += u" | ERROR lados activos: " + _texto(e)
if isinstance(_vpl, dict) and _vpl.get("lados"):
    if _texto(_vpl.get("chip")) != _texto(chip) or not chip:
        ok = False
        log += u" | ERROR: CHIP de lados distinto del proyecto"
    else:
        clasificacion_lados_json = _ascii_json(_vpl)
        # No confundir indices del perimetro raw con indices simplificados.
        log += u" | tramos preservados: {} | vecinos requieren adaptador de indices".format(len(_vpl["lados"]))
        grupos = {}
        for lado in _vpl["lados"]:
            card = _texto(lado.get("cardinal"))
            grupos.setdefault(card, []).append(lado)
        fo = {}
        for card, tramos in grupos.items():
            if not card:
                continue
            if len(tramos) > 1:
                log += u" | cardinal ambiguo excluido del legacy: " + card
                continue
            fr = tramos[0].get("frente_override")
            if fr in ("via", "via_no_frontal", "predio", "espacio_publico"):
                fo[card] = fr
        if fo:
            frente_override_json = _ascii_json(fo)
else:
    ok = False
    log += u" | ERROR: clasificacion de lados ausente"

