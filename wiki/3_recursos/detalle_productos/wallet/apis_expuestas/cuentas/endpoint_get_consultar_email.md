# Endpoint — Consultar cuentas por email

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-cuentas-por-email
> Producto: Wallet — Cuentas

## Descripción

Obtiene los datos de una cuenta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaByEmail?email={email}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `email` | string | REQUIRED | Correo electrónico asociado a la cuenta a consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaByEmail?email=juanperez%40gmail.com' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Array de objetos con los mismos campos que Consultar por ID (ver `endpoint_get_consultar_id.md`).

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No hay ninguna cuenta para el email ingresado |
| `400` | El email ingresado no tiene un formato válido |
| `401` | Token de autenticación inválido |
