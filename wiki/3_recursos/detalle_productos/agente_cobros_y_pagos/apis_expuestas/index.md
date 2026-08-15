# API Pública Expuesta — Agente de Cobros y Pagos

> **ADVERTENCIA:** Este directorio contiene EXCLUSIVAMENTE las APIs públicas expuestas al cliente en el portal web (`psp.bind.com.ar/developers`). Dominio exclusivo de la skill `/sync_web`. Reubicado desde `3_recursos/documentacion_api/apis_expuestas/agente_cobros/` en la reestructuración PARA en cascada (2026-08-12).
>
> Ver [3_recursos/arquitectura_sistema/entornos_y_autenticacion_oauth2.md](../../../arquitectura_sistema/index.md) para OAuth2/entornos/TLS, comunes a toda la API pública.

2 funcionalidades:

### Transferencias Entrantes CVU — `transferencias_entrantes_cvu/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_transferencias_entrantes_cvu.md](transferencias_entrantes_cvu/guia_transferencias_entrantes_cvu.md) | Guía | Flujo de CVU recaudadora agente |
| [endpoint_post_crear_cvu.md](transferencias_entrantes_cvu/endpoint_post_crear_cvu.md) | POST | Crear CVU agente |
| [endpoint_get_consultar_transferencias.md](transferencias_entrantes_cvu/endpoint_get_consultar_transferencias.md) | GET | Consultar transferencias entrantes |
| [endpoint_event_transferencia_entrante_cvu.md](transferencias_entrantes_cvu/endpoint_event_transferencia_entrante_cvu.md) | EVENT | Webhook: transferencia entrante CVU |

> Ver también `transferencias_cvu/` — guía complementaria del mismo dominio, documentada por separado en el portal.

### Operar CBU Recaudadora — `operar_cbu/`
| Archivo | Tipo | Descripción |
|---------|------|-------------|
| [guia_operar_cbu.md](operar_cbu/guia_operar_cbu.md) | Guía | Flujo CBU recaudadora agente |
| [endpoint_post_realizar_transferencia_cbu.md](operar_cbu/endpoint_post_realizar_transferencia_cbu.md) | POST | Realizar transferencia desde CBU |
| [endpoint_get_consultar_transferencia.md](operar_cbu/endpoint_get_consultar_transferencia.md) | GET | Consultar transferencia |
| [endpoint_get_consultar_saldo_recaudadora_cbu.md](operar_cbu/endpoint_get_consultar_saldo_recaudadora_cbu.md) | GET | Consultar saldo recaudadora CBU |
| [endpoint_event_transferencia_saliente_cbu.md](operar_cbu/endpoint_event_transferencia_saliente_cbu.md) | EVENT | Webhook: transferencia saliente CBU |
| [endpoint_event_transferencia_entrante_cbu.md](operar_cbu/endpoint_event_transferencia_entrante_cbu.md) | EVENT | Webhook: transferencia entrante CBU |

## Ver también
- [detalle_productos/agente_cobros_y_pagos/index.md](../index.md) — resto del conocimiento de producto del Agente de Cobros y Pagos (no API pública).

---
*Última actualización: 2026-08-12 — Reubicado desde `documentacion_api/apis_expuestas/agente_cobros/` (reestructuración PARA en cascada). Contenido y estructura sin cambios, solo la ruta.*
*Última actualización anterior: 2026-06-30 — Fuente: https://psp.bind.com.ar/developers*
