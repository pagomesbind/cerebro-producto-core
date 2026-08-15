# Guía: ¿Cómo cobrar con QR estático?

> Sincronizado el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/guia-qrest%C3%A1tico
> Producto: Adquirencia > QR Estático

---

## Contenido literal de la guía del portal

Esta solución permite cobrar a partir de la generación de un QR interoperable que puede ser leído y pagado por cualquier billetera digital en Argentina.

En este caso la entidad puede generar un QR del tipo estático, es decir que contiene información fija y no modificable. En nuestro sistema, un QR estático se genera asociado a una caja. Por lo tanto, cuando ingresen pagos realizados a un QR, estos resultarán en transacciones asociadas a la caja.

Por cada caja, el QR estático se puede generar una vez sola y guardarse, ya que nunca cambiará.

En este esquema de cobro sólo el comercio dueño del QR tiene la posibilidad de iniciar una devolución parcial o total de un pago. El usuario pagador del QR nunca podrá ejecutar un contracargo o desconocimiento por su cuenta.

Estos QR pueden ser de monto abierto, de monto cerrado o admitir ambos:

- **De monto abierto:** Puede ser pagado sin tener una orden de venta asociada. Esto significa que si una billetera lo lee con la intención de pagarlo, la aplicación le indicará al usuario que debe ingresar el monto a pagar. Entonces, si el usuario concreta un pago, el monto cobrado será el que ingresó el usuario.
- **De monto cerrado:** Tiene una orden de venta asociada. Esto significa que si una billetera lo lee con la intención de pagarlo, la aplicación le indicará al usuario que debe abonar un monto fijo. Entonces, si el usuario concreta un pago, el monto cobrado será si o si el fijado por el comercio en la orden de venta. En nuestra solución, un QR puede restringirse a ser pagado sólo como monto cerrado o no. En el caso de restringirse un QR a que sólo admita monto cerrado, si una billetera lo lee y este no tiene una orden de venta pendiente para ser pagada, la billetera mostrará un error y no se le permitirá pagar.

## Monto abierto o cerrado

Lo que determina si la modalidad de cobro será de monto abierto o cerrado es la caja. Una caja con atributo `soloOrden=false` admite que el QR sea pagado tanto con monto abierto como con monto cerrado. En cambio, si `soloOrden=true` solo admitirá ser pagado con monto cerrado.

La imagen del código QR asociado a una caja puede generarse y guardarse una única vez ya que no cambiará.

## Casos de uso posibles

Algunos ejemplos de caso de uso posibles en donde se podría implementar esta modalidad de cobranza son:

- **Cobranza presente en caja:** En comercios físicos se puede crear una caja con su QR estático por cada puesto de cobranza (cajero). En este caso, la cobranza puede limitarse o no a pagarse solo con monto cerrado, haciendo que el cajero desde su plataforma de cobros cree las ordenes de venta cuando corresponda.
- **Cobranza no presente con QR en facturas:** En recaudaciones de deudas recurrentes en donde se identifica al deudor o deuda a pagar recurrentemente (por ejemplo, factura de un servicio a un cliente o cuotas de un préstamo) se puede crear una caja con su QR estático por cada deudor. De esta forma, luego pueden conciliarse los pagos y saldos de deudas al informarse transacciones por pagos a cada caja asociada al deudor.

## Flujo — QR estático de monto cerrado con orden de venta

```
SETUP (una sola vez por puesto de cobro):
  POST /crear-caja (soloOrden=true) → {id de caja}
  GET /generar-qr (codigoCaja) → {qrCode} → guardar imagen del QR (nunca cambia)

POR CADA COBRO:
  1. Entidad crea orden de venta: POST /orden-de-venta (codigoCaja + monto)
  2. Usuario escanea el QR con su billetera
     → Billetera muestra el monto fijo de la orden pendiente
  3. Usuario confirma el pago
  4. Red procesa → cobro acreditado
  5. EVENT "aviso.transaccion.qr.estatico" → webhook a la entidad
```

## Flujo — QR estático de monto abierto

```
SETUP (una sola vez):
  POST /crear-caja (soloOrden=false) → {id de caja}
  GET /generar-qr (codigoCaja) → {qrCode} → guardar imagen del QR

POR CADA COBRO:
  1. Usuario escanea el QR con su billetera
     → Billetera solicita al usuario que ingrese el monto a pagar
  2. Usuario ingresa monto y confirma
  3. Red procesa → cobro acreditado
  4. EVENT "aviso.transaccion.qr.estatico" → webhook a la entidad
```

## Flujo — Intento de cobro con monto cerrado sin orden de venta

```
  caja tiene soloOrden=true pero NO hay orden de venta pendiente
  → Usuario escanea el QR con su billetera
  → Billetera muestra ERROR: no se puede pagar (sin orden disponible)
  → El pago es bloqueado; no se genera transacción
```

## API Reference de este módulo

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | Generar código QR | Genera el string del QR estático de la caja |
| POST | Crear orden de venta | Crea una orden de venta con monto fijo en la caja |
| DELETE | Eliminar orden de venta | Elimina una orden de venta existente |
| GET | Consultar orden de venta por id | Consulta una orden de venta por su ID interno |
| GET | Consultar orden de venta por código externo | Consulta órdenes de venta por código externo |
| POST | Crear devolución QR | Instruye un contracargo de un pago QR |
| GET | Consultar devolución | Consulta el estado de un contracargo |
| EVENT | Aviso de transacción QR estático | Webhook de notificación de pago acreditado/rechazado |
| EVENT | Aviso de devolución QR estático | Webhook de notificación de contracargo |
