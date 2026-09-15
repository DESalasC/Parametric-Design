---
fecha: 2026-09-07
tipo: plan
tema: disenoparametrico
estado: borrador
tags: [plan, disenoparametrico, quality-gates, gobernanza, pipeline]
---

> **Estado:** borrador pendiente de aprobación humana (PC-0). Documento hermano: `Plan_Maestro_DiseñoParametrico_2026-09-07.docx` (entregable Word). Según P12, la copia canónica vive en `docs\` del proyecto y el vault es espejo de navegación; en conflicto gana el canónico.

# Plan V2 — DiseñoParamétrico: configuración, capacidades, pipeline y puntos de control (integración de críticas)

**Fecha:** 2026-09-07 · **Rol:** sintetizador del plan final. **Insumos:** `subagent_05_plan_v1.md` (plan original v1), `subagent_06_critica_tecnica.md` (hallazgos H-01…H-16), `subagent_07_critica_trazabilidad.md` (hallazgos T-01…T-14). **Método:** cada hallazgo de ambas críticas se resuelve con un cambio explícito (traza completa en §5); lo sólido del v1 —no sobre-automatizar el modelado 3D, sanear antes de automatizar, gates en límites de cadena, F4/F5 al final— se conserva sin reescritura innecesaria. Este documento no ejecuta nada del pipeline; propone. ⚠️ = decisión humana.

---

## 0. Resumen de cambios v1→v2

- **A5 nuevo — bloqueante del puerto 19723 (H-01):** el conflicto AutoClaw↔ArchiCAD deja de ser "riesgo residual" de tres objetivos y pasa a objetivo dedicado con criterio medible (conexión Live Connection/Tapir real con el gateway activo) y ADR-011. Sin su cierre, la parte ArchiCAD de S3 no se agenda a ejecución.
- **La obra principal entra en la gobernanza (H-02):** objetivos formales **F2-EXT**, **F4-VAL** y **F5-MAPEO** con reparto agente/humano, entregables, PC y criterios de aceptación.
- **Orden corregido C3→C2 (H-03):** primero el root cause del frame de coordenadas; después el re-export/override, validado sobre un GFA creíble y con criterio por lado.
- **Instalado ≠ verificado (H-04):** P4 se reescribe; rhino.compute.exe, prueba punta a punta del puente MCP y compatibilidad Live Connection/Tapir con ArchiCAD 29 son pre-verificación obligatoria (paso 0) antes de B2/C4/C5.
- **Criterios medibles (H-06/H-07):** tolerancia relativa explícita (1e-6, no 0) y tabla completa de plugins en B2; umbrales numéricos de sanidad F1 (ancho de vía, Ocup, IO, IC, GFA) en PC-1.
- **Gates con ciclo de vida (H-08/H-16/T-02/T-05):** revisor por PC, actas con estados aprobado/rechazado/en-bloqueo + campo alcance, ruta de escape con dueño y re-entrada, prohibición de "cierre parcial", modo bootstrap S1, actas archivadas junto a los runs.
- **Presupuesto humano (H-09):** horas por objetivo, capacidad semanal supuesta (≈8 h) y ruta crítica explícita; las 14 decisiones de B1 se agrupan en una sesión por lotes.
- **Conciliación de los TRES planes (T-01):** matriz con estado y dueño para el plan 08-14, el orquestador 08-22 (Etapas 0–6) y este plan; integración 09-03 como restricciones.
- **Gobernanza documental completa (T-03/T-04/T-06/T-07/T-08/T-09/T-13/T-14):** tabla de ubicaciones con canónico/espejo/trigger, regla de propagación de versiones (P11), precedencia de copias (P12), manual único estable sin versión en el nombre, tabla única de vigentes, auditoría P6 de decisiones, manifest con versión de contrato y schemas versionados, regla 70-trabajos, numeración ADR cerrada (máx+1, hoy 011).
- **Menores incorporados (H-05/H-10/H-11/H-12/H-13/H-14/T-10/T-11/T-12):** dependencia jsonschema/pydantic con aprobación previa, check de paridad pre-gate, criterio separado terceros vs editable, grafo de dependencias intra-S1, hilos huérfanos 3/6 y mojibake de labels, árbol de decisión del job 07:30, criterio invariante de suite, PC-0 con evidencia mínima y verificación automatizada.

---

## 1. Principios y restricciones

### 1.1 Principios (P1–P12; actualizados respecto a v1)

- **P1 — Verdad documental antes que velocidad.** El canvas maestro real es `F1_Contexto_Base-Editado_v03.ghx` (09-01); nada se automatiza sobre estado en drift: primero fijar qué es vigente (tabla única, T-14), luego acelerar.
- **P2 — Pocos gates, en límites de cadena, con checks automáticos antes de la revisión humana.** El humano decide, no detecta. Cada gate tiene revisor, umbrales y ruta de escape (§4.2). **"Evidencia registrada" ≠ "gate aprobado"**: un acta con capturas de un intento fallido no aprueba nada.
- **P3 — El contrato de datos es el lenguaje único; los schemas se versionan.** `data/activo/` con 6 JSON canónicos, roles `fuente/operador/calculado`, orquestador como único productor. Un schema nunca se edita in situ: un cambio = versión nueva, para que los manifests históricos sigan resolviendo (T-08).
- **P4 — Instalado ≠ verificado.** AgentKit (11 módulos probados), rhino3dm 8.32.0 en el venv, puentes MCP instalados (Tapir, Hops, rhinogh-mcp-grasshopper, Rhino-MCP-Platform), Graphify 0.9.42, cron de OpenClaw en producción: **instalados**. Quedan **pendientes de verificación** y se verifican con criterio propio antes de usarse: (a) presencia y arranque REST de `rhino.compute.exe` (el informe de capacidades solo verificó `Rhino.exe 8.34`); (b) prueba punta a punta del puente MCP (leer/escribir 1 parámetro real); (c) compatibilidad Live Connection/Tapir con **ArchiCAD 29**. Nada depende de IA local hasta decisión humana (P6).
- **P5 — Lo 3D lo modela el humano en sesión GUI** (modelar en la sesión Rhino donde está el lote; perímetro = `envelope_curve`). El agente prepara, verifica headless y registra; el humano modela y aprueba.
- **P6 — Decisiones estructurales con registro proporcional.** Instalaciones y decisiones estructurales requieren aprobación humana explícita. Regla de registro (T-04): *si la decisión sobrevive a la sesión que la tomó, es ADR o contrato; si no, nota de decisión con ubicación declarada*. **Numeración ADR cerrada (T-13):** siguiente = máximo existente + 1 (**hoy 011**); los huecos 001/003/009 **no se reutilizan**.
- **P7 — Trazabilidad por corrida y origen puro.** Runs `YYYY-MM-DD-<proceso>-NNN`; manifest por corrida con hash del canvas, versiones de scripts, **versión del contrato de datos y hash de los schemas usados** (T-08), gate, y rutas de salida; histórico append-only y `meta.sync` al consumir MercadoViviendaBogota.
- **P8 — Compatibilidad, nomenclatura y runtime de tests declarado (H-08).** GHPython nuevo en IronPython 2.7 (sin f-strings/type hints); scripts `MAYUS_FASE_VERBO_vNN.py`; vigente a raíz, caduco a `_legacy`. **Los tests de lógica pura corren en CPython 3.12 con sintaxis 2.7-compatible y stubs de geometría** (patrón de la suite vigente de 273); pytest no corre bajo IronPython.
- **P9 — Documentación por temas, espejo proyecto↔vault;** avances en la documentación del proyecto (nunca en MEMORY.md); `mapa-conocimiento.md` enlaza toda nota nueva.
- **P10 — UTF-8 estricto, también retroactivo.** Toda herramienta nueva maneja UTF-8 y rutas con ñ; además se **sanean los labels ya corruptos** (mojibake) como tarea de A1/A2 (H-13).
- **P11 — Propagación de versiones (nuevo, T-06).** Toda subida de versión de un vigente (script o canvas) exige, como condición del gate correspondiente: (1) actualizar la **tabla única de vigentes**, (2) corte en estado-avance, (3) **grep de citas obsoletas** (automatizado en D2/D5), (4) contrato actualizado si cambia la interfaz.
- **P12 — Precedencia de copias (nuevo, T-07).** Canónico en docs del proyecto; vault como espejo de navegación; trigger de sincronización: **el mismo commit**. En conflicto, gana la copia canónica.

### 1.2 Restricciones duras (actualizadas)

| Restricción | Evidencia | Consecuencia en v2 |
|---|---|---|
| Puerto 19723 en conflicto (AutoClaw ↔ ArchiCAD) | R4; ticket externo sin fecha | Ya no es "riesgo residual": tiene objetivo **A5** con criterio medible; C4-ArchiCAD, C5, F5-MAPEO y PC-4 no se agendan a ejecución sin su cierre |
| rhino.compute.exe / puente MCP / AC29 sin verificar | inf. 02 solo verificó Rhino.exe 8.34 | Paso 0 obligatorio de B2; P4 degradado a "instalado, pendiente de verificación" |
| jsonschema y pydantic ausentes del venv | inf. 02 §3 | B3 exige aprobación previa ⚠️ (instalar = P6) o validador propio con tests negativos |
| IA local NO operativa | Ollama 0 modelos; binarios FCC ausentes | Ninguna línea depende de inferencia local; recuperación = decisión humana (B4, con ADR si se reinstala) |
| Modelado 3D requiere sesión GUI humana | Regla AGENTS.md | F3/F5 con etapas manuales obligatorias (C1–C4) |
| Sin pandoc; python-docx y pyshp fuera del venv | inf. 02 §7 | Entregables vía HTML→PDF (Edge) y Excel (openpyxl) |
| IronPython 2.7 como runtime de GHPython; pytest solo en CPython | R10 + inf. 02 | P8 ampliado: tests Zona en CPython con sintaxis 2.7-compatible y stubs |
| Backup dependiente del gateway; job 07:30 en error (HTTP 403) | inf. 02 §6–7 | Objetivo A4 con árbol de decisión por ramas (H-14) |
| Suite actual = 273 passed | Commit 09-02 | Criterio invariante: verde, sin fallos nuevos respecto a la corrida previa (T-11) |

---

## 2. Objetivos por eje

Formato v1: descripción · agente vs humano · entregables · PC · criterio de aceptación · riesgos · prioridad/horizonte · horas humanas (nuevo, H-09).

### Eje A — Configuración

#### A1. Saneamiento del repositorio y del entorno — `alta · S1`
- **Descripción.** Retirar del árbol activo los caducos (tabla §2.2 del diagnóstico); sacar los 457 MB de binarios ArchiCAD y propuestas de cliente de `src\fase-1-contexto\tests\`; aislar el corpus de `src\research\` de los testpaths; depurar artefactos de test en `gh-definitions\`; saneamiento de codificación (mojibake) en labels existentes (H-13). **Dos criterios separados (H-11):** (i) dependencias de terceros instaladas sin error; (ii) paquete editable: decidir ⚠️ entre (a) reparar la línea editable creando packaging (pyproject/setup) o (b) eliminarla y declarar cómo resuelve el proyecto sus imports (sys.path/orquestador).
- **Agente.** Inventario con `git mv` propuestos; corrige `requirements.txt` y `testpaths`; pytest antes/después; grep de rutas vivas; redacta la opción (a)/(b).
- **Humano.** Aprueba movimientos; confirma en Rhino que el canvas v03 no referencia archivos movidos; decide (a) o (b) ⚠️.
- **Entregables.** Commit de saneamiento; informe en `docs\sesiones\`; requirements funcional; decisión editable registrada (nota; ADR solo si es estructural).
- **PC.** PC-0 + suite verde.
- **Criterio de aceptación (invariante, T-11).** Suite completa en verde, **sin fallos ni skips nuevos respecto a la corrida previa al cambio**; cero caducos en árbol activo; `pip install` de dependencias de terceros sin error en venv fresco; corpus fuera de testpaths; labels sensibles legibles en UTF-8.
- **Riesgos.** Romper rutas (grep previo + git); mojibake (P10); la opción (a) puede exigir packaging no previsto → se registra como tarea propia, no bloqueante de S1.
- **Horas humano:** ≈2.

#### A2. Verdad documental: canvas v03 maestro, manual único estable, tabla única de vigentes — `alta · S1`
- **Descripción.** Eliminar drift (R1/R8/R9): declarar v03 maestro; **un único manual estable `MANUAL_DE_EJECUCION.md`, sin versión en el nombre**, en la raíz del proyecto, con encabezado "versión vigente: canvas vX + fecha + hash" enlazado al manifest de D3 — el versionado vive en git y en la tabla única, no en el nombre del archivo (T-03/H-15). **Retiro explícito** de `MANUAL_DE_EJECUCION.md` (08-23) y `MANUAL_DE_EJECUCION_v02.md` (08-24) a `_legacy\`, con grep verificable de que nada vivo los enlaza. **Tabla única de versiones vigentes** (T-14) como extensión del estado-avance: fuente autoritativa que manual/README/docs **referencian** en vez de repetir. Crónica 08-25→09-05 reconstruida con fuente por dato; corte 2026-09-07.
- **Agente.** Redacta; diff de citas v02→v03; retiro de manuales con verificación por comando; crea la sección "Vigentes" del estado-avance.
- **Humano.** Valida el contenido real del v03 (con C1); aprueba retiros.
- **Entregables.** Manual único; dos manuales en `_legacy\`; tabla única de vigentes; crónica; corte del estado-avance.
- **PC.** PC-0.
- **Criterio.** Un solo manual fuera de `_legacy` (verificable con un comando); ningún doc vivo cita v02 como maestro; la tabla única existe y es referenciada, no duplicada.
- **Riesgos.** Reconstrucción con suposiciones (cada afirmación con fuente git o "por confirmar en C1").
- **Horas humano:** ≈2.

#### A3. Contratos de datos coherentes y auditables — `alta · S2`
- **Descripción.** Conciliar `data\activo\`: CHIP activo de referencia (AZPA vs ZXJH) ⚠️ y política para esqueletos vacíos (R7); actualizar el contrato (v1.1) con las interfaces nuevas; **la adopción de `config\schemas\` como parte del contrato se registra con ADR** (T-04); schemas versionados (P3).
- **Agente.** Auditoría de los 6 JSON + overrides; propuesta de regla CHIP/esqueleto; actualiza contrato y doc 08-22 si cambia algo; tabla de vigencia de contratos conectada al manifest (D3).
- **Humano.** Decide CHIP activo ⚠️ y política de esqueletos; el registro va a ADR o nota de decisión (§4.4).
- **Entregables.** Contrato v1.1; ADR o nota del CHIP; tabla de vigencia; `data\activo\` coherente.
- **PC.** PC-1/PC-2.
- **Criterio.** CHIP único documentado o regla explícita; auditoría sin hallazgos; toda interfaz canónica con schema versionado referenciado en la tabla de vigencia.
- **Riesgos.** Consumidores leyendo esqueletos vacíos (R7); sobreespecificar (mitigado: versionar).
- **Dependencia (H-12).** Las corridas formales con CHIP (C2, F2-EXT) esperan esta decisión.
- **Horas humano:** ≈2.

#### A4. Continuidad operativa: backup y cron — `media · S1`
- **Descripción.** Reparar el job 07:30 (HTTP 403) mediante un **árbol de decisión con criterios por rama (H-14):** (1) diagnóstico → causa local (credenciales/config): fix + 2 corridas OK → cierre; (2) causa externa (proveedor): escalar con evidencia y fecha límite; sin respuesta en 2 semanas → (3) dar de baja o rediseñar el job y cerrar con decisión documentada. La tarea de Windows (si se aprueba ⚠️) se especifica: horario fuera de uso o VSS, flags de reintento, verificación post-copia (conteo/hash) y prueba con Rhino abierto. Cubrir huecos de backup (04-09, 25-08→01-09).
- **Agente.** Diagnóstico; backup manual verificado; registra la tarea asistida si se aprueba.
- **Humano.** Aprueba credenciales/fix y la tarea de Windows (P6).
- **Entregables.** Cron verde o baja documentada; huecos cubiertos; especificación de tarea.
- **PC.** PC-0 + verificación propia del backup (log robocopy + git).
- **Criterio.** La rama del árbol que aplique con su criterio cumplido; 2 corridas consecutivas OK (si la rama fue fix local).
- **Riesgos.** Causa externa (las ramas 2/3 evitan bloqueo indefinido de S1); archivos abiertos durante robocopy (VSS/horario).
- **Horas humano:** ≈2.

#### A5. Desbloqueo del puerto 19723 (AutoClaw ↔ ArchiCAD) — `alta · S1–S2` ⚠️ — **NUEVO (H-01)**
- **Descripción.** R4 es un bloqueador conocido y activo cuya contraparte es la plataforma residente que ejecuta a los agentes; el workaround "orden de apertura" es probablemente insuficiente. Objetivo dedicado: (1) diagnosticar qué proceso liga 19723 y en qué modo; (2) evaluar opciones: reconfigurar el puerto del gateway AutoClaw, el de la API JSON de ArchiCAD, o validar documentadamente el workaround; (3) registrar la decisión como **ADR-011**. Incluye verificar la compatibilidad del add-on Live Connection y de Tapir con **ArchiCAD 29** (H-04c).
- **Agente.** Diagnóstico (netstat, config del gateway — con aprobación previa para tocar config, backup del cambio y reversibilidad); dossier comparativo de opciones; prueba de conexión.
- **Humano.** Aprueba diagnosticar la config del gateway ⚠️; elige opción ⚠️; aprueba el ADR.
- **Entregables.** ADR-011; dossier; evidencia de conexión real.
- **PC.** Sub-check de PC-4 (prerequisito); evidencia en acta.
- **Criterio de aceptación.** **Una conexión Live Connection/Tapir real y exitosa con el gateway AutoClaw activo**, que incluya al menos una lectura y una escritura vía la API JSON de ArchiCAD en el puerto resultante.
- **Riesgos.** Ticket externo sin fecha: si ninguna opción funciona → decisión humana ⚠️ de replanificar S3 (diferir la parte ArchiCAD con horizonte o escalar el ticket); tocar config del gateway exige cambio reversible con backup.
- **Horas humano:** ≈3.

### Eje B — Nuevas capacidades para los agentes locales

#### B1. Aprobar e instalar las 14 skills-ready de AgentKit — `alta · S1` ⚠️
- **Descripción.** Dossier único por skill (función, dependencias reales contra el venv, riesgos, smoke test) con **tabla resumen para una sesión de decisión por lotes** (H-09). Es prerequisito que A1 haya saneado el venv (H-12): ningún smoke test contra un entorno en reparación.
- **Agente.** Dossier; detecta brechas (pyshp, python-docx); tras aprobación instala y corre smoke test por skill.
- **Humano.** Decide por lotes: aprobar/rechazar/aplazar; rechazadas con motivo.
- **Entregables.** Dossier; registro de decisiones (ubicación en §4.1); skills instaladas con smoke tests.
- **PC.** Smoke tests como **sub-checks del PC-0 con registro en el dossier/acta del skill** (T-10).
- **Criterio.** Cada skill instalada pasa su smoke test contra el venv saneado; no aprobadas con registro y fecha.
- **Riesgos.** Dependencias faltantes (instalar = nueva aprobación); solapamiento con skills de AutoClaw (el dossier lo señala).
- **Horas humano:** ≈1,5 (la sesión; los smoke tests los corre el agente).

#### B2. Motor headless de Grasshopper: pre-verificación + PoC Rhino.Compute + auditoría MCP — `alta · S2`
- **Paso 0 — pre-verificación (H-04), con criterio propio:** (a) presencia y versión de `rhino.compute.exe` + arranque REST mínimo; (b) **prueba punta a punta del puente MCP** (agente lee/escribe 1 parámetro de GH en sesión supervisada) como entregable; (c) compatibilidad Live Connection/Tapir con AC29 (cruce con A5). Solo con paso 0 en verde se ejecuta el PoC.
- **PoC.** Correr `F1_Contexto_Base-Editado_v03` vía Rhino.Compute con 2 CHIP y comparar contra salida GUI de referencia.
- **Agente.** Checklist del paso 0; PoC; tabla de compatibilidad; propuesta de ADR.
- **Humano.** Provee las corridas GUI de referencia; aprueba poner en marcha Rhino.Compute y el ADR.
- **Entregables.** Evidencia del paso 0; PoC con JSON verificado; **tabla plugin×modo(GUI/headless)×resultado COMPLETA sobre el inventario real de plugins del .ghx** (human-ui, Parachute, raven, etc.), con los no-headless marcados y plan alternativo (canvas "stripped" para compute); ADR.
- **PC.** PC-1 (misma salida que la GUI pasa los mismos checks).
- **Criterio (H-06).** Valores discretos (`pisos_finales`) **exactos**; valores continuos (`gfa_total_m2`, `io_real`, `ic_real`) con **tolerancia relativa explícita 1e-6**; `valido:true`; la tabla completa de plugins es parte del criterio, no un extra.
- **Riesgos.** Plugins no headless (la tabla los anticipa con plan alternativo); licencias/instancias; puerto 19723 si aplica (resuelto por A5).
- **Horas humano:** ≈3.

#### B3. JSON Schema + validador automático en las fronteras — `alta · S2`
- **Paso 0 (H-05).** Declarar y aprobar ⚠️ la dependencia `jsonschema` o `pydantic` (no constan en el venv; instalar paquetes = aprobación P6), con smoke test del validador contra 1 payload válido + 1 inválido. Alternativa aceptada: validador mínimo propio **con cobertura de tests negativos definida**.
- **Descripción.** Formalizar los contratos (A3) como JSON Schema versionados en `config\schemas\` — cuya adopción forma parte del contrato y va con ADR (T-04) — y un validador Python antes de cada gate. Cubre: `gfa-gh`, `programa-areas`, `f2_entrada`, `f2_resultado`, `f3_masa`, `mercado_zonal`, overrides y el acta estructurada de gates.
- **Agente.** Escribe los `.schema.json` versionados; crea `F0_VALIDAR_CONTRATOS_v01.py` (P8) integrado a `run_pipeline_v01.py` y `servidor.py`; mensajes accionables.
- **Humano.** Aprueba dependencia y schemas (son contratos).
- **Entregables.** Carpeta de schemas versionada; validador integrado; guía de uso.
- **PC.** Ejecutado en PC-1…PC-4.
- **Criterio.** 100 % de contratos canónicos con schema versionado; payload inválido de prueba rechazado con mensaje accionable; suite verde sin fallos nuevos.
- **Riesgos.** Triple implementación Python/IronPython/JS (R2) → check de paridad en D2 o ADR de riesgo aceptado (H-10); sobreespecificación (mitigada: versionado).
- **Horas humano:** ≈1.

#### B4. IA local: dossier de decisión (reinstalar vs dar de baja) — `media · S2–S3` ⚠️
- **Descripción.** Como v1. **Cambio v2 (T-04):** si (a) reinstala → **ADR obligatorio**; si (b) da de baja → nota de decisión con ubicación declarada.
- **Agente.** Dossier con costos y casos de uso reales; ejecuta lo aprobado (instala modelos con smoke test JSON-schema, o corrige MODELS.md/README).
- **Criterio.** (a) un modelo responde JSON válido en una tarea real de prueba; (b) ningún doc referencia modelos/binarios inexistentes.
- **Horas humano:** ≈1.

#### B5. Entregables automatizados con AgentKit ya probado — `media · S2`
- **Descripción.** Activar el ciclo: 02 f2-excel, 01 html-to-pdf (Edge headless), 07 ifc, 08 html-qa, 10 obsidian (vault_append). **Cambio v2 (T-09):** los reportes internos de pipeline son **evidencia de gate (runs)**, no entregables publicables; lo que vaya a cliente se rige por 70-trabajos (§4.5).
- **Criterio.** 1 ciclo F2 → Excel → PDF → vault sin intervención manual intermedia; ningún reporte interno publicable por error de ubicación.
- **PC.** PC-2 (el entregable es evidencia del gate).
- **Horas humano:** ≈1.

#### B6. Backlog declarado fuera del alcance — `baja · S3+`
- **Descripción.** No se compromete por falta de verificación: Revit/AutoCAD 2027 (pyRevit sin instalar), Twinmotion, Graphify profundo, Wallacei, agente-propositor con LLM (depende de B4). **Cambio v2 (H-13):** incorpora los hilos huérfanos con estado explícito — **hilo 3** (nicknames/cardinal_label en salida LADOS/NORMATIVA, insumo del check D2 de coherencia CHIP) y **hilo 6** (persistencia por CHIP "resto por verificar"); el mojibake de labels existentes se sana en A1/A2.
- **Criterio.** Ningún ítem sin estado (pendiente/absorbido/cerrado) se ejecuta sin pasar a objetivo formal con gate.
- **Horas humano:** ≈0,5.

### Eje C — Etapas manuales (humano) — **orden corregido: C1 → C3 → C2 → C4 → C5**

#### C1. Verificar el canvas v03 y declarar maestro — `alta · S1`
- **Descripción.** Confirmar qué contiene el v03 respecto a v02 (¿re-export de LADOS v06.3 y NORMATIVA v08.3? ¿outputs Zona 19–22?) y declararlo maestro — o re-exportar v04 (bloqueante de PC-1). Es prerequisito de B2: el PoC acredita el canvas que C1 valide (H-12).
- **Agente.** Checklist; compara componentes embebidos vs `.py` vigentes (ghx_inspect + rhino3dm).
- **Humano.** Recorre el checklist en su sesión Rhino; decide v03 maestro / re-exportar v04.
- **Entregables.** Checklist firmado; declaración en el manual único (A2).
- **PC.** PC-1 (cierre del drift R1).
- **Criterio.** Canvas maestro documentado = canvas real; componentes embebidos = versiones .py vigentes.
- **Horas humano:** ≈2.

#### C3. Root cause del frame de coordenadas (GFA) — `alta · S2 · ANTES de C2` (H-03)
- **Descripción.** Validar que vías/EP/vecinos usen el MISMO origen local del lote (síntoma: ancho de vía 41,7 m, Ocup 1,6 m²). Es la raíz de la credibilidad del GFA y por eso va antes del re-export/override. **Al cierre, fija los umbrales numéricos de sanidad F1 que PC-1 exige (H-07).**
- **Agente.** Análisis headless de coordenadas; propuesta de corrección con evidencia numérica.
- **Humano.** Inspección visual de frames en GH; decide y aplica el fix en sesión GUI.
- **Entregables.** Diagnóstico numérico; fix aplicado; corrida de referencia corregida; **umbrales versionados en el contrato de datos (A3)**.
- **PC.** PC-1.
- **Criterio.** Corrida F1 con métricas dentro de los umbrales (propuesta, a validar en C3): **ancho de vía ∈ [5, 30] m según clase de vía; Ocup ≤ área_lote × COS_norma; IO ≤ 1 + 0,01; IC ≤ 1 + 0,01; GFA dentro de banda edificabilidad × área**; documentado en el corte del estado-avance. Re-baseline de casos A/B/B_SALUD/C anunciado como esperado.
- **Riesgos.** Cambio de GFA históricos → re-baseline (esperado); umbrales iniciales mal calibrados (se versionan y ajustan con el gate).
- **Horas humano:** ≈3.

#### C2. Re-export de GHPython y override de setback por lado — `alta · S2 · tras C3`
- **Descripción.** El `.gh` embebe código (editar el `.py` no actualiza el componente); el override de setback por lado (v06.3) falta sincronizar al canvas, generar `lado_via_setback_override_json` desde el orquestador y probar con AAA0240ZXJH. **Cambio v2:** se ejecuta después del fix de C3, sobre el frame corregido — ya no valida un número destinado a cambiar.
- **Agente.** Genera el JSON de override; verifica diffs embebido vs `.py`; corre la suite; instrucciones paso a paso.
- **Humano.** Ejecuta la edición/re-export en sesión Rhino (P5).
- **Entregables.** Canvas re-exportado; override operativo; corrida ZXJH con override.
- **PC.** PC-1.
- **Criterio.** Corrida F1 de AAA0240ZXJH con override produce GFA en rango esperado (rango "3" tras corrección del "1" heredado de geobase), `valido:true` y **validación por lado: delta de GFA por lado y io/ic por lado coherentes con el override aplicado** (independiente del frame global).
- **Riesgos.** Divergencia de triple implementación (R2 → paridad en D2).
- **Horas humano:** ≈3.

#### C4. F3: validar Zonas y prueba real en ArchiCAD — `alta · S2–S3`
- **Descripción.** Validar Zonas con los 4 casos (A/B/B_SALUD/C), tests unitarios de la lógica Zona, prueba real de Morphs/Zonas en ArchiCAD 29 vía Live Connection/Tapir. La parte ArchiCAD requiere A5 cerrado y la suite de integración del clon (D4) como red previa.
- **Cambios v2 (H-08/H-16).**
  - **Evidencia ≠ gate:** el acta de la prueba ArchiCAD registra el resultado con capturas; **PC-3 se aprueba solo con corrida exitosa**. Si hay bloqueante, el acta queda en estado **en-bloqueo** (no aprobado) con plan de resolución fechado, dueño y criterio de re-entrada; F4/F5 no avanzan sobre un PC-3 en-bloqueo.
  - **Runtime de tests Zona declarado:** lógica pura en **CPython 3.12 con sintaxis 2.7-compatible y stubs de geometría** (patrón de la suite vigente); nada de pytest bajo IronPython (P8).
- **Agente.** Tests unitarios; verifica `morph-manifest.json` por caso; guía de ejecución manual.
- **Humano.** Corre los casos en Rhino; prueba en ArchiCAD; evalúa la calidad arquitectónica de la masa (no delegable).
- **Entregables.** Suite Zona en verde (CPython); 4 casos validados; acta de prueba ArchiCAD con capturas.
- **PC.** PC-3.
- **Criterio.** 4 casos generan Zonas sin errores y manifest coincide; **PC-3 aprobado solo con prueba ArchiCAD exitosa** — un bloqueante deja el gate en-bloqueo, nunca aprobado.
- **Riesgos.** R4 (mitigado por A5); borrados mal soportados por Live Connection → diseñar regeneración, no borrado.
- **Horas humano:** ≈6.

#### C5. Decisión de vía de disparo del canvas (EJECUCION_TAPIR) — `media · S3` ⚠️
- **Descripción.** Elegir la vía de disparo (recomendación documentada: 1+3 — reescritura de `proyecto.json` + script Tapir de confirmación). **Prerequisito explícito: A5 cerrado.**
- **Agente.** Dossier comparativo; implementación del script si se aprueba 1+3.
- **Humano.** Decide la vía (P6); ADR con número máximo+1.
- **Entregables.** ADR; script (si aplica); `EJECUCION_TAPIR.md` actualizado.
- **PC.** PC-4.
- **Criterio.** ADR numerado por regla §4.4; una corrida de disparo real de punta a punta.
- **Horas humano:** ≈2.

#### C6. Decisiones de negocio y normativa — `media · transversal` ⚠️
- **Descripción.** (a) Usos por sector definitivo (Sinupot / CU-5.4.x / Decreto 555 Art. 243); (b) OCR ficha 041 Muzú (re-agendar o cerrar); (c) CHIP activo de referencia (A3); (d) **destino de las propuestas "Deysy Peraza" (T-09):** los números se canalizan a F2/F3; los documentos de cliente entran al régimen 70-trabajos (§4.5) — los binarios hoy en `tests\` se retiran en A1.
- **Agente.** Dossiers breves; ejecuta lo aprobado.
- **Humano.** Decide cada punto; lo estructural va a ADR o contrato; lo demás, nota de decisión con ubicación (§4.4).
- **Entregables.** Notas de decisión enlazadas desde diario/doc de fase.
- **PC.** PC-0.
- **Criterio.** Los 4 puntos con estado explícito (decidido / re-agendado con fecha / cerrado).
- **Riesgos.** Indefinición perpetúa los overrides manuales como única fuente de verdad (R6).
- **Horas humano:** ≈2.

### Eje D — Puntos de control

#### D1. Definir los PC-0…PC-4 con su ciclo de vida completo — `alta · S1`
Núcleo del cambio v2 (T-02/T-05/H-08/H-16). Tabla de gates:

| PC | Límite de cadena | Revisor | Checks bloqueantes previos | Umbrales clave | Al fallo | Re-entrada |
|---|---|---|---|---|---|---|
| **PC-0** | Cada sesión | Agente (auto) + humano lector | Diario + espejo + mapa | Evidencia mínima: **el cierre del diario = pase** (T-12) | Cierre diferido con fecha en el diario | Siguiente sesión |
| **PC-1** | F1→F2 | Humano (agente prepara) | Suite invariante; validador de contratos (desde D2); sanidad F1 | Ancho de vía ∈ [5,30] m según clase; Ocup ≤ lote×COS; IO, IC ≤ 1+0,01; GFA en banda edificabilidad (**se fijan al cierre de C3**, H-07) | Acta en-bloqueo + bloqueante con **dueño y fecha** + re-agenda | Tras corregir causa raíz y re-corrida |
| **PC-2** | F2→F3 | Humano | Suite; contratos; frescura mercado ≤60 d; coherencia CHIP | `f2_resultado` coherente con `f2_entrada`; entregable B5 generado | Ídem | Ídem |
| **PC-3** | F3→F4/F5 | Humano (calidad arquitectónica no delegable) | Manifest completo; 4 casos Zona sin errores | `morph-manifest.json` completo y coincidente | Ídem (bloqueante ≠ aprobado) | Ídem |
| **PC-4** | F5 | Humano | Suite de integración del clon (D4); conexión ArchiCAD activa (A5); disparo punta a punta | Ciclo de inyección completo sin errores | Ídem | Ídem |

- **Actas (T-02).** JSON con estados **aprobado / rechazado / en-bloqueo** + campo **alcance** (qué contratos/entradas cubre la aprobación). Ubicación: **junto a los runs, `YYYY-MM-DD-<proceso>-NNN\acta-pcN.json`**, con veredicto espejo en el diario. **Prohibido el "cierre parcial"**: o el gate cubre lo declarado, o queda en-bloqueo con el faltante listado.
- **Modo bootstrap S1 (T-05).** Mientras D2 no exista, los gates se ejecutan en modo manual (checklist del doc de gates); PC-0 con verificación automatizada disponible desde S1 (cron/skill obsidian).
- **Agente.** Redacta el doc de gates + plantilla de actas; referencia en el checklist del orquestador. **Humano.** Valida el diseño (es su agenda de decisiones).
- **Criterio.** 5 PC documentados con revisor, umbrales y ruta de escape; 1 gate ejecutado con acta real dentro de S1–S2.
- **Riesgos.** Burocratizar (PC-0 ligero; acta de 5 campos + alcance).
- **Horas humano:** ≈1.

#### D2. Checks automáticos pre-gate — `alta · S2`
- **Descripción.** Suite con criterio invariante; validador de contratos (B3); frescura de mercado ≤60 días; coherencia CHIP (con los nicknames del hilo 3 como insumo); métricas de sanidad F1 con umbrales; completitud de `morph-manifest` para PC-3. **Añadidos v2:** **check de paridad para R2** — corridas espejo sobre fixtures con comparación de salida Python vs IronPython; si la paridad JS no es testeable → **ADR de riesgo aceptado** (H-10); **grep automatizado de citas** (propagación P11); verificación de PC-0 (T-12).
- **Agente.** Implementa el pre-gate en `run_pipeline_v01.py` y `servidor.py`; exit codes accionables. **Humano.** Aprueba bloqueantes vs informativos.
- **Criterio.** Un fallo inyectado es rechazado con mensaje accionable antes del humano; check de paridad en verde o ADR firmado.
- **Horas humano:** ≈1.

#### D3. Trazabilidad de versiones por corrida — `media · S2`
- **Descripción.** Manifest por run (hash del `.ghx`, versiones de `.py`, fecha, CHIP, caso, gate, rutas de salida). **Añadido (T-08): versión del contrato de datos y hash/versión de cada schema usado + apuntador a la fila de la tabla de vigencia.** Como los schemas nunca se editan in situ (B3), los manifests históricos siguen resolviendo.
- **Agente.** El orquestador genera el manifest automáticamente; índice de runs consultable (ubicación §4.1). **Humano.** Aprueba el formato.
- **Criterio.** Cualquier `resultados_<CHIP>.json` rastreable a canvas+scripts+contrato+schemas+gate en ≤1 minuto.
- **Horas humano:** ≈0,5.

#### D4. Conciliar y cerrar los planes anteriores — `media · S2–S3`
- **Descripción.** Ejecutar la **matriz de conciliación de los tres planes (§4.3)**: actualizar frontmatters (08-14 y 08-22, con estados del enum vigente), ejecutar la suite de integración en el clon `D:\Work\AI\clones\disenoparametrico-integracion` como prerequisito de PC-4.
- **Agente.** Ejecuta la conciliación documental y la suite cuando toque. **Humano.** Aprueba la conciliación.
- **Criterio.** Cada etapa de cada plan con estado explícito y dueño; suite corrida o cierre justificado.
- **Riesgos.** Repetir "plan documentado no ejecutado" (cada re-agenda lleva gate y horizonte).
- **Horas humano:** ≈1.

#### D5. Auditoría de coherencia documental — `baja · primer ciclo al cierre de S1, luego mensual`
- **Descripción.** Chequeo recurrente: drift docs↔código, huecos de sesiones, frontmatter y ≤5 tags, enlaces del mapa, **grep de citas (P11) y verificación de PC-0**. **Cambio v2 (T-12): el primer ciclo se adelanta al cierre de S1** (no S3).
- **Agente.** Ejecuta y emite informe corto; automatizable como cron mensual. **Humano.** Recibe el informe; corrige derivas.
- **Criterio.** Primer ciclo con hallazgos con dueño.
- **Horas humano:** ≈0,5 por ciclo.

### Objetivos de pipeline (nuevos — H-02: la obra principal bajo gobernanza)

#### F2-EXT. F2 extendido / build-to-rent + piloto MercadoViviendaBogota — `alta · S2`
- **Descripción.** Completar el extendido: recursos disponibles, saldo, financiación (`financiacion_saldo[]`), acabados, multi-escenario (forma ya en `f2_entrada.json` del 08-25); operar el modo renta (build-to-rent) con `F2_RENTA_MOTOR_v03` dentro del orquestador; primer ciclo piloto completo `MercadoViviendaBogota` → `F2_SINCRONIZAR_MERCADO_v01` con las lecciones 09-03 como restricciones (origen puro, append-only, `meta.sync`, frescura ≤60 días).
- **Agente.** Implementación y corridas; prepara los checks de PC-2. **Humano.** Revisa supuestos de escenario; decide en PC-2.
- **Entregables.** `f2_entrada.json` multi-escenario; `resultados_<CHIP>.json` del extendido + BtR; piloto de mercado con evidencia de fuente y frescura; reporte B5.
- **PC.** PC-2.
- **Criterio.** Un CHIP real pasa el ciclo extendido+BtR completo con validador en verde; piloto con fuente y fecha ≤60 días; resultados trazables por manifest (D3).
- **Riesgos.** Dependencias: A3 (contratos, CHIP activo) y B3 (validador) antes de cerrar; capacidad humana de S2.
- **Horas humano:** ≈3.

#### F4-VAL. Primera corrida Ladybug validada + fusión de duplicados — `media · S3`
- **Descripción.** Primera corrida de `F4_LADYBUG_ANALISIS_v01/v02` con EPW real (hoy nunca corrió — R11), consumiendo Zonas ya validadas (PC-3 aprobado); decidir la fusión de los duplicados ⚠️.
- **Agente.** Prepara la corrida; compara resultados contra expectativas físicas básicas; dossier de fusión. **Humano.** Valida plausibilidad ambiental; decide la fusión.
- **Entregables.** Corrida validada con manifest; decisión de fusión (nota o ADR si es estructural).
- **PC.** Acta propia en el alcance de PC-3 (sub-gate documentado); criterio: corrida con EPW real sin errores y resultado plausible para Bogotá (radiación/temperaturas en rango).
- **Riesgos.** Plugins Ladybug headless (anticipado por la tabla de B2); consumir Zonas no validadas (bloqueado por PC-3).
- **Horas humano:** ≈2.

#### F5-MAPEO. Crear `F5_MAPEO_TAPIR_v01.py` y primer ciclo de inyección — `alta · S3`
- **Descripción.** Crear el script de mapeo (capas F0 + stories vía `F3_StorySync_v01` + confirmación Tapir) y ejecutar el primer ciclo de inyección con PC-4 completo.
- **Agente.** Script (nomenclatura P8); corrida; manifest; acta. **Humano.** Acompaña la sesión ArchiCAD; decide en PC-4.
- **Entregables.** Script vigente; primer ciclo punta a punta; acta PC-4.
- **PC.** PC-4.
- **Criterio.** Ciclo completo de inyección exitoso **con el gateway AutoClaw activo** (A5 cerrado); manifest y acta completos.
- **Riesgos.** Dependencias duras declaradas: A5, C5 (ADR de disparo), D4 (suite de integración); regeneración en vez de borrado.
- **Horas humano:** ≈2.

---

## 3. Secuenciación corregida (S1/S2/S3)

**Supuesto de capacidad (H-09).** 1 persona ≈ **8 h/semana** de trabajo humano (sesiones GUI + decisiones); el agente absorbe diagnóstico, dossiers, implementación y verificación. Presupuesto humano total ≈ **47 h** (≈6 semanas a 8 h/sem). Los horizontes son de carga, no de calendario exacto. **Ruta crítica:** A1 → C1 → C3 → C2 → PC-1 → F2-EXT → PC-2; y en paralelo **A5 → C4(ArchiCAD) / C5 → D4 → F5-MAPEO → PC-4**. Recortables sin romper S2/S3: B4, B5, B6, D5 (y D3/B5 si S2 se saturara).

**Grafo de dependencias (H-12).** A1→B1 (no smoke tests contra venv en reparación); C1→B2 (no PoC sobre canvas sin veredicto); A3→toda corrida formal con CHIP (C2, F2-EXT); A5→C4-ArchiCAD, C5, F5-MAPEO. Regla: ningún smoke test/PoC contra un entorno o canvas cuyo saneamiento/veredicto esté pendiente.

**S1 — Fundamentos de confianza (~13 h humano; ≈1,5–2 semanas a 8 h/sem).**
A1 (2) → A2 + C1 (4) → A4 (2) → **A5 arranque de diagnóstico (2)** → B1 dossier + sesión por lotes (1,5) → D1 gates + plantilla de actas (1) → D5 primer ciclo (0,5). No toca la lógica de fases; cierra el drift, pone dueño y criterio al bloqueador 19723 y deja los gates definidos en modo bootstrap.

**S2 — Credibilidad del GFA y F2 extendido (~18,5 h; ≈2–2,5 semanas).**
- F3 en orden corregido: **C3 (3) → C2 (3)**; PC-1 activo con umbrales fijados por C3.
- F2: A3 (2) → B3 (1) → **F2-EXT (3)** con PC-2; B5 (1) en paralelo.
- Capacidades: B2 (3, con paso 0), D2 (1), D3 (0,5); cierre de A5 (1).
- Nota de capacidad: 18,5 h > 16 disponibles en 2 semanas; **B5 y D3 son recortables a S3** sin romper la ruta crítica.

**S3 — F3 en ArchiCAD, F4, F5 (~15 h; ≈2 semanas).**
C4 (6, prueba ArchiCAD; requiere A5) → C5 (2, ADR) → **F4-VAL (2)** → **F5-MAPEO (2)** → D4 (1, conciliación de los tres planes + suite del clon) → B4 (1) → B6 (0,5) → D5 (0,5). B5/D3 si se recortaron de S2.

⚠️ **Reserva sobre S3:** mientras A5 no registre la conexión real, C4-ArchiCAD, C5 y F5-MAPEO quedan con agenda condicional; F4-VAL (Rhino/Ladybug) no depende del puerto y se mantiene. Si A5 no cierra al final de S2 → decisión humana de replanificación (diferir la parte ArchiCAD con horizonte, o escalar el ticket).

---

## 4. Gobernanza documental y trazabilidad

### 4.1 Dónde se registra cada cosa — con canónico/espejo/trigger (T-02/T-07)

| Contenido | Canónico | Espejo | Trigger |
|---|---|---|---|
| Plan v2 aprobado | `docs\` del proyecto | Vault `10-arquitectura\2026-09-07-plan-avance-disenoparametrico.md` | Mismo commit |
| Doc de quality gates (D1) | `docs\arquitectura\` del proyecto | Vault `10-arquitectura\2026-09-07-quality-gates-pipeline.md` | Mismo commit |
| **Actas de gates** | Carpeta de runs: `YYYY-MM-DD-<proceso>-NNN\acta-pcN.json` | Veredicto en el diario del día | Al cerrar el gate |
| Contrato de datos | `docs\archivos-intercambio-canonicos.md` (proyecto) | Vault `10-arquitectura\2026-08-22-contrato-datos.md` | Mismo commit |
| Schemas (`config\schemas\`) | Proyecto, versionados (no edición in situ) | Referencia en contrato v1.1 | Mismo commit |
| ADRs | Vault `10-arquitectura\decisiones-adr\adr-NNN-*.md` | `docs\arquitectura\decisiones-adr\` | Mismo commit |
| Registro de decisiones por skill (B1) | Dossier del skill en `docs\sesiones\` o doc de fase | Veredicto en el diario | Al decidir cada lote |
| Notas de decisión (C6, CHIP, B4-baja, fusión F4) | Doc de fase correspondiente | Enlace desde diario y mapa | Al decidir |
| Dossieres (B1/B2/B4/C5/A5) | `docs\sesiones\` del proyecto | Enlace desde el mapa | Al redactar |
| Índice de runs (D3) | Carpeta de runs del orquestador | Corte en estado-avance por hito | Automático (orquestador) |
| Trabajos por fase | Vault `20-fases\fase-N-*\` | `docs\` del proyecto | Mismo commit |
| Diarios | Vault `60-diario\YYYY-MM-DD.md` | `docs\daily\` (patrón vigente) | Mismo commit |
| Lecciones | Vault `50-lecciones\` | — | Al cerrar lección |
| Casos de prueba documentados | Vault `40-tests\` | — | Al crear caso |
| Sesiones/crónicas | `docs\sesiones\` | Enlace desde diario | Al cerrar sesión |
| Estado consolidado + **tabla única de vigentes** (T-14) | Vault `10-arquitectura\estado-avance-disenoparametrico.md` | Referenciado (no repetido) por manual/README/docs | Corte por hito (P11) |
| Entregables al cliente (T-09) | `05_ENTREGABLES` (única zona PUBLICADO, 70-trabajos) | ARCHIVADO a `I:\archivo` | Al publicar |

Regla general: canónico en docs del proyecto, vault espejo de navegación, trigger = mismo commit; en conflicto gana el canónico (patrón ya vigente de diarios, extendido a todos los artefactos).

### 4.2 Reglas de oro (checklist actualizado)
Frontmatter YAML; ≤5 tags en español; `YYYY-MM-DD-titulo-kebab.md`; enlace desde `mapa-conocimiento.md`; ADR con numeración cerrada; corte en estado-avance cuando el plan toque scripts/datos/pipeline; nomenclatura P8 y runtime de tests P8; origen puro/append-only con `meta.sync`; **regla de propagación P11** (tabla única → corte → grep → contrato si cambia interfaz; grep automatizado en D2/D5); **precedencia P12**; identidad `DSalasC-SW-Work` para servicios externos si algún objetivo los requiere (hoy ninguno).

### 4.3 Conciliación de los tres planes (T-01)

**Plan 08-14** (diagnóstico y plan de acción, borrador):

| Etapa 08-14 | Estado real hoy | Decisión | Dueño |
|---|---|---|---|
| Inmediato (header NORMATIVA v02a, `_legacy` F1) | Hecho | Cerrado | — |
| Etapa 1: tests de integración en clon | Documentada, nunca ejecutada | **Re-agendada a S3** como prerequisito de PC-4 | Agente ejecuta; humano aprueba |
| Etapa 2: manejo de errores y logging | Sin evidencia | **Absorbida** en B3/D2 | Agente |
| Etapa 3: perfilado/rendimiento (opcional) | Sin evidencia | **Cerrada** como opcional → B6 | — |

**Plan orquestador 08-22** (Etapas 0–6, `por-desarrollar`, handoff vigente). Su frontmatter pasa a `activo` (enum vigente) **con nota de conciliación enlazada a este plan** — no se inventa un estado fuera del enum. El handoff del orquestador lo heredan **D2/D3** (checks y manifest integran `run_pipeline_v01.py` y `servidor.py`) y **A3** (dueño de `data\activo\`). Matriz propuesta:

| Etapa 08-22 | Decisión propuesta ⚠️ (confirmar contra el doc al ejecutar D4) | Heredada por | Dueño |
|---|---|---|---|
| Etapa 0 — orquestación base / productor único | Sigue vigente | Orquestador (transversal) | Agente |
| Etapas que tocan `data\activo\` y overrides | Absorbida | A3 | Agente + humano |
| Etapas de validación / manejo de errores | Absorbida | B3 / D2 | Agente |
| Etapas de trazabilidad / manifest | Absorbida | D3 | Agente |
| Etapas de disparo ArchiCAD | Sigue vigente → se concreta en | C5 / A5 | Humano |
| Etapas restantes | Sigue-vigente-con-dueño o re-agendada a S# | Según contenido | Agente/humano |

**Integración 09-03 (MercadoViviendaBogota):** las lecciones (origen puro, append-only, `meta.sync`, frescura ≤60 d) quedan como **restricciones de F2-EXT**, no como plan separado.

Anomalías formales del doc 08-14 (6 tags, sin fecha en el nombre) se anotan sin mover el archivo, para no romper enlaces. Regla dura (checklist inf. 03, ítem 9): **ningún tercer plan paralelo sin conciliar.**

### 4.4 Auditoría P6 de decisiones → registro (T-04) y regla ADR (T-13)
Regla: *si la decisión sobrevive a la sesión que la tomó, es ADR o contrato; si no, nota de decisión con ubicación declarada.* Aplicación en v2: **A5** → ADR-011; **B2** → ADR (Rhino.Compute); **C5** → ADR (vía de disparo); **B4** → ADR si se reinstala IA local, nota si se da de baja; **adopción de `config\schemas\`** → ADR + contrato v1.1; **CHIP activo de referencia** → ADR o nota (decide el humano en A3); **A4** → ADR solo si se crea la tarea de Windows; **C6 y fusión F4** → notas de decisión. **Numeración:** siguiente = máximo existente + 1 (**hoy 011**); huecos 001/003/009 **no se reutilizan**; nota breve en `10-arquitectura` que registre las inconsistencias conocidas (adr-010 con H1 "ADR-008", enlaces adr-008/009) para no re-descubrirlas.

### 4.5 Entregables y 70-trabajos (T-09)
Los reportes internos de pipeline (Excel/PDF de B5, actas, manifests) son **evidencia de gate**: viven en runs y no se publican. Todo lo que vaya a cliente o publicación se rige por 70-trabajos con estados ISO 19650: **PUBLICADO solo en `05_ENTREGABLES`**; ARCHIVADO a `I:\archivo`. Propuestas "Deysy Peraza": números → F2/F3 (C6d); documentos → 70-trabajos; los binarios hoy en `tests\` se retiran en A1.

---

## 5. Trazabilidad crítica → resolución (30/30)

| ID | Resolución en v2 |
|---|---|
| H-01 | **A5** (nuevo) + reserva de S3 (§3) |
| H-02 | Objetivos **F2-EXT / F4-VAL / F5-MAPEO** (§2) con PC y criterios |
| H-03 | Orden **C3→C2** + criterio de C2 por lado (§2, §3) |
| H-04 | **Paso 0 de B2** (rhino.compute.exe, MCP punta a punta, AC29) + P4 reescrito |
| H-05 | **Paso 0 de B3**: aprobación jsonschema/pydantic ⚠️ o validador propio con tests negativos |
| H-06 | Criterio B2: **tolerancia relativa 1e-6** + **tabla completa de plugins** |
| H-07 | **Umbrales numéricos de PC-1** (D1), fijados al cierre de C3 y versionados en el contrato |
| H-08 | C4: **evidencia ≠ gate** (estados de acta) + **runtime CPython/stubs** (P8) |
| H-09 | **Horas por objetivo** (§6) + capacidad 8 h/sem + ruta crítica (§3) + B1 por lotes |
| H-10 | **Check de paridad en D2** o ADR de riesgo aceptado |
| H-11 | A1: criterio separado **terceros vs editable**, decisión (a)/(b) ⚠️ |
| H-12 | **Grafo de dependencias** (§3): A1→B1, C1→B2, A3→corridas CHIP, A5→C4/C5/F5 |
| H-13 | **Hilos 3/6 en B6** con estado; **mojibake de labels** en A1/A2 (P10) |
| H-14 | A4: **árbol de decisión 07:30** con criterios por rama + especificación de tarea Windows |
| H-15 | A2: `MANUAL_DE_EJECUCION.md` **sin versión en el nombre**, encabezado con hash + manifest |
| H-16 | D1: estados **aprobado/rechazado/en-bloqueo** + alcance; **prohibido cierre parcial** |
| T-01 | **§4.3: matriz de conciliación de los tres planes** con estado y dueño por etapa |
| T-02 | **§4.1**: filas para actas, registros de decisión, dossieres e índice de runs |
| T-03 | A2: **retiro a `_legacy`** de los dos manuales divergentes + grep verificable |
| T-04 | **§4.4: auditoría P6 completa** (B4, schemas, CHIP) con ADR/nota y ubicación |
| T-05 | **D1: tabla por gate** con revisor, umbrales, ruta de escape, re-entrada y **modo bootstrap S1** |
| T-06 | **P11: regla de propagación de versiones** + grep automatizado en D2/D5 |
| T-07 | **P12 + §4.1**: canónico docs / espejo vault / trigger mismo commit |
| T-08 | **D3: manifest con versión de contrato + hash de schemas**; schemas versionados (B3) |
| T-09 | **§4.5: regla 70-trabajos**; destino Deysy Peraza en C6(d) |
| T-10 | **§6: columna PC normalizada**; smoke de B1 como sub-check de PC-0 con registro |
| T-11 | A1/D2: **criterio invariante de suite** (verde, sin fallos nuevos respecto a corrida previa) |
| T-12 | **PC-0 con evidencia mínima** (diario = pase) + verificación automatizada; D5 primer ciclo en S1 |
| T-13 | **§4.4: regla ADR máx+1 (hoy 011)**; huecos no reutilizados; nota de inconsistencias |
| T-14 | A2: **tabla única de vigentes** (extensión estado-avance) como fuente autoritativa |

---

## 6. Tabla resumen del plan v2

| Objetivo | Eje | Prioridad | Horizonte | Entregable clave | PC | Horas humano |
|---|---|---|---|---|---|---|
| A1 | A | alta | S1 | Commit de saneamiento + decisión editable | PC-0 + suite | 2 |
| A2 | A | alta | S1 | Manual único estable + tabla única de vigentes | PC-0 | 2 |
| A3 | A | alta | S2 | Contrato v1.1 + schemas versionados | PC-1/PC-2 | 2 |
| A4 | A | media | S1 | Cron verde o baja documentada | PC-0 | 2 |
| **A5** ⚠️ | A | alta | S1–S2 | ADR-011 + conexión real 19723 | Sub-check PC-4 | 3 |
| B1 ⚠️ | B | alta | S1 | 14 skills con smoke tests (lote único) | PC-0 (sub-checks) | 1,5 |
| B2 | B | alta | S2 | PoC + tabla plugins + ADR (con paso 0) | PC-1 | 3 |
| B3 | B | alta | S2 | Schemas + `F0_VALIDAR_CONTRATOS_v01` | PC-1…PC-4 | 1 |
| B4 ⚠️ | B | media | S2–S3 | ADR o docs corregidas | PC-0 | 1 |
| B5 | B | media | S2 | Ciclo F2 → Excel → PDF → vault | PC-2 | 1 |
| B6 | B | baja | S3+ | Backlog con hilos 3/6 | PC-0 | 0,5 |
| C1 | C | alta | S1 | Checklist firmado canvas v03 | PC-1 | 2 |
| C3 | C | alta | S2 | Fix frame + umbrales PC-1 | PC-1 | 3 |
| C2 | C | alta | S2 | Canvas re-exportado + override ZXJH | PC-1 | 3 |
| C4 | C | alta | S2–S3 | Tests Zona + 4 casos + acta ArchiCAD | PC-3 | 6 |
| C5 ⚠️ | C | media | S3 | ADR vía de disparo + script | PC-4 | 2 |
| C6 ⚠️ | C | media | transversal | 4+1 notas de decisión | PC-0 | 2 |
| D1 | D | alta | S1 | Doc de gates + plantilla de actas | PC-0 | 1 |
| D2 | D | alta | S2 | Pre-gate + paridad + grep citas | PC-1…PC-4 | 1 |
| D3 | D | media | S2 | Manifest con contrato+schemas + índice | Todos | 0,5 |
| D4 | D | media | S2–S3 | Conciliación 3 planes + suite clon | PC-4 | 1 |
| D5 | D | baja | S1→mensual | Informe de auditoría | PC-0 | 0,5/ciclo |
| **F2-EXT** | Pipeline | alta | S2 | Extendido + BtR + piloto mercado | PC-2 | 3 |
| **F4-VAL** | Pipeline | media | S3 | Corrida Ladybug validada + fusión ⚠️ | Acta alcance PC-3 | 2 |
| **F5-MAPEO** | Pipeline | alta | S3 | `F5_MAPEO_TAPIR_v01` + primer ciclo | PC-4 | 2 |

**Total ≈ 47 h humano** (más 0,5 h por ciclo de D5). ⚠️ = requiere decisión humana explícita antes de ejecutar (P6).

---

## 7. Riesgos residuales

1. **S3 condicionado al puerto 19723.** Hasta que A5 registre la conexión real (criterio de aceptación), C4-ArchiCAD, C5 y F5-MAPEO quedan con agenda condicional; F4-VAL no depende del puerto y se mantiene. Si A5 no cierra al final de S2 → replanificación humana ⚠️. Esta es la reserva explícita del plan sobre S3.
2. **Paridad JS no testeable.** Si el check de paridad no puede cubrir la capa JS, queda como riesgo aceptado por ADR (H-10): divergencia latente con más automatización encima.
3. **Capacidad humana.** El plan asume 8 h/semana; S2 queda al límite (B5/D3 recortables). Dos semanas perdidas desplazan la cadena completa por la ruta crítica.
4. **Re-baseline de GFA históricos** tras C3: esperado y anunciado; los casos A/B/B_SALUD/C requieren re-corrida de referencia.
5. **Dependencias externas.** Ticket del proveedor (job 07:30): cerrado por rama con criterios (H-14); ticket 19723 externo: cerrado por A5 o por decisión de replanificación.
6. **Sobreespecificación de schemas.** Mitigada por versionado (no edición in situ) y por el manifest que preserva qué schema validó cada corrida.
7. **PC-0 sin verificador durante el bootstrap.** Mitigado con evidencia mínima (diario = pase) y verificación automatizada disponible desde S1 (cron/skill obsidian).
8. **Backlog B6.** Expectativas infladas: declarado explícitamente; ningún ítem se ejecuta sin objetivo formal con gate.

**Verificación de factibilidad.** Ninguna línea depende de capacidades no verificadas: lo instalado-pendiente (rhino.compute.exe, puente MCP punta a punta, AC29) tiene pre-verificación con criterio propio como paso 0; las brechas reales (IA local caída, jsonschema/pydantic ausentes, pandoc/python-docx/pyshp, pyRevit sin instalar) están condicionadas a aprobación humana o excluidas a B6. Con las condiciones mínimas de ambas críticas satisfechas —y ambas lo están en este v2—, el horizonte de ≈6 semanas es realista para una persona + agentes, con la reserva declarada sobre S3 mientras el puerto 19723 no esté cerrado.
