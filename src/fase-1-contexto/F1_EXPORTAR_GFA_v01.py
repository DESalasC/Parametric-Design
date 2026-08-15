# -*- coding: utf-8 -*-
"""
================================================================================
F1_EXPORTAR_GFA_v01.py - Exporta GFA y KPIs de Fase 1 a JSON para Fase 2
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Toma las salidas de F1_ETAPA2_NORMATIVA_v03 (gfa_total, pisos_finales,
  indices, envelope) y escribe un JSON de resultados en data/fase-2-demanda/
  para alimentar el pipeline F2 (motor financiero y modelo Build-to-Rent)
  sin intervencion manual. Es el puente GH -> F2 registrado en el vault
  (60-diario/2026-08-12): "Conectar el GFA real generado en Grasshopper al
  script de Python 3.12 para automatizar la evaluacion de viabilidad".

NORMATIVA APLICABLE:
  Decreto 555 de 2021 (rangos de edificabilidad, piso adicional) - los valores
  ya vienen calculados por F1_ETAPA2_NORMATIVA_v03; aqui solo se serializan.

REGLA DE SEGURIDAD:
  Grasshopper recalcula en cada iteracion del solver. El archivo SOLO se
  escribe cuando el toggle "ejecutar" esta en True; con False se genera el
  preview (json_text) sin tocar disco.

ENTRADAS:
  chip (String)          - CHIP catastral del predio (ej: AAA0127AZPA).
                           Si falta, el componente NO escribe (estado ERROR).
  area_envelope (Number) - Huella fisica con retiros y patio restado [m2].
                           Viene del Area de envelope_curve (NORMATIVA v03).
  gfa_total (Number)     - Area Bruta Construida incl. piso adicional [m2]
                           (NORMATIVA v03).
  ocupacion_real (Number)- Indice de ocupacion real (NORMATIVA v03).
  io_maximo (Number)     - IO normativo (o override de usuario).
  ic_real (Number)       - Indice de construccion real (NORMATIVA v03).
  ic_maximo (Number)     - IC normativo.
  altura_total (Number)  - Altura total [m] = pisos_finales * entrepiso.
  pisos_finales (Number) - Pisos aplicados (rango + piso adicional).
  valido (Boolean)       - Validez del calculo normativo (NORMATIVA v03).
  mensaje (String)       - Diagnostico de NORMATIVA v03.
  output_path (String)   - Carpeta destino. Default: data/fase-2-demanda/
                           del proyecto (ver DEFAULT_OUTPUT_DIR).
  ejecutar (Boolean)     - True = escribir el JSON en disco. Default False.

SALIDAS:
  ruta_json (String)     - Ruta absoluta del archivo escrito ("" si no se
                           escribio).
  json_text (String)     - Contenido JSON completo (preview en Panel).
  estado (String)        - "OK: escrito <ruta>" | "NO_EJECUTADO..." |
                           "ERROR: ...".
  warning (String)       - Advertencias acumuladas (entradas con default).

FUNCIONES INTERNAS:
  unwrap(val)        - Extrae el primer elemento si llega lista de GH.
  parse_gh_bool(val) - Lee toggles de GH a prueba de fallos.
  to_float(val, def) - Convierte a float; default + warning si falla.
  to_int(val, def)   - Convierte a int; default + warning si falla.
  build_payload()    - Arma el dict de resultados con redondeo a 4 decimales.

VERSIONES:
  v01 - Creacion (2026-08-15). Exportador GFA/KPIs F1 -> JSON para F2.

INTEGRACION EN CANVAS (F1_Contexto_Base-Editado_v00):
  1. Colocar aguas abajo de F1_ETAPA2_NORMATIVA_v03 (grupo DIBUJO 2: OCUPACION).
  2. Conectar "area_envelope" al Area (Area component) de envelope_curve.
  3. Conectar gfa_total, ocupacion_real, ic_real, ic_maximo, altura_total,
     pisos_finales, valido, mensaje a las salidas de NORMATIVA v03.
  4. Conectar "chip" a un Panel (mismo CHIP del JSON de contexto).
  5. Conectar "ejecutar" a un Boolean Toggle (False por defecto); ponerlo en
     True solo cuando se quiera generar/actualizar el archivo.
  6. "output_path" es opcional; si no se conecta usa el default del proyecto.
  7. Verificar en un Panel las salidas estado, ruta_json y json_text.
================================================================================
"""

import json
import os
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


# ------------------------------------------------------------------ entradas
# GHPython: una entrada NO conectada no define la variable (NameError).
# Se leen con globals().get() para tolerar entradas sin cable.
chip = globals().get("chip", None)
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
ejecutar = globals().get("ejecutar", False)
output_path = globals().get("output_path", None)


def build_payload():
    """Arma el dict de resultados con los valores (redondeados a 4 dec)."""
    warnings = []

    chip_val = unwrap(chip)
    if chip_val is None:
        chip_val = ""
    chip_str = str(chip_val).strip()

    data = {
        "chip": chip_str,
        "tipo": "resultados-f1-grasshopper",
        "fuente": "F1_Contexto_Base-Editado_v00 (F1_EXPORTAR_GFA_v01)",
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

    if len(warnings) > 0:
        data["warnings"] = warnings
    return data, chip_str, warnings


def resolver_destino(chip_str, warnings):
    """Resuelve la carpeta destino: input output_path o default del proyecto."""
    carpeta = unwrap(output_path)
    if carpeta is None or str(carpeta).strip() == "":
        carpeta = DEFAULT_OUTPUT_DIR
        warnings.append("output_path vacio -> default del proyecto")
    carpeta = str(carpeta).strip()
    return carpeta


# ------------------------------------------------------------------ ejecucion
data, chip_str, warnings = build_payload()
json_text = json.dumps(data, indent=2, ensure_ascii=False)

flag_ejecutar = parse_gh_bool(ejecutar)

if chip_str == "":
    estado = "ERROR: falta entrada chip (no se escribe el archivo)"
    ruta_json = ""
    warnings.append("chip vacio -> archivo NO escrito")
elif not flag_ejecutar:
    estado = "NO_EJECUTADO: toggle ejecutar=False (preview en json_text)"
    ruta_json = ""
else:
    try:
        carpeta = resolver_destino(chip_str, warnings)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        ruta_json = os.path.join(carpeta, chip_str + "-gfa-gh.json")
        # 'wb' + utf-8: seguro para el caracter 'n' del nombre del proyecto
        with open(ruta_json, "wb") as f:
            f.write(json_text.encode("utf-8"))
        estado = "OK: escrito " + ruta_json
    except Exception as e:  # noqa: BLE001 - IronPython 2.7 no tiene logging tipado
        estado = "ERROR escribiendo JSON: " + str(e)
        ruta_json = ""

warning = " | ".join(warnings) if warnings else "sin advertencias"

try:
    ghenv.Component.Message = estado  # noqa: F821 - inyectado por Grasshopper
except Exception:  # noqa: BLE001
    pass
