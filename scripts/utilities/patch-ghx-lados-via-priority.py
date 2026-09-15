# -*- coding: utf-8 -*-
"""Prioridad vía/EP sobre medianería por vértices en el LADOS del canvas v03.

Parchea el bloque 4a/4b del componente F1_ETAPA2_LADOS (GHPython) embebido en
`F1_Contexto_Base-Editado_v03.ghx`, para que un lado "pegado a la vía"
(contacto por longitud >= 0.30 o vértices coincidentes con vecinos) se
clasifique Frontal/EspacioPublico y NO reciba aislamiento lateral.

Idempotente y con backup por timestamp. Tras correrlo, regenerar el .gh con
GH_IO (scripts/utilities/ghx-to-gh.ps1).

Uso:  python patch-ghx-lados-via-priority.py
"""
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = r"D:\Work\PROJECTS\DiseñoParametrico"
GHX = os.path.join(BASE, "gh-definitions", "F1_Contexto_Base-Editado_v03.ghx")

OLD = """            motivo_lado = ""
            # 4a) Lateral por VERTICES COINCIDENTES con vecinos (< 0.10 m):
            #     la medianeria gana aunque haya una via cerca sin contacto
            if lado_lateral_por_vertices(p1, p2, vecinos_list):
                toca_via = False
                toca_ep = False
                toca_vecino = True
                cat = "Lateral"
                motivo_lado = "vertices coincidentes con vecino"
                f_v = 0.0
                f_e = 0.0
                f_n = 1.0
            else:
                # 4b) Contacto por LONGITUD MINIMA (fraccion del lado)
                f_v, f_e, f_n = fracciones_contacto(
                    p1, p2, vias_list, ep_list, vecinos_list)
                toca_via = f_v >= CONTACTO_MIN_FRACCION
                toca_ep = f_e >= CONTACTO_MIN_FRACCION
                toca_vecino = f_n >= CONTACTO_MIN_FRACCION
                if toca_via:
                    cat = "Frontal"
                    motivo_lado = "contacto via {:.0%}".format(f_v)
                elif toca_ep:
                    cat = "EspacioPublico"
                    motivo_lado = "contacto EP {:.0%}".format(f_e)
                elif toca_vecino:
                    cat = "Lateral"
                    motivo_lado = "contacto vecino {:.0%}".format(f_n)
                else:
                    cat = "Lateral"  # provisional; la regla posterior puede reclasificar
                    motivo_lado = "sin contacto minimo"""

NEW = """            motivo_lado = ""
            # 4) Contacto con via/EP por LONGITUD MINIMA (fraccion del lado).
            #    v06.4 (2026-09-15): se evalua SIEMPRE y TIENE PRIORIDAD sobre la
            #    medianeria por vertices. Un lado "pegado a la via" es FRENTE (o
            #    EP), NO medianeria: no debe recibir aislamiento lateral. (Bug: la
            #    regla 4a forzaba toca_via=False y Lateral aunque el lado estuviera
            #    sobre la via, restando area util del primer piso y tumbando F2.)
            f_v, f_e, f_n = fracciones_contacto(
                p1, p2, vias_list, ep_list, vecinos_list)
            bordea_via = f_v >= CONTACTO_MIN_FRACCION
            bordea_ep = f_e >= CONTACTO_MIN_FRACCION
            if bordea_via:
                toca_via = True
                toca_ep = False
                toca_vecino = f_n >= CONTACTO_MIN_FRACCION
                cat = "Frontal"
                motivo_lado = "contacto via {:.0%}".format(f_v)
            elif bordea_ep:
                toca_via = False
                toca_ep = True
                toca_vecino = f_n >= CONTACTO_MIN_FRACCION
                cat = "EspacioPublico"
                motivo_lado = "contacto EP {:.0%}".format(f_e)
            elif lado_lateral_por_vertices(p1, p2, vecinos_list):
                # 4a) Medianeria por VERTICES COINCIDENTES con vecinos (< 0.10 m):
                #     SOLO cuando el lado NO bordea via/EP
                toca_via = False
                toca_ep = False
                toca_vecino = True
                cat = "Lateral"
                motivo_lado = "vertices coincidentes con vecino"
                f_v = 0.0
                f_e = 0.0
                f_n = 1.0
            else:
                # 4b) Clasificacion por contacto minimo
                toca_via = f_v >= CONTACTO_MIN_FRACCION
                toca_ep = f_e >= CONTACTO_MIN_FRACCION
                toca_vecino = f_n >= CONTACTO_MIN_FRACCION
                if toca_vecino:
                    cat = "Lateral"
                    motivo_lado = "contacto vecino {:.0%}".format(f_n)
                else:
                    cat = "Lateral"  # provisional; la regla posterior puede reclasificar
                    motivo_lado = "sin contacto minimo"""

MARKER_NEW = "bordea_via = f_v >= CONTACTO_MIN_FRACCION"

ts = datetime.now().strftime("%Y-%m-%d-%H%M")
shutil.copy2(GHX, GHX + ".bak-" + ts)
print("backup:", GHX + ".bak-" + ts)

tree = ET.parse(GHX)
root = tree.getroot()

hit = 0
skip = 0
for el in root.iter():
    txt = el.text
    if not txt:
        continue
    if MARKER_NEW in txt:
        skip += 1
        continue
    if OLD in txt:
        el.text = txt.replace(OLD, NEW)
        hit += 1

if hit == 0:
    if skip:
        print("ya parchado (idempotente, sin cambios): %d item(s)" % skip)
        sys.exit(0)
    print("ERROR: no se encontro el bloque 4a/4b del LADOS en el .ghx")
    sys.exit(1)

tree.write(GHX, xml_declaration=True, encoding="utf-8")
print("escrito:", GHX, "| items parchados:", hit, "| ya parchados:", skip)

# --- validacion por re-lectura ---
t2 = ET.parse(GHX)
n_new = 0
n_old = 0
for el in t2.getroot().iter():
    if el.text:
        if MARKER_NEW in el.text:
            n_new += 1
        if "#     la medianeria gana aunque haya una via cerca sin contacto" in el.text:
            n_old += 1
print("VALIDACION: bloques nuevos=%d | bloques viejos restantes=%d" % (n_new, n_old))
