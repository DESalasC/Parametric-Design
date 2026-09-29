# -*- coding: utf-8 -*-
"""Arnés: ejecuta F1_ETAPA2_LADOS_v06.py + F1_ETAPA2_PATIO_v02.py con datos
   reales del chip AAA0240ZXJH (stubs de Rhino en CPython)."""
import io
import json
import math
import os
import sys
import types

# Anexo autocontenido: usa la carpeta del propio script para el stub y las salidas.
TMP = os.path.dirname(os.path.abspath(__file__))
BASE = r'D:\Work\PROJECTS\DiseñoParametrico'
CTX = os.path.join(BASE, 'data', 'pot-cache', 'AAA0240ZXJH-contexto.json')

# ---- instalar stub Rhino.Geometry ----
sys.path.insert(0, TMP)
import stub_rg

rhino_mod = types.ModuleType('Rhino')
geo_mod = types.ModuleType('Rhino.Geometry')
for k in ('Point3d', 'Vector3d', 'Polyline', 'PolylineCurve', 'Line'):
    setattr(geo_mod, k, getattr(stub_rg, k))
geo_mod.Intersect = stub_rg.Intersect
rhino_mod.Geometry = geo_mod
sys.modules['Rhino'] = rhino_mod
sys.modules['Rhino.Geometry'] = geo_mod

P = stub_rg

# NOTA (post-fix 2026-09-28): el componente LADOS v06.5 ya define
# point_in_lot; la inyeccion de abajo se mantiene como referencia historica
# y ya no altera la corrida (la definicion del componente prevalece).
INJECT_FIX = '''
def point_in_lot(pt, vertices):
    n = len(vertices)
    if n < 3: return False
    px, py = pt.X, pt.Y
    count = 0
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        if ((v1.Y > py) != (v2.Y > py)):
            if (v2.Y - v1.Y) != 0:
                x_int = v1.X + (py - v1.Y) * (v2.X - v1.X) / (v2.Y - v1.Y)
                if px < x_int:
                    count += 1
    if (count % 2) == 1:
        return True
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        dx = v2.X - v1.X
        dy = v2.Y - v1.Y
        l2 = dx * dx + dy * dy
        if l2 < 1e-12:
            continue
        t = ((px - v1.X) * dx + (py - v1.Y) * dy) / l2
        t = max(0.0, min(1.0, t))
        cx = v1.X + t * dx
        cy = v1.Y + t * dy
        if math.sqrt((px - cx) ** 2 + (py - cy) ** 2) < 0.1:
            return True
    return False
'''

def load_sources():
    d = json.load(io.open(CTX, 'r', encoding='utf-8'))
    lot = [(v[0], v[1]) for v in d['lote_objetivo']['vertices_3d_local']]
    # quitar punto de cierre duplicado
    if len(lot) > 1 and abs(lot[0][0] - lot[-1][0]) < 1e-9 and abs(lot[0][1] - lot[-1][1]) < 1e-9:
        lot = lot[:-1]
    vias = d['vias_oficiales']
    vecinos = d['vecinos']
    eps = d['espacios_publicos']
    return d, lot, vias, vecinos, eps

def curve_from_coords(coords):
    pts = [P.Point3d(c[0], c[1], c[2] if len(c) > 2 else 0.0) for c in coords]
    # quitar cierre duplicado para polilineas cerradas
    if len(pts) > 1 and pts[0].DistanceTo(pts[-1]) < 1e-9:
        pts = pts[:-1]
    poly = P.Polyline()
    for p in pts:
        poly.Add(p)
    return P.PolylineCurve(poly)

def run_component(src_path, gvars, inject_fix=True):
    src = io.open(src_path, 'r', encoding='utf-8').read()
    g = dict(gvars)
    g['__name__'] = 'gh_component'
    if inject_fix:
        exec(compile(INJECT_FIX, '<inject>', 'exec'), g)
    exec(compile(src, src_path, 'exec'), g)
    return g

log = io.open(os.path.join(TMP, 'harness_out.txt'), 'w', encoding='utf-8')
def w(s=''):
    log.write(s + '\n')

d, lot, vias_raw, vecinos_raw, eps_raw = load_sources()
w('CHIP: ' + str(d['metadata']['chip']))
w('Lote: {} vertices (sin cierre)'.format(len(lot)))

LADOS = os.path.join(BASE, 'src', 'fase-1-contexto', 'F1_ETAPA2_LADOS_v06.py')
PATIO = os.path.join(BASE, 'src', 'fase-1-contexto', 'F1_ETAPA2_PATIO_v02.py')

def ejecutar_caso(nombre, lot_pts, usar_vias, usar_vecinos, usar_ep, altura=11.4, inject_fix=True):
    w()
    w('#' * 100)
    w('# CASO: {} | lot_pts={} | vias={} | vecinos={} | ep={}'.format(
        nombre, len(lot_pts), len(usar_vias), len(usar_vecinos), len(usar_ep)))
    w('#' * 100)

    lot_stub = [P.Point3d(p[0], p[1], 0.0) for p in lot_pts]
    vias_stub = [curve_from_coords(v['coordenadas_local']) for v in usar_vias if v.get('coordenadas_local')]
    vec_stub = [curve_from_coords(v['vertices_3d_local']) for v in usar_vecinos if v.get('vertices_3d_local')]
    ep_stub = [curve_from_coords(v['coordenadas_local']) for v in usar_ep if v.get('coordenadas_local')]

    g1 = run_component(LADOS, {
        'lot_vertices': lot_stub,
        'vias_curves': vias_stub,
        'ep_curves': ep_stub,
        'vecinos_curves': vec_stub,
        'andenes_curves': [],
    }, inject_fix=inject_fix)
    w('--- LADOS mensaje ---')
    w(str(g1.get('mensaje')))
    sides = None
    try:
        sides = json.loads(g1.get('sides_table_json') or '{}')
    except Exception as e:
        w('ERROR parse sides: {}'.format(e))

    if sides:
        w('V_A={} V_N={} es_esquina={} ancho={}'.format(
            sides.get('vertice_a'), sides.get('vertice_n'),
            sides.get('es_esquina'), sides.get('ancho_via_m')))
        w('vertice_n_points: {} -> {}'.format(
            len(sides.get('vertice_n_points') or []), sides.get('vertice_n_points')))
        w('vertice_n_method: {}'.format(sides.get('vertice_n_method')))
        w('--- lados ---')
        for l in sides['lados']:
            p1 = lot_pts[l['id']]
            p2 = lot_pts[(l['id'] + 1) % len(lot_pts)]
            L = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
            w('  L{} [{:6.2f}m] {:12s} | {:34s} | fr v/e/n={:.2f}/{:.2f}/{:.2f} | d v/e/n={}/{}/{} | compA={} compN={}'.format(
                l['id'], L, l['clasificacion'], l.get('motivo', '')[:34],
                l['frac_via_m'], l['frac_ep_m'], l['frac_vec_m'],
                l.get('dist_via_m'), l.get('dist_ep_m'), l.get('dist_vec_m'),
                l['comparte_a'], l['comparte_n']))

        g2 = run_component(PATIO, {
            'lot_vertices': lot_stub,
            'sides_table_json': g1.get('sides_table_json'),
            'altura_max_pot': altura,
        })
        w('--- PATIO mensaje ---')
        w(str(g2.get('mensaje')))
        patios = g2.get('patios_curves') or []
        w('patios generados: {}'.format(g2.get('patio_count')))
        for k, cr in enumerate(patios):
            pts = cr._pts if hasattr(cr, '_pts') else []
            w('  patio {}: {} pts: {}'.format(k, len(pts),
                ' '.join('({:.2f},{:.2f})'.format(p.X, p.Y) for p in pts)))
            # area shoelace
            ar = 0.0
            for i in range(len(pts) - 1):
                ar += pts[i].X * pts[i + 1].Y - pts[i + 1].X * pts[i].Y
            w('  area: {:.3f} m2'.format(abs(ar) / 2.0))
            # validar interioridad de la esquina
            pin = g2.get('point_in_lot')
            if pin:
                allin = all(pin(p, lot_stub) for p in pts[:-1])
                w('  todos los vertices dentro del lote: {}'.format(allin))

    # resumen distancias por lado (para interpretacion)
    return sides

# ---- CASO A0: corrida directa del script tal como esta en el repo ----
ejecutar_caso('A0 | lote 13v + 67 vias (directo)', lot, vias_raw, vecinos_raw, eps_raw, inject_fix=False)

# ---- CASO A: lote completo (13 vertices) con TODOS los vecinos/vias/ep ----
sides13 = ejecutar_caso('A | lote 13v + insumos completos', lot, vias_raw, vecinos_raw, eps_raw)

# ---- CASO B: lote 4 esquinas (v0 v1 v3 v7) con insumos completos ----
# indices: v0=(89.847,80.616) v1=(84.877,75.0) v3=(75,83.907) v7=(79.97,89.523)
lot4 = [lot[0], lot[1], lot[3], lot[7]]
sides4 = ejecutar_caso('B | lote 4 esquinas + insumos completos', lot4, vias_raw, vecinos_raw, eps_raw)

# ---- CASO C: lote 13v + subconjunto cercano (simula clasificacion manual) ----
def min_d_lote(v):
    ds = []
    for c in (v.get('coordenadas_local') or v.get('vertices_3d_local') or []):
        for i in range(len(lot)):
            a = lot[i]; b = lot[(i + 1) % len(lot)]
            ax, ay = a; bx, by = b; px, py = c[0], c[1]
            dx = bx - ax; dy = by - ay
            l2 = dx * dx + dy * dy
            if l2 < 1e-12:
                d = math.hypot(px - ax, py - ay)
            else:
                tt = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / l2))
                d = math.hypot(px - (ax + tt * dx), py - (ay + tt * dy))
            ds.append(d)
    return min(ds) if ds else 1e9

vias30 = [v for v in vias_raw if min_d_lote(v) <= 30]
vec30 = [v for v in vecinos_raw if min_d_lote(v) <= 30]
ep60 = [v for v in eps_raw if min_d_lote(v) <= 60]
ejecutar_caso('C | lote 13v + vias<=30m vecinos<=30m', lot, vias30, vec30, ep60)

log.close()
print('OK ->', os.path.join(TMP, 'harness_out.txt'))
