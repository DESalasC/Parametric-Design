with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Indent lines 293-392 (indices 292-391) by 4 spaces
for i in range(292, 392):
    if lines[i].strip():  # only indent non-empty lines
        lines[i] = '    ' + lines[i]

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed indentation')
