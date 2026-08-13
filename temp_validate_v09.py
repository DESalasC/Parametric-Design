"""Quick validation of F1_Contexto_v09.gh"""
import xml.etree.ElementTree as ET
import base64, zlib, re

tree = ET.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v09.gh")
root = tree.getroot()

objects = []
def find_objects(elem):
    if elem.tag == 'chunk' and elem.get('name') == 'Object':
        objects.append(elem)
    for child in elem:
        find_objects(child)

find_objects(root)
print(f"Total Objects: {len(objects)}")
print()

for idx, obj in enumerate(objects):
    nick = ""
    in_cnt = "?"
    out_cnt = "?"
    for item in obj.iter('item'):
        n = item.get('name', '')
        if n == 'NickName': nick = item.text or ''
        elif n == 'InputCount': in_cnt = item.text or '?'
        elif n == 'OutputCount': out_cnt = item.text or '?'
    
    # Find script code
    script_code = None
    for chunk in obj.iter('chunk'):
        if chunk.get('name') == 'Script':
            for item in chunk.iter('item'):
                if item.get('name') == 'Code' and item.text:
                    try:
                        decoded = base64.b64decode(item.text)
                        script_code = zlib.decompress(decoded).decode('utf-8', errors='replace')
                    except:
                        pass
    
    if script_code:
        ver = re.search(r'F1_\w+_v\d+', script_code)
        ver_name = ver.group(0) if ver else '(no version)'
        print(f"Obj {idx}: {ver_name}")
        print(f"  NickName: {nick}")
        print(f"  InputCount: {in_cnt} OutputCount: {out_cnt}")
        
        # Check for IronPython 2.7 issues
        issues = []
        if re.search(r'open\([^)]*encoding=', script_code) and 'io.open' not in script_code:
            issues.append("open() with encoding (use io.open)")
        if re.search(r'f"[^"]*\{', script_code) or re.search(r"f'[^']*\{", script_code):
            issues.append("f-strings (use .format)")
        
        if issues:
            for issue in issues:
                print(f"  ISSUE: {issue}")
        else:
            print(f"  IronPython 2.7: OK")
        
        # Show inputs/outputs
        ins = re.findall(r'<chunk name="InputParam">.*?<item name="Name" type_name="string">([^<]+).*?</chunk>', str(obj), re.DOTALL)
        outs = re.findall(r'<chunk name="OutputParam">.*?<item name="Name" type_name="string">([^<]+).*?</chunk>', str(obj), re.DOTALL)
        if ins: print(f"  Inputs: {ins}")
        if outs: print(f"  Outputs: {outs}")
        print()
