# -*- coding: utf-8 -*-
"""Guardian de regresion para la regla de LOTE DE ESQUINA (2026-08-23).

Valida desde el fuente:
  - LADOS v06: en lote de esquina NO se asigna lado Posterior (idx_posterior
    se anula -> la esquina interior lleva patio 3x3, no aislamiento posterior).
  - PATIO v02.1: el patio de esquina se ancla en el vertice N cuando los dos
    lados que lo comparten son COLINDANTES (Lateral o Posterior), no solo
    Lateral (corrige el caso en que el vecino no coincide exactamente o un
    lado queda clasificado "Posterior").
  - NORMATIVA v08.2: en lote de esquina NO aplica aislamiento posterior
    (solo el frente lleva antejardin); lee es_esquina desde sides_data.
"""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "src", "fase-1-contexto")


def _src(nombre):
    with open(os.path.join(BASE, nombre), "r", encoding="utf-8") as f:
        return f.read()


def test_lados_esquina_anula_posterior():
    s = _src("F1_ETAPA2_LADOS_v06.py")
    assert "if es_esquina:" in s
    assert "idx_posterior = None" in s
    assert "CORRECCION ESQUINA" in s


def test_patio_colindantes_no_solo_lateral():
    s = _src("F1_ETAPA2_PATIO_v02.py")
    assert 'cat1 in ("Lateral", "Posterior")' in s
    assert 'cat2 in ("Lateral", "Posterior")' in s
    assert "PATIO v02.1" in s


def test_normativa_esquina_sin_posterior():
    s = _src("F1_ETAPA2_NORMATIVA_v08.py")
    assert "es_esquina" in s
    assert "sin aislamiento posterior" in s
    assert "if es_esquina:" in s
    assert "retiro_posterior = 0.0" in s
    assert "NORMATIVA v08.1" in s
