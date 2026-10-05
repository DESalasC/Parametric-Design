# Sesión 2026-10-05 — F3_DISTRIBUCION v03.1 (sección GH) + canvas v13.1 parcheado

## Resumen
Reporte del operador sobre el canvas `F1_CONTEXTO_v13.1`:
- `barras_json` del componente `#61-F3_DISTRIBUCION_v03.py` daba
  `Runtime error (SyntaxErrorException): unexpected token ':'` (línea 140,
  `def normalizar_uso(uso: str) -> str:`).
- Consultas: tipo/acceso de cada entrada del script + origen/destino del
  cableado; y por qué `normativa_confirmada` (Boolean=false) y
  `pisos_maximos_total` (Number Slider=5) no vienen "directamente del orquestador".

## Causa raíz (SyntaxError)
IronPython 2.7 (GHPython) no soporta anotaciones de tipo Python 3 (`uso: str`,
`-> str`). El script se escribió como CLI (py3) y se embebió tal cual en el
componente. Además, el script NO tenía sección GH: aunque compilara, no leía
entradas ni publicaba salidas dentro del componente.

## Correcciones aplicadas (v03.1)
1. `src/fase-3-masa/F3_DISTRIBUCION_v03.py`:
   - fix sintaxis IronPython 2.7 (`normalizar_uso` sin anotación).
   - SECCIÓN GRASSHOPPER completa: lee entradas (por nombre normalizado o por
     índice vía `ghenv`) y publica las 7 salidas GH → `barras_json` funcional
     en canvas (schema `f3_barras_salida_v01`, consumible por NORMATIVA v09).
   - Si `presupuesto_ocupacion_m2` está vacío → se deriva = lote × io_max − margen
     (0,1% / mín. 0,25 m²) para no formar el ciclo NORMATIVA→F3→NORMATIVA y que
     la validación APROBADA no falle por centésimas.
   - Raíz de proyecto robusta: archivo (CLI) → env `DISENO_PARAMETRICO_ROOT`
     (canvas) → validación `src/`.
   - Encabezado reescrito con tabla de cableado completa (tipo + acceso Item/List
     + origen/destino) — pedido explícito del operador.
2. Canvas `gh-definitions/F1_CONTEXTO_v13.1.ghx` (+ `.gh` regenerado con
   `scripts/utilities/ghx-to-gh.ps1`, GH_IO):
   - CodeInput de `#61-F3_DISTRIBUCION_v03.py` reemplazado por v03.1
     (19031 → 34082 chars).
   - Entradas renombradas a snake_case: `presupuesto_ocupacion_m2`, `io_max`,
     `n_barras_objetivo`, `entrepiso_adaptativo`, `prioridad_ajuste`,
     `bloques_separacion_m`, `bloques_crujia`, `bloques_nucleo`, `output_json`
     (`chip` y `usos` sin cambios; cables conservados: chip←F0, barras_json→NORMATIVA).
   - Description del componente actualizada (cableado resumido).
   - Script: `scripts/utilities/patch-ghx-v131-f3-distribucion-2026-10-05.py`
     (backups `.bak-20261005-*`; validaciones OK; comentarios XML preservados).
3. Tests: `tests/test_f3_distribucion_v03_gh.py` (10/10) — simula `ghenv` para
   validar lectura de entradas (nombre/índice), derivación con margen y JSON
   consumible por el parser de NORMATIVA v09.

## Revisión v03.2 (misma jornada, tras primera prueba viva ~12:43)
- **Fallo vivo**: al ejecutar #61 en el canvas → `Solution exception: SystemExit`
  (argparse sin argumentos desde `main()`). Causa: en GHPython (Rhino 8)
  `import ghenv` **FALLA** (ghenv se inyecta como VARIABLE de script, no como
  módulo) → `_EN_GH=False`; y `__name__` **ES** `"__main__"` dentro del
  componente → el guard corrió `main()` dentro de Grasshopper.
- **Fix**: detección `_gh_modulo()` = `"ghenv"`/`"ghdoc" in globals()` (ambas
  se inyectan como variables; confirmado en docs de mcneel/ghpython) → fallback
  import + aviso si entorno .NET/Rhino sin ghenv; guard CLI ampliado:
  `__name__=="__main__"` Y no-GH Y no-IronPython (platform / `sys.platform=="cli"`)
  Y no-`clr`. `main()` ya no puede correr dentro de Rhino.
- `barras_json` (salida GH) y los JSON de CLI → `ensure_ascii=True` (convención
  ASCII-safe; evita `UnicodeEncodeError` en el `str()` de NORMATIVA v09 al
  pasar el string entre componentes).
- Canvas re-parcheado (3.ª tanda de backups) + `.gh` regenerado (170.001 bytes)
  y re-validado con GH_IO (lectura OK, 0 avisos).
- Tests: 11/11 (nuevo test de regresión: ghenv como variable + `__name__`
  `"__main__"` → main NO se ejecuta; fallback por módulo; aviso entorno .NET
  sin ghenv).
- Entorno verificado: `DISENO_PARAMETRICO_ROOT` existe como variable de USUARIO
  (= `D:\Work\PROJECTS\DiseñoParametrico`) → la ruta se resuelve en GH.

## Revisión v03.3 (misma jornada, tras 2.ª prueba viva ~12:57)
- **Fallo vivo 2**: tras recargar v03.2 el componente corrió (GH OK) y falló con
  `F3 v03.2 | ERROR: 'unknown' codec can't decode byte 0xed in position 12` —
  mismo patrón de la lección 2026-09-17: en IronPython, `io.open`/`open` en modo
  texto intentan decodificar con el codec por defecto "unknown" y fallan con
  contenido/paths no-ASCII. (El SystemExit quedó resuelto por la v03.2.)
- **Fix v03.3**: lectura JSON con el patrón canónico del proyecto — `open(rb)` +
  cascada utf-8-sig → cp1252 → latin-1 + `json.loads` (`_leer_json`); escrituras
  binarias (`_escribir_texto`); `_texto_seguro()` normaliza rutas/entorno/entradas
  (bytes→unicode por cascada); literales con tilde de rutas activas como u"...";
  prints silenciados dentro de GH.
- **Diagnóstico v03.3**: el mensaje de error ahora indica el PASO
  (p.ej. "ERROR en [leer resultados F2]") + cola del traceback → converge rápido
  si quedara algo.
- Canvas re-parcheado (backups `.bak-20261005-1307*`) + `.gh` regenerado
  (171.241 bytes) y validado con GH_IO (0 avisos).
- Tests: 13/13 (nuevos: `_leer_json` con acentos; mensaje con paso de error).

## Hallazgos: `normativa_confirmada` / `pisos_maximos_total`
- Hoy: `normativa_confirmada` ← `#99-Boolean Toggle` (false);
  `pisos_maximos_total` ← `#94-Number Slider` (5). Son controles manuales del canvas.
- El orquestador (`F0_LOAD_PROYECTO_v01` + `proyecto.json` + servidor) NO expone
  esos campos todavía (no existen en `proyecto.json`, ni como salidas de F0, ni
  como endpoints). "Debería venir del orquestador" = mejora futura: agregar campos
  a `proyecto.json` + salidas F0 + recableado. El plan 2026-10-03 mantiene
  `normativa_confirmada=False` a propósito hasta la revisión humana.

## Verificación
- CLI: `F3_DISTRIBUCION_v03.py --caso B --presupuesto-ocupacion 662.44` → 4
  alternativas; recomendada `ALT-2B-305` (ocupación 662.44, GFA 3312.2) ✓.
- pytest nuevo: 10/10 ✓. Suite completa: **332 passed / 19 failed** — los 19 fallos
  son PREEXISTENTES (tests desactualizados vs fuentes actuales: LADOS v06.5→v06.8,
  NORMATIVA 'POTENCIAL'→'NO VALIDADO', PATIO bifurcación, orquestador; ya presentes
  en la corrida del 04-10; no tocan F3_DISTRIBUCION_v03; fallan también aislados).
- ghx→gh: `GH_IO` re-escribió `F1_CONTEXTO_v13.1.gh` (170 KB) → archivo válido.

## Pendientes
- Validación viva del operador (v03.3): cerrar el canvas SIN guardar, reabrir
  `F1_CONTEXTO_v13.1.gh` (o `.ghx`) y correr con chip `AAA0030JKOE`; verificar
  mensaje "F3 v03.3 | ..." y que `barras_json` → NORMATIVA v09 dé `valido=True`
  y `gfa_aprobado_m2 > 0`. Si algo falla, el mensaje dirá el PASO exacto
  ("ERROR en [paso]: ... | tb: ...") — enviarlo tal cual para converger.
  Si Rhino fue abierto antes de crearse la env var del proyecto, reiniciarlo
  para heredar `DISENO_PARAMETRICO_ROOT`.
- Limpieza de los 19 tests desactualizados (sesión futura).
- Decidir si `normativa_confirmada`/`pisos_maximos_total` se cablean desde el
  orquestador (requiere campos nuevos).
- (Bloqueador histórico) puerto 19723 para conexión AutoClaw↔Live Connection.

## Commits
- `ee84be28` — v03.1 (sección GH + fix sintaxis IronPython; incluye 2.ª pasada).
- `56be9869` — v03.2 (detección ghenv/ghdoc + guard CLI; amend final).
- `e5dd8bea` — v03.3 (lectura canónica rb+cascada; pasos de diagnóstico).
