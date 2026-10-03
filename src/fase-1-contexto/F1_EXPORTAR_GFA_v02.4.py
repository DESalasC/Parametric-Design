# -*- coding: utf-8 -*-
"""
================================================================================
F1_EXPORTAR_GFA_v02.4.py - Exporta GFA APROBADO de Fase 1 a JSON para Fase 2
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

CAMBIOS v02.4 (2026-10-03) — Integración con NORMATIVA v09 + validador barras:
  - Nueva entrada opcional: gfa_aprobado_m2 (Number) — GFA validado por
    NORMATIVA v09 cuando hay barras_json (modo APROBADO).
  - Nueva entrada opcional: ocupacion_aprobada_m2 (Number) — Ocupación aprobada.
  - Nueva entrada opcional: envelope_aprobado_por_piso (Curve/List) — Envelopes aprobados.
  - CAMBIO DE CONTRATO: Si gfa_aprobado_m2 > 0 y valido=True, escribe
    SOLO gfa_aprobado_m2 como "gfa_aprobado_m2" en el JSON (para F2).
    NO escribe gfa_total como gfa_potencial (simplificación D6).
  - Mantiene flag-driven, CHIP derivado, override_uso, ASCII-safe.
  - Homogeneizado: versión interna = nombre archivo (v02.4).

ENTRADAS (adicionales a v02.3):
  gfa_aprobado_m2 (Number)         - [v09] GFA aprobado por validador (si >0)
  ocupacion_aprobada_m2 (Number)   - [v09] Ocupación aprobada (si >0)
  envelope_aprobado_por_piso (List)- [v09] Envelopes aprobados por piso

SALIDAS (actualizadas):
  - JSON incluye "gfa_aprobado_m2" (si modo APROBADO) o "gfa_total_m2" (potencial)
  - NO incluye gfa_potencial_m2 (D6: solo aprobado)

================================================================================
"""

import json
import os
import re
from datetime import date

DEFAULT_OUTPUT_DIR = r"D:\Work\PROJECTS\DiseñoParametrico\data\fase-2-demanda"
REDONDEO = 4
FLAG_PATH = os.path.join(DEFAULT_OUTPUT_DIR, "gfa-export-flag.json")


def _decodificar_cascada(raw, ruta="<bytes>"):
    """LECTOR CANONICO (v02.3): utf-8-sig estricto -> cp1252 -> latin-1."""
    try:
        return raw.decode("utf-8-sig")
    except Exception:
        pass
    try:
        texto = raw.decode("cp1252")
        print("[AVISO ENCODING] leido como cp1252 (no utf-8): %s" % ruta)
        return texto
    except Exception:
        pass
    texto = raw.decode("latin-1")
    print("[AVISO ENCODING] leido como latin-1 (ultimo recurso): %s" % ruta)
    return texto


def leer_flag():
    try:
        with open(FLAG_PATH, "rb") as f:
            d = json.loads(_decodificar_cascada(f.read(), FLAG_PATH))
        return bool(d.get("exportar", False))
    except Exception:
        return False


def reset_flag():
    try:
        if not os.path.isdir(DEFAULT_OUTPUT_DIR):
            os.makedirs(DEFAULT_OUTPUT_DIR)
        with open(FLAG_PATH, "wb") as f:
            f.write(json.dumps({"exportar": False}).encode("utf-8"))
    except Exception:
        pass


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def parse_gh_bool(val):
    if val is None: return False
    if isinstance(val, list): val = val[0] if len(val) > 0 else None
    if val is None: return False
    if isinstance(val, bool): return val
    s = str(val).strip().lower()
    return s in ("true", "1", "verdadero", "yes", "si")


def to_float(val, default, warnings):
    val = unwrap(val)
    if val is None:
        warnings.append("entrada numerica faltante -> default {0}".format(default))
        return default
    try: return float(val)
    except (TypeError, ValueError):
        warnings.append("valor no numerico '{0}' -> default {1}".format(str(val), default))
        return default


def to_int(val, default, warnings):
    val = unwrap(val)
    if val is None:
        warnings.append("entrada entera faltante -> default {0}".format(default))
        return default
    try: return int(round(float(val)))
    except (TypeError, ValueError):
        warnings.append("valor no entero '{0}' -> default {1}".format(str(val), default))
        return default


def derivar_chip(ruta):
    raw = unwrap(ruta)
    if raw is None: return ""
    s = str(raw).strip().strip('"').strip("'").strip()
    if s == "": return ""
    m = re.search(r"([A-Za-z0-9]{4,})-contexto\.json", s.replace("\\", "/"))
    if m: return m.group(1)
    if s.startswith("{"):
        try:
            datos = json.loads(s)
            chip = datos.get("chip") or (datos.get("metadata") or {}).get("chip")
            if chip: return str(chip).strip()
        except Exception: pass
        return ""
    try:
        with open(s, "rb") as f:
            datos = json.loads(_decodificar_cascada(f.read(), s))
        chip = datos.get("chip") or (datos.get("metadata") or {}).get("chip")
        if chip: return str(chip).strip()
    except Exception: pass
    return ""


def parse_flag_pipeline(flag):
    flag = unwrap(flag)
    if flag is None: return None
    s = str(flag).strip()
    if s == "": return None
    if s.startswith("USO_OVERRIDE:"):
        resto = s[len("USO_OVERRIDE:"):]
        uso = resto.split(";")[0].strip()
        nota = resto.split(";", 1)[1].strip() if ";" in resto else ""
        return {"activo": True, "uso": uso, "nota": nota, "token": s}
    if s.startswith("USO_NORMA:"):
        uso = s[len("USO_NORMA:"):].strip()
        return {"activo": False, "uso": uso, "nota": "", "token": s}
    return {"activo": False, "uso": s, "nota": "", "token": s}


# ------------------------------------------------------------------ entradas
json_path = globals().get("json_path", None)
area_envelope = globals().get("area_envelope", None)
gfa_total = globals().get("gfa_total", None)           # GFA potencial (modo POTENCIAL)
ocupacion_real = globals().get("ocupacion_real", None)
io_maximo = globals().get("io_maximo", None)
ic_real = globals().get("ic_real", None)
ic_maximo = globals().get("ic_maximo", None)
altura_total = globals().get("altura_total", None)
pisos_finales = globals().get("pisos_finales", None)
valido = globals().get("valido", False)
mensaje = globals().get("mensaje", None)
flag_pipeline = globals().get("flag_pipeline", None)
output_path = globals().get("output_path", None)

# v09 NUEVAS ENTRADAS (modo APROBADO)
gfa_aprobado_m2 = globals().get("gfa_aprobado_m2", None)
ocupacion_aprobada_m2 = globals().get("ocupacion_aprobada_m2", None)
envelope_aprobado_por_piso = globals().get("envelope_aprobado_por_piso", None)


def build_payload():
    warnings = []
    chip_str = derivar_chip(json_path)
    if chip_str == "": warnings.append("no se pudo derivar CHIP del json_path")

    # MODO APROBADO: gfa_aprobado_m2 > 0 y valido=True
    modo_aprobado = (gfa_aprobado_m2 is not None and
                     to_float(gfa_aprobado_m2, 0.0, []) > 0.0 and
                     parse_gh_bool(valido))

    if modo_aprobado:
        gfa_para_f2 = to_float(gfa_aprobado_m2, 0.0, warnings)
        ocup_para_f2 = to_float(ocupacion_aprobada_m2, 0.0, warnings)
        gfa_label = "gfa_aprobado_m2"
        ocup_label = "ocupacion_aprobada_m2"
    else:
        gfa_para_f2 = to_float(gfa_total, 0.0, warnings)
        ocup_para_f2 = to_float(ocupacion_real, 0.0, warnings)
        gfa_label = "gfa_total_m2"
        ocup_label = "ocupacion_real"

    data = {
        "chip": chip_str,
        "tipo": "resultados-f1-grasshopper",
        "fuente": "F1_Contexto_Base-Editado_v02 (F1_EXPORTAR_GFA_v02.4)",
        "generado": date.today().isoformat(),
        "area_envelope_m2": round(to_float(area_envelope, 0.0, warnings), REDONDEO),
        gfa_label: round(gfa_para_f2, REDONDEO),
        ocup_label: round(ocup_para_f2, REDONDEO),
        "io_maximo": round(to_float(io_maximo, 0.0, warnings), REDONDEO),
        "ic_real": round(to_float(ic_real, 0.0, warnings), REDONDEO),
        "ic_maximo": round(to_float(ic_maximo, 0.0, warnings), REDONDEO),
        "altura_total_m": round(to_float(altura_total, 0.0, warnings), REDONDEO),
        "pisos_finales": to_int(pisos_finales, 0, warnings),
        "valido": parse_gh_bool(valido),
        "mensaje": str(unwrap(mensaje) or ""),
        "modo": "APROBADO" if modo_aprobado else "POTENCIAL",
    }

    override = parse_flag_pipeline(flag_pipeline)
    if override is not None:
        data["override_uso"] = override

    if warnings: data["warnings"] = warnings
    return data, warnings, modo_aprobado


# ------------------------------------------------------------------ ejecucion
data, warnings, modo_aprobado = build_payload()
json_text = json.dumps(data, indent=2, ensure_ascii=True, sort_keys=True)

valido_calc = parse_gh_bool(valido)
flag_exportar = leer_flag()

if data["chip"] == "":
    estado = "ERROR: no se pudo derivar el CHIP del json_path (no se escribe)"
    ruta_json = ""
elif not flag_exportar:
    estado = "EN_ESPERA: flag exportar=False (use 'Exportar GFA' en el orquestador)"
    ruta_json = ""
elif not valido_calc:
    estado = "NO_ESCRITO: valido=False (el calculo normativo no es valido)"
    ruta_json = ""
else:
    try:
        carpeta = unwrap(output_path)
        if carpeta is None or str(carpeta).strip() == "":
            carpeta = DEFAULT_OUTPUT_DIR
            warnings.append("output_path vacio -> default del proyecto")
        carpeta = str(carpeta).strip()
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)

        ruta_archivo = os.path.join(carpeta, data["chip"] + "-gfa-gh.json")
        ruta_activo = os.path.join(carpeta, "CHIP-gfa-gh.json")

        with open(ruta_archivo, "wb") as f:
            f.write(json_text.encode("utf-8"))
        with open(ruta_activo, "wb") as f:
            f.write(json_text.encode("utf-8"))

        reset_flag()
        ruta_json = ruta_archivo
        modo_str = "APROBADO" if modo_aprobado else "POTENCIAL"
        estado = "OK [{0}]: escrito {1} (activo: {2})".format(modo_str, ruta_archivo, ruta_activo)
    except Exception as e:
        estado = "ERROR escribiendo JSON: " + str(e)
        ruta_json = ""

warning = " | ".join(warnings) if warnings else "sin advertencias"

try:
    ghenv.Component.Message = estado
except Exception:
    pass