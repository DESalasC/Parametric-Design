import re
with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the _unwrap function using regex
content = re.sub(
    r'def _unwrap\(v\):.*?def _parse_json_input\(v\):\\n    \"\"\"Parsea entrada JSON',
    '''def _unwrap(v):
    if v is None:
        return None
    # GH DataTree / GH_Structure (Grasshopper.Kernel.Data.GH_Structure)
    if hasattr(v, \"Branch\") and hasattr(v, \"PathCount\"):
        try:
            from Grasshopper.Kernel.Data import GH_Path
            path = GH_Path(0, 0)
            branch = v.Branch(path)
            if branch and branch.Count > 0:
                return _unwrap(branch[0])
            for i in range(v.PathCount):
                b = v.get_Branch(i)
                if b and b.Count > 0:
                    return _unwrap(b[0])
        except:
            pass
    if hasattr(v, \"Value\"):
        return v.Value
    if isinstance(v, (list, tuple)) and len(v) > 0:
        return _unwrap(v[0])
    return v

def _parse_json_input(v):
    \"\"\"Parsea entrada JSON: string, archivo .json, o dict/list ya parseado.\"\"\"''',
    content,
    flags=re.DOTALL
)

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed _unwrap function')
