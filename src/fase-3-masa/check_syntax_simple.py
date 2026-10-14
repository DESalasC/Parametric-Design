# -*- coding: utf-8 -*-
"""Check syntax around the reported error location"""
import ast
import sys

file_path = r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_VOLUM_GENERADOR_v08.py'

print("Checking syntax of:", file_path)

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to parse the entire file
    tree = ast.parse(content)
    print("OK: File parses successfully with AST")
    
except SyntaxError as e:
    print("ERROR: SyntaxError:", str(e))
    print("  Line:", e.lineno)
    if e.text:
        print("  Text:", e.text)
    if e.offset:
        print("  Offset:", e.offset)
        
    # Show context around the error
    lines = content.splitlines()
    start = max(0, e.lineno - 10)
    end = min(len(lines), e.lineno + 10)
    
    print("\nContext around line", e.lineno, ":")
    print("=" * 50)
    for i in range(start, end):
        marker = ">>> " if i == e.lineno - 1 else "    "
        line_num = i + 1
        line_content = lines[i]
        print(marker + str(line_num).rjust(4) + ": " + line_content)
        
except Exception as e:
    print("ERROR: Other error:", str(e))

# Also check specifically around line 2060 as mentioned in the error
print("\n" + "="*50)
print("Checking lines 2055-2065 specifically:")
print("="*50)

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    start_idx = max(0, 2055 - 1)  # Convert to 0-indexed
    end_idx = min(len(lines), 2065)
    
    for i in range(start_idx, end_idx):
        line_num = i + 1
        content = lines[i].rstrip('\n\r')
        # Show non-printable characters
        if line_num >= 2055 and line_num <= 2065:
            print(str(line_num).rjust(4) + ": " + repr(content))
        else:
            print(str(line_num).rjust(4) + ": " + content)
            
except Exception as e:
    print("Error reading file:", str(e))