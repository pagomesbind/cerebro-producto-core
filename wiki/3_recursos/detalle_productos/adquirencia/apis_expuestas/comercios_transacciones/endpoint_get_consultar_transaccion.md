# GET — Consultar Transacciones (Comercios y Transacciones)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/consultar-transacciones
> Producto: Adquirencia > Comercios y Transacciones

## Descripción

"Busca y devuelve una lista de transacciones según los filtros indicados."

## Request

**Método HTTP:** `GET`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1.201/transacciones-pag`

### curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/bindentidad-transaccionquery-v2/v2/api/v1.201/transacciones-pag?fechaNegocioDesde=2024-06-17&fechaNegocioHasta=2025-02-17&Start=0&Length=100' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

### Headers

| Header | Valor |
|--------|-------|
| `Cache-Control` | `no-cache` |
| `Authorization` | `Bearer {{access_token}}` |

### Query Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `Start` | int | NO | Número de página (mínimo: 0) |
| `Length` | int | NO | Cantidad de transacciones por página |
| `fechaNegocioDesde` | string | NO | Fecha inicio búsqueda (UTC-3) |
| `fechaNegocioHasta` | string | NO | Fecha fin búsqueda (UTC-3) |
| `horaNegocioDesde` | string | NO | Hora inicio búsqueda (UTC-3) |
| `horaNegocioHasta` | string | NO | Hora fin búsqueda (UTC-3) |
| `id` | int | NO | Identificador de transacción |
| `referenciasPago` | string | NO | ID referencia externo del pago |
| `idOrdenVentaReferencia` | string | NO | ID orden de venta o deuda |
| `identificadorOrden` | string | NO | ID propio del canal de pago |
| `identificadorProcesadorPago` | string | NO | ID procesador externo |
| `estado` | string | NO | "ACREDITADO", "RECHAZADA", "DEVUELTA" |
| `codigoComercio` | string | NO | ID del comercio |
| `codigoComercioSucursal` | string | NO | ID de la sucursal |
| `codigoComercioCaja` | string | NO | ID de la caja |

## Response

### Respuesta exitosa (200)

```json
{
  "totalRegistros": 0,
  "transacciones": [
    {
      "id": 0,
      "codigoComercio": "string",
      "formadePago": {
        "value": "string",
        "nameOf": "string",
        "name": "string",
        "id": "10|20|40|50|60|70|80|90"
      },
      "fechaLocalNegocio": "string",
      "horaLocalNegocio": "string",
      "importeBruto": 0.0,
      "importeNeto": 0.0,
      "moneda": "ARS",
      "estado": 1,
      "descripcionEstado": "ACREDITADO|RECHAZADA|DEVUELTA|ENPROCESO|REALIZADA",
      "contracargos": [],
      "retenciones": []
    }
  ]
}
```

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa con registros |
| `204` | Consulta exitosa pero no se encontraron registros |
| `400` | Bad Request |
| `422` | Unprocessable Entity |
| `401` | Token de autenticación inválido |
