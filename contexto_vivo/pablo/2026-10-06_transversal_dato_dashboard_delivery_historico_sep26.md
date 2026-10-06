---
id: 2026-10-06_transversal_dato_dashboard_delivery_historico_sep26
pm: pablo
fecha_captura: 2026-10-06
fuente: "/dashboard_delivery — 'Histórico Tickets Publicados Jira.xlsx' actualizado por el PM del equipo de desarrollo con lo publicado en septiembre 2026"
producto: transversal
tema: Delivery — histórico actualizado con Septiembre 2026 (AD + WS) y costos Sep'26 provisorios
tipo: dato
destino_propuesto: 3_recursos/datos/
tipo_destino: reemplazar(solo tipo:dato)
contradice: "3_recursos/datos/log_performance_desarrollo.md — Sep'26 pasa de AD 3 SP (parcial) a AD 91,5 SP; Oct–Dic'25 se mantienen sin cambio (decisión 2026-09-29)"
confianza: media
estado: en_cola
merge_commit:
---

Contenido final de los stores en `wiki/1_proyectos/contexto_vivo/_staging_dashboard_delivery/` (`log_performance_desarrollo.md`, `log_costos_desarrollo.md`, `log_sla_highest.md`) — copiar byte a byte a `3_recursos/datos/`. SLA sin cambios de datos.

**Delivery:** reingesta del export histórico (802 filas; 17 excluidas por Estado; 2 tickets sin SP: WS-1257, WS-1417). Sep'26 queda en AD 37 tk / 91,5 SP, WS 15 tk / 71,75 SP (total 52 tk / 163,25 SP; antes AD 3 SP parcial). Total acumulado: 1122 tk / 3484,5 SP. Ene–Ago'26 sin cambios vs. el canon.

**Decisión mantenida (2026-09-29):** Oct–Dic'25 conservan los valores previos del canon (Oct 212 SP, Nov y Dic sin tocar), porque el export nuevo vuelve a diferir en esos meses (Oct AD 0 SP, Nov WS 130, Dic AD 143 / WS 84,5). Se restauraron del canon antes de empaquetar.

**Costos Sep'26 — PROVISORIO:** el PM aún no tiene el stock de horas de septiembre; por instrucción suya se asumió igual a Agosto (4880 hs / $233.280; AD 2600, OB 80, SER 80, WS 2120; tarifas heredadas de Agosto). Hay que reemplazarlo cuando llegue el stock real de Sep'26 (ver tarea en `1_proyectos/tareas.md`).

**Corrección técnica:** los nombres de Epic de Sep'26 venían con codificación rota en el Excel (ej. "BotÃ³n"); se repararon a UTF-8 antes de empaquetar.
