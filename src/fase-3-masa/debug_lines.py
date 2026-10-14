# -*- coding: utf-8 -*-
"""Debug script to examine specific lines in F3_VOLUM_GENERADOR_v08.py"""
with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_VOLUM_GENERADOR_v08.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Show lines around 2060 (the error location)
start = max(0, 2050)
end = min(len(lines), 2070)

print(f"\nLines {start+1}-{end}:")
print("=" * 50)
for i in range(start, end):
    line_num = i + 1
    content = lines[i].rstrip('\n\r')
    # Show special characters
    if line_num >= 2055 and line_num <= 2065:
        print(f"{line_num:4d}: {repr(content)}")
    else:
        print(f"{line_num:4d}: {content}")

# Specifically check around line 2060
print(f"\nDetailed view of lines 2055-2065:")
print("=" * 50)
for i in range(2054, 2065):  # 0-indexed, so 2054 is line 2055
    if i < len(lines):
        line_num = i + 1
        content = lines[i].rstrip('\n\r')
        print(f"{line_num:4d}: {repr(content)}")