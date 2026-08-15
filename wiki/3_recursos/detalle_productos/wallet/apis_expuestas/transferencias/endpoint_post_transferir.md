# Endpoint — Realizar una transferencia saliente

> Fuente: https://psp.bind.com.ar/developers/apis/realizar-una-transferencia
> Producto: Wallet — Transferencias

## Descripción

Crea una instrucción de transferencia saliente.

La transferencia no siempre obtendrá un estado definitivo en línea por lo que deberá esperar la actualización del estado mediante consulta de operación o con el aviso de transferencia saliente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/transferir` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cvuOrigen` | string | REQUIRED | CVU de la cuenta origen desde la cual se debitará los fondos para realizar la transferencia. |
| `cbu_cvu_destino` | string | REQUIRED | CBU/CVU de la cuenta destino a la cual se le deben acreditar los fondos transferidos. Puede omitirse si se envía alias. |
| `cuit_destino` | string | REQUIRED | CUIL/CUIT del titular de la cuenta destino. Opcional pero si se envía pueden aplicarse reglas de monitoreo transaccional sobre el destinatario. |
| `alias_destino` | string | OPTIONAL | Alias de la cuenta destino. Puede omitirse si se envía `cbu_cvu_destino`. |
| `importe` | double | REQUIRED | Valor del importe a transferir. |
| `referencia` | string | REQUIRED | Descripción de referencia de la transferencia. |
| `concepto` | string | REQUIRED | Concepto de la transferencia. Valores: `"ALQ"`=Alquiler, `"CUO"`=Cuota, `"EXP"`=Expensas, `"FAC"`=Factura, `"PRE"`=Préstamo, `"SEG"`=Seguro, `"HON"`=Honorarios, `"HAB"`=Haberes, `"VAR"`=Varios |
| `emails` | array | OPTIONAL | Array de strings con correos a los que se enviará comprobante de la transferencia. |
| `idExterno` | string | OPTIONAL | Identificador externo de la entidad para relacionar como atributo adicional. Longitud máxima: 50 caracteres. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/transferir' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"cvu_origen": "0000532609100002749314",
"cbu_cvu_destino": "0000531909000067076630",
"cuit_destino": "27334312758",
"alias_destino": null,
"importe": 100.21,
"referencia": "futbol 5",
"concepto": "VAR",
"emails": ["roberto@gmail.com"],
"idExterno": "1234"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `operacionId` | int | Identificador de la operación creada. |
| `operacionIdExterno` | string | Identificador de la transferencia en el banco. |
| `estadoExterno` | string | Identificador de la operación en el banco. |
| `estadoExterno` | string | Descripción del estado de la transferencia informado por el procesador externo. `"UNKNOWN"` = error de comunicación (se actualiza durante el día). `"IN_PROGRESS"` = para CVU, se intenta resolver durante el día. `"UNKNOWN_FOREVER"` = no pudo resolver y no se reintentará automáticamente. `"COMPLETED"` o `"FAILED"` = estados finales. |
| `estadoId` | int | Identificador del estado en el sistema. Valores: 1=A procesar, 2=Aprobada, 3=Rechazada, 4=A consultar, 5=Auditar, 6=Devuelta, 7=Devuelta parcialmente |
| `origenCuentaId` | int | Identificador de la cuenta de la que se debitaron los fondos. |
| `coelsaId` | string | Identificador de Coelsa para esta transferencia. El más importante para intercambiar consultas y reclamos con otros bancos/billeteras. |
| `fechaInicio` | datetime | Fecha y hora en que inició la transferencia en el banco. |
| `fechaFin` | datetime | Fecha y hora en que finalizó la transferencia en el banco. |
| `fechaNegocio` | datetime | Fecha y hora en que se instruyó la creación de la transferencia. |
| `importe` | double | Valor del importe de la transferencia. |
| `cvuOrigen` | string | CVU desde el que se originó la operación. |
| `referencia` | string | Referencia de la operación. |
| `concepto` | string | Concepto de la operación. |
| `cvuCbuContraparte` | string | CBU/CVU de la cuenta destino. |
| `aliasContraparte` | string | Alias de la cuenta destino. |
| `nombreContraparte` | string | Nombre del titular de la cuenta destino. |
| `cuitCuilContraparte` | string | CUIT/CUIL del titular de la cuenta destino. |
| `comprobanteId` | int | Identificador del comprobante de débito del saldo. |
| `comprobanteDevolucionId` | int | Identificador del comprobante de la devolución (si aplica). Se crea si la transferencia falló y se devuelve el saldo. |
| `mensajeAdicional` | string | Descripción adicional del estado enviado por el banco. |
| `esTransferenciaInterna` | boolean | Indica si la transferencia es entre cuentas de la misma entidad. |
| `estaFinalizada` | boolean | Indica si la operación adquirió un estado definitivo que ya no cambiará. |
| `estaRechazada` | boolean | Indica si la transferencia fue rechazada definitivamente. |
| `estaAAuditar` | boolean | Indica si la transferencia está en un estado no definitivo pendiente de auditoría/conciliación. |
| `estaPendiente` | boolean | Indica si la transferencia aún no fue instruida en el procesador externo. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación de transferencia exitosa (no necesariamente completada) |
| `422` | Cuenta con saldo insuficiente |
| `422` | CVU origen inválido |
| `422` | Concepto inválido |
| `422` | El formato de un campo es inválido |
| `400` | idExterno tiene un formato inválido |
| `401` | Token de autenticación inválido |
