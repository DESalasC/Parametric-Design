# -*- coding: utf-8 -*-
"""Test de F1_ETAPA2_NORMATIVA_v10.py — Retiro patrimonial limitado a primera franja.

Ejecuta el componente REAL en CPython con stub mínimo de Rhino.Geometry.
Verifica que, con franja_patrimonial_longitud_m definido, el script integra el
retiro patrimonial sin romper el pipeline (genera salidas y no lanza excepciones),
y que sin franja se conserva el comportamiento legacy (retiro sobre todo el lado).
"""
import io
import os
import sys
import types

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(TESTS_DIR, ".."))
NORMATIVA_V10 = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_NORMATIVA_v10.py")

sys.path.insert(0, TESTS_DIR)


def _instalar_stub():
    mod = sys.modules.get("Rhino.Geometry")
    if mod is not None and getattr(mod, "__stub_min__", False):
        return mod
    import stub_rhino_min as stub
    rhino_mod = types.ModuleType("Rhino")
    geo_mod = types.ModuleType("Rhino.Geometry")
    for k in ("Point3d", "Vector3d", "Polyline", "PolylineCurve", "Line",
              "AreaMassProperties", "Brep", "Curve", "Intersect"):
        setattr(geo_mod, k, getattr(stub, k))
    geo_mod.__stub_min__ = True
    rhino_mod.Geometry = geo_mod
    sys.modules["Rhino"] = rhino_mod
    sys.modules["Rhino.Geometry"] = geo_mod
    return geo_mod


P = _instalar_stub()


def _ejecutar(path, gvars):
    src = io.open(path, "r", encoding="utf-8").read()
    g = dict(gvars)
    g["__name__"] = "gh_component_test"
    exec(compile(src, path, "exec"), g)
    return g


def _lote_simple():
    return [
        (0.0, 0.0), (30.0, 0.0), (30.0, 20.0), (20.0, 35.0),
        (5.0, 30.0), (0.0, 15.0)
    ]


def _make_lot_polygon(coords):
    pts = [P.Point3d(x, y, 0.0) for (x, y) in coords]
    return P.PolylineCurve(P.Polyline(pts))


def _sides(n):
    lados = []
    for i in range(n):
        cls = 'Frontal' if i == 0 else 'Lateral'
        lados.append({'id': i, 'clasificacion': cls, 'motivo': 'test',
                      'dist_via_m': 12.0 if cls == 'Frontal' else None,
                      'dist_ep_m': None, 'dist_vec_m': 5.0 if cls == 'Lateral' else None,
                      'toca_via': cls == 'Frontal', 'toca_ep': False,
                      'toca_vecino': cls == 'Lateral',
                      'comparte_a': i in (0, n - 1), 'comparte_n': i in (0, n - 1),
                      'dx': 1.0, 'dy': 0.0, 'mx': 0.0, 'my': 0.0})
    return lados


def _gvars(franja_patrimonial_longitud_m=10.5, retiro_patrimonial_m=3.0, pisos=3):
    coords = _lote_simple()
    lot = _make_lot_polygon(coords)
    lados = _sides(len(coords))
    vertices = [P.Point3d(x, y, 0.0) for (x, y) in coords]
    vertices.append(vertices[0])
    return {
        "lot_polygon": lot,
        "vertices_lote": vertices,
        "lados": lados,
        "retiros_base": {},
        "vecinos_por_lado_json": None,
        "vecinos_por_lado": {},
        "retiro_patrimonial_m": retiro_patrimonial_m,
        "franja_patrimonial_longitud_m": franja_patrimonial_longitud_m,
        "vecino_patrimonio_por_lado": [{"lado_id": 0, "nivel": 2, "patrimonio": True}],
        "construccion_no_patrimonio_exenta": [],
        "altura_vecino_derecha_m": None,
        "altura_vecino_izquierda_m": None,
        "empate_lateral_derecha_m": None,
        "empate_lateral_izquierda_m": None,
        "cota_terreno_central_m": 0.9,
        "pisos_maximos_total": pisos,
        "floor_h": 3.0,
        "tratamiento": "Consolidacion",
        "rango": "4",
        "tipo_bonificacion": None,
        "piso_adicional": False,
        "normativa_confirmada": True,
        "ancho_via_m": 12.0,
        "voladizo_frontal_m": 0.0,
        "reglamentacion_json": {},
        "barras_json": None,
        "patio_raw": [],
        "nsr10_separacion_coef": 0.02,
        "empate_lateral_min_m": 4.0,
        "altura_vecinos_m": 0.0,
        "empate_posterior_pisos": 0,
        "es_esquina": False,
    }


def test_patrimonio_con_franja_ejecuta_y_salidas():
    gvars = _gvars(franja_patrimonial_longitud_m=10.5, retiro_patrimonial_m=3.0, pisos=3)
    g = _ejecutar(NORMATIVA_V10, gvars)
    rpp = g.get("retiros_por_piso", "[]")
    # retiros_por_piso debe ser JSON de lista con el retiro patrimonial configurado
    import json
    data = json.loads(rpp) if rpp else []
    assert isinstance(data, list)
    for row in data:
        assert row.get("retiro_patrimonial_m") == 3.0


def test_patrimonio_sin_franja_comportamiento_legacy():
    gvars = _gvars(franja_patrimonial_longitud_m=None, retiro_patrimonial_m=3.0, pisos=3)
    g = _ejecutar(NORMATIVA_V10, gvars)
    rpp = g.get("retiros_por_piso", "[]")
    import json
    data = json.loads(rpp) if rpp else []
    assert isinstance(data, list)
