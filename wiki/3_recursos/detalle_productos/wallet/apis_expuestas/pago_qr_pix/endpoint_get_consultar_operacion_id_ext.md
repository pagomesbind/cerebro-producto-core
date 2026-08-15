# Endpoint — Consultar operación por ID externo

> Fuente: https://psp.bind.com.ar/developers/apis/consultaroperacionporidext-pagopix
> Producto: Wallet — Pago QR PIX

## Descripción

Devuelve información completa de una operación, buscándola por el código externo de la entidad.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/OperacionByIdExterno/{IdExterno}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idExterno` | string | REQUIRED | Identificador externo de la organización informado al crear la operación (path param). |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/OperacionByIdExterno/1234' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

Mismos campos que Consultar operación por ID (ver `endpoint_get_consultar_operacion_id.md`).

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `404` | No existe la operación consultada |
| `401` | Token de autenticación inválido |
