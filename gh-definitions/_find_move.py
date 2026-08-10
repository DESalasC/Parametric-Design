"""Find BoundingBox and Move components in v07."""
from lxml import etree
t = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx")
for obj in t.findall('.//chunk[@name="Object"]'):
    items = obj.find('items')
    if items is None: continue
    name_it = items.find('item[@name="Name"]')
    if name_it is None: continue
    n = name_it.text or ''
    
    container = obj.find('.//chunk[@name="Container"]')
    nick = ''
    if container is not None:
        ni = container.find('items/item[@name="NickName"]')
        if ni is not None: nick = ni.text or ''
    
    if n in ('BoundingBox', 'Bounding Box', 'Vector 2Pt', 'Move', 'Point') or 'Box' in n or 'box' in n or 'Move' in n or 'Vector' in n:
        guid = items.find('item[@name="GUID"]')
        g = guid.text[:12] if guid is not None else '?'
        print(f"Name={n:20s} Nick={nick[:35]:35s} GUID={g}")
