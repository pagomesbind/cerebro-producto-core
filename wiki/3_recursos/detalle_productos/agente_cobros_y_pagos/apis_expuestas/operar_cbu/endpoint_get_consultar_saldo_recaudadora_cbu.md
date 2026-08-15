# GET — Consultar Saldo de la Cuenta Recaudadora (CBU)

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-saldo-recaudadora-agentedepago
> Producto: Agente de Cobros — Operar CBU recaudadora

## Descripción

Devuelve el saldo de la cuenta recaudadora de la entidad al momento de la consulta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/Balance` |

## Parámetros del Request

Sin contenido.

## Bloque curl request

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/Balance" \
-H "Authorization: Bearer {{access_token}}"
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `moneda` | string | Moneda de la cuenta: `"ARS"` / `"USD"`. |
| `saldo` | double | Monto del saldo. |
| `fecha` | datetime | Fecha y hora de la consulta de saldo. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |
