# Guía — ¿Cómo integrar dolar CCL standard?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-dolarcclstandard
> Producto: Wallet — Dolar CCL

## Descripción

Esta solución permite comprar dolares utilizando pesos argentinos colectados mediante un CVU propio, así como también vender dolares por pesos argentinos que se acreditan en el mismo CVU.

La operatoria de compra de dolar CCL implica la compra de bonos argentino en pesos y luego venderlos en dolares. Este mecanismo sólo puede realizarlo una ALYC autorizada, quien luego debe disponibilizar estos dolares resultantes en una cuenta en el exterior. Es por eso que nuestro sistema no registra los saldos en dolares de cada cuenta ya que no podemos controlar el final de los fondos al ser estos enviados a una cuenta en el exterior de cualquier entidad financiera externa.

En el modelo Standard de dolar CCL, solo se pueden ejecutar operaciones durante horarios en que el mercado argentino se encuentra abierto. Cada operación ingresada se ejecuta al precio de mercado disponible en ese instante, es decir, que no se puede asegurar un precio de cotización ya que dependerá de la variabilidad del mercado.

Al iniciar una operación de compra, el procesador ejecuta la compra del bono en pesos en el mercado al precio más bajo que se encuentre en ese momento. Luego de ello, ejecutará la venta del bono en dolares para finalmente disponerlos en la cuenta en el exterior correspondiente. Los tiempos para la resolución definitiva de una operación dependerán del parking obligatorio dispuesto por la normativa vigente en el país.

Tanto el precio de compra como el de venta del bono dependerá del más conveniente (el menor para la compra y el mayor para la venta) ofrecido en el mercado exactamente en el momento de la ejecución. Es por ello que no se puede asegurar una cotización y resultado exacto antes.

Por este motivo en las operaciones existe el **vuelto**. Ya que se intenta operar el monto indicado por el usuario pero, al no poder ejecutar el monto exacto, se opera un monto menor. Ya que de fondo la operatoria de dolar consiste en la compra y venta de bonos de precios variables y generalmente el monto que quiere operar el usuario no es multiplo exacto de ellos.

## Gestión del saldo del CVU

- **Compra:** Al confirmarse el inicio de procesamiento, debita el saldo de pesos por la comisión de compra y luego debita el saldo de pesos necesario para comprar los dolares. En caso de que por cualquier motivo la compra no pueda completarse, se acreditan ambos conceptos nuevamente como reversa.
- **Venta:** Al confirmarse que se completó una operación de venta, acredita el saldo de pesos por el valor obtenido por vender los dolares.

Antes de iniciarse cualquier operación, se evalúa la misma en un sistema de monitoreo transaccional que puede disparar una alerta o restringirla por prevención de fraude.

> Con este modelo sólo se puede operar en horarios de mercado y no se puede fijar la cotización.
> Asegurate de elegir el mejor modelo para tu caso de uso. La configuración del modelo en la organización lo parametriza Bind PSP.

## Flujo de compra de dólar CCL — Standard completada

```
1. GET ConsultarHorarioMercado → verificar que mercado esté abierto (T0)
2. GET CotizacionCCL → buyPrice (sin hash en Standard)
3. GET ConsultarDDJJ → aceptar declaración jurada (graba versión en la intención)
4. POST IntencionCompraCCL (monto en ARS) → estado PENDIENTE
   → devuelve vueltoEstimado, montoAObtener (USD), precioDolar
5. POST EjecutarCompraDolarCCL (ddjjAceptada=true + ddjjAceptadaFechaHora)
   → estado EN_PROCESO → COMPLETADA_PARCIAL (compra del bono ARS completada)
6. EVENT "COMPRA_DOLAR_CCL" → IntencionEstado=APROBADA (venta del bono en USD completada)
7. [Opcional] GET Intencion → montoInvertido, montoObtenido, vuelto final
```

**Nota sobre el vuelto:** El monto operado puede ser menor al solicitado porque los bonos tienen precios variables y el monto del usuario generalmente no es múltiplo exacto de ellos.

## Flujo de compra de dólar CCL — Standard con error en procesamiento

```
1-4. Igual al flujo exitoso
5. POST EjecutarCompraDolarCCL → estado RECHAZADA
   → Reversa automática: saldo ARS devuelto (comisión + monto)
6. EVENT "COMPRA_DOLAR_CCL" → IntencionEstado=RECHAZADA
```

## Flujo de venta de dólar CCL — Standard completada

```
1. GET ConsultarHorarioMercado → verificar mercado abierto
2. GET CotizacionCCL → sellPrice (sin hash)
3. GET ConsultarDDJJ → aceptar DDJJ
4. POST IntencionVentaCCL (monto en USD) → estado PENDIENTE
   → devuelve montoAObtener en ARS
5. POST EjecutarVentaDolarCCL (ddjjAceptada=true + ddjjAceptadaFechaHora)
   → estado EN_PROCESO → APROBADA
6. EVENT "VENTA_DOLAR_CCL" → IntencionEstado=APROBADA
   → acredita ARS en CVU
```

## Flujo de venta de dólar CCL — Standard con error en procesamiento

```
1-4. Igual al flujo exitoso
5. POST EjecutarVentaDolarCCL → estado RECHAZADA
6. EVENT "VENTA_DOLAR_CCL" → IntencionEstado=RECHAZADA
```

**Estado AUDITAR:** Si la intención queda en estado AUDITAR, el equipo de Bind realiza revisión manual en las próximas 48 horas hábiles.

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `GET` | Consultar operación por ID externo | [endpoint_get_consultar_operacion_id_externo.md](endpoint_get_consultar_operacion_id_externo.md) |
| `GET` | Consultar operación por ID | [endpoint_get_consultar_operacion_id.md](endpoint_get_consultar_operacion_id.md) |
| `GET` | Consultar horario de mercado | [endpoint_get_consultar_horario_mercado.md](endpoint_get_consultar_horario_mercado.md) |
| `GET` | Consultar DDJJ | [endpoint_get_consultar_ddjj.md](endpoint_get_consultar_ddjj.md) |
| `GET` | Consultar cotización de dolar | [endpoint_get_consultar_cotizacion.md](endpoint_get_consultar_cotizacion.md) |
| `POST` | Crear intención de compra dolar CCL | [endpoint_post_crear_intencion_compra.md](endpoint_post_crear_intencion_compra.md) |
| `POST` | Ejecutar una compra de dolar CCL | [endpoint_post_ejecutar_compra.md](endpoint_post_ejecutar_compra.md) |
| `POST` | Crear intención de venta dolar CCL | [endpoint_post_crear_intencion_venta.md](endpoint_post_crear_intencion_venta.md) |
| `POST` | Ejecutar una venta de dolar CCL | [endpoint_post_ejecutar_venta.md](endpoint_post_ejecutar_venta.md) |
| `GET` | Consultar intención | [endpoint_get_consultar_intencion.md](endpoint_get_consultar_intencion.md) |
| `EVENT` | Aviso de dolar CCL | [endpoint_event_aviso_dolar_ccl.md](endpoint_event_aviso_dolar_ccl.md) |

## Guías adicionales

- [Guía dolar CCL combi](guia_dolar_ccl_combi.md) — `guia-dolarcclcombi`
