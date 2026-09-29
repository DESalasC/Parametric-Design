# -*- coding: utf-8 -*-
"""Test conductual de F1_ETAPA2_LADOS_v06 + F1_ETAPA2_PATIO_v02 (2026-09-28).

Ejecuta los componentes REALES de Grasshopper en CPython con un stub minimo
de Rhino.Geometry (tests/stub_rhino_min.py), sin abrir Rhino.

Cubre:
  1) Regresion del hotfix v06.5: dos vias que se CRUZAN -> la clasificacion
     ya no debe abortar (antes: NameError 'point_in_lot'; sides vacio).
  2) Simplificacion colineal (giro < 2.5 grados): los micro-quiebres se
     fusionan; los quiebres >= 2.5 grados se mantienen.
  3) Garantias del patio v02.3 (decisiones operador 2026-09-28):
     area >= 9 m2 y claridad >= 3 m respecto a cada lado del predio.
  4) Dedup de puntos mejorados del Vertice N (max 1 patio).
  5) Chip real AAA0240ZXJH (si existe el contexto): 13 -> 4 lados y
     1 patio valido en la esquina colindante.
"""
import io
import json
import math
import os
import sys
import types

import pytest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(TESTS_DIR, ".."))
CTX = os.path.join(BASE, "data", "pot-cache", "AAA0240ZXJH-contexto.json")
LADOS = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_LADOS_v06.py")
PATIO = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_PATIO_v02.py")

sys.path.insert(0, TESTS_DIR)


def _instalar_stub():
    mod = sys.modules.get("Rhino.Geometry")
    if mod is not None and getattr(mod, "__stub_min__", False):
        return mod
    import stub_rhino_min as stub
    rhino_mod = types.ModuleType("Rhino")
    geo_mod = types.ModuleType("Rhino.Geometry")
    for k in ("Point3d", "Vector3d", "Polyline", "PolylineCurve", "Line"):
        setattr(geo_mod, k, getattr(stub, k))
    geo_mod.Intersect = stub.Intersect
    geo_mod.__stub_min__ = True
    rhino_mod.Geometry = geo_mod
    sys.modules["Rhino"] = rhino_mod
    sys.modules["Rhino.Geometry"] = geo_mod
    return geo_mod


STUB = _instalar_stub()
P = STUB


def _ejecutar(path, gvars):
    src = io.open(path, "r", encoding="utf-8").read()
    g = dict(gvars)
    g["__name__"] = "gh_component_test"
    exec(compile(src, path, "exec"), g)
    return g


def _poly(coords):
    pl = P.Polyline()
    for c in coords:
        pl.Add(P.Point3d(c[0], c[1], 0.0))
    return P.PolylineCurve(pl)


def _correr_lados(lot, vias=None, vecinos=None, eps=None):
    return _ejecutar(LADOS, {
        "lot_vertices": [P.Point3d(x, y, 0.0) for (x, y) in lot],
        "vias_curves": [_poly(c) for c in (vias or [])],
        "ep_curves": [_poly(c) for c in (eps or [])],
        "vecinos_curves": [_poly(c) for c in (vecinos or [])],
        "andenes_curves": [],
    })


def _correr_patio(lot, sides_json, altura=11.4):
    return _ejecutar(PATIO, {
        "lot_vertices": [P.Point3d(x, y, 0.0) for (x, y) in lot],
        "sides_table_json": sides_json,
        "altura_max_pot": altura,
    })


def _metricas_patio(crv):
    """(area, claridad, pts) del paralelogramo devuelto por PATIO."""
    pts = [p for p in crv._pts]
    p0 = pts[0]
    p1 = pts[1]
    p3 = pts[3]
    e1 = (p1.X - p0.X, p1.Y - p0.Y)
    e2 = (p3.X - p0.X, p3.Y - p0.Y)
    l1 = math.hypot(*e1)
    l2 = math.hypot(*e2)
    sin_t = abs(e1[0] * e2[1] - e1[1] * e2[0]) / (l1 * l2)
    area = l1 * l2 * sin_t
    claridad = min(l1 * sin_t, l2 * sin_t)
    return area, claridad, pts


# --------------------------------------------------------------------------
# 1) Regresion hotfix: vias cruzadas
# --------------------------------------------------------------------------
LOTE_CUADRADO = [(0, 0), (20, 0), (20, 20), (0, 20)]


def test_vias_cruzadas_no_abortan_clasificacion():
    vias = [
        [(25, -10), (25, 30)],
        [(10, 25), (40, 25)],
    ]
    g = _correr_lados(LOTE_CUADRADO, vias=vias)
    msg = str(g.get("mensaje"))
    assert "ERROR" not in msg
    assert "point_in_lot" not in msg
    sides = json.loads(g.get("sides_table_json") or "{}")
    assert sides.get("total_lados") == 4
    assert len(sides.get("lados", [])) == 4


# --------------------------------------------------------------------------
# 2) Simplificacion colineal 2.5 grados
# --------------------------------------------------------------------------
def test_simplificacion_colineal_2_5_grados():
    # v1=(10,0.1): giro ~1.15 grados -> se fusiona
    # v3=(20.4,10): giro ~4.6 grados -> se mantiene
    lot = [(0, 0), (10, 0.1), (20, 0), (20.4, 10), (20, 20), (0, 20)]
    g = _correr_lados(lot)
    sides = json.loads(g.get("sides_table_json") or "{}")
    assert sides.get("n_vertices_originales") == 6
    assert sides.get("total_lados") == 5
    msg = str(g.get("mensaje"))
    assert "Verts 6->5" in msg


# --------------------------------------------------------------------------
# 3) Garantias del patio: esquina no perpendicular (60 grados)
# --------------------------------------------------------------------------
def _sides_pentagono(n=5, vertice_n=0):
    lados = []
    for i in range(n):
        lados.append({"id": i, "clasificacion": "Lateral", "motivo": "test",
                      "frac_via_m": 0.0, "frac_ep_m": 0.0, "frac_vec_m": 1.0,
                      "toca_via": False, "toca_ep": False, "toca_vecino": True,
                      "comparte_a": i in (0, n - 1), "comparte_n": i in (0, n - 1)})
    return {"lados": lados, "total_lados": n, "vertice_a": 0, "vertice_n": vertice_n,
            "es_esquina": False}


PENTAGONO = [(0, 0), (12, 0), (14, 8), (4, 12), (6, 10.392304845413264)]


def test_patio_esquina_no_perpendicular_garantias():
    g = _correr_patio(PENTAGONO, json.dumps(_sides_pentagono()))
    assert g.get("patio_count") == 1
    assert "ERROR" not in str(g.get("mensaje"))
    area, claridad, pts = _metricas_patio(g["patios_curves"][0])
    assert area >= 9.0 - 1e-6, "area {} < 9".format(area)
    assert claridad >= 3.0 - 1e-6, "claridad {} < 3".format(claridad)
    # el lado escala ~3/sin(60) = 3.46
    l1 = math.hypot(pts[1].X - pts[0].X, pts[1].Y - pts[0].Y)
    assert abs(l1 - 3.0 / math.sin(math.radians(60.0))) < 1e-3


def test_patio_dedup_puntos_mejorados():
    sides = _sides_pentagono()
    sides["vertice_n_points"] = [[0.0, 0.0, 0.0], [0.05, 0.0, 0.0], [0.1, 0.02, 0.0]]
    g = _correr_patio(PENTAGONO, json.dumps(sides))
    assert g.get("patio_count") == 1  # dedup: 3 puntos -> 1 patio
    msg = str(g.get("mensaje"))
    assert "puntos_mejorados" in msg


def test_patio_sin_lados_colindantes_reporta_motivo():
    sides = _sides_pentagono()
    sides["lados"][0]["clasificacion"] = "Frontal"
    sides["lados"][4]["clasificacion"] = "Frontal"
    g = _correr_patio(PENTAGONO, json.dumps(sides))
    assert g.get("patio_count") == 0
    assert "Generados: 0" in str(g.get("mensaje"))


# --------------------------------------------------------------------------
# 4) Chip real AAA0240ZXJH (se salta si no esta el contexto)
# --------------------------------------------------------------------------
@pytest.mark.skipif(not os.path.exists(CTX), reason="sin contexto AAA0240ZXJH")
def test_chip_real_simplifica_y_genera_patio():
    d = json.load(io.open(CTX, "r", encoding="utf-8"))
    lot = [(v[0], v[1]) for v in d["lote_objetivo"]["vertices_3d_local"]]
    if len(lot) > 1 and abs(lot[0][0] - lot[-1][0]) < 1e-9 and abs(lot[0][1] - lot[-1][1]) < 1e-9:
        lot = lot[:-1]

    vias = [v["coordenadas_local"] for v in d["vias_oficiales"] if v.get("coordenadas_local")]
    vecinos = [v["vertices_3d_local"] for v in d["vecinos"] if v.get("vertices_3d_local")]
    eps = [v["coordenadas_local"] for v in d["espacios_publicos"] if v.get("coordenadas_local")]

    g1 = _correr_lados(lot, vias=vias, vecinos=vecinos, eps=eps)
    msg = str(g1.get("mensaje"))
    assert "ERROR" not in msg, msg
    sides = json.loads(g1.get("sides_table_json") or "{}")
    assert sides.get("n_vertices_originales") == len(lot)
    assert sides.get("total_lados") == 4, "esperado 4 lados logicos"
    assert "Verts {}->4".format(len(lot)) in msg

    g2 = _correr_patio(lot, g1.get("sides_table_json"), altura=11.4)
    assert g2.get("patio_count") == 1, g2.get("mensaje")
    area, claridad, pts = _metricas_patio(g2["patios_curves"][0])
    assert area >= 9.0 - 1e-6
    assert claridad >= 3.0 - 1e-6
    # todos los vertices del patio dentro del lote
    pin = g2.get("point_in_lot")
    lot_pts = [P.Point3d(x, y, 0.0) for (x, y) in lot]
    assert all(pin(p, lot_pts) for p in pts[:-1])
