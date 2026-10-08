---
id: 2026-10-06_conocimiento-agcyp-salientes-prd-172-origin-id-statemonitor-y-response-apibank-en-v72
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Charla directa con el PM (armado del newsletter de PRD-172, 2026-09-08 a 2026-10-06) + Jira PRD-172, AD-1355, AD-1241, AD-1242, AD-1243, AD-1658 (leídos 2026-09-08)"
producto: agente_cobros_y_pagos
tema: Mejoras de transferencias salientes del Agente de Cobros y Pagos en producción desde la v72 (31/08/2026) — ID propio por Collector hacia Apibank, nuevo esquema de reintentos del StateMonitor y guardado del response de Apibank (PRD-172 / épica AD-1355)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/transferencia_saliente_mecanica.md
tipo_destino: actualizar
contradice: "transferencia_saliente_mecanica.md (§Detalle de la solución) habla de un 'proceso de monitoreo periódico' que reconsulta hasta obtener un estado definitivo; según el PM, antes de AD-1243 el StateMonitor solo volvía a consultar UNA vez, a los 5 minutos. El análisis técnico de Fintexa en AD-1243 decía 'pregunta cada 200 segundos (fijo)': el PM lo corrigió."
confianza: alta
estado: en_cola
---

PRD-172 ("Arreglar transferencias salientes de Agentes de Cobros y Pagos", categoría BAU, 12 SP) salió a producción en la **v72 (31/08/2026)**, publicada y activa el mismo día (confirmado por el PM). En Jira la Idea sigue en "Shipping" sin `fixVersion`, y la épica [AD-1355](https://bindpsp.atlassian.net/browse/AD-1355) sigue "En curso". Son tres cambios que se agravaban con el volumen de salientes.

**1. ID propio hacia Apibank por Collector (AD-1242).**
- Antes, dos Collectors que mandaban el mismo `origin_id` terminaban como la misma transferencia para Apibank, y la segunda daba error.
- Ahora se guarda aparte el `OriginIdApibank`, armado con el código del Collector y el ID del registro en `dbo.Transferences`. El `OriginId` del cliente se sigue guardando tal cual, y el cliente lo ve siempre (consulta, webhook y listados).
- El ID BIND de una transferencia saliente se forma así: `1-CUITBINDPSP-C{codCollector}{idTransferencia}-1`. Ejemplo real: `1-30717449076-C08340000056683-1`.
- El prefijo "C" evita el cruce con las transferencias de Wallet, que usan "W" + código de organización.
- El `origin_id` del cliente se sigue limitando a 15 dígitos y ahora se valida. Se incluye en el webhook de transferencia saliente.
- Las transferencias ya existentes sin `OriginIdApibank` se consultan por el `OriginId` original.

**2. Esquema de reintentos del StateMonitor (AD-1243, finalizada 26/08).**
- Antes **no había esquema de reintentos**: solo volvía a consultar una única vez, a los 5 minutos (corrección del PM).
- Ahora el ciclo es configurable (30 s por defecto, igual que Wallet).
- Ante un **TX019** de Apibank ("transferencia no encontrada", en realidad "todavía no terminé de procesar") sigue reconsultando hasta pasados 5 minutos desde la creación. Recién entonces la marca `FAILED` y avisa al Collector.
- Durante las primeras 6 horas reconsulta cada 30 s. Si no hay estado definitivo, la transferencia queda `UNKNOWN` y pasa a reconsultarse cada 1 hora, hasta un tope de 7 días.
- Solo `COMPLETED` y `FAILED` son estados definitivos y disparan el webhook al Collector. `UNKNOWN` es interno.
- Todos los tiempos son configurables por ambiente. Fintexa solo pudo probar en staging los casos de TX019 y los estados finales dentro de los 5 minutos (Apibank en staging es estable y no deja forzar estados intermedios).

**3. Guardado del response de Apibank (AD-1241, finalizada 31/08 con observaciones no frenantes).**
- Nueva tabla `dbo.TransferenceResponseLog` (1:N con `Transferences`, Flyway V1.8). Guarda el response textual de Apibank en la creación y en cada consulta: el repoll del alta y la consulta terminal que reporta el StateMonitor (vía `POST /v1/notifications`, con un campo opcional `responseRaw`).
- Solo aplica a TRANSFER, no a TRANSFER-CVU ni a las recibidas. El guardado es *best-effort*: si falla, la transferencia no se aborta.
- Sirve a Soporte para ver qué contestó el banco ante una transferencia en estado dudoso, sin escalar a desarrollo.

**Deuda y observaciones abiertas (de Jira, al 2026-09-08):**
- `/v1/notifications` sigue sin `[Authorize]` y ahora persiste texto libre (riesgo CWE-345 y CWE-770). El hardening (HMAC + rate-limit) quedó fuera de alcance de AD-1241, para un ticket de continuación.
- [AD-1559](https://bindpsp.atlassian.net/browse/AD-1559): `TransferenceResponseLog` crece sin límite por reintentos indefinidos del StateMonitor (Asignado).
- [AD-1558](https://bindpsp.atlassian.net/browse/AD-1558): se dispara un repoll incluso cuando Apibank rechazó la creación por validación 422 (Asignado).
- [AD-1658](https://bindpsp.atlassian.net/browse/AD-1658): en transferencias salientes `FAILED`, el `TransferenceId` se guardaba con el `OriginIdApibank` en vez del formato estándar. Estaba en Backlog y pasó a "No aplica" el 10/09/2026.
- AD-1558 y AD-1559 siguen abiertos (Asignado, sin versión). Posiblemente expliquen por qué la épica sigue "En curso". No lo confirmé.

**Versión en Jira (verificado el 2026-10-06):** AD-1241, AD-1242 y AD-1243 tienen `fixVersion` "AD 72", liberada el 2026-08-31. El pase estaba planificado para el 27/08 y se corrió a la noche del 31/08. Desarrollo entre el 12/08 y el 21/08; cierre en Jira: AD-1243 el 26/08, AD-1241 el 31/08 y AD-1242 el 08/09 (después del pase).

**Estimación de `UNKNOWN`.**
- Soporte estima que antes de la mejora quedaban en `UNKNOWN` unas **120 transferencias por mes (~30 por semana)**.
- No es un conteo exacto: Soporte iba pidiéndole a Fintexa el cambio de esos registros. Confianza media.
- Todavía no hay medición posterior a la mejora. Pendiente de seguimiento (T-112).
- Gonzalo Rivera (Gono) tuvo un caso reciente en `UNKNOWN` desde la mejora. Según el PM no debería ocurrir con la lógica nueva (T-113).

**Relación con otros items:**
- Este item completa el del 2026-10-06 `agente-cobros-weekly-05-10...`, que dejaba pendiente confirmar si la corrección de salientes estaba resuelta: lo que corresponde a PRD-172 ya está en producción desde la v72.
- El mapeo erróneo de salientes como recibidas (T-018) es un frente aparte, todavía abierto.

> Fuente: charla directa con el PM durante el armado del newsletter de producto de PRD-172 (borrador "Transferencias salientes más sólidas y trazables", todavía no enviado a los ~27 destinatarios) y tickets Jira citados.
