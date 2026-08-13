# ADR-008: Clasificación Espacial Híbrida — Feedback Loop ArchiCAD ↔ Grasshopper

**Fecha:** 2026-08-10
**Estado:** Aceptado
**Reemplaza:** Clasificación por adyacencia con vecinos (ADR-007, sección lados)

---

## Contexto

La geodatabase oficial del POT (bd_uaecd.gpkg, capa Eje_vial) tiene huecos documentados:
calles reales de la malla vial local que no están digitalizadas. Lo mismo ocurre
con las alturas de vecinos en la capa Predio/Lote.

Confiar ciegamente en datos gubernamentales incompletos para decisiones críticas
de proyecto (retiros, frentes, patios) produce resultados incorrectos.

## Decisión

Adoptar un **enfoque híbrido de clasificación espacial** con feedback loop
ArchiCAD → Grasshopper:

### Regla de clasificación (reemplaza adyacencia por vecinos)

Un borde del lote es **"Frontal"** si la distancia mínima desde cualquier punto
del segmento hasta alguna curva de vía es **< 15 metros**.

Si no hay vía cerca, el borde es **"Lateral"** o **"Posterior"** según su
posición relativa en el polígono (posterior = opuesto al frente principal).

### Fuentes de curvas de vía (combinadas vía Merge en GH)

1. **Datos oficiales**: `vias_curves` del JSON generado por `F1_CONTEXTO` (capa Eje_vial del POT)
2. **Retroalimentación manual**: Curvas dibujadas en ArchiCAD en capas específicas, traídas a Grasshopper vía Tapir

### Feedback Loop

```
ArchiCAD                          Grasshopper
─────────                         ───────────
Dibujar calles faltantes    ──→   Tapir recibe curvas
(en capas 70-30-20,                  │
 00-20-20, 70-50-10)                 ├── Merge (oficial + manual)
                                     │
                              F1_NORMATIVA_APLICAR
                              ┌─ Clasifica bordes (regla 15m)
                              ├─ Aplica retiros diferenciados
                              ├─ Resta patios
                              └─ Calcula huella edificable
                                     │
Resultados visibles          ←──   Tapir envía geometría
en ArchiCAD                         a capas de proyecto
```

### Capas ArchiCAD para el feedback loop

| Capa | Uniclass | Propósito |
|------|----------|-----------|
| `70-30-20_Andenes_preexistentes` | EF_70_30_20 | Andenes existentes |
| `70-50-10_Zonas_verdes_publicas` | EF_70_50_10 | Parques, separadores, zonas verdes |
| `00-20-20_Foto_Aerea_Referencia` | Ac_10_30 | Imagen satelital de referencia (50% transparencia) |
| `00-20-20_Elementos_entorno_urbano_preexistente` | Ac_10_30 | Calles faltantes, elementos del contexto real |

**Nota sobre nomenclatura:** Usar guiones medios `-` en vez de puntos `.` porque
ArchiCAD tiene problemas con la sintaxis `xx.xx.xx`. Formato: `XX-XX-XX_Nombre`.

### Imagen aérea

La ortofoto se obtiene con `fetch-aerial-photo-v6.py` y se coloca en la capa
`00-20-20_Foto_Aerea_Referencia` como fondo de referencia para verificar
alineación de andenes, zonas verdes y calles dibujadas manualmente.

## Consecuencias

**Positivas:**
- Resultados basados en la realidad física del predio, no en datos incompletos
- El arquitecto tiene control total sobre la clasificación corrigiendo lo que falte
- La regla de 15m es simple, determinista y auditable
- La ortofoto permite verificar visualmente el dibujo manual

**Negativas:**
- Requiere trabajo manual inicial por predio (dibujar calles/andenes faltantes)
- El feedback loop añade un paso al flujo de trabajo
- La ortofoto requiere conexión a servicios IDECA/Catastro

**Riesgos mitigados:**
- Calles no digitalizadas → se dibujan manualmente
- Alturas de vecinos faltantes → se miden/estiman en ArchiCAD
- Clasificación incorrecta de frentes → regla física determinista de 15m

## Referencias

- Decreto 555/2021 — POT Bogotá
- Uniclass 2015 — Sistema de clasificación BIM
- GuBIMclass v3 — Adaptación colombiana de Uniclass
