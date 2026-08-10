"""Check GUIDs in v07 output."""
from lxml import etree
t = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx")
for obj in t.findall('.//chunk[@name="Object"]'):
    name_it = obj.find('items/item[@name="Name"]')
    guid_it = obj.find('items/item[@name="GUID"]')
    name = name_it.text if name_it is not None else '?'
    guid = guid_it.text if guid_it is not None else '?'
    print(f"{name:35s} GUID={guid}")
