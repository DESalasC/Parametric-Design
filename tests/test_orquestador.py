# -*- coding: utf-8 -*-
"""Guardian de regresion para src/orquestador/run_pipeline_v01.py.

Valida (sin ejecutar el pipeline pesado):
  1) mapa caso -> chip coherente con F3_DISTRIBUCION_v01,
  2) detectar_estado devuelve los 7 pasos con la estructura esperada,
  3) _comando_f2 construye el comando correcto (venta/renta + overrides),
  4) _generar_html produce un checklist HTML con los marcadores clave.
"""

import os
import sys

SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "orquestador")
sys.path.insert(0, SRC_DIR)

import run_pipeline_v01 as rp  # noqa: E402


def test_mapa_caso_chip():
    assert rp.CASO_CHIP["A"] == "AAA0127AZPA"
    assert rp.CASO_CHIP["B"] == "AAA0030JKOE"
    assert rp.CASO_CHIP["B_SALUD"] == "AAA0030JKOE"
    assert rp.CASO_CHIP["C"] == "AAA0039KRMR"
    assert set(rp.CASOS) == {"A", "B", "B_SALUD", "C"}


def test_detectar_estado_estructura():
    estado = rp.detectar_estado("AAA0127AZPA", "A")
    esperados = {"f1_contexto", "f1_gfa", "f2_venta", "f2_renta",
                 "f3_distribucion", "f3_accesos", "f3_masa_rhino"}
    assert set(estado.keys()) == esperados
    for paso in estado.values():
        assert "estado" in paso
        assert paso["estado"] in ("hecho", "falta", "manual")
        assert "artefacto" in paso
    # los pasos manuales no tienen comando CLI
    assert estado["f1_gfa"]["tipo"] == "manual"
    assert estado["f3_masa_rhino"]["tipo"] == "manual"
    # los automáticos sí
    assert estado["f1_contexto"]["tipo"] == "auto"
    assert "--chip" in estado["f1_contexto"]["comando"]


def test_comando_f2_venta():
    params = {"chip": "AAA0127AZPA", "gfa_m2": None, "costo_lote_cop": None}
    cmd, cwd = rp._comando_f2("venta", params)
    assert "F2_DEMANDA_MOTOR_v03.py" in " ".join(cmd)
    assert "--chip" in cmd
    assert "AAA0127AZPA" in cmd
    assert cwd == rp.F2_VENTA_DIR
    # sin overrides no debe llevar --gfa ni --costo-lote
    assert "--gfa" not in cmd
    assert "--costo-lote" not in cmd


def test_comando_f2_renta_con_overrides():
    params = {"chip": "AAA0127AZPA", "gfa_m2": 1461.1, "costo_lote_cop": 800000000}
    cmd, cwd = rp._comando_f2("renta", params)
    assert "F2_RENTA_MOTOR_v03.py" in " ".join(cmd)
    assert cwd == rp.F2_RENTA_DIR
    assert "--gfa" in cmd and "1461.1" in cmd
    assert "--costo-lote" in cmd and "800000000" in cmd


def test_generar_html_marcadores():
    estado = rp.detectar_estado("AAA0127AZPA", "A")
    html = rp._generar_html(estado, "AAA0127AZPA", "A", "mixto")
    assert "<!DOCTYPE html>" in html
    assert "Orquestador DiseñoParametrico" in html
    assert "Fase 1" in html and "Fase 2" in html and "Fase 3" in html
    assert "Parte 2" in html
    assert "Round-trip del operador" in html
    assert "GetElements" in html
    assert "Ladybug" in html
    assert "AAA0127AZPA" in html
    # badges de estado presentes
    assert "badge" in html
