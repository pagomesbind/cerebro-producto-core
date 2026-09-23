---
id: 2026-09-22_dato_reporte_metricas_semanales_202638
pm: pablo
fecha_captura: 2026-09-22
fuente: "/sync_metrics — análisis y reporte semanal, semana 202638 (14 al 21 de septiembre de 2026)"
producto: transversal
tema: Reporte narrado de métricas semanales (NSM) — semana 202638
tipo: dato
destino_propuesto: 3_recursos/datos/metricas_semanales.md
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Contenido final y completo del archivo `3_recursos/datos/metricas_semanales.md`, con la entrada de la
semana 202638 antepuesta al histórico existente (que se conserva íntegro debajo, sin alterar). El archivo
completo resultante ya está generado en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/metricas_semanales_completo.md` —
`/context_merge` copia ese archivo, byte a byte, sobre `3_recursos/datos/metricas_semanales.md`.

**Resumen de la entrada nueva (semana 202638, 14 al 21 de septiembre de 2026):**

- NSM#1 (Volumen API BANK): $197.263 M, WoW −38,8%, vs. promedio 4 semanas −28,1%, vs. baseline 13 semanas
  −24,3%, tendencia ventana móvil +4,2% (últimas 4 semanas $1.114.648 M vs. 4 previas $1.069.240 M).
- NSM#2 (Volumen Payway): $8.198 M, WoW −34,5%, vs. promedio 4 semanas −19,0%, vs. baseline 13 semanas
  −11,1%, tendencia ventana móvil −3,1% (últimas 4 semanas $41.014 M vs. 4 previas $42.319 M).
- 4 hallazgos: (1) 🔴 Caída generalizada de volumen en ambas NSM, pareja en casi todas las líneas (no
  concentrada en un cliente), coincide temporalmente con dos despliegues de riesgo en Producción esta
  semana — actualización masiva de domicilios en cuentas Wallet (15/9, ~491K registros) y pase a
  producción de Pagos FX/W72.3 (17/9, con riesgo explícito de conciliación de transferencias sin
  herramienta operativa). Sin confirmación causal todavía — se abre gap. (2) 🔴 BSF sigue concentrando el
  55,6% del volumen de Wallet (top-3 82,0%) — mismo riesgo estructural ya conocido, bajó desde el 67,5%
  de la semana pasada. (3) 🟡 Tarjeta Prepaga entra en su tercera semana consecutiva de crecimiento
  explosivo (tendencia +46,5%/semana, acumulado +343,3% vs. baseline 13s) y rechazo muy alto (43,2% vs.
  30,5% histórico) — gap ya abierto desde el 2026-09-14, sigue sin respuesta de Adquirencia. (4) 🟢 Altas
  de comercios de Adquirencia en alza estructural, explicadas por el onboarding PJ de La Virginia (72,5%
  de las altas de la semana) — informativo, sin acción.

**Decisiones confirmadas esta semana:** ninguna sobre la definición de NSM o métricas.

**Próxima ingesta:** se pedirá el mismo lote de 8 queries la semana que viene (202639).
