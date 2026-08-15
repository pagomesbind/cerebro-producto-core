# Wallet Service — Arquitectura Detallada y Mapa de Microservicios

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`. Reubicado desde `arquitectura_sistema/index.md §6-7` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md) y el gap de inconsistencia de conteo (47+ declarados vs. ~23 nombrados acá) en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md).

## 1. Dominios Funcionales

47+ microservicios dedicados (ver nota de inconsistencia), organizados en 7 dominios funcionales:

### 1.1 Gestión de Cuentas y Onboarding (`Wallet.Cuenta`)
Ciclo de vida completo de cuentas virtuales: alta de personas físicas/jurídicas con validación automática AFIP/RENAPER, emisión instantánea de CVU vía Coelsa, cumplimiento KYC/AML y monitoreo de PEPs.
**Valor de negocio:** reduce el onboarding de días a minutos, automatizando validaciones regulatorias.

### 1.2 Operaciones Financieras (`Wallet.Operaciones`)
Procesa todas las transacciones: transferencias inmediatas (CVU/CBU/Alias), pagos QR interoperable, débitos automáticos DEBIN, transferencias internacionales a Brasil vía PIX. Cada operación valida fondos en tiempo real, aplica comisiones, genera comprobantes fiscales y publica eventos downstream.
**Valor de negocio:** operación 24x7 con liquidación inmediata.

### 1.3 Motor de Costos y Comisiones (`Wallet.CalculadorCostos`)
Pricing basado en reglas configurables: segmentación dinámica de clientes, tarifas diferenciadas por tipo/volumen, cálculo automático de impuestos y retenciones (IVA, IIBB, percepciones), liquidación programada. Soporta tarifas planas, porcentuales, mixtas y escalonadas.
**Valor de negocio:** maximiza rentabilidad vía pricing dinámico sin modificar código.

### 1.4 Integraciones Bancarias (`Wallet.Bind`)
Gateway unificado hacia la red bancaria argentina: conectividad Coelsa para CVU, transferencias interbancarias, conciliación automática de movimientos, manejo de rechazos/devoluciones. Reintentos automáticos con Polly y circuit breakers.

### 1.5 Inversiones y Crypto (`Wallet.InvestmentService`)
Suscripción/rescate de FCI, compra/venta de dólar MEP y CCL vía **Poincenot**, trading de criptomonedas vía **Lirium**.

### 1.6 Comprobantes y Cumplimiento Fiscal (`Wallet.Comprobante`)
Facturación electrónica AFIP, comprobantes de retención/percepción, extractos y resúmenes de cuenta, certificados de saldo para auditorías, reportes de impuestos (`Wallet.Tin`). Archivo histórico con validez legal.

### 1.7 Notificaciones Multicanal (`Wallet.Notificaciones`)
Push a apps móviles, emails transaccionales/marketing, SMS (autenticación y alertas), webhooks para terceros. Gestión de preferencias, templating dinámico, compliance de privacidad.

## 2. Mapa de Microservicios (Wallet Service)

| Capa | Microservicio | Responsabilidad Principal |
|---|---|---|
| Presentación | `Wallet.APP` / `Wallet.AppSDK` | App móvil y SDK de integración |
| Presentación | `Wallet.BFF` / `BFF.PSP` | Backend-for-Frontend, agregación, autenticación |
| Dominio (Commands) | `Wallet.Cuenta` | Alta CVU, KYC/AML, onboarding, gestión de cuentas |
| Dominio (Commands) | `Wallet.Operaciones` | Transferencias, QR Pay, DEBIN, PIX |
| Dominio (Commands) | `Wallet.CalculadorCostos` | Pricing, segmentos, liquidación de comisiones |
| Dominio (Commands) | `Wallet.InvestmentService` | FCI, MEP/CCL, criptomonedas |
| Dominio (Commands) | `Wallet.Bind` | Gateway Coelsa, banking, clearing |
| Dominio (Commands) | `Wallet.Comprobante` | Facturación AFIP, PDF, extractos |
| Dominio (Commands) | `Wallet.Notificaciones` | Push, email, SMS, webhooks |
| Dominio (Commands) | `Wallet.Tin` | Impuestos, retenciones, reportes fiscales |
| Queries (CQRS) | `Cuenta.Queries` | Consultas optimizadas de cuentas |
| Queries (CQRS) | `Operaciones.Queries` | Consultas de transacciones e historial |
| Queries (CQRS) | `Comprobante.Queries` | Consultas de comprobantes y extractos |
| Queries (CQRS) | `Wallet.Reporte` | Reportería y analytics |
| Compartidos | `Shared.Debin` / `Shared.Crypto` | Lógica compartida DEBIN y cripto |
| Compartidos | `Shared.Pix` / `Shared.Dispatch` | PIX transfronterizo, dispatch de eventos |
| Compartidos | `Shared.Email` / `Shared.Files` | Email transaccional, gestión de archivos |
| Compartidos | `Shared.QueueSentinel` | Monitoreo y health de colas RabbitMQ |

## Ver también
- [ecosistemas_y_capas.md](ecosistemas_y_capas.md) — capas de plataforma y los 6 ecosistemas de negocio.
- [patrones_de_implementacion.md](patrones_de_implementacion.md) — CQRS, Sagas, Repository, Circuit Breaker.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/index.md §6-7` (reestructuración PARA en cascada). Contenido sin cambios.*
