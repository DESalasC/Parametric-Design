#!/usr/bin/env python3
import xml.etree.ElementTree as ET

# Parse the GHX file
tree = ET.parse('gh-definitions/F1_CONTEXTO_v13.5.ghx')
root = tree.getroot()

# Find the Object with our target GUID
target_guid = "6eaf2956-f649-4540-a900-4b32a10deee4"

# Look through all Object chunks
for obj in root.iter('object'):
    guid = obj.get('instanceGuid')
    if guid == target_guid:
        nick = obj.get('nickName', '')
        print(f"Found Object: NickName='{nick}', GUID={guid}")
        
        # Look for ScriptFile inside this object
        for chunk in obj.iter('chunk'):
            if chunk.get('name') == 'ScriptFile':
                # Look for script element inside ScriptFile
                for sub in chunk.iter('chunk'):
                    if sub.get('name') == 'script':
                        # Get the text content
                        if len(sub) > 0 and sub[0].text:
                            text = sub[0].text
                            print(f"Script text length: {len(text)} characters")
                            print("\nFirst 10 lines:")
                            lines = text.split('\n')
                            for i, line in enumerate(lines[:10]):
                                print(f"{i+1:2}: {line}")
                            print("\nLast 10 lines:")
                            for i, line in enumerate(lines[-10:], len(lines)-9):
                                print(f"{i:2}: {line}")
                        else:
                            print("Script element found but no text content")
                        break
                break
        break
else:
    print(f"Object with GUID {target_guid} not found")