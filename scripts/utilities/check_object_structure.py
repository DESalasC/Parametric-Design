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
        print("\nExamining the structure of Object chunks:")
        print("=" * 60)
        
        # Look at the first few objects to understand the structure
        for i, obj in enumerate(actual_objects[:3]):
            print(f"Object {i}:")
            print(f"  Object attrib: {obj.attrib}")
            
            # Look for item elements inside this object
            items = list(obj.iter('item'))
            print(f"  Found {len(items)} item elements")
            
            # Print first few items
            for j, item in enumerate(items[:10]):
                name = item.get('name')
                text = item.text or ''
                print(f"    Item {j}: name='{name}', text='{text[:50]}{'...' if len(text) > 50 else ''}'")
            
            if len(items) > 10:
                print(f"    ... and {len(items) - 10} more items")
            print()
            
        # Now let's search for our specific GUIDs by looking through item elements
        TARGET_GUIDS = [
            "6eaf2956-f649-4540-a900-4b32a10deee4",
            "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d", 
            "d3bed17b-1b6b-4e89-8761-1985327b292b"
        ]
        
        print("\nSearching for target GUIDs in item elements:")
        print("=" * 60)
        
        for target_guid in TARGET_GUIDS:
            print(f"\nSearching for: {target_guid}")
            found_in_object = None
            found_as_what = None
            
            for obj in actual_objects:
                obj_index = obj.get('index', 'unknown')
                # Look for item with name="InstanceGuid" and matching value
                for item in obj.iter('item'):
                    if item.get('name') == 'InstanceGuid' and item.text:
                        guid_value = item.text.strip()
                        if guid_value.lower() == target_guid.lower():
                            found_in_object = obj
                            found_as_what = "InstanceGuid"
                            break
                    # Also check for item with name="ID" (sometimes it's stored there)
                    elif item.get('name') == 'ID' and item.text:
                        guid_value = item.text.strip()
                        if guid_value.lower() == target_guid.lower():
                            found_in_object = obj
                            found_as_what = "ID"
                            break
                
                if found_in_object:
                    break
            
            if found_in_object:
                obj_index = found_in_object.get('index', 'unknown')
                obj_name = found_in_object.get('name', 'unknown')
                print(f"  FOUND in Object[index={obj_index}, name='{obj_name}'] as {found_as_what}")
                
                # Now look for nickName in this object
                nick_name = None
                for item in found_in_object.iter('item'):
                    if item.get('name') == 'NickName':
                        nick_name = item.text or ''
                        break
                
                if nick_name is not None:
                    print(f"  NickName: '{nick_name}'")
                else:
                    print(f"  NickName: NOT FOUND")
                
                # Look for ScriptFile to see what's currently embedded
                for chunk in found_in_object.iter('chunk'):
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
                print()
            else:
                print(f"  NOT FOUND")
                print()