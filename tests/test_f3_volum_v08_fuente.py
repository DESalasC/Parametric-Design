# -*- coding: utf-8 -*-
"""Guardian de regresion para F3_VOLUM_GENERADOR_v08.py.

v08.0 agrega, paralelas 1:1 a sus salidas de geometria, las listas de piso
`circulacion_pisos`, `servicios_pisos`, `losas_pisos` y `nucleo_pisos`, para
alimentar F3_MORPH_ATRIBUTOS (asignacion de Story en ArchiCAD sin adivinar el
piso). Este guard fija el contrato de salidas y la compatibilidad IronPython 2.7.
"""

import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def test_encabezado_subversiones_v08():
    src = _fuente()
    assert "SUBVERSIONES INTERNAS" in src
    assert "v08.0" in src


def test_salidas_pisos_paralelas_v08():
    src = _fuente()
    assert "circulacion_pisos = []" in src
    assert "servicios_pisos = []" in src
    assert "losas_pisos = []" in src
    assert "nucleo_pisos = []" in src
    assert "usos_pisos = []" in src


def test_nucleo_pisos_es_union():
    src = _fuente()
    assert "nucleo_pisos = list(circulacion_pisos) + list(servicios_pisos)" in src


def test_append_piso_por_geometria():
    src = _fuente()
    assert "circulacion_pisos.append(piso_num)" in src
    assert "servicios_pisos.append(piso_num)" in src
    assert "losas_pisos.append(piso_num)" in src
    assert "usos_pisos.append(piso_num)" in src


def test_contrato_volumetria_por_uso():
    src = _fuente()
    assert "volumenes_por_uso" in src
    assert "usos_etiquetas" in src


def test_mesh_para_morph_archicad():
    src = _fuente()
    assert "_brep_a_mesh" in src
    assert "Live Connection" in src
    assert "MORPH" in src


def test_interruptor_salida_morph():
    src = _fuente()
    assert "salida_morph" in src


def test_ironpython_27_compatible():
    src = _fuente()
    assert 'f"' not in src.replace('"""', "")
    assert not src.lstrip().startswith("#!")
    assert "def _caja_curva(cx, cy, ancho, largo):" in src
    assert "def _recortar_huecos(env_crv, cajas, area_losa, hueco_m2):" in src


def test_zonas_bep_y_stories_v081():
    """v08.1: nomenclatura BEP + cotas en mensaje + export de stories."""
    src = _fuente()
    for marcador in ("v08.1", "CATEGORIAS_BEP", "CATEGORIA_FALLBACK",
                     "def _categoria_bep", "def _nivel_bep", "def _plan_stories",
                     "def _escribir_json_stories", "def _raiz_proyecto",
                     "stories-export-flag.json", "niveles_deseados.json",
                     "cotas B1..B{}", "cotas-arranque.json"):
        assert marcador in src, marcador
    # la numeracion vieja de zonas quedo reemplazada por la BEP
    assert 'block["id"]+" \u00b7 "' not in src
    assert '"-P"+str(fi+1)' not in src
    # nota de decision: morphs fuera de F3 (solo contexto/vecinos)
    assert "ADR-023" in src