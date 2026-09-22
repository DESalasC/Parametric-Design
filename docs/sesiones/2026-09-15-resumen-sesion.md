---
type: project
fecha: 2026-09-15
responsable: Work
tema: ejecucion-pendientes-bloques-a-b-c-d-fases-0-4
---

# Resumen de sesión 2026-09-15 — Ejecución de pendientes (Bloques A–D, Fases 0–4)

> Cierre del gap documental de 2026-09-14 y 2026-09-15. Detalle en el vault:
> `10-arquitectura/2026-09-15-resumen-sesion-pendientes-fases.md`,
> diarios `60-diario/2026-09-14.md` y `2026-09-15.md`, lección
> `50-lecciones/2026-09-15-leccion-contexto50-ruta-primaria.md`.

## Objetivo

Retomar el estado del proyecto, consolidar pendientes y **ejecutar** el plan de
bloques A/B/C/D y fases 0–4 con las decisiones del operador:

- **Bloque A**: ya comprobado y funcionando. Lo único: **deshabilitar la
  creación de objetos en Rhino** (bake/export), conservando los breps y las
  alturas obtenidas de FETCH.
- **Bloque B**: B1 hecho; **falta B2**. B3: **contexto50 = ruta principal**;
  **ruta manual = opcional/fallback**. B4: los volúmenes NO importan para F2,
  pero **sí** para análisis sísmico NSR-10, asoleación y ambiental.
- **Bloque C**: C1–C3 funcionando; C4 pendiente de soporte técnico; C5 diferido;
  C6: evaluar qué plugins/MCP conviene instalar (lección Hostinger).
- **Bloque D**: ejecución completa (D1/D2/D3).
- **Plan**: Fase 0 sin riesgos (cerrando ollama y fcc-server al final); Fase 1
  prácticamente ejecutada al resolver pendientes; Fases 2, 3 y 4 ejecutar.

## Fase 0 — Sanidad y respaldo (✅ ejecutada)

- `backup_projects.ps1 -Real`: git commit local + espejo robocopy.
  Log `D:\Work\Scripts\AgentKit\04-backup\logs\backup-2026-09-15.log`
  (PROJECTS + AI + vault; exit 0). Commit del proyecto: `backup diario 2026-09-15`.
- **Congelado del canvas**: copia fechada de `.ghx` y `.gh` en
  `gh-definitions/_archive/congelado-2026-09-15/`.
- Al final de la prueba: se detiene `ollama` y `fcc-server` (ver más abajo).

## Bloque A — Fase 1 en vivo (✅ resuelto)

- **A1**: verificado por el operador (canvas `F1_Contexto_Base-Editado_v03`).
- **A3 / creación de objetos en Rhino**: el componente `F1_CONTEXTO50_BUILD_v01a`
  tiene inputs `bake` (index 2) y `exportar` (index 3), **ambos alimentados por
  el mismo Boolean Toggle** (GUID `3f45df55-582b-48e8-98b1-992b6a0321d8`,
  Object 152). El parche idempotente `scripts/utilities/patch-ghx-bake-exportar-off.py`
  lo dejó en `false`; `.ghx` parchado y `.gh` regenerado con GH_IO
  (`scripts/utilities/ghx-to-gh.ps1`). Resultado: el componente entrega
  `volumenes`/`huellas` **sin escribir** en el documento Rhino.
- **A2**: la salida `volumenes` sigue disponible para el Live Connection
  (Morphs → capa `70-20-30_Volumetrias_vecinas`).

## Bloque B — Integración contexto50

- **B1 (✅ hecho)**: cadena `FETCH → JSON → F1_ETAPA3_CONTEXTO50_v01` verificada.
- **B2 (✅ hecho)**: `src/fase-1-contexto/tests/test_contexto50_helpers.py`
  (helpers `unwrap`, `parse_bool`, `to_float`, `leer_json`, `normalizar_vertices`,
  `extraer_anillos`, `altura_de`, `_es_horario`, `_area_compacidad`,
  `_punto_en_poligono`, `construir_huella`). Suite completa: **25/25 en verde**
  (14 helpers + 11 integración).
- **B3 (✅ decisión documentada)**: en `CLAUDE.md` →
  - Ruta **primaria**: `contexto50` (extrae construcciones en radio 50 m;
    `CHIP-contexto50.json` → huellas + volúmenes).
  - Ruta **manual** (Morph en ArchiCAD): **opcional/fallback** cuando no exista
    información adecuada para resolverlo por contexto50.
- **B4 (✅ decisión documentada)**: los volúmenes de contexto50 **no** son insumo
  de **F2**; **sí** son insumo de **análisis sísmico NSR-10**, **asoleación** y
  **análisis ambiental (F4)**.

## Bloque C — Infra OpenClaw/agentes

- **C1–C3 (✅)**: reinicio de AutoClaw + regeneración de `openclaw.json` con los 6
  roles `dparam-*`, idioma español de la app y réplica en perfil Work: funcionando.
- **C4 (⏸ bloqueado)**: puerto 19723 — pendiente de respuesta de soporte técnico.
- **C5 (⏸ diferido)**: verificación en vivo de subagentes `fcc-claude`
  (proxy `fcc-server` 8082). Se retoma más tarde.
- **C6 (✅ evaluado)**: ver `10-arquitectura/2026-09-15-c6-plugins-mcp-evaluacion.md` (vault).

## Bloque D — Higiene documental / drift (✅ ejecutado)

- **D1**: documentados 2026-09-14 (solo lección) y 2026-09-15 (madrugada
  `fcc-claude` + esta sesión): diarios, resumen, memoria y mapa de conocimiento.
- **D2**: drift del `.ghx` consolidado: `.v03.1.gh` (sesión fcc-claude) y backups
  redundantes archivados en `gh-definitions/_archive/`. Se conserva la red de
  seguridad (`*.bak-2026-09-13-1527`, `*.bak-2026-09-15-0923` pre-parche).
- **D3**: commit de respaldo del estado actual (proyecto + vault) y backup.

## Cierre de Fase 0 — servicios

- `fcc-server` (8082) ya estaba caído; se confirma sin listener.
- `ollama` (11434, tarea `OllamaServe`): se detiene al cierre de la prueba.

## Artefactos de la sesión

| Artefacto | Ruta |
|---|---|
| Parche toggle bake/exportar | `scripts/utilities/patch-ghx-bake-exportar-off.py` |
| Tests de helpers | `src/fase-1-contexto/tests/test_contexto50_helpers.py` |
| Congelado del canvas | `gh-definitions/_archive/congelado-2026-09-15/` |
| Evaluación C6 | `10-arquitectura/2026-09-15-c6-plugins-mcp-evaluacion.md` (vault) |

## Pendientes

1. **A2 en vivo**: validar llegada de Morphs a ArchiCAD (capa z=0).
2. **C4**: soporte técnico del puerto 19723.
3. **C5**: relanzar `fcc-server` + verificar `fcc-claude` cuando se retome.
4. **C6**: decidir instalación de plugins/MCP según la evaluación.
5. **Fases 2, 3 y 4**: ejecutar conforme a los pendientes establecidos.
