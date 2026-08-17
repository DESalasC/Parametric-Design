# Fase 1 — Contexto Normativo y Lote

Establece el contexto normativo completo del lote (POT Decreto 555/2021 + NSR-10), clasifica los
lados, aplica retiros y patios, y genera la envolvente edificable máxima para Fase 2.

## Pipeline modular vigente (v26, dos etapas)

### ETAPA 1 — Datos en bruto → ArchiCAD (clasificación manual)
```
fetch-urban-context-v6 (scripts/utilities) → data/pot-cache/<CHIP>-contexto.json
  → F1_ETAPA1_CONTEXTO_v02.py (GH: geometría + layers ArchiCAD vía Live Connection;
     garantiza el layer 00-00-10_Lote_proyecto, salida layer_lote_ok)
  → MANUAL en ArchiCAD: clasificar vías, ejes, andenes, zonas verdes, vecinos (Morph)
```

### ETAPA 2 — Geometría clasificada → ocupación y patios
```
ArchiCAD (layers) → Live Connection GetElements → GH
  → F1_ETAPA2_LADOS_v06.py      (clasificación: laterales por vértices coincidentes
                                 con vecinos <0.10 m + contacto mínimo por longitud
                                 (fracción ≥0.30); Esq por contacto real; Posterior SOLO
                                 cuando todos los lados menos uno colindan con vecinos;
                                 ancho de vía TOTAL del perfil vial — incluye andenes)
  → F1_ETAPA2_PATIO_v02.py      (patios de aislamiento en vértices vecino-vecino)
  → F1_ETAPA2_NORMATIVA_v08.py  (retiros por clasificación + tipología Continua/Aislada
                                 + antejardín por ancho de vía (CU-5.5/regla histórica)
                                 + posterior tabla Consolidación por pisos + empate
                                 volumétrico; IO/IC/altura/GFA; ENVOLVENTE ESCALONADA:
                                 retiro lateral en pisos superiores = max(empate Anexo 5
                                 SECCION 1.9.c — 1/5 de la altura desde el nivel de empate,
                                 min configurable 3,0 m; separación sísmica NSR-10 A.6.5 —
                                 2% × h en >3 pisos) solo en lados Lateral (vecino);
                                 Frontales (vía) y EspacioPublico no se escalonan;
                                 VECINOS CON ALTURAS VARIABLES por lateral (v08: entrada
                                 vecinos_por_lado_json, retiro por sub-segmento — SECCION
                                 1.9.c por vecino; recorte por semiplanos robusto en
                                 cóncavos; sin la entrada = comportamiento v07);
                                 salidas envelope_por_piso + retiros_por_piso)
  → envelope_curve → Fase 3 (VOLUM_GENERADOR)
  → F1_OVERRIDE_USO_v01.py      (opcional: override de uso del operador, USO-MULTIPLE)
  → F1_EXPORTAR_GFA_v02.py      (auto-write: data/fase-2-demanda/<CHIP>-gfa-gh.json)
  → Fase 2 (F2_DEMANDA_MOTOR_v03 / F2_RENTA_MOTOR_v03; hook si no llega --gfa)
```

**Vigentes:** `F1_ETAPA1_CONTEXTO_v02` · `F1_ETAPA2_LADOS_v06` · `F1_ETAPA2_PATIO_v02` ·
`F1_ETAPA2_NORMATIVA_v08` · `F1_LAYERS_XML_v02` (merge defensivo de capas críticas) ·
`F1_EXPORTAR_GFA_v02` · `F1_OVERRIDE_USO_v01` (opcional).
El resto del linaje (patios discontinuidad, análisis de vecinos, validador cruzado, desplazar
origen, vértice cercano) se archivó en `_legacy/` el 2026-08-15; no usar en definiciones nuevas.

**Entradas nuevas de NORMATIVA_v08 (canvas):** `tipologia` (Continua/Aislada, default
Continua), `ancho_via_m` (medido entre andenes; default → antejardín 3,00m con aviso),
`antejardin_m` (override con el valor oficial del mapa CU-5.5, Resolución SDP 1631/2023),
`empate_posterior_pisos` (≥3 activa empate volumétrico, Anexo 5 §5.4.c),
`altura_vecinos_m` (altura global de colindantes; default 0 = sin escalonamiento + aviso),
`empate_lateral_min_m` (default 3,0), `nsr10_separacion_coef` (default 0,02),
`voladizo_frontal_m` (override del voladizo frontal, SECCION 1.13.b; default auto
por perfil vial: ≤6 m no se permite; >6-10 → 0,60; >10-15 → 0,80; >15-22 → 1,00;
>22/arterial → 1,50; aplica en pisos 2+, solo lados Frontal; cuenta en GFA, no en
ocupación; prohibido sobre parques/EEP y aislamientos laterales) y
`vecinos_por_lado_json` (v08: vecinos con alturas VARIABLES por lateral —
`{"<id_lado>": [altura, ...]}` o `{"lados": [{"id": .., "vecinos": [{"altura_m": ..}]}]}`;
retiro de empate POR SUB-SEGMENTO, SECCION 1.9.c; sin la entrada = v07).
**Salidas nuevas:** `envelope_por_piso` (curvas por piso, GFA = Σ áreas), `retiros_por_piso`
(JSON por piso); `envelope_curve` se conserva = envolvente del piso 1 (compat F3).
Caso A estimado (vecinos 2 pisos): GFA escalonado ≈ 894,5 m² (−38,8% vs. hook 1.461,1);
ver `scripts/utilities/estimar_gfa_escalonado.py` y
`20-fases/fase-1-contexto/2026-08-16-normativa-escalonamiento-v07.md`.

## Archivo

El linaje anterior (`F1_CONTEXTO_POT_*`, `F1_LADOS_CONFIGURAR_*`, `F1_LADOS_CLASIFICAR_*`,
`F1_NORMATIVA_APLICAR_*`, `F1_NORMATIVA_DIRECTA_*`, `F1_NORMATIVA_LEER_*`, `F1_PATIO_ESQUINA_*`,
`F1_PATIO_VECINO_*`, `F1_PATIO_DIRECTO_*`, `F1_NEW_LAYERS_*`) se archivó en **`_legacy/`**
(2026-08-13) y **no debe usarse** en definiciones nuevas. El 2026-08-15 se sumaron a `_legacy/`
los utilitarios `F1_PATIO_DISCONTINUIDAD_v01/v02/v03`, `F1_VECINOS_ANALISIS_v01(+_sistema)`,
`F1_VECINOS_ANALISIS_v02_sistema`, `F1_VALIDADOR_CRUZADO_v01`, `F1_DESPLAZAR_ORIGEN_v01` y
`F1_VERTICE_CERCANO_v01` (git mv). No eliminar: contiene el historial.

## Tests

```powershell
pytest tests\   # tests/test_fetch_contexto.py, test_normativa_calculos.py, test_patio_esquina.py
```

## Resultados lote AAA0127AZPA (Fase 1)

| Parámetro | Valor |
|---|---|
| CHIP / UPZ | AAA0127AZPA · El Prado |
| Tratamiento | Consolidación |
| Área lote | 315–450 m² (según fuente) |
| Altura POT | 11,4 m · 4 pisos (entrepiso 2,85 m) |
| GFA Fase 1 | 632,7 m² (verificado) — **alternativa curaduría: 1054,49 m²** (ver `data/fase-2-demanda/`) |
| Patio de esquina | 3,0 × 3,0 m (lotes < 500 m², Continua, ≤ 5 pisos) |

## Documentación

Vault de Obsidian → `20-fases\fase-1-contexto\` (especificaciones del canvas, resúmenes de sesión)
y `10-arquitectura\` (pipeline-modular-fase1-v25, guías GHX, ADR-008).
