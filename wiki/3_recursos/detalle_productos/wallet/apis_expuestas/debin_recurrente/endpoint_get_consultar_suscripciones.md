# Endpoint — Consultar suscripciones

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-suscripciones
> Producto: Wallet — Debin recurrente

## Descripción

Devuelve información de las suscripciones creadas por cuenta.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/DebinSubscripciones?cuentaId=&habilitado=` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | OPTIONAL | Identificador de la cuenta para la cual consultar suscripciones. |
| `habilitado` | boolean | OPTIONAL | Filtra por suscripciones habilitadas o no. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/DebinSubscripciones?cuentaId=278243&habilitado=true' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador de la suscripción. |
| `cbuOrigen` | string | CBU/CVU de la cuenta externa. |
| `aliasOrigen` | string | Alias de la cuenta externa. |
| `entidad` | string | Descripción del banco o PSP de la cuenta externa. |
| `cuit` | string | CUIT del titular de la cuenta externa. |
| `concepto` | string | Concepto de los DEBIN de esta suscripción. |
| `provision` | string | Descripción de la provisión con la que se procesan los DEBIN en el banco. |
| `estadoDebin` | string | Estado de la suscripción en el banco. |
| `fechaHoraCreacion` | string | Fecha y hora de creación. |
| `fechaHoraModificacion` | string | Fecha y hora de última modificación. |
| `fechaHoraBaja` | string | Fecha y hora de baja. |
| `originId` | string | Identificador de la suscripción en el banco. |
| `descripcion` | string | Descripción de la suscripción. |
| `provisionReferencia` | string | Referencia de la suscripción. |
| `fechaInicio` | string | Fecha y hora de inicio en el banco. |
| `habilitado` | boolean | Si la suscripción está habilitada. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `200` | No se encuentran suscripciones |
| `422` | CBU externo inválido |
| `422` | Cuenta inválida |
| `401` | Token de autenticación inválido |
