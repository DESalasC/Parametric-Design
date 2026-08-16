# -*- coding: utf-8 -*-
"""Guardian de regresion para F1_ETAPA2_NORMATIVA_v06.py.

Valida desde el fuente: precedencia del ancho de via con respaldo desde
LADOS_v06 (sides_data), tabla de antejardines por ancho de via (CU-5.5 /
regla historica) y prefijo del mensaje.
"""

import ast
import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-1-contexto", "F1_ETAPA2_NORMATIVA_v06.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def _tabla_antejardines():
    tree = ast.parse(_fuente())
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if getattr(t, "id", "") == "FRONTAL_POR_ANCHO_VIA":
                    return ast.literal_eval(node.value)
    raise AssertionError("FRONTAL_POR_ANCHO_VIA no encontrada")


def _retiro(ancho, tabla):
    if ancho is None or ancho <= 0:
        return 3.0
    for limite, retiro in tabla:
        if ancho < limite:
            return retiro
    return tabla[-1][1]


def test_tabla_antejardines_rangos():
    tabla = _tabla_antejardines()
    assert tabla == [(12.0, 3.0), (20.0, 5.0), (999.0, 7.0)]


def test_antejardin_12_96_es_5_m():
    # Caso real AAA0127AZPA (El Prado): perfil vial total 12,96 m
    # -> rango (12, 20] -> antejardin 5,0 m (regla historica / CU-5.5)
    assert _retiro(12.96, _tabla_antejardines()) == 5.0


def test_antejardin_bordes():
    tabla = _tabla_antejardines()
    assert _retiro(11.99, tabla) == 3.0
    assert _retiro(19.99, tabla) == 5.0
    assert _retiro(25.0, tabla) == 7.0


def test_respaldo_ancho_desde_lados():
    src = _fuente()
    assert "sides_data.get(\"ancho_via_m\")" in src
    assert "ancho_via_m desde LADOS_v06" in src


def test_precedencia_ancho():
    src = _fuente()
    assert "operador > LADOS_v06 (sides_data) > reglamentacion" in src


def test_mensaje_v06():
    src = _fuente()
    assert "NORMATIVA v06 | OK" in src
    assert "NORMATIVA v06 | ERROR DE VALIDACION" in src
    assert "NORMATIVA v05 |" not in src
