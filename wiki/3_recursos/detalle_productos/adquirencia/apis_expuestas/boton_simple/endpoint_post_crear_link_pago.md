# POST — Crear Link de Pago

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/boton-crearlinkdepago
> Producto: Adquirencia > Botón Simple

## Descripción

"Crear un link de pago con toda la información necesaria para realizar el cobro."

## Request

**Método HTTP:** `POST`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/create`

### curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/create' \
--header 'Content-Type: application/json' \
--header 'Accept: text/plain' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
  "collector_cuit": "27264710745",
  "collector_branchOffice": "3358",
  "description": "Pago de servicios",
  "totalAmount": 15000,
  "currency": "ARS",
  "channel": 2,
  "expirationDate": "2025-11-09T15:20:00.0000000",
  "successUrl": "https://www.youtube.com/",
  "errorUrl":"https://www.google.com.ar/",
  "clientreference":"T-021999",
  "items": [{"amount": "7000", "description": "Luz", "quantity": "2"}, {"amount": "1000", "description": "Gas", "quantity": "1"}]
}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json` |
| `Accept` | `text/plain` |
| `Authorization` | `Bearer {{access_token}}` |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `collector_cuit` | string | SÍ | CUIT de la Entidad |
| `collector_branchOffice` | int | SÍ | Identificador del comercio (valor indicado por Bind PSP) |
| `description` | string | SÍ | Descripción/título del resumen de pago |
| `totalAmount` | decimal | SÍ | Importe total a cobrar |
| `currency` | string | SÍ | Moneda: "ARS" (Pesos argentinos) |
| `channel` | int | SÍ | Canal de creación (valor: 1 para API) |
| `expirationDate` | datetime | NO | Fecha/hora de expiración del link |
| `successUrl` | string | NO | URL redirección tras pago exitoso (incluir http/https) |
| `errorUrl` | string | NO | URL redirección tras pago fallido (incluir http/https) |
| `clientReference` | string | NO | Identificador interno informativo |
| `items[{}]` | object | NO | Detalles de ítems del pago |
| `items[{}].description` | string | NO | Descripción del ítem |
| `items[{}].amount` | decimal | NO | Monto por unidad |
| `items[{}].quantity` | int | NO | Cantidad del ítem |

### Request JSON

```json
{
  "collector_cuit": "27264710745",
  "collector_branchOffice": "3358",
  "description": "Pago de servicios",
  "totalAmount": 15000,
  "currency": "ARS",
  "channel": 2,
  "expirationDate": "2025-11-09T15:20:00.0000000",
  "successUrl": "https://www.youtube.com/",
  "errorUrl": "https://www.google.com.ar/",
  "clientreference": "T-021999",
  "items": [
    {"amount": "7000", "description": "Luz", "quantity": "2"},
    {"amount": "1000", "description": "Gas", "quantity": "1"}
  ]
}
```

## Response

### Respuesta exitosa (201)

```json
{
  "url": "https://payment-link-url",
  "expirationDate": "2025-11-09T15:20:00.0000000",
  "paymentId": "guid-identifier",
  "qr": "base64-encoded-qr-image"
}
```

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `url` | string | Enlace de pago generado |
| `expirationDate` | datetime | Fecha de vencimiento |
| `paymentId` | string | GUID del pago creado |
| `qr` | string | Código QR en Base64 |

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación exitosa |
| `400` | Datos de collector inválidos / Falta algún dato requerido |
| `401` | Token de autenticación inválido |
