# Arquitectura de Sistema — Infraestructura, Seguridad y Plataforma

> Módulo de **sistemas/IT duro no ligado a un producto**: infraestructura cloud, seguridad de plataforma, NFR/performance, evolución/cambios del sistema, y relación técnica con el proveedor Fintexa. Es el fichero de "cómo está construida y cómo evoluciona la plataforma", complementario a [`detalle_productos/`](../detalle_productos/index.md) (cómo funciona cada producto) y a [`cumplimiento_normativo/`](../cumplimiento_normativo/index.md) (obligaciones regulatorias). Redefinido en la reestructuración PARA en cascada (2026-08-12): antes era solo la traducción de un documento de arquitectura del proveedor; ahora es el destino permanente de todo lo que es infraestructura/plataforma transversal, venga de donde venga.
>
> ⚠️ **Nota de vigencia general:** buena parte de este módulo viene de un documento de arquitectura del proveedor Fintexa (abril 2026) y de un diagrama de red con fecha de corte propia (23/09/2025). **Tratar como contexto general para reglas y patrones amplios, no como fuente de verdad para detalle técnico granular actual** — confirmar siempre con el equipo de Infraestructura/Arquitectura interno. Cada archivo hereda esta nota.

## Documentos de este módulo

| Archivo | Contenido |
|---|---|
| [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md) | Resumen ejecutivo, principios arquitectónicos (microservicios, CQRS, event-driven), stack tecnológico completo (.NET 8, SQL Server, RabbitMQ, Redis, AKS). |
| [ecosistemas_y_capas.md](ecosistemas_y_capas.md) | Capas de la plataforma (presentación → gateway → dominio → event bus → infra) y los 6 ecosistemas de negocio independientes. |
| [mapa_de_microservicios_wallet.md](mapa_de_microservicios_wallet.md) | Los 7 dominios funcionales y el mapa completo de microservicios de Wallet Service. |
| [patrones_de_implementacion.md](patrones_de_implementacion.md) | CQRS con MediatR, Repository/Unit of Work, Circuit Breaker (Polly), y las Sagas de alta de cuenta/transferencia/QR. |
| [flujo_transaccional_transferencia_cvu.md](flujo_transaccional_transferencia_cvu.md) | Viaje técnico paso a paso de una transferencia CVU real, del API público al webhook de salida. |
| [topologia_de_eventos.md](topologia_de_eventos.md) | Event Bus: publishers, consumers y patrones de comunicación asíncrona (RabbitMQ/MassTransit/CloudEvents). |
| [integraciones_externas.md](integraciones_externas.md) | Protocolo y dirección de cada integración externa (Coelsa, AFIP, BCRA, RENAPER, Visa/Mastercard, Lirium, Poincenot, PIX, Ardid, Siscri). |
| [modelo_de_seguridad.md](modelo_de_seguridad.md) | Defensa en profundidad en 5 capas, mapeo normativo (PCI DSS, OWASP, CWE), estándares y controles implementados. |
| [entornos_y_autenticacion_oauth2.md](entornos_y_autenticacion_oauth2.md) | URLs base, OAuth2 client credentials, TLS, errores globales — el contrato de la API pública, fuente de `/sync_web`. |
| [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) | Guía de implementación de mTLS para APIs entrantes y webhooks salientes, arquitectura AppGW/APIM/Entra ID. |
| [politica_de_reintentos_de_webhook.md](politica_de_reintentos_de_webhook.md) | Política de 10 reintentos con backoff creciente, más la excepción de canal sin confirmar en CVUCollect. |
| [hardening_y_remediacion_de_pentests.md](hardening_y_remediacion_de_pentests.md) | Hallazgos reales de 3 rondas de pentest y su remediación, más hardening proactivo (MFA, geobloqueo, rate limiting). |
| [conteo_de_pegadas_api_bank.md](conteo_de_pegadas_api_bank.md) | Header `x-internalclientid` para medir volumen de invocaciones a API Bank por sistema/entidad, con fines de facturación con el proveedor. |
| [infraestructura_cloud_azure.md](infraestructura_cloud_azure.md) | Cluster AKS, servicios de datos, networking/observabilidad, CI/CD y disaster recovery (descripción genérica del proveedor). |
| [topologia_de_red.md](topologia_de_red.md) | Infraestructura Azure **real y nombrada** (VNets, IPs, CIDRs) — distinta de la descripción genérica contractual. Incluye la disputa de atribución de la instancia MongoDB. |
| [nfr_y_slas.md](nfr_y_slas.md) | Alta disponibilidad (réplicas, health checks, circuit breakers, backups) y SLAs técnicos target (uptime, latencia, throughput). |
| [calidad_y_cicd.md](calidad_y_cicd.md) | Testing, CI/CD, estandarización, mecanismos de integración para clientes, roadmap técnico declarado por el proveedor. |
| [modernizacion_plataforma_dotnet.md](modernizacion_plataforma_dotnet.md) | Migración incremental a .NET 8, servicio por servicio, en paralelo al desarrollo de producto. |
| [mantenimiento_y_capacidad_aks.md](mantenimiento_y_capacidad_aks.md) | Plan de mantenimiento AKS de agosto 2026 (reversión post-incidente + optimización de capacidad). |
| [relacion_con_fintexa.md](relacion_con_fintexa.md) | Dotación de recursos del proveedor (bajas consecutivas jul/ago 2026) y estado del Comité de Arquitectura COE. |
| [idempotencia_de_plataforma.md](idempotencia_de_plataforma.md) | Síntesis del patrón transversal de falta de idempotencia centralizada, con evidencia de 5 canales distintos. |
| [incidentes_de_plataforma.md](incidentes_de_plataforma.md) | Incidentes de infraestructura y capacidad de julio-agosto 2026: Wallet Bean Service, sobrecarga por clientes de alto volumen, timeout de inserción (INF-1392), rate limiting, Auto External v2. |
| [modelo_acoplado_vs_desacoplado.md](modelo_acoplado_vs_desacoplado.md) | Split QR del PSP 184, migración de Personal Pay al modelo desacoplado con Banco Industrial, y los riesgos operativos de la ventana de sincronización de 2 minutos. |

## Ver también

- [detalle_productos/index.md](../detalle_productos/index.md) — mecánica de cada producto (no infraestructura transversal).
- [cumplimiento_normativo/index.md](../cumplimiento_normativo/index.md) — obligaciones regulatorias (PCI, PLD/BCRA, UIF).
- [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md) — inconsistencias abiertas de este módulo (conteo de microservicios, versión del documento fuente, PCI DSS omitido del texto narrativo, atribución de MongoDB).

---
*Última actualización: 2026-08-12 — Reestructuración PARA en cascada: los 3 archivos legacy (`index.md`, `flujo_transaccional.md`, `seguridad_y_redes.md`) se desarmaron en 15 archivos temáticos, y se sumaron 6 archivos más provenientes de `detalle_productos/transversal/` y `documentacion_api/general_info.md` desarmados en fases previas — 21 archivos temáticos en total. El módulo pasa a ser explícitamente "sistemas/IT duro no ligado a producto", no solo la traducción de un documento del proveedor.*
