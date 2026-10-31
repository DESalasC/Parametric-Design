import re

path = r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.7.ghx'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

out_path = r'D:\Work\PROJECTS\DiseñoParametrico\ghx_full.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    def w(s):
        out.write(s + '\n')

    object_chunks = re.findall(r'<chunk name="Object"[^>]*>.*?</chunk>', content, flags=re.DOTALL)
    # NOTE: the above regex is non-greedy and will break on nested chunks, but for the
    # top-level Object chunks we need proper nesting too. Let's instead find Object chunks
    # by tracking chunk nesting depth.
    w("Using depth-aware chunk extraction...")

    def extract_chunks(text, chunk_name):
        """Extract all chunks named chunk_name with proper nesting depth handling."""
        results = []
        i = 0
        n = len(text)
        open_tag = '<chunk name="' + chunk_name + '"'
        while True:
            idx = text.find(open_tag, i)
            if idx == -1:
                break
            # find end of opening tag
            gt = text.find('>', idx)
            if gt == -1:
                break
            # depth-aware scan for matching close
            depth = 1
            j = gt + 1
            while j < n and depth > 0:
                # look for next <chunk ...> or </chunk>
                next_open = text.find('<chunk ', j)
                next_close = text.find('</chunk>', j)
                if next_close == -1:
                    break
                if next_open != -1 and next_open < next_close:
                    depth += 1
                    j = next_open + 1
                else:
                    depth -= 1
                    j = next_close + len('</chunk>')
                    if depth == 0:
                        results.append(text[idx:j])
                        i = j
                        break
            else:
                break
        return results

    object_chunks = extract_chunks(content, 'Object')
    w("Object chunks (depth-aware): {}".format(len(object_chunks)))

    ACCESS_MAP = {0: 'Item', 1: 'List', 2: 'Tree'}

    def get_item(chunk, name):
        m = re.search(r'<item name="' + re.escape(name) + r'"[^>]*>(.*?)</item>', chunk, flags=re.DOTALL)
        return m.group(1).strip() if m else None

    def get_items(chunk, name):
        return [m.group(1).strip() for m in re.finditer(r'<item name="' + re.escape(name) + r'"[^>]*>(.*?)</item>', chunk, flags=re.DOTALL)]

    components = []
    for oc in object_chunks:
        instance_guid = get_item(oc, 'InstanceGuid')
        nickname = get_item(oc, 'NickName')
        name = get_item(oc, 'Name')
        code_input = get_item(oc, 'CodeInput')

        pd_chunks = extract_chunks(oc, 'ParameterData')
        pd_text = pd_chunks[0] if pd_chunks else ''

        input_params = extract_chunks(oc, 'InputParam')
        output_params = extract_chunks(oc, 'OutputParam')

        inputs = []
        for ipt in input_params:
            inputs.append({
                'instance_guid': get_item(ipt, 'InstanceGuid'),
                'name': get_item(ipt, 'Name'),
                'nickname': get_item(ipt, 'NickName'),
                'access': ACCESS_MAP.get(int(get_item(ipt, 'ScriptParamAccess') or '-1'), '?'),
                'typehint_id': get_item(ipt, 'TypeHintID'),
                'source': get_items(ipt, 'Source'),
            })

        outputs = []
        for opt in output_params:
            outputs.append({
                'instance_guid': get_item(opt, 'InstanceGuid'),
                'name': get_item(opt, 'Name'),
                'nickname': get_item(opt, 'NickName'),
                'typehint_id': get_item(opt, 'TypeHintID'),
            })

        components.append({
            'instance_guid': instance_guid,
            'nickname': nickname,
            'name': name,
            'code_input': code_input,
            'inputs': inputs,
            'outputs': outputs,
        })

    w("\n=== ALL COMPONENTS ===")
    for c in components:
        w("GUID: {} | Name: {} | NickName: {}".format(c['instance_guid'], c['name'], c['nickname']))

    th_ids = set()
    for c in components:
        for i in c['inputs']:
            if i['typehint_id']:
                th_ids.add(i['typehint_id'])
        for o in c['outputs']:
            if o['typehint_id']:
                th_ids.add(o['typehint_id'])
    w("\n=== UNIQUE TypeHintID GUIDs ({}) ===".format(len(th_ids)))
    for t in sorted(th_ids):
        w(t)

    # Now dump detail for ArchiCAD + GHPython components
    special = [c for c in components if c['name'] in ('ConnectArchicad','GetLayersDetails','Layers') or c['name']=='GhPython Script']
    w("\n=== DETAIL: ArchiCAD + GHPython components ===")
    for c in special:
        w("\n--- GUID: {} | Name: {} | NickName: {} ---".format(c['instance_guid'], c['name'], c['nickname']))
        w("INPUTS:")
        for i in c['inputs']:
            w("   name={} nickname={} access={} typehintID={} source={}".format(i['name'], i['nickname'], i['access'], i['typehint_id'], i['source']))
        w("OUTPUTS:")
        for o in c['outputs']:
            w("   name={} nickname={} typehintID={}".format(o['name'], o['nickname'], o['typehint_id']))

print("wrote", out_path)
