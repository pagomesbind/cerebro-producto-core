---
id: 2026-09-21_conocimiento-cbu-corto-reagendado-favacard-auditoria-v74
pm: nicolas
fecha_captura: 2026-09-21
fuente: "Reunión 'Weekly - Producto / Operaciones' (2026-09-21)"
producto: adquirencia
tema: Mecanismo para detectar pagos erróneos por CBU corto reagendado en Botón Simple Dos (caso FAVACARD) y auditoría formal asignada a v74
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Weekly - Producto / Operaciones" (2026-09-21), Gonzalo Rivera retomó un problema operativo ya conocido (caso FAVACARD, "Fabacar" en la minuta): un usuario paga con un **CBU corto de Botón Simple Dos que quedó agendado/guardado en su app** de una deuda anterior, en vez del CBU corto vigente de la deuda actual — genera inconsistencias de pago difíciles de explicarle al cliente ("¿cómo entendemos que la persona pagó mal porque se guardó el CBU corto en otro momento?").

Nicolás Colón explicó el mecanismo de detección: en el registro de transacciones se puede filtrar por el CBU corto recibido (el CBU de Botón Simple Dos) y comparar los datos del pagador (nombre, apellido, CBU de origen) entre transacciones. Si el mismo pagador aparece asociado a **dos deudas con ID distinto** (no necesariamente de meses distintos, alcanza con que cambie el ID de deuda), es muy probable que el segundo pago haya sido porque el CBU corto quedó agendado en la app del pagador desde el pago anterior — la probabilidad de coincidencia por azar es muy baja.

Ya existía un pedido de auditoría de CBU corto (relacionada a las deudas a las que estuvo asignado) para poder aplicar este análisis de forma sistemática — confirmado en esta reunión que **quedó asignada a la versión 74** (sin fecha todavía, estimada octubre por Matias Alzogaray, ya que v74 no tiene fecha fijada).

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-09-21), minuta Gemini.
