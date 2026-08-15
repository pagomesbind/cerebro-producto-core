# Guía — ¿Cómo funcionan los impuestos?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-impuestos-wallet
> Producto: Wallet — Impuestos

## Descripción

Por cada comprobante de debito o credito creado en una cuenta de la organización se calcula y se determina si se deben aplicar impuestos.

En caso de aplicar uno o más impuestos asociados al movimiento, el sistema crea nuevos comprobantes de débito por cada uno.

Estos comprobantes de impuestos se crean configurados para ser tomados en cuenta por un recycle. Esto implica que si al momento de crearlos no se pueden aplicar porque la cuenta no tenía el saldo suficiente, se reintentará su creación al momento en que la cuenta reciba un crédito. (Ver ¿Cómo funciona el recycle?)

Es posible configurar tipos de comprobante específicos de la organización para que no se tengan en cuenta para cálculo de impuestos. Esta configuración debe ser solicitada al equipo de soporte técnico de Bind PSP.

Los impuestos se analizan y calculan tanto para los comprobantes creados por la organización como para los comprobantes creados internamente por el sistema dentro del flujo de operaciones (como transferencia, pagos QR, dolar, etc).

## Flujo — Impuestos debitados en línea (cuenta con saldo)

```
1. Se crea cualquier comprobante (débito o crédito) en una cuenta
   → Sistema analiza si aplican impuestos al movimiento

2. Si aplican impuestos:
   → Sistema crea N comprobantes de DÉBITO (uno por cada impuesto)
   → Los fondos se descuentan inmediatamente del saldo de la cuenta
   → EVENT "impuesto.online" → webhook a la entidad por cada débito de impuesto
```

## Flujo — Impuestos no debitados en línea (cuenta sin saldo → recycle)

```
1. Se crea comprobante en cuenta → sistema detecta que aplican impuestos
   → Intenta crear comprobantes de débito de impuestos
   → La cuenta NO tiene saldo suficiente → débitos de impuesto no se aplican

2. Los comprobantes de impuesto quedan en RECYCLE (pendientes)

3. Cuando la cuenta recibe el próximo crédito (de cualquier origen):
   → Sistema de recycle intenta aplicar los débitos pendientes
   → Si hay saldo: debita el impuesto + EVENT "impuesto.online"
   → Si no hay saldo: sigue en recycle hasta el siguiente crédito

Nota: tipos de comprobante de la organización pueden excluirse del cálculo de impuestos
(solicitar a soporte técnico de Bind PSP).
```

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `EVENT` | Aviso de impuesto online | [endpoint_event_aviso_impuesto.md](endpoint_event_aviso_impuesto.md) |
