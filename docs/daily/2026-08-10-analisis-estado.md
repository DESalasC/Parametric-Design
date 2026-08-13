# Diagnóstico del Proyecto — 2026-08-10

**Solicitante:** Dario Salas
**Alcance:** Análisis integral del estado actual del proyecto DiseñoParametrico
**Fuentes:** Exploración completa del sistema de archivos, git log, vault, logs previos

---

## 1. Vista General

| Indicador | Estado |
|-----------|--------|
| Proyecto iniciado | 2026-06 (primeros scripts), formalizado 2026-08-01 |
| Última actividad | 2026-08-09 (sesión intensiva de debugging) |
| Commits Git | 15 commits |
| Archivos totales | ~400+ (incluyendo research, tests, docs, data) |
| Scripts Python | ~80+ (contando todas las versiones en src/ y scripts/) |
| Fase más avanzada | Fase 1 (~80% completada) |
| Fase más rezagada | Fase 4/5 BIM (0% código, solo estructura) |

---

## 2. Estado por Fase

### Fase 0 — Setup BIM ✅ COMPLETADA
- Generación XML de capas GuBIMclass para ArchiCAD
- Mapeo de capas (archicad-layer-map.json)
- Variables de entorno, estructura de carpetas, venv Python

### Fase 1 — Contexto Normativo y Lote 🔄 80%
**Pipeline actual (funcional):**
```
fetch-urban-context-v5.py → JSON cache
  └─ F1_Contexto_v07.ghx (Grasshopper)
       ├─ F1_CONTEXTO_POT_v04 → lote_curve, neighbors, topo_mesh, lados_json
       ├─ Discontinuity (nativo GH) → lot_vertices
       ├─ F1_PATIO_DISCONTINUIDAD_v02 → patios, sides_table
       └─ F1_NORMATIVA_APLICAR_v22 → retiros, huella edificable
```

**Scripts principales (versión vigente):**
| Script | v actual | Estado |
|--------|----------|--------|
| F1_CONTEXTO_POT | v04 (sistema) | ✅ Estable |
| F1_LADOS_CONFIGURAR | v07 | ✅ Clasificación por adyacencia |
| F1_PATIO_DISCONTINUIDAD | v02 | ✅ Usa Discontinuity nativo |
| F1_NORMATIVA_APLICAR | v22 | ✅ Aplica retiros + resta patios |
| F1_VECINOS_ANALISIS | v02 (sistema) | 🟡 Pendiente revisión |
| F1_VALIDADOR_CRUZADO | v01 | ✅ Funcional |

**Resultados validados para lote AAA0127AZPA:**
- UPZ El Prado, Tratamiento Consolidación
- Área: 315 m², Altura máx: 11.4 m, 4 pisos
- Patio 3.0×3.0 m, Retiro promedio 2.4 m
- Área edificable: 130.7 m², IO 0.41 (máx 0.70) ✅

**Pendiente Fase 1:**
- [ ] Regenerar JSON con fetch-urban-context-v5.py --chip AAA0127AZPA
- [ ] Verificar clasificación lados en el JSON regenerado
- [ ] Conectar F1_PATIO_DISCONTINUIDAD_v02 en canvas Grasshopper
- [ ] Validar generación de patios visualmente
- [ ] Probar con otros CHIPs (interior, esquina, pasante, irregular)
- [ ] Próximo lote: La Candelaria (AAA0030JKOE, 900+ m², pendiente, Centro Histórico)

### Fase 2 — Motor de Demanda 🟡 15%
- Scripts v01 para: DEMANDA_MOTOR, OPTIMIZADOR_ADYACENCIA, PROG_INTERIOR, PROGRAMA_AREAS
- Sin tests
- Sin integración con pipeline de Fase 1
- Sin definición Grasshopper

### Fase 3 — Generación de Masa 🟡 10%
- Scripts v01/v03 para: VOLUM_GENERADOR, PREP_LADYBUG, ACCESOS_INTEGRADOR
- Sin tests
- Referenciado en README de Fase 1 pero no conectado
- Sin definición Grasshopper

### Fase 4 — Análisis Ambiental (Ladybug) 🟡 5%
- Fase NO planeada originalmente en CLAUDE.md
- 2 scripts v01/v02 de LADYBUG_ANALISIS
- Datos climáticos Bogotá (EPW) completos ✅
- Sin integración ni tests

### Fase 4/5 — Inyección BIM (Tapir) 🔴 0%
- Confusión de numeración: existe `fase-4-bim` (tests vacíos) y `fase-5-bim` (README)
- Sin código implementado
- Tapir samples descargados como referencia en data/ghx-samples/

---

## 3. Infraestructura de Soporte

### Documentación ✅ BUENA
- 5 ADRs activos cubriendo decisiones clave
- Extractos normativos: Decreto 555, 670, NSR-10
- README por fase con pipeline documentado
- CLAUDE.md del proyecto completo y actualizado (~10 KB)
- Diario de trabajo con sesión 2026-08-09 detallada

### Datos ✅ SÓLIDOS
- POT cache para 4 predios (AAA0127AZPA, CHAPINERO-TEST, REAL-002407033006, 002407033006)
- Datos climáticos Bogotá (EPW + DDY + STAT + WEA)
- NSR-10 estructurado (amenaza sísmica, grupos de uso, separaciones)
- Lotes de ejemplo (Centro, Chapinero, Tierralinda)
- Inventarios de campos GDB y capas POT

### Scripts Utilitarios ✅ ROBUSTOS
- fetch-urban-context: evolución v1→v9, v5 es la vigente
- gpkg-to-cache: v1→v4
- Extractores normativos: Decreto 555, 670, NSR-10
- Generación capas ArchiCAD: v1→v3
- Ortofotos aéreas: v1→v6
- +15 scripts de diagnóstico/inspección

### GH Definitions 🔄 ACTIVO
- F1_Contexto_v07.ghx (839 KB) — versión actual de trabajo
- Historial: v03→v07a preservado
- 10+ iteraciones de fix_ghx (v3→v10), mayoría abandonadas
- Herramientas de diagnóstico: _check_*, _dump_*, _find_*, _test_*

### Tests 🔴 MUY DÉBIL
- 1 solo test unitario: test_patio_esquina.py (8/8 ✅)
- Directorios e2e y fixtures vacíos
- Sin tests de integración para el pipeline completo
- Sin tests para ninguno de los scripts utilitarios

---

## 4. Deudas Técnicas Identificadas

### 🔴 Críticas
1. **Falta de tests automatizados**: Solo 1 test unitario. Todo el pipeline carece de cobertura.
2. **Versiones obsoletas acumuladas**: ~40+ scripts con versiones antiguas sin limpiar (git untracked).
3. **Vecinos manuales**: Sin automatización para detección de vecinos (depende de modelado manual en ArchiCAD).

### 🟡 Moderadas
4. **Confusión de fases 4/5**: Numeración duplicada y fase ambiental no planeada.
5. **Vault desactualizado**: El diario del vault solo llega a 2026-08-01, sin registrar avances del 08-09.
6. **Sin CI/CD**: Pruebas requieren Rhino 8 runtime, sin automatización posible.
7. **fetch-urban-context con 9 versiones**: La v5 es vigente; las demás son ruido.
8. **fix_ghx con 10 iteraciones**: Solo se usa fix_ghx_v10; las demás son dead code.

### 🟢 Menores
9. **GH_IO documentation explorer**: ~200+ markdowns generados en src/research, utilidad no clara.
10. **Logs en múltiples ubicaciones**: logs/ y docs/daily/ duplican función.
11. **Inventario de migración**: CSV de 3.4 MB (interfaces_configs.csv) sin proceso documentado.

---

## 5. Riesgos del Proyecto

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Regresiones sin tests al modificar Fase 1 | Alta | Alto | Crear test suite para scripts principales |
| Dependencia de Rhino 8 (licencia, compatibilidad) | Media | Alto | Documentar versión exacta, alternativas |
| Vecinos manuales no escalan | Alta | Medio | Investigar automatización vía GIS |
| Confusión entre versiones de scripts | Media | Medio | Limpiar versiones obsoletas, mantener solo vigentes |
| Vault y proyecto desincronizados | Alta | Bajo | Sincronizar diario y documentación de fases |
| Cambios normativos POT (Decreto 555/670) | Baja | Alto | Versionar datos normativos, documentar fuente |

---

## 6. Métricas

| Métrica | Valor |
|---------|-------|
| Días desde inicio formal | 9 días (2026-08-01 → 08-10) |
| Commits git | 15 |
| Scripts Python totales | ~80 (incluye versiones obsoletas) |
| Scripts vigentes estimados | ~20 |
| GH Definitions activas | 1 (F1_Contexto_v07.ghx) |
| Tests unitarios | 1 (8 assertions) |
| Cobertura de tests | <1% |
| ADRs documentados | 5 |
| Predios con cache POT | 4 |
| Modelos Ollama disponibles | 7 |
