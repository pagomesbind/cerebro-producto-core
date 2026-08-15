# Cuentas menores y Eco cerrado — Wallet

> Estado: en producción.

Flujo de onboarding con cuentas de menores de edad (genérico y caso particular Arcos Dorados), reglas de negocio y segmentación de riesgo (Epic histórica "Cuentas para menores - MVP Arcos"), y funcionalidad de Eco Cerrado (cobro QR cuando billetera y comercio pertenecen a la misma organización).

---

## 0. Reglas de negocio del alta de cuenta de menor y segmentación de riesgo

> Fuente: Notion histórico, Epic **"Cuentas para menores - MVP Arcos"**. Complementa el flujo de endpoints ya documentado en §1 con las reglas de negocio detrás del alta y con una decisión de diseño de riesgo poco obvia.

- **La cuenta se crea deshabilitada y sin CVU**: al dar de alta una cuenta de menor (fecha de nacimiento < 18 años), el sistema NO crea el CVU todavía — solo registra la cuenta deshabilitada y la asociación con la cuenta del tutor (que debe ser una cuenta habilitada mayor de edad de la misma organización), quedando `pendienteTutor = true`. El CVU y la habilitación solo se conceden si el tutor aprueba explícitamente — nunca se puede habilitar la cuenta de un menor por otra vía.
- Los campos `fechaNacimiento`, `idCuentaTutor` son **opcionales** en el endpoint de alta de cuenta general — decisión deliberada para no romper los flujos existentes de altas de cuentas de mayores de edad.
- **Segmentación de riesgo diferenciada en ARDID**: cada organización tiene, por diseño, **dos segmentos ARDID por defecto** ("Standard {Entidad}" y "Standard {Entidad} menor"), con reglas de riesgo presumiblemente más restrictivas para el segundo. Al dar de alta una cuenta+CVU se asigna el segmento según la edad.
- **Proceso de background diario de "mayoría de edad"**: recorre las cuentas de menores y, cuando detecta que un titular cumplió 18 años, **reasigna automáticamente el segmento a "Standard {Entidad}"** tanto en Wallet como en ARDID — sin intervención manual. Aprendizaje reutilizable: cualquier producto que segmente por edad necesita este tipo de job de "graduación" automática, si no las cuentas quedan con reglas de riesgo de menor indefinidamente.

### 0.1 Precisiones adicionales (Jira PRD-17, Finalizada)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA **PRD-17** "Cuentas para menores - MVP Arcos Dorados" → Epic **WS-8** (14 tickets). Mismo MVP ya documentado por Notion en §0-1, con detalle técnico y decisiones de producto adicionales encontradas en los tickets de desarrollo y en los comentarios de la propia IDEA.

- **Payload exacto de segmentación (WS-53)**: el segmento diferenciado se implementa vía `ClientBankType` en Ardid con `externalClientTypeId` distinto por segmento — `0` para el segmento de mayores ("Standard {Entidad}") y `1` para el de menores ("Standard {Entidad} menor"), mismo nombre/descripción que el de mayores con el sufijo "menor" agregado. Se agregaron 6 campos nuevos en `WalletCuentaDB.OrganizacionesArdid` para persistir esta configuración por organización.
- **Cardinalidad tutor↔menor (aclarada por Producto en comentarios de la IDEA)**: un tutor puede tener más de un menor asociado, pero **un menor no puede tener más de un tutor**. Un mismo CUIL de menor no puede iniciar una segunda solicitud si ya tiene una pendiente de aprobación.
- **Cambio de tutor — dos casos de uso distinguidos por Producto**: (1) menor sin OB aprobado/rechazado que quiere cambiar de tutor para que otro lo apruebe → **sí entra en el MVP**; (2) menor con OB ya aprobado y cuenta+CVU dados de alta que quiere cambiar de tutor → **no entra en el MVP**.
- **Deshabilitación en cascada (regla de Producto, no implementada como validación de endpoint sino como criterio operativo)**: mientras la cuenta pertenezca al segmento "menores", siempre debe tener una cuenta de tutor **habilitada y activa** asociada — si se deshabilita la cuenta del tutor, debe deshabilitarse también la del menor y notificarse a la Entidad para que gestione la corrección. Relevante para el envío de notificaciones/reportes al tutor.
- **Responsabilidad de validaciones negativas delegada al cliente**: en una reunión de definición técnica con Arcos Dorados se acordó explícitamente que las **validaciones de casos negativos** (ej. permitir la creación de cuenta/CVU de un menor sin tutor asociado, o con aprobación pero sin verificarla) **quedan del lado de Arcos Dorados**, no como validación bloqueante de Bind PSP — decisión relevante si se integra un segundo cliente con este producto y no tiene el mismo control del lado propio.
- **Aclaración de diseño confirmada tras un bug reportado y no reproducido (WS-145)**: se reportó que enviar `aprobacionTutor=false` al endpoint de habilitar-menor dejaba la cuenta habilitada en la base de datos. Tras no poder reproducirse (ni por QA de Fintexa ni en un segundo intento), se confirmó que el endpoint de habilitar-menor **solo tiene camino de habilitación, no tiene circuito de rechazo** — es decir, no es que el rechazo fallara: el endpoint nunca estuvo pensado para procesar un rechazo explícito. Ticket cerrado como "No aplica".

## 1. Documentación cuentas menores (genérico)

**Alcance:** informativo y apto para desarrollo. **Objeto:** flujo de onboarding que incluye la posibilidad de crear cuentas para menores.

Diagrama de flujo de referencia: `Cuenta_menores_-_Flujo.pdf` (adjunto en la fuente Notion original).

### API — endpoints del flujo

A continuación se describen los endpoints usados en el flujo. Para los estándar del producto Onboarding se remite a la documentación pública; aquí se detallan los que no son estándar.

#### 1. Crear solicitud de OB
Escanea la foto y registra los datos necesarios para iniciar la solicitud. Pueden enviarse aparte los datos del DNI tipeados si hay problemas leyendo la foto.
Documentación: `https://psp.bind.com.ar/developers/apis/crear-solicitud-ob`

#### 2. Validar Renaper Datos
Valida la solicitud en Renaper Datos. Si la persona o el DNI no son válidos, se rechaza la solicitud.
Documentación: `https://psp.bind.com.ar/developers/apis/validar-renaper-datos`

#### 3. Registrar tutor
Asocia un tutor a la solicitud. El tutor debe ser una cuenta existente y habilitada en la organización de wallet; de no ser así, luego se devuelve un error al momento del alta en wallet.

- Endpoint: `POST {{BASE_URL}}/orquestador/api/v1/solicitudes/:id/tutor`
- Path params: `id` [REQ] id de la solicitud.
- Body: `idCuentaTutor` [REQ] id de la cuenta de wallet del tutor; `cuitTutor`, `nombreTutor`, `apellidoTutor`, `telefonoTutor`, `emailTutor` [OPC].

Ejemplo request:

```bash
curl --location 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/55e5c694-8c2c-4f38-214b-08de2092de6e/tutor' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{acces_token}}' \
--data-raw '{
    "idCuentaTutor": 645081,
    "cuitTutor": "23246165289",
    "nombreTutor": "Pablo Enrique",
    "apellidoTutor": "SERRA",
    "telefonoTutor": "1140123472",
    "emailTutor": "pserra.tecfin@gmail.com"
}'
```

HTTP 200 response body: vacío (`{}`).

#### 4. Actualizar email
Necesario para luego usarlo en el alta de la cuenta de wallet. Documentación: `https://psp.bind.com.ar/developers/apis/actualizar-email-solicitud-ob`

#### 5. Actualizar teléfono
Documentación: `https://psp.bind.com.ar/developers/apis/actualizar-telefono-solicitud-ob`

#### 6. Actualizar datos adicionales
Estado civil, ocupación, PEP/UIF/FATCA/OCDE, aceptación de T&C. Documentación: `https://psp.bind.com.ar/developers/apis/actualizar-datos-solicitud-ob`

#### 7. Consultar Nosis
Documentación: `https://psp.bind.com.ar/developers/apis/validar-nosis`

#### 8. Consultar Worldsys
Documentación: `https://psp.bind.com.ar/developers/apis/validar-listas-worldsys`

#### 9. Consultar UIF
Documentación: `https://psp.bind.com.ar/developers/apis/validar-uif`

#### 10. Consultar ARCA
Documentación: `https://psp.bind.com.ar/developers/apis/validar-padrona5`

#### 11. Validar matriz
Analiza resultados de las consultas externas y determina el estado final de validación. Documentación: `https://psp.bind.com.ar/developers/apis/validar-matriz-ob`

#### 12. Alta de wallet
Crea las cuentas de wallet para una solicitud.
- Si la persona es mayor de edad: crea cuenta y CVU, pasa el estado a **Aprobada a revisar**.
- Si es menor de edad: crea sólo la cuenta sin CVU, pasa el estado a **Menor Pendiente**.

Documentación: `https://psp.bind.com.ar/developers/apis/alta-wallet-ob`

#### 13. Habilitar menor
Habilita a un menor para operar. Al invocarlo, la organización determina que el tutor aprobó explícitamente al menor. Si la habilitación es válida, continúa con la creación del CVU del menor y pasa el estado a **Aprobada a revisar**. El tutor debe ser una cuenta existente y habilitada en la organización de wallet, y debe coincidir con el previamente registrado en la solicitud.

- Endpoint: `PATCH {{BASE_URL}}/orquestador/api/v1/solicitudes/:id/tutor/habilitar-menor`
- Path params: `id` [REQ].
- Body: `idCuentaTutor` [REQ].

Ejemplo request:

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/103d4f85-2975-44bb-214e-08de2092de6e/tutor/habilitar-menor' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
    "idCuentaTutor": 645081
}'
```

HTTP 200: vacío (`{}`). Ejemplo HTTP 422 (error):

```json
{
    "eventId": "1031",
    "detalle": "Se produjo un error llamando al metodo Handle() en Tf.Onboarding.Bind.Application.Commands.UpdateAltaCuentaCommand",
    "correlationId": "a5fefd8f-7ab7-4335-97a1-d1d6bdbe4b76",
    "errores": [
        {
            "codigo": "ERROR_ALTA_WALLET",
            "titulo": "Error al dar alta Wallet",
            "detalle": "Error al dar alta Wallet"
        }
    ]
}
```

#### 14. Cerrar solicitud
Cierra la solicitud de onboarding, determina el estado final y dispara el webhook de notificación a la Entidad. Si está todo bien, actualiza el estado a Aprobado.

- Endpoint: `PUT {{BASE_URL}}/orquestador/api/v1/solicitudes/:id/wallet`
- Path params: `id` [REQ].

Ejemplo:

```bash
curl --location --request PUT 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/002b5ba9-6ece-4d2e-5524-08de37f2f4ea/wallet' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}'
```

HTTP 200: vacío (`{}`).

#### 15. Webhooks de aviso

**Solicitud aprobada** — webhook enviado cuando una solicitud cambia a estado Aprobada:

```json
{
  "idSolicitud": "5b3e15b3-fe9e-4da1-2133-08de20921234",
  "idComercio": null,
  "habilitado": false,
  "fecha": "11/11/2025",
  "hora": "12:10",
  "apellidos": "MILEWSKI",
  "nombres": "Joaquin Lionel",
  "cuil": "20506254001",
  "documento": "50625123",
  "fechaNacimiento": "05/11/2010",
  "genero": "M",
  "email": "pagomes@bind.com.ar",
  "telefono": "1169991243",
  "externalRefid": "PruebaBindMenor1",
  "estado": null,
  "Wallet": {
    "cuenta": {
      "id": 649104,
      "cuitCuil": "20506251231",
      "nombre": "Joaquin Lionel",
      "apellido": "MILEWSKI",
      "razonSocial": null,
      "email": "pagomes@bind.com.ar",
      "celular": "1169991243",
      "habilitado": false
    },
    "cuentaCvu": {
      "id": 170867,
      "cvu": "0000532609880006491047",
      "nombre": "Joaquin Lionel MILEWSKI"
    },
    "cvuCreado": true,
    "idOrganizacion": 118,
    "pendienteTutor": false
  }
}
```

(Payload completo incluye además dirección, documento, nacionalidad, etc. — ver ejemplo completo en la fuente original si se necesita el detalle exhaustivo de campos.)

**Solicitud de menor pendiente** — webhook enviado cuando la solicitud cambia a estado Menor pendiente. Mismo formato que el anterior, pero con `estado: "Menor pendiente"`, `Wallet.cuentaCvu: null`, `Wallet.cvuCreado: false`, `Wallet.pendienteTutor: true`.

#### 16. Consultar solicitud por ID
Devuelve la información actual de una solicitud buscando por su ID; puede consultarse en cualquier momento desde su creación.
Documentación: `https://psp.bind.com.ar/developers/apis/consultar-solicitud-por-id`

La respuesta incluye todos los campos de validación (Renaper, Nosis, UIF, Worldsys, AFIP, Amazon, Seon, morfología), datos personales, archivos adjuntos (DNI frente/dorso, Renaper PDF), historial de movimientos de la solicitud y JSON crudo de Renaper. Ver ejemplo completo de response en el documento fuente para el detalle campo a campo (más de 60 atributos).

#### 17. Consultar solicitud por ID externo
Devuelve la información actual de una solicitud buscando por el `externalrefid`.
Documentación: `https://psp.bind.com.ar/developers/apis/consultar-solicitud-por-id-externo`

---

## 2. Documentación cuentas menores — Arcos Dorados

**Alcance:** informativo y apto para desarrollo. **Objeto:** este documento comprende únicamente al flujo de onboarding que integrará **Arcos Dorados**.

Diagrama de flujo específico: `Cuenta_menores_-_Flujo_Arcos_Dorados_-_v2.pdf` (adjunto en la fuente Notion original).

Los endpoints, requests, responses y webhooks documentados para este caso son **idénticos** a los descritos en la sección 1 (Documentación cuentas menores genérica) — mismos 17 pasos, mismos endpoints, mismos ejemplos de payload (incluyendo el caso de prueba `PruebaBindMenor1` / cuenta 649104 / organización 118). No se identificaron diferencias funcionales entre ambas fuentes más allá del alcance/cliente destinatario del documento.

---

## 3. Documentación Eco Cerrado

**Alcance:** informativo y apto para desarrollo. **Objeto:** dirigido específicamente al flujo de cobro con QR cuando tanto la billetera como el comercio corresponden a la **misma Organización**.

> Producto(s) de esta fuente: WALLET, ADQUIRENCIA.

### Flujo funcional

Referencias de diagrama: verde = interacción de la entidad con las APIs de COBRO; azul = interacción de la entidad con las APIs de WALLET; gris = acciones internas del sistema; línea punteada = asincrónico.

Diagramas de referencia (adjuntos en la fuente Notion original):
- Flujo de pago con canal eco cerrado y acreditación al comercio.
- Flujo de devolución de una transacción realizada por canal eco cerrado.

### API

#### Leer QR
La billetera de la entidad debe leer el QR interoperable para identificar que le pertenece y conocer el id de la orden interoperable (necesario para informar al momento del pago y poder cancelar la orden, evitando que otra billetera la pague luego).
Documentación: `Leer QR - Bind Pagos` (`https://psp.bind.com.ar/developers/apis/leer-qr`)

> ℹ️ Este endpoint se consume con credenciales de API del producto **WALLET**.

#### Crear comprobante
Al momento del pago, la entidad debe crear un comprobante para debitar el importe del saldo de la cuenta del usuario pagador, antes de informar el pago de eco cerrado en el comercio. Al momento de la devolución, debe crear un comprobante para acreditar el importe en la cuenta del usuario pagador, luego de confirmar la devolución desde el comercio.

Documentación: `Crear nuevo comprobante - Bind Pagos`. Para ambos casos, la entidad debe considerar crear nuevos tipos de comprobante que justifiquen cada concepto de movimiento, usando `Crear nuevo tipo de comprobante - Bind Pagos`.

> ℹ️ Este endpoint se consume con credenciales de API del producto **WALLET**.

#### Informar pago Eco cerrado
Registra en el sistema de cobro una transacción realizada por el canal Eco cerrado y realiza la liquidación.

> ℹ️ Este endpoint se consume con credenciales de API del producto **COBRO**.

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | POST | `https://gw-staging-qrbind.epays.services/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaPago` |
| PRODUCCIÓN | POST | `https://api.bindpagos.com.ar/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaPago` |

**Request body:**

| Atributo | Tipo | REQ/OPC | Descripción |
|---|---|---|---|
| `identificadorReferencia` | string | OPCIONAL | Identificador externo indicado por la entidad. Se valida idempotencia (no puede repetirse). Se graba en todos los movimientos asociados. |
| `identificadorProcesador` | string | REQUERIDO | Identificador del comprobante con que se debitó el saldo al usuario para informar esta compra. |
| `fechaPago` | datetime | OPCIONAL | Fecha en que se concretó el pago. |
| `identificadorOrdenVenta` | string | REQUERIDO | Identificación de la orden interoperable (`order.id` obtenido en la respuesta de Leer QR). |
| `formaPago` | string | REQUERIDO | Valor fijo: `SALDO_VIRTUAL`. |
| `importeBruto` | double | REQUERIDO | Importe bruto de la transacción. |
| `estadoTransaccion` | string | REQUERIDO | Valor fijo: `ACREDITADO`. |
| `moneda` | string | REQUERIDO | Valor fijo: `ARS`. |
| `comprador` | object | REQUERIDO | Información del comprador. |
| `comprador.identificadorPagador` | string | REQUERIDO | CUIT del usuario pagador. |
| `comprador.cuentaPagador` | string | REQUERIDO | CVU del usuario pagador. |

Ejemplo de request:

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaPago" -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Authorization: Bearer {{access_token}}" --data-raw "{
    \"identificadorReferencia\": \"ABCDE123456789\",
    \"identificadorProcesador\": \"4568789\",
    \"fechaPago\": \"2025-12-08T23:35:48.583532+00:00\",
    \"identificadorOrdenVenta\": \"9OC1D04EE87AB138B00000495128000000106393ET9000ZTOC5288C377AC\",
    \"formaPago\": \"SALDO_VIRTUAL\",
    \"importeBruto\": 15700.84,
    \"estadoTransaccion\": \"ACREDITADO\",
    \"moneda\": \"ARS\",
    \"comprador\": {
    \"identificadorPagador\": \"20374312349\",
    \"cuentaPagador\": \"0000532909000067076630\"
    }
}"
```

**Response:**

| Atributo | Tipo | Descripción |
|---|---|---|
| `identificadorTransaccion` | string | Identificador de la transacción en el sistema. |
| `fechaNegocio` | datetime | Fecha de inserción de la transacción. |

#### Informar devolución Eco cerrado
Registra en el sistema de cobro una devolución realizada por el canal Eco cerrado y realiza la liquidación.

> ℹ️ Se consume con credenciales de API del producto **COBRO**.
> ⚠️ Por el momento, no se encuentra disponible en el ambiente de prueba.

**Endpoint:**

| Ambiente | Método | URL |
|---|---|---|
| STAGING | POST | `https://gw-staging-qrbind.epays.services/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaContracargo` |
| PRODUCCIÓN | POST | `https://api.bindpagos.com.ar/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaContracargo` |

**Request body:**

| Atributo | Tipo | REQ/OPC | Descripción |
|---|---|---|---|
| `identificadorReferencia` | string | OPCIONAL | Identificador externo indicado al informar el pago de eco cerrado. |
| `identificadorTransaccion` | int | REQUERIDO | Identificador de la transacción acreditada. |
| `importeBruto` | double | REQUERIDO | Importe a devolver. |
| `parcial` | boolean | REQUERIDO | `true` = parcial, `false` = total. |
| `motivo` | string | OPCIONAL | Descripción o referencia del motivo del contracargo. |

Ejemplo de request:

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaPago" -H "Content-Type: application/json" -H "Cache-Control: no-cache" -H "Authorization: Bearer {{access_token}}" --data-raw "{
    \"identificadorReferencia\": \"ABCDE123456789\",
    \"identificadorTransaccion\": \"157732\",
    \"importeBruto\": 15700.84,
    \"parcial\": false,
    \"motivo\": \"solicitud del cliente\"
    }
}"
```

**Response:**

| Atributo | Tipo | Descripción |
|---|---|---|
| `id` | int | Identificador del contracargo. |
| `estado` | string | `PENDIENTE` (en proceso) / `ACEPTADO` (completada) / `RECHAZADO` (error, no se cursa). |
| `motivoRechazo` | string | Motivo en caso de rechazo. |

Ejemplo de response:

```json
{
	"id": 5687456,
	"estado": "ACEPTADO",
	"motivoRechazo": null
}
```

#### Webhook de creación de comprobante por cobro
Se dispara a la organización cuando el sistema de cobro crea un comprobante.

> ℹ️ Se envía a la URL configurada para webhooks de la organización en **WALLET**.

**Request body:**

| Atributo | Tipo | REQ/OPC | Descripción |
|---|---|---|---|
| `mensajeId` | string | OPCIONAL | Identificador del webhook. |
| `evento` | string | OPCIONAL | Nombre del tipo de evento. |
| `cuentaId` | datetime | OPCIONAL | Identificador de la cuenta en que se creó el comprobante. |
| `importe` | string | OPCIONAL | Importe del comprobante creado. |
| `comprobanteId` | string | OPCIONAL | Identificador del comprobante creado. |
| `referencia` | double | OPCIONAL | Valor de `identificadorReferencia`. |
| `tipoComprobanteId` | string | OPCIONAL | Identificador del tipo del comprobante (*). |
| `tipoComprobanteNombre` | string | OPCIONAL | Nombre del tipo del comprobante (*). |
| `tipoComprobanteSigno` | object | OPCIONAL | Signo del tipo del comprobante. |
| `fecha` | string | OPCIONAL | Fecha de creación del comprobante. |

Ejemplo:

```json
{
	"mensajeId": "537de36e-6d88-4218-a518-0435f384acb8",
	"evento": "COMPROBANTE_COBROQR",
	"cuentaId": 274409,
	"importe": 45.84,
	"comprobanteId": 155555,
	"referencia": "ABCDE123456789",
	"tipoComprobanteId": 409,
	"tipoComprobanteNombre": "RET_IIBB_SIRTAC Impuestos de Cobro QR Interoperable",
	"tipoComprobanteSigno": -1,
	"fecha":"2024-09-02T19:13:56.1110531+00:00"
}
```

(*) Tipos de comprobante que pueden informarse por este evento:

| tipoComprobanteId | tipoComprobanteNombre | tipoComprobanteCodigo | tipoComprobanteSigno |
|---|---|---|---|
| 400 | PERC_IVA Impuestos de Cobro QR Interoperable | PERC_IVA_COBQR | -1 |
| 403 | PERC_IIBB Impuestos de Cobro QR Interoperable | PERC_IIBB_COBQR | -1 |
| 405 | RET_IVA_3130 Impuestos de Cobro QR Interoperable | RET_IVA_3130_COBQR | -1 |
| 408 | RET_IIBB_RP Impuestos de Cobro QR Interoperable | RET_IIBB_RP_COBQR | -1 |
| 409 | RET_IIBB_SIRTAC Impuestos de Cobro QR Interoperable | RET_IIBB_SIRTAC_COBQR | -1 |
| TBD | Cobro QR Eco Cerrado | ECOC | 1 |
| TBD | Devolución de Cobro QR Eco Cerrado | DEVECOC | 1 |

> **Atribución de releases (vía `/sync_releases`, 2026-07-13):** el webhook `COMPROBANTE_COBROQR` (con envío por cola de baja prioridad y sin webhook cuando el débito cae a Recycle) se publicó en **W 65** (2025-11-17, [WS-33](https://bindpsp.atlassian.net/browse/WS-33), Epic "QRI PSP 184 acreditación en wallet"). Del lado de cuentas de menores: el alta con tutor pendiente ([WS-41](https://bindpsp.atlassian.net/browse/WS-41)) y la aprobación del tutor ([WS-40](https://bindpsp.atlassian.net/browse/WS-40)) salieron en **W 65.1** (2025-11-26), y la **segmentación en Ardid con "graduación" diaria a los 18** ([WS-53](https://bindpsp.atlassian.net/browse/WS-53), 15 SP — `externalClientTypeId=1`, segmento "Standard {Entity} menor") en **W 66** (2025-12-15).

## 3.1 Origen de negocio, lógica de comprobantes y cluster de bugs (Jira PRD-69, Finalizada)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA **PRD-69** "ECO Cerrado" → Epic **AD-97** (24 tickets: 15 Finalizados con contenido, 3 aún abiertos al momento de esta ingesta, resto Test/No aplica). La documentación técnica de §3 (endpoints, webhooks) ya estaba completa vía Notion; acá se agrega el **por qué** del desarrollo y la lógica de negocio detallada de comprobantes que generó la mayoría del cluster de bugs.

**Origen de negocio**: clientes con Wallet propia que además cobran con QR (Arcos Dorados, COTO) pueden resolver un pago en el mismo ecosistema (billetera y comercio de la misma organización) sin salir a Coelsa, ahorrando aranceles — pero Bind PSP sigue obligado a tratar esa operación como una transacción real a efectos de retener impuestos. La decisión fue construirlo del lado del equipo de **Cobro** por tener capacity libre en ese momento, aunque el caso de uso final vive tanto en Wallet como en Adquirencia.

**Lógica de comprobantes confirmada** (más detallada que la documentación técnica de §3):
- **Al acreditarse la transacción** (solo si el plazo de liquidación del comercio para este canal/forma de pago es `0`): se crea un comprobante de **crédito** (`ECOC`, signo `+1`) por el **importe neto** (bruto menos comisión), y un comprobante de **débito por cada impuesto** que corresponda (reutilizando los mismos tipos de comprobante ya usados en "QR acreditación en wallet") — si no aplica ningún impuesto, no se crea ninguno de estos.
- **Al devolverse (contracargo)**: se crea un comprobante de débito (`DEVECOC`) a la cuenta del comercio. La reversa de impuestos ya debitados es **condicional**: solo se reversan si la devolución ocurre el **mismo día** que la acreditación y es **total** — devoluciones parciales o de otro día no tocan los impuestos ya calculados/debitados.
- **Corrección de código/nombre de comprobantes de impuesto existentes**: los tipos ya usados en QR acreditación en wallet (`PERC_IVA_COBQR`, `PERC_IIBB_COBQR`, etc., ver tabla arriba) se renombraron a "Impuesto por cobro" en vez de "Impuestos de Cobro QR Interoperable" al generalizarse también a Eco Cerrado — y se agregó un nuevo tipo `REVCOBQR` ("Reversa devolución de cobro QR interoperable").
- **Contradicción resuelta con la tabla de arriba**: la fuente Notion marcaba `DEVECOC` como `TBD` con signo `1` — el ticket de desarrollo (AD-404) confirma que su signo real es **`-1`** (es un débito). Actualizado acá; si se usa la tabla de arriba como referencia rápida, considerar el signo de `DEVECOC` como `-1`, no `1`.

**Cluster de bugs — todos alrededor del cálculo de importe neto/bruto en las devoluciones** (mismo patrón que otros clusters de esta wiki: una funcionalidad de "devolución" sobre un objeto ya construido para el camino de cobro descubre inconsistencias de neto vs. bruto):
- El comprobante de débito de devolución debitaba al comercio el **importe bruto** en vez del **neto** ([AD-547](https://bindpsp.atlassian.net/browse/AD-547), AD 68 2026-03-30) — causaba que una devolución total fallara con "saldo insuficiente" (el comercio nunca tuvo el bruto acreditado, solo el neto).
- `ImporteNeto` y `ComisionComercio` quedaban **mapeados al revés** en la tabla de transacciones para la forma de pago 70 (Eco Cerrado) ([AD-463](https://bindpsp.atlassian.net/browse/AD-463), AD 67.2 2026-02-10) — el campo neto tenía el valor del bruto, y comisión tenía el valor del neto.

**Pendientes al momento de esta ingesta** (tickets aún no Finalizados): motivo real de rechazo no informado en el endpoint ni en el Admin al rechazarse un contracargo de Eco Cerrado (2 tickets relacionados), y error 422 en el endpoint de migración de comercio a este canal.

**Versiones de publicación de la mecánica base** (vía `/sync_releases`): crear comprobante de crédito ([AD-99](https://bindpsp.atlassian.net/browse/AD-99)) y ajustar endpoint de informar Eco Cerrado ([AD-98](https://bindpsp.atlassian.net/browse/AD-98)) en **AD 66** (2025-12-16); comprobante de débito por impuestos ([AD-213](https://bindpsp.atlassian.net/browse/AD-213)), endpoint crear devolución ([AD-184](https://bindpsp.atlassian.net/browse/AD-184)) y devolución debe crear comprobantes ([AD-290](https://bindpsp.atlassian.net/browse/AD-290)) en **AD 67.2** (2026-02-10) junto con [AD-404](https://bindpsp.atlassian.net/browse/AD-404) (integración Wallet, confirma signo de `DEVECOC`); mensaje de error mal mapeado ([AD-362](https://bindpsp.atlassian.net/browse/AD-362)), error de orden de venta inválida sin mapear ([AD-361](https://bindpsp.atlassian.net/browse/AD-361)) y pago aplicado sobre orden vencida ([AD-358](https://bindpsp.atlassian.net/browse/AD-358)) en **AD 66** también. Migración QR184: CVU de comercio no actualizado ([AD-604](https://bindpsp.atlassian.net/browse/AD-604), AD 68).
