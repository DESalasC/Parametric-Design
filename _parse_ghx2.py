import re
import sys

path = r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.7.ghx'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

out = []

def get_item(chunk, name):
    m = re.search(r'<item name="' + re.escape(name) + r'"[^>]*>(.*?)</item>', chunk, flags=re.DOTALL)
    return m.group(1).strip() if m else None

# Find all Object chunks
object_chunks = re.findall(r'<chunk name="Object"[^>]*>.*?</chunk>', content, flags=re.DOTALL)
out.append("Object chunks found: {}".format(len(object_chunks)))

components = []
for oc in object_chunks:
    instance_guid = get_item(oc, 'InstanceGuid')
    nickname = get_item(oc, 'NickName')
    name = get_item(oc, 'Name')
    code_input = get_item(oc, 'CodeInput')
    components.append({
        'instance_guid': instance_guid,
        'nickname': nickname,
        'name': name,
        'code_input': code_input,
        'chunk': oc,
    })

out.append("\n=== ALL COMPONENTS (instance_guid, nickname, name) ===")
for c in components:
    out.append("{}|{}|{}".format(c['instance_guid'], c['nickname'], c['name']))

# Identify ArchiCAD / Live Connection components (name contains AC_ or archicad or LiveConnection)
out.append("\n=== ARCHICAD / LIVE CONNECTION COMPONENTS ===")
archicad_comps = [c for c in components if c['name'] and ('AC_' in c['name'] or 'archicad' in c['name'].lower() or 'LiveConnection' in c['name'])]
for c in archicad_comps:
    out.append("GUID: {}".format(c['instance_guid']))
    out.append("  Name: {}".format(c['name']))
    out.append("  NickName: {}".format(c['nickname']))

# GHPython components
out.append("\n=== GHPYTHON COMPONENTS ===")
ghpython_comps = [c for c in components if c['name'] == 'GhPython Script']
for c in ghpython_comps:
    out.append("GUID: {} | NickName: {}".format(c['instance_guid'], c['nickname']))

# Write output to file
out_path = r'D:\Work\PROJECTS\DiseñoParametrico\_ghx_report.txt'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Done. Wrote to", out_path)
print("Archicad comps:", len(archicad_comps))
print("GhPython comps:", len(ghpython_comps))
