import io, json, sys, types, os
sys.path.insert(0, r'D:\Work\PROJECTS\DiseñoParametrico\tests')
import stub_rhino_min as stub
rhino_mod = types.ModuleType('Rhino')
geo_mod = types.ModuleType('Rhino.Geometry')
for k in ('Point3d', 'Vector3d', 'Polyline', 'PolylineCurve', 'Line', 'AreaMassProperties', 'Brep', 'Curve', 'Intersect'):
    setattr(geo_mod, k, getattr(stub, k))
geo_mod.__stub_min__ = True
rhino_mod.Geometry = geo_mod
sys.modules['Rhino'] = rhino_mod
sys.modules['Rhino.Geometry'] = geo_mod

import math
P = geo_mod

def _lote_candelaria():
    return [(0.0, 0.0), (28.0, 0.0), (32.0, 12.0), (20.0, 34.0), (5.0, 30.0), (0.0, 18.0)]

def _make_lot_polygon():
    coords = _lote_candelaria()
    pts = [P.Point3d(x, y, 0.0) for (x, y) in coords]
    pts.append(P.Point3d(coords[0][0], coords[0][1], 0.0))
    return P.PolylineCurve(P.Polyline(pts))

def _sides_laterales_todos(n, vertice_n=0):
    lados = []
    for i in range(n):
        lados.append({'id': i, 'clasificacion': 'Lateral', 'motivo': 'test',
                      'dist_via_m': None, 'dist_ep_m': None, 'dist_vec_m': 0.0,
                      'toca_via': False, 'toca_ep': False, 'toca_vecino': True,
                      'comparte_a': i in (0, n - 1), 'comparte_n': i in (0, n - 1),
                      'dx': 1.0, 'dy': 0.0, 'mx': 0.0, 'my': 0.0})
    return {'lados': lados, 'total_lados': n, 'vertice_a': 0, 'vertice_n': vertice_n,
            'es_esquina': False, 'ancho_via_m': 12.0, 'chip': 'AAA0030JKOE', 'puente_lados_ok': True}

def _patio_esquina_simple():
    return [P.PolylineCurve(P.Polyline([P.Point3d(0,0,0), P.Point3d(3,0,0), P.Point3d(3,3,0), P.Point3d(0,3,0), P.Point3d(0,0,0)]))]

gvars = {
    'lot_polygon': _make_lot_polygon(),
    'sides_table_json': json.dumps(_sides_laterales_todos(6)),
    'patio_curves': _patio_esquina_simple(),
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
    'reglamentacion_json': '{"pot_data": {"tipologia": "Continua", "ancho_via_m": 12.0, "antejardin_m": 3.0}}',
    'normativa_confirmada': False,
    'pisos_maximos_total': 5,
    'vecinos_intervalos_json': '{"schema": "vecinos_intervalos_canvas_v02", "chip": "AAA0030JKOE", "lados": [{"id": 0, "es_colindancia_predial": false, "subtramos": []}, {"id": 1, "es_colindancia_predial": false, "subtramos": []}, {"id": 2, "es_colindancia_predial": false, "subtramos": []}, {"id": 3, "es_colindancia_predial": false, "subtramos": []}, {"id": 4, "es_colindancia_predial": false, "subtramos": []}, {"id": 5, "es_colindancia_predial": false, "subtramos": []}]}',
    'barras_json': None,
}

src = io.open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_ETAPA2_NORMATIVA_v09.py', encoding='utf-8').read()
ns = dict(gvars)
ns['__name__'] = 'gh_component_test'
exec(compile(src, 'F1_ETAPA2_NORMATIVA_v09.py', 'exec'), ns, ns)

print('=== DEBUG RETIROS_BASE ===')
print('retiros_base:', ns.get('retiros_base', 'NO HAY'))
print('antejardin:', ns.get('antejardin', 'NO HAY'))
print('retiro_lateral:', ns.get('retiro_lateral', 'NO HAY'))
print('retiro_posterior:', ns.get('retiro_posterior', 'NO HAY'))
print('pisos_finales:', ns.get('pisos_finales', 'NO HAY'))
print('floor_h:', ns.get('floor_h', 'NO HAY'))
print('tipologia:', ns.get('tipologia', 'NO HAY'))

print('\\n=== DEBUG SUBS PISO 1 ===')
# Let's manually trace _subsegmentos_piso for nv=1
from math import hypot
# We need to import the functions from the namespace
if 'retiros_base' in ns and 'lados' in ns:
    print('lados:', ns['lados'])
    print('vertices_lote count:', len(ns.get('vertices_lote', [])))