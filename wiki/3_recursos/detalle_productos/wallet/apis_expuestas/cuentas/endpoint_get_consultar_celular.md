# Endpoint — Consultar cuentas por celular

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-cuentas-por-celular
> Producto: Wallet — Cuentas

## Descripción

Obtiene los datos de una cuenta.

La respuesta de este endpoint es un array debido a que podrían existir más de una cuenta para un mismo celular.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaByCelular?celular={celular}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `celular` | string | REQUIRED | Número telefónico asociado a la cuenta a consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaByCelular?celular=1168599999' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Array de objetos con los mismos campos que Consultar por ID (ver `endpoint_get_consultar_id.md`).

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No hay ninguna cuenta para el celular ingresado |
| `401` | Token de autenticación inválido |
