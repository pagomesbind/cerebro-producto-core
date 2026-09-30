---
id: 2026-09-28_dato_reporte_metricas_semanales_202639
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_metrics — análisis y reporte semanal, semana 202639 (21 al 28 de septiembre de 2026)"
producto: transversal
tema: Reporte narrado de métricas semanales (NSM) — semana 202639
tipo: dato
destino_propuesto: 3_recursos/datos/metricas_semanales.md
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 3492d04
---

Contenido final y completo del archivo `3_recursos/datos/metricas_semanales.md`, con la entrada de la
semana 202639 antepuesta al histórico existente (que se conserva íntegro debajo, sin alterar — partió del
espejo actual, que ya incluye 202638). El archivo completo resultante está en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/metricas_semanales_completo.md` —
`/context_merge` copia ese archivo, byte a byte, sobre `3_recursos/datos/metricas_semanales.md`.

**Resumen de la entrada nueva (semana 202639, 21 al 28 de septiembre de 2026):**

- NSM#1 (Volumen API BANK): $166.577 M, WoW −15,6%, vs. baseline 13 semanas −36,6%, tendencia ventana
  móvil +3,5% (últimas 4 semanas $1.073.666 M vs. 4 previas $1.037.180 M).
- NSM#2 (Volumen Payway): $7.942 M, WoW −3,1%, vs. baseline 13 semanas −16,9%, tendencia ventana móvil
  −3,2% (últimas 4 semanas $40.863 M vs. 4 previas $42.223 M).
- 6 hallazgos: (1) 🟡 la caída de 202638–202639 es el ciclo intra-mes (pico primera semana, valle al
  cierre) — contra la semana equivalente de agosto, Payway −1,9% y 202638 incluso arriba en ambas NSM; esto
  **reencuadra el hallazgo 1 de 202638** (caída asociada a despliegues del 15/9 y 17/9). Lo que sí se mueve:
  el valle de fin de mes de Wallet es cada vez más profundo (Operaciones Wallet $95.074 M vs. $140.235 M
  en 202635 y $182.425 M en 202631; BSF y Sociedad Militar). (2) 🟡 Credicuotas corre volumen de Wallet
  (−29% en ventana) a Agente de Cobros ($74.715 M vs. $11.483 M en ventana), en la misma semana en que se
  apagó Bind PSP liquidaciones cta 2 — sin confirmar si es migración. (3) 🔴 BSF 57,6% de Wallet, top-3
  83,0%. (4) 🟡 Tarjeta Prepaga cuarta semana (rechazo 37,8% vs. 32,9%) y rechazo Débito subiendo (20,2%
  vs. 16,7%) — correlacionar con el despliegue de v73 (BINes, PRD-251) del 29/09. (5) 🟡 altas de cuentas
  Wallet caen por cuarta semana (20.469, −19% vs. semana equivalente de agosto, z=−2,44). (6) 🟢 altas de
  comercios en alza por La Virginia (118 de 194).

**Decisiones confirmadas esta semana:** ninguna sobre la definición de NSM o métricas.

**Próxima ingesta:** semana 202640 (28/9 → 5/10), mismo lote de 8 queries.
