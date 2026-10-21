# -*- coding: utf-8 -*-
"""Verifica que el CodeInput del componente #45 en el .ghx tenga LF limpio y sin fallback a CHIP-contexto.json."""
import os, re

GHX = r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.5.ghx"

with open(GHX, 'r', encoding='utf-8') as f:
    content = f.read()

objetos = re.split(r'<chunk name="Object"', content)
for obj_text in objetos[1:]:
    m_name = re.search(r'<item name="Name" type_name="gh_string" type_code="10">([^<]+)</item>', obj_text)
    if not m_name or m_name.group(1) != 'GhPython Script':
        continue
    m_nick = re.search(r'<item name="NickName" type_name="gh_string" type_code="10">([^<]+)</item>', obj_text)
    nick = m_nick.group(1) if m_nick else '?'
    if '#45-' not in nick:
        continue
    m_code = re.search(r'<item name="CodeInput" type_name="gh_string" type_code="10">(.*?)</item>', obj_text, re.DOTALL)
    if m_code:
        code = m_code.group(1)
        cr = code.count('\r')
        lf = code.count('\n')
        print('NickName:', nick)
        print('  CodeInput CR=%d LF=%d OK=%s' % (cr, lf, cr == 0))
        print('  Tiene CHIP-contexto.json:', 'CHIP-contexto.json' in code)
        print('  Tiene return 0.0:', 'return 0.0' in code)
