# API Pública Expuesta — Onboarding

> **ADVERTENCIA:** Este directorio contiene EXCLUSIVAMENTE las APIs públicas expuestas al cliente en el portal web (`psp.bind.com.ar/developers`). Dominio exclusivo de la skill `/sync_web`. Reubicado desde `3_recursos/documentacion_api/apis_expuestas/onboarding/` en la reestructuración PARA en cascada (2026-08-12).
>
> Ver [3_recursos/arquitectura_sistema/entornos_y_autenticacion_oauth2.md](../../../arquitectura_sistema/index.md) para OAuth2/entornos/TLS, comunes a toda la API pública.

2 funcionalidades:

### Registro Único — `registro_unico/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_registro_unico.md](registro_unico/guia_registro_unico.md) | Guía | Flujo de registro único |
| [endpoint_post_crear_solicitud.md](registro_unico/endpoint_post_crear_solicitud.md) | POST | Crear solicitud de registro |

### Validación por Partes — `validacion_por_partes/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_validacion_por_partes.md](validacion_por_partes/guia_validacion_por_partes.md) | Guía | Flujo paso a paso de validación |
| [endpoint_post_crear_solicitud.md](validacion_por_partes/endpoint_post_crear_solicitud.md) | POST | Crear solicitud |
| [endpoint_patch_validar_renaper_datos.md](validacion_por_partes/endpoint_patch_validar_renaper_datos.md) | PATCH | Validar RENAPER datos |
| [endpoint_patch_validar_renaper_rostro.md](validacion_por_partes/endpoint_patch_validar_renaper_rostro.md) | PATCH | Validar RENAPER rostro |
| [endpoint_patch_validar_nosis.md](validacion_por_partes/endpoint_patch_validar_nosis.md) | PATCH | Validar Nosis |
| [endpoint_patch_validar_padron_a5.md](validacion_por_partes/endpoint_patch_validar_padron_a5.md) | PATCH | Validar Padrón A5 |
| [endpoint_patch_validar_worldsys.md](validacion_por_partes/endpoint_patch_validar_worldsys.md) | PATCH | Validar WorldSys |
| [endpoint_patch_validar_uif.md](validacion_por_partes/endpoint_patch_validar_uif.md) | PATCH | Validar UIF |
| [endpoint_put_actualizar_datos_adicionales.md](validacion_por_partes/endpoint_put_actualizar_datos_adicionales.md) | PUT | Actualizar datos adicionales |
| [endpoint_patch_actualizar_telefono.md](validacion_por_partes/endpoint_patch_actualizar_telefono.md) | PATCH | Actualizar teléfono |
| [endpoint_patch_actualizar_email.md](validacion_por_partes/endpoint_patch_actualizar_email.md) | PATCH | Actualizar email |
| [endpoint_put_validar_matriz_criterios.md](validacion_por_partes/endpoint_put_validar_matriz_criterios.md) | PUT | Validar matriz de criterios |
| [endpoint_patch_alta_wallet.md](validacion_por_partes/endpoint_patch_alta_wallet.md) | PATCH | Alta en wallet |
| [endpoint_put_cerrar_solicitud.md](validacion_por_partes/endpoint_put_cerrar_solicitud.md) | PUT | Cerrar solicitud |
| [endpoint_get_consultar_solicitud_id.md](validacion_por_partes/endpoint_get_consultar_solicitud_id.md) | GET | Consultar solicitud por ID |
| [endpoint_get_consultar_solicitud_id_externo.md](validacion_por_partes/endpoint_get_consultar_solicitud_id_externo.md) | GET | Consultar por ID externo |

## Ver también
- [detalle_productos/onboarding/index.md](../index.md) — resto del conocimiento de producto de Onboarding (no API pública).

---
*Última actualización: 2026-08-12 — Reubicado desde `documentacion_api/apis_expuestas/onboarding/` (reestructuración PARA en cascada). Contenido y estructura sin cambios, solo la ruta.*
*Última actualización anterior: 2026-06-30 — Fuente: https://psp.bind.com.ar/developers*
