# -*- coding: utf-8 -*-
"""v03.1 (2026-09-28): el motor F2 ignora escenarios vacios (placeholders) en
lugar de fallar con KeyError 'eficiencia_nga'.

Caso real: el front-end del orquestador guardo el financiero del chip AAA0030JKOE
con D_MIXTO / D_MIXTO_SALUD / D_MIXTO_OFICINAS = {} y el pipeline F2 fallo.

Ejecutar:  pytest tests/test_f2_escenarios_vacios.py -v
"""
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
FIN_DIR = PROJECT_ROOT / "src" / "fase-2-demanda" / "F2_Modelo_Financiero"
sys.path.insert(0, str(FIN_DIR))

import pytest

import F2_DEMANDA_MOTOR_v03 as motor


def _params_con_vacios():
    with open(FIN_DIR / "parametros_AAA0127AZPA_venta_gfa1053_cl550.json", "r", encoding="utf-8") as f:
        params = json.load(f)
    params["escenarios"]["D_MIXTO"] = {}
    params["escenarios"]["D_MIXTO_SALUD"] = {"precio_venta_m2": None, "costo_construccion_m2": None}
    return params


def test_filtro_escenarios_vacios():
    """La funcion de filtro conserva utiles (simples y mix) y lista los vacios."""
    utiles, ignorados = motor._escenarios_utilizables({
        "A_VIS": {"eficiencia_nga": 0.8},
        "D_MIXTO": {},
        "D_MIXTO_SALUD": {"precio_venta_m2": None},
        "MIX_OK": {"mix_usos": [{"pct_gfa": 1.0}]},
    })
    assert set(utiles.keys()) == {"A_VIS", "MIX_OK"}
    assert ignorados == ["D_MIXTO", "D_MIXTO_SALUD"]


def test_main_ignora_vacios(tmp_path, monkeypatch, capsys):
    """main() corre A/B/C, ignora los vacios y los registra en resultados_completos.json."""
    params = _params_con_vacios()
    ruta_params = tmp_path / "params_prueba.json"
    ruta_params.write_text(json.dumps(params), encoding="utf-8")
    out_dir = tmp_path / "out"

    monkeypatch.setattr(sys, "argv", [
        "F2_DEMANDA_MOTOR_v03.py",
        "--parametros", str(ruta_params),
        "--chip", "TESTCHIP",
        "--gfa", "1053",
        "--pago-parcial", "30",
        "--sin-informe",
        "--outdir", str(out_dir),
    ])
    rc = motor.main()
    assert rc == 0
    salida = capsys.readouterr().out
    assert "Escenarios sin datos ignorados" in salida
    datos = json.loads((out_dir / "resultados_completos.json").read_text(encoding="utf-8"))
    assert set(datos["escenarios_ignorados"]) == {"D_MIXTO", "D_MIXTO_SALUD"}
    ids = [e["escenario_id"] for e in datos["escenarios"]]
    assert "D_MIXTO" not in ids
    assert "A_VIS" in ids
