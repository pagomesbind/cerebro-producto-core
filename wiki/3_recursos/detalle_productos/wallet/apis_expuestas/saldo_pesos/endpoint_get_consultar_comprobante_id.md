# GET — Consultar Comprobante por ID

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-comprobante-por-id
> Producto: Wallet — Saldo en pesos

## Descripción

Devuelve toda la información de un comprobante.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/Comprobante/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador del comprobante a consultar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/Comprobante/8470931' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `idComprobante` | int | Identificador del comprobante. |
| `idTipoComprobante` | int | Identificador del tipo de comprobante. |
| `descripcionTipoComprobante` | string | Descripción o referencia del tipo de comprobante. |
| `idCuenta` | int | Identificador de la cuenta en la que fue aplicado este comprobante. |
| `fecha` | datetime | Fecha de creación del comprobante. |
| `importe` | double | Valor del importe del comprobante. |
| `signo` | int | `1` = Crédito, `-1` = Débito |
| `saldo` | double | Saldo de la cuenta inmediatamente después de la creación de este comprobante. |
| `referencia` | string | Descripción o referencia del comprobante. |
| `idComprobanteRelacionado` | int | Identificador del comprobante relacionado, si corresponde. |
| `descripcionTipoComprobanteRelacionado` | string | Descripción del tipo de comprobante relacionado, si corresponde. |
| `nombreApellidoComprobanteRelacionado` | string | Nombre y apellido del comprobante relacionado, si corresponde. |
| `cuitComprobanteRelacionado` | string | CUIT/CUIL del comprobante relacionado, si corresponde. |
| `cvuComprobanteRelacionado` | string | CBU/CVU del comprobante relacionado, si corresponde. |
| `aliasComprobanteRelacionado` | string | Alias del comprobante relacionado, si corresponde. |
| `idExterno` | string | Identificador externo indicado por la entidad al crear el comprobante. |
| `fechaExterna` | datetime | Fecha externa indicada por la entidad al crear el comprobante. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | El comprobante no existe |
| `401` | Token de autenticación inválido |
