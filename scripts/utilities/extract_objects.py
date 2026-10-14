#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import os

# Parse the GHX file
tree = ET.parse('gh-definitions/F1_CONTEXTO_v13.5.ghx')
root = tree.getroot()

# Target GUIDs and their expected source files
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

print("Checking current embedded scripts vs source files...")
print("=" * 60)

for guid, info in TARGETS.items():
    print(f"\nChecking: {info['name']}")
    print(f"Expected source: {info['source']}")
    
    # Find the object with this GUID
    found = False
    for obj in root.iter('object'):
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
                source_path = os.path.join(os.path.dirname(__file__), '..', '..', info['source'])
                source_path = os.path.normpath(source_path)
                
                try:
                    with open(source_path, 'r', encoding='utf-8') as f:
                        source_content = f.read()
                    
                    # Compare
                    if current_script == source_content:
                        print("✓ GHX content matches source file")
                    else:
                        print("✗ GHX content DOES NOT match source file")
                        print(f"  GHX length: {len(current_script)} chars")
                        print(f"  Source length: {len(source_content)} chars")
                        
                        # Show first difference
                        for i, (c1, c2) in enumerate(zip(current_script, source_content)):
                            if c1 != c2:
                                print(f"  First difference at position {i}:")
                                print(f"    GHX: {repr(c1)}")
                                print(f"    Src: {repr(c2)}")
                                # Show context
                                start = max(0, i-10)
                                end = min(len(current_script), i+10)
                                print(f"    GHX context: {repr(current_script[start:end])}")
                                print(f"    Src context: {repr(source_content[start:end])}")
                                break
                        else:
                            if len(current_script) != len(source_content):
                                print(f"  Lengths differ: GHX={len(current_script)}, Source={len(source_content)}")
                                if len(current_script) < len(source_content):
                                    print(f"  GHX is shorter, missing end: {repr(source_content[len(current_script):])}")
                                else:
                                    print(f"  Source is shorter, GHX has extra: {repr(source_content[len(source_content):])}")
                except FileNotFoundError:
                    print(f"✗ Source file not found: {source_path}")
                except Exception as e:
                    print(f"✗ Error reading source: {e}")
            else:
                print("✗ No script content found in GHX object")
            break
    
    if not found:
        print(f"✗ Object with GUID {guid} not found in GHX")

print("\n" + "=" * 60)