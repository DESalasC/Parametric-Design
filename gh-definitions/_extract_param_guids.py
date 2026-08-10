"""Extract real parameter GUIDs from v06."""
from lxml import etree

v06 = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx")

print("=== param_input InstanceGuids ===")
for pi in v06.findall('.//chunk[@name="param_input"]'):
    ig = pi.find('items/item[@name="InstanceGuid"]')
    name = pi.find('items/item[@name="Name"]')
    guid = ig.text[:12] if ig is not None else '?'
    nm = name.text if name is not None else '?'
    print(f"  {nm:20s} IG={guid}")

print("\n=== param_output InstanceGuids ===")
for po in v06.findall('.//chunk[@name="param_output"]'):
    ig = po.find('items/item[@name="InstanceGuid"]')
    name = po.find('items/item[@name="Name"]')
    guid = ig.text[:12] if ig is not None else '?'
    nm = name.text if name is not None else '?'
    print(f"  {nm:20s} IG={guid}")

# Look for all GUID-type items in param_input to understand what type-related GUIDs exist
print("\n=== ALL GUID items in first param_input ===")
first_pi = v06.find('.//chunk[@name="param_input"]')
if first_pi is not None:
    for item in first_pi.iter('item'):
        if item.get('type_name') == 'gh_guid':
            print(f"  name={item.get('name'):20s} value={item.text}")
