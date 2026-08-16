# -*- coding: utf-8 -*-
"""Guardian de regresion para F1_ETAPA2_LADOS_v04.py.

Las replicas puras de tests no ejercitan Rhino .NET real (Intersection),
asi que este test vigila invariantes de sintaxis del fuente que requieren
el ensamblado de Rhino en el canvas (IronPython GH).
"""

import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "src",
                    "fase-1-contexto", "F1_ETAPA2_LADOS_v04.py")


def _fuente():
    with open(RUTA, "r", encoding="utf-8") as f:
        return f.read()


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


def test_tol_colindancia_configurable():
    """Entrada opcional tol_colindancia_m presente en el MAIN."""
    src = _fuente()
    assert "tol_colindancia_m" in src
