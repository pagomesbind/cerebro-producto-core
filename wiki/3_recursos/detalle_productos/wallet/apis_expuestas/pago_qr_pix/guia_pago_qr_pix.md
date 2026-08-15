# Guía — Pago QR PIX (Wallet)

> Fuente: https://psp.bind.com.ar/developers/apis/guia-pagospix
> Producto: Wallet — Pago QR PIX

## ¿Cómo integrar pagos PIX?

Esta solución permite pagar en un QR PIX con pesos argentinos.

En esta operación, el comercio dueño del QR PIX espera que le sea abonado un monto en Reales Brasileños. Entonces, esta solución se encarga de realizar de forma automática toda la operatoria cambiaria para permitir a la organización pagar en pesos argentinos sin ninguna fricción.

El sistema resuelve la gestión del saldo del CVU y al confirmar la operación registra el débito. En caso de ocurrir un error o rechazo que finalice en una operación fallida, el sistema registra el crédito correspondiente a la reversa del saldo.

Por cada operatoria concretada se debita de forma independiente el cargo por la comisión de cada transacción.

## Flujo — QR PIX monto cerrado

```
1. GET /cotizacion-brl → obtener cotización ARS/BRL del momento

2. POST /leer-qr-pix (código QR escaneado)
   → Bind PSP consulta al sistema PIX la orden de pago
   → Respuesta: monto en BRL fijado por el comercio, sin posibilidad de modificar

3. POST /pagar-qr-pix (monto en BRL + ID del QR leído)
   → Bind PSP calcula equivalente en ARS a la cotización vigente
   → Evalúa monitoreo transaccional (anti-fraude)
   → DEBITA ARS del CVU del pagador (monto + comisión por transacción)
   → Envía BRL al comercio vía red PIX Brasil
   → Respuesta: COMPLETED

4. EVENT "pago.pix" → webhook a la entidad con resultado

Si error/rechazo:
   → REVERSA automática: crédito al CVU pagador (sin la comisión si no llegó a procesarse)
   → EVENT con estado FAILED
```

## Flujo — QR PIX monto abierto

```
1. GET /cotizacion-brl → obtener cotización ARS/BRL del momento

2. POST /leer-qr-pix (código QR)
   → Respuesta: QR de monto abierto → usuario ingresa el monto en BRL

3. POST /pagar-qr-pix (monto en BRL elegido por usuario + ID del QR)
   → Bind PSP convierte BRL → ARS a cotización vigente
   → DEBITA ARS del CVU + comisión
   → Procesa pago en red PIX
   → EVENT "pago.pix" cuando se resuelve

DEVOLUCIÓN (iniciada por el comercio en Brasil):
   → Comercio solicita devol. a su entidad PIX → Bind PSP recibe notificación
   → Bind PSP ACREDITA ARS al CVU del pagador
   → EVENT "devolucion.pix" → webhook a la entidad
```

## Endpoints

| Método | Operación | Archivo |
|--------|-----------|---------|
| `GET` | Consultar cotización reales | endpoint_get_consultar_cotizacion_brl.md |
| `POST` | Leer QR PIX | endpoint_post_leer_qr_pix.md |
| `POST` | Pagar QR PIX | endpoint_post_pagar_qr_pix.md |
| `GET` | Consultar operación por ID | endpoint_get_consultar_operacion_id.md |
| `GET` | Consultar operación por ID externo | endpoint_get_consultar_operacion_id_ext.md |
| `EVENT` | Aviso de pago PIX | endpoint_event_pago_pix.md |
| `EVENT` | Aviso de devolución de pago PIX | endpoint_event_devolucion_pix.md |
