# Endpoint — Asignar alias

> Fuente: https://psp.bind.com.ar/developers/apis/asignar-alias
> Producto: Wallet — CVU

## Descripción

Asigna un nuevo alias o modifica el alias a un CVU existente.

Por defecto, el id requerido para asignar el alias no es el id de la cuenta sino que es el id del CVU, pero el endpoint permite hacerlo usando el id de la cuenta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PATCH` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/AsignarAlias/CVU/{id}` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador del CVU al que se desea asignar un nuevo alias (path param). |
| `alias` | string | REQUIRED | Alias a asignar. Longitud máxima de 20 caracteres. |
| `idEsCuenta` | boolean | OPTIONAL | Indica si el campo `id` enviado corresponde al `idCuenta` en lugar del `idCVU`. Valor por defecto: `false` |

## Bloque curl request

```bash
curl --location --request PATCH 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/AsignarAlias/CVU/154552' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
"alias": "Carlitos.perez7896"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador del CVU creado. Es diferente al CVU de la cuenta. Se utiliza luego para realizar acciones sobre el CVU, como por ejemplo: Eliminar CVU. |
| `cvu` | string | CVU creado. |
| `alias` | string | Alias creado por defecto para este CVU. Puede modificarse. |
| `idCuenta` | int | Identificador de la cuenta. |
| `nombreCvu` | string | Nombre con que se creó el CVU. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Asignación de alias exitosa |
| `422` | No existe el id de CVU |
| `422` | El alias ya se encuentra en uso |
| `422` | El formato del alias es incorrecto |
| `422` | El alias se intenta modificar más de una vez en 24 horas |
| `401` | Token de autenticación inválido |
