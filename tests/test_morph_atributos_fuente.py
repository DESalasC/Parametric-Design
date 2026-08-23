# -*- coding: utf-8 -*-
"""Guardian de regresion para el cableado F3 -> F3_MORPH_ATRIBUTOS -> F1_LAYERS_XML.

Bloque A: fija el contrato de formato entre la salida `layers_json` de
F3_MORPH_ATRIBUTOS_v02 y la entrada `json_text`/`json_path` de F1_LAYERS_XML_v02,
y entre `usos_pisos` (F3_VOLUM_GENERADOR_v08) y `pisos` (F3_MORPH_ATRIBUTOS_v02).
"""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "src")
RUTA_MORPH = os.path.join(BASE, "fase-3-masa", "F3_MORPH_ATRIBUTOS_v02.py")
RUTA_LAYERS = os.path.join(BASE, "fase-1-contexto", "F1_LAYERS_XML_v02.py")
RUTA_VOLUM = os.path.join(BASE, "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py")


def _fuente(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def test_layers_json_emite_lista_nombre_color_visible():
    src = _fuente(RUTA_MORPH)
    # Formato que consume F1_LAYERS_XML_v02: [{"nombre","color","visible"},...]
    assert '{"nombre": nombre, "color": 20 + k, "visible": True}' in src
    assert "layers_json = json.dumps(layers_unicos, ensure_ascii=False)" in src


def test_layers_json_usa_llaves_del_contrato():
    src = _fuente(RUTA_MORPH)
    assert '"nombre"' in src
    assert '"color"' in src
    assert '"visible"' in src


def test_layers_xml_consume_llave_nombre():
    src = _fuente(RUTA_LAYERS)
    # merge_capas_criticas y generar_xml_layers leen solo la llave "nombre".
    assert 'layer.get("nombre", "")' in src
    assert "json_text" in src


def test_layers_xml_acepta_json_path_alternativo():
    src = _fuente(RUTA_LAYERS)
    assert "json_path" in src
    assert "os.path.exists(_json_path)" in src


def test_contrato_usos_pisos_a_pisos():
    # F3 emite usos_pisos paralelo a volumenes_por_uso.
    volum = _fuente(RUTA_VOLUM)
    assert "usos_pisos = []" in volum
    # F3_MORPH_ATRIBUTOS consume la entrada "pisos" y documenta el cableado.
    morph = _fuente(RUTA_MORPH)
    assert "usos_pisos" in morph
    assert "pisos" in morph


def test_merge_defensivo_preserva_lote():
    src = _fuente(RUTA_LAYERS)
    assert "00-00-10_Lote_proyecto" in src
    assert "merge_capas_criticas" in src
