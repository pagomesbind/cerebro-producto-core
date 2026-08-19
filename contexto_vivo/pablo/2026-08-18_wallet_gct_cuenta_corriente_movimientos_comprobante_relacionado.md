---
id: 2026-08-18_wallet_gct_cuenta_corriente_movimientos_comprobante_relacionado
pm: pablo
fecha_captura: 2026-08-18
fuente: "/sync_meetings — reuniones \"Producto\" y \"Productos - Weekly Seguimiento\" (2026-08-18)"
producto: wallet
tema: Mejoras solicitadas por GST — filtro IDSA en cuenta corriente y comprobante relacionado en movimientos
destino_propuesto: 3_recursos/detalle_productos/wallet/pedidos_de_clientes_y_hallazgos_operativos.md
tipo: conocimiento
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

**Pedido de GST (Hipódromo), en aprobación al 2026-08-18** — dos mejoras sobre consultas existentes de Wallet, cada una estimada en ~1 MD (jornada) de desarrollo:

1. **`GET cuenta corriente`:** agregar filtro por **IDSA**.
2. **`GET movimientos`:** traer **comprobantes relacionados que no estén asociados a una operación** — pensado especialmente para comprobantes de impuestos.

Ambas ya estimadas por el equipo; falta la reunión de aprobación final con Emma Vignoles antes de avanzar el desarrollo.

**Discusión relacionada — trazabilidad de transferencias internas salientes:** el equipo identificó que hoy no hay forma de relacionar una transferencia interna saliente con la entrante que origina del otro lado. Se descartó la opción de obligar un ID externo propagado (podría chocar con la creación de una operación externa hecha directamente por el cliente con ese mismo ID). Se acordó, como mínimo, implementar el campo de **"comprobante relacionado"** (comprobante ↔ comprobante) para sostener la trazabilidad — deuda técnica reconocida, no bloqueante hoy porque el campo de referencia libre (que ya se completa desde la app) resuelve el caso de uso de forma parcial.

> Fuente: minutas de Gemini de "Producto" (docId `1qeigxfolsrSD_jPWr6CdjP-WuVWPRQ07ltvF50ZiJVw`) y "Productos - Weekly Seguimiento" (docId `1HjXi7R_F1esr-ExW4DELmvZgckdaFRl5ahRGYnO4W7A`), 2026-08-18.
