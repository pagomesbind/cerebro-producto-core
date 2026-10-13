---
id: 2026-10-09_agente_cobros_y_pagos_conocimiento_transferencias_salientes_v72
pm: pablo
fecha_captura: 2026-10-09
fuente: "/sync_mails — mail '📣 NOVEDADES PRODUCTO - AGCyP: Transferencias salientes más sólidas y trazables' (threadId 1a11c74d82108746), Nicolás Colón, 2026-10-09, comunicación oficial de Producto (feature en producción desde v72, 31/08/2026)"
producto: agente_cobros_y_pagos
tema: Transferencias salientes del Agente de Cobros y Pagos — ID propio anti-colisión por Collector, esquema de reintentos real del StateMonitor, y registro de la respuesta textual del banco (Apibank)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/transferencias_salientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Comunicación oficial de Producto (Nicolás Colón), en producción desde el 31/08/2026 (v72), categoría BAU.

**Tres puntos débiles detectados internamente** (se agravaban con el crecimiento de volumen de operaciones):
1. El ID (`origin_id`) que dos Collectors distintos envían podía coincidir y generar un error de transferencia contra el banco.
2. El StateMonitor no tenía un esquema de reintentos real — solo volvía a consultar una única vez, a los 5 minutos, dejando casos sin resolver.
3. La respuesta del banco se descartaba, sin dejar evidencia para Soporte cuando una transferencia quedaba en un estado dudoso.

**Qué se implementó:**
- ID propio de cara al banco por cada Collector, que nunca se repite entre transferencias de clientes distintos sin importar el ID que cada uno envíe. Formato: `1-CUITBINDPSP-C{codCollector}{idTransferencia}-1` (ejemplo real: `1-30717449076-C08340000056683-1`).
- Se incluye el ID original del cliente en el webhook de transferencia saliente, validado a 15 dígitos.
- Esquema de reintentos real del StateMonitor: reconsulta cada 30 segundos, ventana de 5 minutos ante un "todavía no terminé de procesar" del banco (código TX019 de Apibank) antes de dar la transferencia por rechazada, escala a reintentos cada 1 hora después de las primeras 6 horas sin resultado, tope de 7 días antes de dejar de reconsultar.
- Se empezó a guardar la respuesta textual completa del banco (Apibank), tanto al crear la transferencia como en cada reconsulta posterior — antes se descartaba. Ahora Soporte puede ver directamente qué contestó el banco ante una transferencia con estado dudoso, sin escalar a desarrollo.

**Métricas:**
- Errores de transferencia por ID duplicado entre clientes: antes podían ocurrir (riesgo creciente por volumen) → sin casos reportados desde el release. Objetivo de diseño: 0%.
- Tiempo hasta completarse (transferencias que pasan al StateMonitor): antes una única reconsulta a los 5 minutos → ahora mediana de 41 segundos, 96,6% antes de los 5 minutos (medido sobre 819 transferencias completadas entre 31/08 y 06/10/2026).
- Transferencias que quedaban "colgadas" sin resolver (estado UNKNOWN): ~120/mes antes del release (estimación de Soporte, no conteo exacto de Fintexa) — sin medición posterior formal todavía, a monitorear cómo evoluciona con el nuevo esquema de reintentos.

**Material técnico para Soporte/Integraciones (adjunto al mail, no leído por esta skill):**
- Épica técnica completa: transferencias salientes AGCyP — [AD-1355](https://bindpsp.atlassian.net/browse/AD-1355)
- Detalle técnico: registro de respuestas de Apibank — [AD-1241](https://bindpsp.atlassian.net/browse/AD-1241)
- Guía "Buscar logs de Transferencias de CVU Collect en tablas de Financial" (tabla `dbo.TransferenceResponseLog`, búsqueda por `TransferenceId`).
- Guía "Buscar transferencias en el StateMonitor de CVU Collect" (búsqueda por `TransaccionId` = OriginId del Collector, o ID BIND si Apibank ya la encontró pero sin estado definitivo).

> Fuente: mail "📣 NOVEDADES PRODUCTO - AGCyP: Transferencias salientes más sólidas y trazables" (threadId `1a11c74d82108746`), Nicolás Colón, 2026-10-09.
