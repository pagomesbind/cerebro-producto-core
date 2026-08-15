# Infraestructura Cloud — Azure

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`, sección 10 (Figura 4), diagrama conservado en `wiki/4_archivos/historial_raw/2026-07-02_arquitectura_proveedor/`. Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §2.1-2.4` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

**Microsoft Azure — Región: Brazil South** (failover: East US 2)

## 1. Cluster Kubernetes — Azure AKS v1.27+

| Node Pool | VM Size | Servicios | Escalado |
|---|---|---|---|
| **Critical** | Standard_D4s_v3 | BFF (3 pods), Ops (3 pods), Bind (3 pods), Cuenta (3 pods) | HPA 3–20 nodos |
| **Services** | Standard_D2s_v3 | Costos, Inversiones, Comprobantes, Notificaciones | HPA 2–10 nodos |
| **Queries** | Standard_D2s_v3 | Cuenta.Q, Ops.Q, Comprobante.Q, Reporte.Q | Read-only optimized |

> Ver [mantenimiento_y_capacidad_aks.md](mantenimiento_y_capacidad_aks.md) para el plan de desescalado/optimización de agosto 2026 sobre este mismo cluster.

## 2. Servicios de Datos

- **Azure SQL Server** — DB por servicio, Read Replicas, TDE.
- **Redis Cache 7.0** — Cluster Mode, Session, Distributed Cache.
- **RabbitMQ 3.11** — Quorum Queues, MassTransit, HA.
- **Azure Blob Storage** — Archivos, Logs, Backups, PDFs.
- **Azure Key Vault** — Secrets, Certificates, Encryption Keys.

## 3. Networking y Observabilidad

- **Networking:** Azure CNI, Network Policies, Ingress NGINX, Azure Load Balancer, Private Endpoints, NSG, VNet Peering, mTLS interno.
- **Observabilidad:** Application Insights, Azure Monitor, Serilog, Distributed Tracing, HealthChecks UI, Alertas.

## 4. CI/CD y Disaster Recovery

| Ítem | Detalle |
|---|---|
| **CI/CD** | Azure DevOps: Build → Test → SonarQube → Docker → ACR → AKS Deploy (Blue-Green) → ArgoCD GitOps |
| **Disaster Recovery** | RTO: 4h · RPO: 1h · Backups diarios · Geo-Replication · Auto-failover group |

## Ver también
- [topologia_de_red.md](topologia_de_red.md) — infraestructura Azure real y nombrada (distinta de esta descripción genérica de evaluación contractual).
- [nfr_y_slas.md](nfr_y_slas.md) — alta disponibilidad y SLAs técnicos sobre esta infraestructura.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §2.1-2.4` (reestructuración PARA en cascada). Contenido sin cambios.*
