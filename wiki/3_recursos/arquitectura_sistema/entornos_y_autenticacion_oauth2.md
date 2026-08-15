# Entornos, Autenticación OAuth2 y Errores Globales — API Pública

> Estado: en producción. Reubicado desde `3_recursos/documentacion_api/general_info.md` en la reestructuración PARA en cascada (2026-08-12) — es infraestructura/plataforma común a toda la API pública, no específica de un producto. Es también la fuente pública (portal `psp.bind.com.ar/developers`) de este mismo contrato, mantenida por `/sync_web`.

## URLs Base

| Entorno | URL Base |
|---------|----------|
| **Staging** | `https://gw-staging-qrbind.epays.services` |
| **Producción** | `https://api.bindpagos.com.ar` |

## Autenticación — OAuth 2.0 Client Credentials

El portal implementa **OAuth 2.0** con tokens Bearer. Cada request requiere el header `Authorization`.

### Endpoints de Token

| Entorno | URL |
|---------|-----|
| **Staging** | `https://login.microsoftonline.com/61ef5b89-8df3-499d-8c13-38fed5d09c72/oauth2/v2.0/token` |
| **Producción** | `https://login.microsoftonline.com/3ee81fb8-f2e8-4475-aef2-c5902f9fb0c3/oauth2/v2.0/token` |

### Parámetros del Request de Token

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `client_id` | string | Sí | Identificador único de la entidad |
| `client_secret` | string | Sí | Contraseña de la entidad |
| `grant_type` | string | Sí | Valor fijo: `"client_credentials"` |
| `scope` | string | Sí | Ver tabla de scopes por entorno |

### Scopes por Entorno

| Entorno | Scope |
|---------|-------|
| **Staging** | `api://staging-bind.epays.services/.default` |
| **Producción** | `api://bindpagos.com.ar/.default` |

### Campos del Response de Token

| Campo | Descripción |
|-------|-------------|
| `token_type` | Retorna `"Bearer"` |
| `access_token` | Valor a usar en el header Authorization |
| `expires_in` | Validez del token en segundos (60 minutos) |
| `ext_expires_in` | Ventana de expiración extendida |

### Ejemplo de Request (curl)

```bash
curl -X POST "https://login.microsoftonline.com/61ef5b89-8df3-499d-8c13-38fed5d09c72/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id={{client_id}}&client_secret={{client_secret}}&grant_type=client_credentials&scope=api://staging-bind.epays.services/.default"
```

### Uso del Token en Requests

```
Authorization: Bearer {{access_token}}
```

## Seguridad de Transporte

- **Protocolo:** HTTPS obligatorio (TLS 1.2 o superior)
- HTTP tradicional está prohibido
- **Conectividad:** Internet público únicamente; no hay canales VPN implementados en este carril estándar (distinto del carril mTLS — ver [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) — y de las VPNs internas de infraestructura documentadas en la topología de red)

### mTLS (Opcional)

Certificados Mutual TLS disponibles para validación de consumo API entrante y de webhooks salientes. Ver [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) para el proceso completo de habilitación.

## Webhooks — Política de Reintentos

Ver [politica_de_reintentos_de_webhook.md](politica_de_reintentos_de_webhook.md) — 10 intentos con backoff creciente, HTTP 200 esperado.

## Errores Globales

| Código HTTP | Descripción |
|-------------|-------------|
| `401` | Token de autenticación inválido |
| `403` | Scopes del token insuficientes para la operación |

## Ver también
- [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) — autenticación mTLS para clientes que lo requieren.
- [politica_de_reintentos_de_webhook.md](politica_de_reintentos_de_webhook.md) — qué pasa si un webhook no responde 200.
- `detalle_productos/<producto>/apis_expuestas/` — documentación específica de cada endpoint por producto.

---
*Última actualización: 2026-08-12 — Reubicado desde `documentacion_api/general_info.md` (reestructuración PARA en cascada). Contenido sin cambios.*
*Última actualización anterior: 2026-06-30 — Fuente: https://psp.bind.com.ar/developers/general*
