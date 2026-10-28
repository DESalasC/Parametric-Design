import re

data = open(r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.5.ghx', 'r', encoding='utf-8', errors='replace').read()

# Buscar componentes GH_Python
matches = re.findall(r'<Object name="GH_Python"[^>]*>.*?</Object>', data, re.DOTALL)
print('Componentes GH_Python:', len(matches))

for m in matches:
    if '0d986a36' in m:
        print('Encontrado componente fuente (0d986a36)')
        # Buscar el script dentro
        script_match = re.search(r'name="Script"[^>]*>(.*?)</item>', m, re.DOTALL)
        if script_match:
            script = script_match.group(1)
            print('Script length:', len(script))
            print(script[:5000])
        break
