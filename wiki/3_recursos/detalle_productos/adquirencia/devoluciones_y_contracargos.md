# Devoluciones y Contracargos — Botón Simple y QR

> Estado: en producción. Reubicado desde `detalle_productos/adquirencia/liquidaciones_y_devoluciones.md` en la reestructuración PARA en cascada (2026-08-12) — el producto **Liquidador** (para terceros como Traditum/Newpay PMC) se extrajo a [liquidador_terceros_traditum_newpay.md](liquidador_terceros_traditum_newpay.md) por ser un tema distinto.
>
> Fuente: `wiki/3_recursos/conocimiento_interno/manual_para_configuraciones/` y `wiki/3_recursos/conocimiento_interno/documentacion_para_clientes/` (ingesta Notion). Contenido sustantivo transcripto tal cual (curls, IDs reales, pasos) — sin redactar.
>
> Ver [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md#parte-4--interchange-y-comisiones-de-qr--especificación-técnica-coelsa) para el mecanismo de liquidación de comisiones de Interchange en Coelsa (distinto del proceso de liquidación al comercio documentado acá).

---

## 0. Desconocimientos de tarjeta (Botón Simple) — contracargo total de uso interno

> Fuente: Notion histórico, Epic **"Desconocimientos de tarjeta"** (Dolor). No confundir con las devoluciones/contracargos estándar documentados abajo — un "desconocimiento" es el caso donde el titular de la tarjeta niega haber hecho la compra.

- **Endpoint de uso exclusivamente interno** (Operaciones Bind PSP, vía Swagger o luego desde el Admin) — nunca expuesto a las entidades/comercios. Marca una transacción de Botón Simple como desconocimiento por transacción.
- Efecto: crea un **contracargo de tipo "desconocimiento"** (total, no parcial — distinto de los contracargos tipo "devolución" ya soportados), pasa la transacción a estado `DEVUELTA`, y registra el timestamp del desconocimiento.
- **Se liquida exactamente igual que una devolución** (mismo criterio de impuestos, archivos y PDF de comercio) — resta en la liquidación al comercio en el siguiente día hábil a la fecha de desconocimiento. Es decir: técnicamente reutiliza todo el motor de devoluciones existente, solo cambia el tipo de contracargo y quién puede dispararlo.

**Implementación en curso (agosto 2026, PRD-146/AD-1360):** > Fuente: Mail "Análisis COBRO: Lun, 10 de ago de 2026" — malzogaray@bind.com.ar, 2026-08-10.
- **Código `004`** identifica el desconocimiento como tipo de contracargo diferenciado de la devolución en el archivo/registro de liquidación — resuelve un bug de importes en cero que ocurría al no distinguirlos.
- El PDF de liquidación suma un apartado propio "Detalle de desconocimientos" + columna nueva en el resumen, sin alterar el total liquidado.
- **No existe el concepto de "desconocimiento parcial"**: cualquier desconocimiento se aplica sobre el remanente total de la transacción.
- **Estrategia de emisión tolerante a fallos:** el PDF de liquidación se emite siempre, incluso con inconsistencias de datos — se prioriza la disponibilidad del comprobante sobre la consistencia (correcciones reactivas post-emisión).
- Detalle completo del seguimiento de este desarrollo en PRD-146 (Tratamiento de contracargos de tarjeta) — proyecto de Nicolás Colón, vive en su propio Cerebro desde 2026-08-13.

## 1. Documentación: devoluciones parciales

## Documentación: devoluciones parciales

> Alcance: informativo y apto para desarrollo. Dirigido específicamente al flujo QR.

### Objetivo
Explicar en general cómo utilizar la funcionalidad de contracargo (total y parcial) de la forma más óptima, aprovechando los nuevos endpoints y webhook.

### Webhook de evento tipo contracargo

Se envía la información de la Transacción actualizada junto a la del Contracargo que sufrió.

> Este endpoint/webhook se consume con credenciales de API del producto **WALLET**.

**Ejemplo de payload:**
```json
{
   "When":"2025-12-29T12:28:23.8012893Z",
   "Payload":{
      "TipoEvento":"CONTRACARGO",
      "TipoOrigen":"ENTIDAD",
      "IdentificadorOrigen":"EDNO",
      "TipoDestino":"ENTIDAD",
      "IdentificadorDestino":"EDNO",
      "DestinoPrincipal":"https://webhook.site/6abc4b11-ba9e-47d2-97fa-4ef97eb78ea4",
      "DestinoSecundario":"string",
      "FechaEmision":"2025-12-29T12:28:23.7292582+00:00",
      "IdMensaje":"69fe7d0e-777f-4099-9ae9-aff863efd233",
      "MensajePago":{
         "IdentificadorProcesador":"0WGRXJE27Z8GPDE97MYQL3",
         "IdentificadorTransaccion":"1322137",
         "IdentificadorOrdenVenta":"9OC3496963658029B00000623438000000153248ET9EDNOTOC1CB30B5AAC",
         "IdentificadorReferencia":"YY1218T0001322137O0000153248",
         "IdOrdenVentaQr":"153248",
         "TipoTransaccion":"Transferencia30",
         "RubroMovimiento":"PagoQrTransferencia30",
         "FechaNegocio":"2025-12-29T09:28:16.0162519-03:00",
         "FechaProceso":"2025-12-18T16:14:34.8220787+00:00",
         "FormaPago":"Transf30",
         "Moneda":"ARS",
         "ImporteBruto":640.0000000,
         "EstadoTransaccion":"DEVUELTA",
         "Retenciones":[],
         "Mcc":"0763",
         "Cpa":"M5525DAK",
         "Cuit":"30715472828",
         "CuentaVendedor":"0000531907879067229001",
         "IdentificadorVendedor":"CVU:0000531907879067229001WAL:20230621|CBU:3220001805007352560018",
         "IdentificadorPagador":"20959468568",
         "CuentaPagador":"0000532609180000170008",
         "CodigoComercio":"C22900",
         "CodigoSucursal":"S18799",
         "CodigoCaja":"B00000623438",
         "InformacionAdicionalPagador":[],
         "Entidad":"EDNO",
         "Psp":"531",
         "Procesador":"0WGRXJE27Z8GPDE97MYQL3",
         "InformacionAdicionalMensaje":[
            {"Descripcion":"motivoContracargo","Valor":""},
            {"Descripcion":"importe","Valor":"640.00"},
            {"Descripcion":"contracargoParcial","Valor":"False"},
            {"Descripcion":"idContracargo","Valor":"4535"},
            {"Descripcion":"fechaContracargo","Valor":"12/29/2025 09:24:41"},
            {"Descripcion":"estadoContracargo","Valor":"ACEPTADO"},
            {"Descripcion":"importeContracargo","Valor":"640.00"},
            {"Descripcion":"tipoContracargo","Valor":"contracargo"},
            {"Descripcion":"idDebin","Valor":"DLMORZP901Z8EEP2EGJ468"},
            {"Descripcion":"debinIdApiBank","Valor":"WZ0KV87941L0XX09PEYDX4"}
         ],
         "FechaLiquidacion":null,
         "FechaPago":null,
         "MotivoRechazo":null
      }
   },
   "Type":"CONTRACARGO"
}
```

### Request — atributos del webhook

| Atributo | Tipo | Descripción |
|---|---|---|
| `When` | datetime | Fecha y hora en que fue enviada la notificación (UTC+0). |
| `Payload` | object | Objeto con información de la notificación. |
| `TipoEvento` | string | Valor fijo: "CONTRACARGO". |
| `TipoOrigen` | string | Valor fijo: "ENTIDAD". |
| `IdentificadorOrigen` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `TipoDestino` | string | Valor fijo: "ENTIDAD". |
| `IdentificadorDestino` | string | Código unívoco de la Entidad a la que pertenece el comercio. |
| `DestinoPrincipal` | string | URL del destino principal donde se envía el webhook. |
| `DestinoSecundario` | string | URL del destino secundario. |
| `FechaEmision` | datetime | Fecha y hora en que se envió la notificación (UTC+0). |
| `IdMensaje` | string | Id guid de la notificación. |
| `MensajePago` | object | Objeto con la información del pago. |
| `IdentificadorProcesador` | string | Id del contracargo enviado por el procesador del pago (Coelsa, Global Processing, Decidir, etc). Identificador usado para conciliar con procesadores. |
| `IdentificadorTransaccion` | string | Id único de la transacción para Bind PSP. |
| `IdentificadorOrdenVenta` | string | Identificador adicional según canal: para `Transferencia30` es el order id de la API Resolve en Coelsa; para `Botón simple` es el PaymentId (id del link de pago); para `CVUCollect` es el CVU en que se recibió el pago; para `MPOS` es el identificador correspondiente. |
| `IdentificadorReferencia` | string | Identificador adicional de referencia por canal. Para Botón Simple 2.0 es el `IdExterno` asignado. |
| `IdOrdenVentaQR` | string | Identificador de la orden de venta de QR. Para Botón Simple 2.0 es el `IdDeuda`. |
| `TipoTransaccion` | string | `Transferencia30` = QR; `BotonSimple` = Botón de pagos de cobro no presente; `CVUCollect` = Recaudación por transferencia a CVU; `MPOS` = Smartpos de cobro presente. |
| `RubroMovimiento` | string | Rubro interno de la transacción. |
| `FechaNegocio` | datetime | Fecha y hora en que el cliente realizó el pago (UTC-3). |
| `FechaProceso` | datetime | Fecha y hora en que se procesó el cobro (UTC-3). |
| `FormaPago` | string | `"Transf30"` = QR interoperable; `"TTDD"` = tarjeta débito; `"TTCC"` = tarjeta crédito; `"Transfer"` = recaudación por transferencia a CVU. |
| `Moneda` | string | Valor fijo: "ARS". |
| `ImporteBruto` | decimal | Importe bruto total de la transacción (lo que pagó el cliente final). |
| `EstadoTransaccion` | string | `"DEVUELTA"` = devolución exitosa (estado definitivo); `"ACREDITADO"` = devolución parcial o fallida. |
| `Retenciones` | string | Valor fijo: "None". |
| `Mcc` | string | Código de rubro según VISA MCC del comercio. |
| `Cpa` | string | Código postal argentino del comercio. |
| `Cuit` | string | CUIT del comercio. |
| `CuentaVendedor` | string | CVU del comercio. |
| `IdentificadorVendedor` | string | Concatena CVU, CBU e ID Wallet del comercio (aplica para pagos con QR). |
| `IdentificadorPagador` | string | CUIT del cliente pagador. |
| `CuentaPagador` | string | CBU/CVU del cliente pagador. |
| `CodigoComercio` / `CodigoSucursal` / `CodigoCaja` | string | Códigos identificadores en el sistema. |
| `InformacionAdicionalPagador` | object | Tuplas llave-valor con información adicional del pagador. |
| `Psp` | string | Código del PSP al que pertenece la Entidad. |
| `Procesador` | string | Id del pago enviado por el procesador. Identificador de conciliación. |
| `InformacionAdicionalMensaje` | object | Tuplas llave-valor: `motivoContracargo`, `importe` (monto devuelto hasta el momento), `contracargoParcial` (boolean), `idContracargo`, `fechaContracargo`, `estadoContracargo` (`"ACEPTADO"`/`"RECHAZADO"`), `importeContracargo`, `tipoContracargo` (fijo "contracargo"), `idDebin` (id del procesador para el contracargo), `debinIdApiBank` (id del procesador que debita al comercio y acredita en la cuenta recaudadora de BindPSP, solo comercios con Split). |
| `Type` | string | `"CONTRACARGO"` = webhook de devolución. |

### Consultar contracargo

> Este endpoint se consume con credenciales de API del producto **COBRO**.

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/{{Id}}` |
| PRODUCCIÓN | GET | (no documentada en la fuente) |

**Request:** `Id` (int, REQUERIDO) — al final de la URL, id del contracargo a consultar.

```json
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1/contracargos/3226' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

**Response:**

| Atributo | Tipo | Descripción |
|---|---|---|
| `id` | int | Id del Contracargo. |
| `transaccionId` | int | Id de la Transacción contracargada relacionada. |
| `fechaNegocioOrigen` | string | Fecha y hora en que se realizó el Contracargo. |
| `importeContracargo` | decimal | Monto del Contracargo. |
| `motivoContracargo` | string | Razón por la cual se realizó el Contracargo. |
| `importeTransaccion` | decimal | Monto total original de la Transacción. |
| `parcial` | boolean | Indica si el Contracargo se hizo por el monto total o parcial respecto a la Transacción original o su restante (más de un contracargo parcial). |
| `tipo` | string | Valor fijo: "contracargo". |
| `estado` | string | `"PENDIENTE"`, `"APROBADO"`, `"RECHAZADO"`. |
| `motivoRechazo` | string | Razón por la cual el Contracargo falló, si `estado` = "RECHAZADO". |
| `vendedorCuit` | string | CUIT del Comercio que recibió la Transacción. |
| `vendedorCbu` | string | CBU/CVU del Comercio que recibió la Transacción. |
| `idDebin` | string | Id Coelsa con el que se realizó la devolución final de cara al cliente pagador. |
| `debinIdApiBank` | string | Id Coelsa (Debin) con el cual se debitan los fondos al Comercio y se acreditan en la cuenta recaudadora de BindPSP (exclusivo para QR Split). |
| `usuario` | string | Usuario que realizó la devolución. |

**Ejemplo de response:**
```json
{
    "id": 3226,
    "transaccionId": 1278414,
    "fechaNegocioOrigen": "2025-10-08T15:51:39.3633088",
    "importeContracargo": 6817.00,
    "motivoContracargo": "string",
    "importeTransaccion": 6817.00,
    "parcial": false,
    "tipo": "contracargo",
    "estado": "ACEPTADO",
    "motivoRechazo": null,
    "vendedorCuit": "20322678275",
    "vendedorCbu": "0000531908320067229030",
    "idDebin": "5L18MKX9RMQPMZK2O6WYV4",
    "debinIdApiBank": "4XJ8G7V95VZ7MG49EMPYR0",
    "usuario": "string"
}
```

---

## 1.1 Historia de producto y cluster de bugs de webhooks — cliente COTO (IDEA Jira PRD-81, Finalizada)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA PRD-81 "COTO: Acomodar devoluciones parciales" (PRD completo en la Descripción) + Epic AD-61 (11 tickets Finalizados + 1 aún Asignado, excluido). Complementa la documentación técnica de §1 con el origen de negocio y la cola de bugs que salieron a la luz al estabilizar la funcionalidad.

**Origen de negocio**: el sistema de cobro no tenía funcionalidades naturales para operar devoluciones parciales por API. El cliente **COTO** (grande, por salir en producción) consideraba esta funcionalidad como excluyente/bloqueante, y Producto aprovechó ese impulso comercial para terminar de cerrar una funcionalidad esencial del producto de Cobro — decisión explícita de priorizar por velocidad ("debe resolverse con gran velocidad porque COTO ya está por salir").

**Alcance aprobado** (MUST): más info del contracargo en el webhook, endpoint para consultar un contracargo por id. (Should): filtrar consulta de transacciones por hora/minuto/segundo. **Fuera de alcance** explícito: nuevo webhook de contracargo, contracargo con id externo, endpoints separados de transacción/lista de contracargos por id/id externo — 5 Story Points totales.

**Cluster de bugs encontrados en QA al estabilizar el webhook de contracargo/devolución** (evidencia de que el webhook de §1 pasó por varias rondas de corrección antes de quedar como está documentado hoy):
- Formato de fecha incorrecto en `fechaContracargo` (MM/DD/AAAA en vez de DD/MM/AAAA).
- `EstadoTransaccion` informado como `ACREDITADO` cuando en realidad ya estaba `DEVUELTA`.
- Webhooks disparados con el contracargo todavía en estado `PENDIENTE`, en vez de esperar a un estado definitivo (`RECHAZADO` o `ACEPTADO`).
- Contracargo QR **parcial** con estado `RECHAZADO` no generaba webhook (sí lo hacía el total).
- Webhook de devolución de pago con tarjeta informaba el `IdTransaccion` en el campo donde se esperaba `IdContracargo`.
- Consulta de contracargo no devolvía el `TransaccionId` (pedido agregado sobre la marcha).
- Tanda de correcciones menores agrupadas en un solo ticket ("Correcciones varias de Webhooks de contracargos"): `idComprobante` informado sin sentido en el webhook de contracargo rechazado, entre otras.

**Lectura para estimaciones futuras**: mismo patrón que el cluster de "Deuda" en [boton_simple_2_0.md §3](boton_simple_2_0.md) — un webhook de evento de negocio (acá: contracargo/devolución) tiende a generar una cola de bugs de "campo incorrecto/estado prematuro/caso no contemplado" proporcional a la cantidad de estados y medios de pago que atraviesa (QR, tarjeta, transferencia), no al tamaño original de la Epic (acá: 5 SP la IDEA, pero 8 de los 12 tickets de la Epic fueron bugs encontrados después).

**Versiones de publicación** (vía `/sync_releases`, backfill XML 2026-07-13): el alcance MUST original — [AD-63](https://bindpsp.atlassian.net/browse/AD-63) (endpoint consultar contracargo) y [AD-62](https://bindpsp.atlassian.net/browse/AD-62) (más info en el webhook), más [AD-64](https://bindpsp.atlassian.net/browse/AD-64) (filtro por hora/minuto/segundo) — se publicaron en **AD 66** (2025-12-16), junto con el resto del cluster de bugs de esa misma tanda: [AD-388](https://bindpsp.atlassian.net/browse/AD-388) (webhook con contracargo PENDIENTE) y [AD-357](https://bindpsp.atlassian.net/browse/AD-357)/[AD-288](https://bindpsp.atlassian.net/browse/AD-288) (correcciones de webhook, `IdTransaccion` en vez de `IdContracargo`). El resto del cluster salió en **AD 67.2** (2026-02-10): [AD-444](https://bindpsp.atlassian.net/browse/AD-444) (formato de fecha), [AD-389](https://bindpsp.atlassian.net/browse/AD-389) (`EstadoTransaccion` ACREDITADO vs DEVUELTA), [AD-316](https://bindpsp.atlassian.net/browse/AD-316) (contracargo QR parcial rechazado sin webhook), [AD-298](https://bindpsp.atlassian.net/browse/AD-298) (falta `TransaccionId`). Capítulo posterior no incluido en la IDEA original: **AD 70.2** (2026-07-02) [AD-1348](https://bindpsp.atlassian.net/browse/AD-1348) — contracargo QR de una cuenta Wallet sin saldo quedaba PENDIENTE para siempre en vez de RECHAZADO; corregido para que Wallet informe el `motivoRechazo` real, aunque el Admin **todavía no lo muestra al comercio** (mejora sugerida, sin ticket propio a la fecha).

**Bug adicional (julio 2026) — `BOTONLIQ` no incluye devoluciones de días anteriores:**
- **Síntoma:** devoluciones hechas por Admin el 25/06 sobre transacciones del 18-19/06 no aparecieron en el archivo `A102BOTONLIQ260626.626` del día siguiente, pese a que Bind ya había desarrollado (a pedido de COTO) que las devoluciones de días anteriores figuren en el `BOTONLIQ` correspondiente al día en que se hace la devolución.
- **Confirmado como bug** por Bind (2026-07-02): en ambiente de prueba funciona correctamente, no así en producción. Ticket Jira Soporte de COTO: `BP-48516`.
- **Resolución:** ad hoc para esta ocurrencia — se subió manualmente al ticket un archivo con las devoluciones faltantes incluidas (2026-07-15, dos semanas después del reporte original). **No hay confirmación de que el fix de raíz haya salido a producción** — registrado como gap en `../../../2_areas/gaps_y_preguntas.md`.

> Fuente: Mail "Archivo de Liquidaciones -> A102BOTONLIQ260626.626 -> No incluyeron Devoluciones" — federico@coto.com.ar / pagomes@bind.com.ar / mvila@bind.com.ar (2026-07-01 a 2026-07-15).

**Cambio de formato (AD V70.3, julio 2026) — Botón LCK, headers y encoding:**
- El archivo de rendiciones (Botón LCK, ticket 2171 para Coto) pasa a diferenciar explícitamente las **devoluciones parciales**, que antes no salían discriminadas del resto — impacta a todos los clientes que consumen el archivo de rendiciones, no solo a Coto.
- Cambio técnico transversal al mismo archivo: headers de **Pascal Case → Snake Case** y encoding a **UTF-8 con BOM**.
- Despliegue planeado para el martes (no lunes, para evitar arrastrar un fin de semana sin observar el comportamiento) — comunicado a clientes pendiente, ver `tareas_producto.md` T-024.

**Ejecución del despliegue (2026-07-30) — pruebas finales y hallazgos:**

> Fuente: reunión "Análisis de riesgos - AD 70.3" (2026-07-30), minuta Gemini.

Tras el cambio de formato descripto arriba (y la baja parcial de alcance de julio, ver informe semanal abajo — solo DAD-1791/timeout pasó a v71, el resto del alcance de Botón LCK/rendiciones de Coto siguió como AD 70.3), el pase a producción finalmente se ejecutó el **2026-07-30 a las 16:00hs**, tras dos semanas de reprogramaciones. Cinco tickets en el alcance final:

- 🟢 Verde, sin cambio funcional: formato del archivo Excel de liquidaciones (headers con guiones/mayúsculas, encoding UTF-8).
- 🟢 Verde, con cambio funcional: Botón Link no debe mostrar registro de devolución cuando una transacción se devuelve en su totalidad el mismo día en que nació.
- 🟢 Verde, sin cambio funcional: redondeo del CFT (Costo Financiero Total) al final del cálculo en vez de sumar decimales individuales, para evitar arrastre de error de redondeo en liquidaciones con muchas transacciones.
- 🟡 Amarillo (ticket interno 855, réplica de un ticket de PMC): comercios sin certificado propio interrumpían la generación de certificados de IVA/ingresos brutos para el resto del lote — se agregó una validación para omitir ese comercio puntual y seguir con el resto sin cortar el proceso. Riesgo identificado como el de mayor probabilidad de falla (depende del cierre del proceso diario de PMC, ~16hs).
- 🟡 Amarillo, con cambio funcional (Coto): las devoluciones parciales no se informaban en el archivo Botón LCK — se agrega el detalle con ID de transacción `003` para que Coto pueda conciliar.
- **Excepción conocida, aceptada explícitamente por Pablo Gomes para no bloquear el pase:** cuando una transacción con tarjeta tiene **dos devoluciones parciales**, la segunda se informa con el detalle `002` en vez de `003` (y se informa como si fuera el total) — caso de baja frecuencia, queda para un fix posterior sin fecha comprometida.
- **Riesgo operativo señalado por el propio equipo de Fintexa (Andrea Orsini):** casi todas las pruebas de esta versión las hizo una sola persona de su lado, sin segunda revisión — riesgo de cobertura de testing en un cambio complejo.

**Informe semanal Adquirencia (13-17 julio 2026) — versión 70.3 cancelada, ticket crítico DAD-1791 y hotfix de timeout:**

> Fuente: Mail "Informe Semanal Adquirencia" — Melisa Belpassi (Fintexa, PM), 2026-07-17.

- **DAD-1791 (crítico de soporte)** — "[SOPORTE] RXT PROD - VARIAS ENT. - Operaciones no figuran en BD Transacciones (AD-588)": se trabajó en la versión 70.3 para incluirlo, pero **el deploy de 70.3 fue cancelado por Bind** — sus tickets, incluido DAD-1791, pasaron a la versión 71 (sin fecha de salida definida a la fecha).
- **Mitigación propuesta mientras tanto:** subir el timeout de Financial hacia el sistema de pagos externo de **500ms a 15s**, para bajar la cantidad de transacciones que no llegan a insertarse. Cambio de config en producción + reinicio secuencial de pods (servicio con 9 réplicas, sin caída de servicio), sin redeploy ni cambio de código — calificado de bajo riesgo por Fintexa, con mecanismo de contingencia para transferencias en curso durante el reinicio. Propuesta llevada también al grupo de Coordinación de versiones. **Ejecución confirmada (reunión "Análisis COBRO", 2026-07-20):** Melisa Belpassi coordina el reinicio del pipeline con Infraestructura (~30 min, fuera de horario laboral, sin pérdida de transaccionalidad esperada).
- **Hotfix DAD-2171 (Botón LCK/BOTONLIQ — ver más abajo) reprogramado:** iba a pasar el jueves 16/07 a las 15hs; se envió toda la documentación el miércoles, pero ese mismo día se decidió suspenderlo y reprogramarlo para el martes siguiente. **Seguimiento (reunión "Análisis COBRO", 2026-07-20):** desarrollo y pruebas de conciliación/visualización (QR vs. débito y transferencias) seguían con confusiones sobre la definición original del ticket — se sumó a Fintexa a los canales de QA para validar si las pruebas corren correctamente, con prioridad para el lanzamiento planeado para el día siguiente (2026-07-21).
- **DAD-1884 validado en producción:** el fix de "Procesos a cambiar en CVU Collect" (desplegado en 70.1 el 24/06) fue validado esta semana — Franco Giménez creó un nuevo lote de CVU para la entidad A161 y se confirmó comportamiento esperado en producción.

**Bug detectado (no resuelto, 2026-07-16) — transacciones con split después de las 17:00hs se acreditan recién al día siguiente:** el débito se ejecuta correctamente en el horario esperado, pero el crédito de la pata split queda pendiente y el banco/Coelsa lo acredita recién al día siguiente. No es una falla del split en sí (que sí se ejecuta), sino de la acreditación posterior de esa pata. Ver `tareas_producto.md` T-023.

> Fuente: reunión "Análisis de Riesgos - AD V 70.3" (2026-07-16), minuta Gemini.

**Informe semanal Adquirencia (20-24 julio 2026) — timeout confirmado, versión 71 acotada, caso GST:**

> Fuente: Mail "RE: Informe Semanal Adquirencia" — Melisa Belpassi (Fintexa, PM), 2026-07-24.

- **Mitigación de timeout Financial (DAD-1791) confirmada en producción:** desde que se aplicó el cambio de config el miércoles 22/07, Fintexa monitoreó y **no volvió a ver transacciones que no se inserten** — cierra el loop del hotfix descripto arriba.
- **Nueva versión 71 acotada, sale jueves 30/07:** al no poder desplegarse en los primeros 10 días del mes y ser la versión 71 completa demasiado extensa para adelantarla, por pedido de Matías Alzogaray se armó una versión acotada con los tickets ya listos para entrega (el resto sigue en pruebas).
- **Caso productivo cliente GST (ecosistema cerrado) — plazo de liquidación QR mal configurado:** el plazo de liquidación de las operaciones QR estaba en 1 en vez de 0. Caso ya cerrado; a partir de este hallazgo Fintexa empezó a revisar convenios y plazos de liquidación de otros clientes para armar una propuesta de mejora general.
- **DAD-2171 (Botón LCK/BOTONLIQ):** Fintexa adjuntó documento de análisis sobre la demora en la salida a producción del hotfix (no leído en esta corrida).

**Reactivación urgente del ticket 2171 (Coto) — 2026-08-03:**

> Fuente: reunión "Análisis COBRO" (2026-08-03), minuta Gemini.

El ticket 2171 (Botón LCK/rendiciones para Coto, ver arriba) — que Pablo Gomes había postergado previamente — vuelve a agenda con urgencia por pedido explícito del cliente. Persisten inconsistencias en las fechas de liquidación/proceso/negocio (especialmente en contracargos, donde las fechas se sobrescriben incorrectamente), que chocan con un ticket más amplio de mejoras en PDF/Excel ya en curso. Nicolás Colón se reúne con Euge (Coto) y Matías Alzogaray para decidir si se avanza con la solución acotada actual o se amplía el alcance — el equipo reconoce que una ampliación significativa no sería viable para el despliegue del día. Ver `tareas_producto.md` T-074.

**Informe semanal Adquirencia (27-31 julio 2026) — caso Tienda Nube, DAD-2171 pausado por inconsistencia, deploy V71 postergado:**

> Fuente: Mail "RE: Informe Semanal Adquirencia" — Melisa Belpassi (Fintexa, PM), 2026-07-31.

- **Caso Tienda Nube — operaciones no figuraban en BD:** la consulta `GetComercioConvenio()` se degradaba con la concurrencia que Tienda Nube genera todos los días a las 6am contra un único comercio. Paliativo aplicado: índice sugerido sobre la tabla `COMERCIO_CONV` (resolvió parcialmente) + escalado del recurso de la base compartida de **20 a 50 DTU** — el pico del 31/07 06hs se procesó sin excepciones ni degradación. Recomendación de fondo (pendiente, a la espera del OK de Nicolás Colón): incorporar **cache a nivel de API** para esta consulta en vez de depender de escalar recursos — feedback interno de Emma Vignoles: "hay que dejar de hacer todo por fuerza bruta, la cuenta la paga Bind y no tenemos billetera".
- **DAD-2171 (Botón LCK/BOTONLIQ, ver más arriba) completado pero pausado por inconsistencia recién detectada:** el desarrollo ya cerrado solo cubría `BOTONLIQ` (alcance acotado a pedido de la urgencia de Coto). Al validar fechas/formas de liquidación con Eugenia Vila se detectó que **los archivos generados por el sistema no coinciden entre sí** — hay un ticket más amplio, **DAD-2209**, que pedía corregir todos los archivos de rendición (no solo BOTONLIQ), y quedó fuera del alcance urgente. El pasaje de rendiciones a producción quedó frenado hasta que se decida el alcance real. Emma Vignoles: "mal organizado el requerimiento, mal el análisis, y peor las demoras — Coto lleva 3 semanas de atraso, al menos". Gap registrado en `../../../2_areas/gaps_y_preguntas.md`.
- **Deploy de la versión 71 postergado a lunes:** estaba previsto para el jueves 30/07, pero se corrió al lunes 03/08 para no arriesgar la demo de Coca-Cola Andina en producción del 31/07 (ver `1_proyectos/proyecto-coca-cola-andina/proyecto.md`). Errores ya reportados en los últimos tickets entregados fueron solucionados y puestos a disposición de QA externo.
- **AD-839 — Impuestos QRI no debitados (Wallet), ticket de desarrollo DAD-2235 en progreso**, a la espera de definir en qué versión se incluye. Emma Vignoles plantea, sin resolver, una pregunta funcional de fondo: si el lote de débito de impuestos hoy solo soporta una única entidad (falta de soporte multientidad) — gap registrado en `../../../2_areas/gaps_y_preguntas.md`.

**Decisión — botones de descarga separados (CSV/Excel) en vez de reemplazar el formato, y rollback de AD-1381 — 2026-08-03:**

> Fuente: reuniones "Análisis COBRO" y "AD 71 - Reunión de Pre-despliegue" (2026-08-03), minutas Gemini.

En el Go/No-Go de la versión AD 71 del mismo día (release general de Adquirencia, no específico de este PRD), el equipo decidió revertir en `main` el ticket **AD-1381** — que cambiaba el formato de exportación de transacciones de CSV a Excel — porque afecta a los clientes que automatizan su conciliación sobre el formato CSV previo; no se les puede migrar el formato sin aviso. En paralelo, en "Análisis COBRO", el equipo llegó a una salida equivalente por otro camino: en vez de reemplazar el formato, ofrecer **botones separados de descarga estándar (CSV) y descarga Excel**, dejando que cada cliente elija — el equipo acordó definir rápido esta estrategia para evaluar si entra en la próxima versión. Criterio acordado para futuros cambios de formato de exportación: ofrecer ambas opciones y avisar a clientes con al menos 2 semanas de anticipación.

**Informe semanal Adquirencia (03-07 agosto 2026) — DAD-2171 en producción (v71.1), incidente AD-863, homologación GP urgente:**

> Fuente: Mail "RE: Informe Semanal Adquirencia" — Melisa Belpassi (Fintexa, PM), 2026-08-07.

- **DAD-2171 (Botón LCK/BOTONLIQ) sale a producción — versión 71.1, jueves 06/08.** Cierra el "pausado" de la entrada anterior: se agregó la funcionalidad de devoluciones parciales al archivo BOTONLIQ (ausente hasta ahora) y se resolvieron las incongruencias detectadas la semana previa — idempotencia del archivo según hora de corrida, transacciones diferidas creadas de noche que no se informaban, devoluciones totales de QR no registradas, devoluciones parciales duplicadas/mal tipificadas, y el cálculo del plazo de liquidación en fines de semana. **Sigue en trabajo** lo detectado durante el desarrollo del ticket — no está 100% cerrado pese al deploy. El ticket más amplio DAD-2209 (corregir todos los archivos de rendición, no solo BOTONLIQ) sigue sin alcance confirmado. Ver `tareas_producto.md` T-018/T-074 y ficha de cliente COTO.
- **Versión 71 a producción sin incidentes (lunes 03/08).**
- 🚨 **Incidente AD-863 (06/08, ~1 hora, impacto alto) — pérdida de habilitación de POS con Global Processing en 5 entidades productivas.** Causa raíz: un intento de eliminar una regla de pago sobre la entidad de pruebas `DemoBindPsp` (ticket AD-862) afectó también a 5 entidades productivas, por un defecto en el endpoint de eliminación de reglas que no filtraba correctamente por entidad — se perdió la Regla N.º 3 (habilitación del procesador GP) y varios comercios no podían operar con terminales POS. Se restauró manualmente la regla en cada entidad afectada; servicio normalizado a las 10:15hs. Acción correctiva: corregir el filtro del endpoint para que la eliminación afecte solo a la entidad seleccionada + agregar casos de prueba sobre modificaciones de reglas críticas.
- ⚙️ **Versión 71.2 — QR masivo para Provincia NET, en armado.** Provincia NET pidió pruebas en producción con generación masiva de QRs asociados a deudas para la semana del 10/08 (ver `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md`). Requiere pasar a producción la **API de Deuda**, que trae cambios de contrato en campos de respuesta (`montoPagado`, `montoPendiente`, `MontoProximoVencimiento`, `MontoTotal`) y en `DevolucionDeuda` — Fintexa pidió reunión de impacto para alinear la comunicación a clientes antes del pase.
- 🔧 **Homologación urgente con Global Processing — deadline 13/08, en riesgo.** GP notificó 3 cambios de producción obligatorios antes del 13/08: v2.7 (URLs de alta/actualización de subcomercios), v2.8 (URL de autenticación) y v2.9 (validaciones sobre URL de comercios) — más un bug nuevo detectado (creación de comercio falla si la fecha de nacimiento del titular se envía en null). Fintexa reporta **varias incidencias abiertas del lado de GP que ponen en riesgo el plazo**: en la 2.8 GP no especificó cuál URL cambiar, avisaron que tras implementar hasta 2.9 va a hacer falta volver a dar de alta algunos comercios, y aparecieron errores 05 de pago al dar de alta comercios nuevos en STG. Se está tratando directamente con Alan Martínez y Gonzalo Rivera (Bind). Ver `tareas_producto.md` (nueva tarea 🔴, deadline 13/08) — no confundir con el frente ya trackeado en T-082 (URL de comercios electrónicos e-commerce/Edits 26-42, alcance distinto: ese ya tiene ticket `AD-1510` cargado y análisis cerrado del lado de Bind).
- 🗒️ **Versión 72 en armado**, fecha prevista 17/08 (a confirmar).

---

> El producto **Liquidador** (API "Informar nueva Transacción para Liquidar", clientes Traditum y Newpay PMC) se extrajo a [liquidador_terceros_traditum_newpay.md](liquidador_terceros_traditum_newpay.md) por ser un tema distinto de las devoluciones/contracargos.

## Crear archivo BATCH DEVOLUCIÓN en STG

Swagger a utilizar: `http://10.210.1.32/swagger/index.html`

Endpoint: **`POST /api/v1/rendicion-contracargo`** — genera una rendición de las transacciones con contracargos (job).

**Parameters:** entidad y fecha.

## Discrepancia de saldo Coto vía API: no es error de cálculo, es corte bancario antes de medianoche — 2026-08-05

> Fuente: reunión "Migra PSP 164" (2026-08-05), minuta Gemini.

Investigando un reclamo de descuadre de saldo de la cuenta recaudadora de **Coto**, el equipo (Gonzalo Rivera, Maria Eugenia Vila, Pablo Gomes) determinó que **no hay error de cálculo** en el saldo que expone la API — el saldo total, consultado vía APIBank (`transactions`, filtrando por `collectorId`/`accountId`), siempre está bien calculado incluyendo todos los movimientos.

**Causa real:** el banco (PIBán) hace su corte de día antes de la medianoche (ej. 23:10-23:41). Un movimiento ocurrido, por ejemplo, a las 23:13 ya queda con **fecha de valor del día siguiente** en el extracto bancario, mientras que la API lo sigue devolviendo como el último movimiento del día en que realmente ocurrió. Resultado: al comparar el saldo que informa la cuadratura (basada en extractos con el corte del banco) contra una consulta directa a la API a otra hora, aparece un desfasaje que en realidad es de **atribución de fecha**, no de monto.

**Recomendación operativa:** para obtener el saldo "cerrado" de un día sin ambigüedad, consultar los movimientos de la cuenta vía API en un horario fijo de la mañana (ej. 11:00-11:30), después de que el corte bancario ya haya sido absorbido, en vez de consultar en horario nocturno cercano al corte. El equipo decidió llevar este hallazgo a Emma Vignoles para explicar la limitación técnica y evaluar si la reunión de cuadratura nocturna sigue siendo necesaria.

---
*Ver también: [botones_de_pago_y_qr.md](botones_de_pago_y_qr.md) para el manejo de órdenes de venta e identificadores externos, [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) para el mecanismo de comisiones/interchange que precede a la liquidación, y [liquidador_terceros_traditum_newpay.md](liquidador_terceros_traditum_newpay.md) para el producto Liquidador (clientes que cobran por su cuenta).*
*Última actualización: 2026-08-12 — Renombrado desde `liquidaciones_y_devoluciones.md`; sección del producto Liquidador extraída a archivo propio (reestructuración PARA en cascada).*
