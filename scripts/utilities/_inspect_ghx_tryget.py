import re

data = open(r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.5.ghx', 'r', encoding='utf-8', errors='replace').read()

# Buscar TryGetPolyline en el GHX
idx = data.find('TryGetPolyline')
if idx >= 0:
    print('TryGetPolyline encontrado en posicion', idx)
    print(data[max(0, idx-500):idx+500])
else:
    print('TryGetPolyline NO encontrado en el GHX')

# Buscar el script del componente fuente 0d986a36
matches = re.findall(r'<Object name="GH_Python"[^>]*>.*?</Object>', data, re.DOTALL)
print('Componentes GH_Python:', len(matches))

for i, m in enumerate(matches):
    if '0d986a36' in m:
        print(f'Componente fuente {i}: encontrado')
        # Extraer nickname
        nick_match = re.search(r'name="NickName"[^>]*>(.*?)</item>', m)
        if nick_match:
            print('  NickName:', nick_match.group(1))
        # Extraer script
        script_match = re.search(r'name="Script"[^>]*>(.*?)</item>', m, re.DOTALL)
        if script_match:
            script = script_match.group(1)
            print('  Script length:', len(script))
            # Buscar TryGetPolyline en el script
            tg_idx = script.find('TryGetPolyline')
            if tg_idx >= 0:
                print('  TryGetPolyline en script:')
                print(script[max(0, tg_idx-300):tg_idx+300])
        break
