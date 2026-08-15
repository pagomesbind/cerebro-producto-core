# Topología de Eventos — Event Bus

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`, sección 13 (Figura 6 — Topología de Eventos), diagrama conservado en `wiki/4_archivos/historial_raw/2026-07-02_arquitectura_proveedor/`. Reubicado desde `arquitectura_sistema/flujo_transaccional.md §3` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

El **Event Bus** (RabbitMQ + MassTransit + CloudEvents) es la columna vertebral de comunicación asíncrona entre microservicios.

## Publishers (dominios que emiten eventos)

| Dominio | Eventos |
|---|---|
| **Cuenta** | `AltaCvuEvent`, `EnrolamientoEvent`, `CambioEstadoCuentaEvent`, `ActualizacionKYCEvent` |
| **Operaciones** | `TransferenciaEvent`, `PagoQREvent`, `DEBINEvent`, `OperacionCargoEvent` |
| **Inversiones** | `SuscripcionFCIEvent`, `CompraDolarCCLEvent`, `OperacionCryptoEvent`, `LiquidacionEvent` |
| **Comprobantes** | `ComprobanteGeneradoEvent`, `FacturaAFIPEvent`, `ExtractoEvent` |
| **Integraciones** | `BindTransferEvent`, `CoelsaResponseEvent`, `PixPaymentEvent` |

## Consumers (dominios que consumen eventos)

| Dominio | Alcance |
|---|---|
| **Notificaciones** | Push, Email, SMS, Webhooks |
| **Comprobantes** | AFIP, PDF, Extractos |
| **Costos** | Liquidación, Comisiones |
| **Bind/Banking** | Clearing, Conciliación |
| **Auditoría** | Audit Trail, Compliance Logs |

## Patrones de comunicación implementados

| Patrón | Uso |
|---|---|
| **Publish-Subscribe** | Eventos de dominio broadcast a múltiples consumers. |
| **Request-Reply** | Operaciones síncronas críticas con timeout (ej. `CalcularComision` en el flujo de transferencia). |
| **Routing Slip** | Workflows multi-step complejos. |
| **Saga Pattern** | Transacciones distribuidas con compensación automática — ver [patrones_de_implementacion.md §2](patrones_de_implementacion.md). |

Los eventos se serializan como **CloudEvents** y se procesan mediante **Quorum Queues** de RabbitMQ, garantizando durabilidad y tolerancia a particiones de red.

## Ver también
- [flujo_transaccional_transferencia_cvu.md](flujo_transaccional_transferencia_cvu.md) — dónde entra `TransferenciaConfirmadaEvent` en un flujo real.
- [patrones_de_implementacion.md](patrones_de_implementacion.md) — Sagas y CQRS.

---
*Última actualización: 2026-08-12 — Reubicado desde `arquitectura_sistema/flujo_transaccional.md §3` (reestructuración PARA en cascada). Contenido sin cambios.*
