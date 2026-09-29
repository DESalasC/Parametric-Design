# -*- coding: utf-8 -*-
"""F3_DISTRIBUCION_v02: filtro de usos (seccion 2) y multivolumen v02.1
(orientacion referida al predio, niveles automaticos Entrada->Salida y ancho
minimo por programa)."""

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
    # v02.1: orientacion referida al predio (calle de acceso confirmada en el override)
    assert "calle de acceso" in (b["orientacion"]["franja_descripcion"] or "")
    assert (b["orientacion"]["calle_acceso"] or {}).get("cardinal_label") == "Occidente-2"


def test_generar_bloques_tres_reduce_por_ancho():
    # v02.1: 3 franjas no caben con el ancho minimo del programa (B, lot 52x21 m);
    # se reduce a 2 y se avisa. Sep 4.0 -> minimo normativo 6.0.
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles,
                           {"n": 3, "separacion_m": 4.0, "desnivel_m": -3.4})
    assert b["n_solicitado"] == 3
    assert b["n"] == 2
    assert b["separacion_m"] == 6.0  # minimo normativo (Anexo 5 1.10.b) gana
    assert any("6.00" in a for a in b["avisos"])
    assert any("ancho minimo por programa" in a for a in b["avisos"])
    assert [x["z_base_m"] for x in b["bloques"]] == [0.0, -3.4]  # manual: B1 en 0.00
    assert all(x["area_lote_m2"] > 5.0 for x in b["bloques"])
    assert all(x["huella_objetivo_m2"] > 0 for x in b["bloques"])


def test_niveles_automaticos_entrada_salida():
    # v02.1: auto interpola la topografia MDT: B1 = 0.00 en la calle de acceso
    # (Entrada) y BN en el nivel final del lote (via posterior, Salida).
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles,
                           {"n": 2, "desnivel_auto": True})
    ni = b["niveles"]
    assert ni["modo"] == "auto"
    assert ni["entrada_m"] < ni["salida_m"]
    assert 10.0 < ni["delta_m"] < 16.0  # caso B: ~+13 m entre las dos calles
    zs = [x["z_base_m"] for x in b["bloques"]]
    assert zs[0] == 0.0
    assert abs(zs[-1] - ni["delta_m"]) < 0.01
    # orden: B1 debe ser la franja junto a la calle (menor cota de terreno)
    zt = [x["z_terreno_medio_m"] for x in b["bloques"]]
    assert zt[0] < zt[-1]


def test_orientacion_perpendicular():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles,
                           {"n": 2, "distribucion": "perpendicular_calle_acceso",
                            "desnivel_auto": True})
    assert "perpendiculares a la calle de acceso" in b["orientacion"]["franja_descripcion"]


def test_ancho_min_desglose():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles, {"n": 1})
    am = b["ancho_min"]
    assert am["nucleo_m"] > 0 and am["circulacion_m"] == 1.2
    assert abs(am["ancho_min_m"] - (am["nucleo_m"] + 2 * am["circulacion_m"]
                                    + am["crujia_min_m"])) < 0.01
    assert am["unidad_max_m2"] == 55.0  # vivienda estandar del mix del caso
    assert "Vivienda" in am["crujia_por_uso"]
    assert b["n_max_recomendado"] >= 1


def test_unidades_por_bloque():
    # v02.1: unidades estimadas min-max por uso, segun el GFA del bloque
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles,
                           {"n": 2, "desnivel_auto": True})
    u = b["bloques"][0]["unidades_estimadas"]
    assert set(u.keys()) == {"Local comercial", "Vivienda"}
    assert u["Vivienda"]["min"] >= 1
    assert u["Vivienda"]["max"] >= u["Vivienda"]["min"]


def test_compat_distribucion_longitudinal():
    # los modos v02 siguen aceptandose (geometria igual, etiqueta compat)
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles,
                           {"n": 2, "distribucion": "longitudinal", "desnivel_auto": True})
    assert b["n"] == 2
    assert "compat v02" in b["orientacion"]["franja_descripcion"]


def test_default_niveles_v01():
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    assert niveles == 5
    assert abs(huella - 662.515) < 0.5
