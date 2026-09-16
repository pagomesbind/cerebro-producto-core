---
id: 2026-09-16_transversal_dato_dashboard_delivery_historico_jul26_ago26
pm: pablo
fecha_captura: 2026-09-16
fuente: "/dashboard_delivery — export histórico consolidado de tickets (oct'25-ago'26) + stock de horas Fintexa jul'26 y ago'26"
producto: transversal
tema: Actualización del log de delivery y costos — reload histórico oct'25-jun'26 + jul'26/ago'26 nuevos
tipo: dato
destino_propuesto: 3_recursos/datos/
tipo_destino: reemplazar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Contenido final y completo de `3_recursos/datos/log_performance_desarrollo.md` y `3_recursos/datos/log_costos_desarrollo.md`, ya generado en `wiki/1_proyectos/contexto_vivo/_staging_dashboard_delivery/` (más `log_sla_highest.md`, idéntico byte a byte al ya mergeado — sin cambios esta corrida, incluido solo porque el pipeline reescribe los 3 juntos). `/context_merge` copia esos 3 archivos, byte a byte, sobre `3_recursos/datos/`.

**Qué cambió:**

- **Delivery (`log_performance_desarrollo.md`):** el PM dejó de mandar el Excel mensual incremental y pasó a mandar, en cada invocación, el **export histórico consolidado completo** de Jira (formato nuevo: Mes numérico + columna Año propia + columna Estado, en vez del texto en español sin año de antes). Esta corrida reemplazó por completo oct'25–jun'26 (9 meses, antes cargados con datos de fuentes anteriores) y sumó jul'26 y ago'26 como nuevos. Total histórico acumulado: 942 tickets / 2.891 SP (AD + WS), jul'25–ago'26.
- **Costos (`log_costos_desarrollo.md`):** se sumó el stock de horas de julio 2026 (5.428 hs / $264.952) y agosto 2026 (4.880 hs / $233.280), ambos con tarifa propia (no heredada).
- **Reconciliación histórica, ya confirmada por el usuario en la sesión que generó este item (no es una contradicción abierta):** para los 9 meses reemplazados (oct'25–jun'26), los totales de SP cambiaron bastante respecto de lo que había cargado antes — a veces +100% (ej. nov'25: 47→99 tickets), a veces -60% (ej. jun'26: 67→31 tickets), sin un patrón sistemático hacia un solo lado. El usuario confirmó explícitamente que el export histórico consolidado es la fuente correcta y autorizó el reemplazo completo — se documenta acá solo para que quede trazable si alguien nota el salto de cifras más adelante.
- **Regla nueva aplicada:** el export histórico trae de todo (Bloqueado, EN QA, etc.), no solo lo publicado — se filtró a Estado ∈ {Finalizada, No aplica} antes de sumar (5 filas excluidas esta corrida, todas de agosto 2026).

**Dashboard regenerado** (`outputs/dashboard_performance_desarrollo.html`, no es canon): "Pulso de Delivery", el rediseño de una sola línea con selector de métrica/ventana móvil/espacio aprobado por el usuario en la misma sesión — reemplaza el dashboard anterior de 6 pestañas. Verificado sin errores de consola contra los datos reales de esta ingesta.

**Raw rotado** a `4_archivos/historial_raw/2026-09_reporte_pm_metricas_publicadas/` (el Excel histórico) y `4_archivos/historial_raw/2026-09_backfill_stock_horas_fintexa/` (los 2 Excel de stock de horas). `raw/` no quedó vacía: quedaron `BINES_T1952 (4).TXT` y `SharedIssuerIdentificationDB (2).xlsx`, ajenos a esta skill (no matchean ningún formato conocido — `[ABORT-ARCHIVO]` en el log de la corrida) — no se tocaron, a confirmar con el usuario si son de otra tarea.
