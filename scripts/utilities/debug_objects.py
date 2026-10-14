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
        print("\nExamining first 5 objects in detail:")
        print("=" * 60)
        
        for i, obj in enumerate(actual_objects[:5]):
            guid = obj.get('instanceGuid', '')
            nick = obj.get('nickName', '')
            name = obj.get('name', '')
            print(f"Object {i}:")
            print(f"  Full attrib dict: {obj.attrib}")
            print(f"  instanceGuid: '{guid}' (length: {len(guid)})")
            print(f"  nickName: '{nick}' (length: {len(nick)})")
            print(f"  name: '{name}' (length: {len(name)})")
            
            # Check if it has any child chunks
            child_chunks = list(obj.iter('chunk'))
            print(f"  Number of child chunks: {len(child_chunks)}")
            for j, child in enumerate(child_chunks[:3]):  # First 3 child chunks
                print(f"    Child {j}: name='{child.get('name')}', attrib={child.attrib}")
            if len(child_chunks) > 3:
                print(f"    ... and {len(child_chunks) - 3} more child chunks")
            print()
            
        # Let's also check what attributes these objects actually have
        print("\nChecking what attributes the first object actually has:")
        print("=" * 60)
        if len(actual_objects) > 0:
            obj = actual_objects[0]
            print(f"Object 0 attributes: {obj.attrib}")
            print(f"All attribute keys: {list(obj.attrib.keys())}")
            
            # Check if instanceGuid exists but is empty
            if 'instanceGuid' in obj.attrib:
                print(f"instanceGuid value: '{obj.attrib['instanceGuid']}'")
                print(f"instanceGuid length: {len(obj.attrib['instanceGuid'])}")
                print(f"instanceGuid repr: {repr(obj.attrib['instanceGuid'])}")
            else:
                print("instanceGuid attribute NOT FOUND")
                
            # Check for nickName
            if 'nickName' in obj.attrib:
                print(f"nickName value: '{obj.attrib['nickName']}'")
            else:
                print("nickName attribute NOT FOUND")