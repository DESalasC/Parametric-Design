# -*- coding: utf-8 -*-
"""Guardian para vecinos_por_lado.py (clasificación de vecinos colindantes por lado)."""

import importlib.util
import json
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
MOD = os.path.join(ROOT, "src", "orquestador", "vecinos_por_lado.py")
POT_CACHE = os.path.join(ROOT, "data", "pot-cache")

spec = importlib.util.spec_from_file_location("vecinos_por_lado", MOD)
vpl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vpl)

CARDS = {"Norte", "Sur", "Oriente", "Occidente"}
FRENTES = {"predio", "via", "espacio_publico", "libre"}


def _contexto(chip):
    with open(os.path.join(POT_CACHE, "%s-contexto.json" % chip), "r", encoding="utf-8") as f:
        return json.load(f)


def _clasificar(chip):
    return vpl.clasificar_vecinos_por_lado(_contexto(chip))


def test_clasificacion_estructura_los_3_lotes():
    for chip in ("AAA0127AZPA", "AAA0030JKOE", "AAA0039KRMR"):
        r = _clasificar(chip)
        assert r["chip"] == chip
        assert r["n_lados"] >= 1
        for lado in r["lados"]:
            assert lado["cardinal"] in CARDS
            assert lado["frente"] in FRENTES
            assert lado["frente_fuente"] == "auto"
            assert lado["segmentos"], "todo lado debe referenciar segmentos originales"
            nombres = [v["nombre"] for v in lado["vecinos"]]
            esperados = ["%s%d" % (lado["cardinal"], i) for i in range(1, len(nombres) + 1)]
            assert nombres == esperados
            for v in lado["vecinos"]:
                assert v["chip"]
                assert "altura_m" in v and v["altura_m"] is None
                assert "pisos" in v and v["pisos"] is None


def test_filtra_solo_colindantes():
    for chip in ("AAA0127AZPA", "AAA0030JKOE", "AAA0039KRMR"):
        ctx = _contexto(chip)
        r = _clasificar(chip)
        assert r["n_predios_colindantes"] <= len(ctx.get("vecinos", []))


def test_distingue_via_de_predio():
    # El Prado: Norte = vía (no predio)
    el_prado = {l["cardinal"]: l for l in _clasificar("AAA0127AZPA")["lados"]}
    assert el_prado["Norte"]["frente"] == "via"
    assert el_prado["Norte"]["n_vecinos"] == 0
    # Muzú (lote de esquina): Oriente y Sur = vía
    muzu = {l["cardinal"]: l for l in _clasificar("AAA0039KRMR")["lados"]}
    assert muzu["Oriente"]["frente"] == "via"
    assert muzu["Sur"]["frente"] == "via"


def test_candelaria_multi_vecino_por_lado():
    r = _clasificar("AAA0030JKOE")
    by_card = {l["cardinal"]: l for l in r["lados"]}
    assert "Sur" in by_card
    assert by_card["Sur"]["n_vecinos"] >= 2
    chips = [v["chip"] for v in by_card["Sur"]["vecinos"]]
    assert len(chips) == len(set(chips))


def test_a_normativa_vecinos_por_lado():
    r = _clasificar("AAA0030JKOE")
    for lado in r["lados"]:
        if lado["frente"] == "predio":
            for i, v in enumerate(lado["vecinos"], start=1):
                v["altura_m"] = float(i * 3)
    out = vpl.a_normativa_vecinos_por_lado(r)
    assert out, "debe producir alturas para los lados predio"
    for k, vals in out.items():
        assert int(k) >= 0
        assert isinstance(vals, list) and vals
        assert all(isinstance(x, float) for x in vals)
    # La Candelaria: el segmento 9 (esquina Sur) linda con 2 vecinos
    assert "9" in out and len(out["9"]) == 2
    # los lados no-predio no generan segmentos
    for lado in r["lados"]:
        if lado["frente"] != "predio":
            for sid in lado["segmentos"]:
                assert str(sid) not in out


def test_a_normativa_respeta_confirmacion():
    clasif = {
        "lados": [
            {"cardinal": "Sur", "frente": "predio", "frente_override": None,
             "confirmacion": "sobran", "segmentos": [2, 3],
             "segmentos_vecinos": {"2": ["A"], "3": ["B"]},
             "vecinos": [
                 {"chip": "A", "nombre": "Sur1", "altura_m": 9.0, "corresponde": True},
                 {"chip": "B", "nombre": "Sur2", "altura_m": 12.0, "corresponde": False},
             ],
             "vecinos_manuales": [
                 {"nombre": "Sur_extra1", "chip": "", "altura_m": 6.0},
             ]},
            {"cardinal": "Norte", "frente": "via", "frente_override": None,
             "segmentos": [0], "segmentos_vecinos": {}, "vecinos": [],
             "vecinos_manuales": []},
            {"cardinal": "Oriente", "frente": "predio", "frente_override": None,
             "confirmacion": "no_es_predio", "segmentos": [1],
             "segmentos_vecinos": {"1": ["C"]},
             "vecinos": [{"chip": "C", "nombre": "Oriente1", "altura_m": 10.0,
                          "corresponde": True}],
             "vecinos_manuales": []},
        ]
    }
    out = vpl.a_normativa_vecinos_por_lado(clasif)
    # Sur: A incluido (9.0) + manual (6.0) en el primer segmento "2"; B excluido
    assert out["2"] == [9.0, 6.0]
    assert out["3"] == [6.0]  # manual en todos los segmentos del lado
    # Norte (via) y Oriente (no_es_predio) no generan
    assert "0" not in out
    assert "1" not in out


def test_ep_que_cubre_el_lote_no_clasifica_frentes():
    """Un EP que se SUPERPONE al lote (p.ej. 'Pueblo Viejo', estructurante
    propuesto con fragmentos sobre el predio) no debe voltear la clasificacion
    de frentes a espacio_publico (regresion 2026-09-28)."""
    lote = [(0, 0, 0), (20, 0, 0), (20, 20, 0), (0, 20, 0)]
    vecino_norte = [(0, 20, 0), (20, 20, 0), (20, 30, 0), (0, 30, 0)]
    ep_cubre = [(-5, -5, 0), (25, -5, 0), (25, 15, 0), (-5, 15, 0), (-5, -5, 0)]
    ctx = {
        "metadata": {"chip": "TEST", "origen_sirgas": {"crs": "ESRI:102233"},
                     "azimuth_norte_grados": 0},
        "lote_objetivo": {"vertices_3d_local": lote},
        "vias_oficiales": [],
        "espacios_publicos": [
            {"nombre": "Pueblo Viejo", "fuente": "Parque", "tipo": "Parque",
             "coordenadas_local": ep_cubre},
        ],
        "vecinos": [{"chip": "V1", "vertices_3d_local": vecino_norte}],
    }
    r = vpl.clasificar_vecinos_por_lado(ctx)
    norte = [l for l in r["lados"] if l["cardinal"] == "Norte"]
    assert norte and norte[0]["frente"] == "predio", [l["frente"] for l in r["lados"]]
    assert "Pueblo Viejo" in r.get("eps_ignorados", [])
