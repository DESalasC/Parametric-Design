# View lines around the reported error
with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_VOLUM_GENERADOR_v08.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Total lines:", len(lines))
print()

# Look specifically at the area mentioned in the error (around line 2060)
print("Lines 2055-2065:")
print("=" * 50)
for i in range(2054, min(2065, len(lines))):  # 2054 is line 2055 (0-indexed)
    line_num = i + 1
    content = lines[i].rstrip('\n\r')
    print(f"{line_num:4d}: {repr(content)}")

print()
print("Looking for the specific error pattern...")
print("=" * 50)

# Search for the problematic pattern mentioned in the error
for i in range(len(lines)):
    line_num = i + 1
    content = lines[i]
    if '_safe_json_dumps' in content and ('ensure_ascii=True' in content or 'ensure_ascii = True' in content):
        print(f"Found _safe_json_dumps at line {line_num}:")
        print(f"  {repr(content)}")
        # Show a few lines before and after for context
        start = max(0, i-2)
        end = min(len(lines), i+3)
        for j in range(start, end):
            marker = ">>> " if j == i else "    "
            ln = j + 1
            cnt = lines[j].rstrip('\n\r')
            print(f"{marker}{ln:4d}: {repr(cnt)}")
        print()