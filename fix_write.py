with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_DISTRIBUCION_v03.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''def _escribir_texto(ruta, texto):
    \"\"\"v03.3 - Escribe texto UTF-8 en modo binario (sin codec por defecto).\"\"\"
    ruta_t = _texto_seguro(ruta)
    if not isinstance(texto, bytes):
        texto = _texto_seguro(texto).encode(\"utf-8\")
    with open(ruta_t, \"wb\") as f:
        f.write(texto)'''

new = '''def _escribir_texto(ruta, texto):
    \"\"\"v03.3 - Escribe texto UTF-8 en modo binario (sin codec por defecto).\"\"\"
    ruta_t = _texto_seguro(ruta)
    if not isinstance(texto, bytes):
        texto = _texto_seguro(texto).encode(\"utf-8\")
    # Crear directorio si no existe
    dir_path = os.path.dirname(ruta_t)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(ruta_t, \"wb\") as f:
        f.write(texto)'''

if old in content:
    content = content.replace(old, new)
    with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_DISTRIBUCION_v03.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed _escribir_texto')
else:
    print('Pattern not found')
