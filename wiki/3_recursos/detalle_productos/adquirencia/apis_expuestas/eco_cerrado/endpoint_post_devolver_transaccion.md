# POST — Devolver Transacción de Eco Cerrado

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/devolucionecocerrado
> Producto: Adquirencia > Eco Cerrado

## Descripción

"Crea una devolución por una transacción realizada por eco cerrado."

> ⚠️ **INCONSISTENCIA DETECTADA EN EL PORTAL**: El encabezado del endpoint declara el path `/ECConfirmaContracargo` pero el bloque curl muestra `/ECConfirmaPago`. El path correcto para la devolución es `/ECConfirmaContracargo` según la documentación textual. Pendiente de confirmación con equipo técnico de Bind PSP.

## Request

**Método HTTP:** `POST`
**URL probable:** `https://gw-staging-qrbind.epays.services/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaContracargo`

### curl request (tal como aparece en el portal)

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-pagoexterno-v2/v2/api/v1.201/ECConfirmaPago" \
  -H "Content-Type: application/json" \
  -H "Cache-Control: no-cache" \
  -H "Authorization: Bearer {{access_token}}" \
  --data-raw "{
    \"identificadorReferencia\": \"ABCDE123456789\",
    \"identificadorTransaccion\": \"157732\",
    \"importeBruto\": 15700.84,
    \"parcial\": false,
    \"motivo\": \"solicitud del cliente\"
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
| `identificadorReferencia` | string | NO | Identificador externo de la entidad |
| `identificadorTransaccion` | int | SÍ | ID de transacción acreditada |
| `importeBruto` | double | NO | Monto a reembolsar |
| `parcial` | boolean | SÍ | true=parcial, false=total |
| `motivo` | string | SÍ | Razón del reembolso |

### Request JSON

```json
{
  "identificadorReferencia": "ABCDE123456789",
  "identificadorTransaccion": 157732,
  "importeBruto": 15700.84,
  "parcial": false,
  "motivo": "solicitud del cliente"
}
```

## Response

### Respuesta exitosa (200)

```json
{
  "id": 123456,
  "estado": "PENDIENTE|ACEPTADO|RECHAZADO",
  "motivoRechazo": "descripción opcional"
}
```

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación exitosa |
| `401` | Token inválido |
