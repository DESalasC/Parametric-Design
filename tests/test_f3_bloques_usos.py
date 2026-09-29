# -*- coding: utf-8 -*-
"""F3_DISTRIBUCION_v02: filtro de usos (seccion 2) y parametros de bloques (multivolumen)."""

import os
import sys

SRC = os.path.join(os.path.dirname(__file__), "..", "src", "fase-3-masa")
sys.path.insert(0, SRC)

import F3_DISTRIBUCION_v02 as f3  # noqa: E402


def test_normalizar_usos_ui():
    # etiquetas de la seccion 2 (UI) -> usos canonicos F3
    assert f3.normalizar_uso("Comercio al por menor (mediana y gran superficie)") == "Local comercial"
    assert f3.normalizar_uso("Vivienda (unifamiliar, bifamiliar, multifamiliar, colectiva)") == "Vivienda"
    assert f3.normalizar_uso("Salud") == "Consultorios"
    assert f3.normalizar_uso("Oficinas") == "Oficinas"


def test_filtro_usos_renormaliza():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    total = prog["gfa_total"]
    prog2, aviso = f3.filtrar_usos_programa(prog, ["Vivienda"])
    assert "Vivienda" in aviso
    assert len(prog2["componentes"]) == 1
    c = prog2["componentes"][0]
    assert c["uso"] == "Vivienda"
    assert abs(c["pct_gfa"] - 1.0) < 1e-6
    assert abs(c["gfa_m2"] - total) < 1.0


def test_filtro_sin_coincidencia_devuelve_original():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    prog2, aviso = f3.filtrar_usos_programa(prog, ["Industrial"])
    assert prog2 is prog
    assert aviso.startswith("AVISO")


def test_filtro_vacio_no_cambia():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    prog2, aviso = f3.filtrar_usos_programa(prog, None)
    assert prog2 is prog and aviso == ""


def test_generar_bloques_uno():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles, {"n": 1})
    assert b["n"] == 1
    assert b["bloques"][0]["z_base_m"] == 0.0
    assert b["bloques"][0]["area_lote_m2"] > 100.0


def test_generar_bloques_tres():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles,
                           {"n": 3, "separacion_m": 4.0, "desnivel_m": -3.4})
    assert b["n"] == 3
    assert b["separacion_m"] == 6.0  # minimo normativo (Anexo 5 1.10.b) gana
    assert any("6.00" in a for a in b["avisos"])
    assert [x["z_base_m"] for x in b["bloques"]] == [0.0, -3.4, -6.8]
    assert all(x["area_lote_m2"] > 5.0 for x in b["bloques"])
    assert all(x["huella_objetivo_m2"] > 0 for x in b["bloques"])


def test_default_niveles_v01():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    assert niveles == 5
    assert abs(huella - 662.515) < 0.5
