"""Test full v06 root deepcopy + serialize."""
from lxml import etree
import copy

v06 = etree.parse(r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx")
root = v06.getroot()

# Deep copy the entire root
root_copy = copy.deepcopy(root)

# Find DefinitionObjects
old_def = root_copy.find('.//chunk[@name="DefinitionObjects"]')
print(f"DefObjs found: {old_def is not None}")

# Try tostring on the whole tree
s = etree.tostring(root_copy, encoding='unicode')
print(f"Serialized size: {len(s)} bytes")

# Try re-parsing
try:
    reparsed = etree.fromstring(s)
    print(f"Re-parsed: tag={reparsed.tag}")
    # Check DefinitionObjects is still there
    defobjs = reparsed.find('.//chunk[@name="DefinitionObjects"]')
    print(f"DefObjs in reparsed: {defobjs is not None}")
    if defobjs is not None:
        objs = list(defobjs.findall('.//chunk[@name="Object"]'))
        print(f"Objects in reparsed: {len(objs)}")
except Exception as e:
    print(f"RE-PARSE ERROR: {e}")
