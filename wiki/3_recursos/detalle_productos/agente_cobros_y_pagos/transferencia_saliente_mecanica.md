# Mecánica de Transferencia Saliente — Agente de Cobros y Pagos

> Estado: en producción. Reubicado desde `detalle_productos/cobros/configuracion_y_operacion.md §4` en la reestructuración PARA en cascada (2026-08-12).

# Introducción
El 19/02 a la noche se implementaron cambios en la funcionalidad de transferencia saliente en agente de cobro, para mejorar y evitar inconsistencias con API Bank.

# Contexto
El cliente Jugadon reportaba muchos incidentes de este tipo que hicieron que nos demos cuentas que nos faltaba hacer el flujo más sólido.

# Resumen de la solución
El objetivo, en general, es que cualquier transferencia iniciada se registre en la base de datos de Financial, por más que ni siquiera haya llegado a api bank. Así, luego, de ser necesario, sea monitoreada y consultada hasta conseguir un estado definitivo para informar al cliente.

# Detalle de la solución
El comportamiento acordado (creado en conjunto con Nico Colón, Agus Grau y Cristian Medina, consensuado y usado para desarrollar los ajustes y luego probarlos) fue: toda transferencia saliente se persiste en Financial en el momento de iniciarse, antes incluso de llamar a API Bank; a partir de ahí el estado se actualiza según la respuesta de API Bank (éxito, error, o sin respuesta) y, si queda sin resolver, un proceso de monitoreo periódico reconsulta hasta obtener un estado definitivo.

> Nota: el diagrama de flujo original (con los distintos caminos posibles del comportamiento) es un adjunto nativo de Notion y no se pudo migrar a este archivo. Fuente original: https://app.notion.com/30db3646c94b80558fbbeca28c6b767e

## Bug real — transferencias salientes mapeadas erróneamente como recibidas (2026-08-31, sin desarrollo asociado todavía)

En la reunión "Weekly - Producto / Operaciones" (2026-08-31), Nicolás Colón identificó una inconsistencia técnica: **las transferencias salientes del Agente de Cobros y Pagos se están mapeando erróneamente como transferencias recibidas**. La minuta no detalla en qué endpoint/reporte se ve el mapeo incorrecto, desde cuándo, ni el cliente afectado — registrado como hallazgo a corregir, sin ticket todavía (ver `1_proyectos/tareas.md` T-018 del PM para seguimiento). No queda claro si es parte del mismo grupo de tickets ya en curso para "arreglar transferencias salientes de agente de cobros y pagos" (mencionado en la misma reunión, con foco en reconsultas de monitoreo) o un hallazgo nuevo y separado — a confirmar cuando se cargue el ticket.

## Ver también
- [../wallet/otros_manuales.md](../wallet/index.md) — bug equivalente de transferencia saliente sin comprobante del lado Wallet (WS-490), mismo patrón de fondo.

---
*Última actualización: 2026-09-02 — `/context_merge`: nuevo hallazgo — bug de mapeo de transferencias salientes como recibidas, sin desarrollo asociado todavía.*
*Última actualización anterior: 2026-08-12 — Reubicado desde `detalle_productos/cobros/configuracion_y_operacion.md §4` (reestructuración PARA en cascada). Contenido sin cambios.*
