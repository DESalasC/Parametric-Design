"""Test full replacement pipeline: v06 root + new DefObjs."""
from lxml import etree
import copy

v06 = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx")
root_copy = copy.deepcopy(v06.getroot())

# Build a minimal new DefinitionObjects
new_defobjs = etree.Element('chunk', {'name': 'DefinitionObjects'})
items = etree.SubElement(new_defobjs, 'items', {'count': '1'})
etree.SubElement(items, 'item', {
    'name': 'ObjectCount', 'type_name': 'gh_int32', 'type_code': '3'
}).text = '3'

chunks = etree.SubElement(new_defobjs, 'chunks', {'count': '3'})

# Take 3 objects from v06 (Group, Panel, Python)
for i in range(3):
    src = list(v06.findall('.//chunk[@name="Object"]'))[i]
    c = copy.deepcopy(src)
    c.set('index', str(i))
    chunks.append(c)

# Replace
old_def = root_copy.find('.//chunk[@name="DefinitionObjects"]')
parent = old_def.getparent()
print(f"Parent tag: {parent.tag}, name: {parent.get('name', 'n/a')}")

# parent is a 'chunk' named 'Definition' (from looking at structure)
# But what if it's actually a 'chunks' element?
# Let me check the actual hierarchy
grandparent = parent.getparent()
print(f"Grandparent tag: {grandparent.tag}, name: {grandparent.get('name', 'n/a')}")
great_grandparent = grandparent.getparent()
print(f"Great-grandparent tag: {great_grandparent.tag}")

parent.replace(old_def, new_defobjs)

# Serialize
s = etree.tostring(root_copy, encoding='utf-8', xml_declaration=True).decode('utf-8')
print(f"\nSerialized: {len(s)} bytes")

# Re-parse
try:
    reparsed = etree.fromstring(s.encode('utf-8') if isinstance(s, str) else s)
    defobjs = reparsed.find('.//chunk[@name="DefinitionObjects"]')
    if defobjs is not None:
        objs = list(defobjs.findall('.//chunk[@name="Object"]'))
        print(f"Objects in reparsed: {len(objs)}")
        for o in objs:
            name_it = o.find('items/item[@name="Name"]')
            print(f"  - {name_it.text if name_it is not None else '?'}")
except Exception as e:
    print(f"RE-PARSE ERROR: {e}")

# Write and validate with GhDefinitionExplorer
output = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\_test_replace.ghx"
with open(output, 'wb') as f:
    f.write(s.encode('utf-8'))

print("\n--- Validating with GhDefinitionExplorer ---")
import subprocess
exe = r"D:\Work\LIBRARIES\GhDefinitionExplorer\bin\Release\net8.0\GhDefinitionExplorer.exe"
result = subprocess.run([exe, output, output.replace('.ghx', '.json')],
                       capture_output=True, text=True)
if "Error" in (result.stdout + result.stderr):
    print("FAILED")
    for line in (result.stdout + result.stderr).split('\n'):
        if 'Error' in line or 'error' in line.lower():
            print(f"  {line.strip()}")
else:
    print("VALIDATION OK")
