# -*- coding: utf-8 -*-
"""Extract and show CodeInput for #75-F3_VOLUM_GENERADOR_v08.py"""
import xml.etree.ElementTree as ET
import hashlib

BASE = r"D:\Work\PROJECTS\DiseñoParametrico"
GHX = BASE + r"\gh-definitions\F1_CONTEXTO_v13.2.ghx"

def items_dict(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d[i.get('name')] = (i.text or '').strip()
    return d

tree = ET.parse(GHX)
root = tree.getroot()
target_guid = "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d"
code_text = None
for o in root.iter('chunk'):
    if o.get('name') != 'Object':
        continue
    # find container
    for c in o.iter('chunk'):
        if c.get('name') == 'Container':
            d = items_dict(c)
            if d.get('InstanceGuid', '') == target_guid:
                # found object, now find CodeInput item
                for i in o.iter('item'):
                    if i.get('name') == 'CodeInput':
                        code_text = i.text
                        break
                break
    if code_text is not None:
        break

if code_text is None:
    print("ERROR: CodeInput not found")
    exit(1)

print("Length:", len(code_text))
print("SHA1:", hashlib.sha1(code_text.encode('utf-8')).hexdigest())
print()
print("=== FIRST 10 LINES ===")
for i, line in enumerate(code_text.splitlines()[:10]):
    print(f"{i:2}: {line}")
print()
print("=== LAST 10 LINES ===")
lines = code_text.splitlines()
for i, line in enumerate(lines[-10:], start=len(lines)-10):
    print(f"{i:2}: {line}")
print()
print("=== AROUND LINE WHERE WE INSERT ===")
# look for zonas_atributos.append
for i, line in enumerate(lines):
    if 'zonas_atributos.append' in line and 'py_json.dumps' in line:
        print(f"Found at line {i}: {line.strip()}")
        # show context
        for j in range(max(0, i-2), min(len(lines), i+5)):
            prefix = ">>> " if j == i else "    "
            print(f"{prefix}{j:4}: {lines[j]}")
        break