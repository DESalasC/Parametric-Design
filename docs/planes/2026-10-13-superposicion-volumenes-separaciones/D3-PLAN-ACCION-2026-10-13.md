# D3 — Plan de acción: superposición de volúmenes + separaciones (2026-10-13)

- **Proyecto:** DiseñoParamétrico · **Caso:** B — AAA0030JKOE (Test 07.pln) · **Canvas:** `F1_CONTEXTO_v13.5.ghx/.gh`
- **Objetivo:** dejar ArchiCAD y la previsualización con **una sola versión coherente** del modelo — 4 bloques separados (sin mezcla con la fase de 2 volúmenes), **20/20 zonas**, stories correctos — y **cerrar los pendientes de diseño**: separaciones laterales ancladas al lote y espacio posterior contra el borde.

---

## F0 — Diagnóstico y correcciones offline ✅ (hecho, 2026-10-13)

| Actividad | Estado | Resultado |
|---|---|---|
| Verificación en vivo AC (solo lectura) + censo | ✅ | 3 stories; 16 zonas BEP (Bloque 4 incompleto); 71 morphs contexto; 0 losas/muros → ver **D1** |
| Evidencia registrada | ✅ | `evidencias/` (2 capturas + 2 recortes + CSV morphs + censo en texto) |
| Corrección **PATIO v03.4** (src) + tests | ✅ | Sin patios en multivolumen; `12/12` y `38/38` pruebas "patio" → ver **D2** |
| Herramientas nuevas | ✅ | `F0_CENSO_ELEMENTOS_v01.py`, `dump-red-canvas.py`, `_tmp-zonas-propiedades.py` |

## F1 — Parche del canvas (próxima ventana, GH cerrado)

1. Re-embebidos pendientes: **#198-F3_VOLUM_GENERADOR_v08.1 (fix d)**, **#78-F1_ETAPA2_PATIO (v03.4)** y **#200-F3_DISTRIBUCION_v03 (v03.9 — fix de marcos)**; regenerar `.gh`; backups `.bak-fechados`; validar con `comparar-canvas-src.py` (esperado: `IGUALES: True` en los tres) y GH_IO.
2. Operador: **cerrar sin guardar → reabrir** `F1_CONTEXTO_v13.5.ghx` (recarga limpia).
- *Condiciones:* canvas cerrado durante el parche; no pisar ediciones vivas del operador; conservar cableado.
- *Resultado esperado:* canvas = src; mensajes `PATIO v03.4` y `F3 v03.8`/`IMPLANTACION`.

## F2 — Corrida limpia + saneamiento de ArchiCAD

1. **Borrar en AC las 16 zonas actuales** (selección → suprimir; o filtrar por categoría "Zonas" / capa) — el .pln quedará sin el estado parcial.
2. Correr el canvas (orden de arranque habitual; AutoClaw no antes que AC).
3. **Verificar con censo**: `F0_CENSO_ELEMENTOS_v01.py` → esperado **Zones = 20** (4 bloques × 5 pisos) y mensaje `IMPLANTACION F3 | … | 4 bloques | 20 zonas`.
4. Si faltan zonas: capturar mensaje del componente #198 (+ consola) y diagnosticar antes de seguir.
- *Limitaciones:* la LC no borra elementos huérfanos por sí sola; el borrado manual es parte del procedimiento. Repetir censo si el operador guardó cambios después de las lecturas del D1.

## F3 — Stories (niveles) en ArchiCAD

1. Crear los **8 niveles** (`niveles_deseados.json`: GF @ −11,565 … L07 @ +9,785; floor_h 3,05; snap ≤ 0,31 m) — manual asistido (la API ac29 no crea stories).
2. Verificar: `F3_StorySync_v02.py --list` / `--check --chip AAA0030JKOE` → **0 faltantes**.
3. Re-correr canvas → zonas por nivel con Name/Number BEP visibles en su piso.
- *Resultado esperado:* zonas ubicadas en niveles correctos; fin del "colapso" visual de cotas.

## F4 — Separaciones laterales + espacio posterior (diseño)

Sobre la corrida limpia, validar y ajustar si aplica (F3_DISTRIBUCION v03.8 → v03.9 si hay cambios):

1. **Separaciones laterales**: cada franja de separación entre bloques debe quedar **dentro del lote** con extremos que **empalmen con los bordes laterales** (recorte real contra el polígono; sin bolsillos > 0,5 m²). Revisar el aviso "no alcanza borde derecho" y el margen (~145 m²) del caso B.
2. **Espacio posterior**: el último bloque **empata con el fondo del lote** (anclaje a frente y fondo, sin vacío posterior).
3. **Escalonamiento 1/5** por piso contra el empate (`xmax`) coherente con las alturas de vecinos.
- *Criterios de aceptación:* en planta — bloques dentro del lote, separaciones entre cuerpos = valores declarados, frente/fondo empatados; en AC — 4 bloques / 20 zonas, sin superposiciones.
- *Registro:* capturas antes/después + mensajes del canvas.

## F5 — Cierre

- Re-validación visual (AC + preview), actualización de estado de avance, acta de sesión y lecciones en el Vault; commits de proyecto/vault.
- Arrastres relacionados: dataset mixto (B), `z_base` contexto50, tests stale restantes, F4/F5 del pipeline.

---

## Decisiones abiertas (operador)

| # | Decisión | Nota |
|---|---|---|
| 1 | Confirmar la lectura de la regla patio (D2 §2) | La implementación v03.4 asume: patio solo en régimen 1 volumen; multivolumen = separaciones |
| 2 | Limpieza de zonas AC: total (recomendado) vs incremental | El estado actual es parcial (16/20); total evita residuos |
| 3 | Regla "5 m" empates IDPC (parametrizable) | Pendiente de validación externa |

## Anexo — comandos útiles

```powershell
.venv\Scripts\python.exe src\interfases-archicad\F0_CENSO_ELEMENTOS_v01.py --sel --bbox=Morph,Zone
.venv\Scripts\python.exe src\interfases-archicad\F3_StorySync_v02.py --list
.venv\Scripts\python.exe src\interfases-archicad\F3_StorySync_v02.py --check --chip AAA0030JKOE
.venv\Scripts\python.exe scripts\utilities\comparar-canvas-src.py
.venv\Scripts\python.exe scripts\utilities\dump-red-canvas.py
```
