# -*- coding: utf-8 -*-
"""Test de F1_ETAPA2_NORMATIVA_v09.py — Validador de barras y presupuesto IO.

Ejecuta el componente REAL en CPython con stub mínimo de Rhino.Geometry.
Cubre:
  1) Modo POTENCIAL (sin barras_json): comportamiento v08 compatible.
  2) Modo APROBADO (con barras_json válido): certifica ocupación ≤ presupuesto.
  3) Modo APROBADO RECHAZADO (barras_json excede presupuesto): bloquea.
  4) Exposición de presupuesto_ocupacion_m2 siempre.
  5) Salidas aprobadas: ocupacion_aprobada_m2, gfa_aprobado_m2, envelope_aprobado_por_piso.
"""
import io
import json
import math
import os
import sys
import types

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(TESTS_DIR, ".."))
NORMATIVA_V09 = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_NORMATIVA_v09.py")

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


STUB = _instalar_stub()
P = STUB


def _ejecutar(path, gvars):
    src = io.open(path, "r", encoding="utf-8").read()
    g = dict(gvars)
    g["__name__"] = "gh_component_test"
    exec(compile(src, path, "exec"), g)
    return g


def _lote_candelaria():
    # Aproximación del lote AAA0030JKOE: ~946 m², forma irregular
    return [
        (0.0, 0.0), (28.0, 0.0), (32.0, 12.0), (20.0, 34.0),
        (5.0, 30.0), (0.0, 18.0)
    ]


def _sides_laterales_todos(n, vertice_n=0):
    # Simular lote con 2 frentes (Oriente=Frontal, Occidente=ViaNoPrincipal), 2 laterales, 1 posterior
    # Para n=6 lados, asignar: 0=Frontal, 1=Lateral, 2=ViaNoPrincipal, 3=Lateral, 4=Posterior, 5=Lateral
    clasificaciones = ['Frontal', 'Lateral', 'EspacioPublico', 'Lateral', 'Posterior', 'Lateral']
    lados = []
    for i in range(n):
        cls = clasificaciones[i] if i < len(clasificaciones) else 'Lateral'
        lados.append({'id': i, 'clasificacion': cls, 'motivo': 'test',
                      'dist_via_m': 10.0 if cls in ('Frontal', 'EspacioPublico') else None,
                      'dist_ep_m': None, 'dist_vec_m': 5.0 if cls in ('Lateral', 'Posterior') else None,
                      'toca_via': cls in ('Frontal', 'EspacioPublico'),
                      'toca_ep': False,
                      'toca_vecino': cls in ('Lateral', 'Posterior'),
                      'comparte_a': i in (0, n - 1), 'comparte_n': i in (0, n - 1),
                      'dx': 1.0, 'dy': 0.0, 'mx': 0.0, 'my': 0.0})
    return {'lados': lados, 'total_lados': n, 'vertice_a': 0, 'vertice_n': vertice_n,
            'es_esquina': False, 'ancho_via_m': 12.0, 'chip': 'AAA0030JKOE',
            'puente_lados_ok': True}


def _patio_esquina_simple():
    # Patio pequeño en V0 (3x3 = 9 m²)
    return [P.PolylineCurve(P.Polyline([P.Point3d(0,0,0), P.Point3d(3,0,0), P.Point3d(3,3,0), P.Point3d(0,3,0), P.Point3d(0,0,0)]))]


def _make_lot_polygon():
    coords = _lote_candelaria()
    pts = [P.Point3d(x, y, 0.0) for (x, y) in coords]
    pts.append(P.Point3d(coords[0][0], coords[0][1], 0.0))
    return P.PolylineCurve(P.Polyline(pts))


def _make_vecinos_intervalos():
    return '{"schema": "vecinos_intervalos_canvas_v02", "chip": "AAA0030JKOE", "lados": [{"id": 0, "es_colindancia_predial": false, "subtramos": []}, {"id": 1, "es_colindancia_predial": false, "subtramos": []}, {"id": 2, "es_colindancia_predial": false, "subtramos": []}, {"id": 3, "es_colindancia_predial": false, "subtramos": []}, {"id": 4, "es_colindancia_predial": false, "subtramos": []}, {"id": 5, "es_colindancia_predial": false, "subtramos": []}]}'


def _make_reglamentacion():
    return '{"pot_data": {"tipologia": "Continua", "ancho_via_m": 12.0, "antejardin_m": 3.0}}'


def _make_barras_aprobado():
    """barras_json con 2 barras, ocupación 300 m² (bajo presupuesto 662.44)"""
    d = {
        "schema": "f3_barras_salida_v01",
        "chip": "AAA0030JKOE",
        "alternativas": [
            {
                "id": "ALT-2B-305",
                "n_barras": 2, "crujia": "unica", "profundidad_m": 10.5,
                "separacion_m": 8.2, "floor_h": 3.05, "altura_total_m": 15.25,
                "huellas_por_piso": [
                    [  # Piso 1: 2 barras
                        [[0,0], [15,0], [15,10], [0,10], [0,0]],
                        [[20,0], [35,0], [35,10], [20,10], [20,0]]
                    ],
                    [  # Piso 2
                        [[0,0], [15,0], [15,10], [0,10], [0,0]],
                        [[20,0], [35,0], [35,10], [20,10], [20,0]]
                    ]
                ],
                "areas_por_piso": [[150.0, 150.0], [150.0, 150.0]],
                "ocupacion_total_m2": 300.0,
                "gfa_real_m2": 1500.0,
                "separaciones_validas": True,
                "patio_tipo": "separacion_entre_volumenes",
                "accesos_ok": True
            }
        ],
        "recomendada": "ALT-2B-305",
        "mensaje": "Test aprobado"
    }
    return json.dumps(d)


def _make_barras_rechazado():
    """barras_json con ocupación 700 m² > presupuesto 662.44"""
    d = {
        "schema": "f3_barras_salida_v01",
        "chip": "AAA0030JKOE",
        "alternativas": [
            {
                "id": "ALT-2B-BAD",
                "n_barras": 2, "ocupacion_total_m2": 700.0, "gfa_real_m2": 3500.0,
                "huellas_por_piso": [
                    [[[0,0], [20,0], [20,17.5], [0,17.5], [0,0]]]
                ],
                "areas_por_piso": [[700.0]],
                "separaciones_validas": True, "patio_tipo": "separacion_entre_volumenes", "accesos_ok": True
            }
        ],
        "recomendada": "ALT-2B-BAD"
    }
    return json.dumps(d)


def _base_gvars(barras_json_str=None):
    return {
        "lot_polygon": _make_lot_polygon(),
        "sides_table_json": json.dumps(_sides_laterales_todos(6)),
        "patio_curves": [],
        "altura_max_pot": 15.25,
        "tratamiento": "Consolidacion",
        "rango_edificabilidad": "3",
        "floor_height_user": 3.05,
        "io_maximo_user": 0.0,
        "piso_adicional": False,
        "tipo_bonificacion": "NINGUNO",
        "tipologia": "Continua",
        "ancho_via_m": 12.0,
        "antejardin_m": 3.0,
        "empate_posterior_pisos": 0,
        "altura_vecinos_m": 0,
        "empate_lateral_min_m": 3.0,
        "nsr10_separacion_coef": 0.02,
        "voladizo_frontal_m": 0.0,
        "vecinos_por_lado_json": "{}",
        "frente_override_json": "{}",
        "reglamentacion_json": _make_reglamentacion(),
        "normativa_confirmada": False,
        "pisos_maximos_total": 5,
        "vecinos_intervalos_json": _make_vecinos_intervalos(),
        "barras_json": barras_json_str,
    }


# ============================================================
# 1) MODO POTENCIAL (sin barras_json) — compatibilidad v08
# ============================================================
def test_modo_potencial_sin_barras():
    gvars = _base_gvars(barras_json_str=None)
    gvars["patio_curves"] = _patio_esquina_simple()
    g = _ejecutar(NORMATIVA_V09, gvars)
    # Debe ejecutarse en modo POTENCIAL
    assert "POTENCIAL" in g.get("mensaje", "")
    assert "presupuesto_ocupacion_m2" in g
    presupuesto = g.get("presupuesto_ocupacion_m2")
    assert presupuesto is not None and abs(presupuesto - 662.44) < 1.0  # 0.70 * ~946
    # Salidas aprobadas deben ser 0 (no hay barras_json)
    assert g.get("ocupacion_aprobada_m2", 1) == 0.0
    assert g.get("gfa_aprobado_m2", 1) == 0.0
    assert g.get("envelope_aprobado_por_piso", [1]) == []


# ============================================================
# 2) MODO APROBADO (barras_json válido dentro de presupuesto)
# ============================================================
def test_modo_aprobado_barras_dentro_presupuesto():
    gvars = _base_gvars(barras_json_str=_make_barras_aprobado())
    g = _ejecutar(NORMATIVA_V09, gvars)
    assert "APROBADO" in g.get("mensaje", "")
    assert g.get("valido") == True
    assert abs(g.get("ocupacion_aprobada_m2", 0) - 300.0) < 0.01
    assert abs(g.get("gfa_aprobado_m2", 0) - 1500.0) < 0.01
    assert g.get("envelope_aprobado_por_piso") is not None
    assert len(g.get("envelope_aprobado_por_piso", [])) == 2  # 2 pisos en el test


# ============================================================
# 3) MODO APROBADO RECHAZADO (barras_json EXCEDE presupuesto)
# ============================================================
def test_modo_aprobado_rechazado_excede_presupuesto():
    gvars = _base_gvars(barras_json_str=_make_barras_rechazado())
    g = _ejecutar(NORMATIVA_V09, gvars)
    # Debe fallar validación: valido=False, bloqueo por excedente
    assert g.get("valido") == False
    msg = g.get("mensaje", "")
    assert "NO VALIDADO" in msg
    assert "excedente" in msg or "presupuesto" in msg


# ============================================================
# 4) Presupuesto siempre expuesto
# ============================================================
def test_presupuesto_siempre_expuesto():
    gvars = _base_gvars(barras_json_str=None)
    g = _ejecutar(NORMATIVA_V09, gvars)
    assert "presupuesto_ocupacion_m2" in g
    p = g["presupuesto_ocupacion_m2"]
    assert p is not None and p > 0


# ============================================================
# 5) Versión interna = v09.0 en mensaje
# ============================================================
def test_version_interna_v09():
    gvars = _base_gvars(barras_json_str=None)
    g = _ejecutar(NORMATIVA_V09, gvars)
    assert "v09.0" in g.get("mensaje", "")


if __name__ == "__main__":
    print("=== TESTS NORMATIVA v09 (VALidadOR BARRAS) ===")
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
            print("  [FAIL]", test.__name__, "->", str(e)[:400])
    print("=== RESULTADO: {} pasaron, {} fallaron ===".format(passed, failed))
    if failed:
        sys.exit(1)