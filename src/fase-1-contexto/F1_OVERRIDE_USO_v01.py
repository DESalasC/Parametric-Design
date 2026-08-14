#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
F1_OVERRIDE_USO_v01.py — OVERRIDE de USO (USO-MULTIPLE) para Fase 1
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Permite al USUARIO (solo en desarrollo, dentro de Grasshopper) declarar un uso
  diferente al permitido por la reglamentacion — incluido USO-MULTIPLE — para
  validar hipotesis de construccion y prefactibilidad en las fases siguientes
  (F2 financiero, F3 masa, F4 ambiental, F5 BIM).

  Es un OVERRIDE DE DESARROLLO: NO forma parte de la interfase final del sistema.
  El analisis financiero (F2) es quien decide la recomendacion mas adecuada
  comparando el(los) escenario(s) del uso efectivo contra los de la norma.

  Regla de propagacion:
    - activar = False -> uso_efectivo = uso_normativo (el POT manda).
    - activar = True  -> uso_efectivo = uso_seleccionado.
      La salida flag_pipeline inyecta el token en el JSON de contexto de Fase 1
      (campo "override_uso") para que F2/F3/F4/F5 lo consuman.

ENTRADAS:
  activar (Boolean)          — True = aplicar override de usuario.
  uso_seleccionado (String)  — Uso declarado: "Residencial" | "Comercial" |
                               "Oficinas" | "Mixto" | "Institucional".
                               (default: "Mixto")
  uso_normativo (String)     — Uso permitido por norma (opcional; si no se
                               conecta, default "Residencial").
  justificacion (String)     — Nota opcional del usuario (se propaga al JSON).

SALIDAS:
  uso_efectivo (String)      — Uso que se propaga a las fases siguientes.
  override_aplicado (Bool)   — True si uso_efectivo != uso_normativo.
  uso_normativo_ref (String) — Uso normativo de referencia (echo de entrada).
  flag_pipeline (String)     — Token JSON: "USO_NORMA:<uso>" o
                               "USO_OVERRIDE:<uso>;<justificacion>".
  escenarios_sugeridos (String) — Mapeo a escenarios F2 (A/B/C = usos puros,
                               D_MIXTO = Mixto), separados por "|".
  nota (String)              — Diagnostico (tambien advierte si el uso no esta
                               en la lista permitida).

VERSIONES:
  v01 — Creacion (2026-08-14). Override de desarrollo; USO-MULTIPLE para
        validacion de hipotesis de construccion y prefactibilidad.

  INTEGRACION EN CANVAS (F1_Contexto_Base-Editado_v00):
    1. Colocar este componente aguas abajo de F1_NORMATIVA_APLICAR_v24.
    2. Conectar "uso_normativo" a la salida de uso del componente de norma.
    3. Conectar "activar" a un Panel Booleano (False por defecto).
    4. Conectar "uso_seleccionado" a un Panel/Lista (miembros: Residencial,
       Comercial, Oficinas, Mixto, Institucional).
    5. La salida flag_pipeline se fusiona al JSON de salida de Fase 1
       (campo "override_uso" -> {"activo": bool, "uso": str, "nota": str}).
================================================================================
"""

USOS_PERMITIDOS = ["Residencial", "Comercial", "Oficinas", "Mixto", "Institucional"]

# Mapeo uso -> escenarios F2 (los motores F2_Modelo_Financiero / F2_Modelo_Renta
# definen los escenarios por caso; aqui se sugiere la familia a evaluar).
MAPEO_ESCENARIOS = {
    "Residencial": "A_VIS|B_ESTANDAR|C_LUJO",
    "Comercial": "E_COMERCIAL",
    "Oficinas": "E_OFICINAS",
    "Mixto": "D_MIXTO",
    "Institucional": "E_INSTITUCIONAL",
}


def main():
    # --- Normalizar entradas ------------------------------------------------
    activo = bool(activar) if activar is not None else False
    uso_sel = str(uso_seleccionado or "").strip() or "Mixto"
    uso_norm = str(uso_normativo or "").strip() or "Residencial"
    just = str(justificacion or "").strip()

    # --- Validar uso seleccionado ------------------------------------------
    if uso_sel not in USOS_PERMITIDOS:
        nota = ("USO no valido '%s'. Permitidos: %s. Se propaga uso normativo %s."
                % (uso_sel, ", ".join(USOS_PERMITIDOS), uso_norm))
        uso_efectivo = uso_norm
        override = False
        flag = "USO_NORMA:%s" % uso_norm
        esc = MAPEO_ESCENARIOS.get(uso_norm, "A_VIS|B_ESTANDAR|C_LUJO")
        return uso_efectivo, override, uso_norm, flag, esc, nota

    if activo:
        uso_efectivo = uso_sel
        override = (uso_sel != uso_norm)
        flag = "USO_OVERRIDE:%s;%s" % (uso_sel, just)
        if override:
            nota = ("OVERRIDE DE USO ACTIVO (desarrollo): uso efectivo = %s "
                    "(norma: %s). Fuera de reglamentacion; el analisis financiero "
                    "F2 evaluara la recomendacion." % (uso_sel, uso_norm))
        else:
            nota = ("Override activo pero el uso seleccionado coincide con la "
                    "norma (%s)." % uso_sel)
    else:
        uso_efectivo = uso_norm
        override = False
        flag = "USO_NORMA:%s" % uso_norm
        nota = "Override desactivado: se propaga el uso normativo %s." % uso_norm

    esc = MAPEO_ESCENARIOS.get(uso_efectivo, "A_VIS|B_ESTANDAR|C_LUJO")
    return uso_efectivo, override, uso_norm, flag, esc, nota


uso_efectivo, override_aplicado, uso_normativo_ref, flag_pipeline, escenarios_sugeridos, nota = main()
