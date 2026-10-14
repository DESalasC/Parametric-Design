# Sesión 2026-10-13 — FIX Z-BASE (coordenadas locales) + PATIO v03.4 + Superposición de volúmenes

## 1. Situación inicial (reportes del operador)

**Reporte 1 (mediodía):** En ArchiCAD y preview Rhino se mezclan «dos volúmenes masivos» (fase previa) con «cuatro volúmenes separados» (ocupación actual) → retroceso visible.
- Pendientes asociados: **separaciones laterales** perpendiculares a la vía (no coincidían con bordes del lote) y **espacio posterior** contra el borde.
- Petición: revisión con registro de imagen, precisión del ítem «Resta de patio geométrica» en estado de avance, corrección del script.

**Reporte 2 (tarde, preview):** «Solo el primer nivel de los volúmenes de una crujía en su nivel» → pisos 2..n desplazados/vacíos.

**Reporte 3 (noche, imagen adjunta):** Diferencia de **13.75 m** entre la base del primer nivel de zona y el vecino del lado sur.

## 2. Verificación en vivo (Test 07.pln, solo lectura)

| Elemento | Estado | Esperado |
|----------|--------|----------|
| Stories | **3** (0/3/6) | 8 (GF..L07) |
| Zonas BEP v08.1 | **16** (B1–B3: 5 pisos; **B4 solo P1**) | 20 (la corrida declaró 20) |
| Morphs contexto | 71 | — |
| Mesh terreno | 1 | — |
| Canvas v13.5 #198 | Una revisión atrás (fix (d) pendiente) | Actualizado |
| Canvas v13.5 #78 PATIO | v03.3, slider n=0 (AUTO → 3 patios esquina) | v03.4 |

## 3. Problemas identificados y causas raíz

### P1: Superposición de volúmenes (fases 2 vs 4)
- **Causa:** ArchiCAD quedó en estado **parcial** de corrida anterior (16 zonas donde se declararon 20; Bloque 4 sin P2–P5; plataformas P1 desalineadas). La LC no borra huérfanos; limpieza es parte del procedimiento.
- **Resolución:** Censo en vivo (`F0_CENSO_ELEMENTOS_v01.py`) → borrar zonas viejas → re-empujar completo.

### P2: Regla de patio/separaciones ambigua
- **Causa:** El estado de avance decía «Resta de patio geométrica: resuelta» pero no distinguía 1 vs ≥2 volúmenes.
- **Regla confirmada (operador):**
  - **1 volumen** → patio normativo Anexo 5 §1.12.b (H/3, ≥9 m², lado ≥3 ml).
  - **≥2 volúmenes** → **no hay patios independientes**; rigen **separaciones entre volúmenes** (computan en IO).
- **Implementado:** `F1_ETAPA2_PATIO_v03.py` → **v03.4** (src; re-embebido pendiente).

### P3: Bug de marcos en escalonamiento lateral (`F3_DISTRIBUCION v03.8`)
- **Causa raíz:** El recorte por piso mezclaba marco **LOCAL** (polígono lote) con Y de la huella en marco **CANVAS** ⇒ pisos 2..n desplazados/vacíos; solo piso base correcto.
- **Fix:** **v03.9** — recorta con polígono de la franja en marco local (`cs[_k]`) + banda Y local; respaldo con aviso.
- **Test regresión:** marco rotado 30° → **22/22**; suite **367 ✅ / 7 ✗ stale**.

### P4: SyntaxError en `F3_VOLUM_GENERADOR_v08.py` embebido (canvas #199)
- **Error:** `SyntaxError: unexpected token '<newline>'` línea 2060.
- **Causa raíz:** Fuente con CRLF (`\r\n`); al escribir XML con `ElementTree`, normaliza a LF (`\n`), pero la continuación explícita `if ... \` seguida de línea en blanco y `else` rompía la sintaxis (la continuación requiere la *siguiente línea física*).
- **Solución:** Normalizar saltos a LF **antes** de escribir XML (`.replace('\r\n', '\n').replace('\r', '\n')`).
- **Validación:** 3 componentes compilan (PATIO v03.4 #78, DISTRIBUCION v03.9 #200, VOLUM v08.1 #199). Tests **38/38**.

### P5: Desplazamiento Z (13.75 m) — **Problema crítico**
- **Síntoma:** `desplazamiento_z` de `F1_CONTEXTO50_BUILD` = 14.52 (cota SE corner MDT), no el mínimo Z del terreno (~0.03).
- **Resultado:** Volúmenes bajaban a Z ≈ -14.5; terreno/vecinos quedaban en Z absoluto (14–16) → terreno **por encima** de volúmenes; diferencia vertical con vecinos.
- **Causa raíz:** Tres componentes usaban orígenes Z inconsistentes; prioridad `dz` errónea (promedio vecinos → ancla SE → terreno min), y `F3_VOLUM_GENERADOR` restaba `z_origin` de entradas que ya debían ser locales.

## 4. Decisiones tomadas y resolución (FIX Z-BASE)

**Objetivo:** Sistema de coordenadas local coherente con **SE corner = (0,0,0)** y Z_base = mínimo Z válido del terreno del lote.

| Componente | Versión | Cambio clave |
|------------|---------|--------------|
| `F1_CONTEXTO50_BUILD_v01.3.py` | v01.3 | `compute_dz_from_stage1_context()`: prioridad = **min_z válido malla** (punto más bajo lote) → promedio vecinos N/S → ancla SE → 0.0. `desplazamiento_z` = Z_base (~0.03). |
| `F1_ETAPA1_CONTEXTO_v02.3.py` | v02.3 | **Toda geometría** (lote, vecinos, vías, EP, topografía) en **LOCAL Z** (Z_abs - Z_base). SE = (0,0,0). Terreno empieza en ~0. |
| `F3_VOLUM_GENERADOR_v08.2.py` | v08.2 | Entradas (`altura_z`, `cota_arranque_m`) ya en **LOCAL Z**. `z_origin` param por compat (default 0); **NO restar** si entradas locales. `cota_arranque_local_m` = `cota_arranque_m`. |

**Archivos modificados (src):**
- `src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01.2.py` (→ v01.3)
- `src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v02.py` (→ v02.3)
- `src/fase-1-contexto/F1_ETAPA2_PATIO_v03.py` (→ v03.4)
- `src/fase-3-masa/F3_DISTRIBUCION_v03.py` (→ v03.9)
- `src/fase-3-masa/F3_VOLUM_GENERADOR_v08.py` (→ v08.2)

**Re-embebidos en `F1_CONTEXTO_v13.5.ghx` (4 componentes):**
| InstanceGuid | Componente | NickName |
|--------------|------------|----------|
| `ba3eb3a5...` | #47 | F1_CONTEXTO50_BUILD_v01.3 |
| `d3bed17b...` | #78 | F1_ETAPA2_PATIO_v03.4 |
| `0b462363...` | #198 | F3_VOLUM_GENERADOR_v08.2 |
| `2f5b4ab4...` | #200 | F3_DISTRIBUCION_v03.9 |

**Backup GHX:** `F1_CONTEXTO_v13.5.ghx.bak-20261013-212045`

**Tests:** **38/38** (grupo F3 distribución, patio bifurcación, story sync). Suite: 367 ✅ / 7 ✗ (stale).

## 5. Lecciones aprendidas

1. **Regla patio/separaciones (confirmada):** 1 vol = patio normativo (H/3, ≥9 m², ≥3 ml); ≥2 vol = separaciones (computan en IO). Implementado en v03.4.
2. **ArchiCAD estados parciales:** Antes de diagnosticar "superposiciones", correr censo en vivo y comparar contra mensaje de corrida; limpiar y re-empujar completo.
3. **Tests con stub — inyección COMPLETA e idempotente:** El stub compartido `tests/stub_rhino_min.py` debe **completar** atributos faltantes (no early-return) para no romper otros módulos.
4. **Herramientas nuevas del día:**
   - `src/interfases-archicad/F0_CENSO_ELEMENTOS_v01.py` (censo solo-lectura por tipo + `--sel` + `--bbox`).
   - `scripts/utilities/dump-red-canvas.py` (red completa de conexiones del canvas).
   - `scripts/utilities/_tmp-zonas-propiedades.py` (propiedades de zonas vía `GetPropertyIds` → `GetPropertyValuesOfElements`).
5. **SyntaxError por CRLF en XML:** Normalizar a LF **antes** de `ElementTree.write()` para preservar continuaciones explícitas Python (`\` + `else`).
6. **Nueva regla de trabajo (pedido usuario 18:51):** Si hay ambigüedad, **preguntar hasta aclarar**; si no aclaran, **exponer supuestos y razones** antes de proceder. Registrada en **MEMORY.md** y obligatoria para sesiones futuras.
7. **Z-BASE — Origen coherente:** Z_base = **mínimo Z válido del terreno del lote** (filtrando |z| < 0.001 = placeholders), NO ancla SE (14.52) ni promedio vecinos (z=0). SE corner = (0,0,0) en XY; Z_local = Z_abs - Z_base. Todas las cotas de arranque y niveles resultan **positivas** (salvo sótanos).

## 6. Puntos pendientes (para próxima sesión)

### Inmediatos (requieren recarga canvas + validación viva)
1. [ ] **Recargar canvas** en Grasshopper (cerrar/reabrir `F1_CONTEXTO_v13.5.gh`).
2. [ ] **Corrida limpia**: borrar 16 zonas en AC → correr → **censo 20/20** (+ mensaje «4 bloques \| 20 zonas»).
3. [ ] **Crear 8 stories** en AC (hoja operador: `niveles_operador.txt`) + `F3_StorySync_v02 --check` (0 faltantes).
4. [ ] **Validar separaciones laterales** (extremos a bordes del lote) y **empate posterior**; revisar aviso «no alcanza borde derecho» / margen 145 m².
5. [ ] **Zonas finas** (Category/Layer/Subfloor/ID) y áreas netas.
6. [ ] **Limpieza tests stale** (7 restantes).

### Heredados (sin resolver)
1. **Validación viva caso B** + prevalidación operador + geometría F3 en vivo; confirmar `F1→F3` morphs/capas/Stories → ArchiCAD.
2. **Infra puerto 19723**: tarea programada `Update-LC-PortProxy-19723.ps1` (logon/arranque host+VM); réplica 8082/11434; verificación `iphlpsvc` tras reinicios; re-envío reporte a soporte AutoClaw.
3. **Estación**: ventana mantenimiento (`mantenimiento-equipo.ps1 -Fase Reparacion` + mdsched); discos E/F/G; reporte WebView2 a McNeel.
4. **F4/F5**: conectar salidas F3 → `F4_LADYBUG_ANALISIS_v02`; iniciar `F5_MAPEO_TAPIR_v01` (puerto resuelto).
5. **Gates**: PC-2 (GFA aprobado, validación viva); PC-3/PC-4 condicionados.
6. **Arrastres**: dataset mixto nuevo (B); cota por edificio contexto50 (`z_base_m`); investigar MiMo-Flash-RL; canvas v14 (solo con cambios mayores).

## 7. Archivos de evidencia y documentación

- **Planes y evidencias:** `docs/planes/2026-10-13-superposicion-volumenes-separaciones/`
  - D1-DIAGNOSTICO-2026-10-13.md
  - D2-PRECISION-PATIO-Y-SEPARACIONES.md
  - D3-PLAN-ACCION-2026-10-13.md
  - D4-INSTRUCCIONES-STORIES-OPERADOR.md
  - evidencias/ (censo CSV, capturas, fix-v039-marcos.txt)
- **Lección:** `50-lecciones/2026-10-13-leccion-patio-multivolumen-y-estado-ac.md`
- **Diario:** `60-diario/2026-10-13.md`
- **Memoria proyecto:** `memory/sesion-2026-10-13-superposicion-patio-v034.md`
- **Estado de avance actualizado:** `10-arquitectura/estado-avance-disenoparametrico.md` (corte 2026-10-13)

## 8. Commits de respaldo

- **Proyecto (DiseñoParametrico):** cambios en src/, tests/, gh-definitions/, docs/planes/, memory/
- **Vault (obsidian-vault):** acta, diario, lección, estado-avance, mapa actualizado
- **MEMORY.md** (workspace): regla de trabajo + resumen Z-BASE

---

**Cierre:** Sesión 2026-10-13 completada. Próxima sesión: recarga canvas → validación viva completa → cierre PC-2.