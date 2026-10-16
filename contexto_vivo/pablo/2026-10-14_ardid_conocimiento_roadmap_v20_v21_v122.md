---
id: 2026-10-14_ardid_conocimiento_roadmap_v20_v21_v122
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Ardid+BindPSP: Roadmap' (2026-10-14, 17:31, con Pentass/PSS Corp)"
producto: ardid
tema: Roadmap confirmado de Ardid/Akurtech — versión 20 (diciembre), 21 (enero/febrero) y 122 (febrero/marzo, Coelsa Prevent)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/historico/historial_versiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Versión 20 — diciembre 2026 (ajustada desde noviembre)

Alcance: **Scope** (lo más grande, por el volumen de pruebas y replicación de escenarios — determina la fecha), **Blacklist interentidades**, e **integración con Coelsa** (CPF — Servicio de Validación de Identidad/Consulta de CUIT — y Totalizadores de cuenta normativos). La reportería con agentes se desarrolla en paralelo con otro equipo, sin impactar la fecha del núcleo. El acceso VPN para desarrollar el conector de CPF está **bloqueado del lado de Bind** (Pablo Gomes se compromete a destrabarlo con Nicolás Colón) — Pentass ya designó a una persona (Esteban) para hacer el desarrollo completo desde una sola computadora conectada a la VPN, sin poder probarlo del lado de Pentass (la prueba fuerte recae en Bind).

## Versión 21 — enero/febrero 2027

- **Módulo 360**: vista centralizada de transferencias, pagos, logins y clientes **sin pararse en una entidad específica** (pedido explícito de Rocío Revelli).
- **Ráfagas**: ampliar para permitir múltiples ráfagas del mismo tipo con distintos montos (hoy solo admite una por tipo) — pedido de Credicuotas.
- **Notificaciones por Slack** (pedido de Credicuotas).
- **Auditorías**.
- **Control de cantidad de transferencias a una misma cuenta** (pedido de Credicuotas, confirmado que va en la 120/121, faltaba agregarlo al roadmap compartido).
- **Bloqueo masivo de tarjetas por hash**: ya es posible ejecutarlo hoy vía carga de archivo o manualmente desde el reporte de tarjetas (marca la tarjeta en blacklist, deja de operar) — no es un contracargo, solo inhabilita la tarjeta. Surge del dolor de Rocío Revelli con contracargos de más de 45 días (fuera del alcance de `Payment ID`).

## Versión 122 — febrero 2027 (operativo para marzo)

**Integración con Coelsa Prevent Ardid** para obtener un **score de riesgo por CUIT**, exigido por el BCRA: Coelsa tiene tiempo hasta el **1 de enero de 2027** para disponer el servicio; a partir de ahí corren **90 días para el monitoreo transaccional** y **60 días para el alta** (este último se resuelve del lado de Onboarding, no de Ardid — ver `2026-10-14_onboarding_conocimiento_resolucion_observaciones_compliance_la_virginia`). Mismo deadline y normativa ya referenciados en la reunión "Roadmap compliance" del mismo día.

## Gap de sincronización Wallet↔Ardid en bloqueo/desbloqueo (caso Coto)

Cuando Ardid bloquea a un cliente, Wallet toma esa información y bloquea el sistema. Pero si el cliente se **desbloquea desde el front de Ardid** (como hace Coto), Wallet **no se entera** hasta que el cliente intenta operar de nuevo — no hay notificación en línea del desbloqueo. Acordado: Ardid mandará un **webhook de bloqueo/desbloqueo** (ambos sentidos) para que Wallet se entere en línea y audite el origen (Ardid) y el motivo. Sin fecha confirmada todavía — se levanta como requerimiento nuevo.

## Otros temas pendientes de análisis (no definidos a fecha)

- Monitorear al **pagador** en cobros QR de comercios (hoy Bind no monitorea cobros, solo pagos) — objetivo: controlar extracciones excesivas de efectivo. Nicolás Colón debe revisar los controles estándar de comercios/pagos ya existentes en staging 119 para ver si cubren la necesidad antes de pedir desarrollo nuevo.

> Fuente: reunión "Ardid+BindPSP: Roadmap", 2026-10-14 17:31hs (Pablo Gomes, Nicolás Colón, Luciana Rudaz, Rocío Revelli, Silvana Colasurdo y Lorena Macedo de PSS Corp/Pentass, Mateo Capitanich).
