# Resumen de sesión - 2026-08-22

**Tema:** Rediseño del orquestador — inventario, interfaz, modelo F2 y contrato de datos.

## Contexto
Tras cerrar el fix de `F3_MORPH_ATRIBUTOS` (v02) en la sesión previa, esta sesión
arrancó el rediseño del orquestador: se completó la Etapa 0 (inventario de `src/`),
se definió la interfaz (cajas en una pantalla) y el modelo financiero de F2, y se
redactó el contrato de datos (`data/activo/`). Se verificó que el contrato no rompe
el cableado actual.

## Errores encontrados
1. **Post-procesado del exec:** los listados recursivos grandes fallaban en el
   post-procesado → se resolvió volcando a archivo y leyendo con `read`.
2. **`git mv` bloqueado:** mover `src/fase-1-contexto/tests/` → `tests/fixtures/archicad/`
   devolvió *Permission denied* (archivo abierto, probablemente ArchiCAD).
3. **Falso hallazgo v07:** se creyó erróneo tener `F3_VOLUM_GENERADOR_v07.py` en activo;
   es intencional (los tests "fuente" pinean la ruta activa).
4. **Bloat + acoplamiento:** `src/research/gh-definition-explorer/` tiene ~38.982 archivos
   rastreados de docs generadas; y las salidas F2/F3 (`resultados*/`, `casos/`) están
   acopladas a paths relativos de los motores.

## Modificaciones solicitadas
1. Revisar estado del proyecto y pendientes de la última sesión.
2. Leer las notas del vault (diario + plan de rediseño).
3. Inventario de `src/` + reubicación documentada (nuevas localizaciones, porqué, activas).
4. Interfaz como **cajas dentro de una sola pantalla** (no pantallas), con estados
   gris/color y señal de avance entre fases.
5. F2: reporte **PDF y HTML**, financiación del saldo (preventas / constructor / bancario),
   modalidad del dueño del lote, valores de venta editables, acabados (con obra gris),
   y mercado **zonal** con actualización periódica + un "agente" para ofertas independientes.
6. Redactar el **contrato de datos** y verificar que no rompe nada grave.
7. Cierre de sesión + commit.

## Lecciones aprendidas
1. Para listados grandes, volcar a archivo y leer con `read` evita el post-procesado.
2. Antes de mover archivos: verificar referencias (`git grep`) y locks (ArchiCAD abierto
   bloquea `git mv`).
3. Los tests "fuente" pinean rutas activas: duplicados activo + `_legacy` son intencionales.
4. Las salidas F2/F3 están acopladas a los motores por paths relativos → la reubicación
   debe ir junto al rediseño, no antes.
5. El motor F2 ya tenía acabados (`nivel_acabados`), precio/costo m² y absorción por
   escenario → el contrato **extiende**, no reemplaza.
6. Sin suscripciones a Coordenada Urbana / Galería → fuentes públicas (DANE, Banco de la
   República, Catastro, portales) + agente futuro.

## Soluciones entregadas
- Inventario de `src/` (389 archivos relevantes) + nota de reubicación.
- Nota de interfaz + modelo F2 (cajas, fuentes/operador, financiación, acabados, agente).
- Nota de contrato de datos (`data/activo/`: 6 archivos canónicos con schemas JSON).
- Verificación de compatibilidad del contrato contra las estructuras reales (nada grave).

## Pendientes de esta sesión
1. Validar el esquema con el **operador real** (cuando el orquestador funcione).
2. Crear esqueleto `data/activo/` + `data/predios/` (Etapas 1–2).
3. Definir las **zonas de mercado** y el mecanismo de scraping/descarga.
4. Migrar el código **desde F0** (orquestador → componentes → canvas).
5. Reintentar el `git mv` de las bases ArchiCAD (con ArchiCAD cerrado).
6. Cleanup de git: `src/research/` (~39k archivos) y resultados F2/F3.
7. Implementar el **agente de mercado** (futuro).

## Commits
- `docs(sesion)+fix(f3)`: cierre sesión 2026-08-22 (F3_MORPH_ATRIBUTOS v02 + docs rediseño).
- Vault: inventario, interfaz y contrato de datos del orquestador.
