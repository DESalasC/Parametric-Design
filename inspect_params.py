import re

path = r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.7.ghx'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

out_path = r'D:\Work\PROJECTS\DiseñoParametrico\ghx_params.txt'
with open(out_path, 'w', encoding='utf-8') as out:
    def w(s):
        out.write(s + '\n')

    # Find the ParameterData chunk for the first object (F1_ETAPA1_CONTEXTO)
    # Let's look at a region with ParameterData
    idx = content.find('ParameterData')
    w("First ParameterData at: {}".format(idx))
    w(content[idx:idx+5000])

print("wrote", out_path)
