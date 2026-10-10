with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the if _es_gh block and else
start_gh = -1
else_line = -1
for i, line in enumerate(lines):
    if 'if _es_gh:' in line and i > 290:
        start_gh = i
    if start_gh != -1 and line.strip() == 'else:' and i > start_gh:
        else_line = i
        break

print('GH block starts at line', start_gh+1)
print('else at line', else_line+1)

# Check indentation of lines in this range
for i in range(start_gh+1, else_line):
    if lines[i].strip() and not lines[i].startswith('    '):
        print('Line', i+1, 'not indented:', repr(lines[i][:80]))
