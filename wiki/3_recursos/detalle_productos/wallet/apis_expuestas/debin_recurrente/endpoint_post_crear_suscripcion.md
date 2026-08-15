# Endpoint — Crear suscripción de recurrencia

> Fuente: https://psp.bind.com.ar/developers/apis/crear-suscripcion-de-recurrencia
> Producto: Wallet — Debin recurrente

## Descripción

Crea una suscripción de recurrencia para ingresar dinero con DEBIN recurrente desde una cuenta externa.

Sólo pueden crearse suscripciones sobre cuentas CBU y no CVU, ya que este tipo de operación no puede ejecutarse sobre CVU actualmente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/CrearSuscripcionDebin` |
| Content-Type | `application/json-patch+json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cbuOrigen` | string | REQUIRED | CBU de la cuenta externa de la cuál se debitarán los fondos. Opcional si se envía `aliasOrigen`. |
| `aliasOrigen` | string | OPTIONAL | Alias de la cuenta externa. |
| `concepto` | string | OPTIONAL | Concepto del DEBIN. Valores: `"ALQ"`, `"CUO"`, `"EXP"`, `"FAC"`, `"PRE"`, `"SEG"`, `"HON"`, `"HAB"`, `"VAR"`. Por defecto: `"VAR"` |
| `provision` | string | REQUIRED | Descripción de la operación. Valor permitido: `"Ingresar dinero"` |
| `cuentaId` | int | REQUIRED | Identificador de la cuenta a acreditar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/CrearSuscripcionDebin' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
"cbuOrigen": "3220001881007354720049",
"aliasOrigen": null,
"concepto": "VAR",
"provision": "Ingresar dinero",
"cuentaId": 278243
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la suscripción de recurrencia creada. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación de suscripción exitosa |
| `422` | Ya existe la suscripción |
| `422` | CBU externo inválido |
| `422` | Cuenta inválida |
| `401` | Token de autenticación inválido |
