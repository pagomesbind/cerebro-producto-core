# Endpoint — Leer QR

> Fuente: https://psp.bind.com.ar/developers/apis/leer-qr
> Producto: Wallet — Pago QR

## Descripción

Consulta la información de un QR que esté conformado de forma standard según EMVco y que pertenezca al ecosistema de interoperabilidad de Argentina.

El sistema consulta a la API Resolve del Aceptador dueño del QR para obtener la información necesaria para luego instruir el PCT.

Este servicio responde con la misma estructura standard con la que responde la API Resolve.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/QR/GetInfoPagoQR?textoQR={textoQR}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `textoQR` | string | REQUIRED | String que conforma la imagen QR. Resulta de leer e interpretar el código QR que se quiere pagar. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/QR/GetInfoPagoQR?textoQR={{texto_del_qr}}' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `status` | string | Estado del QR según standard de Transferencia 3.0. Ver valores posibles abajo. |
| `acceptor.name` | string | Nombre del aceptador (Banco o PSP del comercio). |
| `acceptor.identification` | string | Identificación del aceptador. |
| `administrator.name` | string | Nombre del administrador de interoperabilidad (Coelsa, LINK o Prisma). |
| `administrator.identification_number` | string | Identificación del administrador. |
| `collector.name` | string | Nombre del comercio. |
| `collector.identification_number` | string | CUIT del comercio. |
| `collector.account` | string | CBU/CVU en la que se acredita al comercio. |
| `collector.mcc` | string | Rubro del comercio según MCC de VISA. |
| `collector.bank` | string | Identificador del banco de la cuenta del comercio. |
| `collector.branch_office` | string | Número de comercio o sucursal interno. Puede ser vacío. |
| `collector.terminal` | string | Número de terminal. Puede ser vacío. |
| `order.items` | object | Información de los items de la orden. Puede ser vacío. |
| `order.id` | string | Identificador de la orden. Necesario al iniciar el pago PCT. |
| `order.total_amount` | double | Importe a pagar. `null` si es QR de monto abierto. |
| `order.additional_info` | object | Info adicional opcional del aceptador. Puede ser vacío. |
| `retry_delay` | int | Delay mínimo antes de reintentar una nueva lectura, en segundos. |

### Valores de `status`

| Valor | Descripción |
|-------|-------------|
| `open_amount` | El QR no requiere orden de monto cerrado. El comprador debe ingresar el monto a pagar. |
| `closed_amount` | QR de monto cerrado con orden disponible. El pagador tiene toda la info para confirmar. |
| `pending` | QR de monto cerrado sin orden disponible aún. Reintentar según `retry_delay`. |
| `time-out` | Se agotaron los reintentos en estado `pending`. Se aborta la operación. |
| `empty_order` | Integración directa con el acquirer pero sin nada por cobrar (ej: período de gracia en estacionamiento). |
| `authentication_error` | Error de autenticación al obtener la info del QR. Contactar a Bind PSP. |
| `unsupported_qr_code` | El QR no es válido o no cumple el standard. |
| `unsupported_merchant` | El vendedor no ha verificado su identidad ni definido su alias/CVU. |
| `error` | Error general al obtener la información. Contactar a Bind PSP. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Lectura exitosa (varios escenarios según `status`) |
| `422` | QR ingresado es inválido o no cumple con el standard |
| `400` | Falta un campo requerido |
| `401` | Token de autenticación inválido |
