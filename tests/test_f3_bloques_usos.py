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


def test_generar_bloques_reduce_por_ancho_doble():
    # v02.2: con doble crujia (default), 4 franjas no caben (min 13.4 m) y 3
    # tampoco en este lote (13.2 m por la esquina en diagonal) -> se ajusta a 2.
    # Sep 4.0 -> minimo normativo 6.0.
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles,
                           {"n": 4, "separacion_m": 4.0, "desnivel_m": -3.4})
    assert b["n_solicitado"] == 4
    assert b["n"] == 2
    assert b["n_max_recomendado"] == 2
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


def test_ancho_min_por_tipo_crujia():
    # v02.2: doble crujia -> max(2 x crujia + circulacion, nucleo);
    # unica -> max(crujia + circulacion, nucleo); la unica es mas permisiva.
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    bd = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles, {"n": 1, "crujia": "doble"})
    bu = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles, {"n": 1, "crujia": "unica"})
    ad, au = bd["ancho_min"], bu["ancho_min"]
    assert ad["crujia_modo"] == "doble" and ad["circulacion"] == "central"
    assert au["crujia_modo"] == "unica" and au["circulacion"] == "lateral"
    assert abs(ad["ancho_min_m"] - max(2 * ad["crujia_m"] + ad["circulacion_m"],
                                       ad["nucleo_m"])) < 0.02
    assert abs(au["ancho_min_m"] - max(au["crujia_m"] + au["circulacion_m"],
                                       au["nucleo_m"])) < 0.02
    assert au["ancho_min_m"] < ad["ancho_min_m"]
    assert au["unidad_max_m2"] == 55.0  # vivienda estandar del mix del caso
    assert "Vivienda" in au["crujia_por_uso"]


def test_crujia_unica_permite_mas_bloques():
    # v02.2: la crujia unica (circ. lateral) baja el ancho minimo a ~7.3 m y
    # habilita mas bloques en el mismo lote (max 4 vs 2 con doble crujia).
    prog = f3.leer_programa_chip("AAA0030JKOE")
    huella, niveles, _ = f3.distribuir_niveles(prog)
    b = f3.generar_bloques("AAA0030JKOE", prog, huella, niveles,
                           {"n": 5, "crujia": "unica"})
    assert b["n"] == 4
    assert b["n_max_recomendado"] == 4
    assert b["crujia"]["modo"] == "unica"
    assert b["nucleo_posicion"] in ("centro", "extremo")
    assert any("crujia" in a for a in b["avisos"])
    assert all(x["ancho_m"] >= b["ancho_min"]["ancho_min_m"] - 0.06 for x in b["bloques"])


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
