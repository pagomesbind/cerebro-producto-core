# POST — Conciliar Transferencia Entrante (Agente de Cobros CVU)

> Fuente: https://psp.bind.com.ar/developers/apis/transfer-conciliartransferencia
> Producto: Agente de Cobros — Transferencias entrantes en CVU

## Descripción

Devuelve información de una transferencia previamente realizada y la concilia en el sistema.

Si una transferencia es efectivamente conciliada, se creará en el sistema en el momento enviando el webhook de aviso correspondiente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/accounts/owner/concilitations-by-transfer` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `transactions_ids` | array de strings | REQUIRED | Lista de IDs Coelsa que se quieren conciliar. |

## Bloque curl request

```bash
curl -v -X POST "https://gw-staging-qrbind.epays.services/cvucollectentidad-financial/v1/v1.201/banks/322/accounts/owner/concilitations-by-transfer" \
-H "Content-Type: application/json-patch+json" \
-H "Cache-Control: no-cache" \
-H "Authorization: Bearer {{access_token}}" \
--data-raw '{
  "transactions_ids": ["M67REZ8NP3VDK6194KVGOP","8PDX4OGNY83W7KVN0L6EY5","746YGOW9MPRVW34543EXD8J5"]
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `conciliadas` | array | Lista de IDs de transferencias conciliadas exitosamente. Se insertaron en BD y se notificó vía webhook. Ya fueron o serán liquidadas y acreditadas. |
| `conError` | array | Lista de IDs que no pudieron conciliarse por error al consultar el banco. Se recomienda reintentar. Si persiste el error, deberán validarse por archivo batch. |
| `noConciliadas` | array | Lista de IDs que no se conciliaron porque ya existían en BD. Estas transferencias ya fueron o serán liquidadas y acreditadas. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `401` | Token de autenticación inválido |
