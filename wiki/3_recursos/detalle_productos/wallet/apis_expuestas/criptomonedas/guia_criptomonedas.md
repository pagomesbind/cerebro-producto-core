# Guía — ¿Cómo comprar y vender cripto?

> Fuente: https://psp.bind.com.ar/developers/apis/guia-operarcripto
> Producto: Wallet — Cripto

## Descripción

Esta solución permite comprar o vender distintas criptomonedas. Las operaciones de criptomonedas se gestionan desde una cuenta cripto asociada a cada cuenta de la billetera.

Al concretarse una operación de compra de criptomonedas, las mismas se acreditan al saldo de la cuenta cripto y debita saldo de la moneda FIAT de la cuenta de la billetera asociada.

Al concretarse una operación de venta de criptomonedas, las mismas se debitan del saldo de la cuenta cripto y acredita saldo de la moneda FIAT de la cuenta de la billetera asociada.

Para operar con criptomonedas, la cuenta utilizada debe tener asociada una cuenta cripto activa. La misma puede ser creada junto con la creación de la cuenta de la billetera o en un momento diferente.

## Flujo de compra de criptomonedas

```
1. [Opcional] GET CotizacionCripto → obtener ask (precio compra en ARS por unidad)
2. POST IntencionCompraCripto → intencionId + requiereCodigoConfirmacion
   - Especificar montoCripto O montoCambio (ARS), no ambos
   - Combi: incluir priceHash de la cotización para fijar precio
3. [Si requiereCodigoConfirmacion=true] → usuario ingresa código recibido
4. POST EjecutarCompraCripto (intencionId + codigoConfirmacion si aplica)
   → estado: EN_PROCESO → APROBADA o RECHAZADA
5. EVENT "COMPRA_CRIPTO" cuando hay resolución definitiva (webhook)
6. [Opcional] GET IntencionCripto para verificar estado y comprobantes
```

Al aprobarse: débito ARS (debitoComprobanteId) + crédito cripto + débito comisión (cargoComprobanteId).

## Flujo de venta de criptomonedas

```
1. [Opcional] GET CotizacionCripto → obtener bid (precio venta en ARS por unidad)
2. POST IntencionVentaCripto → intencionId + requiereCodigoConfirmacion
3. [Si requiereCodigoConfirmacion=true] → usuario ingresa código
4. POST EjecutarVentaCripto (intencionId + codigoConfirmacion si aplica)
   → estado: EN_PROCESO → APROBADA o RECHAZADA
5. EVENT "VENTA_CRIPTO" cuando hay resolución definitiva (webhook)
6. [Opcional] GET IntencionCripto para verificar
```

Al aprobarse: débito cripto + crédito ARS (comprobanteId) + débito comisión (cargoComprobanteId).

**Nota sobre horario:** GET ConsultarCotizacionCripto devuelve `horarioMercado` bool. Las operaciones fuera de horario pueden quedar en estado pendiente hasta que el mercado abra.

## Endpoints del módulo

| Tipo | Descripción | Archivo |
|------|-------------|---------|
| `GET` | Consultar operación por ID | [endpoint_get_consultar_operacion_id_cripto.md](endpoint_get_consultar_operacion_id_cripto.md) |
| `GET` | Consultar operación por ID externo | [endpoint_get_consultar_operacion_id_externo_cripto.md](endpoint_get_consultar_operacion_id_externo_cripto.md) |
| `GET` | Consultar saldo cripto | [endpoint_get_consultar_saldo_cripto.md](endpoint_get_consultar_saldo_cripto.md) |
| `GET` | Consultar cotización de cripto | [endpoint_get_consultar_cotizacion_cripto.md](endpoint_get_consultar_cotizacion_cripto.md) |
| `POST` | Crear intención de compra cripto | [endpoint_post_crear_intencion_compra_cripto.md](endpoint_post_crear_intencion_compra_cripto.md) |
| `POST` | Ejecutar compra cripto | [endpoint_post_ejecutar_compra_cripto.md](endpoint_post_ejecutar_compra_cripto.md) |
| `POST` | Crear intención de venta cripto | [endpoint_post_crear_intencion_venta_cripto.md](endpoint_post_crear_intencion_venta_cripto.md) |
| `POST` | Ejecutar venta cripto | [endpoint_post_ejecutar_venta_cripto.md](endpoint_post_ejecutar_venta_cripto.md) |
| `GET` | Consultar intención cripto | [endpoint_get_consultar_intencion_cripto.md](endpoint_get_consultar_intencion_cripto.md) |
| `EVENT` | Aviso cripto | [endpoint_event_aviso_cripto.md](endpoint_event_aviso_cripto.md) |
