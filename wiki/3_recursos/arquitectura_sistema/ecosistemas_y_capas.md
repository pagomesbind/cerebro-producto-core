# Arquitectura General de Plataforma — Capas y Ecosistemas de Negocio

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`. Reubicado desde `arquitectura_sistema/index.md §4-5` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

## 1. Arquitectura General de Plataforma

*(Figura 1 del documento fuente — diagrama de capas conservado en `wiki/4_archivos/historial_raw/2026-07-02_arquitectura_proveedor/` junto al `.docx` original)*

| Capa | Componentes |
|---|---|
| **Presentación** | App Móvil (iOS/Android), Web Banking, SDK Integración, API Terceros, Portal PSP. Todos los canales pasan exclusivamente por la capa API Gateway/BFF. |
| **API Gateway / BFF** | `Wallet.BFF` (canal móvil/web) y `BFF.PSP` (portal de configuración/administración). Autenticación JWT, autorización RBAC, rate limiting, agregación de respuestas, transformación por canal. |
| **Servicios de Dominio** | Cuentas (CVU, KYC/AML, onboarding), Operaciones (transferencias, QR, DEBIN, PIX), Costos (pricing, segmentación, liquidación), Inversiones (FCI, MEP/CCL, cripto), Comprobantes (PDF, extractos), Notificaciones (email, SMS, webhooks), Bind (integración Coelsa, banking, clearing). Cada servicio tiene su propia base de datos y se comunica vía Event Bus. |
| **Event Bus** | RabbitMQ — columna vertebral de comunicación asíncrona. Patrones Publish-Subscribe, Request-Reply, Routing Slip. Quorum Queues para durabilidad y tolerancia a particiones. |
| **Servicios Compartidos** | Shared.Debin, Shared.Crypto, Shared.Pix, Shared.Dispatch, Shared.Email, Shared.Files, QueueSentinel (monitoreo de salud de colas). |
| **Cross-Cutting Concerns** | Autenticación JWT, logging Serilog, resiliencia Polly, validación FluentValidation, Correlation ID, data masking, health checks — implementados como middleware y librerías NuGet centralizadas. |
| **Infraestructura** | Azure AKS, SQL Server, Redis Cache, RabbitMQ, Application Insights, Azure DevOps, Blob Storage. |
| **Integraciones Externas** | Coelsa/Bind, AFIP, BCRA, RENAPER, Lirium, Poincenot, PIX/PagBrasil, Visa/Mastercard, Ardid. |

## 2. Ecosistemas de la Plataforma

La plataforma opera **6 ecosistemas de negocio independientes**, cada uno con microservicios, bases de datos y pipelines de despliegue propios:

| Ecosistema | Descripción y Alcance |
|---|---|
| **Aceptador** | Procesamiento de pagos con tarjeta y QR (POS, e-commerce), integración Visa/Mastercard, gestión de terminales, liquidación de comercios. |
| **Wallet Service** | Billetera digital: cuentas virtuales CVU, transferencias, QR interoperable, DEBIN, inversiones, comprobantes fiscales, notificaciones multicanal. **Foco principal de este documento.** |
| **Recaudación** | Cobranzas digitales vía CVU, links de pago, conciliación automática, reportes de recaudación. |
| **Front End Config** | Configuración centralizada: comercios, terminales, parámetros operativos, reglas de negocio, catálogos. |
| **Botón Simple** | Botón de pago e-commerce, en proceso de migración progresiva hacia la arquitectura de microservicios actual (legacy). |
| **Archivos R.I.** | Procesamiento de archivos regulatorios e intercambio con entidades bancarias, compensadoras y reguladores (BCRA, Coelsa). |

> Nota de correlación: estos 6 ecosistemas mapean directamente con los productos de negocio de Bind PSP (ver [2_areas/overview_productos/index.md](../../2_areas/overview_productos/index.md)) más el componente transversal de configuración (Front End Config). "Aceptador" = Adquirencia; "Wallet Service" = Wallet; "Recaudación" = Agente de Cobros y Pagos.

## Ver también
- [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md) — stack tecnológico y cifras clave.
- [mapa_de_microservicios_wallet.md](mapa_de_microservicios_wallet.md) — detalle de microservicios de Wallet Service.
- [integraciones_externas.md](integraciones_externas.md) — protocolo y dirección de cada integración externa.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/index.md §4-5` (reestructuración PARA en cascada). Contenido sin cambios.*
