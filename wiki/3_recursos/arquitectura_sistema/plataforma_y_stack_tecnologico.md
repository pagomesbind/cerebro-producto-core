# Plataforma y Stack Tecnológico — Fintexa (Proveedor)

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx` (documento confidencial del proveedor) + `Diagrama - Bind-PSP.jpg`. Versión del documento fuente: 2.1 (portada) / 2.0 (pie — ver gap de inconsistencia de versión en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md)). Reubicado desde `arquitectura_sistema/index.md §1-3` en la reestructuración PARA en cascada (2026-08-12).
>
> ⚠️ **Nota de vigencia:** este documento del proveedor describe la **arquitectura general** de la plataforma en un momento dado (abril 2026). El sistema suma componentes constantemente y la documentación del proveedor no siempre está al día con el detalle técnico puntual. **Tratar el contenido de este módulo como contexto general para reglas y patrones arquitectónicos amplios, no como fuente de verdad para detalle técnico granular actual** — para eso, confirmar siempre con el equipo de Infraestructura/Arquitectura interno.

## 1. Resumen Ejecutivo

Fintexa es la plataforma de microservicios cloud-native (Microsoft Azure Kubernetes Service) sobre la que corre el ecosistema Bind PSP, incluyendo **Wallet Service** (foco principal del documento fuente) y otros 5 ecosistemas de negocio. Cubre el ciclo de vida completo de operaciones financieras digitales: cuentas virtuales/CVU, pagos omnicanal (transferencias, QR interoperable, DEBIN, PIX transfronterizo), motor de comisiones, inversiones digitales (FCI, dólar MEP/CCL, cripto) y cumplimiento fiscal automatizado.

### Cifras Clave de la Plataforma

| Dimensión | Valor |
|---|---|
| Ecosistemas de negocio | 6 ecosistemas independientes |
| Microservicios activos (toda la plataforma) | 135+ servicios en producción |
| Wallet Service — microservicios dedicados | 47+ (⚠️ ver nota de inconsistencia abajo) |
| Framework principal | .NET Core 8.0 (roadmap .NET 10) |
| Orquestación | Azure Kubernetes Service (AKS) v1.27+ |
| Disponibilidad target | 99.9% SLA |
| Throughput target | 1.000 TPS |
| Latencia P95 | <500ms en APIs críticas |
| Compliance (tabla resumen del proveedor) | OWASP |

> ⚠️ La sección "Mapa de Microservicios" del documento fuente (ver [mapa_de_microservicios_wallet.md](mapa_de_microservicios_wallet.md)) solo nombra ~23 microservicios concretos de Wallet Service, no 47+. Ver gap registrado en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

## 2. Principios Arquitectónicos

| Principio | Descripción |
|---|---|
| **Microservicios** | Cada servicio se desarrolla, despliega y escala de forma autónoma (SRP). Comunicación exclusiva vía REST/JSON y eventos de dominio (RabbitMQ). |
| **Clean Architecture + SOLID** | 4 capas por microservicio: Domain, Application, Infrastructure, API. Inyección de dependencias nativa de .NET Core. |
| **CQRS** | Vía MediatR — separa Commands (escritura) de Queries (lectura, potencialmente cacheadas en Redis). Crítico en servicios de alta concurrencia (Operaciones, Cuenta). |
| **Event-Driven** | MassTransit sobre RabbitMQ. Habilita Sagas (transacciones distribuidas con compensación), Routing Slips (workflows multi-step) y Delayed Retry (backoff exponencial). |
| **REST orientado a recursos** | Métodos HTTP estándar (GET/POST/PUT/PATCH/DELETE), documentado con OpenAPI 3.0/Swagger, versionado, validado con FluentValidation. |
| **Resiliencia por diseño** | Polly Framework: Circuit Breaker, Retry con backoff exponencial, Timeout, Fallback, Bulkhead Isolation. Health Checks (liveness/readiness) para Kubernetes. |

## 3. Stack Tecnológico

| Capa | Tecnología | Versión | Propósito |
|---|---|---|---|
| Backend | .NET Core | 8.0 | Framework principal de microservicios |
| API | ASP.NET Core Web API | 8.0 | Exposición REST con validación y documentación |
| Mediación | MediatR | 12.x | CQRS: Commands, Queries, Notifications |
| ORM | Entity Framework Core | 8.0 | Acceso a datos, migraciones, Unit of Work |
| Base de Datos | SQL Server | 2019+ | Persistencia relacional con TDE, RLS, Read Replicas |
| Mensajería | RabbitMQ + MassTransit | 3.11 / 8.x | Event Bus, Sagas, Publish-Subscribe, Routing Slips |
| Caché | Redis | 7.0 | Caché distribuido, sesiones, rate limiting |
| Contenedores | Docker | Latest | Containerización Linux |
| Orquestación | Azure AKS | 1.27+ | Kubernetes gestionado, HPA, Network Policies |
| CI/CD | Azure DevOps | - | Pipelines automatizados |
| Logging | Serilog | Latest | Logging estructurado multi-sink |
| Resiliencia | Polly | 8.x | Circuit Breaker, Retry, Timeout, Bulkhead |
| Validación | FluentValidation | 11.x | Validación declarativa de requests |
| Monitoreo | Application Insights | - | Telemetría, distributed tracing, alertas |
| Documentación API | Swagger / OpenAPI | 3.0 | Documentación interactiva |
| Análisis Estático | SonarQube | - | Quality gates en CI |

> ⚠️ El diagrama de red real (`Diagrama - Bind-PSP.jpg`) etiqueta una instancia **MongoDB** en producción como `mongodb-botonsimple-prd-boveda-api` (nombre que sugiere Botón Simple), que no figura en esta tabla de stack tecnológico (solo declara SQL Server). **Atribución en disputa:** el usuario indicó que, según su conocimiento, MongoDB solo se usa en **Ardid**, no en Botón Simple, y que no está claro si este documento de arquitectura describe a Ardid. Pendiente de confirmación con Infraestructura — ver gap en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md) y detalle en [topologia_de_red.md](topologia_de_red.md).

## Ver también
- [ecosistemas_y_capas.md](ecosistemas_y_capas.md) — capas de la plataforma y los 6 ecosistemas de negocio.
- [calidad_y_cicd.md](calidad_y_cicd.md) — testing, CI/CD, roadmap técnico.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/index.md §1-3` (reestructuración PARA en cascada). Contenido sin cambios.*
