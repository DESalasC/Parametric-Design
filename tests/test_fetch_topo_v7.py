# -*- coding: utf-8 -*-
"""
Tests del fetch v7 — topografia MDT (plan lote-inclinado-candelaria, P0).

Cubre:
- Parser de la respuesta 'identify' del MDT (formato nuevo y viejo).
- Muestreo densificado: orden v6 estable + rejilla interior + anillo exterior.
- Resumen estadistico: delta, pendiente media y direccion de bajada.

Nota: el runner de la suite (Python 3.12) no trae 'requests'; se inyecta un
stub porque el modulo solo lo usa en runtime (get_elevation_from_api).
"""

import importlib.util
import sys
import types
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FETCH_V7 = PROJECT_ROOT / "scripts" / "utilities" / "fetch-urban-context-v7.py"

geom = pytest.importorskip("shapely.geometry")
Polygon, Point = geom.Polygon, geom.Point


def _stub_missing(name):
    try:
        __import__(name)
    except ImportError:
        sys.modules[name] = types.ModuleType(name)


def _load_fetch_v7():
    _stub_missing("requests")
    spec = importlib.util.spec_from_file_location("fetch_urban_context_v7", str(FETCH_V7))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


fetch = _load_fetch_v7()


class TestParseElevation:
    """Parser de la respuesta 'identify' del MDT (bug v6: leia 'value')."""

    def test_formato_mdt_actual(self):
        resp = {"results": [{"attributes": {"Stretch.Pixel Value": "2645.714111"}}]}
        assert fetch.parse_elevation_value(resp) == pytest.approx(2645.714111)

    def test_formato_viejo_value_numerico(self):
        assert fetch.parse_elevation_value({"results": [{"value": 2634.79}]}) == pytest.approx(2634.79)

    def test_formato_viejo_value_texto(self):
        assert fetch.parse_elevation_value(
            {"results": [{"value": "Elevacion: 2640.5"}]}) == pytest.approx(2640.5)

    def test_fallback_primer_numerico(self):
        resp = {"results": [{"attributes": {"foo": "abc", "bar": "2630.25"}}]}
        assert fetch.parse_elevation_value(resp) == pytest.approx(2630.25)

    def test_resultado_vacio(self):
        assert fetch.parse_elevation_value({"results": []}) is None

    def test_sin_results(self):
        assert fetch.parse_elevation_value({}) is None

    def test_atributo_no_numerico(self):
        resp = {"results": [{"attributes": {"Stretch.Pixel Value": "NoData"}}]}
        assert fetch.parse_elevation_value(resp) is None


class TestMuestreoTopo:
    """Muestreo: orden v6 estable + densificacion interior/anillo."""

    def _poly(self):
        return Polygon([(0.0, 0.0), (30.0, 0.0), (30.0, 20.0), (0.0, 20.0)])

    def test_orden_v6_estable(self):
        pts = fetch.generate_lote_topo_points(self._poly())
        tipos = [t for (_x, _y, t) in pts]
        assert tipos[:4] == ["vertice"] * 4
        assert tipos[4:8] == ["punto_medio"] * 4
        assert tipos[8] == "centroide"
        assert pts[0][0] == pytest.approx(0.0) and pts[0][1] == pytest.approx(0.0)
        assert pts[8][0] == pytest.approx(15.0) and pts[8][1] == pytest.approx(10.0)

    def test_densificacion_interior_y_anillo(self):
        pts = fetch.generate_lote_topo_points(self._poly())
        tipos = [t for (_x, _y, t) in pts]
        assert tipos.count("interior") >= 8
        assert tipos.count("anillo") >= 8
        poly = self._poly()
        for (x, y, t) in pts:
            if t == "anillo":
                assert not poly.contains(Point(x, y)), "punto de anillo dentro del lote"
            if t == "interior":
                assert poly.contains(Point(x, y)), "punto interior fuera del lote"

    def test_tope_max_puntos(self):
        pts = fetch.generate_lote_topo_points(
            self._poly(), paso_interior=0.5, anillo_m=2.0, anillo_paso=1.0)
        assert len(pts) <= fetch.TOPO_MAX_PUNTOS


class TestResumenTopo:
    """Resumen estadistico (ajuste de plano)."""

    def test_sin_cotas(self):
        pts = [{"x": 0, "y": 0, "z": None}, {"x": 1, "y": 1, "z": None}]
        r = fetch.calcular_resumen_topo(pts)
        assert r["n_fallidos"] == 2
        assert r["delta_m"] is None

    def test_plano_horizontal(self):
        pts = [{"x": float(i), "y": float(j), "z": 2634.0}
               for i in range(5) for j in range(5)]
        r = fetch.calcular_resumen_topo(pts)
        assert r["delta_m"] == pytest.approx(0.0)
        assert r["pendiente_media_pct"] == pytest.approx(0.0, abs=0.01)

    def test_plano_inclinado_10pct(self):
        pts = []
        for i in range(10):
            for j in range(10):
                x, y = float(i), float(j)
                pts.append({"x": x, "y": y, "z": 2600.0 + 0.1 * x})
        r = fetch.calcular_resumen_topo(pts)
        assert r["delta_m"] == pytest.approx(0.9, abs=0.05)
        assert r["pendiente_media_pct"] == pytest.approx(10.0, abs=0.5)
        # cuesta abajo hacia -x (270 grados con +y como norte)
        assert r["direccion_bajada_grados"] == pytest.approx(270.0, abs=2.0)
