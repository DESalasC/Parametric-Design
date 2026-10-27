# -*- coding: utf-8 -*-
"""Tests de las cotas MDT (z_base_m) del contexto 50 m.

Regla del proyecto (2026-10-25/26): cada morph del Contexto50 apoya en el punto
MAS BAJO de su huella (no en el centroide) y esa cota debe sobrevivir a cada
regeneracion del JSON. El fallo del 2026-10-26 dejo los 71 morphs a la misma
altura (+14.488 m) porque el fetch reescribio el JSON sin `z_base_m`.
"""

import importlib.util
import io
import json
import os
import subprocess
import sys

import pytest

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FETCH = os.path.join(RAIZ, "src", "fase-1-contexto", "F1_CONTEXTO50_FETCH_v01.py")
DIAG = os.path.join(RAIZ, "scripts", "utilities", "diagnosticar-cotas-contexto.py")


def _cargar_fetch():
    spec = importlib.util.spec_from_file_location("f1_contexto50_fetch", FETCH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _escribir(ruta, datos):
    with io.open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False)


def test_hereda_cotas_por_id(tmp_path):
    fetch = _cargar_fetch()
    previo = os.path.join(str(tmp_path), "AAA-contexto50.json")
    _escribir(previo, {"metadata": {"z_base_fuente": {"metodo": "min de centroide+extremos"}},
                       "edificios": [
                           {"id": "A", "z_base_m": -3.2, "z_base_centroide_m": -2.9,
                            "z_base_min_m": -3.2, "z_base_max_m": -2.4,
                            "z_base_n_puntos": 5, "z_base_metodo": "min de centroide+extremos"},
                           {"id": "B", "z_base_m": 1.7},
                       ]})
    nuevos = [{"id": "A", "altura_m": 6.0}, {"id": "B", "altura_m": 3.0},
              {"id": "C", "altura_m": 3.0}]
    n, meta = fetch.heredar_cotas_zbase(nuevos, previo)

    assert n == 2
    assert nuevos[0]["z_base_m"] == -3.2
    assert nuevos[0]["z_base_min_m"] == -3.2
    assert nuevos[0]["z_base_metodo"] == "min de centroide+extremos"
    assert nuevos[1]["z_base_m"] == 1.7
    assert "z_base_m" not in nuevos[2]          # sin cota previa -> el builder avisa
    assert meta.get("z_base_fuente", {}).get("metodo", "").startswith("min")


def test_sin_json_previo_no_falla(tmp_path):
    fetch = _cargar_fetch()
    nuevos = [{"id": "A", "altura_m": 6.0}]
    n, meta = fetch.heredar_cotas_zbase(nuevos, os.path.join(str(tmp_path), "no-existe.json"))
    assert n == 0
    assert meta == {}
    assert "z_base_m" not in nuevos[0]


def test_json_previo_corrupto_no_falla(tmp_path):
    fetch = _cargar_fetch()
    previo = os.path.join(str(tmp_path), "roto.json")
    with io.open(previo, "w", encoding="utf-8") as f:
        f.write("{no es json")
    n, meta = fetch.heredar_cotas_zbase([{"id": "A"}], previo)
    assert n == 0
    assert meta == {}


def test_id_repetido_se_empareja_por_huella(tmp_path):
    """El id catastral no es unico: dos construcciones del mismo predio deben
    conservar SU cota (no la de la otra)."""
    fetch = _cargar_fetch()
    previo = os.path.join(str(tmp_path), "AAA-contexto50.json")
    _escribir(previo, {"edificios": [
        {"id": "MISMO", "z_base_m": -18.27,
         "vertices": [[-90.0, 25.0], [-95.0, 19.0], [-99.0, 22.0], [-90.0, 25.0]]},
        {"id": "MISMO", "z_base_m": -18.71,
         "vertices": [[-86.0, 36.0], [-84.0, 34.0], [-88.0, 37.0], [-86.0, 36.0]]},
    ]})
    # mismo conjunto, en otro orden y con ruido de 1 cm en los vertices
    nuevos = [
        {"id": "MISMO", "vertices": [[-85.99, 36.01], [-84.01, 33.99], [-87.99, 37.01]]},
        {"id": "MISMO", "vertices": [[-90.01, 24.99], [-94.99, 19.01], [-98.99, 22.01]]},
    ]
    n, _ = fetch.heredar_cotas_zbase(nuevos, previo)
    assert n == 2
    assert nuevos[0]["z_base_m"] == -18.71
    assert nuevos[1]["z_base_m"] == -18.27


def test_huella_movida_no_hereda_cota(tmp_path):
    """Si la huella cambio de sitio (> TOL_HUELLA_M) no se hereda una cota ajena."""
    fetch = _cargar_fetch()
    previo = os.path.join(str(tmp_path), "AAA-contexto50.json")
    _escribir(previo, {"edificios": [
        {"id": "X", "z_base_m": -5.0, "vertices": [[0, 0], [10, 0], [10, 10]]}]})
    nuevos = [{"id": "X", "vertices": [[50, 50], [60, 50], [60, 60]]}]
    n, _ = fetch.heredar_cotas_zbase(nuevos, previo)
    assert n == 0
    assert "z_base_m" not in nuevos[0]


def test_registros_sin_cota_no_se_heredan(tmp_path):
    """z_base_m = null en el JSON previo no debe propagarse como None."""
    fetch = _cargar_fetch()
    previo = os.path.join(str(tmp_path), "AAA-contexto50.json")
    _escribir(previo, {"edificios": [{"id": "A", "z_base_m": None},
                                     {"id": "B", "z_base_m": 0.0}]})
    nuevos = [{"id": "A"}, {"id": "B"}]
    n, _ = fetch.heredar_cotas_zbase(nuevos, previo)
    assert n == 1
    assert "z_base_m" not in nuevos[0]
    assert nuevos[1]["z_base_m"] == 0.0         # 0.0 es una cota valida (nivel del ancla)


def _minimo_c50(chip, edificios):
    return {"metadata": {"chip": chip, "radio_m": 50.0,
                         "origen_sirgas": {"x": 0.0, "y": 0.0, "z": 0.0},
                         "ancla_canvas_local": {"x": 0.0, "y": 0.0, "z": 0.0}},
            "topografia": {"malla_terreno": [
                {"x_local": 0.0, "y_local": 0.0, "z_local": 0.5},
                {"x_local": 10.0, "y_local": 10.0, "z_local": 1.5}]},
            "lote_objetivo": {"vertices_3d_local": [[0.0, 0.0, 0.0], [10.0, 0.0, 0.0],
                                                      [10.0, 10.0, 0.0]]},
            "vias_oficiales": [], "espacios_publicos": [], "vecinos": []}


def test_diagnostico_falla_si_ningun_vecino_tiene_cota(tmp_path):
    """El diagnostico debe salir con codigo 1 si el contexto50 quedo sin z_base_m."""
    d = str(tmp_path)
    _escribir(os.path.join(d, "AAA0030JKOE-contexto.json"), _minimo_c50("AAA0030JKOE", []))
    _escribir(os.path.join(d, "AAA0030JKOE-contexto50.json"),
              {"metadata": {"chip": "AAA0030JKOE",
                            "origen_sirgas": {"z": 0.0},
                            "ancla_canvas_local": {"x": 0.0, "y": 0.0, "z": 0.0}},
               "edificios": [{"id": "A", "vertices": [[0, 0], [10, 0], [10, 10]]},
                             {"id": "B", "vertices": [[20, 0], [30, 0], [30, 10]]}]})
    p = subprocess.run([sys.executable, DIAG, "--chip", "AAA0030JKOE", "--data", d],
                       capture_output=True, text=True)
    assert p.returncode == 1
    assert "sin z_base_m" in (p.stdout + p.stderr)


def test_diagnostico_falla_si_todas_las_cotas_son_iguales(tmp_path):
    """Bases identicas = morphs a la misma altura: debe fallar aunque haya cotas."""
    d = str(tmp_path)
    _escribir(os.path.join(d, "AAA0030JKOE-contexto.json"), _minimo_c50("AAA0030JKOE", []))
    _escribir(os.path.join(d, "AAA0030JKOE-contexto50.json"),
              {"metadata": {"chip": "AAA0030JKOE",
                            "z_base_fuente": {"metodo": "min de centroide+extremos (huella)"},
                            "origen_sirgas": {"z": 0.0},
                            "ancla_canvas_local": {"x": 0.0, "y": 0.0, "z": 0.0}},
               "edificios": [{"id": "A", "vertices": [[0, 0], [10, 0], [10, 10]],
                              "z_base_m": 14.488},
                             {"id": "B", "vertices": [[20, 0], [30, 0], [30, 10]],
                              "z_base_m": 14.488}]})
    p = subprocess.run([sys.executable, DIAG, "--chip", "AAA0030JKOE", "--data", d],
                       capture_output=True, text=True)
    assert p.returncode == 1
    assert "misma altura" in (p.stdout + p.stderr)


def test_diagnostico_ok_con_cotas_distintas(tmp_path):
    d = str(tmp_path)
    _escribir(os.path.join(d, "AAA0030JKOE-contexto.json"), _minimo_c50("AAA0030JKOE", []))
    _escribir(os.path.join(d, "AAA0030JKOE-contexto50.json"),
              {"metadata": {"chip": "AAA0030JKOE",
                            "z_base_fuente": {"metodo": "min de centroide+extremos (huella)"},
                            "origen_sirgas": {"z": 0.0},
                            "ancla_canvas_local": {"x": 0.0, "y": 0.0, "z": 0.0}},
               "edificios": [{"id": "A", "vertices": [[0, 0], [10, 0], [10, 10]],
                              "z_base_m": -6.6},
                             {"id": "B", "vertices": [[20, 0], [30, 0], [30, 10]],
                              "z_base_m": 2.1}]})
    p = subprocess.run([sys.executable, DIAG, "--chip", "AAA0030JKOE", "--data", d],
                       capture_output=True, text=True)
    assert p.returncode == 0, p.stdout + p.stderr
    assert "edificios con cota   = 2/2" in p.stdout
