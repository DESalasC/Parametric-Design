# -*- coding: utf-8 -*-
"""Guardian de regresion: F3_StorySync_v01 no debe hardcodear el puerto 19723.

AutoClaw ocupa 19723; ArchiCAD levanta su JSON API en 19724. El script debe
auto-detectar (puerto None -> ACConnection.connect() escanea 19723-19743).
"""

import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "interfases-archicad", "F3_StorySync_v01.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def test_no_hardcodea_19723():
    src = _fuente()
    assert "puerto = 19723" not in src
    assert "puerto = None" in src


def test_usa_connect_con_puerto_dinamico():
    src = _fuente()
    assert "ACConnection.connect(puerto)" in src
    assert "from archicad import ACConnection" in src


def test_docstring_documenta_auto_deteccion():
    src = _fuente()
    assert "auto-detectado 19723-19743" in src
