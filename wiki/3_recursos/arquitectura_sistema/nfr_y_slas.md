# NFR y SLAs Técnicos — Alta Disponibilidad

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`, sección 10.2. Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §2.5-2.6` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

## 1. Alta Disponibilidad

| Capacidad | Implementación |
|---|---|
| Réplicas mínimas | 3 pods para servicios críticos (BFF, Operaciones, Bind, Cuenta) |
| Health Checks | Liveness y readiness probes en todos los servicios, HealthChecks UI |
| Circuit Breakers | Polly policies para prevenir cascading failures |
| Backups | Snapshots diarios de bases de datos con retención de 30 días, geo-replication |
| Deployment | Blue-Green deployments con zero-downtime, automated rollback ante fallas |

## 2. SLAs Técnicos

| Métrica | Target | Medición |
|---|---|---|
| Uptime | 99.9% | Disponibilidad mensual end-to-end |
| Latencia P95 | <500ms | APIs críticas, percentil 95 |
| Throughput | 1.000 TPS | Transacciones por segundo sostenidas bajo carga normal |
| Error Rate | <0.1% | Porcentaje de requests fallidos sobre total procesado |
| Recovery Time | <5 min | Auto-recuperación ante fallas de pods individuales |

## Ver también
- [infraestructura_cloud_azure.md](infraestructura_cloud_azure.md) — infraestructura que sostiene estos SLAs.
- [mantenimiento_y_capacidad_aks.md](mantenimiento_y_capacidad_aks.md) — plan de mantenimiento que puede impactar temporalmente estos targets.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §2.5-2.6` (reestructuración PARA en cascada). Contenido sin cambios.*
