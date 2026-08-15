# Patrones y Prácticas de Implementación — CQRS, Sagas, Resiliencia

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`. Reubicado y consolidado desde `arquitectura_sistema/index.md §8` y `flujo_transaccional.md §2` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

## 1. Patrones generales

| Patrón | Detalle |
|---|---|
| **CQRS con MediatR** (Figura 2) | Command Side: `MediatR IRequest<TResponse>` → Command Handler + FluentValidation → Domain Layer → Repository (EF Core) → SQL Server (Write) → Publish Domain Event → MassTransit. Query Side: `MediatR IRequest<TResponse>` → Query Handler (Read-Only DTOs) → Redis Cache / SQL Read Replica → DTO optimizado al cliente. Sincronización entre lados vía eventos de dominio asíncronos. |
| **Repository + Unit of Work** | EF Core implementa Unit of Work, garantizando atomicidad por bounded context. Database per Service — sin acoplamiento a nivel de datos. |
| **Circuit Breaker y Resiliencia (Polly)** | Protege llamadas a dependencias externas (bancos, AFIP, proveedores crypto). Circuit Breaker ante umbral de errores consecutivos, retries con backoff exponencial + jitter, Bulkhead con semáforos, Timeouts contra bloqueos por latencia. |

## 2. Sagas (transacciones distribuidas)

Orquestadas por MassTransit, con acciones de compensación por paso. Sagas principales:

### 2.1 Alta de Cuenta con CVU — 7 pasos
1. Inicio de registro
2. Validación de identidad (AFIP/RENAPER)
3. Creación de cuenta interna
4. Solicitud de CVU a Bind
5. Confirmación de Coelsa
6. Activación de cuenta
7. Notificación de bienvenida

> El documento fuente no detalla las acciones de compensación específicas de cada paso — solo confirma que existen. Ver gap correspondiente en [../../2_areas/gaps_y_preguntas.md](../../2_areas/gaps_y_preguntas.md) si se requiere el detalle para diseño de resiliencia propio.

### 2.2 Otras Sagas mencionadas (sin diagrama de secuencia propio en el documento fuente)
- **Transferencia con Liquidación** — 8 pasos.
- **Pago QR Interoperable** — 6 pasos.

## Ver también
- [flujo_transaccional_transferencia_cvu.md](flujo_transaccional_transferencia_cvu.md) — el viaje paso a paso de una transferencia real, aplicando estos patrones.
- [topologia_de_eventos.md](topologia_de_eventos.md) — Event Bus y patrones de comunicación asíncrona.
- [mapa_de_microservicios_wallet.md](mapa_de_microservicios_wallet.md) — microservicios que implementan estos patrones.

---
*Última actualización: 2026-08-12 — Reubicado y consolidado desde `arquitectura_sistema/index.md §8` y `flujo_transaccional.md §2` (reestructuración PARA en cascada). Contenido sin cambios.*
