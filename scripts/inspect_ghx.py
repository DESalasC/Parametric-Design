# -*- coding: utf-8 -*-
"""Inspecciona la estructura de un objeto GHPython en el .ghx."""
import os, re

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")

with open(GHX_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Buscar el nombre F1_CONTEXTO50_BUILD
idx = content.find("F1_CONTEXTO50_BUILD")
print(f"Posición de F1_CONTEXTO50_BUILD: {idx}")

if idx >= 0:
    # Mostrar contexto amplio alrededor
    start = max(0, idx - 3000)
    end = min(len(content), idx + 3000)
    print(content[start:end])
else:
    print("NO ENCONTRADO - mostrando primeros 2000 chars:")
    print(content[:2000])
