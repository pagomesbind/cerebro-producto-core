# Calidad, CI/CD y Roadmap Técnico — Resumen del Proveedor

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`. Reubicado desde `arquitectura_sistema/index.md §10` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md) — el roadmap técnico en particular puede estar desactualizado.

- **Testing:** Unit Tests 75%+ cobertura en domain/application; Integration Tests en todos los endpoints críticos; Contract Tests entre servicios; Load Tests a 10x carga normal; Chaos Engineering mensual (kill pods, network partition, disk full).
- **CI/CD:** Azure DevOps — build → tests → SonarQube (quality gates) → Docker → Azure Container Registry → AKS rolling rollout.
- **Estandarización:** Clean Architecture uniforme, PRs con mínimo 2 aprobaciones, análisis estático en CI, documentación OpenAPI/Swagger al 100%.
- **Mecanismos de integración para clientes:** REST APIs (Swagger/OpenAPI 3.0, JWT, rate limiting), SDK .NET (NuGet), Webhooks (retry exponencial, dead letter, firma HMAC), Batch/SFTP, Event Streaming (en roadmap, CloudEvents).
- **Roadmap técnico:** corto plazo — migración a .NET 10 (ver [modernizacion_plataforma_dotnet.md](modernizacion_plataforma_dotnet.md) para el estado real de la migración a .NET 8, paso previo), upgrade Redis Cluster Mode; mediano plazo — Service Mesh (Istio), certificación ISO 27001; largo plazo — mensajería ISO 20022, Event Streaming para integradores.

## Ver también
- [relacion_con_fintexa.md §2](relacion_con_fintexa.md#2-comité-de-arquitectura-coe--informe-mensual-julio-2026) — estado real (julio 2026) de varias de estas iniciativas de roadmap, según el Comité de Arquitectura.
- [modernizacion_plataforma_dotnet.md](modernizacion_plataforma_dotnet.md) — migración a .NET 8 ya en curso, según Epics históricas.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/index.md §10` (reestructuración PARA en cascada). Contenido sin cambios.*
