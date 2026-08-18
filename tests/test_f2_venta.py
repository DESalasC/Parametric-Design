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

import F2_DEMANDA_MOTOR_v03 as motor


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


# ---------------------------------------------------------------
# Aporte parcial/total (fraccion_aporte_pct)
# ---------------------------------------------------------------

def _resultados_aporte():
    import copy
    params = copy.deepcopy(motor.cargar_parametros(
        str(FIN_DIR / "parametros_AAA0127AZPA_venta_gfa1053_cl550.json")))
    fin = params["financiero"]
    gfa = params.get("gfa_max_m2", 1053.0)
    cl = motor.costo_lote_total(params["lote"])
    resultados = []
    for eid, esc in params["escenarios"].items():
        e = dict(esc)
        e["id"] = eid
        resultados.append(motor.run_scenario(gfa, cl, e, fin))
    return params, resultados, cl


def test_aporte_total_regresion():
    """fraccion 100 (default): comportamiento identico al aporte total previo."""
    params, resultados, cl = _resultados_aporte()
    if not isinstance(params.get("aporte_suelo"), dict):
        params["aporte_suelo"] = {}
    params["aporte_suelo"]["fraccion_aporte_pct"] = 100.0
    a = motor.analizar_aporte_suelo(resultados, params)
    assert a["fraccion_aporte_pct"] == 100.0
    assert a["cl_compra_cop"] == pytest.approx(0.0)
    assert a["cl_aportado_cop"] == pytest.approx(cl)
    for f in a["escenarios"]:
        assert f["ub_equity_cop"] == pytest.approx(f["ub_sin_suelo_cop"])
        assert f["ctd_full_cop"] == pytest.approx(f["ctd_sin_suelo_cop"])
        assert f["cl_compra_cop"] == pytest.approx(0.0)


def test_aporte_parcial_consistente():
    """fraccion 50: el desarrollador compra la mitad; el flujo de caja queda consistente."""
    params, resultados, cl = _resultados_aporte()
    if not isinstance(params.get("aporte_suelo"), dict):
        params["aporte_suelo"] = {}
    params["aporte_suelo"]["fraccion_aporte_pct"] = 50.0
    params["aporte_suelo"]["pct_socio"] = None
    a = motor.analizar_aporte_suelo(resultados, params)
    assert a["fraccion_aporte_pct"] == 50.0
    assert a["cl_compra_cop"] == pytest.approx(cl * 0.5)
    for f in a["escenarios"]:
        assert f["cl_compra_cop"] == pytest.approx(cl * 0.5)
        assert f["ub_equity_cop"] == pytest.approx(f["ub_sin_suelo_cop"] - cl * 0.5)

    esc = max(resultados, key=lambda r: r["ROI_pct"])
    fila = next(f for f in a["escenarios"] if f["escenario_id"] == esc["escenario_id"])
    pct = fila["pct_socio_recomendado_pct"] or 0.0
    flujo = motor.flujo_caja_estimado(esc, params, pct, "aporte")
    assert flujo["consistente"] is True
    assert flujo["fraccion_aporte_pct"] == 50.0
    assert flujo["cl_compra_cop"] == pytest.approx(cl * 0.5)
    ub_nl = esc["utilidad_bruta_cop"] + esc["costo_lote_cop"]
    ub_equity = ub_nl - cl * 0.5
    reparto = max(ub_equity, 0.0) * pct / 100.0
    assert flujo["ub_esperada_cop"] == pytest.approx(ub_equity - reparto)


def test_aporte_pago_parcial():
    """pago_parcial_pct = 40%: el dueno recibe 40% del CL en efectivo y participa del resto."""
    params, resultados, cl = _resultados_aporte()
    if not isinstance(params.get("aporte_suelo"), dict):
        params["aporte_suelo"] = {}
    params["aporte_suelo"]["pago_parcial_pct"] = 40.0
    params["aporte_suelo"]["fraccion_aporte_pct"] = 100.0  # debe ser ignorado (prima pago_parcial)
    params["aporte_suelo"]["pct_socio"] = None
    a = motor.analizar_aporte_suelo(resultados, params)
    assert a["pago_parcial_pct"] == 40.0
    assert a["fraccion_aporte_pct"] == 60.0
    assert a["cl_compra_cop"] == pytest.approx(cl * 0.4)
    assert a["cl_aportado_cop"] == pytest.approx(cl * 0.6)

    esc = max(resultados, key=lambda r: r["ROI_pct"])
    fila = next(f for f in a["escenarios"] if f["escenario_id"] == esc["escenario_id"])
    assert fila["pago_parcial_pct"] == 40.0
    pct = fila["pct_socio_recomendado_pct"] or 0.0
    flujo = motor.flujo_caja_estimado(esc, params, pct, "aporte")
    assert flujo["consistente"] is True
    assert flujo["pago_parcial_pct"] == 40.0
    assert flujo["fraccion_aporte_pct"] == 60.0
    assert flujo["cl_compra_cop"] == pytest.approx(cl * 0.4)
