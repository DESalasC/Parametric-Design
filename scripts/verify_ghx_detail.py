# -*- coding: utf-8 -*-
"""Verifica el contenido real del CodeInput del componente #45 en el .ghx."""
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
        print('NickName:', nick)
        print('  CR=%d LF=%d OK=%s' % (code.count('\r'), code.count('\n'), code.count('\r') == 0))
        print('  Tiene "-ancla_z":', '-ancla_z' in code or '-ancla' in code)
        print('  Tiene "ancla_canvas_local":', 'ancla_canvas_local' in code)
        print('  Tiene "return 0.0" solo (sin -ancla_z):', ('return 0.0' in code and '-ancla_z' not in code))
        # Extraer la función compute_dz_from_stage1_context
        m_func = re.search(r'def compute_dz_from_stage1_context.*?(?=\ndef |\Z)', code, re.DOTALL)
        if m_func:
            func = m_func.group(0)
            print('  Funcion encontrada, len=%d' % len(func))
            print('  Primeras 400 chars de la funcion:')
            print(func[:400])
        break
