import re

path = r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.7.ghx'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

out_path = r'D:\Work\PROJECTS\DiseñoParametrico\ghx_structure.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    def w(s):
        out.write(s + '\n')

    w("TOTAL CHARS: {}".format(len(content)))

    # Find DefinitionObjects chunk
    idx = content.find('DefinitionObjects')
    w("DefinitionObjects at: {}".format(idx))
    w(content[idx:idx+4000])

print("wrote", out_path)
