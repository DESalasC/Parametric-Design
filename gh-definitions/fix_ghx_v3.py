# -*- coding: utf-8 -*-
"""GHX Fixer v3: Converts simplified GHX to native GH_IO format."""
import xml.etree.ElementTree as ET
import uuid
import hashlib
import sys
import os
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

class X:
    def __init__(self):
        self.lines = []
        self.indent = 0
        self.stack = []
    
    def tag(self, name, attrs=None, text=None, close=False, self_close=False):
        prefix = "  " * self.indent
        attr_str = ""
        if attrs:
            parts = [f'{k}="{esc(str(v))}"' for k, v in attrs.items()]
            attr_str = " " + " ".join(parts)
        if self_close:
            self.lines.append(f"{prefix}<{name}{attr_str} />")
        elif close:
            self.lines.append(f"{prefix}</{name}>")
        else:
            if text is not None:
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
    def item_guid(self, name, value): self.item(name, str(value), "gh_guid", "9")
    
    def items_block(self, count): self.tag("items", {"count": str(count)})
    def chunks_block(self, count): self.tag("chunks", {"count": str(count)})
    
    def raw(self, line): self.lines.append("  " * self.indent + line)
    def __str__(self): return "\n".join(self.lines)

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
    x.stack.append("Archive")  # manual push for raw root
    x.raw('  <!--Grasshopper archive-->')
    x.raw('  <!--Fixed by GhDefinitionExplorer-->')
    x.indent = 1
    
    # ArchiveVersion item
    x.items_block(1)
    x.tag("item", {"name": "ArchiveVersion", "type_name": "gh_version", "type_code": "80"})
    x.raw("<Major>0</Major>")
    x.raw("<Minor>2</Minor>")
    x.raw("<Revision>2</Revision>")
    x.close()
    x.close()  # /items
    
    x.chunks_block(1)
    
    # === Definition ===
    x.tag("chunk", {"name": "Definition"})
    
    # plugin_version
    x.items_block(1)
    x.tag("item", {"name": "plugin_version", "type_name": "gh_version", "type_code": "80"})
    x.raw("<Major>1</Major>")
    x.raw("<Minor>0</Minor>")
    x.raw("<Revision>7</Revision>")
    x.close()
    x.close()
    
    x.chunks_block(2)
    
    # DefinitionProperties
    x.tag("chunk", {"name": "DefinitionProperties"})
    x.items_block(3)
    x.item("Date", now_ticks(), "gh_date", "8")
    x.item("Description", doc_obj.findtext('Description') or "", "gh_string", "10")
    x.item("Name", doc_obj.findtext('Name') or doc_obj.get('name', 'Unknown'), "gh_string", "10")
    x.close()
    x.close()  # /DefinitionProperties
    
    # DefinitionObjects
    objects_node = doc_obj.find('Objects')
    obj_list = objects_node.findall('Object') if objects_node is not None else []
    
    x.tag("chunk", {"name": "DefinitionObjects"})
    x.items_block(1)
    x.item_int("ObjectCount", len(obj_list))
    x.close()
    
    x.chunks_block(len(obj_list))
    
    for idx, obj in enumerate(obj_list):
        convert_object(x, obj, idx)
    
    x.close()  # /chunks of DefinitionObjects
    x.close()  # /DefinitionObjects
    
    x.close()  # /chunks of Definition
    x.close()  # /Definition
    
    x.close()  # /chunks of Archive
    x.close()  # /Archive
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(x))
    
    print(f"Written: {output_path}")
    return True

def convert_object(x, obj, index):
    obj_type = obj.get('type', '')
    obj_name_attr = obj.get('name', '')
    obj_name = obj.findtext('Name') or obj_name_attr
    obj_id = obj.findtext('ID') or ''
    obj_nick = obj.findtext('Nickname') or obj_name
    obj_desc = obj.findtext('Description') or ''
    guid = mkguid(obj_id) if obj_id else str(uuid.uuid4())
    
    x.tag("chunk", {"name": "Object", "index": str(index)})
    
    # Object items
    item_count = 3
    if obj_nick: item_count += 1
    if obj_desc: item_count += 1
    
    x.items_block(item_count)
    x.item_guid("GUID", guid)
    x.item("Lib", "00000000-0000-0000-0000-000000000000", "gh_guid", "9")
    x.item("Name", obj_name, "gh_string", "10")
    if obj_nick: x.item("NickName", obj_nick, "gh_string", "10")
    if obj_desc: x.item("Description", obj_desc, "gh_string", "10")
    x.close()
    
    # Container sub-chunk
    x.chunks_block(1)
    x.tag("chunk", {"name": "Container"})
    
    # Container items
    ci = []
    for child in obj:
        tag = child.tag
        if tag in ('Name', 'ID', 'Nickname', 'Description', 'Inputs', 'Outputs',
                   'OptionalParams', 'Code', 'Attributes', 'Wires'):
            continue
        text = (child.text or '').strip()
        if not text: continue
        ci.append((tag, text))
    
    code_node = obj.find('Code')
    if code_node is not None and code_node.text and code_node.text.strip():
        ci.append(('CodeInput', code_node.text.strip()))
    
    x.items_block(len(ci))
    for name, value in ci:
        if name in ('Min', 'Max', 'DecimalCount'):
            try:
                int(value); x.item_int(name, value)
            except:
                x.item(name, value)
        else:
            x.item(name, value, "gh_string", "10")
    x.close()  # /items
    
    # Parameters
    inputs_node = obj.find('Inputs')
    outputs_node = obj.find('Outputs')
    input_els = inputs_node.findall('Input') if inputs_node is not None else []
    output_els = outputs_node.findall('Output') if outputs_node is not None else []
    has_params = len(input_els) > 0 or len(output_els) > 0
    
    if has_params:
        x.chunks_block(1)
        x.tag("chunk", {"name": "ParameterData"})
        
        pi = 0
        if input_els: pi += 1 + len(input_els)
        if output_els: pi += 1 + len(output_els)
        
        x.items_block(pi)
        if input_els:
            x.item_int("InputCount", len(input_els))
            for i, inp in enumerate(input_els):
                x.tag("item", {"name": "InputId", "index": str(i), "type_name": "gh_guid", "type_code": "9"},
                      text=mkguid(f"{obj_name}_in_{i}"))
        if output_els:
            x.item_int("OutputCount", len(output_els))
            for j, outp in enumerate(output_els):
                x.tag("item", {"name": "OutputId", "index": str(j), "type_name": "gh_guid", "type_code": "9"},
                      text=mkguid(f"{obj_name}_out_{j}"))
        x.close()
        
        pc = len(input_els) + len(output_els)
        if pc > 0:
            x.chunks_block(pc)
            
            for i, inp in enumerate(input_els):
                x.tag("chunk", {"name": "InputParam", "index": str(i)})
                inp_name = inp.get('name', f'Input{i}')
                x.items_block(10)
                x.item_bool("AllowTreeAccess", True)
                x.item("Description", f"Script input {inp_name}.", "gh_string", "10")
                x.item_guid("InstanceGuid", mkguid(f"{obj_name}_in_{i}"))
                x.item("Name", inp_name, "gh_string", "10")
                x.item("NickName", inp_name, "gh_string", "10")
                x.item_bool("Optional", True)
                x.item_int("ScriptParamAccess", 0)
                x.item_bool("ShowTypeHints", True)
                x.item_int("SourceCount", 0)
                x.item_guid("TypeHintID", "d60527f5-b5af-4ef6-8970-5f96fe412559")
                x.close()
                x.close()
            
            for j, outp in enumerate(output_els):
                x.tag("chunk", {"name": "OutputParam", "index": str(j)})
                out_name = outp.get('name', f'Output{j}')
                out_nick = outp.get('nickname', out_name)
                x.items_block(3)
                x.item_guid("InstanceGuid", mkguid(f"{obj_name}_out_{j}"))
                x.item("Name", out_name, "gh_string", "10")
                x.item("NickName", out_nick, "gh_string", "10")
                x.close()
                x.close()
            
            x.close()  # /chunks
        else:
            x.chunks_block(0)
            x.close()
        
        x.close()  # /ParameterData
        x.close()  # /chunks of Container
    else:
        x.chunks_block(0)
        x.close()  # /chunks of Container
    
    x.close()  # /Container
    x.close()  # /chunks of Object
    x.close()  # /Object

if __name__ == '__main__':
    input_path = sys.argv[1] if len(sys.argv) > 1 else r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx"
    output_path = sys.argv[2] if len(sys.argv) > 2 else input_path.replace('.ghx', '_fixed.ghx')
    
    success = convert(input_path, output_path)
    if success:
        print("\n--- Testing with GhDefinitionExplorer ---")
        import subprocess
        exe = r"D:\Work\LIBRARIES\GhDefinitionExplorer\bin\Release\net8.0\GhDefinitionExplorer.exe"
        result = subprocess.run([exe, output_path, output_path.replace('.ghx', '.json')],
                               capture_output=True, text=True)
        print(result.stdout)
        if result.stderr: print("STDERR:", result.stderr)
