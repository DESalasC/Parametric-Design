# Compare Container structures between my v07 output and test_06 reference
import xml.etree.ElementTree as ET

# Load both files
ref = ET.parse(r'D:\Work\PROJECTS\DiseñoParametrico\tests\core\test_06_plugin_component.ghx')
my = ET.parse(r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx')

def get_object_containers(root):
    """Get list of (name, container_xml) for all objects."""
    results = []
    for obj in root.iter('chunk'):
        if obj.get('name') != 'Object': continue
        name = ''
        for items_b in obj:
            if items_b.tag == 'items':
                for item in items_b:
                    if item.get('name') == 'Name': name = item.text or ''
        # Find Container
        for c in obj:
            if c.tag == 'chunks':
                for chunk in c:
                    if chunk.get('name') == 'Container':
                        results.append((name, chunk))
        if not results or results[-1][0] != name:
            results.append((name, None))
    return results

def dump_container_structure(container, indent=0):
    """Dump the tag structure of a container."""
    lines = []
    prefix = '  ' * indent
    if container is None:
        return ['(no container)']
    
    # Items
    for child in container:
        if child.tag == 'items':
            items_list = []
            for item in child:
                name = item.get('name', '')
                text = (item.text or '').strip()[:60]
                items_list.append(f'{name}={text}')
            lines.append(f'{prefix}items({child.get("count","?")}): {", ".join(items_list[:8])}')
        elif child.tag == 'chunks':
            chunks_list = []
            for c in child:
                chunks_list.append(f'{c.get("name","")}[{c.get("index","")}]')
            lines.append(f'{prefix}chunks({child.get("count","?")}): {", ".join(chunks_list[:8])}')
    return lines

ref_containers = get_object_containers(ref)
my_containers = get_object_containers(my)

# Compare by component name
ref_by_name = {n: c for n, c in ref_containers}
my_by_name = {}
for n, c in my_containers:
    base = n.replace(' (Vecinos)', '')
    my_by_name[base] = c

for ref_name in ['Deconstruct Brep', 'Join Curves', 'Curve Frame', 'Angle']:
    print(f'\n=== {ref_name} ===')
    print('REFERENCE:')
    ref_c = ref_by_name.get(ref_name)
    for line in dump_container_structure(ref_c):
        print(f'  {line}')
    print('MY OUTPUT:')
    my_c = my_by_name.get(ref_name)
    for line in dump_container_structure(my_c):
        print(f'  {line}')
