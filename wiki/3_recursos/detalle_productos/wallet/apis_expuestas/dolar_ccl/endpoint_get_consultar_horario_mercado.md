# GET — Consultar Horario de Mercado

> Fuente: https://psp.bind.com.ar/developers/apis/inversiones-consultar-horario-de-mercado
> Producto: Wallet — Dólar CCL

## Descripción

Devuelve los horarios de apertura y cierre del mercado. En la operatoria de dólar CCL se utiliza la operatoria T0.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/ConsultarHorarioMercado/{idCuenta}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/ConsultarHorarioMercado/276058' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name` | string | Descripción general de la operatoria. |
| `schedules.T0.openTime` | string | Horario de apertura del mercado. |
| `schedules.T0.closeTime` | string | Horario de cierre del mercado. |
| `schedules.T0.open` | boolean | Si el mercado se encuentra abierto. |
| `timeZone` | string | Huso horario en que se expresan los horarios. |
| `locale` | string | Localización. |
| `nextOperationDate` | datetime | Próxima fecha en que abrirá el mercado. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `422` | Cuenta inválida |
| `401` | Token de autenticación inválido |
