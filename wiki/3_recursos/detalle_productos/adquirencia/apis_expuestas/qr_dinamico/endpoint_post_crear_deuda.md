# POST — Crear Deuda (QR Dinámico)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/deuda-crear
> Producto: Adquirencia > QR Dinámico

## Descripción

"Una deuda puede ser pagada sólo una única vez y puede pagarse con los distintos medios de pago que permita la Entidad."

"Si se registra un pago por cualquier medio de pago no podrá volver a pagarse por el mismo medio de pago ni por otro diferente."

## Request

**Método HTTP:** `POST`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-deuda-v2/v2/api/v1.201/Deuda`

### curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-deuda-v2/v2/api/v1.201/Deuda' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer [TOKEN_JWT]' \
--data '{JSON_PAYLOAD}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer [TOKEN_JWT]` |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `codigoExterno` | object | SÍ | Información externa de la deuda |
| `codigoExterno.codigoDeuda` | string | SÍ | Código externo de la Entidad |
| `codigoExterno.codigoAuxiliar1` | string | NO | Código informativo adicional |
| `codigoExterno.codigoAuxiliar2` | string | NO | Código informativo adicional |
| `codigoExterno.Contexto` | object | NO | Datos informativos asociados |
| `codigoExterno.Contexto.additionalProp[1-3]` | string | NO | Información adicional |
| `codigoCaja` | string | SÍ | Código de caja del comercio |
| `codigoSucursal` | string | SÍ | Código de sucursal |
| `codigoComercio` | string | SÍ | Código del comercio |
| `moneda` | int | SÍ | Identificador moneda (0=Pesos Argentinos) |
| `motivo` | string | SÍ | Descripción del cobro |
| `tipoOrden` | int | SÍ | Tipo de orden (0=Pago único) |
| `montoVencimiento1` | decimal | SÍ | Importe hasta primer vencimiento |
| `fechaVencimiento1` | datetime | SÍ | Fecha primer vencimiento |
| `montoVencimiento2` | decimal | NO | Importe hasta segundo vencimiento |
| `fechaVencimiento2` | datetime | NO | Fecha segundo vencimiento |
| `montoVencimiento3` | decimal | NO | Importe hasta tercer vencimiento |
| `fechaVencimiento3` | datetime | NO | Fecha tercer vencimiento |
| `medioPagoDisponibles` | array | SÍ | Array de medios de pago |
| `medioPagoDisponibles[{}].nombre` | string | SÍ | Descripción medio de pago |
| `medioPagoDisponibles[{}].formaPago` | int | SÍ | Identificador (1=QR) |
| `medioPagoDisponibles[{}].habilitado` | boolean | NO | Estado del medio de pago |

### Request JSON

```json
{
  "codigoExterno": {
    "codigoDeuda": "codigoDeuda111201",
    "codigoAuxiliar1": "codigoAuxiliar1111201",
    "codigoAuxiliar2": "codigoAuxiliar2111201",
    "Contexto": {
      "additionalProp1": "additionalProp1111201",
      "additionalProp2": "additionalProp2111201",
      "additionalProp3": "additionalProp3111201"
    }
  },
  "codigoCaja": "B00000484156",
  "codigoSucursal": "S16574",
  "codigoComercio": "C16547",
  "moneda": 0,
  "motivo": "motivo111201",
  "tipoOrden": 0,
  "montoVencimiento1": 100,
  "fechaVencimiento1": "2024-12-22",
  "montoVencimiento2": 200,
  "fechaVencimiento2": "2024-12-23",
  "montoVencimiento3": 300,
  "fechaVencimiento3": "2024-12-24",
  "medioPagoDisponibles": [
    {
      "nombre": "nombremediodepago",
      "formaPago": 1
    }
  ]
}
```

## Response

### Respuesta exitosa (201)

```json
{
  "id": 12345
}
```

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación exitosa |
| `401` | Token de autenticación inválido |
