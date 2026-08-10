"""Compare Group object between v06 and v6.1 output."""
from lxml import etree

v06 = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx")
v07 = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx")

# Get first Group from each
for label, tree in [("v06", v06), ("v6.1", v07)]:
    for obj in tree.findall('.//chunk[@name="Object"]'):
        name_it = obj.find('items/item[@name="Name"]')
        if name_it is not None and name_it.text == 'Group':
            print(f"\n{'='*60}")
            print(f"=== GROUP from {label} ===")
            print(f"{'='*60}")
            xml = etree.tostring(obj, encoding='unicode', pretty_print=True)
            print(xml[:3000])
            break
