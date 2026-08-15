# Guía — ¿Cómo transferir desde la CBU? (Agente de Cobros)

> Fuente: https://psp.bind.com.ar/developers/apis/guia-agente-de-cobro-saliente
> Producto: Agente de Cobros

## Descripción

Con esta solución se puede automatizar la creación de transferencias salientes con la CBU de la cuenta recaudadora asignada a la entidad como origen.

La operación puede ser en pesos o en dólares, dependiendo de la moneda de la cuenta.

Debe monitorearse cada transferencia hasta asegurar un estado definitivo de la misma.

## Flujo — Integración de transferencia saliente

```
1. [Opcional] GET /Balance → verificar saldo disponible antes de transferir

2. POST /transaction-requests
   → Body: origin_id (máx 15 chars, único por transacción)
           + to.cbu (CBU/CVU destino) o to.alias
           + value.currency ("ARS" o "USD") + value.amount
           + concept ("VAR"/"ALQ"/"CUO"/"EXP"/"FAC"/"PRE"/"SEG"/"HON"/"HAB")
           + description (opcional, máx 100 chars)
           + emails (opcional, para envío de comprobante)
   → Idempotente: si origin_id ya existe, devuelve la transacción original sin crear nueva

3. Respuesta inmediata: estado PENDING o IN_PROGRESS
   → Monitorear con GET /TRANSFER/{origin_id} hasta estado definitivo

4. EVENT "TRANSFER" → webhook cuando alcanza estado definitivo
```

## Flujo de estados posibles de una transferencia saliente

```
                    ┌─────────┐
                    │ PENDING │
                    └────┬────┘
                         │
                    ┌────▼────────┐
                    │ IN_PROGRESS │
                    └────┬────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
    ┌─────▼──────┐ ┌────▼────┐ ┌──────▼──────────┐
    │ COMPLETED  │ │ FAILED  │ │    UNKNOWN        │
    │  ✓ final   │ │ ✗ final │ │ (reintenta en día)│
    └────────────┘ └─────────┘ └──────┬────────────┘
                                       │
                               ┌───────▼───────────┐
                               │ UNKNOWN_FOREVER    │
                               │ (gestión manual)   │
                               └───────────────────┘
```

| Estado | Definitivo | Descripción |
|--------|------------|-------------|
| `PENDING` | No | Pendiente de iniciar |
| `IN_PROGRESS` | No | En curso (transferencias a CVU arrancan aquí) |
| `COMPLETED` | Sí | Fondos acreditados en destino |
| `FAILED` | Sí | Rechazada; saldo devuelto automáticamente |
| `UNKNOWN` | No | Error de comunicación; sistema reintenta resolver durante el día |
| `UNKNOWN_FOREVER` | Sí | No pudo resolverse; requiere gestión manual |

**Nota:** Las transferencias a CVU pueden quedar en IN_PROGRESS hasta el cierre del día cuando se concilian todas las operaciones del batch.
