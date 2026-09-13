# -*- coding: utf-8 -*-
"""Parchea el componente F1_CONTEXTO50_BUILD embebido en el canvas v03 (.ghx).

Reemplaza el CodeInput por el codigo del .py fuente, elimina inputs huerfanos
y renumera los indices. Idempotente. Despues de correr, regenerar el .gh con:
  GH_IO.dll: ReadFromFile(.ghx) -> WriteToFile(.gh)  (ver MANUAL o historial).

Uso:
  python patch-ghx-contexto50-v03.py
"""
import io
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = r"D:\Work\PROJECTS\DiseñoParametrico"
GHX = os.path.join(BASE, "gh-definitions", "F1_Contexto_Base-Editado_v03.ghx")
PY_FIXED = os.path.join(BASE, "src", "fase-1-contexto", "F1_CONTEXTO50_BUILD_v01a.py")
INPUT_HUERFANO = "in_altura_default"

ts = datetime.now().strftime("%Y-%m-%d-%H%M")
BACKUP = GHX + ".bak-" + ts

shutil.copy2(GHX, BACKUP)
print("backup:", BACKUP)

with io.open(PY_FIXED, "rb") as f:
    CODIGO_NUEVO = f.read().decode("utf-8")
print("codigo nuevo: {0} chars".format(len(CODIGO_NUEVO)))

tree = ET.parse(GHX)
root = tree.getroot()
parent = {c: p for p in root.iter() for c in p}

code_el = None
for el in root.iter():
    if el.get("name") == "CodeInput" and el.text and "CONTEXTO50" in el.text \
            and len(el.text) > 10000:
        code_el = el
        break
if code_el is None:
    print("ERROR: no se encontro el CodeInput del componente")
    sys.exit(1)

obj = None
cur = code_el
while cur is not None:
    if cur.get("name") == "Object" and cur.get("index") is not None:
        obj = cur
        break
    cur = parent.get(cur)
print("Object index:", obj.get("index"))

if (code_el.text or "") == CODIGO_NUEVO:
    print("CodeInput ya esta actualizado")
else:
    viejo = len(code_el.text or "")
    code_el.text = CODIGO_NUEVO
    print("CodeInput: {0} -> {1} chars".format(viejo, len(CODIGO_NUEVO)))

# ---- ParameterData (un solo chunk con wrappers <items>/<chunks>) ----
pd = None
for ch in obj.iter():
    if ch.get("name") == "ParameterData":
        pd = ch
        break
if pd is None:
    print("ERROR: ParameterData no encontrado")
    sys.exit(1)


def encontrar_padre(padre, nombre, idx=None):
    for p in padre.iter():
        for c in list(p):
            if c.get("name") == nombre and (idx is None or c.get("index") == idx):
                return p, c
    return None, None


def inputs_actuales():
    out = []
    for p in pd.iter():
        for c in list(p):
            if c.get("name", "").startswith("InputParam"):
                nick = None
                guid = None
                for s2 in c.iter():
                    if s2.get("name") == "NickName":
                        nick = (s2.text or "").strip()
                    if s2.get("name") == "InstanceGuid":
                        guid = (s2.text or "").strip()
                out.append((c, nick, guid))
    return out


# ---- quitar input huerfano si existe ----
huerfano = [t for t in inputs_actuales() if t[1] == INPUT_HUERFANO]
if huerfano:
    sub, nick, guid = huerfano[0]
    referencias = 0
    for src in root.iter():
        if src.get("name") == "Source" and src.tag == "item":
            if (src.text or "").strip() == guid:
                referencias += 1
    if referencias:
        print("ERROR: {0} tiene {1} referencias; abortando".format(INPUT_HUERFANO, referencias))
        sys.exit(1)
    p_sub, _ = encontrar_padre(pd, "InputParam", sub.get("index"))
    if p_sub is not None:
        p_sub.remove(sub)
    p_count, c_count = encontrar_padre(pd, "InputCount")
    old_n = int(c_count.text)
    c_count.text = str(old_n - 1)
    p_id, c_id = encontrar_padre(pd, "InputId", str(old_n - 1))
    if p_id is not None and c_id is not None:
        p_id.remove(c_id)
    print("input huerfano '{0}' removido: InputCount {1} -> {2}".format(
        INPUT_HUERFANO, old_n, old_n - 1))
else:
    print("sin input huerfano '{0}'".format(INPUT_HUERFANO))

# ---- renumerar InputParam 0..n-1 (idempotente) ----
ips = [t[0] for t in inputs_actuales()]
antes = [c.get("index") for c in ips]
for i, c in enumerate(ips):
    c.set("index", str(i))
print("InputParam idx: {0} -> {1}".format(antes, [str(i) for i in range(len(ips))]))

# ---- escribir + validar ----
tree.write(GHX, xml_declaration=True, encoding="utf-8")
print("escrito:", GHX)

tree2 = ET.parse(GHX)
root2 = tree2.getroot()
n_code = 0
for el in root2.iter():
    if el.get("name") == "CodeInput" and el.text and "CONTEXTO50" in el.text \
            and len(el.text) > 10000:
        n_code += 1
        if el.text != CODIGO_NUEVO:
            print("ERROR: texto CodeInput no coincide")
            sys.exit(1)
n_bad = 0
for el in root2.iter():
    if el.tag == "items":
        for c in el:
            if c.tag == "chunk" and c.get("name") == "PersistentData":
                n_bad += 1
ic = ii = ip = None
for el in root2.iter():
    if el.get("name") == "InputCount":
        ic = el.text
print("VALIDACION: CodeInput ok ({0}) | chunks mal ubicados: {1} | InputCount: {2}".format(
    n_code, n_bad, ic))
