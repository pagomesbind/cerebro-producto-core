---
id: 2026-10-07_adquirencia_conocimiento_mapeo_respuesta_prisma_a_transaccion
pm: pablo
fecha_captura: 2026-10-07
fuente: "sesión directa con el PM (PRD-70, POS con Prisma) — tabla de mapeo que Fintexa le pasó al PM (imagen), con la columna 'dónde se guarda' de cada campo de la respuesta de Prisma al ejecutar un cobro POS; análisis del PM + Cerebro contra el manual ISO 8583 de Prisma y las pruebas en vivo del 2026-09-22/23"
producto: adquirencia
tema: qué campos de la respuesta de Prisma (gateway Zpay) guarda Bind PSP en cada transacción POS, y cuáles faltan para conciliar/rastrear en Payway
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/integracion_prisma_conexion_directa.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

> **Alcance y límites.** La tabla la armó Fintexa (varias filas citan "(código)" y "(ISO 8583)" como fuente, es decir, salen de leer el código y el manual, no de una especificación de Payway). Nadie validó todavía qué campos usa Payway en su archivo de liquidación/conciliación — ese layout no está en el Cerebro. Las recomendaciones de abajo son análisis, no decisiones: ver tarea T-192 en `1_proyectos/tareas.md`.

## 1. Mapeo vigente: respuesta de Prisma → tabla `Transaccion`

Cada cobro POS por Prisma devuelve un JSON con dos bloques, `metaData` (datos del gateway Zpay) y `dataAdquirente` (datos del autorizador). Lo que Bind PSP guarda hoy:

| Campo de la respuesta | Qué es | ¿Se guarda? | Dónde |
|---|---|---|---|
| `metaData.ZpayTransactionId` | Id de la operación en el gateway Zpay de Prisma. El código lo comenta como "MAY BE UNIQUE" y lo usa como clave de la transacción | Sí | `Transaccion.IdentificadorOrden`; también `ReferenciasPago` si no hay orden de venta; `PropiedadesAdicionales` (RRN); Auditoría |
| `dataAdquirente.ReferenceNumber` | Número de referencia de la operación (RRN, ISO 37). El código lo comenta como "RRN" | Sí | `Transaccion.IdentificadorProcesadorPago` (si viene vacío, se usa el `ZpayTransactionId`); Auditoría |
| `dataAdquirente.ResponseCode` | Código de respuesta del autorizador (ISO 39); `00` = aprobada | Sí | `Transaccion.EstadoMotivo` y `Estado`; Auditoría |
| `dataAdquirente.TransmisionDate` | Fecha y hora de la transmisión (ISO 7); termina siendo la fecha de negocio de la transacción | Sí | `Transaccion.FechaLocalNegocio`, `HoraLocalNegocio`, `FechaPago`; Auditoría |
| `dataAdquirente.ResponseDescription` | Texto que explica el código de respuesta, p. ej. el motivo de un rechazo | Solo en Auditoría | `AdditionalResponseInformation` |
| `Message` | Mensaje general de la respuesta del gateway | Solo en Auditoría | `ResponseReason` |
| `dataAdquirente.Message` | Mensaje de error del adquirente; llega solo cuando hay error | Solo en Auditoría | `ResponseReason`, concatenado al anterior |
| `dataAdquirente.Pan` | Número de la tarjeta | Solo en Auditoría | `PaymentCard.PAN`, **en claro** (anotado por Fintexa/quien armó la tabla como CWE-312) — ver item de riesgo `2026-10-07_adquirencia_riesgo_pan_en_claro_auditoria_pos_prisma` |
| `Status` | Estado general de la llamada al gateway | No | — |
| `dataAdquirente.Amount` | Importe que procesó Prisma. Fintexa usa el importe del POS y **no compara** contra este | No | — |
| `dataAdquirente.Trace` | Trace/STAN (ISO 11), secuencial de la operación en la terminal. Fintexa guarda su propio Trace generado, no este | No | — |
| `dataAdquirente.TerminalId` | Identificador de la terminal en Prisma (ISO 41) | No | — |
| `dataAdquirente.MerchanId` | Número de comercio/establecimiento en Prisma (ISO 42) | No | — |
| `dataAdquirente.AuthorizationCode` | Código de autorización que otorga el emisor (ISO 38); es el que suele figurar en el ticket | No | — |
| `dataAdquirente.ResponseReference` | Referencia de la respuesta del autorizador; su diferencia con `ReferenceNumber` no está clara (**no verificado**) | No | — |
| `dataAdquirente.EmvResponse` | Datos EMV que devuelve el emisor para el chip | No | — |
| `metaData.Timestamp` | Momento en que el gateway generó la respuesta | No | — |
| `metaData.ResponseTime` | Tiempo que tardó el gateway en responder | No | — |

## 2. Análisis: qué falta para conciliar y rastrear en Payway

Contrastado contra el manual ISO 8583 de Prisma (ya en canon) y contra las pruebas en vivo de PRD-70. Orden de prioridad propuesto:

1. **Código de autorización (ISO 38) — el faltante más claro.** Es el dato que el comercio y el cliente ven impreso en el ticket (lo dice la propia tabla de Fintexa). Hoy Soporte no puede buscar en el Admin una transacción a partir de un ticket con reclamo, ni cruzarla con lo que ve Payway.
2. **Establecimiento y terminal de Prisma (ISO 42 y 41) por transacción.** Hoy solo se pueden deducir de la configuración vigente (tabla `CardBusinessRulesDB`), pero esa tabla es editable (ver `pos_multiadquirencia.md`) y varios rubros comparten terminal, así que con el tiempo la deducción deja de ser confiable. Cruza con el hallazgo operativo de la reunión "Weekly - Producto / Operaciones" del 2026-10-05 (Gonzalo Rivera): Payway exige el **número de establecimiento** para gestionar reclamos, no el identificador de sitio de Bind — ver `contexto_vivo/2026-10-05_adquirencia_conocimiento_mapeo_establecimientos_payway.md`. Guardar el establecimiento y la terminal usados en cada cobro resuelve ese cruce manual en origen.
3. **Importe autorizado por Prisma (ISO 4) y control de diferencia.** Hoy se registra el importe del POS y no se compara. En las pruebas del 2026-09-22 la pantalla de cuotas del POS mostraba totales distintos al monto base (p. ej. $100,00 en 1 pago vs. $122,40 en 3 cuotas): hay que confirmar con Fintexa qué importe se registra con cuotas y guardar el que realmente autorizó Prisma, alertando diferencias.
4. **Ticket (ISO 62), trace (ISO 11) y lote — confirmar que se persisten del lado Bind.** Los tres los genera el sistema propio (el manual lo establece así). El ticket (4 dígitos, cíclico 0001-9999) más la fecha de la operación original son **obligatorios en una devolución** (ISO 48, sección 6.25 del manual), y el manual describe un **cierre de lote** con contadores y montos que el host concilia contra la terminal (código de respuesta 95: "diferencias en la conciliación del cierre"). La tabla de Fintexa solo cubre campos de respuesta; no dice dónde viven estos tres ni quién ejecuta el cierre de lote.
5. **Cuotas/plan (ISO 48):** confirmar si la cantidad de cuotas y el plan quedan en la transacción — afectan la liquidación.
6. **Tarjeta enmascarada en `Transaccion` (BIN + últimos 4 + marca):** hoy el PAN solo figura en Auditoría. Para soporte y para ubicar una operación en el portal de Payway conviene tener BIN, últimos 4 y marca en la propia transacción, sin PAN completo.
7. **Mostrar `ResponseDescription` en el Admin.** Hoy solo está en Auditoría; con rechazos genéricos como el `05` ("Denegada", ver tabla de códigos en este mismo archivo) la descripción es lo que podría orientar al diagnóstico.
8. **Clave de unicidad:** el propio código comenta el `ZpayTransactionId` como "MAY BE UNIQUE" y, en las pruebas, los `ID Procesador` (RRN) fueron correlativos y cortos (`000000000098` a `000000000103`) — parecen un contador, no un identificador global. Para conciliar conviene una clave compuesta (RRN + fecha + establecimiento + terminal + autorización), no el RRN solo.

**Baja prioridad o sin valor claro para conciliación:** `Status`, `ResponseReference` (hasta que se aclare qué es), `EmvResponse` (útil solo ante disputas de chip; alcanza con Auditoría), `Timestamp`/`ResponseTime` (diagnóstico de latencia, no conciliación; alcanza con Auditoría).

**Nota sobre fechas (corregida el 2026-10-07, tras ver la solicitud que Fintexa manda a Prisma):** el manual de Prisma define el campo ISO 7 en horario GMT-3, pero Fintexa **envía** `dateTimeLocalTransaction` y `dateTimeTransmission` en UTC (ver item `2026-10-07_adquirencia_conocimiento_request_compra_a_prisma_fintexa`, hallazgo 1). Como `TransmisionDate` se guarda como fecha/hora local de negocio, el desfase UTC de la grilla (ya reportado a QA) probablemente nace en lo que Bind le manda a Prisma, no en lo que Prisma devuelve. Hipótesis sin verificar con Fintexa. En una versión previa de este item se sostuvo lo contrario, antes de tener la solicitud.

## 3. Pendiente de validar (no es canon todavía)

Todo el §2 es análisis del Cerebro y el PM, sin confirmación de Fintexa ni de Payway. El criterio definitivo de "qué guardar" es el layout del archivo de liquidación/extracto de Payway, que hay que pedirles (T-192). Hasta entonces, tratar la lista de prioridades como hipótesis de trabajo.
