---
id: 2026-10-01_agente_cobros_y_pagos_interpretacion_csv_transacciones_boton_pago
pm: pablo
fecha_captura: 2026-10-01
fuente: "/sync_mails — hilo \"Botón de Pago: Archivos para BI\" (threadId 1a0eeb087558720d), Pablo Gomes / Adriana Endzeliz / Western Union-SEPSA, 2026-09-29/2026-09-30"
producto: agente_cobros_y_pagos
tema: "Mecánica para interpretar el CSV de transacciones exportado desde el Admin (medio de pago, billetera/banco origen, marca de tarjeta) — pedido de Western Union/SEPSA para su equipo de BI"
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

A pedido de Western Union/SEPSA (cliente de Botón de Pago, mismo grupo que Pago Fácil), Pablo Gomes compartió el 2026-09-29 instrucciones para que el equipo de PowerBI de WU pueda interpretar el CSV exportado desde el Admin de Bind PSP. Esta es la mecánica completa, citada tal cual (no está documentada en otro lugar de la wiki):

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

> Fuente: hilo de mail "Botón de Pago: Archivos para BI" — Pablo Gomes / Adriana Endzeliz / Western Union (Guillermo Paolucci, Verónica Redondo, Marcos López), 2026-09-29 a 2026-09-30, threadId `1a0eeb087558720d`.
