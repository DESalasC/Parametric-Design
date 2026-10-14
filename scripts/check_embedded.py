with open(r'D:\Work\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.5.ghx', 'r', encoding='utf-8-sig') as f:
    content = f.read()

start = 1993679
end = content.find('</', start)
snippet = content[start:end]

# Replace HTML entities
snippet = snippet.replace('<', '<').replace('>', '>').replace('&', '&').replace('"', '"').replace(''', "'")

# Check for syntax errors
try:
    compile(snippet, 'embedded', 'exec')
    print('Embedded (decoded): No syntax errors')
except SyntaxError as e:
    print('Embedded SyntaxError at line {}: {}'.format(e.lineno, e.msg))
    print('Line: {}'.format(e.text))