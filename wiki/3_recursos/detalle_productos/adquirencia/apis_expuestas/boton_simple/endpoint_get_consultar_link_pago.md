# GET — Consultar Link de Pago por GUID

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/consultar-link-de-pago
> Producto: Adquirencia > Botón Simple

## Descripción

"Consultar información sobre un link de pago previamente creado por el GUID."

## Request

**Método HTTP:** `GET`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/getPayComplete`

### curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/getPayComplete?Guid=03a3a503-f32c-46ed-9699-6aa1d9b20f9e' \
--header 'Authorization: Bearer {{access_token}}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Query Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `Guid` | string | SÍ | "Identificador del link de pago, devuelto al momento de creación" |

## Response

### Respuesta exitosa (200)

```json
{
  "paymentId": "int",
  "guid": "string",
  "currency": "string (ARS)",
  "totalAmount": "decimal",
  "description": "string",
  "tsCreate": "datetime",
  "status": "int (1-7)",
  "expirationDate": "datetime",
  "payDate": "datetime",
  "cardType": "int (0-2)",
  "installmentQuantity": "int",
  "successUrl": "string",
  "errorUrl": "string"
}
```

### Estados del link de pago (campo `status`)

| Valor | Estado |
|-------|--------|
| `1` | Nuevo |
| `2` | Pendiente |
| `3` | Completado |
| `4` | Error |
| `5` | Cancelado |
| `6` | Reversado |
| `7` | Rechazado |

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No existe link con ese ID |
| `400` | Campo requerido faltante |
| `401` | Token de autenticación inválido |

## ⚠️ Notas y Advertencias del Portal

> "El único estado válido para dar como pagado satisfactoriamente un link de pago es Completado."

> Estados negativos: Error, Cancelado, Reversado, Rechazado (impiden futuros pagos).
