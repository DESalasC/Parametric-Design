"""Update CONTEXTO_POT_v04 in v07 GHX with the displacement fix."""
from lxml import etree
import base64, shutil, subprocess

ghx_path = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx"
script_path = r"D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_CONTEXTO_POT_v04.py"

# Read new code
with open(script_path, 'r', encoding='utf-8') as f:
    new_code = f.read()

tree = etree.parse(ghx_path)
root = tree.getroot()

found = False
for obj in root.findall('.//chunk[@name="Object"]'):
    gi = obj.find('items/item[@name="GUID"]')
    if gi is None or gi.text != '719467e6-7cf5-4848-99b0-c5dd57e5442c':
        continue
    container = obj.find('.//chunk[@name="Container"]')
    if container is None: continue
    nick = ''
    for it in container.iter('item'):
        if it.get('name') == 'NickName':
            nick = it.text or ''
            break
    if 'CONTEXTO' not in nick.upper() and 'CONTEXT' not in nick.upper():
        continue
    
    print(f"Found: NickName='{nick}'")
    script = container.find('.//chunk[@name="Script"]')
    if script is None: continue
    
    for it in script.iter('item'):
        if it.get('name') == 'Text':
            old_len = len(it.text or '')
            it.text = base64.b64encode(new_code.encode('utf-8')).decode('ascii')
            print(f"  Code: {old_len} -> {len(it.text)} bytes (base64)")
            found = True

if found:
    xml_bytes = etree.tostring(root, encoding='utf-8', pretty_print=True, xml_declaration=True)
    with open(ghx_path, 'wb') as f:
        f.write(xml_bytes)
    print(f"\nUpdated: {ghx_path} ({len(xml_bytes)} bytes)")
    
    exe = r"D:\Work\LIBRARIES\GhDefinitionExplorer\bin\Release\net8.0\GhDefinitionExplorer.exe"
    result = subprocess.run([exe, ghx_path, ghx_path.replace('.ghx', '.json')],
                           capture_output=True, text=True)
    if "Error" in (result.stdout + result.stderr):
        print("VALIDATION FAILED")
        for line in (result.stdout + result.stderr).split('\n'):
            if 'Error' in line.lower(): print(f"  {line.strip()}")
    else:
        print("VALIDATION OK")
else:
    print("NOT FOUND - searching all Python components:")
    for obj in root.findall('.//chunk[@name="Object"]'):
        gi = obj.find('items/item[@name="GUID"]')
        if gi is None or gi.text != '719467e6-7cf5-4848-99b0-c5dd57e5442c': continue
        c = obj.find('.//chunk[@name="Container"]')
        if c is None: continue
        nick = ''
        for it in c.iter('item'):
            if it.get('name') == 'NickName': nick = it.text or ''; break
        print(f"  '{nick}'")
