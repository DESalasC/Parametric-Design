with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'r', encoding='utf-8') as f:
    content = f.read()

# The file structure should be:
# 1. Module-level functions: _unwrap, _parse_json_input
# 2. if _es_gh: block with GH processing code
# 3. else: main()

# First, let's extract the functions and put them at module level (before if _es_gh:)
# Find the function definitions
import re

# Find _unwrap function
unwrap_match = re.search(r'(^def _unwrap\(v\):.*?^def _parse_json_input)', content, re.MULTILINE | re.DOTALL)
if unwrap_match:
    unwrap_func = unwrap_match.group(1)
    print('Found _unwrap function')

# Find _parse_json_input function  
parse_match = re.search(r'(^def _parse_json_input\(v\):.*?)(?=^# Debug:|^if _es_gh:|^else:)', content, re.MULTILINE | re.DOTALL)
if parse_match:
    parse_func = parse_match.group(1)
    print('Found _parse_json_input function')

# Find the GH processing code (between the functions and else:)
gh_code_match = re.search(r'(^# Debug: listar globales disponibles.*?)(?=^else:)', content, re.MULTILINE | re.DOTALL)
if gh_code_match:
    gh_code = gh_code_match.group(1)
    print('Found GH code')

# Find the else block
else_match = re.search(r'(^else:.*?^main\(\))', content, re.MULTILINE | re.DOTALL)
if else_match:
    else_block = else_match.group(1)
    print('Found else block')

# Now rebuild the file properly
# Get everything before the first function
before_funcs = content[:unwrap_match.start()] if unwrap_match else ''

# Build new content
new_content = before_funcs.rstrip() + '\n\n'
new_content += unwrap_func.rstrip() + '\n\n'
new_content += parse_func.rstrip() + '\n\n'
new_content += 'if _es_gh:\n'
# Indent the GH code
for line in gh_code.splitlines(True):
    new_content += '    ' + line
new_content += '\n'
new_content += else_block

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Rebuilt file structure')
