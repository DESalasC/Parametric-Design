"""Generate minimal test: single Panel from v06, verify in Grasshopper."""
from lxml import etree
import copy, subprocess

v06 = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx")
root = copy.deepcopy(v06.getroot())

# Get a Panel template
panel_template = None
for obj in v06.findall('.//chunk[@name="Object"]'):
    name_it = obj.find('items/item[@name="Name"]')
    if name_it is not None and name_it.text == 'Panel':
        panel_template = obj
        break

# Create new DefinitionObjects with just one Panel
panel_copy = copy.deepcopy(panel_template)
panel_copy.set('index', '0')

# Update InstanceGuid, UserText
for it in panel_copy.iter('item'):
    if it.get('name') == 'InstanceGuid':
        it.text = '11111111-1111-1111-1111-111111111111'
    elif it.get('name') == 'NickName':
        it.text = 'Test Panel'
    elif it.get('name') == 'UserText':
        it.text = 'Hello from v07 converter!'

new_defobjs = etree.Element('chunk', {'name': 'DefinitionObjects'})
items = etree.SubElement(new_defobjs, 'items', {'count': '1'})
etree.SubElement(items, 'item', {
    'name': 'ObjectCount', 'type_name': 'gh_int32', 'type_code': '3'
}).text = '1'
chunks = etree.SubElement(new_defobjs, 'chunks', {'count': '1'})
chunks.append(panel_copy)

# Replace
old_def = root.find('.//chunk[@name="DefinitionObjects"]')
parent = old_def.getparent()
parent.replace(old_def, new_defobjs)

# Write
output = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\test_panel.ghx"
xml_bytes = etree.tostring(root, encoding='utf-8', pretty_print=True, xml_declaration=True)
with open(output, 'wb') as f:
    f.write(xml_bytes)

print(f"Written: {output} ({len(xml_bytes)} bytes)")

# Validate
exe = r"D:\Work\LIBRARIES\GhDefinitionExplorer\bin\Release\net8.0\GhDefinitionExplorer.exe"
result = subprocess.run([exe, output, output.replace('.ghx', '.json')],
                       capture_output=True, text=True)
if "Error" in (result.stdout + result.stderr):
    print("GH_IO: FAILED")
    for line in (result.stdout + result.stderr).split('\n'):
        if 'Error' in line or 'error' in line.lower():
            print(f"  {line.strip()}")
else:
    print("GH_IO: OK")
