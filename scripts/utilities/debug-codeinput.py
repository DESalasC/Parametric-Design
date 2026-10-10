# -*- coding: utf-8 -*-
"""Debug: list all CodeInput items in the .ghx and their guids."""
import xml.etree.ElementTree as ET
import hashlib

BASE = r"D:\Work\PROJECTS\DiseñoParametrico"
GHX = BASE + r"\gh-definitions\F1_CONTEXTO_v13.2.ghx"

def items_dict(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d[i.get('name')] = (i.text or '').strip()
    return d

tree = ET.parse(GHX)
root = tree.getroot()
print('Total objects:', len([o for o in root.iter('chunk') if o.get('name') == 'Object']))
for o in root.iter('chunk'):
    if o.get('name') != 'Object':
        continue
    # find container
    container = None
    for c in o.iter('chunk'):
        if c.get('name') == 'Container':
            container = c
            break
    if container is None:
        continue
    d = items_dict(container)
    nick = d.get('NickName', '')
    guid = d.get('InstanceGuid', '')
    # find CodeInput item
    code_item = None
    for i in o.iter('item'):
        if i.get('name') == 'CodeInput':
            code_item = i
            break
    if code_item is None:
        continue
    code_text = code_item.text or ''
    sha = hashlib.sha1(code_text.encode('utf-8')).hexdigest()
    print(f'Object: {nick} ({guid[:8]})')
    print(f'  CodeInput length: {len(code_text)}')
    print(f'  CodeInput SHA1: {sha}')
    print()