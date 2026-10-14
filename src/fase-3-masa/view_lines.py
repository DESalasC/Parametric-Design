# Simple script to view specific lines
lines = []
with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_VOLUM_GENERADOR_v08.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines:", len(lines))
print()
print("Lines 2050-2070:")
print("-" * 40)
for i in range(2049, min(2070, len(lines))):  # 0-indexed, so 2049 is line 2050
    line_num = i + 1
    content = lines[i].rstrip('\\n\\r')
    print(f"{line_num:4d}: {repr(content)}")