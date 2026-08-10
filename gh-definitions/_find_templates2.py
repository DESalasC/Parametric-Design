from lxml import etree
import os
paths = [
    r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\DiseñoParametrico_BaseConexiones.ghx",
    r"D:\Work\PROJECTS\DiseñoParametrico\docs\knowledge-base\ghx-samples\plugins\tapir\sandbox\gh-wip\tapir_wip_rc1.ghx",
]
for p in paths:
    if not os.path.exists(p):
        print(f"NOT FOUND: {p}")
        continue
    print(f"\n=== {os.path.basename(p)} ===")
    t = etree.parse(p)
    for obj in t.findall('.//chunk[@name="Object"]'):
        items = obj.find('items')
        if items is None: continue
        name_it = items.find('item[@name="Name"]')
        guid_it = items.find('item[@name="GUID"]')
        n = name_it.text if name_it is not None else '?'
        g = guid_it.text[:20] if guid_it is not None else '?'
        print(f"  {n:30s} GUID={g}")
