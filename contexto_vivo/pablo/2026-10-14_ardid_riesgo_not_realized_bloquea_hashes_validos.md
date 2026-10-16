---
id: 2026-10-14_ardid_riesgo_not_realized_bloquea_hashes_validos
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'W 74 - QA+Producto' (2026-10-14, 16:00)"
producto: ardid
tema: Pagos de Botón Simple rechazados por el procesador no notifican 'not realized' a Ardid, generan acumulados incorrectos y bloquean hashes de tarjetas válidas — máxima prioridad para v74
tipo: riesgo
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Problema crítico

Luciana Rudaz y Pablo Gomes identificaron que los **pagos rechazados por el procesador** (no por Ardid) en Botón Simple **no están notificando correctamente a Ardid mediante la función de "not realized"** (transacción no concretada). Esto genera dos efectos encadenados:
1. **Acumulados incorrectos** en Ardid (cuenta transacciones como si hubieran ocurrido, afectando reglas de frecuencia/scoring que dependen de ese conteo).
2. **Bloqueo de hashes de tarjetas válidas** — tarjetas legítimas terminan bloqueadas por Ardid a causa de este conteo erróneo.

## Impacto confirmado

Luciana Rudaz señaló que esto **eleva la tasa de rechazos en pagos recurrentes de entidades como los servicios del Grupo DESA**. Dado el impacto directo sobre clientes con pagos recurrentes, Pablo Gomes clasificó esta corrección con **máxima prioridad absoluta para la versión actual (v74)** — por encima de todos los demás tickets evaluados en la misma sesión de priorización QA+Producto.

## Contexto de la sesión

Esta reunión definió un nuevo criterio de priorización de tickets de versión (variables tipo semáforo: impacto a clientes externo/interno, riesgo colateral, urgencia de entrega 1-3) que el equipo acordó integrar directamente en Jira a futuro, en vez de usar un documento externo. Otros hallazgos de la misma sesión, de menor severidad: error de doble comilla en el código externo de QR en webhooks de pago; omisión de código/raíz de productos en webhooks (sin impacto en clientes externos); alias de Coelsa visible en checkout de Botón Simple 2.0 para Pago Fácil (parametrizable por entidad, nace desactivado); problema de contracargo cuando un CBU corto se reasigna a otro comercio antes de procesar una devolución de 10 días atrás (afecta conciliación, reclamado a diario por Mariana Nadalin).

> Fuente: reunión "W 74 - QA+Producto", 2026-10-14 16:00hs (Pablo Gomes, Luciana Rudaz, Andrea Orsini, Nicolás Colón, Ana María Moreno, Bethania Tornari, Hernán Clarich).
