# -*- coding: utf-8 -*-
"""Guardian de regresion para F3_ACCESOS_INTEGRADOR_v02.py.

Valida desde el fuente y funcionalmente:
  1) IronPython 2.7 compatible (sin f-strings, sin shebang, sin rs, sin type hints)
  2) consume los productos REALES de F3 (layout_espacial + matriz_adyacencias)
  3) accesos por uso: publico -> fachada, privado -> nucleo, segregacion de flujos
"""

import os
import sys
import json
import io

SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "fase-3-masa")
sys.path.insert(0, SRC_DIR)

import F3_ACCESOS_INTEGRADOR_v02 as acc  # noqa: E402

RUTA = os.path.join(SRC_DIR, "F3_ACCESOS_INTEGRADOR_v02.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def _caso(cid):
    base = os.path.join(SRC_DIR, "casos", cid)
    layout = json.load(io.open(os.path.join(base, "layout_espacial.json"),
                               encoding="utf-8"))
    matriz = json.load(io.open(os.path.join(base, "matriz_adyacencias.json"),
                               encoding="utf-8"))
    return layout, matriz


def test_ironpython_27_compatible():
    src = _fuente()
    assert 'f"' not in src.replace('"""', "")
    assert not src.lstrip().startswith("#!")
    assert "rhinoscriptsyntax" not in src
    assert "from typing" not in src


def test_consume_layout_y_matriz_reales():
    src = _fuente()
    assert "layout_espacial.json" in src
    assert "matriz_adyacencias.json" in src
    assert "reparto_vertical" in src
    assert "def analizar_accesos" in src
    assert "nucleos" in src


def test_caso_a_accesos_por_uso():
    layout, matriz = _caso("A")
    r = acc.analizar_accesos(layout, matriz)
    usos = {a["uso"]: a for a in r["accesos"]}
    assert usos["Local comercial"]["tipo_acceso"] == "directo_fachada"
    assert usos["Local comercial"]["categoria"] == "publico"
    assert usos["Local comercial"]["planta_baja"] is True
    assert usos["Vivienda"]["tipo_acceso"] == "independiente_nucleo"
    assert usos["Vivienda"]["categoria"] == "privado"
    assert r["resumen"]["total_usos"] == 2
    assert r["resumen"]["total_accesos"] == 2


def test_caso_b_salud_consultorios_publico():
    layout, matriz = _caso("B_SALUD")
    r = acc.analizar_accesos(layout, matriz)
    usos = {a["uso"]: a for a in r["accesos"]}
    assert usos["Consultorios"]["categoria"] == "publico"
    assert usos["Consultorios"]["tipo_acceso"] == "directo_fachada"
    assert usos["Vivienda"]["categoria"] == "privado"


def test_segregaciones_detectadas_si_incompatibles():
    # matriz con un par incompatible (nivel 0) debe generar segregacion
    layout = {
        "reparto_vertical": {"Comercio": [1], "Vivienda": [2, 3]},
        "nucleos": {"total_m2_piso": 40.0},
        "niveles": [],
        "poblacion_estimada": {"total": 30},
    }
    matriz = {
        "usos": ["Comercio", "Vivienda"],
        "matriz": {"Comercio": {"Vivienda": 0}, "Vivienda": {"Comercio": 0}},
    }
    r = acc.analizar_accesos(layout, matriz)
    assert r["resumen"]["pares_incompatibles"] == 1
    assert r["segregaciones"][0]["par"] == ["Comercio", "Vivienda"]
