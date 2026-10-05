# Pedidos de Clientes y Hallazgos Operativos Históricos — Agente de Cobros y Pagos

> Estado: mezcla de en producción y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 3 archivos-cola de `detalle_productos/transversal/` (`pedidos_puntuales_de_clientes.md`, `dolores_soporte_y_administracion.md`, `defectos_encontrados_en_qa.md`) que mezclaban pedidos de varios productos en un solo archivo. Fuente original: Epics de Notion "Dolores de clientes" y "Dolores de Soporte y administración", ingesta 2026-07-06.

## Pedidos puntuales por cliente

- **Astropay**: agregar filtro por CVU propio y por CVU contraparte al endpoint de consulta de movimientos/operaciones (en producción), y pedido de webhook de transferencia entrante (quedó Pendiente).
- **COTO / GLOBANT**: pedido de idempotencia en transferencia saliente (quedó Pendiente) — mismo cliente que la Epic COTO de devoluciones parciales de Adquirencia (Jira PRD-81), pidiendo esta vez protección de duplicados del lado de salida de dinero del Agente de Cobros y Pagos.
- **TINSA**: 2 bugs de RxT/CVUCollect en el Admin — cambiar el nombre de una caja terminaba cambiando el nombre del titular del CVU asociado (bug de acoplamiento de datos), y el Admin rompía al ver las cajas de una sucursal (ambos quedaron Pendientes).

## Optimización de tiempos de respuesta en pagos QR — Hipódromo de Palermo (2026-10-01)

> Fuente: reunión semanal "Análisis COBRO" con Fintexa (2026-10-01).

El análisis técnico de un pedido de optimización de tiempos de respuesta en los pagos QR del **Hipódromo de Palermo** determinó que el proceso de registro de un pago QR consta de **16 pasos**, reducibles a **11** (y en una segunda vuelta, a **8**) sin perder funcionalidad.

**Problema operativo identificado:** cuando un usuario escanea el QR muy rápido, la transacción no alcanza a insertarse en la base de datos a tiempo — se envía a una cola de procesamiento que genera demoras considerables. La solución propuesta es eliminar ese camino de cola para los casos de escaneo rápido, bajando el tiempo de respuesta de los ~7 segundos actuales a un objetivo estimado de **~4 segundos**.

**Nota sin confirmar:** se mencionó de forma tangencial un ticket de cambio de "Barchart Max" (BMX) para optimizar el rendimiento general de la base de datos, sin detalle técnico adicional.

**Estado:** análisis técnico ya realizado por Fintexa; sin ticket de Jira identificado en la minuta ni fecha de implementación confirmada — queda dentro del backlog general de la versión 74/75 (ver también la propuesta de liberaciones quincenales en curso, sin decidir, mencionada en la misma reunión).

## Bugs sin cliente específico (RxT/CVUCollect)

- **Endpoint conciliar transferencias devuelve HTTP 200 con un mensaje de error adentro** (en vez de un código de error real) — mismo patrón de "error poco transparente" documentado en otras partes de la plataforma (CCL, DEBIN, TIN en Wallet).
- **Transferencias RxT perdidas** (en producción) — bug de pérdida de transacciones en el flujo RxT/CVUCollect.
- **Transferencias duplicadas por mismo ID Coelsa** en RxT — mismo dominio de fragilidad de RxT.
- **Idempotencia**: no insertar una transacción de **RxT** con el mismo `identificadorProcesador` — el control existente (solo `identificadorProcesador` + misma fecha) no alcanzaba. Ver [3_recursos/arquitectura_sistema/idempotencia_de_plataforma.md](../../arquitectura_sistema/idempotencia_de_plataforma.md) para la lectura transversal completa.

## Herramientas operativas de Soporte

- Consulta de transacciones RxT en Admin por CVU/CBU + CUIT/CUIL, con mapeo de Razón Social del comprador y anexo en Report Manager.

## Mecánica para interpretar el CSV de transacciones exportado desde el Admin (pedido de Western Union/SEPSA para su BI, 2026-09-29/30)

> Fuente: hilo "Botón de Pago: Archivos para BI" — Pablo Gomes / Adriana Endzeliz / Western Union (Guillermo Paolucci, Verónica Redondo, Marcos López), 2026-09-29 a 2026-09-30, threadId `1a0eeb087558720d`.

A pedido de Western Union/SEPSA (cliente de Botón de Pago, mismo grupo que Pago Fácil), Pablo Gomes compartió el 2026-09-29 instrucciones para que el equipo de PowerBI de WU pueda interpretar el CSV exportado desde el Admin de Bind PSP. Esta es la mecánica completa, citada tal cual (no estaba documentada en otro lugar de la wiki):

**Cómo descargar el CSV:** desde el Admin, sección Transacciones, se filtra la búsqueda y se exporta con el botón "Descargar csv". Pueden solicitarse usuarios de acceso al Admin para ver la Entidad propia.

**Cómo interpretar el medio de pago — campo `MedioPagoId`:**
- `20` = QR interoperable
- `40` = Transferencia a CVU
- `60` = Tarjeta prepaga
- `80` = Tarjeta de crédito
- `90` = Tarjeta de débito

Para los medios `20` y `40`, el campo `CompradorCuenta` trae el **CBU o CVU** asociado a la billetera o banco que transfiere o con el que se pagó el QR. Para los medios `60`, `80` y `90`, `CompradorCuenta` trae los **primeros 6 y últimos 4 dígitos del PAN** de la tarjeta.

**Cómo interpretar la billetera/banco de origen (medios 20/40):** tomar los primeros 7 caracteres de `CompradorCuenta`.
- Si los primeros 3 caracteres son `"000"` → es un **CVU**; identificar la billetera en la tabla `EntidadCbuCvu` donde `codigoEntidad` tiene longitud 4 (ej.: los CVU de Mercado Pago empiezan con `"0000003..."`).
- Si los primeros 3 caracteres son distintos de `"000"` → es un **CBU**; identificar el banco en `EntidadCbuCvu` donde `codigoEntidad` tiene longitud 3 (ej.: los CBU de Banco Nación empiezan con `"011..."`).

**Cómo interpretar la marca de la tarjeta (medios 60/80/90):** evaluar el PAN contra estas reglas, en orden — la primera que matchea gana:
1. Amex = empieza con `34` o `37`
2. Diners Club = `36`
3. UnionPay = `62`
4. Cabal = `604`, `5896`, `6502`, o `6509`
5. Discover = `644` a `649`, o `650` a `659`
6. Visa = empieza con `4`
7. Mastercard = `51` a `55`, `2221` a `2720`, `56` a `58`, o `60` a `69` (todo lo que no matcheó antes)

**Caso abierto sin resolver al cierre de este hilo (2026-09-30):** Western Union identificó dos transacciones marcadas como QR interoperable cuyo `CompradorCuenta` empieza con `453` (sería un CBU por la regla de arriba), pero ese valor **no aparece en la tabla `EntidadCbuCvu`** que Bind les compartió. Quedó sin responder si un QR puede pagarse también con dinero en cuenta vía Débito/Crédito y, si es así, cómo se identificaría ese caso — pregunta pendiente de Bind PSP.

## Seguimiento Bind-SEPSA (Western Union/Pago Fácil, Botón de Pago) — minuta 23-9, estado al 2026-09-30

> Fuente: mail "RE: Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 23-9" — Guillermo Paolucci (Western Union), 2026-09-30, threadId `1a0cefe80bcb7ecc`. Minuta de seguimiento recurrente, sin IDEA propia en Jira — serie de minutas periódicas.

1. **Piloto PRD — bug de estado:** al finalizar una operación queda en estado `INICIADA` y hace falta refrescar varias veces para que pase a `CONFIRMADA`. Reproducido en 2 pruebas en USINA (trace IDs compartidos). Asignado a Adriana Endzeliz para confirmar con el equipo de IT de Bind.
2. **Envío de comprobante por mail:** propuesta recibida y aprobada para avanzar (9/9). **Fecha UAT: semana del 20/10. Fecha PRD: semana del 27/10.**
3. **Confirmación online a entidades:** documento funcional enviado, en análisis del lado de SEPSA (sin resolución a la fecha).
4. **Identificación de billetera en pagos QR/Transferencia y de marca de tarjeta:** reunión realizada el 29/09 con Banco Industrial, se compartió el detalle de la base de datos (`EntidadCbuCvu`) — en análisis de SEPSA (ver mecánica completa en la sección de arriba).
5. **Alias para pagos con transferencias:** en curso, pasaje a PRD programado para la **próxima versión — no entra en octubre 2026**.
6. **Eliminar definitivamente el botón "flecha":** propuesta de pantallas ya compartida, con comentarios de Marketing ya devueltos (ver también `2_areas/tareas.md` T-017, mismo tema). Es desarrollo de front, en curso — Adriana Endzeliz debe confirmar fecha de pasaje.
7. **Pedido nuevo — cliente Mercedes Benz:** necesitan identificar en el reporte transaccional el CUIT del pagador/titular de la billetera o cuenta que transfiere, y la descripción del CVU de destino tal como la ve el usuario. Pendiente: validar con Adriana Endzeliz con qué dato se puede trazar la transacción (si se puede incorporar el `trace id`) y compartir un archivo de ejemplo.

## Propuesta de cuenta recaudadora dedicada por ente (Provincia Net) + sinergia con Botón 2.0 (2026-10-02)

> Fuente: reunión "PNET / Boton 2.0 y RxT a CBU" (2026-10-02).

**Contexto:** Provincia Net (PNET, integración existente de recaudación bancaria con Banco Industrial — proyecto `1_proyectos/prd-66_provincianet_creacion_masiva_qr/`) planteó un caso de uso nuevo de uno de sus clientes ("entes"): un cliente corporativo con 250 usuarios finales necesita que esos usuarios le transfieran montos altos por plataformas no convencionales. El circuito actual de Provincia Net (CBU corto / RxT, pensado para asociar una deuda a un monto exacto) no es viable para este caso — los montos variables generan costos de impuestos débito/crédito al tener que devolver diferencias, y el volumen/monto excede lo operable por RxT.

**Propuesta técnica (Gustavo Lazzaro, BIN PCP):** en vez de una integración nueva, reutilizar la infraestructura ya existente de Agente de Cobros y Pagos: crear una **subcuenta con CBU largo exclusiva por "ente"** (cada cliente corporativo de Provincia Net que lo necesite), bajo el mismo CUIT/quid recaudador de BIN PCP que ya opera Provincia Net.
- El ente le da a sus clientes finales el CBU largo de su subcuenta dedicada (no un alias, para no generar rotación de identificadores).
- Cada transferencia entrante llega directo a esa subcuenta — Provincia Net ve, vía la integración de Agente de Cobros y Pagos que ya tiene, todos los movimientos y el saldo de esa cuenta en línea, igual que hoy.
- El webhook que reciben ya no asocia la transferencia a una deuda/CB corto, sino que informa directamente el CUIT originante de quien transfirió (identificación por pagador, no por deuda).
- **No requiere desarrollo nuevo** — solo alta de la subcuenta y nuevas credenciales de acceso para Provincia Net. Punto a definir del lado de BIN: la salida de fondos hacia una cuenta de BAPRO (o equivalente) y si el costo pasa a ser por transacción (hoy Provincia Net paga costo fijo) — Diego Weledniger evalúa bonificar el servicio de cuenta para que la propuesta sea competitiva.
- Pendiente de confirmación técnica y comercial por parte de Provincia Net el lunes 2026-10-05.

**Botón 2.0 — sinergia detectada:** en la misma reunión, Adriana Endzeliz/Diego Weledniger presentaron el Botón 2.0 (checkout web con tarjeta/QR/transferencia, vía API + generación de link de pago, con devolución automática de fondos si el monto transferido no coincide con la deuda). Gilda Carneiro (Provincia Net) señaló que ya operan un producto equivalente, **"Net Pagos"**, con **+130 clientes integrados hace más de 2 años** — se evalúa sinergia entre ambas herramientas (posible reventa del Botón 2.0 por parte de Provincia Net a sus propios "entes", integrado dentro de su propia botonera, sin que el ente tenga que integrarse directo con BIN). Mecánica de integración del Botón 2.0 explicada por Pablo Gomes: el ente conecta su sistema ERP/base de deudas, Bind genera el link de pago y notifica por webhook — la integración completa (conexión a la base de deudas) tomó ~2 meses en el caso de referencia (Provincia Net); también es posible operar el botón sin búsqueda de deuda, con monto manual.

## Ver también

- [configuracion_y_operacion.md](index.md) — cómo se crea un collector, mecánica de webhooks entrantes/salientes.
- [cuenta_recaudadora_usd.md](cuenta_recaudadora_usd.md) — cluster de bugs de la puesta en producción en USD (mismo circuito CVUCollect).

---
*Última actualización: 2026-10-05 — `/context_merge`: nueva sección "Propuesta de cuenta recaudadora dedicada por ente (Provincia Net) + sinergia con Botón 2.0" (Pablo Gomes).*
*Última actualización anterior: 2026-10-02 — `/context_merge`: nueva sección "Optimización de tiempos de respuesta en pagos QR — Hipódromo de Palermo" (Pablo Gomes).*
*Última actualización anterior: 2026-10-01 — `/context_merge`: nuevas secciones "Mecánica para interpretar el CSV de transacciones exportado desde el Admin" y "Seguimiento Bind-SEPSA (Western Union/Pago Fácil, Botón de Pago) — minuta 23-9" (Pablo Gomes).*
*Última actualización anterior: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Agente de Cobros y Pagos de 3 archivos-cola de `detalle_productos/transversal/`.*
