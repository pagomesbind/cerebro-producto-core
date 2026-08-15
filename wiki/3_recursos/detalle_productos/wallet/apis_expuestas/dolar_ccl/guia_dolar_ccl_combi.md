# Guía — ¿Cómo integrar dolar CCL combi?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-dolarcclcombi
> Producto: Wallet — Dolar CCL

## Descripción

Esta solución permite comprar dolares utilizando pesos argentinos colectados mediante un CVU propio, así como también vender dolares por pesos argentinos que se acreditan en el mismo CVU.

La operatoria de compra de dolar CCL implica la compra de bonos argentino en pesos y luego venderlos en dolares. Este mecanismo sólo puede realizarlo una ALYC autorizada, quien luego debe disponibilizar estos dolares resultantes en una cuenta en el exterior. Es por eso que nuestro sistema no registra los saldos en dolares de cada cuenta ya que no podemos controlar el final de los fondos al ser estos enviados a una cuenta en el exterior de cualquier entidad financiera externa.

En el modelo Combi de dolar CCL, cualquier operación de compra o venta puede ejecutarse en cualquier momento, incluso fuera de horario de mercado. Ya que por más que finalmente igual dependa de la compra y venta de bonos argentinos que debe realizarse en horario de mercado, el procesador guarda el mecanismo para asegurar la operatoria en cualquier momento.

También, en este modelo, el procesador asegura un precio de cotización por unos minutos. Esto se materializa en la integración con un hash asociado a la cotización.

Por ello cuando una operación se encuentre en proceso la entidad ya podrá confirmar que la misma se completará con el precio de cotización fijado. Y es por eso que en este modelo el **vuelto es nulo**, comparado con el modelo Standard.

## Gestión del saldo del CVU

- **Compra:** Al confirmarse el inicio de procesamiento, debita el saldo de pesos por la comisión de compra y luego debita el saldo de pesos necesario para comprar los dolares. En caso de que por cualquier motivo la compra no pueda completarse, se acreditan ambos conceptos nuevamente como reversa.
- **Venta:** Al confirmarse que se completó una operación de venta, acredita el saldo de pesos por el valor obtenido por vender los dolares.

Antes de iniciarse cualquier operación, se evalúa la misma en un sistema de monitoreo transaccional que puede disparar una alerta o restringirla por prevención de fraude.

> Con este modelo se puede operar 24/7 y con un precio de cotización fijado.
> Asegurate de elegir el mejor modelo para tu caso de uso. La configuración del modelo en la organización lo parametriza Bind PSP.

## Flujo de compra de dólar CCL — Combi completada

```
1. GET CotizacionCCL → buyPrice + hash + priceLimitTime (ventana de precio garantizado)
2. GET ConsultarDDJJ → aceptar declaración jurada
3. POST IntencionCompraCCL (monto en ARS, priceHash) → estado PENDIENTE
   → devuelve vueltoEstimado=0 (precio fijo), montoAObtener (USD)
4. POST EjecutarCompraDolarCCL (ddjjAceptada=true + ddjjAceptadaFechaHora + hash)
   → estado EN_PROCESO (procesador reserva el precio; puede operar fuera de horario)
5. EVENT "COMPRA_DOLAR_CCL" → IntencionEstado=APROBADA
6. [Opcional] GET Intencion → montoInvertido, montoObtenido, vuelto=0
```

**Diferencia clave vs Standard:** el hash fija la cotización por `priceLimitTimeInSeconds` segundos; mientras la operación esté EN_PROCESO, el precio ya está asegurado. El vuelto final es siempre 0.

## Flujo de venta de dólar CCL — Combi completada

```
1. GET CotizacionCCL → sellPrice + hash + priceLimitTime
2. GET ConsultarDDJJ → aceptar DDJJ
3. POST IntencionVentaCCL (monto en USD, priceHash) → estado PENDIENTE
   → devuelve montoAObtener en ARS (fijo)
4. POST EjecutarVentaDolarCCL (ddjjAceptada=true + ddjjAceptadaFechaHora + hash)
   → estado EN_PROCESO
5. EVENT "VENTA_DOLAR_CCL" → IntencionEstado=APROBADA
   → acredita ARS en CVU
```
