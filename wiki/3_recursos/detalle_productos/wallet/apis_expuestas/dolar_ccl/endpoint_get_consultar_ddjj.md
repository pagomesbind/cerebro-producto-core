# GET — Consultar DDJJ

> Fuente: https://psp.bind.com.ar/developers/apis/inversiones-consultar-ddjj
> Producto: Wallet — Dólar CCL

## Descripción

Obtiene el texto de la declaración jurada que debe aceptar el cliente titular de la cuenta que realizará la operación de compra de dólar. Además graba en la intención la versión consultada.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/DeclaracionJurada` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCuenta` | int | REQUIRED | Identificador de la cuenta. |
| `idIntencion` | int | OPTIONAL | Identificador de la intención de compra. Opcional si se envía `idExternoIntencion`. |
| `idExternoIntencion` | string | OPTIONAL | Identificador externo de la intención. Opcional si se envía `idIntencion`. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-investment/v1/api/v1.201/Inversion/DeclaracionJurada?idCuenta=276058&idExternoIntencion=20241219test2' \
--header 'Authorization: {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `disclaimer` | string | Texto de la declaración jurada que el titular de la cuenta debe aceptar para concretar la operación. |
| `createdDate` | datetime | Fecha y hora en que se creó esta versión de la declaración jurada. |
| `key` | string | Identificador de la versión del texto de la declaración jurada. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `422` | Intención no existente |
| `422` | Cuenta inexistente |
| `401` | Token de autenticación inválido |
