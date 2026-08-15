# Idempotencia — Patrón Transversal sin Capa Centralizada

> Estado: gap de arquitectura confirmado, sin resolver. Síntesis creada en la reestructuración PARA en cascada (2026-08-12) a partir de hallazgos dispersos en `detalle_productos/transversal/pedidos_puntuales_de_clientes.md` y `dolores_soporte_y_administracion.md` — es un patrón de infraestructura/diseño transversal a todos los productos, no un hallazgo de un solo producto.

## El patrón

La plataforma no tiene una **capa de idempotencia centralizada** — cada canal/endpoint resuelve la protección contra duplicados por su cuenta, con resultados inconsistentes. Evidencia acumulada de al menos 5 apariciones independientes del mismo problema de fondo:

| Canal | Síntoma | Producto | Detalle |
|---|---|---|---|
| Deuda QR | Pedido de cliente (DESA), dos intentos de fix (uno "no performante") | Adquirencia | Ver [detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md](../detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md) |
| Transferencia saliente | Pedido de cliente (COTO/GLOBANT), sin resolver | Agente de Cobros y Pagos | Ver [detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md](../detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md) |
| Botón Simple (`identificadorOrden`) | Caso real: transacción `ACREDITADA` y `RECHAZADA` para el mismo pago con distinto `identificadorProcesador` | Adquirencia | Ver mismo archivo de arriba |
| RxT (`identificadorProcesador`) | Mismo control insuficiente (`identificadorProcesador` + fecha) que Botón Simple | Agente de Cobros y Pagos | Ver mismo archivo de arriba |
| Alta de cuenta Wallet | Bug real: timeout con respuesta exitosa duplicó la cuenta | Onboarding/Wallet | Ver [detalle_productos/onboarding/hallazgos_operativos_historicos.md](../detalle_productos/onboarding/hallazgos_operativos_historicos.md) |

## Lectura para diseño futuro

Cada endpoint agregó su propia validación de idempotencia por separado en vez de apoyarse en un mecanismo compartido (ej. `externalRefId`/idempotency key genérico a nivel de plataforma). El diseño del contrato de API universal de Onboarding (PRD-202) sí incorpora explícitamente `externalRefId` como idempotency key desde el diseño — ver `1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/` — es el primer caso relevado donde se resuelve por diseño en vez de parchear después.

---
*Última actualización: 2026-08-12 — Creación del archivo en la reestructuración PARA en cascada, sintetizando hallazgos que antes estaban dispersos en 2 archivos-cola de `detalle_productos/transversal/`.*
