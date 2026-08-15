# POST — Crear CVU para una Caja (RxT)

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/crear-cvu-para-una-caja
> Producto: Adquirencia > Recaudación por Transferencia (RxT)

## Descripción

"Da de alta un CVU para cobrar con Recaudación por transferencia y lo asocia a una caja existente. El CVU se creará con titularidad del comercio asociado a la caja."

## Request

**Método HTTP:** `POST`
**URL:** `https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/cajas/{idCaja}`

### curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/bindentidad-comercio-v2/v2/api/v1.201/cajas/B00000455197" \
  -H "Authorization: Bearer {{access_token}}"
```

### Headers

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer {{access_token}}` |

### Path Parameters

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `idCaja` | string | SÍ | "Código identificador de la caja a la cual se asociará el CVU" |

## Response

### Respuesta exitosa (201)

```json
{
  "cvu": "string"
}
```

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cvu` | string | "Es el CVU que se creó asociado a la caja para utilizarlo con el producto Recaudación por transferencia." |

### Códigos de estado HTTP

| Código | Descripción |
|--------|-------------|
| `201` | CVU creado exitosamente |
| `404` | El código de caja es inválido |
| `422` | Falta configuración de Bind PSP / Caja ya tiene CVU |
| `401` | Token de autenticación inválido |
