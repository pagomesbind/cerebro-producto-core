# POST — Crear CVU (Agente de Cobros)

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-crearcvu
> Producto: Agente de Cobros — Transferencias entrantes en CVU

## Descripción

Crea un CVU. Cualquier persona podrá realizar transferencias a este CVU y los fondos ingresarán en una cuenta recaudadora asignada a la Entidad.

El CUIT utilizado para la creación de los CVUs debe ser el mismo de la Entidad, ya que debe ser el titular de todas las cuentas que cree para este tipo de operación.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/view/owner/wallet/cvu` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `client_id` | string | REQUIRED | Código externo a elección de la Entidad. Único por CVU, no puede repetirse. |
| `cuit` | string | REQUIRED | CUIT de la entidad titular del CVU. |
| `name` | string | REQUIRED | Razón social o nombre de la Entidad titular del CVU. Es el nombre del titular que verá el cliente al hacer una transferencia al CVU. |

## Bloque curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/view/owner/wallet/cvu" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer {{access_token}}" \
--data-raw '{
  "client_id": 191220231,
  "cuit": "30717449076",
  "name": "Nombre de la entidad"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cvu` | string | CVU creado. |
| `label` | string | Alias de la cuenta. Por defecto, el CVU es creado sin alias (debe asignarse posteriormente si es necesario). |
| `reactivated` | boolean | Indica si el CVU fue reactivado. Será `true` si se trata de un CVU que había sido eliminado y fue creado nuevamente con los mismos datos. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Creación exitosa |
| `401` | Token de autenticación inválido |
