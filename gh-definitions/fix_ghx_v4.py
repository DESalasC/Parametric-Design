# -*- coding: utf-8 -*-
"""
GHX Fixer v4: Convierte GHX simplificado a formato GH_IO nativo usando
F1_Contexto_v06.ghx como plantilla de referencia para estructura exacta.

Diferencias clave vs v3:
- Componentes nativos usan param_input/param_output (no InputParam/OutputParam)
- Python scripts usan chunk Script + LanguageSpec (no item CodeInput)
- Object-level: solo GUID y Name
- Container incluye Attributes, InstanceGuid, etc.
"""
import xml.etree.ElementTree as ET
import uuid, hashlib, sys, os, base64
from datetime import datetime, timezone

# Component GUIDs extracted from F1_Contexto_v06.ghx (Grasshopper 8.33)

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
    'Vector 2Pt': '934ede4a-924a-4973-bb05-0dc4b36fae75',
    'Vector2Pt': '934ede4a-924a-4973-bb05-0dc4b36fae75',
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
    '2D Polyline': 'b71dc107-4be8-4a96-86d8-a656c502f71c',
    'Deconstruct2DPolyline': 'b71dc107-4be8-4a96-86d8-a656c502f71c',
    'File Path': '06953bda-1d37-4d58-9b38-4b3c74e54c8f',
    'Boolean Toggle': '2e78987b-9dfb-42a2-8b76-3923ac8bd91a',
    'GH_BooleanToggle': '2e78987b-9dfb-42a2-8b76-3923ac8bd91a',
    'Curve': 'd5967b9f-e8ee-436b-a8ad-29fdcecf32d5',
    'Point': 'fbac3e32-f100-4292-8692-77240a42fd1a',
    'Mesh': 'b17bfd88-3eeb-4531-bd62-f659c75a90b3',
    'Bounding Box': '0bb3d234-9097-45db-9998-621639c87d3b',
    'Deconstruct Mesh': 'ba2d8f57-0738-42b4-b5a5-fe4d853517eb',
    'Move': 'e9eb1dcf-92f6-4d4d-84ae-96222d60f56b',
    'Extrude': '962034e9-cc27-4394-afc4-5c16e3447cf9',
    'Unit Z': '9103c240-a6a9-4223-9b42-dbd19bf38e2b',
    'Relay': 'b6236720-8d88-4289-93c3-ac4c99f9b97b',
    'Value List': '00027467-0d24-4fa7-b178-8dc0ac5f42ec',
    'Construct Domain': 'd1a28e95-cf96-4936-bf34-8bf142d731bf',
    'Discontinuity': '269eaa85-9997-4d77-a9ba-4c58cb45c9d3',
    # Well-known Grasshopper component GUIDs (from GH SDK)
    'DeconstructBrep': '8d372bdc-9800-45e9-8a26-6e33c5253e21',
    'JoinCurves': '8073a420-6bec-49e3-9b18-367f6fd76ac3',
    'CurveFrame': '6b2a5853-07aa-4329-ba84-0a5d46b51dbd',
    'Angle': 'b464fccb-50e7-41bd-9789-8438db9bea9f',
    'GH_Import': '3728e6f7-2fc5-4b86-911a-386f511e152f',  # DF Model From geoJSON (Dragonfly)
    # Plugin components
    'Tapir.GH.ReceiveGeometry': '8ee23aed-ee26-4966-ba00-6d718e844dbd',  # TeamworkReceive
}

def get_component_guid(obj_type, obj_name):
    """Get the correct Component GUID for a given object."""
    # Try exact type match first
    for key in obj_type.split('.'):
        mapped = COMPONENT_GUIDS.get(key)
        if mapped:
            return mapped
    # Try full type
    mapped = COMPONENT_GUIDS.get(obj_type)
    if mapped:
        return mapped
    # Try name match
    mapped = COMPONENT_GUIDS.get(obj_name)
    if mapped:
        return mapped
    # Default: use a well-known Grasshopper base GUID
    return '00000000-0000-0000-0000-000000000000'

def now_ticks():
    return str(int(datetime.now(timezone.utc).timestamp() * 10000000 + 621355968000000000))

def esc(s):
    if s is None: return ""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

class X:
    def __init__(self):
        self.lines = []
        self.indent = 0
        self.stack = []
    def tag(self, name, attrs=None, text=None, close=False):
        prefix = "  " * self.indent
        attr_str = ""
        if attrs:
            parts = [f'{k}="{esc(str(v))}"' for k, v in attrs.items()]
            attr_str = " " + " ".join(parts)
        if close:
            self.lines.append(f"{prefix}</{name}>")
        elif text is not None:
            self.lines.append(f"{prefix}<{name}{attr_str}>{text}</{name}>")
        else:
            self.lines.append(f"{prefix}<{name}{attr_str}>")
            self.stack.append(name)
            self.indent += 1
    def close(self):
        name = self.stack.pop()
        self.indent -= 1
        self.tag(name, close=True)
    def item(self, name, value, tn="gh_string", tc="10"):
        self.tag("item", {"name": name, "type_name": tn, "type_code": tc}, text=esc(str(value)))
    def item_int(self, name, value): self.item(name, str(value), "gh_int32", "3")
    def item_bool(self, name, value): self.item(name, "true" if value else "false", "gh_bool", "1")
    def item_guid(self, name, value, idx=None):
        attrs = {"name": name, "type_name": "gh_guid", "type_code": "9"}
        if idx is not None: attrs["index"] = str(idx)
        self.tag("item", attrs, text=str(value))
    def items_block(self, count): self.tag("items", {"count": str(count)})
    def chunks_block(self, count): self.tag("chunks", {"count": str(count)})
    def raw(self, line): self.lines.append("  " * self.indent + line)
    def __str__(self): return "\n".join(self.lines)

# ── Component type helpers ──

# Types that are native Grasshopper components (use param_input/param_output)
NATIVE_TYPES = {
    'DeconstructBrep', 'JoinCurves', 'Area', 'Deconstruct2DPolyline',
    'Explode', 'CurveMiddle', 'CurveFrame', 'Angle', 'Vector2Pt',
    'GH_Import', 'GH_Panel', 'GH_Palette', 'GH_Group', 'GH_NumberSlider',
    'GH_BooleanToggle',
}

def is_python(obj_elem):
    """Check if this is a Python script component."""
    return 'Python' in (obj_elem.get('type', '') or '')

def is_native(obj_elem):
    """Check if this is a native Grasshopper component."""
    t = obj_elem.get('type', '') or ''
    for nt in NATIVE_TYPES:
        if nt in t:
            return True
    return False

def is_group(obj_elem):
    t = obj_elem.get('type', '') or ''
    return 'GH_Group' in t

def is_panel(obj_elem):
    t = obj_elem.get('type', '') or ''
    return 'GH_Panel' in t or 'GH_Palette' in t

# ── Converter ──

def convert(input_path, output_path, template_path=None):
    tree = ET.parse(input_path)
    root = tree.getroot()
    doc_obj = root.find('Object')
    if doc_obj is None:
        print("ERROR: No <Object> under root")
        return False
    
    x = X()
    
    # Header + Archive
    x.raw('<?xml version="1.0" encoding="utf-8" standalone="yes"?>')
    x.raw('<Archive name="Root">')
    x.stack.append("Archive")
    x.raw('  <!--Grasshopper archive-->')
    x.raw('  <!--Fixed by GhDefinitionExplorer v4-->')
    x.indent = 1
    
    # ArchiveVersion
    x.items_block(1)
    x.tag("item", {"name": "ArchiveVersion", "type_name": "gh_version", "type_code": "80"})
    x.raw("<Major>0</Major>")
    x.raw("<Minor>2</Minor>")
    x.raw("<Revision>2</Revision>")
    x.close()
    x.close()
    
    x.chunks_block(1)
    
    # === Definition ===
    x.tag("chunk", {"name": "Definition"})
    
    # plugin_version
    x.items_block(1)
    x.tag("item", {"name": "plugin_version", "type_name": "gh_version", "type_code": "80"})
    x.raw("<Major>1</Major>")
    x.raw("<Minor>0</Minor>")
    x.raw("<Revision>8</Revision>")
    x.close()
    x.close()
    
    # Copy structural chunks from template if available
    structural_chunks = {}
    if template_path and os.path.exists(template_path):
        tpl_tree = ET.parse(template_path)
        tpl_root = tpl_tree.getroot()
        for def_chunk in tpl_root.iter('chunk'):
            if def_chunk.get('name') == 'Definition':
                for child in def_chunk:
                    if child.tag == 'chunks':
                        for sub in child:
                            name = sub.get('name', '')
                            if name in ('DocumentHeader', 'RcpLayout', 'ValueTable', 'GHALibraries',
                                       'DefinitionProperties'):
                                structural_chunks[name] = ET.tostring(sub, encoding='unicode')
    
    chunk_names = ['DocumentHeader', 'DefinitionProperties', 'RcpLayout', 'ValueTable',
                   'GHALibraries', 'DefinitionObjects']
    
    x.chunks_block(len(chunk_names))
    
    for cn in chunk_names:
        if cn == 'DefinitionObjects':
            write_definition_objects(x, doc_obj)
        elif cn == 'DefinitionProperties':
            write_definition_properties(x, doc_obj, structural_chunks.get(cn))
        elif cn in structural_chunks:
            # Copy raw XML from template
            for line in structural_chunks[cn].split('\n'):
                stripped = line.strip()
                if stripped:
                    x.raw(stripped)
        else:
            write_minimal_chunk(x, cn)
    
    # Close remaining
    x.close()  # /chunks of Definition
    x.close()  # /Definition
    x.close()  # /chunks of Archive
    x.close()  # /Archive
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(x))
    print(f"Written: {output_path}")
    return True

def write_minimal_chunk(x, name):
    if name == 'DocumentHeader':
        x.tag("chunk", {"name": "DocumentHeader"})
        x.items_block(5)
        x.item_guid("DocumentID", str(uuid.uuid4()))
        x.item("Preview", "Shaded", "gh_string", "10")
        x.item_int("PreviewMeshType", 1)
        x.tag("item", {"name": "PreviewNormal", "type_name": "gh_drawing_color", "type_code": "36"})
        x.raw("<ARGB>100;150;0;0</ARGB>")
        x.close()
        x.tag("item", {"name": "PreviewSelected", "type_name": "gh_drawing_color", "type_code": "36"})
        x.raw("<ARGB>100;0;150;0</ARGB>")
        x.close()
        x.close()
        x.close()
    elif name == 'RcpLayout':
        x.tag("chunk", {"name": "RcpLayout"})
        x.items_block(1)
        x.item_int("GroupCount", 0)
        x.close()
        x.close()
    elif name == 'ValueTable':
        x.tag("chunk", {"name": "ValueTable"})
        x.items_block(4)
        x.item_int("ColumnCount", 0)
        x.item_int("RowCount", 0)
        x.item_bool("TableIsInvalid", False)
        x.item_bool("ValueTableIsUser", False)
        x.close()
        x.close()
    elif name == 'GHALibraries':
        x.tag("chunk", {"name": "GHALibraries"})
        x.items_block(1)
        x.item_int("Count", 0)
        x.close()
        x.chunks_block(0)
        x.close()
        x.close()

def write_definition_properties(x, doc_obj, tpl_xml=None):
    doc_name = doc_obj.findtext('Name') or doc_obj.get('name', 'Unknown')
    doc_desc = doc_obj.findtext('Description') or ''
    
    x.tag("chunk", {"name": "DefinitionProperties"})
    x.items_block(4)
    x.item("Date", now_ticks(), "gh_date", "8")
    x.item("Description", doc_desc, "gh_string", "10")
    x.item_bool("KeepOpen", False)
    x.item("Name", doc_name, "gh_string", "10")
    x.close()
    
    # Sub-chunks from template or minimal
    x.chunks_block(3)
    
    # Revisions
    x.tag("chunk", {"name": "Revisions"})
    x.items_block(1)
    x.item_int("RevisionCount", 0)
    x.close()
    x.close()
    
    # Projection
    x.tag("chunk", {"name": "Projection"})
    x.items_block(2)
    x.tag("item", {"name": "Target", "type_name": "gh_drawing_point", "type_code": "30"})
    x.raw("<X>0</X>")
    x.raw("<Y>0</Y>")
    x.close()
    x.item("Zoom", "1.0", "gh_single", "5")
    x.close()
    x.close()
    
    # Views
    x.tag("chunk", {"name": "Views"})
    x.items_block(1)
    x.item_int("ViewCount", 0)
    x.close()
    x.close()
    
    x.close()  # /chunks
    x.close()  # /DefinitionProperties

def write_definition_objects(x, doc_obj):
    objects_node = doc_obj.find('Objects')
    obj_list = objects_node.findall('Object') if objects_node is not None else []
    
    x.tag("chunk", {"name": "DefinitionObjects"})
    x.items_block(1)
    x.item_int("ObjectCount", len(obj_list))
    x.close()
    
    x.chunks_block(len(obj_list))
    for idx, obj in enumerate(obj_list):
        write_object(x, obj, idx)
    x.close()  # /chunks
    x.close()  # /DefinitionObjects

def write_object(x, obj, index):
    obj_type = obj.get('type', '')
    obj_name = obj.findtext('Name') or obj.get('name', '')
    obj_id = obj.findtext('ID') or ''
    obj_nick = obj.findtext('Nickname') or obj_name
    obj_desc = obj.findtext('Description') or ''
    guid = get_component_guid(obj_type, obj_name)
    
    x.tag("chunk", {"name": "Object", "index": str(index)})
    
    # Only GUID + Name at Object level
    x.items_block(2)
    x.item_guid("GUID", guid)
    x.item("Name", obj_name, "gh_string", "10")
    x.close()
    
    x.chunks_block(1)
    x.tag("chunk", {"name": "Container"})
    
    if is_python(obj):
        write_python_container(x, obj, guid, obj_name, obj_nick, obj_desc)
    elif is_native(obj):
        write_native_container(x, obj, guid, obj_name, obj_nick, obj_desc)
    elif is_group(obj):
        write_group_container(x, obj, guid, obj_name, obj_nick)
    elif is_panel(obj):
        write_panel_container(x, obj, guid, obj_name, obj_nick, obj_desc)
    else:
        write_generic_container(x, obj, guid, obj_name, obj_nick, obj_desc)
    
    x.close()  # /Container
    x.close()  # /chunks
    x.close()  # /Object

def write_container_items(x, obj, include_code=False):
    """Write standard Container items (skipping Inputs/Outputs/Code)."""
    items = []
    for child in obj:
        tag = child.tag
        if tag in ('Name', 'ID', 'Nickname', 'Description', 'Inputs', 'Outputs',
                   'OptionalParams', 'Code', 'Attributes', 'Wires'):
            continue
        text = (child.text or '').strip()
        if not text:
            continue
        items.append((tag, text))
    
    if include_code:
        code_node = obj.find('Code')
        if code_node is not None and code_node.text and code_node.text.strip():
            items.append(('CodeInput', code_node.text.strip()))
    
    return items

def write_native_container(x, obj, guid, obj_name, obj_nick, obj_desc):
    """Native Grasshopper component: uses param_input/param_output."""
    instance_guid = str(uuid.uuid4())
    
    # Container items
    extra_items = write_container_items(x, obj, include_code=False)
    
    item_count = 4 + len(extra_items)
    x.items_block(item_count)
    x.item("Description", obj_desc, "gh_string", "10")
    x.item_guid("InstanceGuid", instance_guid)
    x.item("Name", obj_name, "gh_string", "10")
    x.item("NickName", obj_nick, "gh_string", "10")
    for name, value in extra_items:
        if name in ('Min', 'Max', 'DecimalCount', 'SourceCount'):
            try:
                int(value); x.item_int(name, value)
            except:
                x.item(name, value, "gh_string", "10")
        elif name == 'ValueList':
            x.item(name, value, "gh_string", "10")
        elif name == 'Value':
            x.item(name, value, "gh_string", "10")
        elif name == 'Color':
            x.item(name, value, "gh_string", "10")
        elif name == 'MemberIds':
            x.item(name, value, "gh_string", "10")
        elif name == 'UserText':
            x.item(name, value, "gh_string", "10")
        elif name == 'ScrollRatio':
            try:
                float(value); x.item(name, value, "gh_double", "6")
            except:
                x.item(name, value)
        else:
            x.item(name, value, "gh_string", "10")
    x.close()
    
    # Sub-chunks: Attributes + parameters
    inputs_node = obj.find('Inputs')
    outputs_node = obj.find('Outputs')
    input_els = inputs_node.findall('Input') if inputs_node is not None else []
    output_els = outputs_node.findall('Output') if outputs_node is not None else []
    
    sub_chunk_count = 1  # Attributes
    sub_chunk_count += len(input_els) + len(output_els)
    
    x.chunks_block(sub_chunk_count)
    
    # Attributes
    write_attributes(x)
    
    # param_input
    for i, inp in enumerate(input_els):
        write_param_input(x, inp, i, obj_name)
    
    # param_output
    for j, outp in enumerate(output_els):
        write_param_output(x, outp, j, obj_name)
    
    x.close()  # /chunks

def write_param_input(x, inp, index, obj_name):
    x.tag("chunk", {"name": "param_input", "index": str(index)})
    inp_name = inp.get('name', f'Input{index}')
    inp_nick = inp_name
    instance_guid = mkguid(f"{obj_name}_in_{index}")
    source = inp.get('source', '')
    
    item_count = 7 if source else 6
    x.items_block(item_count)
    x.item("Description", f"Script input {inp_name}.", "gh_string", "10")
    x.item_guid("InstanceGuid", instance_guid)
    x.item("Name", inp_name, "gh_string", "10")
    x.item("NickName", inp_nick, "gh_string", "10")
    x.item_bool("Optional", False)
    if source:
        x.item_guid("Source", mkguid(source))
    x.item_int("SourceCount", 1 if source else 0)
    x.close()
    
    x.chunks_block(1)
    write_attributes(x)
    x.close()  # /chunks
    x.close()  # /param_input

def write_param_output(x, outp, index, obj_name):
    x.tag("chunk", {"name": "param_output", "index": str(index)})
    out_name = outp.get('name', f'Output{index}')
    out_nick = outp.get('nickname', out_name)
    instance_guid = mkguid(f"{obj_name}_out_{index}")
    
    x.items_block(6)
    x.item("Description", f"Script output {out_name}.", "gh_string", "10")
    x.item_guid("InstanceGuid", instance_guid)
    x.item("Name", out_name, "gh_string", "10")
    x.item("NickName", out_nick, "gh_string", "10")
    x.item_bool("Optional", False)
    x.item_int("SourceCount", 0)
    x.close()
    
    x.chunks_block(1)
    write_attributes(x)
    x.close()
    x.close()

def write_python_container(x, obj, guid, obj_name, obj_nick, obj_desc):
    """Python script component."""
    instance_guid = str(uuid.uuid4())
    code_node = obj.find('Code')
    code_text = (code_node.text or '').strip() if code_node is not None else ''
    
    # Container items
    x.items_block(14)
    x.item("Description", obj_desc or "", "gh_string", "10")
    x.item_bool("GraftStandardOutputLines", True)
    x.item_guid("InstanceGuid", instance_guid)
    x.item_bool("MarshGuids", True)
    x.item_bool("MarshInputs", True)
    x.item_bool("MarshOutputs", True)
    x.item("Name", obj_name, "gh_string", "10")
    x.item("NickName", obj_nick, "gh_string", "10")
    x.item_int("ScriptComponentVersion", 3)
    x.item("Tooltip", "", "gh_string", "10")
    x.item_bool("UsingLibraryInputParam", False)
    x.item_bool("UsingScriptInputParam", False)
    x.item_bool("UsingScriptOutputParam", False)
    x.item_bool("UsingStandardOutputParam", False)
    x.close()
    
    
    # Sub-chunks: Attributes + ParameterData + Script + ScriptEditor
    x.chunks_block(4)
    
    write_attributes(x)
    
    # ParameterData
    inputs_node = obj.find('Inputs')
    outputs_node = obj.find('Outputs')
    input_els = inputs_node.findall('Input') if inputs_node is not None else []
    output_els = outputs_node.findall('Output') if outputs_node is not None else []
    write_python_parameter_data(x, input_els, output_els, obj_name)
    
    # Script chunk
    write_python_script(x, code_text, obj_nick)
    
    # ScriptEditor
    write_script_editor(x)
    
    
    x.close()  # /chunks

def write_python_parameter_data(x, input_els, output_els, obj_name):
    x.tag("chunk", {"name": "ParameterData"})
    
    pi = 0
    if input_els: pi += 1 + len(input_els)
    if output_els: pi += 1 + len(output_els)
    
    x.items_block(pi)
    if input_els:
        x.item_int("InputCount", len(input_els))
        for i in range(len(input_els)):
            x.item_guid("InputId", mkguid(f"{obj_name}_in_{i}"), idx=i)
    if output_els:
        x.item_int("OutputCount", len(output_els))
        for j in range(len(output_els)):
            x.item_guid("OutputId", mkguid(f"{obj_name}_out_{j}"), idx=j)
    x.close()
    
    pc = len(input_els) + len(output_els)
    x.chunks_block(pc)
    
    for i, inp in enumerate(input_els):
        write_python_input_param(x, inp, i, obj_name)
    
    for j, outp in enumerate(output_els):
        write_python_output_param(x, outp, j, obj_name)
    
    x.close()
    x.close()

def write_python_input_param(x, inp, index, obj_name):
    x.tag("chunk", {"name": "InputParam", "index": str(index)})
    inp_name = inp.get('name', f'Input{index}')
    instance_guid = mkguid(f"{obj_name}_in_{index}")
    source = inp.get('source', '')
    
    x.items_block(13)
    x.item_bool("AllowTreeAccess", True)
    x.item("Description", f"Script input {inp_name}.", "gh_string", "10")
    x.item_guid("InstanceGuid", instance_guid)
    x.item("Name", inp_name, "gh_string", "10")
    x.item("NickName", inp_name, "gh_string", "10")
    x.item_bool("Optional", True)
    x.item_int("ScriptParamAccess", 0)
    x.item_int("ScriptParameterVersion", 2)
    x.item_bool("ShowTypeHints", True)
    if source:
        x.item_guid("Source", mkguid(source))
    x.item_int("SourceCount", 1 if source else 0)
    x.item("ToolTip", "", "gh_string", "10")
    x.item_guid("TypeHintID", "d60527f5-b5af-4ef6-8970-5f96fe412559")
    x.close()
    
    x.chunks_block(2)
    write_attributes(x)
    # ConverterData for Python inputs
    x.tag("chunk", {"name": "ConverterData"})
    x.items_block(2)
    x.item("AssemblyName", "System.Private.CoreLib", "gh_string", "10")
    x.item("TypeName", "System.Object", "gh_string", "10")
    x.close()
    x.close()
    x.close()  # /chunks
    x.close()  # /InputParam

def write_python_output_param(x, outp, index, obj_name):
    x.tag("chunk", {"name": "OutputParam", "index": str(index)})
    out_name = outp.get('name', f'Output{index}')
    out_nick = outp.get('nickname', out_name)
    instance_guid = mkguid(f"{obj_name}_out_{index}")
    
    x.items_block(12)
    x.item_bool("AllowTreeAccess", False)
    x.item("Description", f"Script output {out_name}.", "gh_string", "10")
    x.item_guid("InstanceGuid", instance_guid)
    x.item("Name", out_name, "gh_string", "10")
    x.item("NickName", out_nick, "gh_string", "10")
    x.item_bool("Optional", False)
    x.item_int("ScriptParamAccess", 0)
    x.item_int("ScriptParameterVersion", 2)
    x.item_bool("ShowTypeHints", True)
    x.item_int("SourceCount", 0)
    x.item("ToolTip", "", "gh_string", "10")
    x.item_guid("TypeHintID", "1c282eeb-dd16-439f-94e4-7d92b542fe8b")
    x.close()
    
    x.chunks_block(2)
    write_attributes(x)
    x.tag("chunk", {"name": "ConverterData"})
    x.items_block(2)
    x.item("AssemblyName", "System.Private.CoreLib", "gh_string", "10")
    x.item("TypeName", "System.Object", "gh_string", "10")
    x.close()
    x.close()
    x.close()
    x.close()

def write_python_script(x, code_text, title):
    x.tag("chunk", {"name": "Script"})
    # Encode code as base64
    encoded = base64.b64encode(code_text.encode('utf-8')).decode('ascii')
    x.items_block(5)
    x.item_bool("MarshGuids", True)
    x.item_bool("MarshInputs", True)
    x.item_bool("MarshOutputs", True)
    x.item("Text", encoded, "gh_string", "10")
    x.item("Title", title, "gh_string", "10")
    x.close()
    
    x.chunks_block(1)
    x.tag("chunk", {"name": "LanguageSpec"})
    x.items_block(2)
    x.item("Taxon", "*.*.python", "gh_string", "10")
    x.item("Version", "3.*", "gh_string", "10")
    x.close()
    x.close()
    x.close()
    x.close()

def write_script_editor(x):
    x.tag("chunk", {"name": "ScriptEditor"})
    x.items_block(1)
    x.tag("item", {"name": "StartBounds", "type_name": "gh_drawing_rectangle", "type_code": "34"})
    x.raw("<X>0</X>")
    x.raw("<Y>0</Y>")
    x.raw("<W>0</W>")
    x.raw("<H>0</H>")
    x.close()
    x.close()
    x.close()

def write_attributes(x):
    x.tag("chunk", {"name": "Attributes"})
    x.items_block(2)
    x.tag("item", {"name": "Bounds", "type_name": "gh_drawing_rectanglef", "type_code": "35"})
    x.raw("<X>0</X>")
    x.raw("<Y>0</Y>")
    x.raw("<W>0</W>")
    x.raw("<H>0</H>")
    x.close()
    x.tag("item", {"name": "Pivot", "type_name": "gh_drawing_pointf", "type_code": "31"})
    x.raw("<X>0</X>")
    x.raw("<Y>0</Y>")
    x.close()
    x.close()
    x.close()

def write_group_container(x, obj, guid, obj_name, obj_nick):
    """GH_Group: just has Attributes + MemberIds item."""
    instance_guid = str(uuid.uuid4())
    extra_items = write_container_items(x, obj)
    
    x.items_block(4 + len(extra_items))
    x.item("Description", "", "gh_string", "10")
    x.item_guid("InstanceGuid", instance_guid)
    x.item("Name", obj_name, "gh_string", "10")
    x.item("NickName", obj_nick, "gh_string", "10")
    for name, value in extra_items:
        x.item(name, value, "gh_string", "10")
    x.close()
    
    x.chunks_block(1)
    write_attributes(x)
    x.close()

def write_panel_container(x, obj, guid, obj_name, obj_nick, obj_desc):
    """GH_Panel/GH_Palette."""
    instance_guid = str(uuid.uuid4())
    extra_items = write_container_items(x, obj)
    
    x.items_block(4 + len(extra_items))
    x.item("Description", obj_desc or "A panel for custom notes and text values", "gh_string", "10")
    x.item_guid("InstanceGuid", instance_guid)
    x.item("Name", obj_name, "gh_string", "10")
    x.item("NickName", obj_nick, "gh_string", "10")
    for name, value in extra_items:
        x.item(name, value, "gh_string", "10")
    x.close()
    
    # Attributes + PanelProperties
    x.chunks_block(2)
    write_attributes(x)
    
    x.tag("chunk", {"name": "PanelProperties"})
    x.items_block(7)
    x.tag("item", {"name": "Colour", "type_name": "gh_drawing_color", "type_code": "36"})
    x.raw("<ARGB>255;255;255;255</ARGB>")
    x.close()
    x.item_bool("DrawIndices", True)
    x.item_bool("DrawPaths", True)
    x.item_bool("Multiline", True)
    x.item_bool("SpecialCodes", False)
    x.item_bool("Stream", False)
    x.item_bool("Wrap", True)
    x.close()
    x.close()
    
    x.close()  # /chunks

def write_generic_container(x, obj, guid, obj_name, obj_nick, obj_desc):
    """Fallback for unknown component types."""
    instance_guid = str(uuid.uuid4())
    extra_items = write_container_items(x, obj)
    
    x.items_block(4 + len(extra_items))
    x.item("Description", obj_desc, "gh_string", "10")
    x.item_guid("InstanceGuid", instance_guid)
    x.item("Name", obj_name, "gh_string", "10")
    x.item("NickName", obj_nick, "gh_string", "10")
    for name, value in extra_items:
        x.item(name, value, "gh_string", "10")
    x.close()
    
    # Attributes only
    x.chunks_block(1)
    write_attributes(x)
    x.close()

# ── Main ──

if __name__ == '__main__':
    input_path = sys.argv[1] if len(sys.argv) > 1 else r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx"
    output_path = sys.argv[2] if len(sys.argv) > 2 else input_path.replace('.ghx', '_v4.ghx')
    template = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx"
    
    success = convert(input_path, output_path, template)
    
    if success:
        print("\n--- Validating with GhDefinitionExplorer ---")
        import subprocess
        exe = r"D:\Work\LIBRARIES\GhDefinitionExplorer\bin\Release\net8.0\GhDefinitionExplorer.exe"
        result = subprocess.run([exe, output_path, output_path.replace('.ghx', '.json')],
                               capture_output=True, text=True)
        print(result.stdout)
        if result.stderr: print("STDERR:", result.stderr)
