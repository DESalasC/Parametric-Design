# -*- coding: utf-8 -*-
"""
GHX Fixer v10.1: Templates (matched by GUID) for 10 known types,
build-from-scratch for 5 edge cases (Gene Pool, Deconstruct2DPolyline, Angle-builtin, TapirReceive, DFImport).
"""
import sys, os, uuid, hashlib, base64, copy
from lxml import etree

NS = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')
def iguid(*parts): return str(uuid.uuid5(NS, '-'.join(str(p) for p in parts)))

TEMPLATE_PATHS = [
    r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx",
    r"D:\Work\PROJECTS\DiseñoParametrico\tests\core\test_06_plugin_component.ghx",
]

COMPONENT_GUIDS = {
    'Area': '86b28a7e-94d9-4791-8306-e13e10d5f8d5',
    'Explode': 'afb96615-c59a-45c9-9cac-e27acb1c7ca0',
    'CurveMiddle': 'ccc7b468-e743-4049-891f-299432545898',
    'Vector2Pt': '934ede4a-924a-4973-bb05-0dc4b36fae75',
    'Python 3 Script': '719467e6-7cf5-4848-99b0-c5dd57e5442c',
    'Panel': '59e0b89a-e487-49f8-bab8-b5bab16be14c',
    'GH_Palette': '59e0b89a-e487-49f8-bab8-b5bab16be14c',
    'Number Slider': '57da07bd-ecab-415d-9d86-af36d7073abc',
    'Gene Pool': '57da07bd-ecab-415d-9d86-af36d7073abc',
    'Group': 'c552a431-af5b-46a9-a8a4-0fcbc27ef596',
    'GH_Group': 'c552a431-af5b-46a9-a8a4-0fcbc27ef596',
    'Deconstruct2DPolyline': 'b71dc107-4be8-4a96-86d8-a656c502f71c',
    'DeconstructBrep': '8d372bdc-9800-45e9-8a26-6e33c5253e21',
    'JoinCurves': '8073a420-6bec-49e3-9b18-367f6fd76ac3',
    'CurveFrame': '6b2a5853-07aa-4329-ba84-0a5d46b51dbd',
    'Angle': 'b464fccb-50e7-41bd-9789-8438db9bea9f',
    'Tapir.ReceiveGeometry': '8ee23aed-ee26-4966-ba00-6d718e844dbd',
    'ReceiveGeometry': '8ee23aed-ee26-4966-ba00-6d718e844dbd',
    'Tapir Receive Geometry': '8ee23aed-ee26-4966-ba00-6d718e844dbd',
    'GH_Import': '3728e6f7-2fc5-4b86-911a-386f511e152f',
    'DF_Import': '3728e6f7-2fc5-4b86-911a-386f511e152f',
    'Import GeoJSON': '3728e6f7-2fc5-4b86-911a-386f511e152f',
}

def v07_guid(obj_type, obj_name):
    obj_type = (obj_type or '').strip()
    parts = obj_type.split('.')
    for key in parts:
        key = key.strip()
        if key in COMPONENT_GUIDS:
            return COMPONENT_GUIDS[key]
    if obj_type in COMPONENT_GUIDS:
        return COMPONENT_GUIDS[obj_type]
    obj_name = (obj_name or '').strip()
    if obj_name in COMPONENT_GUIDS:
        return COMPONENT_GUIDS[obj_name]
    return None

# ── Template helpers ──
def find_template_by_guid(target_guid):
    for fpath in TEMPLATE_PATHS:
        if not os.path.exists(fpath): continue
        t = etree.parse(fpath)
        for obj in t.findall('.//chunk[@name="Object"]'):
            gi = obj.find('items/item[@name="GUID"]')
            if gi is not None and gi.text == target_guid:
                return copy.deepcopy(obj), os.path.basename(fpath)
    return None, None

def find_second_angle():
    """Find the second Angle object (built-in variant) in test_06."""
    t = etree.parse(TEMPLATE_PATHS[1])
    count = 0
    for obj in t.findall('.//chunk[@name="Object"]'):
        gi = obj.find('items/item[@name="GUID"]')
        if gi is not None and gi.text == COMPONENT_GUIDS['Angle']:
            count += 1
            if count == 2:  # Second one is the built-in
                return copy.deepcopy(obj), os.path.basename(TEMPLATE_PATHS[1])
    return None, None

def regenerate_instance_guids(obj_elem, v07_idx):
    counter = [0]
    for it in obj_elem.iter('item'):
        if it.get('name') == 'InstanceGuid':
            p = it.getparent()
            gp = p.getparent() if p is not None else None
            cn = gp.get('name', '') if gp is not None and gp.tag == 'chunk' else ''
            ci = gp.get('index', '') if gp is not None and gp.tag == 'chunk' else ''
            it.text = iguid('v10', v07_idx, cn, ci, counter[0])
            counter[0] += 1

def remove_all_sources(container):
    for it in container.iter('item'):
        if it.get('name') == 'Source':
            p = it.getparent()
            if p is not None: p.remove(it)
        elif it.get('name') == 'SourceCount':
            it.text = '0'

def clear_group_members(container):
    items = container.find('items')
    if items is None: return
    for it in list(items):
        if it.get('name') == 'ID': items.remove(it)
    idc = items.find('item[@name="ID_Count"]')
    if idc is not None: idc.text = '0'
    items.set('count', str(len(list(items))))

# ── Template modifier ──
def modify_template(new_obj, v07_obj, v07_idx):
    v07_nick = v07_obj.findtext('Nickname') or ''
    v07_desc = v07_obj.findtext('Description') or ''
    v07_type = v07_obj.get('type', '')
    v07_name = v07_obj.findtext('Name') or ''
    guid = v07_guid(v07_type, v07_name)
    
    obj_items = new_obj.find('items')
    if obj_items is not None and guid:
        for it in obj_items:
            if it.get('name') == 'GUID':
                it.text = guid
    
    regenerate_instance_guids(new_obj, v07_idx)
    container = new_obj.find('.//chunk[@name="Container"]')
    if container is None: return
    
    remove_all_sources(container)
    
    if guid == COMPONENT_GUIDS.get('Group'):
        clear_group_members(container)
    
    for it in container.iter('item'):
        if it.get('name') == 'NickName' and v07_nick:
            it.text = v07_nick
        elif it.get('name') == 'Description' and v07_desc:
            it.text = v07_desc
    
    if guid == COMPONENT_GUIDS.get('Panel'):
        text = v07_obj.findtext('Value') or ''
        for it in container.iter('item'):
            if it.get('name') == 'UserText': it.text = text
    
    if guid == COMPONENT_GUIDS.get('Number Slider'):
        _update_slider(container, v07_obj)
    
    if guid == COMPONENT_GUIDS.get('Python 3 Script'):
        code = v07_obj.findtext('Code') or ''
        nick = v07_obj.findtext('Nickname') or ''
        for it in container.iter('item'):
            if it.get('name') == 'Text':
                p = it.getparent()
                gp = p.getparent() if p is not None else None
                if gp is not None and gp.get('name') == 'Script':
                    it.text = base64.b64encode(code.encode('utf-8')).decode('ascii')
            elif it.get('name') == 'Title':
                p = it.getparent()
                gp = p.getparent() if p is not None else None
                if gp is not None and gp.get('name') == 'Script':
                    it.text = nick

def _update_slider(container, v07_obj):
    mn = v07_obj.findtext('Min') or '0'
    mx = v07_obj.findtext('Max') or '1'
    dec = v07_obj.findtext('DecimalCount') or '0'
    vlist = v07_obj.findtext('ValueList') or ''
    values = [v.strip() for v in vlist.split(',') if v.strip()] if vlist else ['1']
    for it in container.iter('item'):
        n = it.get('name')
        if n == 'Min': it.text = mn
        elif n == 'Max': it.text = mx
        elif n == 'Rounding': it.text = dec
        elif n == 'ValueCount': it.text = str(len(values))
    pd = container.find('.//chunk[@name="PersistentData"]')
    if pd is None: return
    branch = pd.find('chunks/chunk[@name="Branch"]')
    if branch is None: return
    for it in branch.iter('item'):
        if it.get('name') == 'Count': it.text = str(len(values))
    bc = branch.find('chunks')
    if bc is not None:
        ex = list(bc)
        for c in ex[len(values):]: bc.remove(c)
        for i, c in enumerate(bc):
            if i < len(values):
                for it in c.iter('item'):
                    if it.get('name') in ('number','Value') or it.get('type_code') in ('3','6'):
                        it.text = values[i]
        bc.set('count', str(len(list(bc))))

# ── lxml element builders (for edge cases) ──
def _item(parent, name, value, tn='gh_string', tc='10', idx=None):
    a = {'name': name, 'type_name': tn, 'type_code': tc}
    if idx is not None: a['index'] = str(idx)
    e = etree.SubElement(parent, 'item', a)
    e.text = str(value) if value is not None else ''
    return e

def _item_guid(parent, name, value, idx=None):
    a = {'name': name, 'type_name': 'gh_guid', 'type_code': '9'}
    if idx is not None: a['index'] = str(idx)
    e = etree.SubElement(parent, 'item', a)
    e.text = str(value)
    return e

def _item_bool(parent, name, v):
    return _item(parent, name, 'true' if v else 'false', 'gh_bool', '1')

def _item_int(parent, name, v):
    return _item(parent, name, str(v), 'gh_int32', '3')

def _item_double(parent, name, v):
    return _item(parent, name, str(v), 'gh_double', '6')

def _item_color(parent, name, argb):
    e = etree.SubElement(parent, 'item', {'name': name, 'type_name': 'gh_drawing_color', 'type_code': '36'})
    etree.SubElement(e, 'ARGB').text = argb

def _items(parent, count):
    return etree.SubElement(parent, 'items', {'count': str(count)})

def _chunks(parent, count):
    return etree.SubElement(parent, 'chunks', {'count': str(count)})

def _chunk(parent, name, index=None):
    a = {'name': name}
    if index is not None: a['index'] = str(index)
    return etree.SubElement(parent, 'chunk', a)

def _attrs(parent, x=0, y=0, w=0, h=0):
    e = _chunk(parent, 'Attributes')
    it = _items(e, 2)
    b = etree.SubElement(it, 'item', {'name': 'Bounds', 'type_name': 'gh_drawing_rectanglef', 'type_code': '35'})
    for t, v in [('X',x), ('Y',y), ('W',w), ('H',h)]:
        etree.SubElement(b, t).text = str(v)
    p = etree.SubElement(it, 'item', {'name': 'Pivot', 'type_name': 'gh_drawing_pointf', 'type_code': '31'})
    etree.SubElement(p, 'X').text = str(x)
    etree.SubElement(p, 'Y').text = str(y)
    return e

def _build_param_input(parent, name, idx, v07_idx, obj_class):
    pi = _chunk(parent, 'param_input', idx)
    pi_ig = iguid('v10', v07_idx, obj_class, 'in', idx)
    it = _items(pi, 6)
    _item(it, 'Description', f'Script input {name}.')
    _item_guid(it, 'InstanceGuid', pi_ig)
    _item(it, 'Name', name)
    _item(it, 'NickName', name)
    _item_bool(it, 'Optional', False)
    _item_int(it, 'SourceCount', 0)
    ck = _chunks(pi, 1)
    _attrs(ck)
    return pi

def _build_param_output(parent, name, idx, v07_idx, obj_class, has_access=False):
    po = _chunk(parent, 'param_output', idx)
    po_ig = iguid('v10', v07_idx, obj_class, 'out', idx)
    nitems = 7 if has_access else 6
    it = _items(po, nitems)
    if has_access:
        _item_int(it, 'Access', 1)
    _item(it, 'Description', f'Script output {name}.')
    _item_guid(it, 'InstanceGuid', po_ig)
    _item(it, 'Name', name)
    _item(it, 'NickName', name)
    _item_bool(it, 'Optional', False)
    _item_int(it, 'SourceCount', 0)
    ck = _chunks(po, 1)
    _attrs(ck)
    return po

def build_native(v07_obj, idx, guid, disp_name, inputs, outputs, output_access=False):
    """Build a native component Object from scratch."""
    nick = v07_obj.findtext('Nickname') or ''
    desc = v07_obj.findtext('Description') or ''
    obj_ig = iguid('v10', idx, disp_name)
    
    obj = etree.Element('chunk', {'name': 'Object', 'index': str(idx)})
    it = _items(obj, 2)
    _item_guid(it, 'GUID', guid)
    _item(it, 'Name', disp_name)
    
    ck = _chunks(obj, 1)
    cont = _chunk(ck, 'Container')
    
    it = _items(cont, 4)
    _item(it, 'Description', desc)
    _item_guid(it, 'InstanceGuid', obj_ig)
    _item(it, 'Name', disp_name)
    _item(it, 'NickName', nick)
    
    total = 1 + len(inputs) + len(outputs)
    ck2 = _chunks(cont, total)
    _attrs(ck2)
    
    for i, pn in enumerate(inputs):
        _build_param_input(ck2, pn, i, idx, disp_name)
    
    for j, pn in enumerate(outputs):
        _build_param_output(ck2, pn, j, idx, disp_name, output_access)
    
    return obj

def build_genepool(v07_obj, idx):
    """Build Gene Pool (Number Slider COMPONENT) from scratch."""
    nick = v07_obj.findtext('Nickname') or 'Gene Pool'
    mn = v07_obj.findtext('Min') or '0'
    mx = v07_obj.findtext('Max') or '1'
    dec = v07_obj.findtext('DecimalCount') or '0'
    vlist = v07_obj.findtext('ValueList') or ''
    values = [v.strip() for v in vlist.split(',') if v.strip()] if vlist else ['1']
    obj_ig = iguid('v10', idx, 'GenePool')
    
    obj = etree.Element('chunk', {'name': 'Object', 'index': str(idx)})
    it = _items(obj, 2)
    _item_guid(it, 'GUID', COMPONENT_GUIDS['Gene Pool'])
    _item(it, 'Name', 'Gene Pool')
    
    ck = _chunks(obj, 1)
    cont = _chunk(ck, 'Container')
    
    it = _items(cont, 16)
    _item(it, 'Description', 'A Gene Pool')
    _item_bool(it, 'DrawValue', True)
    _item_guid(it, 'InstanceGuid', obj_ig)
    _item(it, 'Max', mx, 'gh_double', '6')
    _item(it, 'Min', mn, 'gh_double', '6')
    _item(it, 'Name', 'Gene Pool')
    _item(it, 'NickName', nick)
    _item_int(it, 'Rounding', int(dec))
    _item_bool(it, 'ShowCompile', True)
    _item_bool(it, 'ShowPerturb', True)
    _item_bool(it, 'ShowRecombine', True)
    _item_bool(it, 'Slider', False)
    _item_bool(it, 'Snap', True)
    _item_double(it, 'Spacing', 0)
    _item_bool(it, 'Symbolic', False)
    _item_int(it, 'ValueCount', len(values))
    
    ck2 = _chunks(cont, 2)
    _attrs(ck2)
    
    pd = _chunk(ck2, 'PersistentData')
    it = _items(pd, 1)
    _item_int(it, 'Count', 1)
    ck3 = _chunks(pd, 1)
    branch = _chunk(ck3, 'Branch', 0)
    it = _items(branch, 2)
    _item_int(it, 'Count', len(values))
    _item(it, 'Path', '{0}')
    ck4 = _chunks(branch, len(values))
    for vi, val in enumerate(values):
        ci = _chunk(ck4, 'Item', vi)
        it = _items(ci, 1)
        try:
            if '.' in val: _item_double(it, val, val)
            else: _item(it, 'number', val, 'gh_int32', '3')
        except:
            _item(it, 'number', val)
    
    return obj

# ── EDGE CASE SPECS (verified from test_06 / Grasshopper docs) ──
EDGE_CASES = {
    # Only GUIDs that have NO template at all in any source file
    '8ee23aed-ee26-4966-ba00-6d718e844dbd': ('Tapir Receive Geometry', [], ['Geometry'], True),
    '3728e6f7-2fc5-4b86-911a-386f511e152f': ('Import GeoJSON', ['FilePath'], ['Features'], True),
}

# ── Main ──
def convert(input_path, output_path):
    v07_tree = etree.parse(input_path)
    v07_root = v07_tree.getroot()
    doc_obj = v07_root.find('Object')
    objects_node = doc_obj.find('Objects')
    obj_list = objects_node.findall('Object')
    print(f"v07 objects: {len(obj_list)}")
    
    template_cache = {}
    
    # Special: cache the SECOND Angle (built-in, not Kangaroo)
    builtin_angle, angle_src = find_second_angle()
    if builtin_angle is not None:
        template_cache[COMPONENT_GUIDS['Angle']] = builtin_angle
        print(f"  Template [Angle-builtin] <- Angle (built-in, {angle_src})")
    
    new_defobjs = etree.Element('chunk', {'name': 'DefinitionObjects'})
    it = _items(new_defobjs, 1)
    _item_int(it, 'ObjectCount', len(obj_list))
    ck = _chunks(new_defobjs, len(obj_list))
    
    for idx, v07_obj in enumerate(obj_list):
        v07_name = v07_obj.findtext('Name') or '??'
        v07_type = v07_obj.get('type', '')
        guid = v07_guid(v07_type, v07_name)
        
        if not guid:
            print(f"  [{idx:2d}] {v07_name[:40]:40s} NO GUID (type={v07_type.split('.')[-1] if '.' in v07_type else v07_type})")
            continue
        
        # Check if edge case (no template available)
        if guid in EDGE_CASES:
            dn, inputs, outputs, oa = EDGE_CASES[guid]
            new_obj = build_native(v07_obj, idx, guid, dn, inputs, outputs, oa)
            print(f"  [{idx:2d}] {v07_name[:40]:40s} -> built-from-scratch [{dn}]")
            ck.append(new_obj)
            continue
        
        # Get or cache template
        if guid not in template_cache:
            template_cache[guid], src = find_template_by_guid(guid)
            if src and template_cache[guid] is not None:
                tn = template_cache[guid].find('items/item[@name="Name"]')
                print(f"  Template [{guid[:8]}] <- {tn.text if tn is not None else '?'} ({src})")
        
        template = template_cache.get(guid)
        if template is None:
            print(f"  [{idx:2d}] {v07_name[:40]:40s} GUID={guid[:8]} [NO TEMPLATE]")
            continue
        
        new_obj = copy.deepcopy(template)
        new_obj.set('index', str(idx))
        modify_template(new_obj, v07_obj, idx)
        print(f"  [{idx:2d}] {v07_name[:40]:40s} GUID={guid[:8]}")
        ck.append(new_obj)
    
    # Build output from v06 header
    v06_tree = etree.parse(TEMPLATE_PATHS[0])
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
