# Pedidos de Clientes y Hallazgos Operativos Históricos — Agente de Cobros y Pagos

> Estado: mezcla de en producción y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 3 archivos-cola de `detalle_productos/transversal/` (`pedidos_puntuales_de_clientes.md`, `dolores_soporte_y_administracion.md`, `defectos_encontrados_en_qa.md`) que mezclaban pedidos de varios productos en un solo archivo. Fuente original: Epics de Notion "Dolores de clientes" y "Dolores de Soporte y administración", ingesta 2026-07-06.

## Pedidos puntuales por cliente

- **Astropay**: agregar filtro por CVU propio y por CVU contraparte al endpoint de consulta de movimientos/operaciones (en producción), y pedido de webhook de transferencia entrante (quedó Pendiente).
- **COTO / GLOBANT**: pedido de idempotencia en transferencia saliente (quedó Pendiente) — mismo cliente que la Epic COTO de devoluciones parciales de Adquirencia (Jira PRD-81), pidiendo esta vez protección de duplicados del lado de salida de dinero del Agente de Cobros y Pagos.
- **TINSA**: 2 bugs de RxT/CVUCollect en el Admin — cambiar el nombre de una caja terminaba cambiando el nombre del titular del CVU asociado (bug de acoplamiento de datos), y el Admin rompía al ver las cajas de una sucursal (ambos quedaron Pendientes).

## Bugs sin cliente específico (RxT/CVUCollect)

- **Endpoint conciliar transferencias devuelve HTTP 200 con un mensaje de error adentro** (en vez de un código de error real) — mismo patrón de "error poco transparente" documentado en otras partes de la plataforma (CCL, DEBIN, TIN en Wallet).
- **Transferencias RxT perdidas** (en producción) — bug de pérdida de transacciones en el flujo RxT/CVUCollect.
- **Transferencias duplicadas por mismo ID Coelsa** en RxT — mismo dominio de fragilidad de RxT.
- **Idempotencia**: no insertar una transacción de **RxT** con el mismo `identificadorProcesador` — el control existente (solo `identificadorProcesador` + misma fecha) no alcanzaba. Ver [3_recursos/arquitectura_sistema/idempotencia_de_plataforma.md](../../arquitectura_sistema/idempotencia_de_plataforma.md) para la lectura transversal completa.

## Herramientas operativas de Soporte

- Consulta de transacciones RxT en Admin por CVU/CBU + CUIT/CUIL, con mapeo de Razón Social del comprador y anexo en Report Manager.

## Ver también

- [configuracion_y_operacion.md](index.md) — cómo se crea un collector, mecánica de webhooks entrantes/salientes.
- [cuenta_recaudadora_usd.md](cuenta_recaudadora_usd.md) — cluster de bugs de la puesta en producción en USD (mismo circuito CVUCollect).

---
*Fuente: Epics Notion "Dolores de clientes" (38 tickets) y "Dolores de Soporte y administración" (~93 tickets, muestra relevante) — ingesta cola final 2026-07-06.*
*Última actualización: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Agente de Cobros y Pagos de 3 archivos-cola de `detalle_productos/transversal/`.*
