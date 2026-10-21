# -*- coding: utf-8 -*-
"""Lista los NickName reales de todos los GHPython en el .ghx."""
import os, re

GHX = r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico\gh-definitions\F1_CONTEXTO_v13.5.ghx"

with open(GHX, 'r', encoding='utf-8') as f:
    content = f.read()

# Dividir por Object chunks
objetos = re.split(r'<chunk name="Object"', content)
print("Total Object chunks:", len(objetos) - 1)

for obj_text in objetos[1:]:
    m_name = re.search(r'<item name="Name" type_name="gh_string" type_code="10">([^<]+)</item>', obj_text)
    if not m_name or m_name.group(1) != "GhPython Script":
        continue
    
    m_nick = re.search(r'<item name="NickName" type_name="gh_string" type_code="10">([^<]+)</item>', obj_text)
    nick = m_nick.group(1) if m_nick else "?"
    
    m_code = re.search(r'<item name="CodeInput" type_name="gh_string" type_code="10">(.*?)</item>', obj_text, re.DOTALL)
    code = m_code.group(1) if m_code else ""
    
    tiene_return0 = "return 0.0" in code
    tiene_zbase_fallback = "CHIP-contexto.json" in code
    
    # Mostrar solo los que tengan CONTEXTO, PATIO, DISTRIBUCION, VOLUM_GENERADOR, ETAPA1
    if any(k in nick for k in ['CONTEXTO', 'PATIO', 'DISTRIBUCION', 'VOLUM_GENERADOR', 'ETAPA1']):
        print(f"NickName: {nick}")
        print(f"  CodeInput len: {len(code)}")
        print(f"  Tiene 'return 0.0': {tiene_return0}")
        print(f"  Tiene 'CHIP-contexto.json': {tiene_zbase_fallback}")
        print()
