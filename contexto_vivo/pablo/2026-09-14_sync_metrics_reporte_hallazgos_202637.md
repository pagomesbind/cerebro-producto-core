---
id: 2026-09-14_sync_metrics_reporte_hallazgos_202637
pm: pablo
fecha_captura: 2026-09-14
fuente: "/sync_metrics — análisis y reporte semanal, semana 202637 (7 al 14 de septiembre de 2026)"
producto: transversal
tema: Reporte narrado de métricas semanales (NSM) — semana 202637
tipo: dato
destino_propuesto: 3_recursos/datos/metricas_semanales.md
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: en_cola
---

Contenido final y completo del archivo `3_recursos/datos/metricas_semanales.md`, con la entrada de la
semana 202637 antepuesta al histórico existente (que se conserva íntegro debajo, sin alterar). El archivo
completo resultante ya está generado en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/metricas_semanales_completo.md` —
`/context_merge` copia ese archivo, byte a byte, sobre `3_recursos/datos/metricas_semanales.md`.

**Resumen de la entrada nueva (semana 202637, 7 al 14 de septiembre de 2026):**

- NSM#1 (Volumen API BANK): $322.438 M, WoW −16,8%, vs. promedio 4 semanas +21,7%, vs. baseline 13 semanas
  +26,3%, tendencia ventana móvil +3,1% (últimas 4 semanas $1.097.174 M vs. 4 previas $1.064.222 M).
- NSM#2 (Volumen Payway): $12.525 M, WoW +2,7%, vs. promedio 4 semanas +26,1%, vs. baseline 13 semanas
  +44,1%, tendencia ventana móvil −4,2% (últimas 4 semanas $40.475 M vs. 4 previas $42.263 M).
- 4 hallazgos: (1) 🔴 Tarjeta Prepaga sigue disparada y con rechazo muy por encima de lo normal — segunda
  semana consecutiva de crecimiento explosivo (+197,5% WoW, acumulado +973,9% vs. baseline 13s) combinado
  con rechazo de 42,8% (vs. 27,8% habitual), sin causa confirmada; se abre gap formal esta vez. (2) 🟡 BSF
  (Carrefour) sigue concentrando el 61,4% del volumen de Wallet (bajó de 67,5% la semana pasada, pero
  sigue siendo dependencia estructural); sigue pendiente la pregunta abierta sobre ajuste de tiempos de QR.
  (3) 🟡 El balance IN/OUT de NSM#1 se corrió hacia OUT (71,2% vs. 64,3% habitual), posiblemente reflejo de
  la volatilidad de BSF más que un cambio de fondo — a confirmar la semana que viene. (4) 🟢 El salto en
  altas de comercios de Adquirencia sigue siendo el proyecto de onboarding de La Virginia (193 altas,
  80,8% del total), no una anomalía.

**Nota operativa — `dim_collectors` sin encabezado, cuarta vez:** el export de Collectors volvió a llegar
sin fila de encabezado. Se aplicó otra vez, como workaround local, el mismo mapeo posicional confirmado por
el usuario en 2026-08-26 y reconfirmado en 2026-08-31 (Id/CollectAccountId/Name/Cuit/Psp/Cbu/Webhook/
FechaAlta/sin-identificar/Codigo/BankId/sin-identificar). Se abre un gap actualizado pidiendo que se
priorice el cambio en `pipeline.py` (vía `CEREBRO_CORE`), ya que el mapeo no tiene ninguna ambigüedad
pendiente — ver `2026-09-14_gap_dim_collectors_mapeo_confirmado_cuarta_vez` en este mismo lote.

**Email:** se generó el reporte HTML con `render_email.py` y se dejó como borrador en Gmail (asunto "Bind
PSP — Reporte semanal NSM — Semana 202637"), verificado con `list_drafts` que persistió correctamente.
