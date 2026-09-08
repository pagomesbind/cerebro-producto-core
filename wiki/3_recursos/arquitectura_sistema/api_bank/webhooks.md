# API BANK — Webhooks

> Grupo **Webhooks**: administración de las suscripciones de webhook del cliente (Bind, en este caso) — a qué URL y a qué eventos se notifica de forma asincrónica (transferencias recibidas, DEBIN acreditado/rechazado, etc.). Los payloads concretos de cada tipo de evento están documentados en el grupo [Eventos](eventos.md). Header `Authorization: JWT :token` obligatorio en todos.

## 1. Alta o modificación de webhook — `AltaModificacionWebhook`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Webhooks-AltaModificacionWebhook

Permite el alta o modificación de un webhook del cliente.

### Reglas de identidad e idempotencia (importante)

- Si se encuentra un webhook por `code` o por `url` ya existente, se toma como **modificación** del existente.
- Para modificar la `url` de un webhook, enviar el `code` que se desea modificar.
- Para modificar el `code`, enviar la `url` del webhook.
- **No es posible modificar `code` y `url` al mismo tiempo** — si se envían ambos distintos a los ya registrados, se interpreta como un webhook nuevo.

### Validación activa de la URL en el alta

Al dar de alta o modificar, el banco **envía un mensaje `POST [url]` para validar la URL** — si ese envío falla, el alta es rechazada. El formato de ese mensaje de prueba es el mismo que el de un evento real (ver grupo Eventos, endpoint `WebhookCreated`).

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PUT` |
| URL | `/webhooks` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `body.url` | String | Sí | URL del webhook. Debe responder `200` al `POST` de validación. |
| `body.description` | String | No | Descripción del webhook. |
| `body.code` | String | Sí | Código único de identificación del webhook, definido por el cliente. |
| `body.enabled` | Boolean | Sí | Habilita/deshabilita el webhook. Si se envía deshabilitado, **no** se valida que responda; si se envía habilitado, **sí** se valida. |
| `body.events` | String[] | Sí | Lista de eventos a suscribir — catálogo en Referencias-EventsEnpoints (pendiente de relevar), incluye el valor especial `"ALL"`. |

### Ejemplo de request

```json
{ "url": "https://unlugar.com/webhook/", "description": "una descripción", "code": "1", "enabled": true, "events": ["ALL"] }
```

### Ejemplo del mensaje de validación que envía el banco al endpoint del cliente

```bash
curl -X POST "https://unlugar.com/webhook" \
  -H "Content-Type: application/json" \
  -H "breadcrumbId: 23611c4d-3576-483e-aca4-2d19ca080d79" \
  -H "User-Agent: Apache-HttpClient/4.5.5 (Java/1.8.0_144)" \
  -H "Accept-Encoding: gzip,deflate" \
  -d '{
    "id": "23611c4d-3576-483e-aca4-2d19ca080d79",
    "object": "Endpoint",
    "created": "2024-08-15T14:59:11.237Z",
    "data": { "url": "https://unlugar.com/webhook", "description": "una descripcion", "enabled": true, "events": ["ALL"] },
    "type": "endpoint.created",
    "redeliveries": 0
  }'
```

### Response — atributos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `process` (header) | String | Identificador del proceso. |
| `url` / `description` / `code` / `enabled` / `events_list` | — | Ecos de la configuración. |
| `request_body` / `request_headers` | String | Body/headers del request de validación enviado al webhook del cliente. |
| `response_code` / `response_body` / `response_headers` | String | Respuesta recibida del webhook del cliente. |
| `error_description` | String | Descripción del error, si lo hubo. |
| `connection` | Boolean | `true` si la prueba de conexión fue satisfactoria, `false` si no se pudo acceder a la URL. |
| `saved` | Boolean | `true` si el alta/modificación quedó registrada, `false` si no (típicamente porque `connection` fue `false`). |

### Ejemplos de error de validación (todos HTTP 409, con `connection`/`saved` en `false`)

- **401 Unauthorized** del endpoint del cliente → `errorDescription: "HTTP operation failed invoking ... with statusCode: 401"`.
- **403 Forbidden** del endpoint del cliente → mismo patrón, `responseCode: "403"`.
- **404 / DNS no resuelto** → `errorDescription: "no.existe.io: Name or service not known"`.
- **URL con formato inválido** → `code: "EP002"`, `message: "El valor de 'url' debe ser una dirección de internet válida"`.

Esto es información operativa clave para troubleshooting: si Bind (u otro cliente de API BANK) intenta configurar un webhook y la URL no responde `200` en ese momento — aunque luego esté disponible — el alta queda rechazada por completo, no en un estado "deshabilitado a reintentar".

### Otros códigos de error (HTTP 409)

`GE500`, `GE403`, `EP001` (url vacía), `EP003` (description vacía), `EP004` (enabled vacío), `EP005` (code vacío), `EP006` (events vacío), `EP007` (events con valores no válidos).

## 2. Listado de webhooks — `ConsultaWebhooks`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Webhooks-ConsultaWebhooks

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL | `/webhooks` |

### Response

Array de objetos con `url`, `description`, `code`, `enabled`, `events[]` (catálogo Referencias-EventsEnpoints).

## 3. Eliminar webhook — `EliminarWebhook`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Webhooks-EliminarWebhook

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `DELETE` |
| URL | `/webhooks/code/:code` |

### Códigos de error

| Código | Descripción |
|--------|-------------|
| `EP008` | Endpoint no encontrado. |

## 4. Envío de mensaje al webhook configurado — `WebhookTestSendMessage`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Webhooks-WebhookTestSendMessage

Permite enviar mensajes de prueba al webhook del cliente, simulando un evento real.

### Comportamiento

- Se envía **una operación por mensaje**, identificada opcionalmente por `origin_id` o `id`. Si se informan esos datos, se conservan en el mensaje.
- Si la operación (por `origin_id`/`id`) ya existe y se informan `status` o `amount`, esos valores tienen prioridad sobre los guardados al armar el mensaje de prueba.
- Si la operación no existe, se envían los datos informados en el `body` tal cual.
- El servicio del cliente debe responder `HTTP 200` dentro de **3 segundos**.
- **En modo sandbox se realiza un solo envío, sin reintentos.** En modo no-sandbox (producción), ante error de conexión se realizan **2 reintentos**.

### URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL | `/webhooks/testSendMessage` |

### Parámetros del request

| Parámetro | Tipo | Obligatorio | Descripción |
|-----------|------|-------------|-------------|
| `body.id` | String | Sí | Identificador único del mensaje webhook. |
| `body.object` | String | Sí | Tipo del objeto (objetos del mismo `type` comparten estructura). |
| `body.created` | DateTime | Sí | Fecha de creación del mensaje. |
| `body.data` | Object | Sí | Contenido particular del webhook, variable según el tipo — ver ejemplos en grupo Eventos. |
| `body.type` | String | Sí | Ej. `debin.created`, `webhook.created`. |
| `body.redeliveries` | String | Sí | Número de reintento de envío. |

### Códigos de error (HTTP 409)

`GE500`, `GE403`, `PA007` (tipo de transacción inválida).

## Nota de relevamiento

Grupo completo (4/4 endpoints relevados) desde `https://sandbox.bind.com.ar/apidoc/api_data.json`. El catálogo `Referencias-EventsEnpoints` (lista de eventos suscribibles) y el detalle de cada payload de evento pertenecen al grupo Eventos (ver [eventos.md](eventos.md)) y `Referencias` (fuera de alcance de esta ronda).

> Capturado por Pablo Gomes, 2026-09-01.
