# Detalle de Producto — Agente de Cobros y Pagos

> Conocimiento detallado de producto/operación (manuales, procesos, hacks) que NO es la API pública oficial de Bind PSP. Renombrado desde `detalle_productos/cobros/` en la reestructuración PARA en cascada (2026-08-12) — el nombre "cobros" generaba confusión con Adquirencia (histórico "Solución de Cobros"); este módulo es específicamente el **Agente de Cobros y Pagos** (capa multi-collector sobre API BANK, CVUCollect/RxT como mecanismo). Para el overview funcional/de negocio vivo del producto ver [overview_agente_cobros_y_pagos.md](../../../2_areas/overview_productos/overview_agente_cobros_y_pagos.md).

## Documentos de este módulo

| Archivo | Contenido |
|---|---|
| [crear_collector.md](crear_collector.md) | Cómo crear un collector paso a paso (PSP=184 y PSP≠184), con IDs y bodies reales. |
| [webhook_transferencia_entrante_cbu.md](webhook_transferencia_entrante_cbu.md) | Webhook de aviso de transferencia entrante a CBU/CVU (caso Astropay). |
| [transferencia_saliente_mecanica.md](transferencia_saliente_mecanica.md) | Cómo funciona una transferencia saliente, con persistencia temprana en Financial para monitoreo (fix Jugadon). |
| [cuenta_recaudadora_usd.md](cuenta_recaudadora_usd.md) | Cuenta recaudadora en USD (caso Astropay): mecánica, diferenciación CBU/CVU en webhooks, cluster de bugs de moneda; + consulta de saldo de cuenta recaudadora en ARS. |
| [pedidos_de_clientes_y_hallazgos_operativos.md](pedidos_de_clientes_y_hallazgos_operativos.md) | Pedidos puntuales de clientes (Astropay, COTO/GLOBANT, TINSA) y bugs operativos históricos de RxT/CVUCollect. |
| [integracion_procesadores_pago.md](integracion_procesadores_pago.md) | Integración de procesadores de pago Prisma/GP: deuda técnica de grupos de reglas, parámetro "pago único" (botón de pago vs. RXT), regla de liquidación same-day de transacciones en línea, limitación del panel admin con Prisma, hotfix de localidades/códigos postales. |

## Relación con otros documentos de la wiki

- [overview_agente_cobros_y_pagos.md](../../../2_areas/overview_productos/overview_agente_cobros_y_pagos.md) — overview funcional/de negocio (qué es, modelo de uso, integraciones); este módulo profundiza en la operación concreta.
- [detalle_productos/adquirencia/carga_masiva_cajas_rxt.md](../adquirencia/carga_masiva_cajas_rxt.md) — carga masiva de cajas RxT: vive en Adquirencia (RxT es un canal de cobro de ese producto), aunque comparte el circuito CVUCollect con este módulo.
- [detalle_productos/wallet/transferencias_pull.md](../wallet/transferencias_pull.md) — transferencias pull/débito directo: vive en Wallet, no acá, pese a estar en la carpeta histórica `cobros/` antes de esta reestructuración.
- [apis_expuestas/index.md](apis_expuestas/index.md) — API pública oficial expuesta a clientes; dominio exclusivo de la skill `/sync_web`, no tocar desde acá.

---
*Última actualización: 2026-08-27 — `/context_merge`: nuevo archivo `integracion_procesadores_pago.md` (deuda técnica Prisma/GP, parámetro "pago único", regla de liquidación same-day, limitación de panel admin, hotfix de localidades, cronograma v72) a partir de la reunión "Análisis COBRO" (2026-08-20).*
*Última actualización anterior: 2026-08-12 — Renombrado desde `cobros/` en la reestructuración PARA en cascada; `carga_masiva_cajas.md` movido a Adquirencia (RxT) y `transferencias_pull.md` movido a Wallet por no ser de este producto; `configuracion_y_operacion.md` desarmado en 3 archivos temáticos.*
*Última actualización anterior: 2026-07-06 — Ingesta de Epics de Notion (lote C1): 3 archivos nuevos (cuenta_recaudadora_usd.md, carga_masiva_cajas.md, transferencias_pull.md).*
