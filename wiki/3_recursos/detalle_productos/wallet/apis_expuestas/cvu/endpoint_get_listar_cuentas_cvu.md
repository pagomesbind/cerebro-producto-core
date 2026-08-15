# Endpoint — Consultar cuentas CVU

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-lista-de-cuentas-cvu
> Producto: Wallet — CVU

## Descripción

Devuelve la información de todas las cuentas CVU de una entidad.

Con este endpoint se pueden consultar datos de cuentas de la misma organización pero también externas de otros bancos, billeteras y proveedores de cuentas.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentasCVU?pageNumber={pageNumber}&pageSize={pageSize}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `pageNumber` | int | REQUIRED | Número de página a mostrar. |
| `pageSize` | int | REQUIRED | Cantidad de cuentas por página a mostrar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentasCVU?pageNumber=20&pageSize=3' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `totalPages` | int | Cantidad total de páginas disponibles para consultar. |
| `totalRecords` | int | Cantidad total de cuentas disponibles para consultar. |
| `cuentasCVU` | object | Objeto que contiene todas las cuentas disponibles para consultar. |
| `cuentasCVU[].id` | int | Identificador del CVU asociado a la cuenta consultada. |
| `cuentasCVU[].idCuenta` | int | Identificador de la cuenta consultada. |
| `cuentasCVU[].nombre` | string | Nombres de la cuenta consultada. |
| `cuentasCVU[].apellido` | string | Apellidos de la cuenta consultada. |
| `cuentasCVU[].cuitCuil` | string | CUIT/CUIL de la cuenta consultada. |
| `cuentasCVU[].cvu` | string | CVU asociado a la cuenta consultada. |
| `cuentasCVU[].alias` | string | Alias asignado al CVU de la cuenta consultada. |
| `cuentasCVU[].fechaAlta` | datetime | Fecha y hora en que la cuenta se dio de alta. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No hay contenido en la página seleccionada |
| `400` | Falta un campo requerido |
| `401` | Token de autenticación inválido |
