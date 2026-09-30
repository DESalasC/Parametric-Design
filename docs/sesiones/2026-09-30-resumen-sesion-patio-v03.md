# Resumen de sesión — 2026-09-30 — Patio v03 (bifurcación + AUTO), restauración del par v12 y renombres de lectores

**Cierre completo (acta + diario + lecciones):** vault `D:\Work\NOTES\obsidian-vault\` → `10-arquitectura/2026-09-30-acta-sesion-cierre-patio-v03-bifurcacion.md` · `60-diario/2026-09-30.md` · `50-lecciones/2026-09-30-*` (3).

## Situación encontrada
- Prueba del operador con `F1_CONTEXTO_v12` (Test 07, chip AAA0030JKOE, 946.45 m²): bloqueo normativo (`PATIO Generados: 0 → NORMATIVA Ocupacion >= Area bruta`) y 3D sin terreno/linderos/vecinos.
- El `.ghx` de la carpeta había sido **sobrescrito por la sesión de la mañana** (sin rama 3D); el `.gh` del build (29-09 19:42) estaba intacto. Instrucción: usar el par del build.
- Reproducción offline: **V0 = esquina reflex** → "patio en V0 no valida"; patios=0 → error de NORMATIVA.

## Decisiones y ejecución
1. **Restauración del par v12** desde git (hash verificado; timestamps sincronizados; `.bak` de la versión de la mañana).
2. **PATIO v03.0 → v03.1**: bifurcación `n_volumenes` (único vs MULTI) + **AUTO** (0/vacío → `min(esquinas válidas, capacidad=round(área/300 m²))`; V_N preferente, anclaje alternativo si no valida). Slider **#166** default **0 = AUTO**. Export F1.5 ampliado.
3. **Diseño futuro documentado**: volumen aislado → retiros + lista 0..N (vacía/separaciones); patios interiores `n_int = max(0, ceil(A_piso/300)-1)` (v03.2); interfaz futura `zonas_patio_json` (retroalimentación de "Zonas").
4. **Renombres lectores AC**: `#36-Predio`, `#43-Vias`, `#44-Verdes`, `#45-Vecinos`, `#46-andenes` (mapeo trazado por GUID).
5. **Conexión/apps**: Rhino/ArchiCAD cerrados; AutoClaw en 19723; guía de arranque documentada; reporte 19723 pendiente de decisión.

## Evidencia
- Tests: `test_patio_v03_bifurcacion.py` 12/12; suite raíz 338/338; fase-1 56/56.
- Smoke real: `AUTO | inferido: 3 (esquinas válidas 3 · capacidad 3) | Anclas: V1, V2, V5`.
- Canvas: 331 objetos; 0 duplicados; 0 sources sin resolver; round-trip GH_IO OK; par sincronizado **30-09 10:33**.
- Commits: `64023e13` · `b76ac79c` · `026b851f` + cierre.

## Pendientes de esta sesión
1. Validación viva del par v12 (AUTO; NORMATIVA; rama 3D; exports; revisar LADOS `Ancho via: 0.00m`).
2. v03.2 patios interiores + interfaz Zonas.
3. Confirmar staleness de `KeyError 'eficiencia_nga'` (`Errores-DP.txt`) y de `Invalid Curve value… horizontal plane` con el par nuevo.
4. Decisión re-envío reporte 19723.

## Pendientes anteriores (resumen)
NORMATIVA v09 (ADR-022); P2/P3 Candelaria (ETAPA4_TERRENO, PLATAFORMAS, MULTIVOLUMEN/VOLUM v09, ACCESOS v03); capas de Morphs en ArchiCAD; datasets mix B; retirar `patch-ghx-contexto50-defensiva.py`; LADOS v07; 19723; agentes/ADR-015; fcc-sanitizer; Revit/AutoCAD; Dropbox/H:; MiMo-Flash-RL; ComfyUI.

## Listo para la próxima sesión
- Abrir `gh-definitions\F1_CONTEXTO_v12.gh` (par 30-09 10:33) → F5 → AUTO → 3 patios → NORMATIVA OK → exports → 3D.
