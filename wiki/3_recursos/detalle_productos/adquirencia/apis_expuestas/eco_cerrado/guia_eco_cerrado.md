# Guía: Eco Cerrado — Adquirencia

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/guia-ecocerrado
> Producto: Adquirencia / Soluciones de Cobro

---

## Descripción

Esta solución "permite registrar transacciones para las que se resolvió el cobro dentro del ecosistema cerrado de la entidad sin haber realizado un procesamiento externo."

Aplica a entidades con billetera virtual propia que debitan directamente del saldo del pagador.

La funcionalidad trabaja en sinergia con canales de pago QR interoperables, permitiendo a los comercios aceptar pagos de cualquier billetera mientras restringen las órdenes pagadas a través de la billetera propia de la entidad de pagos subsiguientes por otros proveedores.

Cuando las cuentas de los comercios se conectan a los productos de Wallet de Bind PSP con cuentas CVU asociadas, el sistema gestiona automáticamente los saldos acreditando importes netos de transacción y debitando asincrónicamente los impuestos aplicables.

## Flujo — Cobro en ecosistema cerrado

```
CASO DE USO TÍPICO:
  Entidad tiene billetera propia + QR interoperable expuesto en el comercio
  
  Escenario A: pagador usa billetera de otra entidad → flujo QR interoperable estándar
  Escenario B: pagador usa la billetera propia de la entidad → flujo eco cerrado

FLUJO ECO CERRADO:
  1. Entidad resuelve el cobro internamente (débito del saldo del pagador en su billetera)
     → Sin procesamiento externo (sin Coelsa/red)

  2. POST /informar-eco-cerrado
     → Body: datos de la transacción (comercio, caja, monto, medio de pago, referencia)
     → Si hay orden de venta/deuda activa (QR abierto): la aprueba y la cierra
       para evitar que se pague nuevamente con otra billetera

  3. Bind PSP registra la transacción en el sistema
     → EVENT "aviso.eco.cerrado" → webhook a la entidad
     → Liquidación: si comercio tiene CVU de Wallet:
         Crédito en línea (importe neto) + Débito asincrónico de impuestos

DEVOLUCIÓN:
  POST /devolucion-eco-cerrado → revierte el cobro registrado
  → La entidad gestiona manualmente el reembolso al pagador en su billetera
```

## Endpoints Disponibles (Slugs Reales del Portal)

| Slug Real | Método | Operación |
|-----------|--------|-----------|
| `./informarecocerrado` | POST | Informar transacción de eco cerrado |
| `./devolucionecocerrado` | POST | Devolver transacción de eco cerrado |
| `./webhook-adecocerrado` | EVENT | Aviso de transacción eco cerrado |
