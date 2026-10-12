"""
================================================================================
F1_LAYERS_XML_v02.py — Genera XML de capas importable por ArchiCAD
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Reemplaza el enfoque de creacion directa de layers via HTTP/plugins
  (que no funciona). Convierte la lista de capas (json_text) en un archivo
  XML en formato AttributeFile nativo de ArchiCAD.

  El XML resultante se importa en ArchiCAD con:
    Opciones > Atributos de Elemento > Administrador de Atributos > Importar

CAMBIOS v02 (2026-08-15):
  MERGE DEFENSIVO DE CAPAS CRITICAS: si el operador alimenta un json_text
  propio incompleto (p.ej. sin el layer del lote), se re-anaden al final
  las capas criticas del estandar que falten. Esto garantiza que el layer
  "00-00-10_Lote_proyecto" (y los del entorno urbano) SIEMPRE existan en
  ArchiCAD, como pidio el usuario: el layer del lote debe estar incluido
  en el script de arranque. Salida nueva: missing_layers (String JSON).

ENTRADAS:
  json_text   (String)  — Lista JSON de capas: [{"nombre","color","visible"},...]
  output_path (String)  — Ruta completa del archivo XML a escribir
  execute     (Boolean) — True = escribe el archivo; False = solo genera xml_text

SALIDAS:
  xml_text       (String)  — Contenido XML generado
  status         (String)  — Diagnostico
  layer_count    (Integer) — Numero de capas procesadas
  missing_layers (String)  — JSON con las capas criticas re-anadidas ([] si nada)

NOTA: IronPython 2.7 — sin f-strings, usar .format(). Escritura con io.open().
================================================================================
"""

import json
import io
import os
import uuid
from xml.sax.saxutils import escape

# Capas por defecto del estandar del proyecto (pipeline v26)
CAPAS_ESTANDAR = [
    {"nombre": "00-00-10_Lote_proyecto", "color": 1, "visible": True},
    {"nombre": "00-20-20_Elementos_entorno_urbano", "color": 2, "visible": True},
    {"nombre": "00-20-30_Ejes_vias", "color": 8, "visible": True},
    {"nombre": "70-50-10_Zonas_verdes_publicas", "color": 3, "visible": True},
    {"nombre": "70-30-20_Andenes_preexistentes", "color": 4, "visible": True},
    {"nombre": "10-20-10_Topografia", "color": 5, "visible": True},
    {"nombre": "70-20-20_Perimetros_vecinos", "color": 9, "visible": True},
    {"nombre": "70-20-30_Volumetrias_vecinas", "color": 6, "visible": True},
    {"nombre": "00-10-20_Elementos_referencia", "color": 7, "visible": True},
]

# Capas criticas: deben existir SIEMPRE (merge defensivo v02)
CAPAS_CRITICAS = [
    "00-00-10_Lote_proyecto",
    "00-20-20_Elementos_entorno_urbano",
    "00-20-30_Ejes_vias",
    "70-50-10_Zonas_verdes_publicas",
    "70-30-20_Andenes_preexistentes",
    "70-20-20_Perimetros_vecinos",
    "70-20-30_Volumetrias_vecinas",
]

EMPTY_ATTRS = [
    ("Composites", "1129791794"), ("Dimension Standards", "1398033970"),
    ("Fills", "1179208755"), ("Layer Combinations", "1279479602"),
    ("Lines", "1279872562"), ("Surfaces", "1296127026"),
    ("Pens", "1347699276"), ("Zone Categories", "1380795186"),
    ("Issue Styles", "1297306713"), ("Profiles", "1347571526"),
    ("MEP Systems", "1296388179"), ("Operation Profiles", "1162104656"),
    ("Renovation Override Styles", "1196381778"), ("Building Materials", "1112359252"),
]


def merge_capas_criticas(layers):
    """v02: re-anade las capas criticas del estandar que falten en la lista.

    Retorna (layers_ok, missing) donde missing es la lista de capas anadidas.
    """
    existentes = set()
    for layer in layers:
        nombre = str(layer.get("nombre", "")).strip()
        if nombre:
            existentes.add(nombre)

    missing = []
    for capa in CAPAS_ESTANDAR:
        if capa["nombre"] in CAPAS_CRITICAS and capa["nombre"] not in existentes:
            layers.append(dict(capa))
            missing.append(capa["nombre"])

    return layers, missing


def generar_xml_layers(layers):
    """
    Genera el XML AttributeFile de ArchiCAD con las capas dadas.
    Retorna el XML como string.
    """
    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>')
    lines.append('<AttributeFile Mv="1" Sv="2">')
    lines.append('\t<PlatformSign>22359</PlatformSign>')
    lines.append('\t<RegisteredAttributes>')
    lines.append('\t\t<NumberOfRegisteredAttributes>1</NumberOfRegisteredAttributes>')
    lines.append('\t\t<Attributes Type="Layers">')
    lines.append('\t\t\t<RefID>1279351090</RefID>')

    for idx, layer in enumerate(layers, start=1):
        nombre = str(layer.get("nombre", "")).strip()
        if not nombre:
            continue
        guid = str(uuid.uuid4()).upper()
        nombre_esc = escape(nombre)

        lines.append('\t\t\t<Layer Idx="{0}" Name="{1}">'.format(idx, nombre_esc))
        lines.append('\t\t\t\t<OdbObj Mv="2" Sv="0">')
        lines.append('\t\t\t\t\t<OdbRef>')
        lines.append('\t\t\t\t\t\t<guid>{0}</guid>'.format(guid))
        lines.append('\t\t\t\t\t</OdbRef>')
        lines.append('\t\t\t\t\t<CreaTime>23970</CreaTime>')
        lines.append('\t\t\t\t\t<ModiTime>23972</ModiTime>')
        lines.append('\t\t\t\t</OdbObj>')
        lines.append('\t\t\t\t<Name>{0}</Name>'.format(nombre_esc))
        lines.append('\t\t\t\t<Index>{0}</Index>'.format(idx))
        lines.append('\t\t\t\t<Flags/>')
        lines.append('\t\t\t\t<ModiTime>1164398284</ModiTime>')
        lines.append('\t\t\t\t<RegMemoTable MemoNumber="0" Mv="1" Sv="0"/>')
        lines.append('\t\t\t\t<ReadOnly>false</ReadOnly>')
        lines.append('\t\t\t\t<ConnectionClassId>1</ConnectionClassId>')
        lines.append('\t\t\t\t</Layer>')

    lines.append('\t\t</Attributes>')

    for attr, refid in EMPTY_ATTRS:
        lines.append('\t\t<Attributes Type="{0}">'.format(attr))
        lines.append('\t\t\t<RefID>{0}</RefID>'.format(refid))
        lines.append('\t\t</Attributes>')

    lines.append('\t</RegisteredAttributes>')
    lines.append('\t<Folders>')
    lines.append('\t\t<TypeRoot RefID="1279351090"/>')
    lines.append('\t</Folders>')
    lines.append('</AttributeFile>')

    return '\n'.join(lines)


# ==============================================================================
# MAIN
# ==============================================================================

json_text_raw = globals().get("json_text", None)
json_path_raw = globals().get("json_path", None)
output_path_raw = globals().get("output_path", None)
execute_raw = globals().get("execute", None)

try:
    if isinstance(json_text_raw, list):
        json_text = str(json_text_raw[0]) if json_text_raw else ""
    elif json_text_raw is not None:
        json_text = str(json_text_raw)
    else:
        json_text = ""
except:
    json_text = ""

# Limpiar caracteres de control de GH Panel
json_text = json_text.replace('\r', '').replace('\n', '').replace('\t', '').strip()

try:
    if isinstance(output_path_raw, list):
        output_path = str(output_path_raw[0]) if output_path_raw else ""
    elif output_path_raw is not None:
        output_path = str(output_path_raw)
    else:
        output_path = ""
except:
    output_path = ""

# Limpiar caracteres de control que GH Panel agrega (\r\n, \t, espacios)
output_path = output_path.replace('\r', '').replace('\n', '').replace('\t', '').strip()

try:
    execute = bool(execute_raw) if execute_raw is not None else False
except:
    execute = False

# --- Procesar capas ---
layers = []
# Fuente alternativa: archivo JSON de capas (si json_text viene vacio).
_json_path = ""
try:
    if isinstance(json_path_raw, list):
        _json_path = str(json_path_raw[0]) if json_path_raw else ""
    elif json_path_raw is not None:
        _json_path = str(json_path_raw)
except:
    _json_path = ""
_json_path = (_json_path or "").replace('\r', '').replace('\n', '').strip()
json_text_limpio = json_text.strip().strip("'\"")
if json_text_limpio:
    try:
        data = json.loads(json_text_limpio)
        if isinstance(data, list):
            layers = data
    except:
        layers = []
elif _json_path and os.path.exists(_json_path):
    try:
        with open(_json_path, 'rb') as f:
            _raw = f.read()
        try:
            _capa = json.loads(_raw.decode('utf-8'))
        except Exception:
            _capa = json.loads(_raw.decode('latin-1'))
        if isinstance(_capa, list):
            layers = _capa
    except:
        layers = []

if not layers:
    layers = [dict(c) for c in CAPAS_ESTANDAR]

# --- v02: merge defensivo de capas criticas ---
layers, missing = merge_capas_criticas(layers)

layer_count = len(layers)
missing_layers = json.dumps(missing)
xml_text = generar_xml_layers(layers)
status = "XML generado: {} capas".format(layer_count)

# --- Escribir archivo ---
if execute and output_path:
    try:
        # Si output_path es un directorio o no tiene extension, ajustar
        ruta_es_dir = os.path.isdir(output_path) or output_path.endswith(('/','\\'))
        if ruta_es_dir or not output_path.lower().endswith('.xml'):
            if ruta_es_dir:
                output_path = os.path.join(output_path, 'F1_Layers_Proyecto_v01.xml')
            else:
                output_path = output_path + '.xml'
        dir_out = os.path.dirname(output_path)
        if dir_out and not os.path.exists(dir_out):
            try:
                os.makedirs(dir_out)
            except Exception as e:
                status = "ERROR: No se pudo crear el directorio {}: {}".format(dir_out, str(e))
            else:
                with io.open(output_path, 'w', encoding='utf-8') as f:
                    f.write(xml_text)
                status = "EXITO: XML escrito en {} ({} capas)".format(output_path, layer_count)
        else:
            with io.open(output_path, 'w', encoding='utf-8') as f:
                f.write(xml_text)
            status = "EXITO: XML escrito en {} ({} capas)".format(output_path, layer_count)
    except Exception as e:
        status = "ERROR al escribir XML: {} (output_path={})".format(str(e), output_path)
elif not output_path:
    status = "AVISO: Falta output_path. Solo se genero xml_text ({} capas)".format(layer_count)
