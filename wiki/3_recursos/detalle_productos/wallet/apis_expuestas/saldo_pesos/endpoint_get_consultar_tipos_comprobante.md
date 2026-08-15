# Endpoint — Consultar tipos de comprobante

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-lista-de-tipos-de-comprobante
> Producto: Wallet — Saldo en pesos

## Descripción

Devuelve todos los tipos de comprobante disponibles en la entidad.

La entidad debe crear sus propios tipos de comprobante. No tiene permitido utilizar los tipos de comprobante reservados para operaciones internas del sistema (IdTipoComprobante: 1, 2, 3, 4, 5 y 6).

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/TiposComprobantes` |

## Parámetros del Request

Sin contenido.

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-comprobante/v1/api/v1.201/TiposComprobantes' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Identificador del tipo de comprobante. |
| `nombre` | string | Nombre del tipo de comprobante. |
| `codigo` | string | Código externo de la entidad. |
| `descripcion` | string | Descripción adicional. |
| `signo` | int | `1` = Crédito, `-1` = Débito |
| `habilitado` | boolean | Si el tipo de comprobante está habilitado. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |
