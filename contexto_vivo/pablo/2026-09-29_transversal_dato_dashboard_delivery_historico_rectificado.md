---
id: 2026-09-29_transversal_dato_dashboard_delivery_historico_rectificado
pm: pablo
fecha_captura: 2026-09-29
fuente: "/dashboard_delivery — 'Histórico Tickets Publicados Jira.xlsx' rectificado por el PM del equipo de desarrollo (reemplaza al export del 2026-09-16, que traía errores)"
producto: transversal
tema: Delivery — histórico de tickets publicados rectificado (Oct 2025 – Sep 2026, AD + WS)
tipo: dato
destino_propuesto: 3_recursos/datos/
tipo_destino: reemplazar(solo tipo:dato)
contradice: "3_recursos/datos/log_performance_desarrollo.md — el histórico del 2026-09-16 queda corregido en Oct'25–Ago'26 (ver cuerpo)"
confianza: alta
estado: ingestado
merge_commit: 3492d04
---

Contenido final de los stores en `wiki/1_proyectos/contexto_vivo/_staging_dashboard_delivery/` (`log_performance_desarrollo.md`, `log_costos_desarrollo.md`, `log_sla_highest.md`) — copiar byte a byte a `3_recursos/datos/`. Costos y SLA sin cambios de datos.

**Qué cambió:** reingesta del export histórico rectificado (767 filas; 16 excluidas por Estado; 2 tickets sin SP: WS-1417, WS-1257) para Ene'26–Sep'26 (+ Sep'26 nuevo: AD 3 SP, WS 71,75 SP).

**Decisión del usuario (2026-09-29):** Oct'25–Dic'25 (AD y WS) se mantienen con los valores previos al nuevo export (Oct 212 SP, Nov 261,5, Dic 323), porque el export nuevo difería de la fuente por versión (Ago'25–Dic'25) y traía dudas (Oct'25 AD con 0 SP, sin Oct'25 WS ni Nov'25 AD). Esos valores previos tampoco coinciden del todo con la fuente por versión que pasó el usuario (Oct 180, Nov 249, Dic 267 SP); queda a resolver cuál fuente es la verdad para Oct–Dic'25.

Total acumulado resultante: 1087 tk / 3396 SP. Cambios vs. el histórico del 16-sep en Ene–Ago'26: Ene 255→139,75, Feb 247,25→172, Mar 152→424,75, Abr 132→277,5, May 52,5→43,25, Jun 45→217,5, Jul 32,25→60,25, Ago 219,5→230,75.
