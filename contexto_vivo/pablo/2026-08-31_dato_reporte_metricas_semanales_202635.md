---
id: 2026-08-31_dato_reporte_metricas_semanales_202635
pm: pablo
fecha_captura: 2026-08-31
fuente: "/sync_metrics — análisis y reporte semanal, semana 202635 (24 al 31 de agosto de 2026)"
producto: transversal
tema: Reporte narrado de métricas semanales (NSM) — semana 202635
tipo: dato
destino_propuesto: 3_recursos/datos/metricas_semanales.md
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

Contenido final y completo del archivo `3_recursos/datos/metricas_semanales.md`, con la entrada de la
semana 202635 antepuesta al histórico existente (que se conserva íntegro debajo, sin alterar). El archivo
completo resultante ya está generado en
`wiki/1_proyectos/contexto_vivo/_staging_sync_metrics/metricas_semanales_completo.md` —
`/context_merge` copia ese archivo, byte a byte, sobre `3_recursos/datos/metricas_semanales.md`.

**Resumen de la entrada nueva (semana 202635, 24 al 31 de agosto de 2026):**

- NSM#1 (Volumen API BANK): $207.559 M, WoW +15,4%, vs. promedio 4 semanas −22,4%, vs. baseline 13 semanas
  −15,3%, tendencia ventana móvil +4,6% (últimas 4 semanas $1.037.180 M vs. 4 previas $991.843 M).
- NSM#2 (Volumen Payway): $8.094 M, WoW +5,7%, vs. promedio 4 semanas −23,5%, vs. baseline 13 semanas
  +3,4%, tendencia ventana móvil +21,5% (últimas 4 semanas $42.223 M vs. 4 previas $34.755 M).
- 4 hallazgos: (1) 🟢 Terra Blockchain: la caída de 5 semanas consecutivas queda resuelta — el usuario
  confirmó que el cliente fue dado de baja por Compliance (no un caso de churn); se cierra el gap abierto
  desde el 2026-08-04 y se retira la tarea de escalación T-036 (los hallazgos de esta skill son
  informativos, no generan tareas de seguimiento por sí solos). (2) 🟢 Sociedad Militar: el
  salto semanal (+175,9%) no es ruido — la tendencia 4×4 confirma un crecimiento real y sostenido
  (+40,3%), ya es la segunda organización en volumen de Wallet. (3) 🟡 Concentración estructural
  reforzada: BSF + Sociedad Militar + Global 66 explican el 85,5% de Wallet, aunque BSF individualmente
  está estable (tendencia +0,2%). (4) 🟡 La Virginia sigue explicando casi todas las altas de comercios de
  Adquirencia — sexta semana consecutiva del mismo patrón (88,8% esta semana), ya ligado al proyecto
  activo de onboarding PJ de este cliente.

**Metodología aplicada esta corrida — validación cruzada de "caída/crecimiento de cliente" con tendencia
4×4 semanas.** Siguiendo la decisión del usuario del 2026-08-26 (`[[2026-08-26_decision_metodologia_caida_cliente_ventana_movil]]`,
todavía sin implementar en `pipeline.py`), se recalcularon a mano los 16 candidatos de "Caída de cliente"
que arrojó el detector automático (semana vs. promedio de 4 semanas previas) contra la metodología más
robusta (acumulado de últimas 4 semanas cerradas vs. 4 previas). Resultado: **15 de los 16 candidatos eran
ruido de una sola semana** (ej. "Bind PSP liquidaciones cta 39" cayó −92,6% en la comparación semanal pero
en realidad viene **+81,6%** en la tendencia 4×4) — solo Terra Blockchain se confirmó como caída real y
sostenida en ambas metodologías. Este chequeo evitó reportar ~14 falsas alarmas de clientes en el reporte
y el email de esta semana.

**Corrección post-borrador (2026-08-31, mismo día):** el borrador de email y la primera versión de este
reporte se armaron con el hallazgo de Terra Blockchain todavía en tono de escalación ("sigue sin
confirmar, sube la urgencia"). Al preguntarle al usuario si correspondía subir la urgencia, confirmó que
el cliente ya fue dado de baja por Compliance — se corrigió el hallazgo (wiki y email) para reflejar el
cierre, y se retiró la tarea T-036 de `1_proyectos/tareas.md`. **Feedback del usuario, aplicable a toda
corrida futura de esta skill:** los hallazgos de `/sync_metrics` son informativos — no crear tareas de
seguimiento en `tareas.md` a partir de ellos.

**Email:** borrador de Gmail creado, actualizado con la corrección de Terra Blockchain, y confirmado
presente en `list_drafts` — pendiente de revisión y envío manual por el usuario.
