# -*- coding: utf-8 -*-
"""Test conductual de F1_ETAPA2_PATIO_v03 (BIFURCACION por numero de volumenes).

Ejecuta el componente REAL de Grasshopper en CPython con el stub minimo de
Rhino.Geometry (tests/stub_rhino_min.py), sin abrir Rhino.

Cubre (pedido del operador 2026-09-30):
  1) modo UNICO (default): comportamiento v02.5 intacto (1 patio desde V_N,
     garantias area >= 9 m2 y claridad >= 3 m).
  2) modo UNICO cuando el V_N no valida: 0 patios + motivo + sugerencia multi.
  3) modo MULTI (n_volumenes >= 2): varios patios en esquinas interiores
     elegibles, priorizando V_N y luego interioridad; sin solapes; garantias.
  4) modo MULTI: tope por numero de volumenes y por esquinas disponibles.
  5) modo MULTI sin esquinas elegibles: 0 patios con motivo.
  6) tolerancia del input n_volumenes (0/None -> unico; valores string).
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
PATIO_V03 = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_PATIO_v03.py")

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


def _correr_patio_v03(lot, sides_json, altura=11.4, n_volumenes=None):
    gvars = {
        "lot_vertices": [P.Point3d(x, y, 0.0) for (x, y) in lot],
        "sides_table_json": sides_json,
        "altura_max_pot": altura,
    }
    if n_volumenes is not None:
        gvars["n_volumenes"] = n_volumenes
    return _ejecutar(PATIO_V03, gvars)


def _metricas_patio(crv):
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


def _sides_todos_laterales(n, vertice_n=0):
    lados = []
    for i in range(n):
        lados.append({"id": i, "clasificacion": "Lateral", "motivo": "test",
                      "dist_via_m": None, "dist_ep_m": None, "dist_vec_m": 0.0,
                      "toca_via": False, "toca_ep": False, "toca_vecino": True,
                      "comparte_a": i in (0, n - 1), "comparte_n": i in (0, n - 1)})
    return {"lados": lados, "total_lados": n, "vertice_a": 0, "vertice_n": vertice_n,
            "es_esquina": False}


PENTAGONO = [(0, 0), (12, 0), (14, 8), (4, 12), (6, 10.392304845413264)]
CUADRADO_30 = [(0, 0), (30, 0), (30, 30), (0, 30)]
RECT_4X20 = [(0, 0), (4, 0), (4, 20), (0, 20)]
# V0 con lado adyacente corto (2.5 m) -> el patio de 3 m no cabe
PENT_ASIM = [(0, 0), (2.5, 0), (18, 2), (20, 18), (0, 15)]


# --------------------------------------------------------------------------
# 1) modo UNICO (default = v02.5)
# --------------------------------------------------------------------------
def test_unico_default_igual_v02():
    g = _correr_patio_v03(PENTAGONO, json.dumps(_sides_todos_laterales(5)))
    assert g.get("patio_count") == 1
    msg = str(g.get("mensaje"))
    assert "PATIO v03" in msg and "modo unico" in msg
    area, claridad, pts = _metricas_patio(g["patios_curves"][0])
    assert area >= 9.0 - 1e-6
    assert claridad >= 3.0 - 1e-6
    l1 = math.hypot(pts[1].X - pts[0].X, pts[1].Y - pts[0].Y)
    assert abs(l1 - 3.0 / math.sin(math.radians(60.0))) < 1e-3


def test_unico_n_volumenes_1_explicito():
    g = _correr_patio_v03(PENTAGONO, json.dumps(_sides_todos_laterales(5)), n_volumenes=1)
    assert g.get("patio_count") == 1
    assert "modo unico" in str(g.get("mensaje"))


def test_tolerancia_input_n_volumenes():
    # 0 / None / string -> modo unico
    g0 = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)), n_volumenes=0)
    assert g0.get("patio_count") == 1
    assert "modo unico" in str(g0.get("mensaje"))
    gs = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)), n_volumenes="3")
    assert "modo MULTI" in str(gs.get("mensaje"))


# --------------------------------------------------------------------------
# 2) modo UNICO cuando el V_N no cabe -> 0 + motivo + sugerencia
# --------------------------------------------------------------------------
def test_unico_vn_no_cabe_sugiere_multi():
    g = _correr_patio_v03(PENT_ASIM, json.dumps(_sides_todos_laterales(5)))
    assert g.get("patio_count") == 0
    msg = str(g.get("mensaje"))
    assert "Generados: 0" in msg
    assert "no valida" in msg
    assert "Sugerencia" in msg and "n_volumenes" in msg


# --------------------------------------------------------------------------
# 3) modo MULTI
# --------------------------------------------------------------------------
def test_multi_cuadrado_2_patios_sin_solape():
    g = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)), n_volumenes=2)
    assert g.get("patio_count") == 2
    msg = str(g.get("mensaje"))
    assert "modo MULTI" in msg and "Generados: 2/2" in msg
    patios = g["patios_curves"]
    # anclas V0 (V_N) y luego V1 (orden estable sin datos de interioridad)
    exp = g.get("patios_export") or []
    anchors = [p.get("vertice_ancla") for p in exp] if exp else None
    assert anchors == [0, 1] or anchors is None  # export puede no estar; validar geometria
    for crv in patios:
        area, claridad, pts = _metricas_patio(crv)
        assert area >= 9.0 - 1e-6
        assert claridad >= 3.0 - 1e-6
    # sin solapes entre si
    a0, _, p0 = _metricas_patio(patios[0])
    a1, _, p1 = _metricas_patio(patios[1])
    assert not _solapan(p0, p1)


def test_multi_pentagono_2_patios_garantias():
    g = _correr_patio_v03(PENTAGONO, json.dumps(_sides_todos_laterales(5)), n_volumenes=2)
    assert g.get("patio_count") == 2
    for crv in g["patios_curves"]:
        area, claridad, pts = _metricas_patio(crv)
        assert area >= 9.0 - 1e-6
        assert claridad >= 3.0 - 1e-6


def test_multi_tope_por_esquinas_disponibles():
    g = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)), n_volumenes=9)
    assert g.get("patio_count") == 4  # solo 4 esquinas
    msg = str(g.get("mensaje"))
    assert "Generados: 4/9" in msg


def test_multi_solape_rechaza_y_continua():
    # rectangulo de 4 m de ancho: V0 ok; V1 se solapa -> rechazado; V2 ok
    g = _correr_patio_v03(RECT_4X20, json.dumps(_sides_todos_laterales(4)), n_volumenes=2)
    assert g.get("patio_count") == 2
    msg = str(g.get("mensaje"))
    assert "solapa" in msg
    p0 = _metricas_patio(g["patios_curves"][0])[2]
    p1 = _metricas_patio(g["patios_curves"][1])[2]
    assert not _solapan(p0, p1)


def test_multi_sin_esquinas_elegibles():
    sides = _sides_todos_laterales(4)
    for l in sides["lados"]:
        l["clasificacion"] = "Frontal"
    g = _correr_patio_v03(CUADRADO_30, json.dumps(sides), n_volumenes=2)
    assert g.get("patio_count") == 0
    msg = str(g.get("mensaje"))
    assert "Generados: 0" in msg and "modo MULTI" in msg


# --------------------------------------------------------------------------
# util local de solape (replica la logica de v03 para validar en el test)
# --------------------------------------------------------------------------
def _punto_en_poly(pt, pts):
    n = len(pts)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = pts[i].X, pts[i].Y
        xj, yj = pts[j].X, pts[j].Y
        if (yi > pt.Y) != (yj > pt.Y):
            if abs(yj - yi) > 1e-12:
                x_int = xi + (pt.Y - yi) * (xj - xi) / (yj - yi)
                if pt.X < x_int:
                    inside = not inside
        j = i
    return inside


def _solapan(pa, pb):
    muestras_a = list(pa) + [P.Point3d(sum(p.X for p in pa) / len(pa),
                                       sum(p.Y for p in pa) / len(pa), 0.0)]
    muestras_b = list(pb) + [P.Point3d(sum(p.X for p in pb) / len(pb),
                                       sum(p.Y for p in pb) / len(pb), 0.0)]
    for p in muestras_a:
        if _punto_en_poly(p, pb):
            return True
    for p in muestras_b:
        if _punto_en_poly(p, pa):
            return True
    return False


if __name__ == "__main__":
    print("=== TESTS PATIO v03 (BIFURCACION) ===")
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
            print("  [OK]", test.__name__)
        except Exception as e:
            failed += 1
            print("  [FAIL]", test.__name__, "->", str(e)[:300])
    print("=== RESULTADO: {} pasaron, {} fallaron ===".format(passed, failed))
    if failed:
        sys.exit(1)
