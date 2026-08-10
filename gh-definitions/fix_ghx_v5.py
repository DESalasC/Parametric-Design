# -*- coding: utf-8 -*-
"""
GHX Fixer v5: Conversor GHX simplificado a GH_IO nativo.
Estructuras de Container validadas contra F1_Contexto_v06.ghx y test_06_plugin_component.ghx.
"""
import xml.etree.ElementTree as ET
import uuid, hashlib, sys, os, base64
from datetime import datetime, timezone

def mkguid(s):
    h = hashlib.md5(s.encode('utf-8')).digest()
    h = bytearray(h)
    h[6] = (h[6] & 0x0F) | 0x30
    h[8] = (h[8] & 0x3F) | 0x80
    return str(uuid.UUID(bytes=bytes(h)))

def now_ticks():
    return str(int(datetime.now(timezone.utc).timestamp() * 10000000 + 621355968000000000))

def esc(s):
    if s is None: return ""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# ── COMPONENT GUIDS (all validated) ──
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
    'Deconstruct2DPolyline': 'b71dc107-4be8-4a96-86d8-a656c502f71c',
    'DeconstructBrep': '8d372bdc-9800-45e9-8a26-6e33c5253e21',
    'JoinCurves': '8073a420-6bec-49e3-9b18-367f6fd76ac3',
    'CurveFrame': '6b2a5853-07aa-4329-ba84-0a5d46b51dbd',
    'Angle': 'b464fccb-50e7-41bd-9789-8438db9bea9f',
    'GH_Import': '3728e6f7-2fc5-4b86-911a-386f511e152f',
    'Tapir.GH.ReceiveGeometry': '8ee23aed-ee26-4966-ba00-6d718e844dbd',
    'ReceiveGeometry': '8ee23aed-ee26-4966-ba00-6d718e844dbd',
}

def get_component_guid(obj_type, obj_name):
    for key in obj_type.split('.'):
        m = COMPONENT_GUIDS.get(key)
        if m: return m
    m = COMPONENT_GUIDS.get(obj_type)
    if m: return m
    m = COMPONENT_GUIDS.get(obj_name)
    if m: return m
    return '00000000-0000-0000-0000-000000000000'

def is_python(obj_elem):
    return 'Python' in (obj_elem.get('type', '') or '')
def is_group(obj_elem):
    return 'GH_Group' in (obj_elem.get('type', '') or '')
def is_panel(obj_elem):
    t = obj_elem.get('type', '') or ''
    return 'GH_Panel' in t or 'GH_Palette' in t
def is_slider(obj_elem):
    return 'GH_NumberSlider' in (obj_elem.get('type', '') or '')

# ── XML Builder ──

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
    def item(self, name, value, tn="gh_string", tc="10", idx=None, empty=False):
        attrs = {"name": name, "type_name": tn, "type_code": tc}
        if idx is not None: attrs["index"] = str(idx)
        if empty:
            self.lines.append(f"{'  '*self.indent}<item name=\"{name}\" type_name=\"{tn}\" type_code=\"{tc}\" />")
        else:
            self.tag("item", attrs, text=esc(str(value)))
    def item_int(self, n, v): self.item(n, str(v), "gh_int32", "3")
    def item_bool(self, n, v): self.item(n, "true" if v else "false", "gh_bool", "1")
    def item_guid(self, n, v, idx=None):
        attrs = {"name": n, "type_name": "gh_guid", "type_code": "9"}
        if idx is not None: attrs["index"] = str(idx)
        self.tag("item", attrs, text=str(v))
    def item_color(self, n, argb):
        self.tag("item", {"name": n, "type_name": "gh_drawing_color", "type_code": "36"})
        self.raw(f"<ARGB>{argb}</ARGB>")
        self.close()
    def items_block(self, count): self.tag("items", {"count": str(count)})
    def chunks_block(self, count): self.tag("chunks", {"count": str(count)})
    def raw(self, line): self.lines.append("  " * self.indent + line)
    def self_close(self, name, attrs=None):
        prefix = "  " * self.indent
        attr_str = ""
        if attrs:
            parts = [f'{k}="{esc(str(v))}"' for k, v in attrs.items()]
            attr_str = " " + " ".join(parts)
        self.lines.append(f"{prefix}<{name}{attr_str} />")
    def __str__(self): return "\n".join(self.lines)

# ── Structural helpers ──

def write_version_item(x):
    x.tag("item", {"name": "ArchiveVersion", "type_name": "gh_version", "type_code": "80"})
    x.raw("<Major>0</Major>")
    x.raw("<Minor>2</Minor>")
    x.raw("<Revision>2</Revision>")
    x.close()

def write_plugin_version(x):
    x.tag("item", {"name": "plugin_version", "type_name": "gh_version", "type_code": "80"})
    x.raw("<Major>1</Major>")
    x.raw("<Minor>0</Minor>")
    x.raw("<Revision>8</Revision>")
    x.close()

def write_attrs(x, bounds=False):
    x.tag("chunk", {"name": "Attributes"})
    if bounds:
        x.items_block(2)
        x.tag("item", {"name": "Bounds", "type_name": "gh_drawing_rectanglef", "type_code": "35"})
        x.raw("<X>0</X>"); x.raw("<Y>0</Y>"); x.raw("<W>0</W>"); x.raw("<H>0</H>")
        x.close()
        x.tag("item", {"name": "Pivot", "type_name": "gh_drawing_pointf", "type_code": "31"})
        x.raw("<X>0</X>"); x.raw("<Y>0</Y>")
        x.close()
        x.close()
    else:
        # Empty self-closing Attributes (for Group)
        pass
    x.close()  # self-closing chunk

def write_panel_attrs(x):
    x.tag("chunk", {"name": "Attributes"})
    x.items_block(5)
    x.tag("item", {"name": "Bounds", "type_name": "gh_drawing_rectanglef", "type_code": "35"})
    x.raw("<X>0</X>"); x.raw("<Y>0</Y>"); x.raw("<W>0</W>"); x.raw("<H>0</H>")
    x.close()
    x.item_int("MarginLeft", 0)
    x.item_int("MarginRight", 0)
    x.item_int("MarginTop", 0)
    x.tag("item", {"name": "Pivot", "type_name": "gh_drawing_pointf", "type_code": "31"})
    x.raw("<X>0</X>"); x.raw("<Y>0</Y>")
    x.close()
    x.close()
    x.close()

def write_panel_props(x):
    x.tag("chunk", {"name": "PanelProperties"})
    x.items_block(7)
    x.item_color("Colour", "255;255;255;255")
    x.item_bool("DrawIndices", True)
    x.item_bool("DrawPaths", True)
    x.item_bool("Multiline", True)
    x.item_bool("SpecialCodes", False)
    x.item_bool("Stream", False)
    x.item_bool("Wrap", True)
    x.close()
    x.close()

# ── Component writers ──

def write_group_container(x, obj, obj_name):
    """Match v06 Group exactly: Border, Colour(ARGB), ID[0..n], ID_Count, InstanceGuid, Name, NickName empty."""
    ig = str(uuid.uuid4())
    member_ids_str = obj.findtext('MemberIds') or ''
    member_ids = [m.strip() for m in member_ids_str.split(',') if m.strip()]
    color_str = obj.findtext('Color') or '#FF8C00'
    # Parse color: #RRGGBB -> A;R;G;B (use default alpha 150)
    r, g, b = 170, 135, 255  # default
    if color_str.startswith('#') and len(color_str) >= 7:
        try:
            r = int(color_str[1:3], 16)
            g = int(color_str[3:5], 16)
            b = int(color_str[5:7], 16)
        except: pass
    
    item_count = 6 + len(member_ids)  # Border, Colour, Description, ID_Count, InstanceGuid, Name, NickName
    x.items_block(item_count)
    x.item_int("Border", 1)
    x.item_color("Colour", f"150;{r};{g};{b}")
    x.item("Description", "A group of Grasshopper objects", "gh_string", "10")
    for i, mid in enumerate(member_ids):
        # Convert member IDs to GUIDs
        x.item_guid("ID", mkguid(mid), idx=i)
    x.item_int("ID_Count", len(member_ids))
    x.item_guid("InstanceGuid", ig)
    x.item("Name", "Group", "gh_string", "10")
    x.item("NickName", "", "gh_string", "10", empty=True)
    x.close()
    
    x.chunks_block(1)
    write_attrs(x, bounds=False)  # self-closing
    x.close()

def write_panel_container(x, obj, obj_name, obj_nick, obj_desc):
    """Match v06 Panel: Description, InstanceGuid, Name, NickName(empty), Optional, ScrollRatio, SourceCount, UserText."""
    ig = str(uuid.uuid4())
    user_text = obj.findtext('Value') or ''
    
    x.items_block(8)
    x.item("Description", "A panel for custom notes and text values", "gh_string", "10")
    x.item_guid("InstanceGuid", ig)
    x.item("Name", "Panel", "gh_string", "10")
    x.item("NickName", "", "gh_string", "10", empty=True)
    x.item_bool("Optional", False)
    x.item("ScrollRatio", "0", "gh_double", "6")
    x.item_int("SourceCount", 0)
    x.item("UserText", user_text, "gh_string", "10")
    x.close()
    
    x.chunks_block(2)
    write_panel_attrs(x)
    write_panel_props(x)
    x.close()

def write_slider_container(x, obj, obj_name, obj_nick, obj_desc):
    """Number Slider (Gene Pool) container."""
    ig = str(uuid.uuid4())
    min_val = obj.findtext('Min') or '0'
    max_val = obj.findtext('Max') or '1'
    decimals = obj.findtext('DecimalCount') or '0'
    value_list = obj.findtext('ValueList') or ''
    
    # Number Slider items
    x.items_block(16)
    x.item("Description", "A Gene Pool", "gh_string", "10")
    x.item_bool("DrawValue", True)
    x.item_guid("InstanceGuid", ig)
    x.item("Max", max_val, "gh_double", "6")
    x.item("Min", min_val, "gh_double", "6")
    x.item("Name", "Number Slider", "gh_string", "10")
    x.item("NickName", obj_nick, "gh_string", "10")
    x.item_int("Rounding", int(decimals))
    x.item_bool("ShowCompile", True)
    x.item_bool("ShowPerturb", True)
    x.item_bool("ShowRecombine", True)
    x.item_bool("Slider", False)
    x.item_bool("Snap", True)
    x.item("Spacing", "0", "gh_double", "6")
    x.item_bool("Symbolic", False)
    x.item("ValueCount", str(len(value_list.split(',')) if value_list else 1), "gh_int32", "3")
    x.close()
    
    # Attributes + PersistentData
    x.chunks_block(2)
    write_attrs(x, bounds=True)
    
    # PersistentData with values
    x.tag("chunk", {"name": "PersistentData"})
    x.items_block(1)
    x.item_int("Count", 1)
    x.close()
    x.chunks_block(1)
    x.tag("chunk", {"name": "Branch", "index": "0"})
    values = [v.strip() for v in value_list.split(',') if v.strip()] if value_list else ['1']
    x.items_block(2)
    x.item_int("Count", len(values))
    x.item("Path", "{0}", "gh_string", "10")
    x.close()
    x.chunks_block(len(values))
    for vi, val in enumerate(values):
        x.tag("chunk", {"name": "Item", "index": str(vi)})
        x.items_block(1)
        # Determine if integer or double
        try:
            if '.' in val: x.item(val, val, "gh_double", "6")
            else: x.item_int("number", int(val))
        except:
            x.item("number", val, "gh_string", "10")
        x.close()
        x.close()
    x.close()  # /chunks of Branch
    x.close()  # /Branch
    x.close()  # /chunks of PersistentData
    x.close()  # /PersistentData
    
    x.close()  # /chunks

def write_native_container(x, obj, obj_name, obj_nick, obj_desc):
    """Native Grasshopper component with param_input/param_output."""
    ig = str(uuid.uuid4())
    inputs_node = obj.find('Inputs')
    outputs_node = obj.find('Outputs')
    input_els = inputs_node.findall('Input') if inputs_node is not None else []
    output_els = outputs_node.findall('Output') if outputs_node is not None else []
    
    # Container items
    x.items_block(4)
    x.item("Description", obj_desc or "", "gh_string", "10")
    x.item_guid("InstanceGuid", ig)
    x.item("Name", obj_name, "gh_string", "10")
    x.item("NickName", obj_nick, "gh_string", "10")
    x.close()
    
    # Sub-chunks: Attributes + inputs + outputs
    total_chunks = 1 + len(input_els) + len(output_els)
    x.chunks_block(total_chunks)
    write_attrs(x, bounds=True)
    
    for i, inp in enumerate(input_els):
        write_native_input(x, inp, i, obj_name)
    
    for j, outp in enumerate(output_els):
        write_native_output(x, outp, j, obj_name)
    
    x.close()

def write_native_input(x, inp, index, obj_name):
    x.tag("chunk", {"name": "param_input", "index": str(index)})
    inp_name = inp.get('name', f'Input{index}')
    ig = mkguid(f"{obj_name}_in_{index}")
    source = inp.get('source', '')
    
    x.items_block(6)
    x.item("Description", f"Script input {inp_name}.", "gh_string", "10")
    x.item_guid("InstanceGuid", ig)
    x.item("Name", inp_name, "gh_string", "10")
    x.item("NickName", inp_name, "gh_string", "10")
    x.item_bool("Optional", False)
    if source:
        x.item_guid("Source", mkguid(source))
    x.item_int("SourceCount", 1 if source else 0)
    x.close()
    
    x.chunks_block(1)
    write_attrs(x, bounds=True)
    x.close()
    x.close()

def write_native_output(x, outp, index, obj_name):
    x.tag("chunk", {"name": "param_output", "index": str(index)})
    out_name = outp.get('name', f'Output{index}')
    out_nick = outp.get('nickname', out_name)
    ig = mkguid(f"{obj_name}_out_{index}")
    
    x.items_block(6)
    x.item("Description", f"Script output {out_name}.", "gh_string", "10")
    x.item_guid("InstanceGuid", ig)
    x.item("Name", out_name, "gh_string", "10")
    x.item("NickName", out_nick, "gh_string", "10")
    x.item_bool("Optional", False)
    x.item_int("SourceCount", 0)
    x.close()
    
    x.chunks_block(1)
    write_attrs(x, bounds=True)
    x.close()
    x.close()

def write_python_container(x, obj, obj_name, obj_nick, obj_desc):
    """Python Script matching v06 format."""
    ig = str(uuid.uuid4())
    code_node = obj.find('Code')
    code_text = (code_node.text or '').strip() if code_node is not None else ''
    
    x.items_block(14)
    x.item("Description", obj_desc or "", "gh_string", "10")
    x.item_bool("GraftStandardOutputLines", True)
    x.item_guid("InstanceGuid", ig)
    x.item_bool("MarshGuids", True)
    x.item_bool("MarshInputs", True)
    x.item_bool("MarshOutputs", True)
    x.item("Name", "Python 3 Script", "gh_string", "10")
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
    write_attrs(x, bounds=True)
    
    # ParameterData
    inputs_node = obj.find('Inputs')
    outputs_node = obj.find('Outputs')
    input_els = inputs_node.findall('Input') if inputs_node is not None else []
    output_els = outputs_node.findall('Output') if outputs_node is not None else []
    write_python_params(x, input_els, output_els, obj_name)
    
    # Script
    write_py_script(x, code_text, obj_nick)
    
    # ScriptEditor
    write_py_editor(x)
    
    x.close()

def write_python_params(x, input_els, output_els, obj_name):
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
        write_py_input(x, inp, i, obj_name)
    
    for j, outp in enumerate(output_els):
        write_py_output(x, outp, j, obj_name)
    
    x.close()
    x.close()

def write_py_input(x, inp, index, obj_name):
    x.tag("chunk", {"name": "InputParam", "index": str(index)})
    inp_name = inp.get('name', f'Input{index}')
    ig = mkguid(f"{obj_name}_in_{index}")
    source = inp.get('source', '')
    
    item_count = 13 if source else 12
    x.items_block(item_count)
    x.item_bool("AllowTreeAccess", True)
    x.item("Description", f"Script input {inp_name}.", "gh_string", "10")
    x.item_guid("InstanceGuid", ig)
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
    write_attrs(x, bounds=True)
    x.tag("chunk", {"name": "ConverterData"})
    x.items_block(2)
    x.item("AssemblyName", "System.Private.CoreLib", "gh_string", "10")
    x.item("TypeName", "System.Object", "gh_string", "10")
    x.close()
    x.close()
    x.close()
    x.close()

def write_py_output(x, outp, index, obj_name):
    x.tag("chunk", {"name": "OutputParam", "index": str(index)})
    out_name = outp.get('name', f'Output{index}')
    out_nick = outp.get('nickname', out_name)
    ig = mkguid(f"{obj_name}_out_{index}")
    
    x.items_block(12)
    x.item_bool("AllowTreeAccess", False)
    x.item("Description", f"Script output {out_name}.", "gh_string", "10")
    x.item_guid("InstanceGuid", ig)
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
    write_attrs(x, bounds=True)
    x.tag("chunk", {"name": "ConverterData"})
    x.items_block(2)
    x.item("AssemblyName", "System.Private.CoreLib", "gh_string", "10")
    x.item("TypeName", "System.Object", "gh_string", "10")
    x.close()
    x.close()
    x.close()
    x.close()

def write_py_script(x, code_text, title):
    x.tag("chunk", {"name": "Script"})
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

def write_py_editor(x):
    x.tag("chunk", {"name": "ScriptEditor"})
    x.items_block(1)
    x.tag("item", {"name": "StartBounds", "type_name": "gh_drawing_rectangle", "type_code": "34"})
    x.raw("<X>0</X>"); x.raw("<Y>0</Y>"); x.raw("<W>0</W>"); x.raw("<H>0</H>")
    x.close()
    x.close()
    x.close()

# ── Main converter ──

def convert(input_path, output_path):
    tree = ET.parse(input_path)
    root = tree.getroot()
    doc_obj = root.find('Object')
    if doc_obj is None:
        print("ERROR: No <Object> under root")
        return False
    
    x = X()
    
    # Header
    x.raw('<?xml version="1.0" encoding="utf-8" standalone="yes"?>')
    x.raw('<Archive name="Root">')
    x.stack.append("Archive")
    x.raw('  <!--Grasshopper archive-->')
    x.raw('  <!--Grasshopper and GH_IO.dll are copyrighted by Robert McNeel & Associates-->')
    x.raw('  <!--Archive generated by GH_IO.dll file utility library {0.2.0002}-->')
    x.indent = 1
    
    x.items_block(1)
    write_version_item(x)
    x.close()
    
    x.chunks_block(1)
    x.tag("chunk", {"name": "Definition"})
    
    x.items_block(1)
    write_plugin_version(x)
    x.close()
    
    # Top-level chunks: DocumentHeader, DefinitionProperties, RcpLayout, ValueTable, GHALibraries, DefinitionObjects
    x.chunks_block(6)
    
    # DocumentHeader
    x.tag("chunk", {"name": "DocumentHeader"})
    x.items_block(5)
    x.item_guid("DocumentID", str(uuid.uuid4()))
    x.item("Preview", "Shaded", "gh_string", "10")
    x.item_int("PreviewMeshType", 1)
    x.item_color("PreviewNormal", "100;150;0;0")
    x.item_color("PreviewSelected", "100;0;150;0")
    x.close()
    x.close()
    
    # DefinitionProperties
    doc_name = doc_obj.findtext('Name') or doc_obj.get('name', 'Unknown')
    doc_desc = doc_obj.findtext('Description') or ''
    x.tag("chunk", {"name": "DefinitionProperties"})
    x.items_block(4)
    x.item("Date", now_ticks(), "gh_date", "8")
    x.item("Description", doc_desc, "gh_string", "10")
    x.item_bool("KeepOpen", False)
    x.item("Name", doc_name, "gh_string", "10")
    x.close()
    x.chunks_block(3)
    # Revisions
    x.tag("chunk", {"name": "Revisions"})
    x.items_block(1); x.item_int("RevisionCount", 0); x.close()
    x.close()
    # Projection
    x.tag("chunk", {"name": "Projection"})
    x.items_block(2)
    x.tag("item", {"name": "Target", "type_name": "gh_drawing_point", "type_code": "30"})
    x.raw("<X>0</X>"); x.raw("<Y>0</Y>"); x.close()
    x.item("Zoom", "1.0", "gh_single", "5")
    x.close()
    x.close()
    # Views
    x.tag("chunk", {"name": "Views"})
    x.items_block(1); x.item_int("ViewCount", 0); x.close()
    x.close()
    x.close()  # /chunks
    x.close()  # /DefinitionProperties
    
    # RcpLayout
    x.tag("chunk", {"name": "RcpLayout"})
    x.items_block(1); x.item_int("GroupCount", 0); x.close()
    x.close()
    
    # ValueTable
    x.tag("chunk", {"name": "ValueTable"})
    x.items_block(1)
    x.item("raven.ids", "", "gh_string", "10")
    x.close()
    x.close()
    
    # GHALibraries - copy from v06
    copy_gha_libraries(x)
    
    # DefinitionObjects
    objects_node = doc_obj.find('Objects')
    obj_list = objects_node.findall('Object') if objects_node is not None else []
    
    x.tag("chunk", {"name": "DefinitionObjects"})
    x.items_block(1)
    x.item_int("ObjectCount", len(obj_list))
    x.close()
    
    x.chunks_block(len(obj_list))
    for idx, obj in enumerate(obj_list):
        write_object(x, obj, idx)
    x.close()
    x.close()  # /DefinitionObjects
    
    import traceback
    print(f'Lines before final closes: {len(x.lines)}')
    print(f'Stack: {x.stack}')
    print(f'Last 5 before close: {x.lines[-5:]}')
    try:
        x.close()  # /chunks of Definition
        x.close()  # /Definition
        x.close()  # /chunks of Archive
        x.close()  # /Archive
    except Exception as e:
        print(f'ERROR during final closes: {e}')
        traceback.print_exc()
        return False
    print(f'Lines after final closes: {len(x.lines)}')
    print(f'Last 8 lines: {x.lines[-8:]}')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(x))
    print(f"Written: {output_path}")
    return True

def copy_gha_libraries(x):
    """Copy GHALibraries from v06 if available."""
    v06_path = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx"
    try:
        t6 = ET.parse(v06_path)
        for chunk in t6.getroot().iter('chunk'):
            if chunk.get('name') == 'GHALibraries':
                xml = ET.tostring(chunk, encoding='unicode')
                for line in xml.split('\n'):
                    s = line.strip()
                    if s:
                        x.raw(s)
                return
    except:
        pass
    # Fallback: minimal libraries
    x.tag("chunk", {"name": "GHALibraries"})
    x.items_block(1); x.item_int("Count", 1); x.close()
    x.chunks_block(1)
    x.tag("chunk", {"name": "Library", "index": "0"})
    x.items_block(4)
    x.item("Author", "Robert McNeel &amp; Associates", "gh_string", "10")
    x.item_guid("Id", "00000000-0000-0000-0000-000000000000")
    x.item("Name", "Grasshopper", "gh_string", "10")
    x.item("Version", "8.33.26188.13001", "gh_string", "10")
    x.close()
    x.close()
    x.close()
    x.close()

def write_object(x, obj, index):
    obj_type = obj.get('type', '')
    obj_name = obj.findtext('Name') or obj.get('name', '')
    obj_nick = obj.findtext('Nickname') or obj_name
    obj_desc = obj.findtext('Description') or ''
    guid = get_component_guid(obj_type, obj_name)
    
    x.tag("chunk", {"name": "Object", "index": str(index)})
    x.items_block(2)
    x.item_guid("GUID", guid)
    # Use the component TYPE name, not the user's group name
    if is_python(obj):
        disp_name = "Python 3 Script"
    elif is_group(obj):
        disp_name = "Group"
    elif is_panel(obj):
        disp_name = "Panel" if 'Panel' in obj_type else "Palette"
    elif is_slider(obj):
        disp_name = "Number Slider"
    else:
        disp_name = obj_name
    x.item("Name", disp_name, "gh_string", "10")
    x.close()
    
    x.chunks_block(1)
    x.tag("chunk", {"name": "Container"})
    
    if is_group(obj):
        write_group_container(x, obj, obj_name)
    elif is_panel(obj):
        write_panel_container(x, obj, obj_name, obj_nick, obj_desc)
    elif is_slider(obj):
        write_slider_container(x, obj, obj_name, obj_nick, obj_desc)
    elif is_python(obj):
        write_python_container(x, obj, obj_name, obj_nick, obj_desc)
    else:
        write_native_container(x, obj, obj_name, obj_nick, obj_desc)
    
    x.close()  # /Container
    x.close()  # /chunks
    x.close()  # /Object

if __name__ == '__main__':
    input_path = sys.argv[1] if len(sys.argv) > 1 else r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx.bak"
    output_path = sys.argv[2] if len(sys.argv) > 2 else input_path.replace('.ghx.bak', '.ghx')
    
    success = convert(input_path, output_path)
    if success:
        print("\n--- Validating with GhDefinitionExplorer ---")
        import subprocess
        exe = r"D:\Work\LIBRARIES\GhDefinitionExplorer\bin\Release\net8.0\GhDefinitionExplorer.exe"
        result = subprocess.run([exe, output_path, output_path.replace('.ghx', '.json')],
                               capture_output=True, text=True)
        print(result.stdout)
        if result.stderr: print("STDERR:", result.stderr)
