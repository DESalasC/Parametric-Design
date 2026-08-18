# -*- coding: utf-8 -*-
"""Guardian para F0_LOAD_PROYECTO_v01.py (carga de proyecto.json en el canvas).

Valida desde el fuente (sin Rhino):
  1) compatibilidad IronPython 2.7 (sin f-strings, sin shebang, sin type hints,
     sin pathlib, sin walrus),
  2) comportamiento real: carga un proyecto.json y expone las salidas esperadas,
  3) manejo de error ante ruta invalida.
"""

import json
import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src", "orquestador",
                    "F0_LOAD_PROYECTO_v01.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def test_fuente_sin_constructos_prohibidos():
    src = _fuente()
    assert not src.lstrip().startswith("#!")
    assert "pathlib" not in src
    assert ":=" not in src
    assert "f'" not in src and 'f"' not in src
    # sin type hints en funciones (IronPython 2.7)
    assert "def _val(d, k, default):" in src


def test_salidas_esperadas_presentes():
    src = _fuente()
    for salida in ("chip", "tipologia", "piso_adicional", "tipo_bonificacion",
                   "floor_height_user", "antejardin_decision",
                   "empate_posterior_pisos", "empate_posterior_m", "tratamiento",
                   "caso", "alineacion_nucleo", "usos", "modos", "escenarios",
                   "ok", "log"):
        assert salida in src


def _ejecutar(ruta_json, caso_default="A"):
    g = {"ruta_json": ruta_json, "caso_default": caso_default}
    exec(compile(_fuente(), RUTA, "exec"), g)
    return g


def test_carga_proyecto_funcional(tmp_path):
    p = tmp_path / "proyecto.json"
    p.write_text(json.dumps({
        "nombre": "proyecto-01",
        "chip": "AAA0127AZPA",
        "variables": {
            "tipologia": "Aislada",
            "piso_adicional": True,
            "tipo_bonificacion": "VIS",
            "floor_height_user": 3.2,
            "antejardin_decision": "Aumentar antejardín",
            "empate_posterior_pisos": 2,
            "empate_posterior_m": None,
            "tratamiento": "Consolidación",
            "caso": "B",
            "alineacion_nucleo": 2,
        },
        "usos": ["Vivienda", "Comercio"],
        "modos": ["venta", "renta"],
        "escenarios": ["A_VIS", "C_LUJO"],
    }, ensure_ascii=False), encoding="utf-8")

    g = _ejecutar(str(p))
    assert g["ok"] is True
    assert g["chip"] == "AAA0127AZPA"
    assert g["tipologia"] == "Aislada"
    assert g["piso_adicional"] is True
    assert g["tipo_bonificacion"] == "VIS"
    assert g["floor_height_user"] == 3.2
    assert g["empate_posterior_pisos"] == 2
    assert g["empate_posterior_m"] is None
    assert g["caso"] == "B"
    assert g["alineacion_nucleo"] == 2
    assert g["usos"] == ["Vivienda", "Comercio"]
    assert g["modos"] == ["venta", "renta"]
    assert g["escenarios"] == ["A_VIS", "C_LUJO"]


def test_carga_proyecto_ruta_invalida():
    g = _ejecutar("")
    assert g["ok"] is False
    assert "ERROR" in g["log"]
    # valores por defecto ante error
    assert g["tipologia"] == "Continua"
    assert g["caso"] == "A"
    assert g["usos"] == []
