#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# Parse the GHX file
tree = ET.parse('gh-definitions/F1_CONTEXTO_v13.5.ghx')
root = tree.getroot()

print("All objects in GHX file:")
print("=" * 80)

objects = []
for obj in root.iter('object'):
    guid = obj.get('instanceGuid')
    nick = obj.get('nickName', '')
    name = obj.get('name', '')
    if guid:
        objects.append((guid, nick, name))

print(f"Found {len(objects)} objects\n")

# Sort by nickname for easier viewing
objects.sort(key=lambda x: x[1])

for guid, nick, name in objects:
    print(f"GUID: {guid}")
    print(f"  NickName: '{nick}'")
    print(f"  Name: '{name}'")
    print()

# Now let's look for objects that might be our targets by nickname
print("\n" + "=" * 80)
print("Looking for objects with keywords in nickname:")
print("=" * 80)

keywords = ['DISTRIBUCION', 'VOLUM', 'PATIO', 'F3_', 'F1_ETAPA2']
for guid, nick, name in objects:
    for keyword in keywords:
        if keyword.upper() in nick.upper():
            print(f"Found match for '{keyword}':")
            print(f"  GUID: {guid}")
            print(f"  NickName: '{nick}'")
            print(f"  Name: '{name}'")
            print()
            break