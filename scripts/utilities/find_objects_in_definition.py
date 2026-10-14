#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# Parse the GHX file
tree = ET.parse('gh-definitions/F1_CONTEXTO_v13.5.ghx')
root = tree.getroot()

print("Searching for objects in DefinitionObjects...")
print("=" * 60)

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
    object_chunks = list(definition_objects.iter('chunk'))
    print(f"Found {len(object_chunks)} chunks in DefinitionObjects")
    
    # Filter for actual Object chunks
    actual_objects = [chunk for chunk in object_chunks if chunk.get('name') == 'Object']
    print(f"Found {len(actual_objects)} Object chunks")
    
    if len(actual_objects) > 0:
        print("\nFirst few objects:")
        for i, obj in enumerate(actual_objects[:10]):
            guid = obj.get('instanceGuid', '')
            nick = obj.get('nickName', '')
            name = obj.get('name', '')
            print(f"  {i}: GUID={guid}")
            print(f"      NickName='{nick}'")
            print(f"      Name='{name}'")
            print()
            
        # Now check for our specific targets
        TARGETS = {
            "6eaf2956-f649-4540-a900-4b32a10deee4": {
                "name": "#198-F3_DISTRIBUCION_v03.py",
                "source": "src/fase-3-masa/F3_DISTRIBUCION_v03.py",
                "description": "#200 F3_DISTRIBUCION_v03.py → v03.9 (fix marcos)"
            },
            "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d": {
                "name": "#199-F3_VOLUM_GENERADOR_v08.py", 
                "source": "src/fase-3-masa/F3_VOLUM_GENERADOR_v08.py",
                "description": "#198 F3_VOLUM_GENERADOR_v08.py → fix (d) + _safe_json_dumps"
            },
            "d3bed17b-1b6b-4e89-8761-1985327b292b": {
                "name": "#78-F1_ETAPA2_PATIO_v03.py",
                "source": "src/fase-1-contexto/F1_ETAPA2_PATIO_v03.py",
                "description": "#78 F1_ETAPA2_PATIO_v03.py → v03.4 (regla patio confirmada)"
            }
        }
        
        print("\nChecking target objects:")
        print("=" * 60)
        
        for guid, info in TARGETS.items():
            print(f"\nChecking: {info['name']}")
            print(f"Expected source: {info['source']}")
            
            # Find the object with this GUID
            found = False
            for obj in actual_objects:
                if obj.get('instanceGuid') == guid:
                    found = True
                    nick = obj.get('nickName', '')
                    print(f"Found in GHX: NickName='{nick}'")
                    
                    # Extract current embedded script
                    current_script = None
                    for chunk in obj.iter('chunk'):
                        if chunk.get('name') == 'ScriptFile':
                            for sub in chunk.iter('chunk'):
                                if sub.get('name') == 'script' and len(sub) > 0 and sub[0].text:
                                    current_script = sub[0].text
                                    break
                            break
                    
                    if current_script is not None:
                        # Read the source file
                        import os
                        source_path = os.path.join(os.path.dirname(__file__), '..', '..', info['source'])
                        source_path = os.path.normpath(source_path)
                        
                        try:
                            with open(source_path, 'r', encoding='utf-8') as f:
                                source_content = f.read()
                            
                            # Compare
                            if current_script == source_content:
                                print("OK: GHX content matches source file")
                            else:
                                print("ERROR: GHX content DOES NOT match source file")
                                print(f"  GHX length: {len(current_script)} chars")
                                print(f"  Source length: {len(source_content)} chars")
                                
                        except FileNotFoundError:
                            print(f"ERROR: Source file not found: {source_path}")
                        except Exception as e:
                            print(f"ERROR: Error reading source: {e}")
                    else:
                        print("ERROR: No script content found in GHX object")
                    break
            
            if not found:
                print(f"ERROR: Object with GUID {guid} not found in GHX")
    else:
        print("No Object chunks found in DefinitionObjects")