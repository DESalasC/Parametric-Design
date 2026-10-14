# -*- coding: utf-8 -*-
"""F3_StorySync_v02: guardian de regresion + plan (CLI y funcion).

  - --plan NO debe importar `archicad` (import perezoso): corre en cualquier PC.
  - La funcion plan_stories replica el algoritmo del canvas (grilla base+j*h,
    snap, GF/L01.., RF opcional).
  - CLI: --plan --cotas ... escribe niveles_deseados.json valido.
"""
import importlib.util
import io
import json
import os
import subprocess
import sys

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(TESTS_DIR, ".."))
SS = os.path.join(BASE, "src", "interfases-archicad", "F3_StorySync_v02.py")


def _modulo():
    spec = importlib.util.spec_from_file_location("f3_storysync_v02_t", SS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_fuente_import_perezoso():
    txt = io.open(SS, "r", encoding="utf-8").read()
    assert "from archicad import" not in txt.split("def _cmd_list")[0]
    assert "def plan_stories" in txt
    assert "--plan" in txt and "--check" in txt


def test_plan_stories_valores():
    ss = _modulo()
    bloques = [
        {"id": "B1-R1", "cota_arranque_m": 0.20, "pisos": 5},
        {"id": "B2-R1", "cota_arranque_m": 3.35, "pisos": 5},
        {"id": "B3-R1", "cota_arranque_m": 6.85, "pisos": 5},
        {"id": "B4-R1", "cota_arranque_m": 10.15, "pisos": 5},
    ]
    plan = ss.plan_stories(bloques, 3.05)
    assert plan["base_z_m"] == 0.2
    assert len(plan["stories"]) == 8
    assert plan["stories"][0]["name"] == "GF"
    assert plan["stories"][-1]["name"] == "L07"
    assert abs(plan["stories"][1]["elevation"] - 3.25) < 1e-9
    assert plan["bloques"][2]["offset_niveles"] == 2
    assert abs(plan["bloques"][3]["ajuste_m"] - (-0.80)) < 1e-9
    plan_t = ss.plan_stories(bloques, 3.05, con_tapa=True)
    assert plan_t["stories"][-1]["name"] == "RF"


def test_cli_plan_escribe_json(tmp_path):
    out = os.path.join(str(tmp_path), "niveles_deseados.json")
    r = subprocess.run(
        [sys.executable, SS, "--plan", "--cotas", "1.0,2.0",
         "--pisos", "3", "--floor-h", "3.0", "--out", out],
        cwd=BASE, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    datos = json.loads(io.open(out, "r", encoding="utf-8").read())
    # cotas 1.0 y 2.0 -> snap: offsets 0 y 0 (2.0-1.0 < 1.5) -> 3 niveles
    assert datos["base_z_m"] == 1.0
    assert [s["name"] for s in datos["stories"]] == ["GF", "L01", "L02"]
    assert datos["stories"][2]["elevation"] == 7.0


def test_cli_plan_hoja_operador(tmp_path):
    """v02.1: --plan --hoja genera la hoja del operador (tabla + pasos)."""
    out = os.path.join(str(tmp_path), "niveles_deseados.json")
    r = subprocess.run(
        [sys.executable, SS, "--plan", "--cotas", "0.2,3.35", "--pisos", "5",
         "--floor-h", "3.05", "--out", out, "--hoja"],
        cwd=BASE, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    hoja = os.path.join(str(tmp_path), "niveles_operador.txt")
    assert os.path.isfile(hoja)
    txt = io.open(hoja, "r", encoding="utf-8").read()
    assert "GF" in txt and "L05" in txt
    assert "Configuracion de pisos" in txt
    assert "F3_StorySync_v02.py --check" in txt
    assert "NIVELES PARA ARCHICAD" in txt
