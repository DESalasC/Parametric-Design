# -*- coding: utf-8 -*-
"""Tests unitarios de las funciones de ayuda de F1_CONTEXTO50_BUILD_v01b.py.

Cubre directamente los helpers (leer_json, normalizar_vertices, altura_de,
_es_horario, _area_compacidad, _punto_en_poligono, construir_huella, ...),
reutilizando los stubs de Rhino del test de integracion.

Corre en CPython (no requiere Rhino ni Grasshopper).
"""

import io
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(__file__))
from test_contexto50_build import (  # noqa: E402
    JSON_REAL,
    SRC,
    _ejecutar_componente,
)


def _helpers():
    """Namespace del componente con todos los helpers ya definidos (sin JSON)."""
    ns = _ejecutar_componente(None)  # json_path vacio -> define funciones y sale
    return ns


# --------------------------------------------------------------- unwrap / tipos
def test_unwrap_variantes():
    ns = _helpers()
    unwrap = ns["unwrap"]
    assert unwrap(None) is None
    assert unwrap([5]) == 5
    assert unwrap((7, 8)) == 7
    assert unwrap([]) is None
    assert unwrap("x") == "x"
    assert unwrap(3.2) == 3.2


def test_parse_bool_variantes():
    ns = _helpers()
    parse_bool = ns["parse_bool"]
    assert parse_bool(True) is True
    assert parse_bool(False) is False
    assert parse_bool(None) is False
    for v in ("true", "1", "verdadero", "yes", "si", "True", " SI "):
        assert parse_bool(v) is True, v
    for v in ("false", "0", "no", "", "nada"):
        assert parse_bool(v) is False, v
    assert parse_bool([True]) is True  # lista de 1 (GH)


def test_to_float_variantes():
    ns = _helpers()
    to_float = ns["to_float"]
    assert abs(to_float("3.5", 0.0) - 3.5) < 1e-9
    assert to_float(4, 0.0) == 4.0
    assert to_float("no-num", 9.9) == 9.9
    assert to_float(None, 2.0) == 2.0
    assert abs(to_float(["6.25"], 0.0) - 6.25) < 1e-9


def test_pt_xy_variantes():
    ns = _helpers()
    pt_xy = ns["_pt_xy"]
    assert pt_xy([1, 2]) == (1.0, 2.0)
    assert pt_xy([1, 2, 3]) == (1.0, 2.0)
    assert pt_xy({"x": 4, "y": 5}) == (4.0, 5.0)
    assert pt_xy(None) is None
    assert pt_xy("no") is None


def test_meta_get_raiz_y_metadata():
    ns = _helpers()
    meta_get = ns["meta_get"]
    assert meta_get({"a": 1}, "a") == 1
    assert meta_get({"metadata": {"b": 2}}, "b") == 2
    assert meta_get({"metadata": {"b": 2}}, "z", 99) == 99
    assert meta_get(None, "a") is None


# --------------------------------------------------------------- json
def test_leer_json_utf8(tmp_path):
    ns = _helpers()
    leer_json = ns["leer_json"]
    p = tmp_path / "u.json"
    p.write_bytes('{"chip": "CAFÉ"}'.encode("utf-8"))
    assert leer_json(str(p))["chip"] == "CAFÉ"


def test_leer_json_latin1_fallback(tmp_path):
    ns = _helpers()
    leer_json = ns["leer_json"]
    p = tmp_path / "l.json"
    p.write_bytes(b'{"chip": "\xe9"}')  # 0xe9 = 'é' en latin-1, invalido en utf-8
    assert leer_json(str(p))["chip"] == "é"


# --------------------------------------------------------------- geometria
def test_normalizar_vertices_dedup_y_cierre():
    ns = _helpers()
    nv = ns["normalizar_vertices"]
    # consecutivos repetidos + cierre redundante
    raw = [[0, 0], [0, 0], [10, 0], [10, 0], [10, 10], [0, 0]]
    assert nv(raw) == [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0)]
    # menos de 3 -> no es anillo valido para el llamador
    assert nv([[0, 0], [1, 0]]) == [(0.0, 0.0), (1.0, 0.0)]
    # filtra invalidos
    assert nv([[0, 0], None, ["x", "y"], [1, 0], [1, 1]]) == [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0)]


def test_extraer_anillos_desde_vertices():
    ns = _helpers()
    ea = ns["extraer_anillos"]
    ed = {"vertices": [[0, 0], [4, 0], [4, 4], [0, 4]]}
    rings = ea(ed)
    assert len(rings) == 1
    assert len(rings[0]) == 4


def test_extraer_anillos_geojson_polygon():
    ns = _helpers()
    ea = ns["extraer_anillos"]
    ed = {"geometry": {"type": "Polygon",
                       "coordinates": [[[0, 0], [5, 0], [5, 5], [0, 5], [0, 0]]]}}
    rings = ea(ed)
    assert len(rings) == 1 and len(rings[0]) == 4


def test_altura_de_prioridades():
    ns = _helpers()
    altura_de = ns["altura_de"]
    # altura_m manda sobre pisos (ahora retorna 4 valores: h, p, fb, z_base)
    h, p, fb, zb = altura_de({"altura_m": 19.0, "pisos": 5}, 3.8)
    assert abs(h - 19.0) < 1e-9 and p == 5 and fb is False and zb == 0.0
    # sin altura_m -> pisos * altura_piso (fallback True)
    h, p, fb, zb = altura_de({"pisos": 4}, 3.8)
    assert abs(h - 15.2) < 1e-9 and p == 4 and fb is True and zb == 0.0
    # sin nada -> DEFAULT_ALTURA_M (3.0), 1 piso
    h, p, fb, zb = altura_de({}, 3.8)
    assert abs(h - 3.0) < 1e-9 and p == 1 and fb is True and zb == 0.0
    # altura_m infiere pisos si no vienen
    h, p, fb, zb = altura_de({"altura_m": 7.6}, 3.8)
    assert p == 2 and fb is False and zb == 0.0


def test_es_horario_y_area_compacidad():
    ns = _helpers()
    es_horario = ns["_es_horario"]
    ac = ns["_area_compacidad"]
    ccw = [(0, 0), (10, 0), (10, 10), (0, 10)]      # antihorario
    cw = list(reversed(ccw))                          # horario
    assert es_horario(ccw) is False
    assert es_horario(cw) is True
    area, comp = ac(ccw)
    assert abs(area - 100.0) < 1e-6
    # cuadrado: compacidad = 16r^2/(4 pi r^2) = 4/pi ~ 1.273
    assert abs(comp - (40.0 ** 2) / (4 * 3.141592653589793 * 100.0)) < 1e-6


def test_punto_en_poligono():
    ns = _helpers()
    pip = ns["_punto_en_poligono"]
    sq = [(0, 0), (10, 0), (10, 10), (0, 10)]
    assert pip(5, 5, sq) is True
    assert pip(15, 5, sq) is False
    assert pip(-1, 5, sq) is False


def test_construir_huella_fuerza_antihorario():
    ns = _helpers()
    ch = ns["construir_huella"]
    cw = [(0, 0), (0, 10), (10, 10), (10, 0)]  # horario
    crv = ch(cw)
    assert crv is not None
    pts = crv.pts[:-1]  # quitar cierre duplicado del stub
    s = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i][0], pts[i][1]
        x2, y2 = pts[(i + 1) % n][0], pts[(i + 1) % n][1]
        s += x1 * y2 - x2 * y1
    assert s > 0, "la huella debe quedar antihoraria"
    # menos de 3 puntos -> None
    assert ch([(0, 0), (1, 1)]) is None
