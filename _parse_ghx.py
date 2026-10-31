import re
import xml.etree.ElementTree as ET

path = r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.7.ghx'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

print("TOTAL CHARS:", len(content))

# Find all Object chunks - they start with <chunk name="Object" ...> and end with </chunk>
# Use regex to capture each Object chunk (non-greedy but Object chunks can nest Container)
object_chunks = re.findall(r'<chunk name="Object"[^>]*>.*?</chunk>', content, flags=re.DOTALL)
print("Object chunks found:", len(object_chunks))

components = []
for oc in object_chunks:
    # Parse items within this object chunk
    def get_item(name):
        m = re.search(r'<item name="' + re.escape(name) + r'"[^>]*>(.*?)</item>', oc, flags=re.DOTALL)
        return m.group(1).strip() if m else None

    instance_guid = get_item('InstanceGuid')
    nickname = get_item('NickName')
    name = get_item('Name')
    code_input = get_item('CodeInput')

    components.append({
        'instance_guid': instance_guid,
        'nickname': nickname,
        'name': name,
        'code_input': code_input,
    })

print("\n=== ALL COMPONENTS (instance_guid, nickname, name) ===")
for c in components:
    print("{}|{}|{}".format(c['instance_guid'], c['nickname'], c['name']))

print("\n=== GHPython components with CodeInput ===")
for c in components:
    if c['code_input']:
        print("GUID:", c['instance_guid'])
        print("NickName:", c['nickname'])
        print("--- code (first 400 chars) ---")
        print(c['code_input'][:400])
        print("...")
