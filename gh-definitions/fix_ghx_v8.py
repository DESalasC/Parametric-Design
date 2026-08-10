# -*- coding: utf-8 -*-
"""
GHX Fixer v8: Unique InstanceGuids everywhere.
All InstanceGuids (top-level + sub-objects) are regenerated deterministically.
Source/connection references are NOT set (v07 data lacks enough mapping info),
so Grasshopper will open with disconnected components but correct structure.
"""
import sys, os, uuid, hashlib, base64, copy
from lxml import etree

TEMPLATE_FILES = [
    r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx",
    r"D:\Work\PROJECTS\DiseñoParametrico\tests\core\test_06_plugin_component.ghx",
]

# ── GUID system ──
NS = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')

def mk_guid(*parts):
    """Deterministic UUID v5 from string parts."""
    key = "-".join(str(p) for p in parts)
    return str(uuid.uuid5(NS, key))

TYPE_DISPLAY_NAMES = {
    'Group': 'Group',
    'Panel': 'Panel',
    'Slider': 'Number Slider',
    'Python': 'Python 3 Script',
    'Area': 'Area',
    'Explode': 'Explode',
    'CurveMiddle': 'Curve Middle',
    'Deconstruct2DPolyline': '2D Polyline',
    'DeconstructBrep': 'Deconstruct Brep',
    'JoinCurves': 'Join Curves',
    'CurveFrame': 'Curve Frame',
    'Angle': 'Angle',
    'Vector2Pt': 'Vector 2Pt',
    'TapirReceive': 'Tapir Receive Geometry',
    'DFImport': 'Import GeoJSON',
    'Generic': 'Unknown',
}

COMPONENT_GUIDS = {
    'Area':                       '86b28a7e-94d9-4791-8306-e13e10d5f8d5',
    'Explode':                    'afb96615-c59a-45c9-9cac-e27acb1c7ca0',
    'CurveMiddle':                'ccc7b468-e743-4049-891f-299432545898',
    'Curve Middle':               'ccc7b468-e743-4049-891f-299432545898',
    'Vector2Pt':                  '934ede4a-924a-4973-bb05-0dc4b36fae75',
    'Vector 2Pt':                 '934ede4a-924a-4973-bb05-0dc4b36fae75',
    'Python 3 Script':            '719467e6-7cf5-4848-99b0-c5dd57e5442c',
    'PythonScript':               '719467e6-7cf5-4848-99b0-c5dd57e5442c',
    'Panel':                      '59e0b89a-e487-49f8-bab8-b5bab16be14c',
    'GH_Panel':                   '59e0b89a-e487-49f8-bab8-b5bab16be14c',
    'GH_Palette':                 '59e0b89a-e487-49f8-bab8-b5bab16be14c',
    'Number Slider':              '57da07bd-ecab-415d-9d86-af36d7073abc',
    'GH_NumberSlider':            '57da07bd-ecab-415d-9d86-af36d7073abc',
    'Gene Pool':                  '57da07bd-ecab-415d-9d86-af36d7073abc',
    'Group':                      'c552a431-af5b-46a9-a8a4-0fcbc27ef596',
    'GH_Group':                   'c552a431-af5b-46a9-a8a4-0fcbc27ef596',
    'Deconstruct2DPolyline':      'b71dc107-4be8-4a96-86d8-a656c502f71c',
    'DeconstructBrep':            '8d372bdc-9800-45e9-8a26-6e33c5253e21',
    'JoinCurves':                 '8073a420-6bec-49e3-9b18-367f6fd76ac3',
    'CurveFrame':                 '6b2a5853-07aa-4329-ba84-0a5d46b51dbd',
    'Angle':                      'b464fccb-50e7-41bd-9789-8438db9bea9f',
    'DF_Import':                  '3728e6f7-2fc5-4b86-911a-386f511e152f',
    'GH_Import':                  '3728e6f7-2fc5-4b86-911a-386f511e152f',
    'Tapir.ReceiveGeometry':      '8ee23aed-ee26-4966-ba00-6d718e844dbd',
    'ReceiveGeometry':            '8ee23aed-ee26-4966-ba00-6d718e844dbd',
}

def get_component_guid(obj_type, obj_name):
    for key in obj_type.split('.'):
        if key in COMPONENT_GUIDS: return COMPONENT_GUIDS[key]
    if obj_type in COMPONENT_GUIDS: return COMPONENT_GUIDS[obj_type]
    if obj_name in COMPONENT_GUIDS: return COMPONENT_GUIDS[obj_name]
    return '00000000-0000-0000-0000-000000000000'

# ── Classification ──
TYPE_TO_CLASS = {
    'Group': 'Group', 'GH_Group': 'Group',
    'Panel': 'Panel', 'GH_Panel': 'Panel', 'GH_Palette': 'Panel',
    'Slider': 'Slider', 'NumberSlider': 'Slider', 'GH_NumberSlider': 'Slider', 'Gene': 'Slider',
    'Python': 'Python', 'PythonScript': 'Python',
    'Area': 'Area', 'Explode': 'Explode',
    'CurveMiddle': 'CurveMiddle', 'Curve Middle': 'CurveMiddle',
    'Deconstruct2DPolyline': 'Deconstruct2DPolyline', 'Deconstruct2D': 'Deconstruct2DPolyline',
    'DeconstructBrep': 'DeconstructBrep', 'Deconstruct Brep': 'DeconstructBrep',
    'JoinCurves': 'JoinCurves', 'Join Curves': 'JoinCurves',
    'CurveFrame': 'CurveFrame', 'Curve Frame': 'CurveFrame',
    'Angle': 'Angle',
    'Vector2Pt': 'Vector2Pt', 'Vector 2Pt': 'Vector2Pt',
    'Tapir': 'TapirReceive', 'ReceiveGeometry': 'TapirReceive',
    'DF_Import': 'DFImport', 'GH_Import': 'DFImport', 'geoJSON': 'DFImport',
}

def classify_obj(obj_elem):
    otype = obj_elem.get('type', '')
    oname = obj_elem.findtext('Name') or ''
    for tkey in otype.split('.'):
        if tkey in TYPE_TO_CLASS: return TYPE_TO_CLASS[tkey]
    if otype in TYPE_TO_CLASS: return TYPE_TO_CLASS[otype]
    for nkey in TYPE_TO_CLASS:
        if nkey in oname or nkey.replace(' ', '_') in oname:
            return TYPE_TO_CLASS[nkey]
    return 'Generic'

# ── Template matching ──
NAME_TO_CLASS = {
    'Group': 'Group', 'Panel': 'Panel', 'Palette': 'Panel',
    'Number Slider': 'Slider', 'Gene Pool': 'Slider',
    'Python 3 Script': 'Python',
    'Area': 'Area', 'Explode': 'Explode',
    'Curve Middle': 'CurveMiddle', 'Vector 2Pt': 'Vector2Pt',
    'Deconstruct Brep': 'DeconstructBrep', 'Join Curves': 'JoinCurves',
    'Deconstruct 2D Polyline': 'Deconstruct2DPolyline', '2D Polyline': 'Deconstruct2DPolyline',
    'Curve Frame': 'CurveFrame', 'Angle': 'Angle',
    'File Path': 'FileNative',
}

def find_templates():
    templates = {}
    for fpath in TEMPLATE_FILES:
        if not os.path.exists(fpath): continue
        tree = etree.parse(fpath)
        for obj in tree.findall('.//chunk[@name="Object"]'):
            items = obj.find('items')
            if items is None: continue
            name_it = items.find('item[@name="Name"]')
            if name_it is None: continue
            obj_name = (name_it.text or '').strip()
            for nkey, cls in NAME_TO_CLASS.items():
                if obj_name == nkey and cls not in templates:
                    templates[cls] = copy.deepcopy(obj)
                    print(f"  Template [{cls}] <- {obj_name}")
                    break
    if 'Generic' not in templates:
        for fpath in TEMPLATE_FILES:
            tree = etree.parse(fpath)
            for obj in tree.findall('.//chunk[@name="Object"]'):
                templates['Generic'] = copy.deepcopy(obj)
                break
            if 'Generic' in templates: break
    return templates

# ── GUID regeneration ──

def regenerate_instance_guids(obj_elem, v07_idx):
    """
    Replace ALL InstanceGuid items in an object tree with deterministic values.
    Uses the parent element's tag + index as context for uniqueness.
    """
    counter = [0]
    
    def _regenerate(el, parent_tag, parent_index):
        for chunk in el.findall('chunks/chunk'):
            name = chunk.get('name', '')
            idx = chunk.get('index', '0')
            
            for items in chunk.findall('items'):
                for it in items.findall('item'):
                    if it.get('name') == 'InstanceGuid':
                        new_guid = mk_guid('v07', v07_idx, name, idx, counter[0])
                        it.text = new_guid
                        counter[0] += 1
            
            # Recurse
            _regenerate(chunk, name, idx)
        
        # Also handle direct items in the container
        for items in el.findall('items'):
            for it in items.findall('item'):
                if it.get('name') == 'InstanceGuid':
                    new_guid = mk_guid('v07', v07_idx, 'container', 'top', counter[0])
                    it.text = new_guid
                    counter[0] += 1
    
    container = obj_elem.find('.//chunk[@name="Container"]')
    if container is not None:
        _regenerate(container, 'Container', '0')

# ── Data transformers ──

def transform_container(template_obj, v07_obj, obj_class, v07_idx):
    container = template_obj.find('.//chunk[@name="Container"]')
    if container is None: return

    v07_nick = v07_obj.findtext('Nickname') or v07_obj.findtext('Name') or ''
    v07_desc = v07_obj.findtext('Description') or ''

    # Set NickName and Description
    for it in container.iter('item'):
        if it.get('name') == 'NickName' and v07_nick:
            it.text = v07_nick
        elif it.get('name') == 'Description' and v07_desc:
            it.text = v07_desc

    # Class-specific transforms
    if obj_class == 'Group':
        _tr_group(container, v07_obj, v07_idx)
    elif obj_class == 'Panel':
        _tr_panel(container, v07_obj)
    elif obj_class == 'Slider':
        _tr_slider(container, v07_obj)
    elif obj_class == 'Python':
        _tr_python(container, v07_obj)
    else:
        _tr_native(container, v07_obj, obj_class)

    return container

def _tr_group(container, v07_obj, v07_idx):
    """Set Group member IDs to empty (no reference mapping available)."""
    items = container.find('items')
    if items is None: return
    
    # Remove all old ID items
    for it in list(items):
        if it.get('name') == 'ID':
            items.remove(it)
    
    # Set ID_Count to 0
    idc = items.find('item[@name="ID_Count"]')
    if idc is not None:
        idc.text = '0'
    
    items.set('count', str(len(list(items))))

def _tr_panel(container, v07_obj):
    user_text = v07_obj.findtext('Value') or ''
    for it in container.iter('item'):
        if it.get('name') == 'UserText':
            it.text = user_text

def _tr_slider(container, v07_obj):
    min_val = v07_obj.findtext('Min') or '0'
    max_val = v07_obj.findtext('Max') or '1'
    decimals = v07_obj.findtext('DecimalCount') or '0'
    value_list = v07_obj.findtext('ValueList') or ''
    values = [v.strip() for v in value_list.split(',') if v.strip()] if value_list else ['1']
    
    for it in container.iter('item'):
        n = it.get('name')
        if n == 'Min': it.text = min_val
        elif n == 'Max': it.text = max_val
        elif n == 'Rounding': it.text = decimals
        elif n == 'ValueCount': it.text = str(len(values))
    
    branch = container.find('.//chunk[@name="PersistentData"]/chunks/chunk[@name="Branch"]')
    if branch is not None:
        branch_chunks = branch.find('chunks')
        if branch_chunks is not None:
            items_in_branch = list(branch_chunks)
            for chunk in items_in_branch[len(values):]:
                branch_chunks.remove(chunk)
            for i, chunk in enumerate(branch_chunks):
                if i < len(values):
                    for it in chunk.iter('item'):
                        if it.get('name') == 'number' or it.get('type_code') in ('3', '6'):
                            it.text = values[i]
            branch_chunks.set('count', str(len(list(branch_chunks))))
        
        branch_items = branch.find('items')
        if branch_items is not None:
            for it in branch_items:
                if it.get('name') == 'Count':
                    it.text = str(len(values))

def _tr_python(container, v07_obj):
    code_text = v07_obj.findtext('Code') or ''
    v07_nick = v07_obj.findtext('Nickname') or ''
    inputs_node = v07_obj.find('Inputs')
    outputs_node = v07_obj.find('Outputs')
    input_els = inputs_node.findall('Input') if inputs_node is not None else []
    output_els = outputs_node.findall('Output') if outputs_node is not None else []
    
    # Replace code
    for it in container.iter('item'):
        if it.get('name') == 'Text':
            p = it.getparent()
            gp = p.getparent() if p is not None else None
            if gp is not None and gp.get('name') == 'Script':
                it.text = base64.b64encode(code_text.encode('utf-8')).decode('ascii')
        elif it.get('name') == 'Title':
            p = it.getparent()
            gp = p.getparent() if p is not None else None
            if gp is not None and gp.get('name') == 'Script':
                it.text = v07_nick
    
    # Update param names, clear sources
    for i, ip in enumerate(container.findall('.//chunk[@name="InputParam"]')):
        if i < len(input_els):
            name = input_els[i].get('name', f'I{i}')
            for it in ip.iter('item'):
                if it.get('name') in ('Name', 'NickName'):
                    it.text = name
                elif it.get('name') == 'Source':
                    # Remove source reference (can't map reliably)
                    p = it.getparent()
                    if p is not None: p.remove(it)
                elif it.get('name') == 'SourceCount':
                    it.text = '0'
    
    for j, op in enumerate(container.findall('.//chunk[@name="OutputParam"]')):
        if j < len(output_els):
            name = output_els[j].get('name', f'O{j}')
            nick = output_els[j].get('nickname', name)
            for it in op.iter('item'):
                if it.get('name') == 'Name': it.text = name
                elif it.get('name') == 'NickName': it.text = nick
    
    # Update ParameterData counts
    pd = container.find('.//chunk[@name="ParameterData"]')
    if pd is not None:
        for it in pd.iter('item'):
            if it.get('name') == 'InputCount': it.text = str(len(input_els))
            elif it.get('name') == 'OutputCount': it.text = str(len(output_els))
        
        chunks = pd.find('chunks')
        if chunks is not None:
            existing = list(chunks)
            expected = len(input_els) + len(output_els)
            while len(existing) > expected:
                chunks.remove(existing[-1])
                existing.pop()
            chunks.set('count', str(len(list(chunks))))

def _tr_native(container, v07_obj, obj_class):
    inputs_node = v07_obj.find('Inputs')
    outputs_node = v07_obj.find('Outputs')
    input_els = inputs_node.findall('Input') if inputs_node is not None else []
    output_els = outputs_node.findall('Output') if outputs_node is not None else []
    
    for i, pi in enumerate(container.findall('.//chunk[@name="param_input"]')):
        if i < len(input_els):
            name = input_els[i].get('name', f'I{i}')
            for it in pi.iter('item'):
                if it.get('name') in ('Name', 'NickName'):
                    it.text = name
                elif it.get('name') == 'Source':
                    p = it.getparent()
                    if p is not None: p.remove(it)
                elif it.get('name') == 'SourceCount':
                    it.text = '0'
    
    for j, po in enumerate(container.findall('.//chunk[@name="param_output"]')):
        if j < len(output_els):
            name = output_els[j].get('name', f'O{j}')
            nick = output_els[j].get('nickname', name)
            for it in po.iter('item'):
                if it.get('name') == 'Name': it.text = name
                elif it.get('name') == 'NickName': it.text = nick
    
    # Trim extra params
    container_chunks = container.find('chunks')
    if container_chunks is not None:
        input_params = container_chunks.findall('.//chunk[@name="param_input"]')
        output_params = container_chunks.findall('.//chunk[@name="param_output"]')
        for ic in input_params[len(input_els):]:
            container_chunks.remove(ic)
        for oc in output_params[len(output_els):]:
            container_chunks.remove(oc)
        container_chunks.set('count', str(len(list(container_chunks))))


# ── Main ──

def convert(input_path, output_path):
    v07_tree = etree.parse(input_path)
    v07_root = v07_tree.getroot()
    
    doc_obj = v07_root.find('Object')
    objects_node = doc_obj.find('Objects')
    obj_list = objects_node.findall('Object')
    print(f"v07 objects: {len(obj_list)}")
    
    templates = find_templates()
    print(f"Templates: {list(templates.keys())}\n")
    
    new_defobjs = etree.Element('chunk', {'name': 'DefinitionObjects'})
    items = etree.SubElement(new_defobjs, 'items', {'count': '1'})
    etree.SubElement(items, 'item', {
        'name': 'ObjectCount', 'type_name': 'gh_int32', 'type_code': '3'
    }).text = str(len(obj_list))
    
    chunks = etree.SubElement(new_defobjs, 'chunks', {'count': str(len(obj_list))})
    
    for idx, v07_obj in enumerate(obj_list):
        obj_class = classify_obj(v07_obj)
        v07_name = v07_obj.findtext('Name') or '??'
        v07_type = v07_obj.get('type', '')
        guid = get_component_guid(v07_type, v07_name)
        
        template = templates.get(obj_class, templates.get('Generic'))
        status = "" if obj_class in templates else "[FALLBACK]"
        
        print(f"  [{idx:2d}] {v07_name[:40]:40s} {obj_class:20s} {status}")
        
        if template is None:
            print("    SKIP")
            continue
        
        new_obj = copy.deepcopy(template)
        new_obj.set('index', str(idx))
        
        obj_items = new_obj.find('items')
        if obj_items is not None:
            display_name = TYPE_DISPLAY_NAMES.get(obj_class, v07_name)
            for it in obj_items:
                if it.get('name') == 'GUID':
                    it.text = guid
                elif it.get('name') == 'Name':
                    it.text = display_name
        
        # REGENERATE ALL InstanceGuids with unique deterministic values
        regenerate_instance_guids(new_obj, idx)
        
        # Transform data
        transform_container(new_obj, v07_obj, obj_class, idx)
        
        chunks.append(new_obj)
    
    # Build output from v06 header
    v06_path = TEMPLATE_FILES[0]
    v06_tree = etree.parse(v06_path)
    v06_root = v06_tree.getroot()
    
    old_defobjs = v06_root.find('.//chunk[@name="DefinitionObjects"]')
    if old_defobjs is not None:
        parent = old_defobjs.getparent()
        if parent is not None:
            parent.replace(old_defobjs, new_defobjs)
    
    xml_bytes = etree.tostring(v06_root, encoding='utf-8', pretty_print=True, xml_declaration=True)
    
    with open(output_path, 'wb') as f:
        f.write(xml_bytes)
    
    print(f"\nWritten: {output_path} ({len(xml_bytes)} bytes)")
    return True


if __name__ == '__main__':
    input_path = sys.argv[1] if len(sys.argv) > 1 else r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx.bak"
    output_path = sys.argv[2] if len(sys.argv) > 2 else input_path.replace('.ghx.bak', '.ghx')
    
    success = convert(input_path, output_path)
    if success:
        print("\n--- Validating ---")
        import subprocess
        exe = r"D:\Work\LIBRARIES\GhDefinitionExplorer\bin\Release\net8.0\GhDefinitionExplorer.exe"
        result = subprocess.run([exe, output_path, output_path.replace('.ghx', '.json')],
                               capture_output=True, text=True)
        if "Error" in (result.stdout + result.stderr):
            print("FAILED")
            for line in (result.stdout + result.stderr).split('\n'):
                if 'Error' in line.lower():
                    print(f"  {line.strip()}")
        else:
            print("OK")
