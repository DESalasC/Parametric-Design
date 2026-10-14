#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import os

# Parse the GHX file
tree = ET.parse('gh-definitions/F1_CONTEXTO_v13.5.ghx')
root = tree.getroot()

# Find the DefinitionObjects chunk
definition_objects = None
for chunk in root.iter('chunk'):
    if chunk.get('name') == 'DefinitionObjects':
        definition_objects = chunk
        break

if definition_objects is not None:
    # Look for the specific object we want to check: index=191 which should be our F3_DISTRIBUCION_v03.py
    target_index = "191"
    target_obj = None
    
    for obj in definition_objects.iter('chunk'):
        if obj.get('name') == 'Object' and obj.get('index') == target_index:
            target_obj = obj
            break
    
    if target_obj is not None:
        print(f"Found Object with index={target_index}")
        print(f"Full attrib: {target_obj.attrib}")
        
        # Get the actual GUID from the item
        actual_guid = None
        nick_name = None
        for item in target_obj.iter('item'):
            if item.get('name') == 'GUID' and item.text:
                actual_guid = item.text.strip()
                print(f"Found GUID item: '{actual_guid}'")
            elif item.get('name') == 'NickName' and item.text:
                nick_name = item.text.strip()
                print(f"Found NickName item: '{nick_name}'")
        
        if actual_guid:
            print(f"Actual GUID: {actual_guid}")
            print(f"Does it start with '6eaf2956'? {actual_guid.lower().startswith('6eaf2956')}")
        
        # Now let's see what's in the ScriptFile
        print("\nLooking for ScriptFile...")
        for chunk in target_obj.iter('chunk'):
            if chunk.get('name') == 'ScriptFile':
                print("Found ScriptFile chunk")
                for sub in chunk.iter('chunk'):
                    if sub.get('name') == 'script':
                        print("Found script element")
                        if len(sub) > 0 and sub[0].text:
                            script_text = sub[0].text
                            print(f"Script text length: {len(script_text)} characters")
                            print(f"First 100 chars: {repr(script_text[:100])}")
                            print(f"Last 100 chars: {repr(script_text[-100:] if len(script_text) > 100 else script_text)}")
                            
                            # Compare with source file
                            source_path = os.path.join(os.path.dirname(__file__), '..', '..', 'src/fase-3-masa/F3_DISTRIBUCION_v03.py')
                            source_path = os.path.normpath(source_path)
                            print(f"\nChecking source file: {source_path}")
                            try:
                                with open(source_path, 'r', encoding='utf-8') as f:
                                    source_content = f.read()
                                print(f"Source file length: {len(source_content)} characters")
                                print(f"Source first 100 chars: {repr(source_content[:100])}")
                                print(f"Source last 100 chars: {repr(source_content[-100:] if len(source_content) > 100 else source_content)}")
                                
                                if script_text == source_content:
                                    print("\n✓ MATCH: Script content equals source file content")
                                else:
                                    print("\n✗ MISMATCH: Script content differs from source file")
                                    if len(script_text) != len(source_content):
                                        print(f"  Length difference: script={len(script_text)}, source={len(source_content)}")
                                    # Find first difference
                                    for i, (c1, c2) in enumerate(zip(script_text, source_content)):
                                        if c1 != c2:
                                            print(f"  First difference at position {i}:")
                                            print(f"    Script: {repr(c1)}")
                                            print(f"    Source: {repr(c2)}")
                                            # Show some context
                                            start = max(0, i-20)
                                            end = min(len(script_text), i+20)
                                            print(f"    Script context: {repr(script_text[start:end])}")
                                            print(f"    Source context: {repr(source_content[start:end])}")
                                            break
                                    else:
                                        if len(script_text) < len(source_content):
                                            print(f"  Script is shorter than source")
                                            print(f"  Missing end: {repr(source_content[len(script_text):])}")
                                        else:
                                            print(f"  Source is shorter than script")
                                            print(f"  Extra in script: {repr(script_text[len(source_content):])}")
                            except Exception as e:
                                print(f"Error reading source file: {e}")
                        else:
                            print("Script element found but no text content")
                        break
                break
        else:
            print("No ScriptFile chunk found in object")
    else:
        print(f"No Object found with index={target_index}")
        # Let's see what indexes we DO have
        indexes = []
        for obj in definition_objects.iter('chunk'):
            if obj.get('name') == 'Object':
                idx = obj.get('index')
                if idx:
                    indexes.append(int(idx))
        if indexes:
            print(f"Available indexes: {sorted(indexes)[:20]}..." if len(indexes) > 20 else f"Available indexes: {sorted(indexes)}")
else:
    print("ERROR: No DefinitionObjects chunk found")