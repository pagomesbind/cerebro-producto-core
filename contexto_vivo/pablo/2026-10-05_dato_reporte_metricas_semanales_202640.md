---
id: 2026-10-05_dato_reporte_metricas_semanales_202640
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_metrics — análisis y reporte semanal, semana 202640 (28 de septiembre al 5 de octubre de 2026)"
producto: transversal
tema: Reporte narrado de métricas semanales (NSM) — semana 202640
tipo: dato
destino_propuesto: 3_recursos/datos/metricas_semanales.md
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Contenido final y completo del archivo `3_recursos/datos/metricas_semanales.md`, con la entrada de la
semana 202640 antepuesta al histórico existente (que se conserva íntegro debajo, sin alterar — partió del
espejo actual, que ya incluye hasta 202639). El archivo completo resultante está en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/metricas_semanales_completo.md` —
`/context_merge` copia ese archivo, byte a byte, sobre `3_recursos/datos/metricas_semanales.md`.

**Resumen de la entrada nueva (semana 202640, 28 de septiembre al 5 de octubre de 2026):**

- NSM#1 (Volumen API BANK): $299.554 M, WoW +79,8%, vs. baseline 13 semanas +13,8%, tendencia ventana móvil
  de 4 semanas −7,0% (sigue negativa pese al rebote semanal).
- NSM#2 (Volumen Payway): $11.701 M, WoW +47,3%, vs. baseline 13 semanas +19,7%, tendencia ventana móvil
  +1,6%.
- El salto fuerte de ambas NSM coincide con la ventana de estacionalidad confirmada (días 1-10 del mes, pico
  de cobro de servicios/facturas) — aplica fuerte y claro en NSM#2 (distribuidoras eléctricas EDEA/EDELAP/
  EDEN/EDESA/EDES todas +37/+61% WoW), más débil/no concluyente en NSM#1/Wallet.

**5 hallazgos priorizados en la entrada** (ver archivo completo para detalle): (1) rebote de inicio de mes
más flojo que los meses previos en NSM#1; (2) concentración de BSF en Wallet sube a 60,6% (top-3 87,2%);
(3) tercera cuenta de liquidación interna de Bind PSP con comportamiento errático — "cta 39" no tuvo el pico
de inicio de mes esperado (ver item de gap aparte); (4) primer chequeo post-corrección de BINes (v73,
29/9) — mejora el rechazo de Débito/Crédito en Payway, Tarjeta Prepaga sigue sin ceder (ver item de gap
aparte); (5) altas de comercios de Adquirencia traccionadas por La Virginia (96 de 134, informativo).

**Decisiones confirmadas esta semana:** ninguna sobre la definición de NSM o métricas.

**Próxima ingesta:** se pedirá el mismo lote de 8 queries la semana que viene (semana 202641, 5 → 12 de
octubre de 2026).
