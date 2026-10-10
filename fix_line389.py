with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 389 (index 388) - add 4 more spaces to be inside the if block
lines[388] = '            ' + lines[388].lstrip()

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed')
