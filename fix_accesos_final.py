with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Split the content into parts
# 1. Everything before 'if _es_gh:' (line 292) - this is the module-level code
# 2. The GH block code (indented)
# 3. The else block

# Find the positions
idx_if_es_gh = content.find('if _es_gh:')
idx_else = content.rfind('else:\n    # MODO CLI: ejecutar main()')

print('if _es_gh at:', idx_if_es_gh)
print('else at:', idx_else)

# Part 1: module level code (before if _es_gh:)
module_code = content[:idx_if_es_gh]

# Part 2: GH block code (between if _es_gh: and the else block)
gh_block = content[idx_if_es_gh:idx_else]

# Part 3: else block
else_block = content[idx_else:]

# Now extract the two functions from the GH block (they're at 4-space indent)
# and move them to module level
import re

# Extract _unwrap function (at 4-space indent in the block)
unwrap_match = re.search(r'^    def _unwrap\(v\):.*?(?=^    def _parse_json_input|^    # Debug:)', gh_block, re.MULTILINE | re.DOTALL)
if unwrap_match:
    unwrap_func = unwrap_match.group(0)
    # Remove the 4-space indent
    unwrap_func = '\n'.join(line[4:] if line.startswith('    ') else line for line in unwrap_func.splitlines())
    print('Extracted _unwrap')

# Extract _parse_json_input function
parse_match = re.search(r'^    def _parse_json_input\(v\):.*?(?=^    # Debug:)', gh_block, re.MULTILINE | re.DOTALL)
if parse_match:
    parse_func = parse_match.group(0)
    parse_func = '\n'.join(line[4:] if line.startswith('    ') else line for line in parse_func.splitlines())
    print('Extracted _parse_json_input')

# Extract GH processing code (after the functions, at 8-space indent)
# Find the '# Debug:' line in gh_block
debug_idx = gh_block.find('# Debug: listar globales disponibles')
if debug_idx != -1:
    gh_processing = gh_block[debug_idx:]
    # Remove 8-space indent (or 4-space if it's at block level)
    gh_processing = '\n'.join(line[8:] if line.startswith('        ') else (line[4:] if line.startswith('    ') else line) for line in gh_processing.splitlines())
    print('Extracted GH processing')

# Rebuild
new_content = module_code.rstrip() + '\n\n'
new_content += unwrap_func.rstrip() + '\n\n'
new_content += parse_func.rstrip() + '\n\n'
new_content += 'if _es_gh:\n'
for line in gh_processing.splitlines(True):
    new_content += '    ' + line
new_content += '\n'
new_content += else_block

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_ACCESOS_INTEGRADOR_v02.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('File rebuilt')
