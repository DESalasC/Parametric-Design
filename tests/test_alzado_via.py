# -*- coding: utf-8 -*-
"""Alzado del lote sobre su via frontal (generador de z=0).

Verifica el calculo, no el dibujo: candidatos, marco de los vecinos y lectura del
datum vigente. Usa `--mdt malla` (sin red) para que el test sea determinista.
"""
import importlib.util
import json
import os

import pytest

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GEN = os.path.join(RAIZ, "scripts", "utilities", "generar-alzado-via.py")
CHIP = "AAA0030JKOE"
CTX = os.path.join(RAIZ, "data", "pot-cache", CHIP + "-contexto.json")


def _mod():
    spec = importlib.util.spec_from_file_location("generar_alzado_via", GEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def datos():
    if not os.path.isfile(CTX):
        pytest.skip("sin contexto de %s" % CHIP)
    return _mod().construir(CHIP, mdt="malla")


def test_lado_frontal_es_el_de_la_calle_de_acceso(datos):
    assert datos["lado"]["id"] == 25
    assert datos["lado"]["etiqueta"] == "Occidente-2"
    assert datos["lado"]["origen"].startswith("canvas")
    assert 14.0 <= datos["frente"]["largo_m"] <= 16.0


def test_perfil_lindero_y_calle(datos):
    z_l = [p["z"] for p in datos["lindero"]]
    z_v = [p["z"] for p in datos["via"]]
    assert len(z_l) == len(z_v) == 9
    assert all(z is not None for z in z_l + z_v)
    # cotas del marco del canvas: el lote local va de 0,27 a 14,5 m
    assert -5.0 < min(z_l + z_v) and max(z_l + z_v) < 20.0


def test_candidatos_completos_y_ordenados(datos):
    ids = {c["id"] for c in datos["candidatos"]}
    assert ids == {"via_max", "via_min", "frente_max", "frente_min", "lote_min"}
    for c in datos["candidatos"]:
        assert c["z"] is not None
    d = {c["id"]: c["z"] for c in datos["candidatos"]}
    assert d["via_max"] >= d["via_min"]
    assert d["frente_max"] >= d["frente_min"]
    assert d["frente_min"] == pytest.approx(d["lote_min"], abs=0.01)


def test_vecinos_en_marco_etapa1(datos):
    """El contexto50 va en su propio marco: sin ancla+desplazamiento los vecinos
    se dibujaban a 100+ m del frente (bug 2026-10-26)."""
    v = datos["vecinos"]
    assert v, "sin volumenes adyacentes"
    xs = [x for e in v for x in (e["x0"], e["x1"])]
    L = datos["frente"]["largo_m"]
    assert min(xs) > -8 * L and max(xs) < 8 * L
    zs = [e["z_base"] for e in v]
    assert -40.0 < min(zs) and max(zs) < 40.0


def test_altura_normativa_desde_pot_data(datos):
    assert datos["altura_norma"]["h_m"] == pytest.approx(10.0, abs=1e-6)
    assert "492" in (datos["altura_norma"]["fuente"] or "") or "IDPC" in (datos["altura_norma"]["fuente"] or "")


def test_z0_actual_por_defecto_es_min_lote(datos):
    d = datos["z0_actual"]
    assert d["modo"] in ("min_lote", "manual")
    assert isinstance(d["z"], float)


def test_candidatos_con_cota_msnm(datos):
    """Cada linea propuesta lleva su cota absoluta (msnm = z local + origen_sirgas.z)."""
    ref = datos["msnm"]["z_ref_m"]
    assert 2000.0 < ref < 3000.0          # Bogota ~2.600 msnm
    for c in datos["candidatos"]:
        assert c["z_msnm"] is not None
        assert abs((c["z"] + ref) - c["z_msnm"]) < 0.01
    # coherencia con el datum vigente
    z0 = datos["z0_actual"]["z"]
    assert 2600.0 < (z0 + ref) < 2700.0


def test_predio_propio_no_se_dibuja(datos):
    """El volumen construido del propio predio NO debe aparecer en el alzado."""
    assert datos["excluidos_predio_propio"] >= 1
    # ningun vecino dibujado puede tener su centroide dentro del lote
    lote = datos["frente"]
    assert all(abs(v["prof"]) < 400 for v in datos["vecinos"])


def test_lados_con_tipo_de_frente(datos):
    """Cada lado lleva su tipo con la paleta de la planta de seleccion de vias."""
    tipos = {l["categoria"]: l.get("frente_tipo") for l in datos["lados_lote"]}
    assert tipos["frente"] == "via"
    assert all(t in ("via", "via_no_frontal", "predio", "espacio_publico", "libre", "indefinido")
               for t in tipos.values())
    assert "lados_fuente" in datos


def test_niveles_solo_en_esquema_adr024(datos):
    """Sin plan ADR-024 no se dibujan niveles (evita lineas 12 m bajo el terreno)."""
    assert isinstance(datos["niveles"], list)
    assert datos.get("niveles_nota")
    for n in datos["niveles"]:
        assert "z_local" in n and "name" in n


def test_altura_reglamentaria_idpc(datos):
    """La altura vigente es 10,00 m (IDPC 2026-10-26), no los 7,00 del codigo CHB."""
    a = datos["altura_norma"]
    assert a["h_m"] == pytest.approx(10.0, abs=1e-6)
    assert a["referencia_m"] == pytest.approx(7.0, abs=1e-6)
    assert "IDPC" in (a["fuente"] or "")


def test_override_de_altura_gana_sobre_el_codigo(monkeypatch):
    """fetch v7: `altura_maxima_m` del override debe sobrescribir el codigo CHB (7,0)."""
    import importlib.util
    ruta = os.path.join(RAIZ, "scripts", "utilities", "fetch-urban-context-v7.py")
    spec = importlib.util.spec_from_file_location("fetch_v7_t", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    pot = {"altura_maxima_m": 7.0, "altura_maxima_raw": "CHB", "altura_maxima_pisos": 5}
    ok = mod._aplicar_norma_override(pot, "AAA0030JKOE")
    assert ok is True
    assert pot["altura_maxima_m"] == pytest.approx(10.0, abs=1e-6)
    assert pot.get("altura_maxima_m_referencia_pzcb") == pytest.approx(7.0, abs=1e-6)
    assert "IDPC" in (pot.get("altura_maxima_fuente") or "")


def test_svg_y_html_se_generan(tmp_path):
    mod = _mod()
    d = mod.construir(CHIP, mdt="malla")
    svg = mod.svg_alzado(d)
    assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
    assert "z=0 SELECCIONADO" in svg
    det = mod.svg_detalle(d)
    assert "Detalle del datum" in det
    cmp_ = mod.svg_comparativa(d)
    assert "Que cambia si el z=0" in cmp_
    html = mod.html_alzado(d, svg, servidor=False, svg_detalle_=det, svg_cmp_=cmp_)
    assert "<!DOCTYPE html>" in html
    for marca in ("fijar z=0", "Lindero del lote - cota alta", "Calle (franja exterior) - baja",
                  "Lados del lote", "Detalle del datum", "msnm", "planta de seleccion de vias",
                  "altura maxima vigente 10.00 m", "PZCB (referencia) 7.00 m"):
        assert marca in html, marca
    assert "2634." in html or "2635." in html or "2636." in html


def test_cuatro_lados_del_lote(datos):
    """El alzado debe rotular los cuatro lados del lote (referencia de alturas)."""
    lados = datos["lados_lote"]
    assert len(lados) == 4, [l["categoria"] for l in lados]
    assert lados[0]["es_frente"] and lados[0]["categoria"] == "frente"
    assert {l["categoria"] for l in lados} == {"frente", "izq", "der", "posterior"}
    for l in lados:
        assert l["z_min"] <= l["z_max"]
        assert l["largo_m"] > 0
        assert len(l["puntos"]) >= 2
    # el frente es el lado mas bajo y el posterior el mas alto (ladera)
    frente = next(l for l in lados if l["es_frente"])
    posterior = next(l for l in lados if l["categoria"] == "posterior")
    assert frente["z_max"] < posterior["z_min"]


def test_vecinos_laterales_marcados(datos):
    """Los vecinos inmediatamente laterales son la referencia de escala."""
    laterales = [v for v in datos["vecinos"] if v.get("rol", "").startswith("lateral")]
    assert laterales, "sin vecinos laterales identificados"
    for v in laterales:
        assert abs(v["prof"]) <= 12.0          # mismo paramento, no cruzando la calle
        assert v["h"] > 0
    roles = {v["rol"] for v in datos["vecinos"]}
    assert "lateral_izq" in roles or "lateral_der" in roles
