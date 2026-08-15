# Endpoint — Consultar un link de pago 2.0

> Fuente: https://psp.bind.com.ar/developers/apis/boton20-consultarlink
> Producto: Adquirencia — Botón Simple 2.0

## Descripción

Consulta la información de un link de pago asociado a una deuda.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/deuda?DeudaId=&IdExterno=` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `DeudaId` | int | OPCIONAL | Id de la deuda. Es el respondido al momento de crear el link de pago. |
| `IdExterno` | string | OPCIONAL | Código de deuda externo que informó la Entidad. Enviado como "codigoDeuda" en creación de la deuda. |
| `Productos` | string | OPCIONAL | Indica si en la consulta deben incluirse los productos asociados. En general, la entidad no necesitaría esta información y debe enviar false para asegurar una mejor performance de la consulta. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-cardnotpresent-v2/v2/api/v1.201/deuda?DeudaId=373028&Productos=false' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | int | Id de la deuda. |
| `codigo` | string | Identificador guid de la deuda. |
| `codigoExterno` | object | Contiene información externa informada por la Entidad. |
| `codigoExterno.codigoDeuda` | string | Código de deuda externo informado por la Entidad. |
| `codigoExterno.codigoAuxiliar1` | string | Código informativo adicional. |
| `codigoExterno.codigoAuxiliar2` | string | Código informativo adicional. |
| `codigoExterno.Contexto` | object | Contiene datos sólo informativos que se guardarán asociados a la deuda. En el caso de link de pago 2.0 contiene los items creados en el link de pago. |
| `codigoCaja` | string | Código de la caja. |
| `codigoSucursal` | string | Código de la sucursal. |
| `codigoComercio` | string | Código del comercio. |
| `codigoEntidad` | string | Código de la entidad. |
| `montoTotal` | decimal | Monto actual a cobrar. Es el monto que se cobró o que está pendiente de cobrar dependiendo de la fecha de vencimiento vigente. |
| `moneda` | int | Identificador de moneda del importe a cobrar. Valores posibles: `1` (Pesos argentinos) |
| `motivo` | string | Descripción de la deuda. |
| `tipoOrden` | int | Identificador del tipo de orden de deuda. Valores posibles: `1` (Deuda de pago único) |
| `estado` | int | Identificador estado en que se encuentra la deuda. Valores posibles: `1` PRECARGADO, `2` PENDIENTE, `3` EN_PROCESO, `4` PAGADA, `5` PAGADA_PARCIALMENTE, `6` CANCELADO_MANUAL, `7` CANCELADO, `8` DEVUELTA, `9` DEVUELTA_PARCIALMENTE |
| `estadoDescripcion` | string | Descripción del estado de la deuda. |
| `vencimientos` | int | Cantidad de vencimientos que registra la deuda. |
| `montoVencimiento1` | decimal | Importe a cobrar hasta que se cumpla fecha y hora del primer vencimiento. |
| `fechaVencimiento1` | datetime | Fecha y hora del primer vencimiento. |
| `montoVencimiento2` | decimal | Importe a cobrar hasta que se cumpla fecha y hora del segundo vencimiento. |
| `fechaVencimiento2` | datetime | Fecha y hora del segundo vencimiento. |
| `montoVencimiento3` | decimal | Importe a cobrar hasta que se cumpla fecha y hora del tercer vencimiento. |
| `fechaVencimiento3` | datetime | Fecha y hora del tercer vencimiento. |
| `montoProximoVencimiento` | decimal | Importe vigente según la fecha de vencimiento más próxima. |
| `fechaProximoVencimiento` | datetime | Fecha y hora actual de vencimiento más próxima. |
| `url` | string | Url del link de pago creado. |
| `medioPagoDisponibles` | object | Contiene información de los medios de pago habilitados para esta deuda. |
| `medioPagoDisponibles.id` | int | Identificador del medio de pago registrado. |
| `medioPagoDisponibles.nombre` | string | Nombre del medio de pago. Valores posibles: `"QR"`, `"TARJETA"`, `"RXT"` |
| `medioPagoDisponibles.formaPago` | int | Identificador del tipo de medio de pago. Valores posibles: `1` (QR), `2` (Tarjeta), `3` (Recaudación por transferencia) |
| `medioPagoDisponibles.formaPagoDescripcion` | string | Descripción interna del medio de pago. Valores posibles: `"QR"`, `"TARJETA"`, `"TRANSFERENCIA BANCARIA"` |
| `medioPagoDisponibles.detalleEspecifico.data` | string | Información específica por medio de pago. Si formaPago=1: qr_raw (string EMVCo para generar QR). Si formaPago=2: identificador interno del pago con tarjeta. Si formaPago=3: CVU. |
| `pagos` | object | Contiene información de los intentos de pago asociados a la deuda. Vacío si no hay pagos. |
| `pagos[].id` | int | Identificador del intento de pago de una deuda. |
| `pagos[].montoPagado` | decimal | Importe del pago. |
| `pagos[].fechaDePago` | datetime | Fecha y hora en que se realizó el pago. |
| `pagos[].iDReferenciaTx` | string | Identificador de referencia para realizar el pago con su procesador correspondiente. |
| `pagos[].jsonDetalleTx` | string | Contiene el json con toda la información registrada de la transacción. |
| `pagos[].estado` | int | Estado del intento de pago. Valores posibles: `1` (En proceso), `2` (Aprobado), `3` (Rechazado) |
| `pagos[].fechaAnulacion` | datetime | Fecha y hora en que la deuda fue eliminada. |
| `pagos[].motivoAnulacion` | datetime | Descripción del motivo por el cual la deuda fue eliminada. |
| `pagos[].deudaId` | int | Identificador de la deuda que se intentó pagar. |
| `pagos[].medioPagoDisponibleId` | int | Identificador del medio de pago registrado para pagar la deuda. |
| `esBoton20` | boolean | Indica si es una deuda para el producto Botón 2.0. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |
