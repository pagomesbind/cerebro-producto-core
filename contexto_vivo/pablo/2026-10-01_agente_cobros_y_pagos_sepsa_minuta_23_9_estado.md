---
id: 2026-10-01_agente_cobros_y_pagos_sepsa_minuta_23_9_estado
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_mails — mail \"RE: Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 23-9\" (threadId 1a0cefe80bcb7ecc), Guillermo Paolucci (Western Union), 2026-09-30"
producto: agente_cobros_y_pagos
tema: "Seguimiento del desarrollo de la pasarela Bind-SEPSA (Botón de Pago, cliente Western Union/Pago Fácil) — estado al 2026-09-30, con fechas UAT/PRD confirmadas para envío de comprobante por mail"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Minuta de seguimiento recurrente del desarrollo de la pasarela de pagos Bind-SEPSA (Western Union, mismo cliente/grupo que Pago Fácil en el checkout de Botón de Pago). No está asociado a un proyecto tracker en Jira — es una serie de minutas periódicas sin IDEA propia en `1_proyectos/index.md`. Estado reportado por Guillermo Paolucci (WU) el 2026-09-30:

1. **Piloto PRD — bug de estado:** al finalizar una operación queda en estado `INICIADA` y hace falta refrescar varias veces para que pase a `CONFIRMADA`. Reproducido en 2 pruebas en USINA (trace IDs compartidos). Asignado a Adriana Endzeliz para confirmar con el equipo de IT de Bind.
2. **Envío de comprobante por mail:** propuesta recibida y aprobada para avanzar (9/9). **Fecha UAT: semana del 20/10. Fecha PRD: semana del 27/10.**
3. **Confirmación online a entidades:** documento funcional enviado, en análisis del lado de SEPSA (sin resolución a la fecha).
4. **Identificación de billetera en pagos QR/Transferencia y de marca de tarjeta:** reunión realizada el 29/09 con Banco Industrial, se compartió el detalle de la base de datos (`EntidadCbuCvu`) — en análisis de SEPSA (ver mecánica completa en el item separado `2026-10-01_agente_cobros_y_pagos_interpretacion_csv_transacciones_boton_pago.md`).
5. **Alias para pagos con transferencias:** en curso, pasaje a PRD programado para la **próxima versión — no entra en octubre 2026**.
6. **Eliminar definitivamente el botón "flecha":** propuesta de pantallas ya compartida, con comentarios de Marketing ya devueltos. Es desarrollo de front, en curso — Adriana Endzeliz debe confirmar fecha de pasaje.
7. **Pedido nuevo — cliente Mercedes Benz:** necesitan identificar en el reporte transaccional el CUIT del pagador/titular de la billetera o cuenta que transfiere, y la descripción del CVU de destino tal como la ve el usuario. Pendiente: validar con Adriana Endzeliz con qué dato se puede trazar la transacción (si se puede incorporar el `trace id`) y compartir un archivo de ejemplo.

> Fuente: mail "RE: Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 23-9" — Guillermo Paolucci (Western Union), 2026-09-30, threadId `1a0cefe80bcb7ecc`.
