# Endpoint — Devolver un link de pago 2.0

> Fuente: https://psp.bind.com.ar/developers/apis/boton20-devolverlinkdepago
> Producto: Adquirencia — Botón Simple 2.0

## Descripción

Crea una devolución total o parcial por un link de pago de Botón Simple 2.0 asociado a una deuda.

Si se indica devolver el monto total de una deuda se devolverán todas las transacciones acreditadas asociadas. Por eso la respuesta es un array de contracargos.

Puede indicarse devolver una transacción en particular e incluso devolver un monto parcial de una transacción particular.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/refund` |
| Content-Type | `application/json-patch+json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idDeuda` | int | REQUERIDO | Identificador de la deuda. |
| `monto` | int | REQUERIDO | Monto a devolver. |
| `transaccionId` | int | OPCIONAL | Identificador de una transacción particular a devolver. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/payments/refund' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
"idDeuda": 14364606,
"monto": 100,
"transaccionId": null
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Id del contracargo creado. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación exitosa |
| `500` | La deuda indicada ya fue devuelta |
| `422` | Estado de deuda inválido para devolución |
| `404` | No existe la deuda |
| `401` | Token de autenticación inválido |
