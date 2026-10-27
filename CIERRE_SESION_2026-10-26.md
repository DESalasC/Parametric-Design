# Cierre de sesión — 2026-10-26 (DiseñoParametrico)

## Sesión de trabajo

**Fecha:** 2026-10-26  
**Proyecto:** DiseñoParametrico  
**Tipo:** Cierre de sesión — validación de reglas de empates laterales y retiros patrimoniales  
**Estado:** Cerrado ordenadamente, pendiente ejecución en vivo (canvas + orquestador)

---

## Situación encontrada al inicio de la sesión

El proyecto DiseñoParametrico tiene el canvas maestro `F1_CONTEXTO_v13.6.ghx` en `gh-definitions/` y el pipeline modular F1 (ETAPA1/ETAPA2) en `src/fase-1-contexto/`. El componente `F1_ETAPA2_NORMATIVA_v09.1.py` estaba en uso pero no contemplaba:

- Retiro patrimonial de 3,0 m solo en primera franja de fachada (predio vecino nivel patrimonial 2).
- Exención de construcciones no patrimoniales al fondo del predio vecino.
- Empate diferencial con vecino derecho (11,40 m) sin distancia especificada al lindero.
- Cota de terreno central (+0,90 m) para validar altura máxima 10,00 m sobre cota.
- Diferenciación de alturas de vecino por lado izquierdo vs derecho.

La sesión anterior (2026-08-24) había dejado pendiente la sincronización del componente `F1_ETAPA2_LADOS_v06` en el canvas y la configuración del orquestador para generar JSON de overrides por lado.

---

## Problemas planteados en esta sesión

1. **Empates laterales no resueltos:** el predio vecino izquierdo es patrimonio nivel 2 (exige retiro 3,0 m durante toda la longitud del edificio patrimonial sobre fachada); el predio vecino derecho tiene 11,40 m de altura y el reglamento no especifica distancia exacta al lindero para el empate.
2. **Construcción no patrimonial al fondo:** exenta de retiros, pero no hay mecanismo para excluirla.
3. **Cota de terreno:** +0,90 m en el centro del lote juega a favor para los 10,00 m máximos, pero no hay entrada para reconciliar cota con altura máxima.
4. **Error de sintaxis en el canvas:** `F3_DISTRIBUCION_v03.py` usa type hints de Python 3 (`def normalizar_uso(uso: str) -> str:`) incompatibles con IronPython 2.7 (`SyntaxError: unexpected token ':'`), bloqueando el flujo `barras_json` → NORMATIVA.
5. **Error de sintaxis en `F1_ETAPA2_NORMATIVA_v10.py`:** paréntesis desbalanceado en la llamada a `.format()` del bloque `else` (línea 1441), corrigido.
6. **Error de runtime en IronPython 2.7:** `MissingMemberException: 'DataTree[object]' object has no attribute '__float__'` en `numero_opcional`, porque las entradas de Grasshopper llegan como `DataTree[object]`, no como listas simples. Corregido con función `_extraer_valor_gh` recursiva.
7. **Textos en chino apareciendo en pantalla:** reportado por el usuario, no investigado (no se encontró en los archivos del proyecto).

---

## Decisiones tomadas

1. **Crear `F1_ETAPA2_NORMATIVA_v10.py`** como cambio mayor (v09 → v10) con las 9 nuevas entradas v10 para retiros patrimoniales, empates diferenciales por lado y cota de terreno.
2. **Agregar campos a `data/pot-bogota/norma-override.json`** para `AAA0030JKOE`: `retiro_patrimonial_m`, `franja_patrimonial_longitud_m`, `vecino_patrimonio_por_lado`, `construccion_no_patrimonio_exenta`, `altura_vecino_derecha_m`, `altura_vecino_izquierda_m`, `empate_lateral_derecha_m`, `empate_lateral_izquierda_m`, `cota_terreno_central_m`.
3. **Filtrado por lado en el orquestador:** si la geobase indica patrimonio solo a la izquierda, mostrar solo opciones de izquierda; si solo a la derecha, solo derecha; si ambos, ambas. Nunca mostrar todas las opciones a la vez.
4. **Entrada manual condicional:** si no hay MDT disponible, activar campos manuales solo si el operador lo solicita explícitamente o el sistema confirma ausencia de dato.
5. **No asumen cero retiro ni 3 m para el empate derecho:** solicitar criterio escrito a la curaduría.

---

## Cómo se resolvieron los problemas

| Problema | Resolución |
|---|---|
| Paréntesis desbalanceado en `.format()` | Simplificado a llamadas `.format()` con argumentos nombrados, eliminando anidamiento complejo |
| `MissingMemberException: DataTree` | Creada función `_extraer_valor_gh` recursiva con `getattr(val, 'Data', None)` dentro de `try/except`, aplicada a `unwrap`, `safe_list`, `parse_gh_bool`, `numero_opcional` |
| Faltaban entradas v10 | Agregadas 9 entradas al script y al JSON de override |
| No hay mecanismo de patrimonio por lado | `vecino_patrimonio_por_lado` acepta JSON con `lado_id`, `nivel`, `patrimonio`; `construccion_no_patrimonio_exenta` acepta `{lado_id, exenta}` |
| Sin altura diferencial izquierda/derecha | Agregadas `altura_vecino_izquierda_m` y `empate_lateral_izquierda_m` |

---

## Lecciones aprendidas

1. **IronPython 2.7 no acepta type hints** (`def func(arg: type) -> type:`). Validar con `py_compile` antes de pegar en Grasshopper.
2. **Las entradas de Grasshopper llegan como `DataTree[object]`**, no como listas de Python. Siempre envolver extracción en `try/except` con `getattr(val, 'Data', None)`.
3. **No copiar código desde el chat al componente Script de Grasshopper.** Abrir el archivo directamente desde el disco (Bloc de notas o VS Code) y copiar, para evitar cortes y caracteres invisibles.
4. **Validar con Python 3 (`compile()`) antes de llevar a IronPython 2.7.** Python 3 detecta errores de paréntesis que IronPython reporta de forma críptica.
5. **El registro del vault usa formato markdown con YAML frontmatter** y notas de cierre de sesión por fecha en `60-diario/`.

---

## Puntos pendientes de esta sesión

| Pendiente | Responsable | Estado |
|---|---|---|
| Conectar las 9 entradas v10 en el canvas con sliders/panels para probar | Operador | Pendiente |
| Ejecutar el canvas y validar mensaje de salida + `alertas_patrimonio` | Operador | Pendiente |
| Implementar cambios al orquestador (`src/orquestador/servidor.py`): endpoints norma-override, pantalla de patrimonio, filtrado por lado | Desarrollo | Pendiente |
| Volver a ejecutar todo el flujo desde el principio (ArchiCAD con modelo cargado) | Operador | Pendiente |
| Validar `franja_patrimonial_longitud_m` desde MDT + selección de segmentos patrimoniales | Desarrollo/Operador | Pendiente |
| Corregir type hints en `F3_DISTRIBUCION_v03.py` (IronPython 2.7) | Desarrollo | Pendiente desde sesión anterior |
| Investigar textos en chino apareciendo en pantalla | Operador | Pendiente |

---

## Puntos pendientes de sesiones anteriores (no resueltos)

| Pendiente | Sesión origen | Estado |
|---|---|---|
| Sincronizar componente `F1_ETAPA2_LADOS_v06` en el canvas (`gh-definitions\F1_Contexto_Base-Editado_v02.ghx`) | 2026-08-24 | Pendiente |
| Configurar orquestador para generar JSON de overrides por lado | 2026-08-24 | Pendiente |
| Probar con lote AAA0240ZXJH (solo frente con setback) | 2026-08-24 | Pendiente |
| Commit de componentes trabajados | 2026-08-24 | Pendiente |
| Validación viva con ArchiCAD: ejecutar `F3_StorySync_v02.py --plan --chip AAA0030JKOE` | 2026-10-25 (ADR-024) | Pendiente |
| Conectar `zgf_m` al canvas en `F3_VOLUM_GENERADOR` | 2026-10-25 (ADR-024) | Pendiente |
| Front-end del orquestador: exponer selector de datum Z0 | 2026-10-25 (ADR-024) | Pendiente |
| Verificar persistencia de registros MCP tras reiniciar AutoClaw | 2026-10-25 | Pendiente |

---

## Archivos modificados en esta sesión

| Archivo | Cambio |
|---|---|
| `src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v10.py` | Creado (v10.0): retiros patrimoniales, empates diferenciales, cota de terreno, entradas izquierda/derecha, manejo DataTree GH |
| `data/pot-bogota/norma-override.json` | Agregados 9 campos v10 para lote `AAA0030JKOE` |

---

## Archivos entregados

- `src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v10.py` — listo para pegar en el componente Script de Grasshopper (IronPython 2.7)

---

## Próxima sesión

Continuar con:
1. Conexión manual de las 9 entradas v10 en el canvas.
2. Ejecución de prueba del canvas.
3. Implementación de cambios al orquestador.
4. Validación completa end-to-end.

---

*Sesión cerrada ordenadamente el 2026-10-26 por AutoClaw.*
