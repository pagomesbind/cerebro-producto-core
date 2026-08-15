# GET — Consultar Deuda (QR Dinámico)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/deuda-consultar
> Producto: Adquirencia > QR Dinámico

## Descripción

"Consulta la información de una deuda, filtrando por su id o el código externo indicado por la entidad al momento de su creación."

"Tiene los datos necesarios para poder proceder con exponer cada medio de cobro a los clientes para que puedan pagar la deuda."

## Request

**Método HTTP:** `GET`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-deuda-v2/v2/api/v1.201/Deuda`

### curl request

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/bindentidad-deuda-v2/v2/api/v1.201/Deuda?deudaId=8" -H "Content-Type: application/json" -H "Authorization: Bearer {{access_token}}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json` |
| `Authorization` | `Bearer {{access_token}}` |

### Query Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `deudaId` | int | NO | Id de la deuda |
| `codigoDeuda` | string | NO | Código externo de la deuda |
| `moneda` | int | SÍ | Identificador de moneda (0=Pesos Argentinos) |

## Response

### Respuesta exitosa (200)

```json
{
  "id": 8,
  "codigo": "guid-string",
  "codigoExterno": {
    "codigoDeuda": "EXT123",
    "codigoAuxiliar1": "AUX1",
    "codigoAuxiliar2": "AUX2",
    "Contexto": {
      "additionalProp1": "info",
      "additionalProp2": "info",
      "additionalProp3": "info"
    }
  },
  "montoTotal": 1000.50,
  "moneda": 0,
  "estado": 2,
  "estadoDescripcion": "Pendiente",
  "medioPagoDisponibles": [{
    "id": 1,
    "nombre": "QR",
    "formaPago": 1,
    "DetalleEspecifico": {"data": "qr_raw_string"}
  }],
  "pagos": []
}
```

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |
