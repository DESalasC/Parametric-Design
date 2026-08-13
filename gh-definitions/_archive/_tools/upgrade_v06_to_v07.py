"""Find LADOS_CONFIGURAR Python component in v06 and replace its code with v07."""
from lxml import etree
import base64, copy, os

v06_path = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx"
v07_code_path = r"D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_LADOS_CONFIGURAR_v07.py"
output_path = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v07.ghx"
backup_path = r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06_backup.ghx"

# Backup v06
import shutil
shutil.copy2(v06_path, backup_path)
print(f"Backup: {backup_path}")

# Read v07 code
with open(v07_code_path, 'r', encoding='utf-8') as f:
    v07_code = f.read()

# Parse v06
tree = etree.parse(v06_path)
root = tree.getroot()

# Find all Python Script components
found = False
for obj in root.findall('.//chunk[@name="Object"]'):
    # Check if it's a Python component
    guid_it = obj.find('items/item[@name="GUID"]')
    if guid_it is None or guid_it.text != '719467e6-7cf5-4848-99b0-c5dd57e5442c':
        continue
    
    # Check NickName to find LADOS_CONFIGURAR
    container = obj.find('.//chunk[@name="Container"]')
    if container is None:
        continue
    
    nick = ''
    for it in container.iter('item'):
        if it.get('name') == 'NickName':
            nick = it.text or ''
            break
    
    if 'LADOS' not in nick and 'lados' not in nick.lower():
        continue
    
    print(f"Found: NickName='{nick}'")
    
    # Find Script chunk and update code
    script_chunk = container.find('.//chunk[@name="Script"]')
    if script_chunk is None:
        print("  No Script chunk found!")
        continue
    
    # Update the base64-encoded code
    for it in script_chunk.iter('item'):
        if it.get('name') == 'Text':
            old_len = len(it.text or '')
            new_b64 = base64.b64encode(v07_code.encode('utf-8')).decode('ascii')
            it.text = new_b64
            print(f"  Code updated: {old_len} -> {len(new_b64)} bytes (base64)")
            found = True
        elif it.get('name') == 'Title':
            old_title = it.text
            it.text = 'F1_LADOS_CONFIGURAR_v07'
            print(f"  Title updated: '{old_title}' -> 'F1_LADOS_CONFIGURAR_v07'")

if not found:
    print("\nERROR: Could not find LADOS_CONFIGURAR Python component!")
    print("Searching all Python components...")
    for obj in root.findall('.//chunk[@name="Object"]'):
        gi = obj.find('items/item[@name="GUID"]')
        if gi is None or gi.text != '719467e6-7cf5-4848-99b0-c5dd57e5442c':
            continue
        container = obj.find('.//chunk[@name="Container"]')
        if container is None:
            continue
        nick = ''
        for it in container.iter('item'):
            if it.get('name') == 'NickName':
                nick = it.text or ''
                break
        print(f"  Python component: NickName='{nick}'")
else:
    # Write output
    xml_bytes = etree.tostring(root, encoding='utf-8', pretty_print=True, xml_declaration=True)
    with open(output_path, 'wb') as f:
        f.write(xml_bytes)
    
    print(f"\nOutput: {output_path} ({len(xml_bytes)} bytes)")
    
    # Validate
    import subprocess
    exe = r"D:\Work\LIBRARIES\GhDefinitionExplorer\bin\Release\net8.0\GhDefinitionExplorer.exe"
    result = subprocess.run([exe, output_path, output_path.replace('.ghx', '.json')],
                           capture_output=True, text=True)
    if "Error" in (result.stdout + result.stderr):
        print("VALIDATION FAILED")
        for line in (result.stdout + result.stderr).split('\n'):
            if 'Error' in line.lower():
                print(f"  {line.strip()}")
    else:
        print("VALIDATION OK - Ready for Grasshopper")
