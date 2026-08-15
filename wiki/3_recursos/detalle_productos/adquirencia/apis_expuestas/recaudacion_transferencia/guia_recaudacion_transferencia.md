# Guía: Recaudación por Transferencia (RxT) — Adquirencia

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/guia-rxt
> Producto: Adquirencia / Soluciones de Cobro

---

## Descripción

Esta solución "permite crear un CVU fijo y asociado a una caja." Cuando llegan transferencias a ese CVU, el sistema crea transacciones automáticamente asociadas a esa caja.

La solución trabaja en sinergia con métodos de pago QR estático, permitiendo la asociación de una caja a un cliente mientras concilia pagos realizados a través de ambos métodos de recaudación.

Un caso de uso adicional implica la recepción de transferencias en un punto de venta físico y la conciliación online integrando las mismas en el sistema ERP de la entidad.

## Flujo — Cobro por recaudación de transferencia (RxT)

```
SETUP (una sola vez por cliente o punto de cobro):
  POST /crear-cvu-para-una-caja (codigoCaja)
  → CVU fijo asignado a la caja
  PATCH /asignar-alias → asignar alias al CVU (opcional)

  Caso de uso típico:
  - 1 caja + 1 CVU por cada cliente/deudor (conciliación por caja)
  - O 1 caja + 1 CVU por cada punto de venta físico

OPERATORIA NORMAL:
  1. Pagador transfiere desde su CBU/CVU al CVU de la caja
  2. Bind PSP recibe la transferencia
     → Crea automáticamente una TRANSACCIÓN asociada a la caja
  3. EVENT "aviso.transaccion.rxt" → webhook a la entidad
     → La entidad concilia la transacción en su sistema (ERP, etc.)

SINERGIA CON QR ESTÁTICO:
  → La misma caja puede tener QR estático + CVU RxT
  → Ambos medios generan transacciones en la misma caja → un único punto de conciliación

BAJA:
  DEL /deshabilitar-cvu → CVU deja de recibir transferencias
```

## Endpoints Disponibles (Slugs Reales del Portal)

| Slug Real | Método | Operación |
|-----------|--------|-----------|
| `./crear-cvu-para-una-caja` | POST | Crear CVU para una caja |
| `./asignar-alias-a-cvu-de-una-caja` | PATCH | Asignar alias a CVU de una caja |
| `./deshabilitar-el-cvu-de-una-caja` | DEL | Deshabilitar CVU de una caja |
| `./webhook-adrxt` | EVENT | Aviso de transacción recaudación por transferencia |
