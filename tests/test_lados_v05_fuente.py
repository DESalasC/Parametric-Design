# -*- coding: utf-8 -*-
"""Guardian de regresion para F1_ETAPA2_LADOS_v05.py.

Verifica invariantes de sintaxis que requieren Rhino .NET real en el canvas
(IronPython GH): interseccion, medicion de ancho total y mensaje v05.
"""

import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-1-contexto", "F1_ETAPA2_LADOS_v05.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


def test_medicion_ancho_total_presente():
    """v05 mide el ancho TOTAL del perfil vial (no entre andenes)."""
    src = _fuente()
    assert "medir_ancho_via_total" in src
    assert "medir_ancho_via_andenes" not in src
    assert "ancho total" in src


def test_intersection_namespace_correcto():
    """Usar Rhino.Geometry.Intersect.Intersection.CurveLine (linea larga)."""
    src = _fuente()
    assert "rg.Intersection.Intersection" not in src
    assert "rg.Intersect.Intersection.CurveLine" in src


def test_intersection_point_accedido():
    """IntersectionEvent.PointA (Rhino 8) o IntersectionPoint (legacy)."""
    src = _fuente()
    assert "punto_interseccion" in src
    assert "PointA" in src


def test_andenes_obsoletos():
    """andenes_curves se recibe solo informativo (sin filtrar/medir)."""
    src = _fuente()
    assert "OBSOLETA" in src


def test_mensaje_v05():
    src = _fuente()
    assert "LADOS v05 |" in src


def test_tol_colindancia_configurable():
    src = _fuente()
    assert "tol_colindancia_m" in src
