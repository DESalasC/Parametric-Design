# -*- coding: utf-8 -*-
"""Guardian para el puente frente_override (orquestador -> canvas, 2026-08-23).

Valida:
  - NORMATIVA_v08.2: parseo de frente_override_json {cardinal: frente}, y la
    derivacion de cardinal por normal saliente (misma convencion que
    vecinos_por_lado.py: azimut = atan2(nx,ny) % 360).
  - F0_LOAD_PROYECTO_v01.4: emite frente_override_json desde
    proyecto.json.vecinos_por_lado (via/predio/espacio_publico; ignora
    indefinido/libre).
"""

import ast
import json
import math
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "src", "fase-1-contexto")
RUTA_NORM = os.path.join(BASE, "F1_ETAPA2_NORMATIVA_v08.py")
RUTA_F0 = os.path.join(os.path.dirname(__file__), "..", "src", "orquestador",
                       "F0_LOAD_PROYECTO_v01.py")


def _fuente(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def _extraer(ruta, nombre):
    src = _fuente(ruta)
    tree = ast.parse(src)
    ns = {"json": json, "math": math}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if getattr(t, "id", "").isupper():
                    try:
                        ns[t.id] = ast.literal_eval(node.value)
                    except Exception:
                        pass
    # cargar TODAS las funciones puras (deps cruzadas, p.ej. _cardinal_lado ->
    # _cardinal_normal) antes de devolver la pedida
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            try:
                exec(ast.get_source_segment(src, node), ns)
            except Exception:
                pass
    if nombre in ns:
        return ns[nombre]
    raise AssertionError("funcion %s no encontrada" % nombre)


def test_parsear_frente_override_valido():
    f = _extraer(RUTA_NORM, "_parsear_frente_override")
    r = f(json.dumps({"Norte": "predio", "Sur": "via", "Oriente": "via",
                      "Occidente": "predio"}))
    assert r == {"Norte": "predio", "Sur": "via", "Oriente": "via",
                 "Occidente": "predio"}


def test_parsear_frente_override_ignora_libre_indefinido():
    f = _extraer(RUTA_NORM, "_parsear_frente_override")
    r = f(json.dumps({"Norte": "libre", "Sur": "indefinido", "Oriente": "via"}))
    assert r == {"Oriente": "via"}


def test_cardinal_normal():
    f = _extraer(RUTA_NORM, "_cardinal_normal")
    assert f(0.0, 1.0) == "Norte"
    assert f(1.0, 0.0) == "Oriente"
    assert f(0.0, -1.0) == "Sur"
    assert f(-1.0, 0.0) == "Occidente"


def test_cardinal_lado_por_normal_saliente():
    f = _extraer(RUTA_NORM, "_cardinal_lado")
    # lote centrado en (0,0); cada lado con su normal saliente esperada
    assert f(10, 0, 0, 5, 0, 0) == "Norte"      # borde norte, normal (0,+1)
    assert f(-10, 0, 0, -5, 0, 0) == "Sur"      # borde sur, normal (0,-1)
    assert f(0, 10, 5, 0, 0, 0) == "Oriente"    # borde este, normal (+1,0)
    assert f(0, -10, -5, 0, 0, 0) == "Occidente"  # borde oeste, normal (-1,0)


def test_normativa_fuente_tiene_puente():
    s = _fuente(RUTA_NORM)
    assert "frente_override_json" in s
    assert "FRENTE_A_CLASIFICACION" in s
    assert "_cardinal_lado" in s
    assert "if _card in frente_override:" in s


def test_f0_emite_frente_override_json(tmp_path):
    src = _fuente(RUTA_F0)
    p = tmp_path / "proyecto.json"
    p.write_text(json.dumps({
        "chip": "AAA0240ZXJH",
        "variables": {},
        "vecinos_por_lado": {
            "lados": [
                {"cardinal": "Norte", "frente": "predio", "frente_override": None},
                {"cardinal": "Sur", "frente": "via", "frente_override": None},
                {"cardinal": "Oriente", "frente": "via", "frente_override": None},
                {"cardinal": "Occidente", "frente": "predio", "frente_override": None},
                {"cardinal": "Norte", "frente": "libre", "frente_override": None},
            ]
        }
    }, ensure_ascii=False), encoding="utf-8")
    g = {"ruta_json": str(p), "caso_default": "A"}
    exec(compile(src, RUTA_F0, "exec"), g)
    fo = json.loads(g["frente_override_json"])
    assert fo == {"Norte": "predio", "Sur": "via", "Oriente": "via",
                  "Occidente": "predio"}
