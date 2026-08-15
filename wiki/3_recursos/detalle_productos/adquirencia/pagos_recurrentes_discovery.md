# Discovery — Alianza con DEBI para Pagos Recurrentes (Débito Automático)

> Estado: discovery — no construido. Contenido destilado de la Epic de Notion "Recurrencia en cobros" (Status "Discovery - Producto", sin backlog de desarrollo — nunca pasó a construcción). Reubicado desde `detalle_productos/transversal/pagos_recurrentes_discovery.md` en la reestructuración PARA en cascada (2026-08-12). Toca tanto Adquirencia (RxT, Decidir/Payway) como Agente de Cobros y Pagos (cuenta recaudadora, liquidación a comercios) — se clasifica en Adquirencia por ser el producto donde nace la propuesta (RxT), no por exclusividad.

## 1. Qué es DEBI

**DEBI** (ex "Tu Cuota", [debi.pro](https://debi.pro)) es un proveedor de pagos recurrentes/débito automático con tres productos: captación y validación (links de pago + identificación de medios de pago), procesamiento y recuperación (routing inteligente entre procesadores + reintento de rechazos), y métricas integradas (panel unificado multi-procesador).

## 2. Modelo de negocio propuesto

- **Alianza de revenue sharing**: si el producto lo vende Bind PSP con número de establecimiento propio, Bind PSP se queda con el 80% de la ganancia. Costo directo informado por DEBI: 1.60%.
- **Volumen de referencia**: ~$1.000 millones de pesos por mes, ticket promedio $75.000.
- **Convenio multicartera** (Visa + Mastercard).

## 3. Etapas de integración planteadas

1. **"Compara en casa"**: DEBI procesa los pagos directamente contra Decidir/Payway (extranet Prisma, presentación de archivos `DEBLIQC`/`DEBLIQD`, descarga de resultados). Bind PSP valida comisiones y plazos, y debe dar de alta establecimientos nuevos bajo rubro 4816 (Comercio Electrónico) para Visa y Mastercard habilitados para pagos recurrentes.
2. **DEBI integrándose al resto de las soluciones de cobro de Bind PSP**: caso "Compara" se integra a **RxT** (Adquirencia).
3. **Bind PSP integrando la solución de pagos recurrentes como canal propio para ofrecer a sus clientes** — discovery de producto (cómo venderlo), sin avanzar más allá de la idea.

## 4. Limitación de conocimiento identificada

Bind PSP no conoce la deuda del cliente de DEBI ni gestiona la deuda de los cobros recurrentes — el rol de Bind PSP en el modelo es recibir esos cobros en una cuenta recaudadora propia (Agente de Cobros y Pagos) y liquidar a los comercios (Adquirencia/RxT), sin visibilidad ni gestión de la cartera de deuda subyacente.

## Ver también

- `detalle_productos/agente_cobros_y_pagos/` — cuenta recaudadora y liquidación a comercios, el lado de Bind PSP en este modelo.

---
*Fuente: Notion histórico, Epic "Recurrencia en cobros" — ingesta 2026-07-06. Nunca pasó de discovery: sin tickets de desarrollo, sin definición de producto cerrada.*
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/pagos_recurrentes_discovery.md` (reestructuración PARA en cascada). Contenido sin cambios.*
