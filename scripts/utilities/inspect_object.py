#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import os

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")

tree = ET.parse(GHX_PATH)
root = tree.getroot()

# Find DefinitionObjects
definition_objects = None
for chunk in root.iter('chunk'):
    if chunk.get('name') == 'DefinitionObjects':
        definition_objects = chunk
        break

if definition_objects is not None:
    print("Found DefinitionObjects chunk")
    
    # Inspect a few objects to understand the structure
    for obj_index in ["2", "191", "194"]:
        print(f"\n{'='*60}")
        print(f"Inspecting Object[index={obj_index}]")
        print('='*60)
        
        target_obj = None
        for obj in definition_objects.iter('chunk'):
            if obj.get('name') == 'Object' and obj.get('index') == obj_index:
                target_obj = obj
                break
        
        if target_obj is None:
            print(f"Object[index={obj_index}] not found")
            continue
            
        print(f"Object attrib: {target_obj.attrib}")
        
        # List all item elements
        items = list(target_obj.iter('item'))
        print(f"Number of item elements: {len(items)}")
        
        # Show first 20 items
        for i, item in enumerate(items[:20]):
            name = item.get('name')
            text = item.text or ''
            if text and len(text) > 100:
                text_display = text[:100] + "..."
            else:
                text_display = text
            print(f"  Item {i:2d}: name='{name}', text='{text_display}'")
        
        if len(items) > 20:
            print(f"  ... and {len(items) - 20} more items")
            
        # Look for ScriptFile or similar
        print(f"\nLooking for script-related chunks:")
        script_related = []
        for chunk in target_obj.iter('chunk'):
            chunk_name = chunk.get('name')
            if 'script' in chunk_name.lower() or 'code' in chunk_name.lower() or 'file' in chunk_name.lower():
                script_related.append((chunk_name, chunk.attrib))
                # Look inside for script content
                for sub in chunk.iter('chunk'):
                    sub_name = sub.get('name')
                    sub_text = sub.text or '' if len(sub) > 0 and sub[0].text is not None else ''
                    if sub_name and ('script' in sub_name.lower() or 'code' in sub_name.lower()):
                        if sub_text and len(sub_text) > 100:
                            sub_text_display = sub_text[:100] + "..."
                        else:
                            sub_text_display = sub_text
                        print(f"    Sub-element: name='{sub_name}', text='{sub_text_display}'")
        
        if script_related:
            print(f"Found {len(script_related)} script-related chunks:")
            for name, attrib in script_related:
                print(f"  Chunk: name='{name}', attrib={attrib}")
        else:
            print("No script-related chunks found")
            
        # Let's see what chunks we DO have
        chunk_names = [chunk.get('name') for chunk in target_obj.iter('chunk')]
        unique_chunk_names = list(set(chunk_names))
        print(f"\nAll chunk types in this object: {unique_chunk_names}")
        
        # Let's look for any element that might contain substantial text
        print(f"\nLooking for elements with substantial text content:")
        text_elements = []
        for elem in target_obj.iter():
            if elem.text and len(elem.text.strip()) > 50:  # At least 50 chars of text
                tag = elem.tag
                text_preview = elem.text.strip()[:100]
                text_elements.append((tag, text_preview, len(elem.text.strip())))
        
        if text_elements:
            print(f"Found {len(text_elements)} elements with substantial text:")
            for tag, preview, length in text_elements[:10]:  # Show first 10
                print(f"  <{tag}>: {length} chars - '{preview}...'")
        else:
            print("No elements with substantial text content found")
else:
    print("ERROR: No DefinitionObjects chunk found")