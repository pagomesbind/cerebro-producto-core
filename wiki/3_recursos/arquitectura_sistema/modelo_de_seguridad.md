# Modelo de Seguridad — Defensa en Profundidad

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`, sección 9 (Figura 3), diagrama conservado en `wiki/4_archivos/historial_raw/2026-07-02_arquitectura_proveedor/`. Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §1` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

## 1. Modelo de 5 capas

Cada capa mapeada a requisitos específicos de **PCI DSS v4.0 Level 1**, OWASP Top 10 2021, CWE Top 25 y OWASP ASVS v4.0:

| Capa | Controles | Mapeo normativo (según diagrama) |
|---|---|---|
| **Perímetro** | TLS 1.2+, WAF, DDoS Protection, Certificate Pinning, Rate Limiting | PCI DSS Req. 1, 2, 4 · OWASP ASVS L2 |
| **Autenticación y Autorización** | JWT Bearer Tokens, RBAC, Claims-Based Access, MFA, OAuth 2.0, API Keys | PCI DSS Req. 7, 8 · OWASP Top 10 A01, A07 |
| **Aplicación** | FluentValidation, Input Sanitization, CORS, CSP Headers, Anti-CSRF, Parameterized Queries | PCI DSS Req. 6 · OWASP Top 10 A03/A08 · CWE Top 25 |
| **Datos** | Tokenización PCI, TDE (SQL Server), Data Masking en Logs, Row-Level Security, Encryption at Rest | PCI DSS Req. 3, 4 · BCRA A-7724 · UIF Res. 67/2011 |
| **Auditoría y Monitoreo** | Serilog Structured Logging, Correlation ID, Application Insights, Immutable Audit Trail | PCI DSS Req. 10, 11 · OWASP Top 10 A09 |

> ⚠️ **Inconsistencia detectada:** este diagrama (Figura 3) es la **única mención de PCI DSS v4.0 Level 1** en todo el documento fuente. La sección de texto "9.1 Estándares y Normativas" (tabla siguiente) y la tabla de "Cifras Clave" del resumen ejecutivo no listan PCI DSS entre los estándares de compliance. Dado que PCI DSS es crítico para el ecosistema Aceptador (procesamiento de tarjetas Visa/Mastercard), esta omisión en el texto narrativo se registró como gap de severidad Media en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md). La recertificación PCI **propia de Bind PSP** (distinta de esta certificación del proveedor) está documentada en [3_recursos/cumplimiento_normativo/pci_dss_recertificacion.md](../cumplimiento_normativo/pci_dss_recertificacion.md).

### 1.1 Estándares y Normativas (tabla de texto, sección 9.1)

| Estándar | Alcance y Estado |
|---|---|
| OWASP Top 10 (2021) | Protección contra vulnerabilidades web críticas: inyección, autenticación rota, exposición de datos, XXE, control de acceso, configuración incorrecta, XSS, deserialización insegura, componentes vulnerables, logging insuficiente. |
| CWE Top 25 (2023) | Mitigación de debilidades de software más peligrosas (MITRE), con análisis estático en pipeline CI. |
| OWASP ASVS v4.0 | Application Security Verification Standard Level 2: verificación de requisitos de seguridad en desarrollo y testing. |
| UIF | Prevención de lavado de activos (AML), reporte de operaciones sospechosas (ROS), monitoreo de PEPs. |
| ISO 27001 | Framework de gestión de seguridad de la información. **Proceso de certificación en curso** (no certificado aún). |

### 1.2 Controles de Seguridad Implementados

| Control | Descripción Técnica |
|---|---|
| Autenticación JWT | Tokens Bearer con claims, roles y expiración. Validación en cada request. |
| Autorización RBAC | Control de acceso basado en roles con policies granulares por endpoint. |
| Cifrado TLS 1.2+ | Cifrado en tránsito obligatorio, certificate pinning, mTLS interno. |
| Tokenización | Datos de tarjeta tokenizados antes del almacenamiento. |
| Rate Limiting | Políticas Polly contra abuso y DDoS en gateway y servicios. |
| Input Validation | FluentValidation en todas las APIs, parameterized queries. |
| Auditoría Completa | Logs de operaciones con Serilog structured logging. |
| Correlation ID | Trazabilidad end-to-end de cada request a través de todos los servicios. |
| Encryption at Rest | TDE en SQL Server, Azure Key Vault para gestión de secretos. |

## Ver también
- [hardening_y_remediacion_de_pentests.md](hardening_y_remediacion_de_pentests.md) — hallazgos reales de pentest y su remediación (complementario a este modelo declarado por el proveedor).
- [mtls_apis_y_webhooks.md](mtls_apis_y_webhooks.md) — mTLS en detalle.
- [3_recursos/cumplimiento_normativo/pci_dss_recertificacion.md](../cumplimiento_normativo/pci_dss_recertificacion.md) — recertificación PCI propia de Bind PSP.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §1` (reestructuración PARA en cascada). Contenido sin cambios.*
