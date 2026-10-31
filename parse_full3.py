import re

path = r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.7.ghx'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

out_path = r'D:\Work\PROJECTS\DiseñoParametrico\ghx_full.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    def w(s):
        out.write(s + '\n')

    ACCESS_MAP = {0: 'Item', 1: 'List', 2: 'Tree'}

    def get_item(chunk, name):
        m = re.search(r'<item name="' + re.escape(name) + r'"[^>]*>(.*?)</item>', chunk, flags=re.DOTALL)
        return m.group(1).strip() if m else None

    def get_items(chunk, name):
        return [m.group(1).strip() for m in re.finditer(r'<item name="' + re.escape(name) + r'"[^>]*>(.*?)</item>', chunk, flags=re.DOTALL)]

    # Find all Object chunk regions by locating each '<chunk name="Object"' and taking
    # a bounded slice up to the next '<chunk name="Object"' or '</chunks>' of DefinitionObjects.
    # Simpler: use regex findall for Object chunks. Non-greedy works because Object chunks
    # don't contain another Object chunk. The first '</chunk>' might be nested (Attributes),
    # but we only need InstanceGuid/NickName/Name/CodeInput which are in Container items,
    # all before the nested Attributes chunk. So we can take a generous prefix.
    object_starts = [m.start() for m in re.finditer(r'<chunk name="Object"', content)]
    w("Object starts: {}".format(len(object_starts)))

    components = []
    for si in object_starts:
        # take a slice from this Object start to the next Object start (or +200000 chars)
        next_si = None
        for ns in object_starts:
            if ns > si:
                next_si = ns
                break
        end = next_si if next_si else si + 300000
        oc = content[si:end]

        instance_guid = get_item(oc, 'InstanceGuid')
        nickname = get_item(oc, 'NickName')
        name = get_item(oc, 'Name')
        code_input = get_item(oc, 'CodeInput')

        # InputParams: find each '<chunk name="InputParam"' within oc, take prefix up to '<chunks count='
        inputs = []
        for m in re.finditer(r'<chunk name="InputParam"[^>]*>', oc):
            start = m.start()
            # end at next '<chunks count=' or next '<chunk name="InputParam"' or '</chunk>' at depth
            sub = oc[start:]
            # cut at first '<chunks count='
            cut = sub.find('<chunks count=')
            if cut == -1:
                cut = len(sub)
            ipt = sub[:cut]
            inputs.append({
                'instance_guid': get_item(ipt, 'InstanceGuid'),
                'name': get_item(ipt, 'Name'),
                'nickname': get_item(ipt, 'NickName'),
                'access': ACCESS_MAP.get(int(get_item(ipt, 'ScriptParamAccess') or '-1'), '?'),
                'typehint_id': get_item(ipt, 'TypeHintID'),
                'source': get_items(ipt, 'Source'),
            })

        # OutputParams
        outputs = []
        for m in re.finditer(r'<chunk name="OutputParam"[^>]*>', oc):
            start = m.start()
            sub = oc[start:]
            cut = sub.find('<chunks count=')
            if cut == -1:
                cut = len(sub)
            opt = sub[:cut]
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

    w("Components parsed: {}".format(len(components)))

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

    w("\n=== DETAIL: ArchiCAD + GHPython components ===")
    special = [c for c in components if c['name'] in ('ConnectArchicad','GetLayersDetails','Layers') or c['name']=='GhPython Script']
    for c in special:
        w("\n--- GUID: {} | Name: {} | NickName: {} ---".format(c['instance_guid'], c['name'], c['nickname']))
        w("INPUTS ({}):".format(len(c['inputs'])))
        for i in c['inputs']:
            w("   name={!r} nickname={!r} access={} typehintID={} source={}".format(i['name'], i['nickname'], i['access'], i['typehint_id'], i['source']))
        w("OUTPUTS ({}):".format(len(c['outputs'])))
        for o in c['outputs']:
            w("   name={!r} nickname={!r} typehintID={}".format(o['name'], o['nickname'], o['typehint_id']))

print("wrote", out_path)
