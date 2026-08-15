# POST — Asignar Alias a CVU (Agente de Cobros)

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-asignaralias
> Producto: Agente de Cobros — Transferencias entrantes en CVU

## Descripción

Crea o modifica el alias a un CVU previamente creado.

Los CVU se crean por defecto sin alias. En caso de ser necesario, debe utilizarse este método para crear un alias. Si una cuenta ya tiene un alias asignado, puede actualizarse con este mismo método.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/view/owner/wallet/alias` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cuit` | string | REQUIRED | CUIT de la entidad titular del CVU al que se quiere asignar/modificar el alias. |
| `cvu` | string | REQUIRED | CVU de la cuenta a la que se quiere asignar/modificar el alias. |
| `label` | string | REQUIRED | Alias a asignar/modificar. Longitud entre 6 y 20 caracteres. |

## Bloque curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/view/owner/wallet/alias" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer {{access_token}}" \
--data-raw '{
  "cuit": "20340342888",
  "cvu": "0000532600001003222228",
  "label": "alias20122023"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cvu` | string | CVU de la cuenta. |
| `label` | string | Alias asignado. |
| `reactivated` | boolean | Si el CVU fue reactivado en el proceso. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Asignación exitosa |
| `401` | Token de autenticación inválido |
