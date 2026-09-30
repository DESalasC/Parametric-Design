# Posición inicial del Arquitecto (antes de leer al consejo)

- **Fecha:** 2026-09-29
- **Tema:** corrección de raíz de (A) codificación JSON ↔ GHPython; (B) visibilidad/utilidad 3D de perímetros de vecinos y envolvente.
- **Esquema:** skill `council` (marketplace ECC; referido por el operador como "claude-council"). Cuatro voces: Arquitecto (en sesión) + Escéptico + Pragmático + Crítico (subagentes independientes).

## Posición

- **Vía principal:** **canvas v12 construido incrementalmente desde v11** — preservar lo ya validado y añadir las ramas nuevas (3D + lecturas robustas). **No** reformulación total desde cero; **no** parche mínimo dentro del v11 actual.
- **Para (A):** blindaje en **dos capas** —
  1. *Escritores*: salida segura por defecto (ASCII-safe; UTF-8 explícito donde aplique) en todo JSON que cruce herramientas del ecosistema.
  2. *Lectores GHPython*: decodificación sobre **bytes** con cascada `utf-8-sig (estricto) → cp1252 → latin-1` + validación JSON + log del formato detectado.
  - Complementos: utilidad de verificación/reparación de cachés; tests con fixtures cp1252 ("Consolidación", ó en índice 11).
- **Para (B):** en v12: salidas de bandas drapeadas de ETAPA1 v05 → nodos **Morph Solid** (capas correctas por categoría); envolvente: extensión de NORMATIVA (v08.1) con `envelope_banda_3d` drapeada al MDT (+ opción de prisma/extrusión); dejar de huérfana la `topo_mesh` cableándola al nodo **Mesh** de la Live Connection; las cadenas 2D actuales quedan intactas (las necesita la clasificación manual en planta).

## Tres razones

1. **v11 está a medio validar** (validación viva del runbook aún pendiente): no conviene meter cirugía mayor en el mismo archivo que sirve de referencia/fallback.
2. **El material para v12 ya existe y está probado offline** (ETAPA1 v05 bandas 6/6; z_base v01d; NORMATIVA v08 re-encajada): la ruta incremental convierte trabajo hecho en valor y minimiza incógnitas.
3. Una reformulación total desde cero **reintroduce el riesgo de perder reglas duras acumuladas** (ADR-022, empates por tramo, antejardines, z_base, contratos de export) sin ganancia funcional demostrable.

## Riesgo principal de mi ruta

Coexistencia temporal de dos canvases (v11 fallback + v12 en obra) → confusión de versiones/parches. Mitigación: nomenclatura estricta, un solo runbook, criterios de aceptación por fase y congelar v11 como fallback declarado (sin cambios salvo bloqueo).

## Qué espero del consejo

- ¿La ruta incremental es suficiente, o la reformulación total tiene argumentos fuertes?
- ¿Dónde debe vivir el blindaje de codificación (¿solo lectores? ¿también escritores? ¿reparación de cachés? ¿fixtures de test?).
- ¿Qué riesgos/bordes no estoy viendo (Morphs pesados en LC, puerto 19723, validación viva, numeración volátil)?
