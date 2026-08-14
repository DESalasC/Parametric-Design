# -*- coding: utf-8 -*-
"""
Tests del modelo F2 (venta) — Fase 2, incluye el escenario de USO-MULTIPLE
(D_MIXTO con mix_usos, override de usuario fuera de reglamentacion).

Ejecutar:  pytest tests/test_f2_venta.py -v
"""
import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
FIN_DIR = PROJECT_ROOT / "src" / "fase-2-demanda" / "F2_Modelo_Financiero"
sys.path.insert(0, str(FIN_DIR))

import pytest

import F2_DEMANDA_MOTOR_v01 as motor


@pytest.fixture(scope="module")
def params_caso_a():
    with open(FIN_DIR / "parametros_AAA0127AZPA_venta_gfa1053_cl550.json", "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------
# Regresion: escenario puro (sin mix_usos) mantiene la logica v2.1
# ---------------------------------------------------------------

def test_run_scenario_estandar_regresion(params_caso_a):
    """B estandar GFA 1053: ef 0,75 -> NGA 789,75 -> 9 unid x 85 = 765 m2;
    IT = 765 x 6,8M = 5.202M; CD = 1053 x 3,0M = 3.159M."""
    esc = dict(params_caso_a["escenarios"]["B_ESTANDAR"])
    esc["id"] = "B_ESTANDAR"
    fin = params_caso_a["financiero"]
    res = motor.run_scenario(1053.0, 550_000_000, esc, fin)
    assert res["num_unidades"] == 9
    assert res["area_vendible_m2"] == pytest.approx(765.0)
    assert res["ingresos_totales_cop"] == pytest.approx(765.0 * 6_800_000)
    assert res["costo_duro_cop"] == pytest.approx(1053.0 * 3_000_000)
    assert res["mix_usos_detalle"] is None


# ---------------------------------------------------------------
# USO-MULTIPLE: escenario mixto (override usuario)
# ---------------------------------------------------------------

def test_run_scenario_mix_detalle(params_caso_a):
    """D_MIXTO del caso A (GFA 1053): 20% local (50 m2, ef 0,85) + 80% vivienda
    (65 m2, ef 0,78). Local: 179,01 NGA -> 3 locales = 150 m2 x 9,0M = 1.350M.
    Vivienda: 657,07 NGA -> 10 unid = 650 m2 x 6,8M = 4.420M.
    IT total = 5.770M; CD = (210,6 x 3,6M) + (842,4 x 3,0M) = 3.285,36M."""
    esc = dict(params_caso_a["escenarios"]["D_MIXTO"])
    esc["id"] = "D_MIXTO"
    fin = params_caso_a["financiero"]
    res = motor.run_scenario(1053.0, 550_000_000, esc, fin)
    assert res["num_unidades"] == 13
    assert res["area_vendible_m2"] == pytest.approx(800.0)
    assert res["ingresos_totales_cop"] == pytest.approx(5_770_000_000.0, rel=1e-9)
    assert res["costo_duro_cop"] == pytest.approx(3_285_360_000.0, rel=1e-9)
    assert res["mix_usos_detalle"] is not None
    assert len(res["mix_usos_detalle"]) == 2
    # precio promedio ponderado por area vendible
    it = sum(c["area_vendible_m2"] * c["precio_venta_m2"] for c in res["mix_usos_detalle"])
    assert it == pytest.approx(res["ingresos_totales_cop"], rel=1e-9)


def test_normalizar_mix_campos_agregados(params_caso_a):
    """La normalizacion agrega eficiencia/precio/costo promedio para que la
    sensibilidad marginal y el informe funcionen sin tocar el calculo principal."""
    escenarios = {k: dict(v) for k, v in params_caso_a["escenarios"].items()}
    motor._normalizar_mix(escenarios, 1053.0)
    mix = escenarios["D_MIXTO"]
    assert mix["_es_mixto"] is True
    assert mix["eficiencia_nga"] == pytest.approx(0.2 * 0.85 + 0.8 * 0.78)
    assert mix["precio_venta_m2"] == pytest.approx(5_770_000_000.0 / 800.0, rel=1e-6)
    # los escenarios puros no se tocan
    assert "_es_mixto" not in escenarios["A_VIS"]
