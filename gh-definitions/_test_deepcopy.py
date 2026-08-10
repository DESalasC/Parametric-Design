"""Test if lxml deepcopy + roundtrip works for GHX fragments."""
from lxml import etree
import copy

paths = [
    r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx",
    r"D:\Work\PROJECTS\DiseñoParametrico\tests\core\test_06_plugin_component.ghx",
]

for p in paths:
    print(f"\n=== {p.split(chr(92))[-1]} ===")
    t = etree.parse(p)
    objs = list(t.findall('.//chunk[@name="Object"]'))
    print(f"Objects: {len(objs)}")
    
    # Test first 5 objects
    for i, o in enumerate(objs[:5]):
        name_it = o.find('items/item[@name="Name"]')
        name = name_it.text if name_it is not None else '?'
        
        # Deep copy
        c = copy.deepcopy(o)
        
        # Serialize
        s = etree.tostring(c, encoding='unicode')
        
        # Re-parse
        try:
            c2 = etree.fromstring(s)
            ok = "OK" if c2.tag == o.tag else "TAG MISMATCH"
        except Exception as e:
            ok = f"PARSE ERROR: {e}"
        
        print(f"  [{i}] {name:25s} deepcopy->serialize->parse: {ok}  ({len(s)} bytes)")
