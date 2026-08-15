# Pedidos de Clientes y Hallazgos Operativos Históricos — Wallet

> Estado: mezcla de en producción y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 3 archivos-cola de `detalle_productos/transversal/` (`pedidos_puntuales_de_clientes.md`, `dolores_soporte_y_administracion.md`, `mejoras_e_iniciativas_tecnicas.md`) que mezclaban pedidos de varios productos en un solo archivo.

## Pedidos puntuales por cliente

- **Banza**: endpoint GET de webhooks configurados (Pendiente).
- **PLD/Worldsys**: envío de interfaz de actividad de cuentas Wallet — ver [3_recursos/cumplimiento_normativo/reporteria_worldsys_bcra.md](../../cumplimiento_normativo/reporteria_worldsys_bcra.md) (en producción).

## Cluster de confiabilidad — Astropay (cliente de mayor volumen)

Conjunto de Spikes y mejoras sobre el mismo dolor: transferencias entrantes de Astropay que tardaban demasiado en notificarse a la organización, o cuya operación existía pero sin comprobante asociado:
- Gestión de colas y políticas ante errores para transferencias entrantes sin comprobante.
- Mejoras al endpoint de conciliar: aceptar una lista de ids (en vez de uno a uno) e indicar explícitamente si se quiere que dispare notificación — ambas para poder re-conciliar en lote sin generar notificaciones duplicadas.
- Limpieza de la base de datos `NotificacionesWallet` (acumulación de registros).
- Operaciones que quedaban en estado "a auditar" (acreditadas o fallidas) durante mucho tiempo sin revisión automática — se agregó una consulta que recorre todas las operaciones en ese estado.
- **Endpoint dedicado de conciliación optimizado** (paginado grande, campos mínimos) — construido específicamente para el volumen de Astropay.

Ver también `detalle_productos/wallet/clientes_white_label.md` (Astropay como cliente de mayor volumen relevado).

## Resiliencia del backend de eventos (comprobantes/operaciones)

Cluster de manejo de excepciones y contingencia para operaciones que podían quedar sin su comprobante asociado en el flujo event-driven (consumers de Cuenta/Comprobantes/Operaciones):
- Manejo de excepciones centralizado en los consumers.
- Contingencia para operaciones sin comprobante, específicamente en transferencias salientes (mismo patrón de bug — WS-490 — que la mecánica equivalente del Agente de Cobros y Pagos, ver [agente_cobros_y_pagos/transferencia_saliente_mecanica.md](../agente_cobros_y_pagos/transferencia_saliente_mecanica.md)).
- API "Comprobantes Espejo" dedicada a generación masiva de comprobantes (mecanismo de reconciliación/backfill).
- Delay aleatorio (random) en un background service para evitar la duplicidad de devoluciones de transferencias — mitigación de una condición de carrera conocida más que un fix de raíz.

## Operación de Wallet (pedidos de Soporte)

- No permitir transferir si `monto + costo > saldo` (validación de saldo insuficiente considerando el costo de la operación, no solo el monto).
- Guardar el saldo del día de la cuenta recaudadora por organización.
- Las cuadraturas (conciliación contable) no deberían generarse si no se encuentra el extracto correspondiente.
- **Bug de segmentación cruzada**: las cuentas de **TIN** se daban de alta en el calculador de costos con el segmento de **SUR FINANZAS** (mezcla de configuración entre dos clientes white-label distintos) — ver [ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md](../ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md).

## Ver también
- [3_recursos/arquitectura_sistema/idempotencia_de_plataforma.md](../../arquitectura_sistema/idempotencia_de_plataforma.md) — patrón transversal de falta de idempotencia centralizada.

---
*Fuente: Epics Notion "Dolores de clientes", "Dolores de Soporte y administración" y "Mejoras e Iniciativas Técnicas" — ingesta 2026-07-06.*
*Última actualización: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Wallet de 3 archivos-cola de `detalle_productos/transversal/`.*
