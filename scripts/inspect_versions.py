# -*- coding: utf-8 -*-
"""Inspecciona las versiones embebidas de los 5 componentes clave en el .ghx."""
import os, re, sys

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")

with open(GHX_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

objetos = re.split(r'<chunk name="Object"', content)

print(f"Total Object chunks: {len(objetos)-1}")
print("=" * 100)

nombres_buscados = ["F1_CONTEXTO50_BUILD", "F1_ETAPA1_CONTEXTO", "F1_ETAPA2_PATIO", "F3_DISTRIBUCION", "F3_VOLUM_GENERADOR"]

for obj_text in objetos[1:]:
    m_guid = re.search(r'<item name="GUID" type_name="gh_guid" type_code="9">([^<]+)</item>', obj_text)
    m_name = re.search(r'<item name="Name" type_name="gh_string" type_code="10">([^<]+)</item>', obj_text)
    
    if not m_name or m_name.group(1) != "GhPython Script":
        continue
    
    guid = m_guid.group(1) if m_guid else "?"
    
    m_nick = re.search(r'<item name="NickName" type_name="gh_string" type_code="10">([^<]+)</item>', obj_text)
    nick = m_nick.group(1) if m_nick else "?"
    
    m_code = re.search(r'<item name="CodeInput" type_name="gh_string" type_code="10">(.*?)</item>', obj_text, re.DOTALL)
    code = m_code.group(1) if m_code else ""
    
    version_line = ""
    for line in code.split('\n')[:30]:
        s = line.strip()
        if any(k in s for k in ['v01', 'v02', 'v03', 'v08', 'CAMBIOS', 'CORRECCIONES']):
            version_line = s[:90]
            break
    
    tiene_zbase = "Z_base" in code or "desplazamiento_z" in code or "min_z" in code
    
    match = any(nb in nick for nb in nombres_buscados)
    if match:
        vline_safe = version_line.encode('ascii', 'replace').decode('ascii')
        print(f"NickName: {nick}")
        print(f"  GUID: {guid}")
        print(f"  Version: {vline_safe}")
        print(f"  Tiene Z-BASE: {tiene_zbase}")
        print()
