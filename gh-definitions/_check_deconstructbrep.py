"""Check DeconstructBrep params in test_06."""
from lxml import etree
t = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\tests\core\test_06_plugin_component.ghx")

for obj in t.findall('.//chunk[@name="Object"]'):
    name = obj.find('items/item[@name="Name"]')
    if name is None or name.text != 'Deconstruct Brep':
        continue
    print("=== Deconstruct Brep FULL ===")
    xml = etree.tostring(obj, encoding='unicode', pretty_print=True)
    print(xml)
    break
