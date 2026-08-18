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
