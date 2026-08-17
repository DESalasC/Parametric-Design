# -*- coding: utf-8 -*-
"""Guardian de regresion para F1_ETAPA2_LADOS_v06.py.

Verifica invariantes de sintaxis que requieren Rhino .NET real en el canvas:
clasificacion por vertices coincidentes, contacto minimo, esquina real,
interseccion y mensaje v06.
"""

import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-1-contexto", "F1_ETAPA2_LADOS_v06.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def test_clasificacion_por_vertices_coincidentes():
    src = _fuente()
    assert "lado_lateral_por_vertices" in src
    assert "TOL_VERTICES_COINC_M" in src


def test_contacto_minimo_por_longitud():
    src = _fuente()
    assert "fracciones_contacto" in src
    assert "CONTACTO_MIN_FRACCION" in src
    assert "contacto_min_frac" in src


def test_esquina_por_contacto_real():
    src = _fuente()
    assert "vertice_toca_via_o_ep" in src
    assert "UMBRAL_FRONTAL" not in src


def test_obsoletas_eliminadas():
    src = _fuente()
    assert "lado_colindante" not in src
    assert "curva_toca_segmento" not in src


def test_medicion_ancho_total():
    src = _fuente()
    assert "medir_ancho_via_total" in src


def test_intersection_namespace():
    src = _fuente()
    assert "rg.Intersection.Intersection" not in src
    assert "rg.Intersect.Intersection.CurveLine" in src
    assert "punto_interseccion" in src


def test_mensaje_v06():
    src = _fuente()
    assert "LADOS v06.1 |" in src
    assert "fr:" in src
    assert "aislamiento_tipo" in src


def test_helper_contacto_definido():
    """min_dist_pt_a_curvas debe estar DEFINIDA (no solo llamada)."""
    src = _fuente()
    assert "def min_dist_pt_a_curvas" in src
    assert "min_dist_pt_a_curvas(pt, vias)" in src


def test_prefijo_error_v06():
    """El prefijo del mensaje de error debe decir v06.1 (no v04 heredado)."""
    src = _fuente()
    assert "LADOS v04 | ERROR" not in src
    assert "LADOS v06.1 | ERROR" in src


def test_version_v061_encabezado():
    """v06.1 debe aparecer en el historial de versiones del encabezado."""
    src = _fuente()
    assert "v06.1 (2026-08-17)" in src
    assert "dx/dy/mx/my" in src


def test_lado_direccion_v061():
    """v06.1: cada lado entrega dx/dy/mx/my para F3 (medianera sin depender
    del orden de lote_vertices)."""
    src = _fuente()
    assert '"dx": round(p2.X - p1.X, 4)' in src
    assert '"dy": round(p2.Y - p1.Y, 4)' in src
    assert '"mx": round((p1.X + p2.X) / 2.0, 4)' in src
    assert '"my": round((p1.Y + p2.Y) / 2.0, 4)' in src
