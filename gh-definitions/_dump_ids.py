"""Show v07 simplified format IDs."""
import xml.etree.ElementTree as ET
t = ET.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx.bak")
for i, o in enumerate(t.getroot().find('Object/Objects').findall('Object')):
    oid = o.get('id', '')
    otype = o.get('type', '')
    name = (o.findtext('Name') or '')[:35]
    mbrs = (o.findtext('MemberIds') or '')[:60]
    # Show inputs with sources
    inputs_str = ''
    inputs_node = o.find('Inputs')
    if inputs_node is not None and len(inputs_node) > 0:
        parts = []
        for inp in inputs_node.findall('Input'):
            src = inp.get('source', '')
            if src:
                parts.append(f"{inp.get('name','?')}<-{src}")
        inputs_str = ','.join(parts)
    print(f"[{i:2d}] type={otype:50s} id={oid:8s} name={name:35s} members={mbrs} inputs={inputs_str}")
