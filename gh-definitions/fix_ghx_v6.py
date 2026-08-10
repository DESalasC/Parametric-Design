# -*- coding: utf-8 -*-
"""
GHX Fixer v6.1: Multi-source templates (v06 + test_06_plugin_component).
Deep-copies template objects and replaces only the data fields.
"""
import sys, os, uuid, hashlib, base64, copy
from lxml import etree

TEMPLATE_FILES = [
    r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx",
    r"D:\Work\PROJECTS\DiseñoParametrico\tests\core\test_06_plugin_component.ghx",
]

def mkguid(s):
    h = hashlib.md5(s.encode('utf-8')).digest()
    h = bytearray(h)
    h[6] = (h[6] & 0x0F) | 0x30
    h[8] = (h[8] & 0x3F) | 0x80
    return str(uuid.UUID(bytes=bytes(h)))

COMPONENT_GUIDS = {
    'Area': '86b28a7e-94d9-4791-8306-e13e10d5f8d5',
    'Explode': 'afb96615-c59a-45c9-9cac-e27acb1c7ca0',
    'CurveMiddle': 'ccc7b468-e743-4049-891f-299432545898',
    'Curve Middle': 'ccc7b468-e743-4049-891f-299432545898',
    'Vector2Pt': '934ede4a-924a-4973-bb05-0dc4b36fae75',
    'Vector 2Pt': '934ede4a-924a-4973-bb05-0dc4b36fae75',
    'Python 3 Script': '719467e6-7cf5-4848-99b0-c5dd57e5442c',
    'PythonScript': '719467e6-7cf5-4848-99b0-c5dd57e5442c',
    'Panel': '59e0b89a-e487-49f8-bab8-b5bab16be14c',
    'GH_Panel': '59e0b89a-e487-49f8-bab8-b5bab16be14c',
    'GH_Palette': '59e0b89a-e487-49f8-bab8-b5bab16be14c',
    'Number Slider': '57da07bd-ecab-415d-9d86-af36d7073abc',
    'GH_NumberSlider': '57da07bd-ecab-415d-9d86-af36d7073abc',
    'Gene Pool': '57da07bd-ecab-415d-9d86-af36d7073abc',
    'Group': 'c552a431-af5b-46a9-a8a4-0fcbc27ef596',
    'GH_Group': 'c552a431-af5b-46a9-a8a4-0fcbc27ef596',
    'Deconstruct2DPolyline': 'b71dc107-4be8-4a96-86d8-a656c502f71c',
    'DeconstructBrep': '8d372bdc-9800-45e9-8a26-6e33c5253e21',
    'JoinCurves': '8073a420-6bec-49e3-9b18-367f6fd76ac3',
    'CurveFrame': '6b2a5853-07aa-4329-ba84-0a5d46b51dbd',
    'Angle': 'b464fccb-50e7-41bd-9789-8438db9bea9f',
    'DF_Import': '3728e6f7-2fc5-4b86-911a-386f511e152f',
    'GH_Import': '3728e6f7-2fc5-4b86-911a-386f511e152f',
    'Tapir.ReceiveGeometry': '8ee23aed-ee26-4966-ba00-6d718e844dbd',
    'ReceiveGeometry': '8ee23aed-ee26-4966-ba00-6d718e844dbd',
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
    # Check type directly
    for tkey in otype.split('.'):
        if tkey in TYPE_TO_CLASS: return TYPE_TO_CLASS[tkey]
    if otype in TYPE_TO_CLASS: return TYPE_TO_CLASS[otype]
    # Check name
    for nkey in TYPE_TO_CLASS:
        if nkey in oname or nkey.replace(' ', '_') in oname:
            return TYPE_TO_CLASS[nkey]
    return 'Generic'

# ── Template matching by component NAME ──

NAME_TO_CLASS = {
    'Group': 'Group',
    'Panel': 'Panel', 'Palette': 'Panel',
    'Number Slider': 'Slider', 'Gene Pool': 'Slider',
    'Python 3 Script': 'Python',
    'Area': 'Area',
    'Explode': 'Explode',
    'Curve Middle': 'CurveMiddle',
    'Vector 2Pt': 'Vector2Pt',
    'Deconstruct Brep': 'DeconstructBrep',
    'Join Curves': 'JoinCurves',
    'Deconstruct 2D Polyline': 'Deconstruct2DPolyline',
    '2D Polyline': 'Deconstruct2DPolyline',
    'Curve Frame': 'CurveFrame',
    'Angle': 'Angle',
    'File Path': 'FileNative',  # fallback native template
}

def find_templates():
    templates = {}
    for fpath in TEMPLATE_FILES:
        if not os.path.exists(fpath):
            print(f"  Template file not found: {fpath}")
            continue
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
                    print(f"  Template [{cls}] <- {obj_name} (from {os.path.basename(fpath)})")
                    break
    if 'Generic' not in templates:
        for fpath in TEMPLATE_FILES:
            tree = etree.parse(fpath)
            for obj in tree.findall('.//chunk[@name="Object"]'):
                templates['Generic'] = copy.deepcopy(obj)
                name_it = obj.find('items/item[@name="Name"]')
                print(f"  Fallback [Generic] <- {name_it.text if name_it is not None else '??'}")
                break
            if 'Generic' in templates: break
    return templates


# ── Data transformers ──

def transform_container(template_obj, v07_obj, obj_class):
    container = template_obj.find('.//chunk[@name="Container"]')
    if container is None:
        print("    WARN: No Container in template")
        return

    v07_nick = v07_obj.findtext('Nickname') or v07_obj.findtext('Name') or ''
    v07_desc = v07_obj.findtext('Description') or ''
    new_ig = str(uuid.uuid4())

    # Replace InstanceGuid
    for it in container.iter('item'):
        if it.get('name') == 'InstanceGuid':
            it.text = new_ig
        elif it.get('name') == 'NickName' and v07_nick:
            it.text = v07_nick
        elif it.get('name') == 'Description' and v07_desc:
            it.text = v07_desc

    # Class-specific transforms
    if obj_class == 'Group':
        _tr_group(container, v07_obj)
    elif obj_class == 'Panel':
        _tr_panel(container, v07_obj)
    elif obj_class == 'Slider':
        _tr_slider(container, v07_obj)
    elif obj_class == 'Python':
        _tr_python(container, v07_obj)
    else:
        _tr_native(container, v07_obj, obj_class)
    
    return container


def _tr_group(container, v07_obj):
    member_ids_str = v07_obj.findtext('MemberIds') or ''
    member_ids = [m.strip() for m in member_ids_str.split(',') if m.strip()]
    items = container.find('items')
    if items is None: return

    # Remove old ID items
    for it in list(items):
        if it.get('name') == 'ID':
            items.remove(it)
    
    # Update ID_Count
    idc = items.find('item[@name="ID_Count"]')
    if idc is not None:
        idc.text = str(len(member_ids))
    
    # Insert new ID items BEFORE ID_Count
    idc_idx = None
    all_items = list(items)
    for i, it in enumerate(all_items):
        if it.get('name') == 'ID_Count':
            idc_idx = i
            break
    
    if idc_idx is None:
        # Fallback: before InstanceGuid
        for i, it in enumerate(all_items):
            if it.get('name') == 'InstanceGuid':
                idc_idx = i
                break
    
    if idc_idx is not None:
        for mi, mid in enumerate(member_ids):
            e = etree.Element('item', {
                'name': 'ID', 'index': str(mi),
                'type_name': 'gh_guid', 'type_code': '9'
            })
            e.text = mkguid(mid)
            e.tail = all_items[idc_idx].tail if idc_idx < len(all_items) else '\n                    '
            items.insert(idc_idx + mi, e)
    
    # Update count
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
    
    # Update PersistentData items
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
            parent = it.getparent()
            gparent = parent.getparent() if parent is not None else None
            if gparent is not None and gparent.get('name') == 'Script':
                it.text = base64.b64encode(code_text.encode('utf-8')).decode('ascii')
        elif it.get('name') == 'Title':
            parent = it.getparent()
            gparent = parent.getparent() if parent is not None else None
            if gparent is not None and gparent.get('name') == 'Script':
                it.text = v07_nick
    
    # Update param names
    for i, ip in enumerate(container.findall('.//chunk[@name="InputParam"]')):
        if i < len(input_els):
            name = input_els[i].get('name', f'I{i}')
            for it in ip.iter('item'):
                if it.get('name') in ('Name', 'NickName'):
                    it.text = name
    
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
        
        # Adjust chunk count
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
    
    templates = find_templates()
    print(f"\nTemplates: {list(templates.keys())}")
    
    doc_obj = v07_root.find('Object')
    objects_node = doc_obj.find('Objects')
    obj_list = objects_node.findall('Object')
    print(f"v07 has {len(obj_list)} objects\n")
    
    # Build new DefinitionObjects
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
        
        status = ""
        template = templates.get(obj_class)
        if template is None:
            template = templates.get('Generic')
            status = "[FALLBACK]"
        
        print(f"  [{idx:2d}] {v07_name:40s} class={obj_class:20s} guid={guid[:8]} {status}")
        
        if template is None:
            print("    SKIP: no template")
            continue
        
        new_obj = copy.deepcopy(template)
        new_obj.set('index', str(idx))
        
        # Update Object GUID/Name
        obj_items = new_obj.find('items')
        if obj_items is not None:
            for it in obj_items:
                if it.get('name') == 'GUID':
                    it.text = guid
        
        transform_container(new_obj, v07_obj, obj_class)
        chunks.append(new_obj)
    
    # Build output from v06 template
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
            print("VALIDATION FAILED")
            for line in (result.stdout + result.stderr).split('\n'):
                if 'Error' in line or 'error' in line.lower():
                    print(f"  {line.strip()}")
        else:
            print("VALIDATION OK")
        if result.stderr.strip():
            print("STDERR:", result.stderr[:200])
