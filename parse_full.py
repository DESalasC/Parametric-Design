import re

path = r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.7.ghx'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

out_path = r'D:\Work\PROJECTS\DiseñoParametrico\ghx_full.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    def w(s):
        out.write(s + '\n')

    # Split into Object chunks within DefinitionObjects
    # Find DefinitionObjects region
    start = content.find('<chunk name="DefinitionObjects"')
    end = content.find('</chunk>', start)
    # But DefinitionObjects has nested chunks; find matching closing chunk is hard with regex.
    # Instead just find all <chunk name="Object" ...>...</chunk> globally (already works)
    object_chunks = re.findall(r'<chunk name="Object"[^>]*>.*?</chunk>', content, flags=re.DOTALL)
    w("Object chunks: {}".format(len(object_chunks)))

    ACCESS_MAP = {0: 'Item', 1: 'List', 2: 'Tree'}

    def get_item(chunk, name, index=None):
        if index is not None:
            pattern = r'<item name="' + re.escape(name) + r'" index="%d"[^>]*>(.*?)</item>' % index
            m = re.search(pattern, chunk, flags=re.DOTALL)
        else:
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

        # ParameterData
        pd = re.search(r'<chunk name="ParameterData".*?</chunk>', oc, flags=re.DOTALL)
        pd_text = pd.group(0) if pd else ''

        input_count = int(get_item(pd_text, 'InputCount') or '0')
        output_count = int(get_item(pd_text, 'OutputCount') or '0')

        input_ids = get_items(pd_text, 'InputId')
        output_ids = get_items(pd_text, 'OutputId')

        # InputParams
        inputs = []
        for ip in re.finditer(r'<chunk name="InputParam"[^>]*>.*?</chunk>', oc, flags=re.DOTALL):
            ipt = ip.group(0)
            inputs.append({
                'instance_guid': get_item(ipt, 'InstanceGuid'),
                'name': get_item(ipt, 'Name'),
                'nickname': get_item(ipt, 'NickName'),
                'access': ACCESS_MAP.get(int(get_item(ipt, 'ScriptParamAccess') or '-1'), str(get_item(ipt, 'ScriptParamAccess'))),
                'typehint_id': get_item(ipt, 'TypeHintID'),
                'source': get_items(ipt, 'Source'),
                'optional': get_item(ipt, 'Optional'),
                'allow_tree': get_item(ipt, 'AllowTreeAccess'),
            })

        # OutputParams
        outputs = []
        for op in re.finditer(r'<chunk name="OutputParam"[^>]*>.*?</chunk>', oc, flags=re.DOTALL):
            opt = op.group(0)
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
            'input_count': input_count,
            'output_count': output_count,
        })

    w("\n=== ALL COMPONENTS ===")
    for c in components:
        w("GUID: {} | Name: {} | NickName: {}".format(c['instance_guid'], c['name'], c['nickname']))

    # Collect all typehint IDs
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

print("wrote", out_path)
