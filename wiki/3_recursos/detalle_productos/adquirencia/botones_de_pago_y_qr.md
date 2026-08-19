# Botones de Pago y QR — Configuración e Identificadores Externos

> Estado: en producción.

> Fuente: `wiki/3_recursos/conocimiento_interno/manual_para_configuraciones/` y `wiki/3_recursos/conocimiento_interno/documentacion_para_clientes/` (ingesta Notion). Contenido sustantivo transcripto tal cual (curls, IDs reales, pasos) — sin redactar. Metadata Notion (Tipo/Producto/Estado/Fuente) omitida.
>
> Ver [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) para la mecánica de fondo del canal QR (normativa, flujo Coelsa, alta de comercio, interchange).

---

## Estados de los Webhooks (WH) en COBRO PROD

> ⚠️ Fuente original en Notion es únicamente una imagen (captura de pantalla con la tabla de estados de los Webhooks en COBRO PROD) — no contiene texto adicional extraíble. No se pudo transcribir el contenido tabular; referirse a la fuente Notion original para el detalle visual, o solicitar al usuario una versión en texto.

---

## Documentación: ID externo en orden de venta y caja

> Alcance: informativo y apto para desarrollo. Aplica solo al producto Solución de Cobro.

### Objetivo
Instruir al desarrollador de la Entidad que quiere crear órdenes de venta utilizando un id externo propio, que también le sirva para consultar e identificarlas luego de su creación.

### Crear orden de venta pendiente con códigos externos

Endpoint ya existente al que se agregaron los campos necesarios para esta funcionalidad. Crea una orden de venta pendiente asociada a una caja para que, cuando alguien lea el QR estático de la misma, deba pagar el monto cerrado indicado.

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | POST | `https://gw-staging-qrbind.epays.services/bindentidad-transaction-v2/v2/api/v1.201/orden-venta-pendiente` |
| PRODUCCIÓN | POST | `https://api.bindpagos.com.ar/bindentidad-transaction-v2/v2/api/v1.201/orden-venta-pendiente` |

**Request body:**

| Atributo | Tipo | Req/Opc | Descripción |
|---|---|---|---|
| `codigoCaja` | string | OPCIONAL | Código de la caja en la cual se quiere crear la orden de venta. |
| `fechaNegocio` | datetime | REQUERIDO | Fecha y hora en que se crea la orden de venta. |
| `montoTotal` | decimal | REQUERIDO | Importe total a cobrar en el QR con la orden de venta. |
| `moneda` | string | REQUERIDO | Valores permitidos: `"ARS"`. |
| `tiempoExpiracion` | int | OPCIONAL | Tiempo de expiración de la orden de venta en segundos. Cumplido, pasa a vencida y no puede pagarse. Rango: `0` (mínimo) a `10000000` (máximo). Default: `600`. |
| `codigoExterno` | string | OPCIONAL | Código externo que la Entidad puede grabar en la orden de venta. No se puede crear una orden de venta con un `codigoExterno` si ya existe una en estado PENDIENTE o APROBADA con el mismo valor. |
| `codigoExternoCaja` | string | OPCIONAL | idExterno de la caja. Debe enviarse obligatoriamente `codigoCaja` o `codigoExternoCaja` (no ambos). |

**Ejemplo de request:**
```json
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-transaction-v2/v2/api/v1.201/orden-venta-pendiente' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
"codigoCaja": null,
"fechaNegocio": "2026-03-04",
"montoTotal": 4235.87,
"moneda": "ARS",
"tiempoExpiracion": 120
"codigoExterno": "ABC456",
"codigoExternoCaja": "XYZ789"
}'
```

**Response:**

| Atributo | Tipo | Descripción |
|---|---|---|
| `idOrdenVenta` | int | Id de la orden de venta creada. |
| `fechaExpiracion` | datetime | Fecha y hora en que expirará la orden de venta. |
| `codigoExterno` | string | Código externo que la Entidad grabó en la orden de venta. |

HTTP 201 - Creación exitosa:
```json
{
    "idOrdenVenta": 54638,
    "fechaExpiracion": "2026-04-21T23:43:51.9895086+00:00",
    "codigoExterno": "ABC456"
}
```

HTTP 422 - Error de negocio / HTTP 500 - Error desconocido:
```json
{
  "eventId": "string",
  "detalle": "string",
  "correlationId": "string",
  "errores": [
    {
      "codigo": "string",
      "titulo": "string",
      "detalle": "string"
    }
  ]
}
```

### Consultar orden de venta pendiente por código externo

Endpoint nuevo. Devuelve una lista de órdenes de venta que tengan asociado un valor de `codigoExterno`.

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1.201/orden-venta-por-codigoexterno/{codigoExterno}` |
| PRODUCCIÓN | GET | `https://api.bindpagos.com.ar/bindentidad-transaccionquery-v2/v2/api/v1.201/orden-venta-por-codigoexterno/{codigoExterno}` |

**Ejemplo de request:**
```json
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1.201/orden-venta-por-codigoexterno/ABC456' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

**Response:**

| Atributo | Tipo | Descripción |
|---|---|---|
| `idOrdenVenta` | int | Id de la orden de venta creada. |
| `codigoExterno` | string | Código externo que la Entidad grabó en la orden de venta. |
| `identificador` | string | — |
| `fechaProceso` | datetime | Fecha en que se creó la orden de venta. |
| `codigoCaja` | string | Código de la caja asociada. |
| `codigoComercio` | string | Código del comercio asociado. |
| `nombreComercio` | string | Nombre del comercio asociado. |
| `entidad` | string | Código de la entidad asociada. |
| `moneda` | string | `"ARS"` = Pesos argentinos. |
| `estado` | string | Valores: `"PENDIENTE"`, `"EN-PROCESO"`, `"INTENCION-PAGO"`, `"PRE-APROBADA"`, `"APROBADA"`, `"RECHAZADA"`, `"EXPIRADA"`. |
| `tipoOrden` | string | `"closed_amount"` = Monto cerrado. |
| `cuit` | string | CUIT del comercio asociado. |
| `montoTotal` | decimal | Importe de la orden de venta. |
| `formaPago` | int | Forma de pago permitida (puede ser vacío). |
| `productos` | object | Productos asociados (puede ser vacío). |

HTTP 200 - Consulta exitosa:
```json
{
	[{
  "idOrdenVenta": 123,
  "codigoExterno": "ABC456",
  "identificador": "123",
  "fechaProceso": "2026-01-26T16:13:54.271Z",
  "codigoCaja": "B00000455196",
  "codigoComercio": "C07663",
  "nombreComercio": "Supermercado Sol",
  "entidad": "A043",
  "moneda": "ARS",
  "estado": "PENDIENTE",
  "tipoOrden": "1",
  "cuit": "30847382931",
  "montoTotal": 53456.231,
  "formaPago": 1, 
  "productos": []
  }
  ]
}
```

### Webhook de aviso de pago

No hubo cambios en este webhook, solo se mapea el dato necesario. Se envía cuando una transacción pasa a estado ACREDITADO o RECHAZADA. Es el webhook documentado en: https://psp.bind.com.ar/developers/apis/notificacion-webhookpago

Si la orden de venta asociada a la transacción tiene un valor en `codigoExterno`, este se envía en el campo `Payload.MensajePago.IdentificadorReferencia`.

### Consulta de transacciones

No hubo cambios en este endpoint, solo se mapea el dato necesario. Es el endpoint documentado en: https://psp.bind.com.ar/developers/apis/consultar-transacciones

Si la orden de venta asociada a la transacción tiene un valor en `codigoExterno`:
- Puede buscarse indicándolo como valor del request query param `referenciasPago`.
- En el response body viene el valor de `codigoExterno` en el campo `transacciones.referenciasPago`.

### Crear caja indicando código externo

Endpoint ya existente para crear cajas, al que se agregó el campo necesario para esta funcionalidad.

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | POST | `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/{id}/sucursales/{idSucursal}/cajas` |
| PRODUCCIÓN | POST | `https://api.bindpagos.com.ar/bindentidad-comercio-v2/v2/api/v1.201/comercios/{id}/sucursales/{idSucursal}/cajas` |

**Request path params:** `id` (código del comercio, REQUERIDO), `idSucursal` (código de la sucursal, REQUERIDO).

**Request body:**

| Atributo | Tipo | Req/Opc | Descripción |
|---|---|---|---|
| `codigoCaja` | string | OPCIONAL | Nombre o denominación de la caja. |
| `soloOrden` | boolean | REQUERIDO | `true` = solo acepta cobros si hay orden de venta creada. `false` = acepta cobros aunque no haya orden de venta. |
| `tipoCajaId` | int | OPCIONAL | `1` = caja para cobro presente (físico en punto de venta). `2` = caja para cobro no presente (e-commerce, email, web, factura, cupón, etc). Default: `1`. |
| `codigoExterno` | string | OPCIONAL | Código externo indicado por la Entidad. |

**Ejemplo de request:**
```json
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/comercios/C07663/sucursales/S02825/cajas" -H "Content-Type: application/json" -H "Authorization: Bearer {{access_token}}" --data-raw "{     \"nombre\": \"Caja UNO\",     \"soloOrden\": true,     \"tipoCajaId\": 1,     \"codigoExterno\": \"CAJA123ABCDE\"}"
```

HTTP 201 - Creación exitosa:
```json
{
    "id": "B00000455197",
    "cvu": null
}
```

### Generar QR de caja usando código externo

Endpoint existente al que se agregó soporte para invocarlo con el código externo de la caja en lugar del código interno de Bind PSP.

**Endpoint:** `POST /api/v1.201/generacion-qr-estatico` — acepta `codigoCaja` **o** `codigoCajaExterno` (uno u otro, no ambos; error si se envían los dos o ninguno). Si el `codigoCajaExterno` no está asociado a ninguna caja de la entidad, responde error indicando que no existe una caja con ese código externo.

### `codigoDeuda` — mismo mecanismo aplicado a Deudas

El mismo patrón de identificador externo se extendió también a **Deudas** (no solo a Órdenes de Venta): si la entidad envía un valor en `codigoDeuda` al crear una deuda y esta se paga, la transacción asociada lo guarda en `referenciasPago` y el webhook de notificación lo trae en `Payload.MensajePago.IdentificadorReferencia` — mismo comportamiento que `codigoExterno` en Orden de Venta.

---

## Origen de negocio y cluster de bugs — cliente Hipódromo de Palermo (IDEA Jira PRD-112)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA [PRD-112](https://bindpsp.atlassian.net/browse/PRD-112) "HIPÓDROMO: Orden de venta con códigos externos" → Epic [AD-619](https://bindpsp.atlassian.net/browse/AD-619) "Codigos externos en orden de venta" (17 tickets de desarrollo retenidos, sin contar Tests). La funcionalidad de ID externo documentada arriba (§ "ID externo en orden de venta y caja") es la misma que construyó este Epic — lo que sigue es el delta que solo Jira revela: origen de negocio y bugs.

**Por qué se construyó**: el cliente Hipódromo de Palermo llegó a Bind PSP buscando **wallet services** (fondear saldo para cargar crédito en máquinas de juego). En el proceso surgió la oportunidad de ofrecerles el **ecosistema cerrado**, lo que implicaba reemplazar su forma actual de cargar saldo (QR dinámico de Mercado Pago en cada máquina) por QR estático de Bind PSP — de ahí la necesidad de identificar órdenes de venta y cajas con códigos propios del cliente, para no perder la referencia al migrar.

**Cluster de bugs encontrados durante el desarrollo/QA** (todos en Epic AD-619):

*Corregidos:*
- El response de creación de OV pendiente y de creación de caja no mostraba el `codigoExterno`/`idExterno` asignado ([AD-870](https://bindpsp.atlassian.net/browse/AD-870), [AD-871](https://bindpsp.atlassian.net/browse/AD-871)) — corregido en AD 68 (2026-03-30).
- El `codigoExterno` de la OV no se grababa en `Transaccion.referenciasPago` ni en `webhook.identificadorReferencia` ([AD-818](https://bindpsp.atlassian.net/browse/AD-818), [AD-819](https://bindpsp.atlassian.net/browse/AD-819)) — corregido en AD 68 (2026-03-30).
- **Bugs generales de Orden de Venta** (no específicos de código externo, encontrados incidentalmente y reportados por el cliente GST) — corregidos en AD 67.3 (2026-02-19), antes del release principal de la feature:
  - Una orden de venta vencida podía pagarse si el QR se había leído antes de vencer ([AD-629](https://bindpsp.atlassian.net/browse/AD-629)).
  - Crear una nueva orden de venta sobre la misma caja no expiraba la anterior, permitiendo pagar ambas ([AD-630](https://bindpsp.atlassian.net/browse/AD-630)).
  - Las órdenes de venta pagadas quedaban en estado `PRE-APROBADA` en vez de un estado final tipo `PAGADA` ([AD-651](https://bindpsp.atlassian.net/browse/AD-651)) — corregido en AD 69 (2026-04-29).

*No corregidos (estado "No aplica"/"En curso" en Jira — limitaciones conocidas, no confundir con "resuelto")*:
- El endpoint de consulta de OV por `codigoExterno` no muestra los productos asociados, y estos tampoco se visualizan en `dbo.OrdenVenta` ([AD-876](https://bindpsp.atlassian.net/browse/AD-876), [AD-872](https://bindpsp.atlassian.net/browse/AD-872)).
- El estado de la OV no se actualiza a `RECHAZADA` cuando el pago es rechazado ([AD-927](https://bindpsp.atlassian.net/browse/AD-927)).
- Mensajes de error inconsistentes entre los atributos `Descripcion` y `Monto` de productos cuando faltan en la creación de OV ([AD-918](https://bindpsp.atlassian.net/browse/AD-918), aún "En curso").

**Calibración de estimación**: la IDEA estimó 3 Story Points; la suma real de SP de los tickets de desarrollo retenidos fue ≈29 (AD-518=7, AD-621=3, AD-677=3, AD-651=3, resto entre 0 y 1). Diferencia de casi 10x — coherente con el patrón ya visto en PRD-56 de subestimar Epics que terminan destapando bugs de regresión en funcionalidad existente.

---

## Gap de mapeo en la lectura de QR: productos, sucursal y terminal (cliente Arcos Dorados, 2026-07-22)

> Fuente: Reunión "Consultar Arcos QR eco cerrado" (2026-07-22), minuta Gemini. Con Julieta Gimenez y Melisa Belpassi (Fintexa).

**Motivo del pedido:** Arcos Dorados (ecosistema cerrado, ver ficha en [`casos_de_uso_clientes.md`](../../../2_areas/clientes/casos_de_uso_clientes.md#arcos-dorados-mcdonalds)) tiene sus sistemas de ventas y de fidelización (loyalty) desarrollados por empresas distintas y no integrados entre sí. Para poder asociar promociones/fidelidad necesitan identificar, al momento de leer el QR con la billetera, a qué sucursal pertenece — y piden mandar un código externo propio de sucursal.

**Confirmación del bug ya conocido (AD-876/AD-872, §"Cluster de bugs" arriba):** Julieta Gimenez confirmó en vivo que el endpoint de lectura de QR (IEP/API Resolve) **sigue sin mapear el listado de productos** de la orden de venta en el `ViewModel` de respuesta — el mismo gap "No corregido" ya documentado, todavía sin resolver a esta fecha. La causa: la conexión existe (la IEP sí consulta la orden de venta), pero nunca se implementó el mapeo de los productos en la respuesta — funcionalidad muerta desde que se creó (nadie la usaba, nadie reclamó).

**Hallazgo nuevo — el mismo endpoint tampoco mapea sucursal ni terminal:** además de productos, la respuesta de lectura de QR **no incluye los campos `branchOffice` (sucursal) ni `terminal` (caja)** — llegan nulos/vacíos. Un intento de prueba con una orden de venta real devolvió el objeto `collector` nulo. Bind PSP sí tiene esta información internamente (código de sucursal y código de caja propios), simplemente no la está enviando en el response.

**Descartado como solución:** reutilizar el campo `producto` de forma genérica para que la Entidad meta ahí su propio código de sucursal — considerado una "chanchada" (parche no ordenado) que generaría un cambio de significado del campo para el resto de las integraciones.

**Decisión (consenso del equipo):** priorizar una solución estructurada en dos frentes, útil para cualquier cliente (no solo Arcos Dorados):
1. Mapear correctamente el listado de productos de la orden de venta en la respuesta de lectura de QR (arreglar el gap AD-876/AD-872 de una vez).
2. Agregar los campos de código de sucursal y código de caja/terminal (propios de Bind, no el externo de la Entidad) a esa misma respuesta.

Nota: esto **no resuelve directamente** el pedido de Arcos Dorados (ellos necesitan su propio código externo de sucursal, que Bind hoy no tiene modelado — solo existe código externo de caja, ver `codigoExternoCaja` arriba) — es un paso previo de higiene que además deja el sistema mejor preparado para una eventual extensión con código externo de sucursal a futuro.

**Próximo paso:** Julieta Gimenez y Melisa Belpassi evalúan el esfuerzo técnico antes de que Pablo Gomes cree los tickets formales — ver `tareas_producto.md` T-049.

---

## Documentación: nuevos filtros en endpoints de consulta para RIPSA-DESA

> Alcance: informativo y apto para desarrollo. Aplica solo para el producto Solución de Cobro, para el cliente RIPSA. Ver también [boton_simple_2_0.md §9](boton_simple_2_0.md) para el origen de producto (IDEA Jira PRD-87) y el cluster de bugs de QA encontrados al construir estos mismos endpoints (paginación, camelCase, fechaDePago).

### Objetivo
Instruir al desarrollador de la Entidad sobre los agregados realizados en los endpoints de consulta de links de pago y consulta de deudas, solicitados por RIPSA.

### Obtener un listado de links de pago

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/getFilteredPaymentLinks[?FechaDesde][&FechaHasta][&Status][&Page][&Take][&Email][&Dni][&PayFrom][&PayTo][&BinNumber][&CardBrand][&CardType]` |
| PRODUCCIÓN | GET | `https://api.bindpagos.com.ar/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/getFilteredPaymentLinks[?FechaDesde][&FechaHasta][&Status][&Page][&Take][&Email][&Dni][&PayFrom][&PayTo][&BinNumber][&CardBrand][&CardType]` |

**Query params:**

| Atributo | Tipo | Req/Opc | Descripción |
|---|---|---|---|
| `FechaDesde` | string | OPCIONAL | Fecha desde creación del link de pago. |
| `FechaHasta` | string | OPCIONAL | Fecha hasta creación del link de pago. |
| `Status` | string | OPCIONAL | Nuevo=`1`, Pendiente=`2`, Completado=`3`, Error=`4`, Cancelado=`5`, Reversado=`6`, Rechazado=`7`. |
| `Page` | int | OPCIONAL | Número de página. |
| `Take` | int | OPCIONAL | Cantidad de elementos por página. |
| `Email` | string | OPCIONAL | Correo electrónico del link de pago. |
| `Dni` | string | OPCIONAL | DNI del link de pago. |
| `PayFrom` | string | OPCIONAL | Fecha desde pago del link de pago. |
| `PayTo` | string | OPCIONAL | Fecha hasta pago del link de pago. |
| `BinNumber` | string | OPCIONAL | BIN de la tarjeta del link de pago. |
| `CardBrand` | string | OPCIONAL | `VISA`, `MASTERCARD`, `AMEX`. |
| `CardType` | string | OPCIONAL | Crédito=`1`, Débito=`2`. |

**Ejemplo de request:**
```json
curl -v -X GET "https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/getFilteredPaymentLinks?FechaDesde=2026-02-23&FechaHasta=2026-02-15&Page=1&Take=5" -H "Cache-Control: no-cache" -H "Authorization: Bearer {{access_token}}"
```

**Ejemplo de response (HTTP 200):**
```json
{
    "items": [{
        "guid": "056723d5-e26b-4faf-8c48-0354dd2748ca",
        "currency": "1",
        "totalAmount": 10243.75,
        "description": "EDELAP S.A.",
        "tsCreate": "2026-02-23T15:56:14.5559739",
        "cardType": "1",
        "status": "3",
        "expirationDate": "2026-02-23T13:03:40",
        "items": [{
            "paymentItemId": 21370,
            "amount": 10243.75,
            "quantity": 1,
            "description": "CNV-3604126-3-1"
        }],
        "service": "3",
        "installmentQuantity": 1,
        "installmentAmount": 10243.75,
        "user": {
            "userId": 6525,
            "firstName": null,
            "lastName": null,
            "dni": 12345678,
            "email": "facundobarreiros@gmail.com"
        },
        "payDate": "2026-02-23T15:57:39",
        "successUrl": "http://localhost:52953/estado-del-pago/pago-exitoso?callBack=http://localhost:52953/tramites/convenio?paymentSuccess=true",
        "errorUrl": "http://localhost:52953/estado-del-pago/error-al-pagar?callBack=http://localhost:52953/tramites/convenio?paymentError=true",
        "deudaId": null,
        "clientReference": "7254474",
        "binNumber": "529991",
        "cardBrand": "MASTERCARD",
        "lastNumbers": "0015"
    }],
    "total": 1355,
    "page": 1,
    "pages": 271
}
```
> Nota: response de ejemplo truncado a un solo ítem representativo; ver la fuente Notion para el listado completo de ejemplo (6 ítems).

### Obtener un listado de deudas

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/bindentidad-deuda-v2/v2/api/v1.201/Deudas?CodigoComercio={CodigoComercio}[&CodigoExterno][&DeudaId][&Start][&Length][&FechaDesde][&FechaHasta][&Estado][&FechaCobro]` |
| PRODUCCIÓN | GET | `https://api.bindpagos.com.ar/bindentidad-deuda-v2/v2/api/v1.201/Deudas?CodigoComercio={CodigoComercio}[&CodigoExterno][&DeudaId][&Start][&Length][&FechaDesde][&FechaHasta][&Estado][&FechaCobro]` |

**Query params:**

| Atributo | Tipo | Req/Opc | Descripción |
|---|---|---|---|
| `CodigoComercio` | string | REQUERIDO | Código del comercio en donde se crearon las deudas. |
| `CodigoExterno` | string | OPCIONAL | Identificador externo de la entidad en la deuda. |
| `DeudaId` | string | OPCIONAL | Identificador de la deuda. |
| `Start` | int | OPCIONAL | Número de orden de deuda inicial en la consulta. |
| `Length` | int | OPCIONAL | Cantidad de elementos por página. |
| `FechaDesde` | string | OPCIONAL | Fecha desde creación de la deuda. |
| `FechaHasta` | string | OPCIONAL | Fecha hasta creación de la deuda. |
| `Estado` | string | OPCIONAL | `PRECARGADO`, `PENDIENTE`, `EN PROCESO`, `PAGADA`, `PAGADA PARCIALMENTE`, `CANCELADA MANUAL`, `CANCELADO`. |
| `FechaCobro` | string | OPCIONAL | Fecha en que se realizó el pago de la deuda. |

**Ejemplo de request:**
```json
curl -v -X GET "https://gw-staging-qrbind.epays.services/bindentidad-deuda-v2/v2/api/v1.201/Deudas?CodigoComercio=C02086&Start=1&Length=5&FechaDesde=2026-02-15&FechaHasta=2026-02-23" -H "Cache-Control: no-cache" -H "Authorization: Bearer {{acceess_token}}"
```

**Ejemplo de response (HTTP 200), incluye el QR estático como string EMVCo (`detalleEspecifico.data`):**
```json
[{
    "id": 9647663,
    "codigo": "855893b3-8281-471d-a1a0-833452b3615f",
    "codigoExterno": {
        "codigoDeuda": "7254473",
        "codigoAuxiliar1": null,
        "codigoAuxiliar2": null,
        "Contexto": {}
    },
    "codigoCaja": "B00000791123",
    "codigoSucursal": "S19481",
    "codigoComercio": "C23262",
    "codigoEntidad": "A064",
    "nombreDeuda": null,
    "montoTotal": 10243.75,
    "moneda": 0,
    "motivo": "EDELAP S.A.",
    "tipoOrden": 0,
    "estado": 7,
    "estadoDescripcion": "CANCELADO",
    "fechaCreacion": "2026-02-23T15:54:44.9659199+00:00",
    "vencida": true,
    "vencimientos": 3,
    "montoProximoVencimiento": 10243.75,
    "fechaProximoVencimiento": "2026-02-23T13:02:10.4304274-03:00",
    "MedioPagoDisponibles": [{
        "id": 9747858,
        "nombre": "QR",
        "formaPago": 1,
        "formaPagoDescripcion": "QR",
        "detalleEspecifico": {
            "data": "00020101021102080000000041370012com.TESTbind98114668759911499020143360032B00000791123OD000096476639ETA0645015001120322678275512600220000531905064067232629520457345802AR5906EDELAP6014CABA - Almagro6108C1006ACT530303262100706S1948181080004A06463044FD7"
        },
        "habilitado": true
    }],
    "pagos": [],
    "esBoton20": false
}]
```

---

## Asociar productos a transacción (Deuda y Orden de Venta) — cliente Ministerio de Justicia

> Fuente: Jira `bindpsp.atlassian.net`, Epics **"Ministerio de Justicia - Asociar productos a transacción"** y **"Ministerio de Justicia - Cobro en POS"**, publicadas entre W 68 (2026-03-30) y W 70.1 (2026-06-24) — backfill vía `/sync_releases`.

**Qué resuelve**: permite que un comercio adjunte un detalle de productos/ítems (`jsonProductos`) a una **Deuda** ([AD-509](https://bindpsp.atlassian.net/browse/AD-509), W 68) o a una **Orden de Venta**, para que ese detalle viaje con la transacción hasta el webhook de aviso de pago ([AD-381](https://bindpsp.atlassian.net/browse/AD-381), W 68) y quede consultable después ([AD-378](https://bindpsp.atlassian.net/browse/AD-378), W 68; expuesto también en `GET Deuda` de la API CardNotPresent — [AD-1005](https://bindpsp.atlassian.net/browse/AD-1005), W 69).

**Caso de uso concreto — Ministerio de Justicia, cobro en POS**: el POS del comercio, en pantalla de inicio, muestra un único botón que consulta si hay una **orden de venta pendiente en la caja** asociada ([AD-578](https://bindpsp.atlassian.net/browse/AD-578), W 70.1) — si la OV pendiente tiene medio de pago tarjeta o QR ya definido, dirige directo a ese flujo de cobro; sin medio definido, pide elegir. No permite tipear un monto libre: solo cobra lo que ya existe como OV. El **código externo de la orden de venta** viaja hasta la transacción pagada por POS ([AD-771](https://bindpsp.atlassian.net/browse/AD-771), W 70.1), y los productos asociados a esa OV se propagan igual que en el camino de Deuda ([AD-647](https://bindpsp.atlassian.net/browse/AD-647), W 70).

**Cluster de bugs de estabilización** (todos en Botón Simple 2.0/Deuda, encontrados al construir/usar este flujo):
- El atributo `valor` de la descripción de deuda pagada con Transferencia se mapeaba incorrecto en los webhooks ([AD-943](https://bindpsp.atlassian.net/browse/AD-943), W 68).
- El CVU de la deuda no se daba de baja cuando la deuda pasaba a `PAGADA` o `VENCIDA` ([AD-942](https://bindpsp.atlassian.net/browse/AD-942), W 68) — mismo patrón de fuga de recursos del pool de CVUs ya documentado en [boton_simple_2_0.md §3](boton_simple_2_0.md).
- Al transferir un monto menor al esperado, quedaba un pop-up viejo visible detrás del nuevo ([AD-917](https://bindpsp.atlassian.net/browse/AD-917), W 68) — mejora de UX/UI relacionada ([AD-767](https://bindpsp.atlassian.net/browse/AD-767), W 68).
- `GET Deuda` de una deuda vencida con pago parcial daba error ([AD-999](https://bindpsp.atlassian.net/browse/AD-999), W 69); se habilitó permitir devolución de una deuda vencida con pago parcial ([AD-769](https://bindpsp.atlassian.net/browse/AD-769), W 69) y considerar pagos hechos luego del vencimiento de la deuda (ver [boton_simple_2_0.md §10](boton_simple_2_0.md), AD-971).

## Carga masiva de deudas — cliente ProvinciaNET

> Fuente: Jira, Epic **"Carga masiva de deudas para ProvinciaNET"** — [AD-496](https://bindpsp.atlassian.net/browse/AD-496) (15 SP, generación manual masiva de QRs, AD 67.X 2026-02-09) y [AD-660](https://bindpsp.atlassian.net/browse/AD-660) (3 SP, automatización del proceso vía **SFTP**, AD 69 2026-04-29). Cliente que necesita generar en lote un gran volumen de QRs de cobro (deudas/facturas provinciales) — primero como proceso manual, luego automatizado por transferencia de archivos.

### Mejoras al Monitor de API Deuda (AD 71.2 FIX, 2026-08-12)

> Fuente: Jira, versión AD 71.2 FIX (PNET), tickets AD-1515/AD-1516/AD-1517/AD-1518 (todos "Desarrollo para PNET, no requiere testing", Andrea Orsini). Referencian internamente el Jira de Fintexa (DAD-2045, DAD-2001, DAD-2000, DAD-1778) — sin Epic Link de Bind PSP, sin SP cargados.

- **Manejo de archivos fallidos** ([AD-1518](https://bindpsp.atlassian.net/browse/AD-1518)): si un archivo está bien nombrado pero mal generado (ej. falta un dato obligatorio en alguna fila), hoy queda indefinidamente en la carpeta `En_Proceso` con estado `ERROR` en `dbo.EjecucionFlujo`, bloqueando el procesamiento del resto de los archivos en `A_Procesar`. Fix: se crea una carpeta `Fallidos` en el Storage; el Monitor mueve ahí los archivos con estado `ERROR`. El archivo queda comprimido (se elimina el `.csv` suelto si existe) y descargable desde el endpoint de la API `FileManager`.
- **Salida comprimida** ([AD-1517](https://bindpsp.atlassian.net/browse/AD-1517)): los archivos de salida del proceso ahora se generan en `.zip`, para evitar problemas de descarga por tamaño.
- **Entrada comprimida** ([AD-1516](https://bindpsp.atlassian.net/browse/AD-1516)): el Monitor ahora descomprime los `.zip` de entrada para poder procesar el `.csv` (contraparte del anterior, del lado de ingesta).
- **Archivado histórico** ([AD-1515](https://bindpsp.atlassian.net/browse/AD-1515)): se deja copia del archivo histórico procesado (`{nombre-archivo}_{fecha-proceso}.csv`) en `rendiciones/entidades/A026/QrMasivo/Historico`, se deja de copiar a `rendiciones/entidades/A026/QrMasivo/Procesados`, y una vez que el proceso del archivo actual queda `NOTIFICADO`, se mueven a `Historico` los archivos del procesamiento anterior que no correspondan al nombre recién generado.

> **Nota — no cruza con `1_proyectos/`:** esta misma versión (AD 71.2 FIX (PNET)) también publicó AD-861, AD-860 y AD-1140, ya documentados vía `/sync_meetings` (release v71.2 2026-08-10, ver abajo) y en `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md` y `1_proyectos/proyecto-ministerio/prd-134_ministerio_productos_bs20_pos/proyecto.md` — esta ingesta solo confirma la versión de publicación de esos tres.

## Cobro con tarjeta al leer un QR — billetera Modo (PRD-7, AD V71)

> Fuente: Reunión "AD V 71 - Análisis de riesgo" (2026-07-29), minuta Gemini. IDEA trackeada: PRD-7 — Cobrar QR con tarjetas (MODO) (Nicolás Colón, EN CURSO — proyecto en su propio Cerebro desde 2026-08-13) — Epic [AD-336](https://bindpsp.atlassian.net/browse/AD-336). Release en camino a producción, pospuesto al lunes por la demo Coca-Cola Andina (esta sección cubre solo la mecánica de producto).

Nueva funcionalidad: cuando una billetera digital (caso piloto: **Modo**) escanea un QR de cobro, además de pagar con los medios habituales (transferencia/CVU) puede pagar directamente con **tarjeta**, sin que el comercio necesite otro dispositivo.

- **Requisito técnico interno:** autenticación Bearer sobre External v2, base necesaria para habilitar el resto de las funcionalidades de cobro QR con tarjeta.
- **Nuevo endpoint `POST payment` con datos de tarjeta:** habilita que la billetera envíe instrucciones y procese el pago con tarjeta al escanear el QR.
- **`API Resolve` extendida en dos frentes:** (1) responde si el QR escaneado admite pago con tarjeta; (2) devuelve atributos de identificación del comercio que Modo necesita para aplicar sus propias promociones bancarias en el momento del pago.
- **Regla de habilitación por entidad/comercio:** nueva configuración para que cada entidad o comercio decida individualmente si acepta cobrar con tarjeta vía QR — no es un cambio global, conviven con comercios que solo aceptan los medios de pago QR actuales.
- **Riesgo de regresión identificado:** el equipo remarcó (a raíz de un incidente previo no detectado a tiempo con dólar CCL) la necesidad de probar el flujo con **múltiples billeteras** además de Modo antes de habilitar en producción — no alcanza con validar solo el caso nuevo, hay que confirmar que no rompe el QR estándar que usan Mercado Pago y otras.

---

## Ampliación del webhook de Deuda y cálculo de vencimientos (release v71.2, 2026-08-10)

> Fuente: Reunión "Análisis de riesgos Fix Provincia Net" (2026-08-10), minuta Gemini. Mismo release que habilita la carga masiva de deudas de Provincia NET (ver [proyecto.md PRD-66 §7](../../../1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md#7-seguimiento-pm)) — estos tickets viajan juntos por compartir la API de Deuda, pero son iniciativas separadas sin relación funcional con Provincia NET.

- **Webhook de pago/devolución de deuda — cliente Ministerio de Justicia:** se agregan los campos `montoTotal`, `montoPagado` y `montoPendiente` al webhook. Se decide un **pase parcial** (solo backend) para no exponer los datos al cliente hasta una versión posterior — evita que el cambio de contrato impacte a todos los clientes que ya consumen el webhook (ver `codigoDeuda`/`montoProximoVencimiento` arriba) sin la comunicación previa correspondiente. **Relación con [PRD-104](../../../1_proyectos/proyecto-ministerio/prd-104_ministerio_cobro_ripsa/proyecto.md) sin confirmar** — ese frente del proyecto Ministerio está en stand-by desde el 2026-07-28 (motivo desconocido); no está claro si este ticket es parte de esa misma iniciativa retomada o trabajo de infraestructura independiente sobre la API de Deuda que comparten varios clientes.
- **Simple Button 2.0 — incluir devoluciones en el cálculo de `montoProximoVencimiento`:** cambio funcional (modifica el valor del campo ya documentado arriba en "Obtener un listado de deudas"), impacta a clientes existentes y requiere aviso previo — clasificado riesgo amarillo.
- **Simple Button 2.0 — integración de devoluciones en Carnot:** nueva función de consulta para verificar el estado de las devoluciones; cambio funcional tanto en el endpoint de deuda como en Carnot — el equipo debatió si la prioridad debía ser amarilla o roja, sin cerrar en la reunión.

---

## QR estático para red física de retail — caso Western Union/SEPSA (discovery, 2026-08-12)

> Estado: discovery — no construido. Fuente: Reunión "QR PF red fisica" (2026-08-12), minuta Gemini. Participantes: Emma Vignoles, Andres Uranga, Guillermo Paolucci y Diego Martinez (Western Union), Gonzalo Rivera, Pablo Gomes. **Mismo cliente que la integración Bind-SEPSA ya trackeada** en `2_areas/direccion/oportunidades.md` OP-004 y en el gap `[2026-07-16]` de `../../../2_areas/gaps_y_preguntas.md` — este frente nuevo expande esa relación hacia la **red física de retail** (más allá del Botón de Pago ya en piloto).

**Objetivo de negocio:** llevar el cobro con QR (hoy solo en bocas propias/agentes de Bind) a las cadenas de retail que Western Union atiende con su sistema propio **SF2/BPFG** (ej. supermercados tipo Carrefour) — hoy esas cadenas solo cobran en efectivo por ese canal. El caso ancla mencionado es escalar a grandes cadenas corporativas (Carrefour).

**Mecánica acordada (nivel diseño, sin desarrollo iniciado):**
- SF2 sigue siendo quien busca la deuda/genera la orden con la entidad — Bind PSP solo agrega el QR como nuevo medio de pago en el mismo flujo que hoy usan para efectivo, replicando el patrón que Western Union ya usa con Redlink.
- **QR de pago y QR de extracción deben ser dos códigos separados** (no unificables) — requisito de Compliance: el tipo de transacción "extracción en caja" necesita quedar identificado explícitamente, y hoy no hay forma de indicarlo dentro de los conceptos de un cobro normal.
- **Topes de extracción preliminares** (a confirmar con Compliance): **$5M por transacción, $25M acumulados por mes por CUIT** — mismo criterio que ya aplica a clientes de Bind PSP en general, para frenar a un usuario de otra billetera (no cliente directo, sin documentación de respaldo) que intente sacar montos altos por una caja de Western Union.
- **Alcance inicial: solo saldo en cuenta.** Integración con MODO (pago con tarjeta) está en desarrollo, estimada para fin de año.
- **Devoluciones totales y parciales soportadas** del lado de Bind PSP — automáticas a la billetera del usuario cuando el cobro se procesa pero no se puede imputar en SF2 (mismo patrón que otros clientes de QR).
- **Liquidación:** una CBU Corta U de BIN PCP a nombre de Western Union, con el arancel descontado — evaluando pasar de facturación mensual a **autorretención diaria** del arancel (evita el proceso administrativo de orden de compra recurrente).
- **CUIT de Pago Fácil para todos los QR** de este esquema, para aplicar el arancel reducido por operatoria extrabancaria — no hace falta crear una entidad separada por cada cadena de retail, el sistema puede rastrear por terminal internamente.
- **Conciliación:** archivos batch de detalle de transacciones para que Western Union pueda rendir contra SF2.

**Próximos pasos:** reunión presencial con equipo técnico de Western Union para diagramar el flujo de integración a cadenas corporativas; Emma Vignoles comparte documentación de API de QR estático/consulta de órdenes/conciliación; armar un documento de requerimientos comerciales (BRD) antes de definir alcance técnico final; Compliance confirma los topes de extracción definitivos.

---
*Ver también: [configuracion_de_entidades.md](configuracion_de_entidades.md) para el alta de entidades/comercios/cajas, y [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) para la mecánica interna del canal QR.*
*Última actualización: 2026-08-14 — `/sync_meetings`: nueva sección "QR estático para red física de retail — caso Western Union/SEPSA" (discovery, sin desarrollo iniciado). Ver reunión "QR PF red fisica" (2026-08-12) en `wiki/2_areas/control/log_reuniones.md`.*
*Última actualización anterior: 2026-08-10 — `/sync_meetings`: nueva sección "Ampliación del webhook de Deuda y cálculo de vencimientos (release v71.2)" desde la reunión "Análisis de riesgos Fix Provincia Net".*
