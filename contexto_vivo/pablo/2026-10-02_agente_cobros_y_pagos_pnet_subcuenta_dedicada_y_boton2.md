---
id: 2026-10-02_agente_cobros_y_pagos_pnet_subcuenta_dedicada_y_boton2
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'PNET / Boton 2.0 y RxT a CBU', 2026-10-02 16:01, Drive docId 1YUSiHLRHrFMzAWl8JaACe2gAARrmtndOV7xDTFQ43nE"
producto: agente_cobros_y_pagos
tema: Propuesta de cuenta recaudadora dedicada por ente (subcuenta) para transferencias de alto monto + sinergia con Botón 2.0
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Contexto:** Provincia Net (PNET, integración existente de recaudación bancaria con Banco Industrial — proyecto `prd-66_provincianet_creacion_masiva_qr/`) planteó un caso de uso nuevo de uno de sus clientes ("entes"): un cliente corporativo con 250 usuarios finales necesita que esos usuarios le transfieran montos altos por plataformas no convencionales. El circuito actual de Provincia Net (CBU corto / RxT, pensado para asociar una deuda a un monto exacto) no es viable para este caso — los montos variables generan costos de impuestos débito/crédito al tener que devolver diferencias, y el volumen/monto excede lo operable por RxT.

**Propuesta técnica (Gustavo Lazzaro, BIN PCP):** en vez de una integración nueva, reutilizar la infraestructura ya existente de **Agente de Cobros y Pagos**: crear una **subcuenta con CBU largo exclusiva por "ente"** (cada cliente corporativo de Provincia Net que lo necesite), bajo el mismo CUIT/quid recaudador de BIN PCP que ya opera Provincia Net. Mecánica:
- El ente le da a sus clientes finales el CBU largo de su subcuenta dedicada (no un alias, para no generar rotación de identificadores).
- Cada transferencia entrante llega directo a esa subcuenta — Provincia Net ve, vía la integración de Agente de Cobros y Pagos que ya tiene, todos los movimientos y el saldo de esa cuenta en línea, igual que hoy.
- El webhook que reciben ya no asocia la transferencia a una deuda/CB corto, sino que informa directamente el CUIT originante de quien transfirió (identificación por pagador, no por deuda).
- **No requiere desarrollo nuevo** — solo alta de la subcuenta y nuevas credenciales de acceso para Provincia Net. El único punto a definir del lado de BIN es la salida de fondos hacia una cuenta de BAPRO (o equivalente) y si el costo pasa a ser por transacción (hoy Provincia Net paga costo fijo) — Diego Weledniger evalúa bonificar el servicio de cuenta para que la propuesta sea competitiva.
- Pendiente de confirmación técnica y comercial por parte de Provincia Net el **lunes 2026-10-05**.

**Botón 2.0 — sinergia detectada:** en la misma reunión, Adriana Endzeliz/Diego Weledniger presentaron el Botón 2.0 (checkout web con tarjeta/QR/transferencia, vía API + generación de link de pago, con devolución automática de fondos si el monto transferido no coincide con la deuda). Gilda Carneiro (Provincia Net) señaló que ya operan un producto equivalente, **"Net Pagos"**, con **+130 clientes integrados hace más de 2 años** — se evalúa sinergia entre ambas herramientas (posible reventa del Botón 2.0 por parte de Provincia Net a sus propios "entes", integrado dentro de su propia botonera, sin que el ente tenga que integrarse directo con BIN). Mecánica de integración del Botón 2.0 explicada por Pablo Gomes: el ente conecta su sistema ERP/base de deudas, Bind genera el link de pago y notifica por webhook — la integración completa (conexión a la base de deudas) tomó ~2 meses en el caso de referencia (Provincia Net); también es posible operar el botón sin búsqueda de deuda, con monto manual.

**Acción comprometida:** Pablo Gomes se compromete a elaborar un caso de uso/flujo gráfico detallado de la integración del Botón 2.0 para la revisión del equipo (ver tarea T-163 en `tareas.md`).
