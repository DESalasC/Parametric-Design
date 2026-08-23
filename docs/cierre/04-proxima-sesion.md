# Próxima sesión - puntos para continuar (2026-08-22)

Handoff para retomar en una nueva sesión. Estado consolidado tras el inicio del
rediseño del orquestador (inventario, interfaz, modelo F2 y contrato de datos).

## Estado vigente (versiones)
- F1 NORMATIVA **v08**, LADOS **v06**, canvas **F1_Contexto_Base-Editado_v02**.
- F3_VOLUM_GENERADOR **v08**, F3_MORPH_ATRIBUTOS **v02** (fix `OnPingDocument`).
- F0_LOAD_PROYECTO **v01**, F0_STORIES **v01**, F2 motores **v03**.
- `usos-por-sector.json` **v02**.
- Suite: **257 passed**.

## Terminado en esta sesión (2026-08-22)
- Fix completo de `F3_MORPH_ATRIBUTOS` (v02 restaurado + `ghenv.Component.OnPingDocument()`).
- Inventario de `src/` (Etapa 0) + nota de reubicación.
- Interfaz del orquestador (cajas en una pantalla) + modelo F2.
- Contrato de datos (`data/activo/`) con schemas JSON.
- Verificación de compatibilidad (nada grave).

## Bloqueado / pendiente (orden sugerido)
1. **Validar esquema con el operador real** (solo cuando el orquestador funcione; ahí
   surgirán dudas de presentación/organización).
2. **Esqueleto `data/activo/` + `data/predios/`** (Etapas 1–2 del rediseño).
3. **Zonas de mercado** (norte / centro / sur / periferia) + mecanismo de actualización
   periódica (DANE, Banco de la República, Catastro, portales; sin suscripciones).
4. **Migrar código desde F0**: el orquestador produce todos los JSON canónicos; las
   entradas de los componentes cambian desde F0 hasta el canvas.
5. **F2**: añadir `recursos_disponibles`, `saldo`, `financiacion_saldo[]`
   (preventas / constructor / bancario), acabados por opción y multi-escenario.
6. **Reintentar `git mv`** de `src/fase-1-contexto/tests/` → `tests/fixtures/archicad/`
   (con ArchiCAD cerrado; hoy falló por *Permission denied*).
7. **Cleanup git**: `src/research/gh-definition-explorer/` (~39k archivos de docs
   generadas) → gitignore + `git rm --cached`.
8. **Agente de mercado** (futuro): ofertas independientes (obra gris VIS, lujo,
   salud, comercio); el schema ya reserva el hueco.

## Para recordar (reglas de entorno)
- GHPython = IronPython 2.7 (sin f-strings/pathlib/type hints); componente "Script".
- `OnPingDocument` se obtiene vía `ghenv.Component`, NO `ghpythonlib.component`.
- Acceso a entradas del canvas: SIEMPRE `globals().get()`, nunca nombres desnudos.
- LAYER_MAP obligatorio = GuBIMclass, nunca `ARQ_*`.
- `_legacy` es archivo pasivo; los tests "fuente" pinean la ruta activa (duplicados
  activo + `_legacy` son intencionales).
- Derivados (resultados F2/F3, `gfa-gh.json`, `pot-cache/*`) no se commitean.
- El orquestador es el único dueño de la cadena de datos: todo se produce desde F0.

## Notas del vault (esta sesión)
- `10-arquitectura/2026-08-22-plan-rediseno-orquestador.md`
- `10-arquitectura/2026-08-22-inventario-reubicacion-src.md`
- `10-arquitectura/2026-08-22-interfaz-orquestador.md`
- `10-arquitectura/2026-08-22-contrato-datos.md`
