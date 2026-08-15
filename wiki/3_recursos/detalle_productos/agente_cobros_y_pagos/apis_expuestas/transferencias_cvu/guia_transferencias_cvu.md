# Guía: ¿Cómo conciliar con transferencias a CVU? — Agente de Cobros

> Fuente: https://psp.bind.com.ar/developers/apis/guia-agente-de-cobro-cvu
> Producto: Agente de Cobros

## Descripción

Esta solución permite identificar transferencias entrantes asociadas a un CVU específico y de esta manera poder conciliar un pago en línea.

Es posible asignar un alias distinto a cada CVU. También, pueden eliminarse los CVU para que no puedan recibir más transferencias. En caso de querer reactivar un CVU, debe darse de alta con los mismos datos originales.

Por distintos motivos, es posible que alguna transferencia entrante sea correctamente procesada en la red pero la entidad no se notifica de ella. Entonces, la entidad puede conciliarla en línea si conoce el ID Coelsa de la misma.

En esta operatoria, los CVU creados deben ser de titularidad de la entidad cobradora.

## Flujo — Conciliación de transferencia entrante a CVU

```
SETUP (una vez):
  POST /cvu (client_id + cuit + name) → CVU asignado
  POST /alias (cvu + label) → asignar alias si se necesita

OPERATORIA NORMAL (por cada pago):
  1. Pagador realiza transferencia al CVU de la entidad
  2. EVENT "transfer.cvu.received" → webhook a URL configurada
     → data.id = ID Coelsa | data.charge.value.amount = monto
     → data.status = "COMPLETED"
     → data.details.origin_credit.cvu = CVU destino
     → data.details.origin_debit.cvu = CVU/CBU origen del pagador
  3. Entidad identifica el pago por clientId/cvu y concilia en su sistema

CONCILIACIÓN MANUAL (si no llegó el webhook):
  4. GET /transfers (filtrar por cvu / fromDate / toDate / type=TRANSFERENCIAS_RECIBIDAS)
     → buscar la transferencia en el listado

CONCILIACIÓN EN LÍNEA (si se conoce el ID Coelsa pero no está registrada):
  5. POST /concilitations-by-transfer (transactions_ids: [ID Coelsa])
     → conciliadas: insertadas y notificadas | conError: reintentar | noConciliadas: ya existían

BAJA DE CVU:
  DELETE /cvu/{cvu}/{cuit} → inactiva (puede reactivarse creando nuevamente con mismos datos)
```

## API Reference

| Método | Endpoint | Archivo |
|--------|----------|---------|
| `POST` | Crear CVU | [../transferencias_entrantes_cvu/endpoint_post_crear_cvu.md](../transferencias_entrantes_cvu/endpoint_post_crear_cvu.md) |
| `POST` | Asignar alias | [../transferencias_entrantes_cvu/endpoint_post_asignar_alias.md](../transferencias_entrantes_cvu/endpoint_post_asignar_alias.md) |
| `DELETE` | Eliminar CVU | [../transferencias_entrantes_cvu/endpoint_delete_eliminar_cvu.md](../transferencias_entrantes_cvu/endpoint_delete_eliminar_cvu.md) |
| `GET` | Consultar transferencias | [../transferencias_entrantes_cvu/endpoint_get_consultar_transferencias.md](../transferencias_entrantes_cvu/endpoint_get_consultar_transferencias.md) |
| `POST` | Conciliar transferencia entrante | [../transferencias_entrantes_cvu/endpoint_post_conciliar_transferencia.md](../transferencias_entrantes_cvu/endpoint_post_conciliar_transferencia.md) |
| `EVENT` | Aviso de transferencia entrante en CVU | [../transferencias_entrantes_cvu/endpoint_event_transferencia_entrante_cvu.md](../transferencias_entrantes_cvu/endpoint_event_transferencia_entrante_cvu.md) |
