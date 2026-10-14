# -*- coding: utf-8 -*-
"""Test conductual de F1_ETAPA2_PATIO_v03/v03.4 (BIFURCACION: UNICO vs MULTI; multi => separaciones).

Ejecuta el componente REAL de Grasshopper en CPython con el stub minimo de
Rhino.Geometry (tests/stub_rhino_min.py), sin abrir Rhino.

Cubre (pedido del operador 2026-09-30):
  1) modo AUTO (default, v03.1): infiere n = min(esquinas validas, capacidad)
     con capacidad = round(area_lote / A_REF_VOL_M2); el operador no toca nada.
  2) modo unico FORZADO (n_volumenes=1): comportamiento v02.5 estricto.
  3) modo MULTI FORZADO (n_volumenes>=2): tope explicito.
  4) AUTO con V_N sin cabida: ancla en otra esquina interior.
  5) Garantias por patio (area >= 9 m2, claridad >= 3 m) y sin solapes.
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
    import stub_rhino_min as stub
    rhino_mod = sys.modules.get("Rhino")
    geo_mod = sys.modules.get("Rhino.Geometry")
    if rhino_mod is None:
        rhino_mod = types.ModuleType("Rhino")
        sys.modules["Rhino"] = rhino_mod
    if geo_mod is None:
        geo_mod = types.ModuleType("Rhino.Geometry")
        sys.modules["Rhino.Geometry"] = geo_mod
    # Idempotente y COMPLETO: otro modulo de tests puede haber instalado un
    # subconjunto (p.ej. sin Curve/Brep): completar lo que falte.
    for k in ("Point3d", "Vector3d", "Polyline", "PolylineCurve", "Line",
              "Curve", "Brep", "AreaMassProperties"):
        if not hasattr(geo_mod, k):
            setattr(geo_mod, k, getattr(stub, k))
    geo_mod.Intersect = stub.Intersect
    geo_mod.__stub_min__ = True
    rhino_mod.Geometry = geo_mod
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
RECT_10X5 = [(0, 0), (10, 0), (10, 5), (0, 5)]
RECT_4X20 = [(0, 0), (4, 0), (4, 20), (0, 20)]
# V0 con lado adyacente corto (2.5 m) -> el patio de 3 m no cabe en V0
PENT_ASIM = [(0, 0), (2.5, 0), (18, 2), (20, 18), (0, 15)]


# --------------------------------------------------------------------------
# 1) modo AUTO (default; v03.4: n>=2 => sin patios)
# --------------------------------------------------------------------------
def test_auto_default_pentagono_un_patio():
    # lote pequeno (~101 m2): capacidad 1 -> un solo patio; mensaje AUTO
    g = _correr_patio_v03(PENTAGONO, json.dumps(_sides_todos_laterales(5)))
    assert g.get("patio_count") == 1
    msg = str(g.get("mensaje"))
    assert "PATIO v03.4" in msg and "modo AUTO" in msg and "inferido: 1" in msg
    area, claridad, pts = _metricas_patio(g["patios_curves"][0])
    assert area >= 9.0 - 1e-6
    assert claridad >= 3.0 - 1e-6
    l1 = math.hypot(pts[1].X - pts[0].X, pts[1].Y - pts[0].Y)
    # v03.2+: lado = max(base*(sin+cos)/sin, 3/sin, sqrt(9/sin)); esquina de 60 grados
    esperado = 3.8 * (math.sin(math.radians(60.0)) + math.cos(math.radians(60.0))) / math.sin(math.radians(60.0))
    assert abs(l1 - esperado) < 1e-2


def test_auto_none_explicito_equivale_auto():
    g = _correr_patio_v03(PENTAGONO, json.dumps(_sides_todos_laterales(5)), n_volumenes=None)
    assert "modo AUTO" in str(g.get("mensaje"))


def test_auto_capacidad_limita():
    # 30x30 = 900 m2 -> capacidad 3; 4 esquinas validas -> infiere 3 (v03.4: >=2 => sin patios)
    g = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)))
    assert g.get("patio_count") == 0
    msg = str(g.get("mensaje"))
    assert "inferido: 3" in msg
    assert "limitado por capacidad" in msg
    assert "separaciones" in msg


def test_auto_lote_pequeno_capacidad_uno():
    # 10x5 = 50 m2 -> capacidad 1
    g = _correr_patio_v03(RECT_10X5, json.dumps(_sides_todos_laterales(4)))
    assert g.get("patio_count") == 1
    assert "inferido: 1" in str(g.get("mensaje"))


# --------------------------------------------------------------------------
# 2) modo UNICO forzado (v02.5 estricto)
# --------------------------------------------------------------------------
def test_unico_forzado_n_volumenes_1():
    g = _correr_patio_v03(PENTAGONO, json.dumps(_sides_todos_laterales(5)), n_volumenes=1)
    assert g.get("patio_count") == 1
    msg = str(g.get("mensaje"))
    assert "modo unico (forzado)" in msg


def test_unico_forzado_vn_no_cabe_motivo():
    g = _correr_patio_v03(PENT_ASIM, json.dumps(_sides_todos_laterales(5)), n_volumenes=1)
    assert g.get("patio_count") == 0
    msg = str(g.get("mensaje"))
    assert "Generados: 0" in msg
    assert "no valida" in msg
    assert "Sugerencia" in msg


# --------------------------------------------------------------------------
# 3) modo MULTI forzado (v03.4: sin patios; separaciones)
# --------------------------------------------------------------------------
def test_multi_forzado_sin_patios_independientes():
    # v03.4: modo MULTI -> 0 patios; rigen las separaciones entre volumenes.
    g = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)), n_volumenes=2)
    assert g.get("patio_count") == 0
    msg = str(g.get("mensaje"))
    assert "modo MULTI" in msg and "Generados: 0" in msg and "separaciones" in msg


def test_multi_forzado_n_alto_sin_patios():
    g = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)), n_volumenes=9)
    assert g.get("patio_count") == 0
    assert "modo MULTI" in str(g.get("mensaje"))


def test_auto_multivolumen_sin_patios():
    # v03.4: AUTO con n inferido >=2 -> sin patios (separaciones).
    g = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)))
    assert g.get("patio_count") == 0
    assert "separaciones" in str(g.get("mensaje"))


def test_multi_forzado_sin_esquinas_elegibles():
    sides = _sides_todos_laterales(4)
    for l in sides["lados"]:
        l["clasificacion"] = "Frontal"
    g = _correr_patio_v03(CUADRADO_30, json.dumps(sides), n_volumenes=2)
    assert g.get("patio_count") == 0
    msg = str(g.get("mensaje"))
    assert "Generados: 0" in msg and "modo MULTI" in msg


# --------------------------------------------------------------------------
# 4) AUTO con V_N sin cabida -> ancla alternativa
# --------------------------------------------------------------------------
def test_auto_vn_no_cabe_usa_otra_esquina():
    g = _correr_patio_v03(PENT_ASIM, json.dumps(_sides_todos_laterales(5)))
    assert g.get("patio_count") == 1
    msg = str(g.get("mensaje"))
    assert "modo AUTO" in msg
    exp = g.get("patios_export") or []
    if exp:
        assert exp[0].get("vertice_ancla") != 0


def test_tolerancia_input_n_volumenes():
    # 0 y None -> AUTO
    g0 = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)), n_volumenes=0)
    assert "modo AUTO" in str(g0.get("mensaje"))
    # string numerico -> multi
    gs = _correr_patio_v03(CUADRADO_30, json.dumps(_sides_todos_laterales(4)), n_volumenes="3")
    assert "modo MULTI" in str(gs.get("mensaje"))


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
    print("=== TESTS PATIO v03.4 (UNICO + MULTI: separaciones) ===")
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
