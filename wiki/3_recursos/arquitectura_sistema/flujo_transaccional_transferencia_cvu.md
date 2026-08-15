# Flujo de Transferencia CVU — Del API Público al Ledger y Webhook de Salida

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`, sección 12 (Figura 5 — Diagrama de Secuencia), diagrama conservado en `wiki/4_archivos/historial_raw/2026-07-02_arquitectura_proveedor/`. Reubicado desde `arquitectura_sistema/flujo_transaccional.md §1` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

Viaje técnico completo de una transferencia, desde el ingreso por API pública hasta la confirmación al usuario y los procesos asincrónicos posteriores.

Actores del diagrama: **Usuario → BFF → Operaciones → Costos → Bind → Coelsa → Event Bus**

| # | Paso | Detalle técnico |
|---|---|---|
| 1 | `POST /transferencias` | Usuario → BFF. Incluye header `JWT + CorrelationID`. |
| 2 | `CreateTransferenciaCommand` | BFF → Operaciones. Traducción de request HTTP a Command (CQRS). |
| 3 | Validaciones | Dentro de Operaciones, vía FluentValidation. |
| 4 | `CalcularComision` | Operaciones → Costos (síncrono). |
| 4.1 | Respuesta: Monto + Comisión + IVA | Costos → Operaciones. |
| 5 | `ReservarFondos` + `EnviarTransferencia` | Operaciones → Bind. |
| 6 | `Transfer` (mTLS) | Bind → Coelsa — llamada saliente autenticada con certificado mutuo. |
| 7 | Confirmación | Coelsa → Bind. |
| 8 | `TransferenciaConfirmada` | Bind → Operaciones. |
| 9 | Commit TX + Generación de Comprobante | Dentro de Operaciones. Punto de atomicidad transaccional. |
| 10 | `HTTP 200 + Receipt` | Operaciones → BFF. |
| 11 | Response | BFF → Usuario. **Fin del camino síncrono.** |
| 12 | `Publish TransferenciaConfirmadaEvent` | Operaciones → Event Bus (async, post-commit). Consumers: Notificaciones (push), Comprobantes (AFIP), Costos (liquidación). |

**Garantías del flujo:**
- Atomicidad transaccional en cada microservicio (paso 9 — commit local antes de responder al usuario).
- Consistencia eventual entre servicios mediante eventos de dominio (paso 12 en adelante).
- Trazabilidad completa vía **Correlation ID** propagado en todos los servicios involucrados, desde el paso 1.
- Los pasos asincrónicos post-commit (notificación, comprobante fiscal, liquidación de comisión) son independientes y resilientes — una falla en Notificaciones no revierte la transferencia ya confirmada al usuario.

## Ver también
- [modelo_de_seguridad.md](modelo_de_seguridad.md) — mTLS en la conexión a Coelsa (paso 6), JWT en el ingreso del usuario (paso 1), TDE en el commit a SQL Server (paso 9).
- [topologia_de_eventos.md](topologia_de_eventos.md) — qué pasa con `TransferenciaConfirmadaEvent` (paso 12) del lado del Event Bus.
- [patrones_de_implementacion.md](patrones_de_implementacion.md) — Sagas de alta de cuenta y transferencia con liquidación, mismo patrón de fondo.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/flujo_transaccional.md §1` (reestructuración PARA en cascada). Contenido sin cambios.*
