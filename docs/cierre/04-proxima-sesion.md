# Próxima sesión - puntos para continuar (2026-08-23)

Handoff para retomar en una nueva sesión. Estado consolidado tras la sesión de
cierre (rediseño orquestador Etapa 2 + regla de esquina + puente frente_override).

## Estado vigente (versiones)
- F0_LOAD_PROYECTO **v01.4** (emite `frente_override_json`), F0_STORIES v01.
- F1 NORMATIVA **v08.2**, LADOS **v06** (+esquina), PATIO **v02.1**,
  canvas **F1_Contexto_Base-Editado_v02** (sin cablear `frente_override_json`).
- F2 motores v03 (`modalidad_dueno_lote`).
- Suite: **267 passed**.

## Terminado en esta sesión (2026-08-23)
- Regla de lote de esquina en F1 (sin posterior + patio 3×3).
- Puente `frente_override` orquestador→canvas (scripts; falta cableado .ghx).
- Orquestador: mensaje de éxito en normativa, sin casillas duplicadas, financiero
  con fallback + valor del lote, `modalidad_dueno_lote` consolidada.

## Pendiente (orden sugerido)
1. **Cablear `frente_override_json`** en el canvas: conectar la salida
   `frente_override_json` de F0_LOAD_PROYECTO a la entrada `frente_override_json`
   de F1_ETAPA2_NORMATIVA_v08 (Type hint = String, Item Access). Reiniciar equipo
   y abrir programas en orden (ver reglas de entorno).
2. **Re-ejecutar canvas F1→F2** para regenerar `AAA0240ZXJH-gfa-gh.json`.
3. Validar anomalía de área de vecinos AAA0240ZXJH (Norte1 vs Norte2).
4. F2: `recursos_disponibles`, `saldo`, `financiacion_saldo[]`, acabados, multi-escenario.
5. Zonas de mercado + actualización periódica.
6. Cleanup git (`gh-definition-explorer`, `git rm --cached` derivados).
7. F3 → Zonas (no Morphs) para Ladybug.

## Para recordar (reglas de entorno)
- GHPython = IronPython 2.7 (sin f-strings/pathlib/type hints); acceso a entradas
  SIEMPRE `globals().get()`.
- Derivados (resultados F2/F3, `gfa-gh.json`, `pot-cache/*`) no se commitean.
- Matching orquestador↔canvas por **cardinal** (normal saliente), no por índice.
- El override del operador manda sobre la geometría (incluida la regla de esquina).
- Para operar el canvas: cerrar AutoClaw → reiniciar equipo → abrir en orden
  ArchiCAD/Grasshopper → reabrir AutoClaw para verificación (conexión frágil).

## Notas del vault (esta sesión)
- `10-arquitectura/2026-08-23-cierre-sesion.md`
- `10-arquitectura/2026-08-23-regla-lote-esquina.md`
