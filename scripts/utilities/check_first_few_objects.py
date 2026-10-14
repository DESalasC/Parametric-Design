#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# Parse the GHX file
tree = ET.parse('gh-definitions/F1_CONTEXTO_v13.5.ghx')
root = tree.getroot()

# Find the DefinitionObjects chunk
definition_objects = None
for chunk in root.iter('chunk'):
    if chunk.get('name') == 'DefinitionObjects':
        definition_objects = chunk
        break

if definition_objects is None:
    print("ERROR: No DefinitionObjects chunk found")
else:
    print("Found DefinitionObjects chunk")
    
    # Look for Object chunks inside DefinitionObjects
    actual_objects = [chunk for chunk in definition_objects.iter('chunk') if chunk.get('name') == 'Object']
    print(f"Found {len(actual_objects)} Object chunks")
    
    if len(actual_objects) > 0:
        print("\nChecking first 10 objects for GUIDs and nicknames:")
        print("=" * 60)
        
        for i, obj in enumerate(actual_objects[:10]):
            guid = obj.get('instanceGuid', '')
            nick = obj.get('nickName', '')
            name = obj.get('name', '')
            print(f"Object {i}:")
            print(f"  GUID: '{guid}'")
            print(f"  NickName: '{nick}'")
            print(f"  Name: '{name}'")
            
            # Check if this might be one of our targets (by looking for partial matches in nickname)
            if nick:
                nick_lower = nick.lower()
                if 'distribucion' in nick_lower or 'v03' in nick_lower:
                    print(f"  -> Possible DISTRIBUCION match!")
                if 'volum' in nick_lower or 'v08' in nick_lower:
                    print(f"  -> Possible VOLUM match!")
                if 'patio' in nick_lower:
                    print(f"  -> Possible PATIO match!")
            print()
        
        # Now let's search for our specific GUIDs in all objects
        TARGET_GUIDS = [
            "6eaf2956-f649-4540-a900-4b32a10deee4",
            "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d", 
            "d3bed17b-1b6b-4e89-8761-1985327b292b"
        ]
        
        print("\nSearching for target GUIDs in all objects:")
        print("=" * 60)
        
        for target_guid in TARGET_GUIDS:
            found = False
            for obj in actual_objects:
                guid = obj.get('instanceGuid', '')
                if guid and guid.lower() == target_guid.lower():
                    found = True
                    nick = obj.get('nickName', '')
                    print(f"FOUND: {target_guid}")
                    print(f"  NickName: '{nick}'")
                    
                    # Check script content
                    for chunk in obj.iter('chunk'):
                        if chunk.get('name') == 'ScriptFile':
                            for sub in chunk.iter('chunk'):
                                if sub.get('name') == 'script' and len(sub) > 0 and sub[0].text:
                                    script_text = sub[0].text
                                    print(f"  Script length: {len(script_text)} chars")
                                    # Show first line
                                    first_line = script_text.split('\n')[0] if script_text else ""
                                    print(f"  First line: {first_line}")
                                    break
                            break
                    break
            
            if not found:
                print(f"NOT FOUND: {target_guid}")
            print()