from lxml import etree
import os
paths = [
    r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\DiseñoParametrico_BaseConexiones.ghx",
    r"D:\Work\PROJECTS\DiseñoParametrico\docs\knowledge-base\ghx-samples\plugins\tapir\sandbox\gh-wip\tapir_wip_rc1.ghx",
]
for p in paths:
    if os.path.exists(p):
        print(f"\n=== {os.path.basename(p)} ===")
        t = etree.parse(p)
        for obj in t.findall('.//chunk[@name="Object"]'):
            for it in obj.findall('items/item[@name="Name"]'):
                n = it.text or ''
                if 'Tapir' in n or 'Receive' in n or 'geoJSON' in n or 'Import' in n or 'Deconstruct' in n:
                    print(f"  {n}")
