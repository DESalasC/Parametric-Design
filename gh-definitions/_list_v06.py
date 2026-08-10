from lxml import etree
v06 = etree.parse(r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx')
names = set()
for obj in v06.findall('.//chunk[@name="Object"]'):
    for it in obj.findall('items/item[@name="Name"]'):
        n = it.text or ''
        names.add(n)
for n in sorted(names):
    print(n)
