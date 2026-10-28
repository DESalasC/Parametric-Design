import re

data = open(r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.5.ghx', 'r', encoding='utf-8', errors='replace').read()

# Buscar objetos ConnectArchicad colocados
matches = re.findall(r'<Object name="ConnectArchicad"[^>]*>.*?</Object>', data, re.DOTALL)
print('ConnectArchicad placed objects:', len(matches))
for m in matches[:3]:
    guid = re.search(r'guid="([^"]+)"', m)
    print('  GUID:', guid.group(1) if guid else '?')

# Buscar valores de Port
ports = re.findall(r'name="Port"[^>]*>([^<]+)<', data)
print('Port values:', ports[:10] if ports else 'ninguno')

# Nombres de componentes ArchiCAD colocados
names = set(re.findall(r'name="(ConnectArchicad|ArchicadLocation|QuitArchicad|2D Polyline|2DC|Draw[^"]*|2D Curves[^"]*|Fill)"', data))
print('Nombres de componentes ArchiCAD:', sorted(names))

# Buscar puerto 19723 o 19724 en el GHX
for p in ['19723', '19724']:
    if p in data:
        print('Puerto', p, 'encontrado en GHX')
