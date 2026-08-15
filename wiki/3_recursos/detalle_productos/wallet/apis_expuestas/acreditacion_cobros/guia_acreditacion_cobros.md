# Guía — ¿Cómo interacciona cobros con wallet?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-cobrosenwallet
> Producto: Wallet — Acreditación de cobros

## Descripción

Esta integración debe considerarse para entidades que utilicen nuestro producto de Cobro y que a su vez las liquidaciones de cada comercio se realizan en un CVU de nuestro producto Wallet.

De esta manera, al momento de registrarse un cobro que tiene plazo de liquidación = 0 (es decir que se liquida y acredita en línea al comercio) se crean los comprobantes correspondientes en la cuenta asociada al comercio para que su saldo quede ajustado automáticamente según el importe neto de la transacción cobrada.

Se crean:

- Un comprobante de crédito en el mismo momento en que ocurre la transacción por el importe neto de comisiones.
- Se crea uno o más comprobantes de débito luego de que se liquida la transacción y se calculan los impuestos para debitar cada uno de los impuestos correspondientes a la transacción, si corresponden.

Por cada comprobante creado automáticamente por consecuencia de un cobro realizado, se envía un webhook de aviso a la entidad de tipo de evento `"COMPROBANTE_COBROQR"`.

## Flujo — Cobro en ecosistema cerrado (liquidación inmediata en CVU)

```
Pre-requisito: comercio tiene CVU de Wallet asociado + liquidación con plazo = 0

1. Comprador realiza un cobro (QR u otro método de la plataforma de Cobros)

2. Bind PSP registra la transacción → plazo de liquidación = 0
   → EN EL MISMO MOMENTO: crea COMPROBANTE DE CRÉDITO en la cuenta del comercio
     → Importe: monto bruto menos comisiones
     → EVENT "COMPROBANTE_COBROQR" → webhook a la entidad

3. Bind PSP calcula los impuestos aplicables a la transacción
   → Crea uno o más COMPROBANTES DE DÉBITO (uno por cada impuesto)
   → Por cada débito: EVENT "COMPROBANTE_COBROQR" → webhook a la entidad

Resultado neto:
  Saldo del CVU del comercio += (monto cobrado) - (comisiones) - (impuestos)
```

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `EVENT` | Aviso de cobro liquidado en cuenta | [endpoint_event_comprobante_cobro_qr.md](endpoint_event_comprobante_cobro_qr.md) |
