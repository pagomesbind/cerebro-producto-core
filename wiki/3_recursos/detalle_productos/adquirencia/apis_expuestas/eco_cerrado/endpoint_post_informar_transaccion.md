# POST — Informar Transacción de Eco Cerrado

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/informarecocerrado
> Producto: Adquirencia > Eco Cerrado

## Descripción

"Registra en el sistema de cobro una transacción realizada por medio del canal Eco cerrado y realiza la liquidación."

## Request

**Método HTTP:** `POST`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaPago`

### curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaPago" \
  -H "Content-Type: application/json" \
  -H "Cache-Control: no-cache" \
  -H "Authorization: Bearer {{access_token}}" \
  --data-raw "{
    \"identificadorReferencia\": \"ABCDE123456789\",
    \"identificadorProcesador\": \"4568789\",
    \"fechaPago\": \"2025-12-08T23:35:48.583532+00:00\",
    \"identificadorOrdenVenta\": \"9OC1D04EE87AB138B00000495128000000106393ET9000ZTOC5288C377AC\",
    \"formaPago\": \"SALDO_VIRTUAL\",
    \"importeBruto\": 15700.84,
    \"estadoTransaccion\": \"ACREDITADO\",
    \"moneda\": \"ARS\",
    \"comprador\": {
      \"identificadorPagador\": \"20374312349\",
      \"cuentaPagador\": \"0000532909000067076630\"
    }
  }"
```

### Headers

| Header | Valor |
|--------|-------|
| `Content-Type` | `application/json` |
| `Cache-Control` | `no-cache` |
| `Authorization` | `Bearer {{access_token}}` |

### Body

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `identificadorReferencia` | string | NO | Identificador externo de la entidad; valida idempotencia |
| `identificadorProcesador` | string | SÍ | Identificador del comprobante debitado al usuario |
| `fechaPago` | datetime | NO | Fecha en que se concretó el pago |
| `identificadorOrdenVenta` | string | SÍ | Identificación de orden interoperable (order.id del QR) |
| `formaPago` | string | SÍ | Valor fijo: "SALDO_VIRTUAL" |
| `importeBruto` | double | SÍ | Importe bruto de la transacción |
| `estadoTransaccion` | string | SÍ | Valor fijo: "ACREDITADO" |
| `moneda` | string | SÍ | Valor fijo: "ARS" |
| `comprador.identificadorPagador` | string | SÍ | CUIT del pagador |
| `comprador.cuentaPagador` | string | SÍ | CVU del pagador |

### Request JSON

```json
{
  "identificadorReferencia": "ABCDE123456789",
  "identificadorProcesador": "4568789",
  "fechaPago": "2025-12-08T23:35:48.583532+00:00",
  "identificadorOrdenVenta": "9OC1D04EE87AB138B00000495128000000106393ET9000ZTOC5288C377AC",
  "formaPago": "SALDO_VIRTUAL",
  "importeBruto": 15700.84,
  "estadoTransaccion": "ACREDITADO",
  "moneda": "ARS",
  "comprador": {
    "identificadorPagador": "20374312349",
    "cuentaPagador": "0000532909000067076630"
  }
}
```

## Response

### Respuesta exitosa (200)

```json
{
  "identificadorTransaccion": 12345,
  "fechaNegocio": "2025-12-08T23:35:48.583532+00:00"
}
```

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación exitosa |
| `401` | Token de autenticación inválido |
