# -*- coding: utf-8 -*-
"""Guardian del layout del caso A (El Prado) con nucleo descompuesto.

Valida sobre los JSON regenerados (2026-08-16):
  - circulacion (escaleras+ascensores) SEPARADA de servicios (8 m2),
  - hueco real del nucleo = bloque (ancho x largo) y balance por piso = GFA,
  - disposicion con tipos circulacion/servicios para F3_VOLUM_GENERADOR_v07.
"""

import json
import os

CASO = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-3-masa", "casos", "A")


def _layout():
    with open(os.path.join(CASO, "layout_espacial.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def _programa_areas():
    with open(os.path.join(CASO, "programa-areas.json"), "r", encoding="utf-8") as f:
        return json.load(f)


def test_circulacion_y_servicios_separados():
    nuc = _layout()["nucleos"]
    assert nuc["circulacion_m2"] == 31.8   # 2 escaleras (13,5) + 1 ascensor (4,8)
    assert nuc["servicios_m2"] == 8.0      # ductos/basuras/cuarto tecnico
    assert nuc["total_m2_piso"] == 39.8    # solidos = circulacion + servicios


def test_hueco_real_igual_bloque():
    nuc = _layout()["nucleos"]
    bloque = nuc["bloque"]
    assert nuc["hueco_m2_piso"] == round(bloque["ancho_m"] * bloque["largo_m"], 1)
    assert nuc["hueco_m2_piso"] == 48.6    # 5,4 x 9,0 (caso A, 1 ascensor)


def test_disposicion_tipos():
    disp = _layout()["nucleos"]["disposicion"]
    tipos = [c["tipo"] for c in disp]
    assert "circulacion" in tipos and "servicios" in tipos
    # suma de areas de cajas = solidos del nucleo (39,84 ≈ 39,8)
    suma = round(sum(c["ancho_m"] * c["largo_m"] for c in disp), 2)
    assert abs(suma - 39.84) < 0.01


def test_programa_areas_transporta_desglose():
    nuc = _programa_areas()["nucleo"]
    assert nuc["hueco_m2_piso"] == 48.6
    assert nuc["circulacion_m2"] == 31.8
    assert nuc["servicios_m2"] == 8.0
    assert len(nuc["disposicion"]) == 4


def test_balance_por_piso_igual_gfa():
    pa = _programa_areas()
    assert pa["gfa_total"] == 1461.1
    assert pa["pisos"] == 6
    for p in pa["programa_pisos"]:
        suma = round(sum(u["area_bruta"] for u in p["usos"]), 2)
        assert abs(suma - pa["area_por_piso"]) < 0.1
