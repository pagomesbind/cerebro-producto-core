# Pago Fácil — Link de Pago de Deuda (Cobro de Servicios)

> Estado: en producción. Contenido completo transcrito desde `wiki/3_recursos/conocimiento_interno/documentacion_para_clientes/documentacion_link_de_pago_deuda_pago_facil.md`. Reubicado desde `detalle_productos/transversal/pago_facil.md` en la reestructuración PARA en cascada (2026-08-12).
>
> Ver también, del Notion histórico (Epics "APIs para buscar deuda y cobrarla con BS2.0" y "Pago Facil: Multicredencial BS y no liquidar"): `detalle_productos/adquirencia/boton_simple_2_0.md §6` (búsqueda de deuda de Impuestos y Servicios vía BPG) y `§7` (modalidad ThirdPartyStore — Bind como plataforma pura sin ser comercio de registro).

---

# Alcance
El alcance de este documento es informativo y apto para desarrollo.
# Objetivo
El objetivo de este documento es explicar las funcionalidades del producto de link de pago con cobro de servicios y cómo deben integrarse sus clientes.
# Objeto
El objeto de este documento comprende únicamente el caso de uso de Pago Fácil.
# Flujo funcional
A continuación se describe el flujo de integración de un ente.

> Nota: el diagrama de flujo original es un adjunto nativo de Notion y no se pudo migrar a este archivo (`attachment:` no resuelve fuera de Notion). Documento original con la imagen renderizada: https://app.notion.com/2beb3646c94b80f0b24cf2284beed974

# Flujo UX/UI
A continuación se adjuntan los prototipos en donde se indica la experiencia del cliente para distintos casos de uso.
Link al Figma con el prototipo: [FIGMA PROTOTIPO](https://www.figma.com/proto/bz0WgFVrSEiRA3iTY0tWX8/Link-de-pago-para-pago-de-servicios?node-id=104-20&p=f&t=SfLaftigLrudWx1e-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=104%3A20&show-proto-sidebar=1)

> Para visualizar y navegar el prototipo de la forma más óptima, se recomienda ir a "Opciones" (Arriba a la derecha del Figma) y seleccionar "Ajustar al ancho"

En el prototipo se ejemplifican los siguientes casos de uso:
- Flujo A: Búsqueda, pago y confirmación de transacción exitosa, y el usuario tenía **sólo una deuda de monto cerrado** para pagar.
- Flujo B: Búsqueda, pago y confirmación de transacción exitosa, y el usuario tenía **más de una deuda de monto cerrado** para pagar.
- Flujo C: Búsqueda, pago y confirmación de transacción exitosa, y el usuario tenía **más de una deuda de monto abierto** para pagar.
- Flujo D: Búsqueda, pago y confirmación de transacción exitosa, y el usuario tenía **sólo una deuda de monto abierto** para pagar.
- Flujo E: Hubo un error en el procesamiento del pago.
- Flujo F: El pago fue aprobado pero luego hubo un error en la confirmación de la transacción.
- Flujo G: El link es inválido y no pudimos descifrarlo.
- Flujo H: El link es válido pero no se encontraron deudas pendientes para los datos de búsqueda.
- Flujo I: Hubo un error general al querer generar el checkout con los medios de pago.
- Flujo J: Hubo un error general al momento de la búsqueda de la deuda en BPG. (Error no esperado en Lookup)
- Flujo K: Hubo un error general al momento de actualizar la deuda en BPG. (Error no esperado en Update)
- Flujo L: Hubo un error al momento confirmar la transacción en BPG o respondió InProgress y no cambió de estado en enseguida.

# API

## Obtener token
Devuelve el token necesario para autenticarse y consumir las APIs de este producto. Ver [`3_recursos/arquitectura_sistema/entornos_y_autenticacion_oauth2.md`](../../arquitectura_sistema/index.md) para el detalle general de OAuth2/entornos — acá solo se documentan las particularidades de este producto.
### Endpoint
STAGING: POST https://login.microsoftonline.com/61ef5b89-8df3-499d-8c13-38fed5d09c72/oauth2/v2.0/token
PRODUCCIÓN: POST https://login.microsoftonline.com/3ee81fb8-f2e8-4475-aef2-c5902f9fb0c3/oauth2/v2.0/token
### Request

| Atributo | Tipo | REQ/OPC | Descripción |
| --- | --- | --- | --- |
| `client_id` | string | REQUERIDO | Id que identifica al cliente. Es indicado por Bind PSP al entregar los secretos a cada ente. |
| `client_secret` | string | REQUERIDO | Contraseña secreta. Es indicado por Bind PSP al entregar los secretos a cada ente. |
| `grant_type` | string | REQUERIDO | Valor fijo "client_credentials" |
| `scope` | string | REQUERIDO | Valor fijo por ambiente. Para STAGING: "api://staging-bind.epays.services/.default"; Para PRODUCCIÓN: "api://bindpagos.com.ar/.default" |

Ejemplo de request:
```json
curl --location 'https://login.microsoftonline.com/61ef5b89-8df3-499d-8c13-38fed5d09c72/oauth2/v2.0/token' \
--form 'client_id="{{client_id}}"' \
--form 'client_secret="{{client_secret}}"' \
--form 'grant_type="client_credentials"' \
--form 'scope="api://staging-bind.epays.services/.default"'
```
### Response
Atributos del response body:

| Atributo | Tipo | Descripción |
| --- | --- | --- |
| token_type | string | Valor fijo "Bearer" |
| expires_in | int | Tiempo en que se expirará el token en segundos. |
| ext_expires_in | int | Tiempo en que se expirará el token en segundos. |
| access_token | string | Token a utilizar en el Authorization Header de todas las llamadas a las APIs. |

Ejemplo de response HTTP 200 (token truncado por longitud):
```json
{
    "token_type": "Bearer",
    "expires_in": 3599,
    "ext_expires_in": 3599,
    "access_token": "<JWT de ejemplo — ver Postman/colección de referencia del equipo>"
}
```

## Crear intención de pago
Devuelve una url para dirigir un usuario a pagar una deuda indicando los datos para su búsqueda.
### Endpoint
STAGING: POST https://gw-staging-qrbind.epays.services/entidad-deuda-debtmanagement/api/v1.201/operaciones/generar-intencion-de-pago
PRODUCCIÓN: POST https://api.bindpagos.com.ar/entidad-deuda-debtmanagement/api/v1.201/operaciones/generar-intencion-de-pago
### Request
Atributos del request body:

| Atributo | Tipo | REQ/OPC | Descripción |
| --- | --- | --- | --- |
| `datosBusqueda` | object | REQUERIDO | Objeto con lista de datos de input para buscar la deuda. |
| `datosBusqueda.dataList` | object | OPCIONAL | Objeto con lista de datos de input para buscar la deuda. Es el `DataList` tal cual para luego consumir el PALI. |
| `datosBusqueda.dataList.data[ { } ]` | array of objects | OPCIONAL | Array de objetos en que cada uno es un dato de input para buscar una deuda. Es el `Data` tal cual para luego consumir el PALI. |
| `datosBusqueda.dataList.data[ { } ].order` | string | OPCIONAL | Número de orden del dato requerido para buscar deuda. |
| `datosBusqueda.dataList.data[ { } ].name` | string | OPCIONAL | Nombre del dato requerido para buscar deuda. |
| `datosBusqueda.dataList.data[ { } ].value` | string | OPCIONAL | Valor del dato requerido para buscar deuda. |
| `motivo` | string | OPCIONAL | Texto descriptivo que se usará como título del detalle a pagar en el checkout que ve el usuario pagador. Si se envía vacío, se creará el link con el valor seteado a nivel del ente. |
| `fechaVencimiento` | datetime | OPCIONAL | Fecha de vencimiento del link de pago. A partir de ella, no se podrá pagar. Si se envía vacío, se creará el link con el valor seteado a nivel del ente. |
| `habilitaQR` | boolean | OPCIONAL | Indica si el link de pago podrá pagarse con QR o no. Si se envía vacío, se creará el link con el valor seteado a nivel del ente. |
| `habilitaTransferencia` | boolean | OPCIONAL | Indica si el link de pago podrá pagarse con transferencia a CVU o no. Si se envía vacío, se creará el link con el valor seteado a nivel del ente. |
| `habilitaTarjeta` | boolean | OPCIONAL | Indica si el link de pago podrá pagarse con tarjetas o no. Si se envía vacío, se creará el link con el valor seteado a nivel del ente. |
| `successUrl` | string | OPCIONAL | Url a la cual el checkout redirigirá al usuario en caso de que el pago haya sido exitoso. Si se envía vacío, se creará el link con el valor seteado a nivel del ente. |
| `errorUrl` | string | OPCIONAL | Url a la cual el checkout redirigirá al usuario en caso de que el pago haya sido fallido. Si se envía vacío, se creará el link con el valor seteado a nivel del ente. |

> Si los datos opcionales se envían vacíos, para customizar el link de pago se tomarán valores parametrizados a nivel de cada ente. Puede solicitarse el cambio de estos valores en cualquier momento.

Ejemplo de request enviando todos los parámetros del link de pago:
```json
curl -v -X POST "https://gw-staging-qrbind.epays.services/entidad-deuda-debtmanagement/api/v1.201/operaciones/generar-intencion-de-pago" -H "Content-Type: application/json-patch+json" -H "Cache-Control: no-cache" -H "Authorization: Bearer {{access_token}}" --data-raw "{
    \"datosBusqueda\": {
    \"dataList\": {
    \"data\": [
    {
    \"order\": \"1\",
    \"name\": \"codCliente\",
    \"value\": \"123456\"
    }
    ]
    }
    },
    \"motivo\": \"Pago de servicios\",
    \"referencia\": \"Pago de servicios\",
    \"fechaVencimiento\": \"2025-09-30T14:20:08.217Z\",
    \"habilitaQR\": true,
    \"habilitaTransferencia\": true,
    \"habilitaTarjeta\": true,
    \"successUrl\": \"www.google.com\",
    \"errorUrl\": \"www.bind.com.ar\"
}"
```
Ejemplo del request sin enviar ningún parámetro para este link de pago, entonces los tomará por defecto según la configuración del ente:
```json
curl -v -X POST "https://gw-staging-qrbind.epays.services/entidad-deuda-debtmanagement/api/v1.201/operaciones/generar-intencion-de-pago" -H "Content-Type: application/json-patch+json" -H "Cache-Control: no-cache" -H "Authorization: Bearer {{access_token}}" --data-raw "{
    \"datosBusqueda\": {
    \"dataList\": {
    \"data\": [
    {
    \"order\": \"1\",
    \"name\": \"codCliente\",
    \"value\": \"123456\"
    }
    ]
    }
    }
}"
```
### Response
Atributos del response body:

| Atributo | Tipo | Descripción |
| --- | --- | --- |
| `url` | string | Link de búsqueda de deudas y pago de las mismas. |

Ejemplo de response HTTP 200 (url truncada por longitud):
```json
{
    "url": "https://deuda-staging.epays.services/<token-de-sesión-largo>"
}
```

# Configuración
## Creación de entes
Para utilizar el producto cada ente debe ser creado y parametrizado en nuestro sistema. Esta solicitud será al equipo de soporte de Bind PSP.
## Gestión de credenciales para entes
Para utilizar el producto cada ente debe contar con credenciales específicas. La gestión (creación, modificación o eliminación) de las mismas será mediante solicitudes al equipo de soporte de Bind PSP. Las credenciales serán enviadas como secreto a un contacto técnico del ente.
## Modificación de entes
Pueden solicitarse cambios en los parámetros generales de cada ente. Esta solicitud será al equipo de soporte de Bind PSP.
## Eliminación de entes
Pueden solicitarse bajas para que entes dejen de tener la posibilidad de consumir el producto. Esta solicitud será al equipo de soporte de Bind PSP.
## Modificación de medios de pago
Pueden solicitarse cambios en los medios de pago aceptados por el ente (por ejemplo, en tarjetas: aceptar todas, aceptar sólo débito, etc). Esta solicitud será al equipo de soporte de Bind PSP.
## Modificación de comisiones y plazos de acreditación
Pueden solicitarse cambios en los porcentajes de comisión y en la cantidad de días de plazo de liquidación por medio de pago y por ente. Esta solicitud será al equipo de soporte de Bind PSP.

# Ambiente de prueba

> ⚠️ **Credenciales removidas (2026-08-12):** este documento contenía en texto plano el `client_id`/`client_secret` de staging del ente "Pago Fácil" y el usuario/contraseña del Portal Admin de staging. Se quitaron al migrar el archivo (el repo se sincroniza a un remoto de GitHub) — **pedir las credenciales vigentes al equipo de Integraciones/Soporte de Bind PSP**, no reutilizar valores de versiones anteriores de este documento.

## Credenciales para obtener token
Pedir al equipo de Integraciones/Soporte el `client_id`/`client_secret` de staging vigentes para el ente "Pago Fácil".

## Credenciales para acceso al Portal Admin
Para acceder al portal admin y gestionar las cobranzas bajo Pago Fácil, deberán ingresar a:
[admin-staging.epays.services](https://admin-staging.epays.services/)
Pedir usuario y contraseña de staging vigentes al equipo de Integraciones/Soporte.

## Parámetros del Ente de prueba
Las credenciales indicadas son para autenticarse en el sistema como el Ente "Pago Fácil". Cada Ente está asociado y opera con un `idItemProveedor` (en BPG: `SupplierItemId`).
Actualmente, este ente opera con el idItemProveedor = 99999989.
No obstante, para facilitar las pruebas en este ambiente e ir testeando distintos casos de uso, pueden ir cambiando el idItemProveedor asociado con el siguiente endpoint:
```json
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/entidad-deuda-debtmanagement/api/v1.201/entidades' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
    "idItemProveedor": "99999989",
}'
```
## Datos de prueba por medio de pago
### Tarjeta de débito
Para realizar pagos con tarjeta de débito en este ambiente pueden utilizarse los siguientes datos:
4517721004856075 CVV 123 Vto. 08/30 DNI 41586509
### Tarjeta de crédito
Para realizar pagos con tarjeta de crédito en este ambiente pueden utilizarse los siguientes datos:
5299910010000015 CVV 123 Vto. 08/30 DNI 41757926
### QR y Transferencia
Utilizar la app de billetera de prueba brindada por Bind PSP.

> Al descargarse la app, deberán realizar un onboarding para crearse una cuenta en esta aplicación. Al crear la cuenta, deberán solicitar carga de saldo al equipo de soporte de Bind PSP.

## Soporte de integración
De manera de poder dar respuesta rápida a cualquier consulta o duda en la integración, estas deben ser realizadas por el siguiente ticket: [Jira Service Management](https://bindtm.atlassian.net/servicedesk/customer/portal/70/BP-33929?created=true)

---

## Otro cliente sobre el mismo motor de Link de Pago: Grupo DESA (formulario RIPSA)

> Fuente: Epic Notion "[EPIC] Grupo DESA: requerimientos para salir a prod" (Tipo Negocio, Tamaño estimado 52 SP, 7 tickets, todos Funcional, Status Lanzado). Ingesta N3, 2026-07-06.

**Grupo DESA** es otro cliente (grupo de distribuidoras, marca de checkout "RIPSA") que consume el mismo motor de Link de Pago (`payments/create`, `payments/getPayComplete`) documentado arriba para Pago Fácil — no es un producto nuevo, sino un pedido de personalización + gaps de reportería sobre la infraestructura ya existente.

> **Mismo cliente, dos fuentes distintas**: este Epic del Notion histórico (2025, backlog "requerimientos para salir a prod") y la IDEA de Jira PRD-87 documentada en `detalle_productos/adquirencia/boton_simple_2_0.md §9` son pedidos del **mismo cliente** (RIPSA/Grupo DESA) en momentos distintos: acá pide personalización del checkout de Link de Pago + reportería; en Jira (más reciente) pide filtros nuevos sobre Botón Simple 1.0 y la API de Deuda. Confirma que RIPSA es un cliente recurrente con pedidos de mejora sobre múltiples superficies (checkout, Deuda, Botón Simple 1.0) a lo largo del tiempo.

**Pedidos implementados (✅ en el análisis):**
- Campo `ClientReference` (identificador de transacción propio del cliente) agregado como dato obligatorio en creación de Link de pago, recepción de webhooks, creación/consulta de pago QR dinámico (Deuda) y consulta de transacciones — y habilitado como criterio de búsqueda en varios de esos mismos servicios.
- Marca de tarjeta agregada a la respuesta de webhooks y consulta de transacciones.
- Personalización de marca blanca del formulario de pago (RIPSA): logo y colores por distribuidora.
- Timer decreciente en el formulario de pago con el tiempo restante hasta `expirationDate`.
- Reporte exportable (CSV/XLS/API) de transacciones, filtrable por fecha/estado/medio de pago/entidad/`clientReference`, pensado para unificar el modelo de reporting transaccional entre todas las distribuidoras del grupo.
- Consulta estructurada de liquidaciones (Forma de pago, fecha de proceso, montos bruto/deducciones/liquidado/devoluciones) y su reporte exportable — **reemplaza a la plataforma externa MacroClick** que usaban antes para este dato.

**Pedidos pendientes al momento del análisis:** exponer `ClientReference` también en `getPayComplete`, marca de tarjeta en `getPayComplete`, y — el más relevante como gap de plataforma — que el backend permita ver transacciones en estado "cancelado"/"expirado" (hoy no quedan disponibles para consulta, lo que limita auditoría y conciliación).

**Lectura:** este Epic es evidencia de que el motor de Link de Pago (Pago Fácil / ThirdPartyStore, ver también `detalle_productos/adquirencia/boton_simple_2_0.md §7`) es reutilizado por múltiples clientes con branding propio — los pedidos de reportería/liquidaciones exportables tienden a repetirse cliente a cliente.

## Esquema propuesto para disponibilizar el API a integradores externos vía subagentes (discovery, 2026-08-24)

> Estado: discovery — no construido (esquema operativo en validación comercial, sin definición cerrada).
>
> Fuente: Reunión "Proyecto BPG" (2026-08-24), minuta Gemini — Adriana Endzeliz (Comercial) y Pablo Gomes.

Adriana Endzeliz (Comercial) planteó al PM que varios clientes externos están consultando activamente por integrarse al cobro de servicios de BPG (Pago Fácil) — el caso concreto en discusión es **Octagon**, que quiere ofrecer pago de servicios (ej. factura de electricidad) dentro de su propia app/wallet.

**Estado técnico confirmado:** cuando se construyó BPG, se lo pensó **todo por API** para que cualquier cliente con capacidad de desarrollo pudiera integrarse — esas APIs (documentadas arriba en este mismo archivo) ya están en producción, no están ocultas ni deshabilitadas, simplemente **no están activamente disponibilizadas/promocionadas** como oferta comercial estándar hacia afuera.

**Esquema operativo propuesto (a validar):** Bind PSP actúa como **agente** del acuerdo con Pago Fácil (Bin PCP / BPG) — el acuerdo comercial de fondo ya existe: Bind PSP puede actuar como subagente de Pago Fácil. La propuesta en discusión es crear una **entidad relacionada al producto** donde clientes externos como Octagon funcionen como **comercios/subagentes** dentro de esa entidad — análogo al modelo ya usado en Adquirencia, donde cada comercio de Pago Fácil es formalmente "Pago Fácil" independientemente de su rubro real (escuela, municipio, etc.). Quedó abierta la pregunta de si conviene que la titularidad del "agente" recaiga en Bind PSP (como entidad) con Octagon como comercio dentro de ella, o si correspondería un convenio directo Octagon↔Pago Fácil — Adriana Endzeliz se lleva a validar con su equipo cuál esquema conviene más, considerando que las liquidaciones se calculan por comercio.

**Caso de uso descripto para Octagon:** usuario de la wallet de Octagon entra a pago de servicios dentro de la app de Octagon, busca la empresa/deuda a pagar, paga con tarjeta o QR (vía botón de pago externo, no con saldo), la transacción impacta la deuda en BPG, se registra para evitar doble pago, y se emite comprobante.

## Ver también

- `detalle_productos/adquirencia/boton_simple_2_0.md §6-9` — búsqueda de deuda BPG, modalidad ThirdPartyStore, y los pedidos de PRD-87 del mismo cliente RIPSA.
- [3_recursos/arquitectura_sistema/entornos_y_autenticacion_oauth2.md](../../arquitectura_sistema/index.md) — mecánica general de OAuth2 usada por este endpoint.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/pago_facil.md` (reestructuración PARA en cascada); credenciales de ambiente de staging removidas del cuerpo del documento y reemplazadas por referencia a quién las provee.*
*Última actualización anterior: 2026-07-06 — Agregada sección "Grupo DESA (formulario RIPSA)" desde Epic Notion "Grupo DESA: requerimientos para salir a prod" (ingesta N3).*
