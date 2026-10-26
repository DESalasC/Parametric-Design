# Diagnostico de cotas - AAA0030JKOE

## 1. Datum
origen_sirgas.z      = 2634.521 m
ancla_canvas_local.z = 14.518 m
z_ref_m              = 2649.039 m
origen_z + ancla_z   = 2649.039 m (delta -0.0004 m)
ESTADO: OK - el datum cierra (< 0.01 m).

## 2. Z_base de ETAPA1
puntos de malla      = 118 (1 con z=0.000)
Z_base (min valido)  = 0.030 m
Z max malla          = 16.125 m

## 3. Desplazamiento aplicado por CONTEXTO50_BUILD
desplazamiento_z     = origen_z + Z_base - z_ref = -14.488 m
lote en Z local      = 0.236 .. 14.488 m (desnivel 14.25 m)
comprobacion         = z_base_m - desplazamiento_z = z_local - Z_base

## 4. Geometrias planas en ETAPA1 (z=0)
vias_oficiales     registros= 34 vertices= 4685 con z=0:  4685 (100.0%)
espacios_publicos  registros= 13 vertices= 1522 con z=0:  1522 (100.0%)
vecinos            registros= 90 vertices= 2501 con z=0:  2501 (100.0%)

## 5. Vecinos del contexto50 vs malla ETAPA1
metodo z_base        = MDT (REST Catastro) por huella: centroide + extremos (min/max x,y); z_base_m = minimo de las cotas validas
z_base_m (canvas)    = -21.150 .. -0.060 m
z_base ajustado      = -6.662 .. 14.428 m
ajuste por huella   = centroide - min: promedio 1.06 m | max 4.65 m
huellas completas en malla = 9
contraste con malla ETAPA1 (informativo: la malla es una interpolacion de 118 puntos):
  residuo z_vecino-terreno (min huella): promedio -0.18 m | min -1.35 | max 0.39 | |max| 1.35
  no es un criterio de falla: el MDT puntual y la malla IDW son dos superficies distintas.

## Veredicto
- FALLA: vias_oficiales sin cota: 100% de vertices en z=0
- FALLA: espacios_publicos sin cota: 100% de vertices en z=0
- FALLA: vecinos sin cota: 100% de vertices en z=0
- Las geometrias planas (vias/EP/vecinos ETAPA1) no pueden drapearse sin muestrear el MDT
  en sus vertices: la malla de ETAPA1 solo cubre el lote + ~5 m.
