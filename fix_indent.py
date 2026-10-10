with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix line 388 - it should be indented under else: on line 387
# Line 387 is '    else:\n' (4 spaces)
# Line 388 should be '        if not matriz:\n' (8 spaces)
lines[387] = '        if not matriz:\n'

# Also need to indent the rest of the block until the outer else:
# Lines 389-397 should be at 8 spaces (inside the inner else)
for i in range(388, 397):
    if lines[i].strip() and not lines[i].startswith('        '):
        lines[i] = '    ' + lines[i]

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed inner else block')
