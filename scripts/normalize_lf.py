# -*- coding: utf-8 -*-
"""Normaliza terminaciones de línea de F1_CONTEXTO50_BUILD_v01.2.py a LF."""
import os

p = r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_CONTEXTO50_BUILD_v01.2.py"
with open(p, 'rb') as f:
    data = f.read()
data2 = data.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
with open(p, 'wb') as f:
    f.write(data2)
with open(p, 'rb') as f:
    d = f.read()
print(p, ": CR=", d.count(b'\r'), " LF=", d.count(b'\n'), " OK=", d.count(b'\r') == 0)
