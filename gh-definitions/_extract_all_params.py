"""Extract all Container structures from v06 + test_06 as templates."""
from lxml import etree
import copy, json

sources = [
    (r"D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_Contexto_v06.ghx", "v06"),
    (r"D:\Work\PROJECTS\DiseñoParametrico\tests\core\test_06_plugin_component.ghx", "test06"),
]

TARGET_NAMES = [
    'Group', 'Panel', 'Number Slider', 'Python 3 Script',
    'Area', 'Explode', 'Curve Middle', 'Vector 2Pt',
    'Deconstruct Brep', 'Join Curves', '2D Polyline', 'Deconstruct 2D Polyline',
    'Curve Frame', 'Angle',
]

for fpath, label in sources:
    t = etree.parse(fpath)
    for obj in t.findall('.//chunk[@name="Object"]'):
        name_it = obj.find('items/item[@name="Name"]')
        if name_it is None: continue
        name = (name_it.text or '').strip()
        if name not in TARGET_NAMES: continue
        
        # Extract param_input/output details
        container = obj.find('.//chunk[@name="Container"]')
        if container is None: continue
        
        print(f"\n{'='*60}")
        print(f"=== {name} (from {label}) ===")
        
        # Container items
        cont_items = container.find('items')
        if cont_items is not None:
            item_names = [it.get('name') for it in cont_items]
            print(f"Container items({len(item_names)}): {item_names}")
        
        # Param specs
        inputs = container.findall('.//chunk[@name="param_input"]')
        outputs = container.findall('.//chunk[@name="param_output"]')
        print(f"param_inputs: {len(inputs)}, param_outputs: {len(outputs)}")
        
        if inputs:
            pi = inputs[0]
            pi_items = pi.find('items')
            if pi_items is not None:
                names = [it.get('name') for it in pi_items]
                print(f"  Input items({len(names)}): {names}")
        
        if outputs:
            po = outputs[0]
            po_items = po.find('items')
            if po_items is not None:
                names = [it.get('name') for it in po_items]
                print(f"  Output items({len(names)}): {names}")
        
        # List all param names
        in_names = [pi.find('items/item[@name="Name"]').text for pi in inputs if pi.find('items/item[@name="Name"]') is not None]
        out_names = [po.find('items/item[@name="Name"]').text for po in outputs if po.find('items/item[@name="Name"]') is not None]
        print(f"  Inputs: {in_names}")
        print(f"  Outputs: {out_names}")
