# Guía — Transferencias Entrantes CVU (Agente de Cobros)

> Extraído el: 2026-06-30  
> Fuente: https://psp.bind.com.ar/developers/apis/guia-agente-de-cobro-cvu  
> Producto: Agente de Cobros

## Descripción

Permite identificar en línea transferencias entrantes asociadas a un CVU específico para conciliar pagos. Los CVU creados deben ser de titularidad de la entidad cobradora.

## Flujo — Conciliación de transferencias entrantes a CVU

```
SETUP:
  POST /cvu (client_id + cuit + name) → CVU asignado para recibir transferencias
  POST /alias (cvu + label) → alias opcional

OPERATORIA NORMAL:
  1. Pagador transfiere al CVU de la entidad cobradora
  2. EVENT "transfer.cvu.received" → webhook con datos de la transferencia
     → data.details.origin_credit.cvu = CVU destino
     → data.charge.value.amount = monto recibido
  3. Entidad concilia en su sistema

SI NO LLEGÓ EL WEBHOOK:
  GET /transfers (filtros: cvu, fromDate, toDate) → buscar en el listado
  POST /concilitations-by-transfer (transactions_ids) → forzar conciliación por ID Coelsa

BAJA:
  DELETE /cvu/{cvu}/{cuit} → inactiva el CVU (puede reactivarse con los mismos datos)
```

## Endpoints

| Método | Operación | Archivo |
|--------|-----------|---------|
| `POST` | Crear CVU | endpoint_post_crear_cvu.md |
| `POST` | Asignar alias | — |
| `DELETE` | Eliminar CVU | — |
| `GET` | Consultar transferencias | endpoint_get_consultar_transferencias.md |
| `POST` | Conciliar transferencia entrante | — |
| `EVENT` | Webhook transferencia entrante en CVU | endpoint_event_transferencia_entrante_cvu.md |
