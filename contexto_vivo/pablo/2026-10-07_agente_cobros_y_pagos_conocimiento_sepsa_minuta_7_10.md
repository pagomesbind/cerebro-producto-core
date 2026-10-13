---
id: 2026-10-07_agente_cobros_y_pagos_conocimiento_sepsa_minuta_7_10
pm: pablo
fecha_captura: 2026-10-07
fuente: "/sync_mails — mail 'Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 7-10' (threadId 1a1171ebab0a915d), Guillermo Paolucci (Western Union), 2026-10-07, + respuesta de Adriana Endzeliz sobre códigos de error"
producto: agente_cobros_y_pagos
tema: Minuta semanal de seguimiento del desarrollo de la Pasarela de Pagos Bind-SEPSA (Western Union/BPG) — pendientes de producto y hallazgos relevantes
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

Minuta semanal de seguimiento del desarrollo de la Pasarela de Pagos Bind-SEPSA/BPG (Western Union) — reunión recurrente de ingeniería/producto entre Bind PSP y Western Union/Keep IT Simple. Se registran los puntos con relevancia de Producto (se omiten los puramente de estado de desarrollo sin impacto de definición):

- **Comprobante por mail:** aprobado para avanzar. Fecha UAT semana del 26/10, fecha de producción 27/10.
- **Confirmación online a entidades:** el documento funcional está en análisis del lado de SEPSA — pendiente de SEPSA, no de Bind.
- **Mapeo de errores de API:** Brian (WU) había planteado el tema con más detalle; Adriana Endzeliz respondió a la reunión con el estándar actual de la pasarela: **error 429 (too many requests)** cuando alguna de las APIs de Bind presenta algún error, y **error 500** si el sistema sufre una caída o interrupción. Queda pendiente la confirmación de Western Union de si ese nivel de detalle alcanza.
- **Dato de billetera/tarjeta de origen en pagos QR y Transferencia:** Western Union necesita, para pagos con QR y Transferencia, el dato de la billetera desde la cual se emite el pago; para pagos con tarjeta, necesitan saber con qué tarjeta se pagó. Está en análisis del lado de SEPSA. **Hasta diciembre no van a tenerlo en el archivo SFTP** — como contingencia, debería poder bajarse desde el Admin (Pochita/Admin Centralizador).
- **Alias para pagos con transferencias:** en curso, pasa a una versión de PRD próxima — no entra en octubre 2026. Queda pendiente priorizar y definir fecha.
- **Caso Mercedes Benz (cliente):** necesitan, en el reporte transaccional, identificar el **CUIT pagador / titular de la billetera o cuenta que transfiere** y la descripción del CVU de destino que le aparece al usuario. El campo ya existe en el archivo diario — queda pendiente coordinar una reunión con IT de BPG para definir el TID (identificador de transacción). Relacionado con la reunión ya agendada "Boton BIND - BPG Dato unívoco de TXs" (viernes 09/10).
- **Reunión de conciliaciones:** Western Union comparte el contenido de los archivos SFTP de conciliación — sin definición de producto todavía, pendiente de revisión.
- Puntos puramente operativos/técnicos sin impacto de Producto, no destilados en detalle: ajuste de tiempos de refresco del estado de operación en el piloto PRD, bug del cuenta-regresivo del pago (muestra vencimiento del link en vez de los 15 minutos), eliminación de un elemento de UI ("la flecha") en curso con Marketing.

> Fuente: mail "Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 7-10" (threadId `1a1171ebab0a915d`), Guillermo Paolucci (Western Union), 2026-10-07, con respuesta de Adriana Endzeliz (Comercial) el mismo día sobre los códigos de error.
