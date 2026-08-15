# -*- coding: utf-8 -*-
"""
================================================================================
F1_EXPORTAR_GFA_v02.py - Exporta GFA y KPIs de Fase 1 a JSON para Fase 2
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Toma las salidas de F1_ETAPA2_NORMATIVA_v04 (gfa_total, pisos_finales,
  indices, envelope) y escribe <CHIP>-gfa-gh.json en data/fase-2-demanda/
  para alimentar F2 (F2_DEMANDA_MOTOR_v03 y F2_RENTA_MOTOR_v03 leen este
  archivo automaticamente cuando no se les pasa --gfa).

AUTOMATIZACION (v02):
  - SIN toggle de operador: escribe solo cuando valido=True Y el contenido
    cambio respecto al archivo ya escrito (el JSON queda siempre al dia).
  - CHIP derivado automaticamente del json_path (data/pot-cache/<CHIP>-contexto.json,
    el mismo panel que ya alimenta F1_ETAPA1_CONTEXTO_v01). El operador no
    tipea nada.
  - flag_pipeline (opcional, salida de F1_OVERRIDE_USO_v01) se incorpora al
    JSON como "override_uso" para que F2 sepa que uso se evaluo.

NORMATIVA APLICABLE:
  Decreto 555 de 2021 (rangos de edificabilidad, piso adicional) - los valores
  ya vienen calculados por F1_ETAPA2_NORMATIVA_v04; aqui solo se serializan.

ENTRADAS:
  json_path (String)       - Ruta al JSON de contexto de Fase 1
                             (data/pot-cache/<CHIP>-contexto.json). De aqui se
                             deriva el CHIP; si falta, NO se escribe (estado
                             ERROR).
  area_envelope (Number)   - Huella fisica con retiros y patio restado [m2]
                             (Area de envelope_curve, NORMATIVA v04).
  gfa_total (Number)       - Area Bruta Construida TOTAL incl. piso extra [m2].
  ocupacion_real (Number)  - Indice de ocupacion real.
  io_maximo (Number)       - IO normativo (o override de usuario).
  ic_real (Number)         - Indice de construccion real.
  ic_maximo (Number)       - IC normativo (pisos base + incentivos).
  altura_total (Number)    - Altura total [m].
  pisos_finales (Number)   - Pisos aplicados.
  valido (Boolean)         - Validez del calculo normativo. Si False no escribe.
  mensaje (String)         - Diagnostico de NORMATIVA v04.
  flag_pipeline (String)   - [opcional] Salida de F1_OVERRIDE_USO_v01
                             ("USO_NORMA:<uso>" o "USO_OVERRIDE:<uso>;<nota>").
  output_path (String)     - [opcional] Carpeta destino. Default:
                             data/fase-2-demanda/ del proyecto.

SALIDAS:
  ruta_json (String) - Ruta absoluta del archivo escrito ("" si no se escribio).
  json_text (String) - Contenido JSON completo (preview en Panel).
  estado (String)    - "OK: escrito <ruta>" | "SIN_CAMBIOS..." |
                       "NO_ESCRITO: valido=False" | "ERROR: ...".
  warning (String)   - Advertencias acumuladas (entradas con default).

FUNCIONES INTERNAS:
  unwrap(val)          - Extrae el primer elemento si llega lista de GH.
  parse_gh_bool(val)   - Lee toggles/booleans de GH a prueba de fallos.
  to_float(val, def)   - Convierte a float; default + warning si falla.
  to_int(val, def)     - Convierte a int; default + warning si falla.
  derivar_chip(ruta)   - Extrae el CHIP del nombre del JSON de contexto.
  parse_flag_pipeline(flag) - Convierte el token del OVERRIDE a dict.

VERSIONES:
  v02 (2026-08-15) - Escritura automatica (sin toggle): valido=True + cambio
                     de contenido; CHIP derivado de json_path; integra
                     flag_pipeline del OVERRIDE como override_uso.
  v01 (2026-08-15) - Exportador manual con toggle ejecutar y CHIP tipeado.

INTEGRACION EN CANVAS (F1_Contexto_Base-Editado_v00):
  1. Colocar aguas abajo de F1_ETAPA2_NORMATIVA_v04 (grupo DIBUJO 2: OCUPACION).
  2. Conectar "json_path" al MISMO panel que alimenta F1_ETAPA1_CONTEXTO_v01.
  3. Conectar "area_envelope" al Area de envelope_curve, y el resto de
     entradas a las salidas de NORMATIVA v04 (gfa_total, ocupacion_real,
     io_maximo, ic_real, ic_maximo, altura_total, pisos_finales, valido,
     mensaje).
  4. [opcional] Conectar "flag_pipeline" a la salida del OVERRIDE_USO_v01.
  5. Sin toggles: el archivo se escribe/actualiza solo cuando el calculo es
     valido y el valor cambia. Verificar estado/ruta_json/json_text en Panels.
================================================================================
"""

import json
import os
import re
from datetime import date

DEFAULT_OUTPUT_DIR = r"D:\Work\PROJECTS\DiseñoParametrico\data\fase-2-demanda"
REDONDEO = 4


def unwrap(val):
    """Extrae el primer elemento si GH envia una lista de un solo item."""
    if val is None:
        return None
    if isinstance(val, list):
        return val[0] if len(val) > 0 else None
    return val


def parse_gh_bool(val):
    """Lee Toggles de Grasshopper a prueba de fallos (tipos .NET incluidos)."""
    if val is None:
        return False
    if isinstance(val, list):
        val = val[0] if len(val) > 0 else None
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    s = str(val).strip().lower()
    return s in ("true", "1", "verdadero", "yes", "si")


def to_float(val, default, warnings):
    """Convierte a float; si falla usa default y registra warning."""
    val = unwrap(val)
    if val is None:
        warnings.append("entrada numerica faltante -> default {0}".format(default))
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        warnings.append("valor no numerico '{0}' -> default {1}".format(str(val), default))
        return default


def to_int(val, default, warnings):
    """Convierte a int; si falla usa default y registra warning."""
    val = unwrap(val)
    if val is None:
        warnings.append("entrada entera faltante -> default {0}".format(default))
        return default
    try:
        return int(round(float(val)))
    except (TypeError, ValueError):
        warnings.append("valor no entero '{0}' -> default {1}".format(str(val), default))
        return default


def derivar_chip(ruta):
    """Extrae el CHIP de la entrada json_path, tolerante a formatos.

    Acepta:
      - ruta al JSON de contexto: "data/pot-cache/AAA0127AZPA-contexto.json"
      - el nombre solo: "AAA0127AZPA-contexto.json"
      - el CONTENIDO del JSON (empieza con '{') con chip/metadata.chip
      - comillas envolventes y/o saltos de linea alrededor
    """
    raw = unwrap(ruta)
    if raw is None:
        return ""
    s = str(raw).strip()
    s = s.strip().strip('"').strip("'")
    s = s.strip()
    if s == "":
        return ""

    # 1) patron clasico <CHIP>-contexto.json (en cualquier parte de la ruta)
    m = re.search(r"([A-Za-z0-9]{4,})-contexto\.json", s.replace("\\", "/"))
    if m:
        return m.group(1)

    # 2) si el valor ES el contenido del JSON
    if s.startswith("{"):
        try:
            datos = json.loads(s)
            chip = datos.get("chip") or (datos.get("metadata") or {}).get("chip")
            if chip:
                return str(chip).strip()
        except Exception:
            pass
        return ""

    # 3) si es una ruta a un archivo existente, leerlo y buscar chip
    try:
        with open(s, "rb") as f:
            datos = json.loads(f.read().decode("utf-8-sig"))
        chip = datos.get("chip") or (datos.get("metadata") or {}).get("chip")
        if chip:
            return str(chip).strip()
    except Exception:
        pass

    return ""


def parse_flag_pipeline(flag):
    """Convierte el token del OVERRIDE_USO en dict (o None si no llega)."""
    flag = unwrap(flag)
    if flag is None:
        return None
    s = str(flag).strip()
    if s == "":
        return None
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
# GHPython: una entrada NO conectada no define la variable (NameError).
# Se leen con globals().get() como en F1_ETAPA2_NORMATIVA_v04.
json_path = globals().get("json_path", None)
area_envelope = globals().get("area_envelope", None)
gfa_total = globals().get("gfa_total", None)
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


def build_payload():
    """Arma el dict de resultados con los valores (redondeados a 4 dec)."""
    warnings = []

    chip_str = derivar_chip(json_path)
    if chip_str == "":
        warnings.append("no se pudo derivar CHIP del json_path")

    data = {
        "chip": chip_str,
        "tipo": "resultados-f1-grasshopper",
        "fuente": "F1_Contexto_Base-Editado_v00 (F1_EXPORTAR_GFA_v02)",
        "generado": date.today().isoformat(),
        "area_envelope_m2": round(to_float(area_envelope, 0.0, warnings), REDONDEO),
        "gfa_total_m2": round(to_float(gfa_total, 0.0, warnings), REDONDEO),
        "ocupacion_real": round(to_float(ocupacion_real, 0.0, warnings), REDONDEO),
        "io_maximo": round(to_float(io_maximo, 0.0, warnings), REDONDEO),
        "ic_real": round(to_float(ic_real, 0.0, warnings), REDONDEO),
        "ic_maximo": round(to_float(ic_maximo, 0.0, warnings), REDONDEO),
        "altura_total_m": round(to_float(altura_total, 0.0, warnings), REDONDEO),
        "pisos_finales": to_int(pisos_finales, 0, warnings),
        "valido": parse_gh_bool(valido),
        "mensaje": str(unwrap(mensaje) or ""),
    }

    override = parse_flag_pipeline(flag_pipeline)
    if override is not None:
        data["override_uso"] = override

    if len(warnings) > 0:
        data["warnings"] = warnings
    return data, warnings


# ------------------------------------------------------------------ ejecucion
data, warnings = build_payload()
# sort_keys para comparacion estable (evita re-escrituras espurias)
json_text = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True)

valido_calc = parse_gh_bool(valido)

if data["chip"] == "":
    estado = "ERROR: no se pudo derivar el CHIP del json_path (no se escribe)"
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
        ruta_json = os.path.join(carpeta, data["chip"] + "-gfa-gh.json")

        # Deteccion de cambios: solo escribe si el contenido es distinto
        if os.path.exists(ruta_json):
            with open(ruta_json, "rb") as f:
                previo = f.read().decode("utf-8")
            if previo == json_text:
                estado = "SIN_CAMBIOS: el archivo ya esta al dia"
            else:
                with open(ruta_json, "wb") as f:
                    f.write(json_text.encode("utf-8"))
                estado = "OK: escrito " + ruta_json
        else:
            with open(ruta_json, "wb") as f:
                f.write(json_text.encode("utf-8"))
            estado = "OK: escrito " + ruta_json
    except Exception as e:  # noqa: BLE001 - IronPython 2.7
        estado = "ERROR escribiendo JSON: " + str(e)
        ruta_json = ""

warning = " | ".join(warnings) if warnings else "sin advertencias"

try:
    ghenv.Component.Message = estado  # noqa: F821 - inyectado por Grasshopper
except Exception:  # noqa: BLE001
    pass
