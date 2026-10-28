import json

with open(r'D:\Work\PROJECTS\DiseñoParametrico\data\pot-cache\CHIP-contexto.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print('=== lote_objetivo ===')
lo = d.get('lote_objetivo', {})
for k, v in lo.items():
    if k in ('vertices', 'vertices_3d_local', 'area_m2', 'perimetro_m'):
        print(f'  {k}: {len(v) if isinstance(v, list) else v}')

print('=== vecinos ===')
vecinos = d.get('vecinos', [])
print('  n:', len(vecinos))
for v in vecinos[:2]:
    vid = v.get('id', '?')
    nverts = len(v.get('vertices', []))
    nverts3d = len(v.get('vertices_3d_local', []))
    print(f'  {vid}: vertices={nverts}, vertices_3d_local={nverts3d}')

print('=== vias_oficiales ===')
vias = d.get('vias_oficiales', [])
print('  n:', len(vias))
for v in vias[:2]:
    vid = v.get('id', '?')
    nverts = len(v.get('vertices', []))
    print(f'  {vid}: vertices={nverts}')

print('=== espacios_publicos ===')
eps = d.get('espacios_publicos', [])
print('  n:', len(eps))
for e in eps[:2]:
    eid = e.get('id', '?')
    nverts = len(e.get('vertices', []))
    print(f'  {eid}: vertices={nverts}')

print('=== topografia ===')
topo = d.get('topografia', {})
for k, v in topo.items():
    if isinstance(v, list):
        print(f'  {k}: {len(v)} puntos')
    else:
        print(f'  {k}: {v}')

print('=== metadata ===')
print(json.dumps(d.get('metadata', {}), indent=2, ensure_ascii=False)[:500])
