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

## Ver también

- [configuracion_y_operacion.md](index.md) — cómo se crea un collector, mecánica de webhooks entrantes/salientes.
- [cuenta_recaudadora_usd.md](cuenta_recaudadora_usd.md) — cluster de bugs de la puesta en producción en USD (mismo circuito CVUCollect).

---
*Fuente: Epics Notion "Dolores de clientes" (38 tickets) y "Dolores de Soporte y administración" (~93 tickets, muestra relevante) — ingesta cola final 2026-07-06.*
*Última actualización: 2026-10-01 — `/context_merge`: nuevas secciones "Mecánica para interpretar el CSV de transacciones exportado desde el Admin" y "Seguimiento Bind-SEPSA (Western Union/Pago Fácil, Botón de Pago) — minuta 23-9" (Pablo Gomes).*
*Última actualización anterior: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Agente de Cobros y Pagos de 3 archivos-cola de `detalle_productos/transversal/`.*
