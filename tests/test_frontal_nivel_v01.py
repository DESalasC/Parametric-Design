# -*- coding: utf-8 -*-
"""Vista FRONTAL del lote desde la calle y nivel 0,00 (seccion 1d).

Verifica el payload que alimenta el orquestador: lado frontal, perfil y calle,
curvas de nivel en MSNM, perimetro con los colores de la planta, esquinas,
vecinos inmediatos, puntos marcados (max. 5) y banda de altura sobre el terreno.

Sin red: `mdt="malla"` y cache de puntos/z0 redirigida a tmp_path.
"""
import importlib.util
import json
import os

import pytest

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GEN = os.path.join(RAIZ, "scripts", "utilities", "F1_FRONTAL_NIVEL_v01.py")
CHIP = "AAA0030JKOE"
CTX = os.path.join(RAIZ, "data", "pot-cache", CHIP + "-contexto.json")
C50 = os.path.join(RAIZ, "data", "pot-cache", CHIP + "-contexto50.json")


def _mod():
    spec = importlib.util.spec_from_file_location("f1_frontal_nivel", GEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def mod():
    if not os.path.isfile(CTX) or not os.path.isfile(C50):
        pytest.skip("sin contexto/contexto50 de %s" % CHIP)
    return _mod()


@pytest.fixture
def aislado(mod, tmp_path, monkeypatch):
    """Puntos, z0 y cache MDT fuera de data/ (no toca el estado del operador)."""
    monkeypatch.setattr(mod, "ruta_puntos", lambda chip: str(tmp_path / "frontal.json"))
    monkeypatch.setattr(mod, "ruta_mdt_frontal", lambda chip: str(tmp_path / "frontal-mdt.json"))
    z0 = tmp_path / "z0.json"
    z0.write_text(json.dumps({"chip": CHIP, "modo": "min_lote", "z0_m": 0.2661,
                              "origen": "test"}), encoding="utf-8")
    monkeypatch.setattr(mod, "ruta_z0", lambda chip: str(z0))
    return mod


@pytest.fixture(scope="module")
def datos(mod, tmp_path_factory):
    """Payload estable: z0/puntos/cache en tmp (no depende del estado del operador)."""
    tmp = tmp_path_factory.mktemp("frontal_datos")
    z0 = tmp / "z0.json"
    z0.write_text(json.dumps({"chip": CHIP, "modo": "min_lote", "z0_m": 0.2661,
                              "origen": "test"}), encoding="utf-8")
    rz, rp, rm = mod.ruta_z0, mod.ruta_puntos, mod.ruta_mdt_frontal
    mod.ruta_z0 = lambda chip: str(z0)
    mod.ruta_puntos = lambda chip: str(tmp / "frontal.json")
    mod.ruta_mdt_frontal = lambda chip: str(tmp / "frontal-mdt.json")
    try:
        yield mod.construir(CHIP, mdt="malla")
    finally:
        mod.ruta_z0, mod.ruta_puntos, mod.ruta_mdt_frontal = rz, rp, rm


def test_lado_frontal_es_la_calle_de_acceso(datos):
    fr = datos["frente"]
    assert fr["lado_id"] == 25
    assert fr["etiqueta"] == "Occidente-2"
    assert fr["frente_tipo"] == "via"
    assert fr["color"] == "#2563eb"
    assert 14.0 <= fr["largo_m"] <= 16.0
    assert "acceso" in fr["origen"] or "operador" in fr["origen"]


def test_perfil_calle_y_marco_msnm(datos):
    z_ref = datos["msnm"]["z_ref_m"]
    assert 2000.0 < z_ref < 3000.0
    assert len(datos["lindero"]) == len(datos["calle"]) == 25
    for p in datos["lindero"] + datos["calle"]:
        assert p["z"] is not None and p["msnm"] is not None
        assert abs((p["z"] + z_ref) - p["msnm"]) < 0.01
    assert datos["perfil"]["z_min"] <= datos["perfil"]["z_max"]
    assert datos["perfil"]["calle_min"] <= datos["perfil"]["calle_max"]


def test_vista_desde_la_calle_espejo(datos):
    """El eje se invierte si hace falta para mirar desde la calle, no desde el lote."""
    assert isinstance(datos["frente"]["espejo"], bool)
    lo, hi = datos["lote_x"]
    assert lo < 0 < hi
    assert datos["x_rango"][0] < lo and datos["x_rango"][1] > hi
    # las esquinas del frente caen en los extremos del segmento 0..L
    xf = sorted(e["xf"] for e in datos["esquinas"])
    assert min(xf) == pytest.approx(lo, abs=0.2)
    assert max(xf) == pytest.approx(hi, abs=0.2)


def test_curvas_de_nivel_en_msnm(datos):
    curvas = datos["curvas"]
    assert len(curvas) >= 5
    z_ref = datos["msnm"]["z_ref_m"]
    x0, x1 = datos["x_rango"]
    for c in curvas:
        assert abs((c["z"] + z_ref) - c["msnm"]) < 0.02
        assert c["tramos"]
        for a, b in c["tramos"]:
            assert a <= b
            assert x0 - 0.1 <= a <= x1 + 0.1
            assert x0 - 0.1 <= b <= x1 + 0.1
    # las cotas estan ordenadas y son multiplos del paso (0,50 m)
    msnm = [c["msnm"] for c in curvas]
    assert msnm == sorted(msnm)
    for v in msnm:
        assert abs(v * 2 - round(v * 2)) < 1e-6


def test_esquinas_del_poligono(datos):
    esq = datos["esquinas"]
    assert len(esq) == 6
    z_ref = datos["msnm"]["z_ref_m"]
    for e in esq:
        assert abs((e["z"] + z_ref) - e["msnm"]) < 0.01
        assert e["rol"] in ("izq", "der", "fondo")
    assert any(e["rol"] == "izq" for e in esq)
    assert any(e["rol"] == "der" for e in esq)


def test_vecinos_inmediatos_con_altura(datos):
    vec = datos["vecinos"]
    assert vec, "sin volumenes de vecinos inmediatos"
    roles = {v["rol"] for v in vec}
    assert "lateral_izq" in roles and "lateral_der" in roles
    for v in vec:
        assert v["h"] > 0
        assert v["x0"] <= v["x1"]
        assert v["z_top"] == pytest.approx(v["z_base"] + v["h"], abs=0.01)
    # los laterales conservan el color del lado del lote que tocan
    colores_lado = {l["color"] for l in datos["lados"]}
    for v in vec:
        if v["rol"].startswith("lateral"):
            assert v["color"] in colores_lado


def test_perimetro_con_colores_de_la_planta(datos):
    lados = datos["lados"]
    assert lados
    colores = set()
    for l in lados:
        assert l["color"] == datos["lados"][0]["color"] or l["color"].startswith("#")
        colores.add(l["color"])
        assert len(l["polyline_xz"]) >= 2
    frente = [l for l in lados if l["lado_id"] == datos["frente"]["lado_id"]][0]
    assert frente["color"] == "#2563eb"       # via = azul (paleta de la planta)
    assert len(colores) >= 2                   # el lote tiene lados de mas de un tipo


def test_puntos_proyectados_y_altura(aislado):
    mod = aislado
    # dos puntos interiores del lote (grilla ETAPA1)
    estado = mod.guardar_puntos(CHIP, [{"id": "P1", "x": 92.5, "y": 102.5},
                                       {"id": "P2", "x": 112.5, "y": 92.5}],
                                {"P2": 12.5})
    assert len(estado["puntos"]) == 2
    d = mod.construir(CHIP, mdt="malla")
    assert len(d["puntos"]) == 2
    p1, p2 = d["puntos"]
    assert p1["id"] == "P1" and p1["color"] == "#b42318"
    assert p2["id"] == "P2" and p2["color"] == "#6d28d9"
    h = d["altura"]["h_m"]
    for p in d["puntos"]:
        assert p["dentro"] is True
        assert p["z"] is not None and p["msnm"] is not None
        assert p["z_top"] == pytest.approx(p["z"] + p["h_m"], abs=0.001)
        assert d["x_rango"][0] <= p["xf"] <= d["x_rango"][1]
    assert p1["h_m"] == pytest.approx(h, abs=0.001)
    assert p2["h_m"] == pytest.approx(12.5, abs=0.001)


def test_maximo_cinco_puntos_y_validacion(aislado):
    mod = aislado
    fuera = [{"id": "P%d" % i, "x": 60.0, "y": 60.0} for i in range(1, 3)]
    estado = mod.guardar_puntos(CHIP, fuera)
    assert estado["puntos"] == []
    assert estado["descartados"] >= 2
    siete = [{"id": "P%d" % i, "x": 92.5, "y": 102.5} for i in range(1, 8)]
    estado = mod.guardar_puntos(CHIP, siete)
    assert len(estado["puntos"]) == 5
    assert [p["id"] for p in estado["puntos"]] == ["P1", "P2", "P3", "P4", "P5"]


def test_banda_de_altura_sobre_el_terreno(datos):
    b = datos["banda"]
    h = datos["altura"]["h_m"]
    assert b["top_z"] == pytest.approx(b["base_z"] + h, abs=0.001)
    assert b["top_msnm"] == pytest.approx(b["base_msnm"] + h, abs=0.02)
    assert b["delta_vs_z0_m"] == pytest.approx(b["base_z"] - datos["datum"]["z0_m"], abs=0.001)
    # el datum por defecto es el minimo del lote y NO coincide con el terreno
    assert datos["datum"]["modo"] == "min_lote"
    assert datos["datum"]["z0_m"] == pytest.approx(datos["lote_min_z"], abs=0.001)
    assert abs(b["delta_vs_z0_m"]) > 0.2


def test_plano_miniatura(datos):
    pl = datos["plano"]
    assert len(pl["lote"]) >= 3
    assert pl["bbox"][0] < pl["bbox"][2] and pl["bbox"][1] < pl["bbox"][3]
    assert len(pl["lados"]) == len(datos["lados"])
    assert sum(1 for l in pl["lados"] if l["es_frente"]) == 1
    assert pl["frente"]["normal"] != [0, 0]
    assert len(pl["vecinos"]) == len(datos["vecinos"])

