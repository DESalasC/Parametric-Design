with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Parsea entrada JSON' in line and line.count('\"\"\"') > 1:
        print('Line {}: {}'.format(i+1, repr(line)))
        lines[i] = '    \"\"\"Parsea entrada JSON: string, archivo .json, o dict/list ya parseado.\"\"\"\n'
        break

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed')
