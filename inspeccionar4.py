p = r'D:\Work\PROJECTS\DiseñoParametrico\src\orquestador\index.html'
with open(p, encoding='utf-8') as f:
    txt = f.read()

# Buscar el texto suelto
idx = txt.find('div style="margin-top:14px;">')
print('Texto suelto en posición:', idx)
if idx >= 0:
    print(txt[max(0,idx-200):idx+200])

# Buscar bloques_num
idx2 = txt.find('bloques_num')
print()
print('bloques_num en posición:', idx2)
if idx2 >= 0:
    print(txt[max(0,idx2-300):idx2+300])

# Buscar la sección 4 (niveles-bloque-card)
idx3 = txt.find('niveles-bloque-card')
print()
print('niveles-bloque-card en posición:', idx3)
