import re

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-3-masa\F3_VOLUM_GENERADOR_v08.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Check for f-strings (Python 3 only)
fstrings = [(m.start(), m.group()[:50]) for m in re.finditer(r'f"[^"]*\{', content)]
for pos, match in fstrings:
    line_num = content[:pos].count('\n') + 1
    print(f'Line {line_num}: f-string: {match}')

# Check for walrus operator
walrus = [(m.start(), m.group()[:50]) for m in re.finditer(r':=', content)]
for pos, match in walrus:
    line_num = content[:pos].count('\n') + 1
    print(f'Line {line_num}: walrus: {match}')

# Check for Python 3 only syntax in general
# Check for async/await
async_matches = [(m.start(), m.group()[:50]) for m in re.finditer(r'\basync\b|\bawait\b', content)]
for pos, match in async_matches:
    line_num = content[:pos].count('\n') + 1
    print(f'Line {line_num}: async/await: {match}')

# Check for type hints
type_hints = [(m.start(), m.group()[:50]) for m in re.finditer(r':\s*[A-Z][a-z]+\[', content)]
for pos, match in type_hints[:10]:
    line_num = content[:pos].count('\n') + 1
    print(f'Line {line_num}: type hint: {match}')

# Check for match/case
match_case = [(m.start(), m.group()[:50]) for m in re.finditer(r'\bmatch\b|\bcase\b', content)]
for pos, match in match_case:
    line_num = content[:pos].count('\n') + 1
    print(f'Line {line_num}: match/case: {match}')