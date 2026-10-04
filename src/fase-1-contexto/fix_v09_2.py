with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_ETAPA2_NORMATIVA_v09.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the redundant inline calculation - simplify to use io_maximo
old = 'presupuesto_ocupacion_m2 = area_lote * io_maximo if io_user > 0 else area_lote * (0.70 if tratamiento == "Consolidacion" else 0.60 if tratamiento in ("Desarrollo","Mejoramiento") else 0.70)'
new = 'presupuesto_ocupacion_m2 = area_lote * io_maximo'

if old in content:
    content = content.replace(old, new)
    with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_ETAPA2_NORMATIVA_v09.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Reemplazo exitoso')
else:
    print('No se encontró el patrón exacto')
    # Show what's there
    idx = content.find('presupuesto_ocupacion_m2 = area_lote')
    if idx >= 0:
        print('Encontrado en:', idx)
        print(repr(content[idx:idx+150]))