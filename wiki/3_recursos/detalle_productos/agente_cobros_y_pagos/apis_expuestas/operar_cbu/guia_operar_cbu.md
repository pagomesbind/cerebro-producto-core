# Guía — Operar con CBU Recaudadora (Agente de Cobros)

> Fuente: https://psp.bind.com.ar/developers/apis/guia-agente-de-cobro-cbu
> Producto: Agente de Cobros

## Guía 1: ¿Cómo conciliar transferencias recibidas en la CBU?

Esta solución permite detectar en línea transferencias entrantes recibidas directamente en la CBU recaudadora de la PSP asociada a la entidad.

La entidad puede identificar y conciliar en línea transferencias tanto en pesos argentinos como en dólares, dependiendo de la moneda de la cuenta asignada.

> Fuente guía saliente: https://psp.bind.com.ar/developers/apis/guia-agente-de-cobro-saliente

## Guía 2: ¿Cómo transferir desde la CBU?

Ver guía en: https://psp.bind.com.ar/developers/apis/guia-agente-de-cobro-saliente

## Flujo — Conciliar transferencias recibidas en la CBU

```
OPERATORIA NORMAL (por cada pago entrante):
  1. Pagador transfiere directamente al CBU de la cuenta recaudadora de la entidad
  2. EVENT "transfer.cbu.received" → webhook a URL configurada
     → data.id = ID Coelsa
     → data.status = "COMPLETED"
     → data.charge.value.amount = monto | currency = "ARS" o "USD"
     → data.counterparty = información del pagador (nombre, CUIT, CBU/CVU origen)
  3. Entidad concilia el pago en su sistema
```

## Flujo — Transferencia saliente desde la CBU

```
1. POST /transaction-requests (origin_id + cbu/alias destino + currency + amount + concept)
   → estado inicial: PENDING o IN_PROGRESS
   → Si origin_id ya existe: devuelve la transacción original (idempotente)

2. Monitoreo del estado (hasta llegar a estado definitivo):
   GET /transaction-requests/TRANSFER/{origin_id o ID Coelsa}
   → Estados: PENDING → IN_PROGRESS → [definitivo]

3. EVENT "TRANSFER" → webhook cuando se alcanza estado definitivo

Estados definitivos:
  COMPLETED      → fondos acreditados en destino ✓
  FAILED         → rechazada; saldo devuelto automáticamente ✗
  UNKNOWN        → error de comunicación; el sistema reintenta resolver durante el día
  UNKNOWN_FOREVER → no pudo resolverse automáticamente; requiere gestión manual

Nota: transferencias a CVU quedan inicialmente en IN_PROGRESS y se resuelven
durante el día o al cierre cuando se concilian todas las operaciones.

4. [Opcional] GET /Balance → verificar saldo disponible en la recaudadora antes de transferir
```

## API Reference

| Método | Endpoint | Archivo |
|--------|----------|---------|
| `POST` | Realizar Transferencia | [endpoint_post_realizar_transferencia_cbu.md](endpoint_post_realizar_transferencia_cbu.md) |
| `GET` | Consultar transferencia | [endpoint_get_consultar_transferencia.md](endpoint_get_consultar_transferencia.md) |
| `GET` | Consultar saldo de recaudadora | [endpoint_get_consultar_saldo_recaudadora_cbu.md](endpoint_get_consultar_saldo_recaudadora_cbu.md) |
| `EVENT` | Aviso de transferencia saliente desde CBU | [endpoint_event_transferencia_saliente_cbu.md](endpoint_event_transferencia_saliente_cbu.md) |
| `EVENT` | Aviso de transferencia entrante en CBU | [endpoint_event_transferencia_entrante_cbu.md](endpoint_event_transferencia_entrante_cbu.md) |
