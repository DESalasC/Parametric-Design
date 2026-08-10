# -*- coding: utf-8 -*-
"""
GHX Fixer v9: Build Containers from scratch using lxml Element/SubElement.
No templates, no deep copy, no stack tracking.
Every container is built with the exact structure each component type expects.
"""
import sys, os, uuid, hashlib, base64
from lxml import etree

# ── Helpers ──
NS = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')
def iguid(*parts): return str(uuid.uuid5(NS, '-'.join(str(p) for p in parts)))

COMPONENT_GUIDS = {
    'Area': '86b28a7e-94d9-4791-8306-e13e10d5f8d5',
    'Explode': 'afb96615-c59a-45c9-9cac-e27acb1c7ca0',
    'CurveMiddle': 'ccc7b468-e743-4049-891f-299432545898',
    'Curve Mid': 'ccc7b468-e743-4049-891f-299432545898',
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

def component_guid(obj_type, obj_name):
    for key in obj_type.split('.'):
        if key in COMPONENT_GUIDS: return COMPONENT_GUIDS[key]
    if obj_type in COMPONENT_GUIDS: return COMPONENT_GUIDS[obj_type]
    if obj_name in COMPONENT_GUIDS: return COMPONENT_GUIDS[obj_name]
    return '00000000-0000-0000-0000-000000000000'

# ── XML element builders ──
def item(parent, name, value, tn='gh_string', tc='10', idx=None):
    attrs = {'name': name, 'type_name': tn, 'type_code': tc}
    if idx is not None: attrs['index'] = str(idx)
    e = etree.SubElement(parent, 'item', attrs)
    e.text = str(value) if value is not None else ''
    return e

def item_guid(parent, name, value, idx=None):
    attrs = {'name': name, 'type_name': 'gh_guid', 'type_code': '9'}
    if idx is not None: attrs['index'] = str(idx)
    e = etree.SubElement(parent, 'item', attrs)
    e.text = str(value)
    return e

def item_bool(parent, name, v):
    return item(parent, name, 'true' if v else 'false', 'gh_bool', '1')

def item_int(parent, name, v):
    return item(parent, name, str(v), 'gh_int32', '3')

def item_double(parent, name, v):
    return item(parent, name, str(v), 'gh_double', '6')

def item_color(parent, name, argb):
    e = etree.SubElement(parent, 'item', {'name': name, 'type_name': 'gh_drawing_color', 'type_code': '36'})
    etree.SubElement(e, 'ARGB').text = argb
    return e

def items(parent, count): return etree.SubElement(parent, 'items', {'count': str(count)})
def chunks(parent, count): return etree.SubElement(parent, 'chunks', {'count': str(count)})
def chunk(parent, name, index=None):
    attrs = {'name': name}
    if index is not None: attrs['index'] = str(index)
    return etree.SubElement(parent, 'chunk', attrs)

def attrs_bounds(parent, x=0, y=0, w=0, h=0):
    e = chunk(parent, 'Attributes')
    it = items(e, 2)
    b = etree.SubElement(it, 'item', {'name': 'Bounds', 'type_name': 'gh_drawing_rectanglef', 'type_code': '35'})
    for tag, val in [('X',x), ('Y',y), ('W',w), ('H',h)]:
        etree.SubElement(b, tag).text = str(val)
    p = etree.SubElement(it, 'item', {'name': 'Pivot', 'type_name': 'gh_drawing_pointf', 'type_code': '31'})
    etree.SubElement(p, 'X').text = str(x)
    etree.SubElement(p, 'Y').text = str(y)
    return e

def attrs_panel(parent, x=0, y=0, w=0, h=0):
    e = chunk(parent, 'Attributes')
    it = items(e, 5)
    b = etree.SubElement(it, 'item', {'name': 'Bounds', 'type_name': 'gh_drawing_rectanglef', 'type_code': '35'})
    for tag, val in [('X',x), ('Y',y), ('W',w), ('H',h)]:
        etree.SubElement(b, tag).text = str(val)
    item_int(it, 'MarginLeft', 0)
    item_int(it, 'MarginRight', 0)
    item_int(it, 'MarginTop', 0)
    p = etree.SubElement(it, 'item', {'name': 'Pivot', 'type_name': 'gh_drawing_pointf', 'type_code': '31'})
    etree.SubElement(p, 'X').text = str(x)
    etree.SubElement(p, 'Y').text = str(y)
    return e

def attrs_empty(parent):
    e = etree.SubElement(parent, 'chunk', {'name': 'Attributes'})
    return e

# ── Object builders (each returns a complete <chunk name="Object">) ──

def build_group(v07_obj, idx):
    nick = v07_obj.findtext('Nickname') or 'Group'
    desc = v07_obj.findtext('Description') or 'A group of Grasshopper objects'
    ig = iguid('v07', idx, 'Group')
    
    obj = etree.Element('chunk', {'name': 'Object', 'index': str(idx)})
    it = items(obj, 2)
    item_guid(it, 'GUID', COMPONENT_GUIDS['Group'])
    item(it, 'Name', 'Group')
    
    ck = chunks(obj, 1)
    cont = chunk(ck, 'Container')
    
    it = items(cont, 7)
    item_int(it, 'Border', 1)
    item_color(it, 'Colour', '150;170;135;255')
    item(it, 'Description', desc)
    item_int(it, 'ID_Count', 0)
    item_guid(it, 'InstanceGuid', ig)
    item(it, 'Name', 'Group')
    item(it, 'NickName', nick)
    
    ck2 = chunks(cont, 1)
    attrs_empty(ck2)
    
    return obj

def build_panel(v07_obj, idx):
    nick = v07_obj.findtext('Nickname') or 'Panel'
    text = v07_obj.findtext('Value') or ''
    ig = iguid('v07', idx, 'Panel')
    
    obj = etree.Element('chunk', {'name': 'Object', 'index': str(idx)})
    it = items(obj, 2)
    item_guid(it, 'GUID', COMPONENT_GUIDS['Panel'])
    item(it, 'Name', 'Panel')
    
    ck = chunks(obj, 1)
    cont = chunk(ck, 'Container')
    
    it = items(cont, 8)
    item(it, 'Description', 'A panel for custom notes and text values')
    item_guid(it, 'InstanceGuid', ig)
    item(it, 'Name', 'Panel')
    item(it, 'NickName', nick)
    item_bool(it, 'Optional', False)
    item_double(it, 'ScrollRatio', 0)
    item_int(it, 'SourceCount', 0)
    item(it, 'UserText', text)
    
    ck2 = chunks(cont, 2)
    attrs_panel(ck2)
    pp = chunk(ck2, 'PanelProperties')
    it = items(pp, 7)
    item_color(it, 'Colour', '255;255;250;90')
    item_bool(it, 'DrawIndices', True)
    item_bool(it, 'DrawPaths', True)
    item_bool(it, 'Multiline', True)
    item_bool(it, 'SpecialCodes', False)
    item_bool(it, 'Stream', False)
    item_bool(it, 'Wrap', True)
    
    return obj

def build_slider(v07_obj, idx):
    nick = v07_obj.findtext('Nickname') or 'Number Slider'
    mn = v07_obj.findtext('Min') or '0'
    mx = v07_obj.findtext('Max') or '1'
    dec = v07_obj.findtext('DecimalCount') or '0'
    vlist = v07_obj.findtext('ValueList') or ''
    values = [v.strip() for v in vlist.split(',') if v.strip()] if vlist else ['1']
    ig = iguid('v07', idx, 'Slider')
    
    obj = etree.Element('chunk', {'name': 'Object', 'index': str(idx)})
    it = items(obj, 2)
    item_guid(it, 'GUID', COMPONENT_GUIDS['Number Slider'])
    item(it, 'Name', 'Number Slider')
    
    ck = chunks(obj, 1)
    cont = chunk(ck, 'Container')
    
    it = items(cont, 16)
    item(it, 'Description', 'A Gene Pool')
    item_bool(it, 'DrawValue', True)
    item_guid(it, 'InstanceGuid', ig)
    item(it, 'Max', mx, 'gh_double', '6')
    item(it, 'Min', mn, 'gh_double', '6')
    item(it, 'Name', 'Number Slider')
    item(it, 'NickName', nick)
    item_int(it, 'Rounding', int(dec))
    item_bool(it, 'ShowCompile', True)
    item_bool(it, 'ShowPerturb', True)
    item_bool(it, 'ShowRecombine', True)
    item_bool(it, 'Slider', False)
    item_bool(it, 'Snap', True)
    item_double(it, 'Spacing', 0)
    item_bool(it, 'Symbolic', False)
    item_int(it, 'ValueCount', len(values))
    
    ck2 = chunks(cont, 2)
    attrs_bounds(ck2)
    
    # PersistentData
    pd = chunk(ck2, 'PersistentData')
    it = items(pd, 1)
    item_int(it, 'Count', 1)
    ck3 = chunks(pd, 1)
    branch = chunk(ck3, 'Branch', 0)
    it = items(branch, 2)
    item_int(it, 'Count', len(values))
    item(it, 'Path', '{0}')
    ck4 = chunks(branch, len(values))
    for vi, val in enumerate(values):
        ci = chunk(ck4, 'Item', vi)
        it = items(ci, 1)
        try:
            if '.' in val: item_double(it, val, val)
            else: item(it, 'number', val, 'gh_int32', '3')
        except:
            item(it, 'number', val)
    
    return obj

def build_python(v07_obj, idx):
    nick = v07_obj.findtext('Nickname') or 'Python 3 Script'
    desc = v07_obj.findtext('Description') or ''
    code = v07_obj.findtext('Code') or ''
    
    inputs_node = v07_obj.find('Inputs')
    outputs_node = v07_obj.find('Outputs')
    input_els = inputs_node.findall('Input') if inputs_node is not None else []
    output_els = outputs_node.findall('Output') if outputs_node is not None else []
    
    ig = iguid('v07', idx, 'Python')
    
    obj = etree.Element('chunk', {'name': 'Object', 'index': str(idx)})
    it = items(obj, 2)
    item_guid(it, 'GUID', COMPONENT_GUIDS['Python 3 Script'])
    item(it, 'Name', 'Python 3 Script')
    
    ck = chunks(obj, 1)
    cont = chunk(ck, 'Container')
    
    # Container items (14)
    it = items(cont, 14)
    item(it, 'Description', desc)
    item_bool(it, 'GraftStandardOutputLines', True)
    item_guid(it, 'InstanceGuid', ig)
    item_bool(it, 'MarshGuids', True)
    item_bool(it, 'MarshInputs', True)
    item_bool(it, 'MarshOutputs', True)
    item(it, 'Name', 'Python 3 Script')
    item(it, 'NickName', nick)
    item_int(it, 'ScriptComponentVersion', 3)
    item(it, 'Tooltip', '', 'gh_string', '10')
    item_bool(it, 'UsingLibraryInputParam', False)
    item_bool(it, 'UsingScriptInputParam', False)
    item_bool(it, 'UsingScriptOutputParam', False)
    item_bool(it, 'UsingStandardOutputParam', False)
    
    # 4 sub-chunks: Attributes, ParameterData, Script, ScriptEditor
    ck2 = chunks(cont, 4)
    attrs_bounds(ck2)
    
    # ParameterData
    pd = chunk(ck2, 'ParameterData')
    pd_items_count = 0
    if input_els: pd_items_count += 1 + len(input_els)  # InputCount + InputId[0..n]
    if output_els: pd_items_count += 1 + len(output_els)
    it = items(pd, pd_items_count)
    if input_els:
        item_int(it, 'InputCount', len(input_els))
        for i in range(len(input_els)):
            item_guid(it, 'InputId', iguid('v07', idx, 'PyIn', i), idx=i)
    if output_els:
        item_int(it, 'OutputCount', len(output_els))
        for j in range(len(output_els)):
            item_guid(it, 'OutputId', iguid('v07', idx, 'PyOut', j), idx=j)
    
    ck3 = chunks(pd, len(input_els) + len(output_els))
    
    for i, inp in enumerate(input_els):
        ip = chunk(ck3, 'InputParam', i)
        name = inp.get('name', f'I{i}')
        ip_ig = iguid('v07', idx, 'PyIn', i)
        it = items(ip, 12)
        item_bool(it, 'AllowTreeAccess', True)
        item(it, 'Description', f'Script input {name}.')
        item_guid(it, 'InstanceGuid', ip_ig)
        item(it, 'Name', name)
        item(it, 'NickName', name)
        item_bool(it, 'Optional', True)
        item_int(it, 'ScriptParamAccess', 0)
        item_int(it, 'ScriptParameterVersion', 2)
        item_bool(it, 'ShowTypeHints', True)
        item_int(it, 'SourceCount', 0)
        item(it, 'ToolTip', '')
        item_guid(it, 'TypeHintID', 'd60527f5-b5af-4ef6-8970-5f96fe412559')
        ck4 = chunks(ip, 2)
        attrs_bounds(ck4)
        cd = chunk(ck4, 'ConverterData')
        it = items(cd, 2)
        item(it, 'AssemblyName', 'System.Private.CoreLib')
        item(it, 'TypeName', 'System.Object')
    
    for j, outp in enumerate(output_els):
        op = chunk(ck3, 'OutputParam', j)
        name = outp.get('name', f'O{j}')
        nick_out = outp.get('nickname', name)
        op_ig = iguid('v07', idx, 'PyOut', j)
        it = items(op, 12)
        item_bool(it, 'AllowTreeAccess', False)
        item(it, 'Description', f'Script output {name}.')
        item_guid(it, 'InstanceGuid', op_ig)
        item(it, 'Name', name)
        item(it, 'NickName', nick_out)
        item_bool(it, 'Optional', False)
        item_int(it, 'ScriptParamAccess', 0)
        item_int(it, 'ScriptParameterVersion', 2)
        item_bool(it, 'ShowTypeHints', True)
        item_int(it, 'SourceCount', 0)
        item(it, 'ToolTip', '')
        item_guid(it, 'TypeHintID', '1c282eeb-dd16-439f-94e4-7d92b542fe8b')
        ck4 = chunks(op, 2)
        attrs_bounds(ck4)
        cd = chunk(ck4, 'ConverterData')
        it = items(cd, 2)
        item(it, 'AssemblyName', 'System.Private.CoreLib')
        item(it, 'TypeName', 'System.Object')
    
    # Script
    sc = chunk(ck2, 'Script')
    encoded = base64.b64encode(code.encode('utf-8')).decode('ascii')
    it = items(sc, 5)
    item_bool(it, 'MarshGuids', True)
    item_bool(it, 'MarshInputs', True)
    item_bool(it, 'MarshOutputs', True)
    item(it, 'Text', encoded)
    item(it, 'Title', nick)
    ck4 = chunks(sc, 1)
    ls = chunk(ck4, 'LanguageSpec')
    it = items(ls, 2)
    item(it, 'Taxon', '*.*.python')
    item(it, 'Version', '3.*')
    
    # ScriptEditor
    se = chunk(ck2, 'ScriptEditor')
    it = items(se, 1)
    sb = etree.SubElement(it, 'item', {'name': 'StartBounds', 'type_name': 'gh_drawing_rectangle', 'type_code': '34'})
    for tag in ['X', 'Y', 'W', 'H']:
        etree.SubElement(sb, tag).text = '0'
    
    return obj

# ── Native component parameter specs (correct counts per component type) ──
NATIVE_SPECS = {
    'Area':          {'inputs': ['Geometry'], 'outputs': ['Area', 'Centroid']},
    'DeconstructBrep': {'inputs': ['Brep'], 'outputs': ['Faces', 'Edges', 'Vertices']},
    'JoinCurves':    {'inputs': ['Curves', 'Preserve'], 'outputs': ['Curve']},
    'Deconstruct2DPolyline': {'inputs': ['Polyline'], 'outputs': ['Points', 'Segments', 'Vertices']},
    'Explode':       {'inputs': ['Curve'], 'outputs': ['Segments', 'Vertices']},
    'CurveMiddle':   {'inputs': ['Curve'], 'outputs': ['Point']},
    'CurveFrame':    {'inputs': ['Curve', 'Parameter'], 'outputs': ['Frame']},
    'Angle':         {'inputs': ['Vector A', 'Vector B', 'Plane'], 'outputs': ['Angle', 'Reflex']},
    'Vector2Pt':     {'inputs': ['A', 'B', 'Unitize'], 'outputs': ['Vector', 'Length']},
    'TapirReceive':  {'inputs': [], 'outputs': ['Geometry']},
    'DFImport':      {'inputs': ['FilePath'], 'outputs': ['Features']},
}

# Native param type hints (GUIDs for common Grasshopper parameter types)
PARAM_GUIDS = {
    'Brep':       '7aa3d896-4e8b-4ff3-a5d1-bfb55c606b4f',
    'Curve':      '877dc5d5-c30c-4fef-8278-79c5417aefbe',
    'Curves':     '877dc5d5-c30c-4fef-8278-79c5417aefbe',
    'Point':      'd203e177-3d25-446d-bd4d-ec68468a529c',
    'Geometry':   '1426fb8c-df92-46ef-af1d-8c693012565c',
    'Surface':    '0cbd88f2-96b0-492d-9c45-5a2e497b1d38',
    'Polyline':   'e791296e-16ee-4897-8ad3-285a1a105084',
    'Vector':     'acd15f9f-4503-42ab-b888-1158a382dcb2',
    'Plane':      'c5891286-d12e-457d-85dc-70d08e1e951e',
    'Number':     'a7024d4e-4180-4d91-911e-1aaea1b876f6',
    'Integer':    'a7024d4e-4180-4d91-911e-1aaea1b876f6',
    'Boolean':    '89c1ed04-6ae1-418b-a6e1-30c4028c2342',
    'FilePath':   'f8e8e4e0-4d3c-4c3b-9a4a-5f2f2c3e4b5f',
    'Features':   '00000000-0000-0000-0000-000000000000',
    'Vertices':   'd203e177-3d25-446d-bd4d-ec68468a529c',
    'Faces':      '0cbd88f2-96b0-492d-9c45-5a2e497b1d38',
    'Edges':      '877dc5d5-c30c-4fef-8278-79c5417aefbe',
    'Segments':   '877dc5d5-c30c-4fef-8278-79c5417aefbe',
    'Centroid':   'd203e177-3d25-446d-bd4d-ec68468a529c',
    'Area':       'a7024d4e-4180-4d91-911e-1aaea1b876f6',
    'Length':     'a7024d4e-4180-4d91-911e-1aaea1b876f6',
    'Angle':      'a7024d4e-4180-4d91-911e-1aaea1b876f6',
    'Reflex':     'a7024d4e-4180-4d91-911e-1aaea1b876f6',
    'Frame':      'c5891286-d12e-457d-85dc-70d08e1e951e',
    'Unitize':    '89c1ed04-6ae1-418b-a6e1-30c4028c2342',
    'Preserve':   '89c1ed04-6ae1-418b-a6e1-30c4028c2342',
}

def get_param_guid(param_name):
    """Get the correct parameter type GUID for a given parameter name."""
    # Map common param names to their type GUIDs
    pn = param_name.strip()
    if pn in PARAM_GUIDS:
        return PARAM_GUIDS[pn]
    # Try case-insensitive
    for k, v in PARAM_GUIDS.items():
        if k.lower() == pn.lower():
            return v
    return '00000000-0000-0000-0000-000000000000'

def build_native(v07_obj, idx, obj_class):
    nick = v07_obj.findtext('Nickname') or ''
    desc = v07_obj.findtext('Description') or ''
    spec = NATIVE_SPECS.get(obj_class, {'inputs': [], 'outputs': []})
    ig = iguid('v07', idx, obj_class)
    guid = component_guid(v07_obj.get('type', ''), v07_obj.findtext('Name') or '')
    display_name = v07_obj.findtext('Name') or obj_class
    
    # Use component display name from spec
    disp_map = {
        'Area': 'Area', 'DeconstructBrep': 'Deconstruct Brep', 'JoinCurves': 'Join Curves',
        'Deconstruct2DPolyline': '2D Polyline', 'Explode': 'Explode',
        'CurveMiddle': 'Curve Middle', 'CurveFrame': 'Curve Frame', 'Angle': 'Angle',
        'Vector2Pt': 'Vector 2Pt', 'TapirReceive': 'Tapir Receive Geometry',
        'DFImport': 'Import GeoJSON',
    }
    disp_name = disp_map.get(obj_class, display_name)
    
    obj = etree.Element('chunk', {'name': 'Object', 'index': str(idx)})
    it = items(obj, 2)
    item_guid(it, 'GUID', guid)
    item(it, 'Name', disp_name)
    
    ck = chunks(obj, 1)
    cont = chunk(ck, 'Container')
    
    # Container items
    it = items(cont, 4)
    item(it, 'Description', desc)
    item_guid(it, 'InstanceGuid', ig)
    item(it, 'Name', disp_name)
    item(it, 'NickName', nick)
    
    # Sub-chunks: Attributes + inputs + outputs
    total_chunks = 1 + len(spec['inputs']) + len(spec['outputs'])
    ck2 = chunks(cont, total_chunks)
    attrs_bounds(ck2)
    
    for i, pname in enumerate(spec['inputs']):
        pi = chunk(ck2, 'param_input', i)
        pi_ig = iguid('v07', idx, obj_class, 'in', i)
        pi_guid = get_param_guid(pname)
        
        it = items(pi, 6)
        item(it, 'Description', f'Script input {pname}.')
        item_guid(it, 'InstanceGuid', pi_ig)
        item(it, 'Name', pname)
        item(it, 'NickName', pname)
        item_bool(it, 'Optional', False)
        item_int(it, 'SourceCount', 0)
        
        ck3 = chunks(pi, 1)
        attrs_bounds(ck3)
    
    for j, pname in enumerate(spec['outputs']):
        po = chunk(ck2, 'param_output', j)
        po_ig = iguid('v07', idx, obj_class, 'out', j)
        po_guid = get_param_guid(pname)
        
        it = items(po, 6)
        item(it, 'Description', f'Script output {pname}.')
        item_guid(it, 'InstanceGuid', po_ig)
        item(it, 'Name', pname)
        item(it, 'NickName', pname)
        item_bool(it, 'Optional', False)
        item_int(it, 'SourceCount', 0)
        
        ck3 = chunks(po, 1)
        attrs_bounds(ck3)
    
    return obj

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
        if nkey.replace('_', ' ') in oname:
            return TYPE_TO_CLASS[nkey]
    return 'Generic'

# ── Builders dispatch ──
def build_object(v07_obj, idx):
    obj_class = classify_obj(v07_obj)
    
    if obj_class == 'Group':
        return build_group(v07_obj, idx), obj_class
    elif obj_class == 'Panel':
        return build_panel(v07_obj, idx), obj_class
    elif obj_class == 'Slider':
        return build_slider(v07_obj, idx), obj_class
    elif obj_class == 'Python':
        return build_python(v07_obj, idx), obj_class
    elif obj_class in NATIVE_SPECS:
        return build_native(v07_obj, idx, obj_class), obj_class
    else:
        # Unknown: fallback to Generic native
        return build_native(v07_obj, idx, 'Generic'), obj_class

# ── Main ──
def convert(input_path, output_path):
    v07_tree = etree.parse(input_path)
    v07_root = v07_tree.getroot()
    doc_obj = v07_root.find('Object')
    objects_node = doc_obj.find('Objects')
    obj_list = objects_node.findall('Object')
    print(f"v07 objects: {len(obj_list)}")
    
    # Build new DefinitionObjects
    new_defobjs = etree.Element('chunk', {'name': 'DefinitionObjects'})
    it = items(new_defobjs, 1)
    item_int(it, 'ObjectCount', len(obj_list))
    ck = chunks(new_defobjs, len(obj_list))
    
    for idx, v07_obj in enumerate(obj_list):
        obj_class = classify_obj(v07_obj)
        v07_name = v07_obj.findtext('Name') or '??'
        
        new_obj, built_class = build_object(v07_obj, idx)
        status = "[FALLBACK]" if built_class not in NATIVE_SPECS and built_class not in ('Group','Panel','Slider','Python') else ""
        
        print(f"  [{idx:2d}] {v07_name[:40]:40s} -> {built_class:20s} {status}")
        
        if new_obj is not None:
            ck.append(new_obj)
    
    # Load v06 for header
    v06_path = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx"
    v06_tree = etree.parse(v06_path)
    v06_root_copy = v06_tree.getroot()
    
    old_defobjs = v06_root_copy.find('.//chunk[@name="DefinitionObjects"]')
    if old_defobjs is not None:
        parent = old_defobjs.getparent()
        if parent is not None:
            parent.replace(old_defobjs, new_defobjs)
    
    xml_bytes = etree.tostring(v06_root_copy, encoding='utf-8', pretty_print=True, xml_declaration=True)
    
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
