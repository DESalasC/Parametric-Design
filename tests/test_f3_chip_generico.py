# -*- coding: utf-8 -*-
"""F3_DISTRIBUCION_v01 puede leer resultados F2 de cualquier CHIP (no solo A/B/C)."""

import os
import sys

SRC = os.path.join(os.path.dirname(__file__), "..", "src", "fase-3-masa")
sys.path.insert(0, SRC)

import F3_DISTRIBUCION_v01 as f3  # noqa: E402


def test_buscar_resultados_chip():
    assert f3.buscar_resultados("AAA0030JKOE") == "resultados_AAA0030JKOE.json"
    r = f3.buscar_resultados("AAA0127AZPA")
    assert r and r.startswith("resultados_AAA0127AZPA")
    assert f3.buscar_resultados("ZZZ00000000") is None


def test_leer_programa_chip():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    assert prog["gfa_total"] > 0
    assert prog["lote_m2"] > 0
    assert prog["escenario"] == "D_MIXTO"
    assert any(c["uso"] == "Vivienda" for c in prog["componentes"])


def test_leer_programa_backcompat():
    assert abs(f3.leer_programa("A")["gfa_total"] - 1461.0972) < 1e-6
