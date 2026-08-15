# -*- coding: utf-8 -*-
"""
Tests del modelo F2 Renta (Build-to-Rent) — Fase 2.

Ejecutar:  pytest tests/test_f2_renta.py -v
"""
import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
RENTA_DIR = PROJECT_ROOT / "src" / "fase-2-demanda" / "F2_Modelo_Renta"
sys.path.insert(0, str(RENTA_DIR))

import pytest

import F2_RENTA_MOTOR_v03 as motor


@pytest.fixture(scope="module")
def params_lote_real():
    with open(RENTA_DIR / "parametros_AAA0127AZPA_renta.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def params_gfa1054():
    with open(RENTA_DIR / "parametros_AAA0127AZPA_renta_gfa1054.json", "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def params_gfa1053_cl550():
    with open(RENTA_DIR / "parametros_AAA0127AZPA_renta_gfa1053_cl550.json", "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------
# Área arrendable (unidades enteras, misma lógica que F2)
# ---------------------------------------------------------------

def test_area_arrendable_vis():
    """GFA 632,7 x eficiencia 0,8 = 506,16 m2 -> 9 unidades de 55 m2 = 495 m2."""
    esc = {"eficiencia_nga": 0.8, "unidad_m2": 55.0}
    unidades, area = motor.area_arrendable(632.695061, esc)
    assert unidades == 9
    assert area == pytest.approx(495.0)


def test_area_arrendable_estandar():
    """GFA 632,7 x 0,75 = 474,52 m2 -> 5 unidades de 85 m2 = 425 m2."""
    esc = {"eficiencia_nga": 0.75, "unidad_m2": 85.0}
    unidades, area = motor.area_arrendable(632.695061, esc)
    assert unidades == 5
    assert area == pytest.approx(425.0)


# ---------------------------------------------------------------
# NOI año 1 (cálculo literal)
# ---------------------------------------------------------------

def test_noi_anio1_lp_estandar():
    """LP B real: 425 m2 x $38.000 x 12 = GPI 193,8M; EGI 95% = 184,11M;
    adm 425x6.000x12 = 30,6M; gastos+capex 13% EGI = 23,9343M; NOI = 129,5757M."""
    esc = {"canon_m2_mes": {"LP": 38000.0}, "unidad_m2": 85.0,
           "eficiencia_nga": 0.75}
    estr = {"_id": "LP", "ocupacion_pct": 95.0, "administracion_m2_mes": 6000.0,
            "gastos_operativos_pct_egi": 12.0, "capex_pct_egi": 1.0}
    renta = {"incremento_canon_pct": 5.5, "incremento_gastos_pct": 6.5,
             "cap_rate_salida_pct": 6.2}
    unidades, area = motor.area_arrendable(632.695061, esc)
    fl = motor.flujo_anual(area, esc, estr, renta, 10)
    assert fl["gpi_1_cop"] == pytest.approx(193800000.0, rel=1e-9)
    assert fl["egi_1_cop"] == pytest.approx(184110000.0, rel=1e-9)
    assert fl["anos"][0]["administracion_cop"] == pytest.approx(30600000.0, rel=1e-9)
    assert fl["anos"][0]["gastos_cop"] == pytest.approx(23934300.0, rel=1e-9)
    assert fl["noi_1_cop"] == pytest.approx(129575700.0, rel=1e-9)


# ---------------------------------------------------------------
# VPN y TIR con flujos conocidos
# ---------------------------------------------------------------

def test_vpn_flujos_conocidos():
    """Inversion 1000, 10 flujos de 200 -> VPN @10% = 200 * a(10,10%) - 1000."""
    flujos = [-1000.0] + [200.0] * 10
    vpn = motor.vpn(flujos, 0.10)
    esperado = 200.0 * (1 - 1.1 ** -10) / 0.10 - 1000.0
    assert vpn == pytest.approx(esperado, rel=1e-9)


def test_tir_flujos_conocidos():
    """La TIR de [-1000, 200 x 10] es ~15,1% (anualidad)."""
    flujos = [-1000.0] + [200.0] * 10
    tir = motor.tir(flujos)
    assert tir is not None
    assert tir * 100.0 == pytest.approx(15.098, abs=0.05)


def test_tir_flujo_perdedor_negativa():
    """Flujo que no recupera el capital: TIR negativa (no None)."""
    flujos = [-1000.0] + [50.0] * 5
    tir = motor.tir(flujos)
    assert tir is not None
    assert tir * 100.0 < 0.0


def test_tir_sin_raiz_devuelve_none():
    """Flujo sin ingresos: VPN nunca cruza cero -> None."""
    flujos = [-1000.0] + [0.0] * 5
    assert motor.tir(flujos) is None


# ---------------------------------------------------------------
# Punto de equilibrio de ocupación
# ---------------------------------------------------------------

def test_ocupacion_breakeven_lp_vis_gfa1054():
    """GFA 1054 LP A: GPI1 = 825x32.000x12 = 316,8M; adm1 = 59,4M;
    gastos 13% -> be = 59,4 / (316,8 x 0,87) = 21,55%."""
    gpi = 825.0 * 32000.0 * 12.0
    adm = 825.0 * 6000.0 * 12.0
    be = motor.ocupacion_breakeven(gpi, adm, 0.13)
    assert be * 100.0 == pytest.approx(21.55, abs=0.05)


# ---------------------------------------------------------------
# Suelo soportable: identidad VPN = 0 al usar el CL soportable
# ---------------------------------------------------------------

def test_suelo_soportable_identidad(params_gfa1054):
    """Con CL = suelo soportable (LP A, GFA 1054), el VPN debe ser ~0."""
    p = params_gfa1054
    esc = p["escenarios"]["A_VIS"]
    esc["id"] = "A_VIS"
    estr = dict(p["estrategias"]["LP"])
    estr["_id"] = "LP"
    cl = motor.costo_lote_total(p["lote"])
    res = motor.run_combinacion(p["gfa_max_m2"], cl, esc, "LP", estr,
                                p["financiero"], p["renta"], p["reglas_renta"])
    suelo = res["suelo_soportable_cop"]
    # Recalcular con CL = suelo soportable: VPN ~ 0
    res2 = motor.run_combinacion(p["gfa_max_m2"], suelo, esc, "LP", estr,
                                 p["financiero"], p["renta"], p["reglas_renta"])
    assert abs(res2["VPN_cop"]) < 1.0e6
    assert suelo > 0


# ---------------------------------------------------------------
# Integración: lote real NO viable en renta (igual que en venta)
# ---------------------------------------------------------------

def test_lote_real_no_viable_renta(params_lote_real):
    """Con CL $1.200M y GFA 632,7 ninguna combinacion supera TIR 10%."""
    p = params_lote_real
    mejores = []
    for esc_id, esc in p["escenarios"].items():
        esc["id"] = esc_id
        for estr_id, estr in p["estrategias"].items():
            estr = dict(estr)
            estr["_id"] = estr_id
            res = motor.run_combinacion(p["gfa_max_m2"],
                                        motor.costo_lote_total(p["lote"]),
                                        esc, estr_id, estr,
                                        p["financiero"], p["renta"],
                                        p["reglas_renta"])
            mejores.append(res["TIR_pct"] or -99.0)
    assert max(mejores) < 10.0


def test_lote_real_suelo_soportable_lp_vis(params_lote_real):
    """LP A del lote real: suelo soportable ~490M (vs CL pedido 1.200M)."""
    p = params_lote_real
    esc = p["escenarios"]["A_VIS"]
    esc["id"] = "A_VIS"
    estr = dict(p["estrategias"]["LP"])
    estr["_id"] = "LP"
    res = motor.run_combinacion(p["gfa_max_m2"], motor.costo_lote_total(p["lote"]),
                                esc, "LP", estr, p["financiero"], p["renta"],
                                p["reglas_renta"])
    assert res["suelo_soportable_cop"] == pytest.approx(490.0e6, rel=0.05)
    assert res["suelo_soportable_cop"] < 1200.0e6


# ---------------------------------------------------------------
# USO-MULTIPLE (override usuario): escenario mixto con mix_usos
# ---------------------------------------------------------------

def test_area_arrendable_mix():
    """Mix: 20% local (50 m2, ef 0,85) + 80% vivienda (65 m2, ef 0,78) sobre GFA 1053.
    Local: 1053*0,2*0,85 = 179,01 -> 3 locales de 50 = 150 m2.
    Vivienda: 1053*0,8*0,78 = 657,07 -> 10 unid de 65 = 650 m2.
    Total 13 unidades, 800 m2."""
    esc = {"mix_usos": [
        {"pct_gfa": 0.20, "unidad_m2": 50.0, "eficiencia_nga": 0.85},
        {"pct_gfa": 0.80, "unidad_m2": 65.0, "eficiencia_nga": 0.78},
    ]}
    unidades, area = motor.area_arrendable(1053.0, esc)
    assert unidades == 13
    assert area == pytest.approx(800.0)


def test_run_combinacion_mix_detalle_y_canon(params_gfa1053_cl550):
    """El escenario D_MIXTO del caso A (GFA 1053, CL 550M) debe:
    - desglosar componentes (mix_usos_detalle) con canon ponderado por area
    - producir una inversion = CL + CD(mix) + CB + MKT + mobiliario
    - cumplir la identidad de suelo soportable (VPN ~ 0 con CL = suelo)"""
    p = params_gfa1053_cl550
    esc = p["escenarios"]["D_MIXTO"]
    esc["id"] = "D_MIXTO"
    estr = dict(p["estrategias"]["LP"])
    estr["_id"] = "LP"
    cl = motor.costo_lote_total(p["lote"])
    res = motor.run_combinacion(p["gfa_max_m2"], cl, esc, "LP", estr,
                                p["financiero"], p["renta"], p["reglas_renta"])
    assert res["mix_usos_detalle"] is not None
    assert len(res["mix_usos_detalle"]) == 2
    # canon efectivo = ponderado por area de los componentes
    det = res["mix_usos_detalle"]
    area_t = sum(c["area"] for c in det)
    canon_ef = sum(c["area"] * c["canon"] for c in det) / area_t
    assert res["canon_m2_mes"] == pytest.approx(canon_ef, rel=1e-6)
    # CD del mix = suma de gfa_i x costo_i
    cd_esp = sum(c["gfa_i"] * c["costo"] for c in det)
    assert res["costo_duro_cop"] == pytest.approx(cd_esp, rel=1e-6)
    # identidad de suelo soportable (solo si el suelo es positivo; si es $0,
    # el proyecto pierde valor incluso con suelo gratis y eso es lo que se verifica)
    suelo = res["suelo_soportable_cop"]
    res2 = motor.run_combinacion(p["gfa_max_m2"], suelo, esc, "LP", estr,
                                 p["financiero"], p["renta"], p["reglas_renta"])
    if suelo > 0:
        assert abs(res2["VPN_cop"]) < 1.0e6
    else:
        assert res2["VPN_cop"] <= 1.0e6


def test_mix_sensibilidad_canon_escala_componentes(params_gfa1053_cl550):
    """En sensibilidad, la variable canon de un escenario mixto escala TODOS los
    componentes (el canon efectivo varia en el mismo factor)."""
    p = params_gfa1053_cl550
    esc = p["escenarios"]["D_MIXTO"]
    esc["id"] = "D_MIXTO"
    estr = dict(p["estrategias"]["LP"])
    estr["_id"] = "LP"
    base = motor.run_combinacion(p["gfa_max_m2"], motor.costo_lote_total(p["lote"]),
                                 esc, "LP", estr, p["financiero"], p["renta"],
                                 p["reglas_renta"])
    esc_m = dict(esc)
    mix = []
    for c in esc["mix_usos"]:
        c2 = dict(c)
        c2["canon_m2_mes"] = {k: v * 0.9 for k, v in c["canon_m2_mes"].items()}
        mix.append(c2)
    esc_m["mix_usos"] = mix
    res90 = motor.run_combinacion(p["gfa_max_m2"], motor.costo_lote_total(p["lote"]),
                                  esc_m, "LP", estr, p["financiero"], p["renta"],
                                  p["reglas_renta"])
    assert res90["gpi_1_cop"] == pytest.approx(base["gpi_1_cop"] * 0.9, rel=1e-6)
