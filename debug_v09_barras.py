import sys
import os
import io
import json
import types

TESTS_DIR = os.path.dirname(os.path.abspath('tests/test_normativa_v09_fuente.py'))
BASE = os.path.abspath(os.path.join(TESTS_DIR, '..'))
NORMATIVA_V09 = os.path.join(BASE, 'src', 'fase-1-contexto', 'F1_ETAPA2_NORMATIVA_v09.py')

sys.path.insert(0, TESTS_DIR)

import stub_rhino_min as stub
rhino_mod = types.ModuleType('Rhino')
geo_mod = types.ModuleType('Rhino.Geometry')
for k in ('Point3d', 'Vector3d', 'Polyline', 'PolylineCurve', 'Line',
          'AreaMassProperties', 'Brep', 'Curve', 'Intersect'):
    setattr(geo_mod, k, getattr(stub, k))
geo_mod.__stub_min__ = True
rhino_mod.Geometry = geo_mod
sys.modules['Rhino'] = rhino_mod
sys.modules['Rhino.Geometry'] = geo_mod
STUB = geo_mod
P = STUB

def _lote_candelaria():
    return [
        (0.0, 0.0), (28.0, 0.0), (32.0, 12.0), (20.0, 34.0),
        (5.0, 30.0), (0.0, 18.0)
    ]

def _sides_laterales_todos(n, vertice_n=0):
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

gvars = {
    'lot_polygon': _make_lot_polygon(),
    'sides_table_json': json.dumps(_sides_laterales_todos(6)),
    'patio_curves': [],
    'altura_max_pot': 15.25,
    'tratamiento': 'Consolidacion',
    'rango_edificabilidad': '3',
    'floor_height_user': 3.05,
    'io_maximo_user': 0.0,
    'piso_adicional': False,
    'tipo_bonificacion': 'NINGUNO',
    'tipologia': 'Continua',
    'ancho_via_m': 12.0,
    'antejardin_m': 3.0,
    'empate_posterior_pisos': 0,
    'altura_vecinos_m': 0,
    'empate_lateral_min_m': 3.0,
    'nsr10_separacion_coef': 0.02,
    'voladizo_frontal_m': 0.0,
    'vecinos_por_lado_json': '{}',
    'frente_override_json': '{}',
    'reglamentacion_json': _make_reglamentacion(),
    'normativa_confirmada': False,
    'pisos_maximos_total': 5,
    'vecinos_intervalos_json': _make_vecinos_intervalos(),
    'barras_json': _make_barras_aprobado(),
}

src = io.open(NORMATIVA_V09, 'r', encoding='utf-8').read()
g = dict(gvars)
g['__name__'] = 'gh_component_test'
exec(compile(src, NORMATIVA_V09, 'exec'), g)

print('mensaje:', g.get('mensaje', 'NO MESSAGE'))
print('valido:', g.get('valido'))
print('bloqueos:', g.get('bloqueos', []))
print('presupuesto_ocupacion_m2:', g.get('presupuesto_ocupacion_m2'))
print('io_maximo:', g.get('io_maximo'))
print('area_lote:', g.get('area_lote'))
print('pisos_finales:', g.get('pisos_finales'))
print('altura_total:', g.get('altura_total'))
print('ocupacion_aprobada_m2:', g.get('ocupacion_aprobada_m2'))
print('gfa_aprobado_m2:', g.get('gfa_aprobado_m2'))
print('envelope_aprobado_por_piso:', g.get('envelope_aprobado_por_piso'))