# Análisis Multi-CHIP — Fase 1

**Fecha:** 2026-08-10
**Objetivo:** Detectar fallos en la clasificación de lados con diferentes tipologías

---

## CHIPs disponibles en cache

| CHIP | Área (m²) | Vértices | Vecinos | UPZ | Tratamiento | Altura POT |
|------|-----------|----------|---------|-----|-------------|------------|
| AAA0127AZPA | 315.0 | 10 | 53 | EL PRADO | Consolidación | 11.4 m (rango 3) |
| AAA0030JKOE | 946.5 | 31 | 90 | N/A | Conservación | ❌ Datos no parseados |
| 002407033006 | 193.9 | 10 | N/D | N/D | N/D | ❌ Sin datos POT |

---

## Hallazgos por tipología

### AAA0127AZPA — Lote irregular (9 lados)
- **Clasificación GIS:** 0 frentes, 9 laterales
- **Problema:** Calle Carrera 49 no digitalizada en Eje_vial
- **Solución:** Dibujar manualmente en ArchiCAD (capa 00-20-20)
- **Tipo:** Lote interior con un frente (en realidad da a vía)

### AAA0030JKOE — La Candelaria, Centro Histórico (30 lados)
- **Clasificación GIS:** 0 frentes, 30 laterales
- **Problema crítico:** POT GDB no pudo parsear altura. El campo ALTURA_MAXIMA tiene valor "CHB" (Centro Histórico Bogotá) en vez de número
- **Consecuencia:** Sin altura POT ni rango de edificabilidad → el script usa defaults
- **Tipo:** Lote muy irregular con múltiples frentes, pendiente significativa
- **Vecinos:** 90 predios en buffer de 75m (zona densa)

### 002407033006 — Lote pequeño (10 lados)
- **Clasificación GIS:** Sin datos
- **Problema:** Sin datos POT en absoluto
- **Tipo:** Lote pequeño (~194 m²)

---

## Problemas detectados

### 🔴 Bloqueante: POT GDB no parsea "CHB"
El campo `ALTURA_MAXIMA` en la capa `TratamientoUrbanistico` de la GDB tiene
valores no numéricos como "CHB" para predios en Centro Histórico.

**Impacto:** Cualquier lote en Centro Histórico, Conservación o sectores especiales
no tendrá altura máxima ni rango de edificabilidad del POT.

**Solución propuesta:** Agregar un mapeo de valores especiales en `fetch-urban-context-v5.py`:
```python
ALTURA_ESPECIAL = {
    "CHB": {"altura_max": 7.0, "rango": "1", "tratamiento": "Conservación"},
    # Centro Histórico: altura limitada, norma especial
}
```

### 🟡 Clasificación GIS: 0 frentes en todos los CHIPs
La capa Eje_vial del POT no contiene calles locales en zonas consolidadas.
Esto valida la decisión de ADR-008: no se puede confiar solo en datos oficiales.

### 🟡 Sin datos POT para 002407033006
Este CHIP no tiene cobertura en el POT .gdb. Puede ser un predio rural, en zona
de expansión, o con código no estándar.

---

## Recomendaciones

1. **Corregir parseo de ALTURA_MAXIMA** para manejar valores "CHB" y otros códigos alfanuméricos
2. **Priorizar dibujo manual de vías** para AAA0127AZPA (ya tiene resultados validados previos)
3. **La Candelaria requiere investigación normativa adicional** — Centro Histórico tiene restricciones especiales no capturadas en el POT estándar
4. **Agregar test automatizado** que corra fetch-urban-context para múltiples CHIPs y valide estructura JSON
