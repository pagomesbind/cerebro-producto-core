# Guía — Pago QR (Wallet)

> Fuente: https://psp.bind.com.ar/developers/apis/guia-pago-qr
> Producto: Wallet — Pago QR

## ¿Cómo integrar pago QR?

Esta solución permite leer cualquier QR interoperable de Argentina. Si el QR es válido puede iniciarse un pago.

El sistema resuelve la gestión del saldo del CVU. No se iniciará la operación si la cuenta no tiene saldo suficiente. Antes de procesar el pago se debita el saldo necesario para cursarla y, en caso de que la transferencia haya resultado errónea, se devuelve el saldo en concepto de reversa.

También, antes de iniciar el pago, se evalúa el mismo en un sistema de monitoreo transaccional que puede desaprobarlo según restricciones por prevención de fraude.

Al ejecutar la lectura de un QR, si pertenece a un Aceptador aprobado por el BCRA (ver Aceptadores del registro de proveedores de pagos del BCRA), el sistema consulta a esta entidad externa la información del QR. El estado en la lectura del QR es el indicado por el Aceptador.

El comercio dueño del QR tiene la habilidad de iniciar una devolución parcial o total de un pago. En tal caso, el sistema acredita el saldo devuelto a la cuenta del usuario pagador.

La respuesta de la lectura de un QR es la que devuelve el Aceptador y es standard según la normativa de Transferencia 3.0. Por eso, si la respuesta de la lectura del QR tiene un status diferente a "open_amount", "closed_amount" o "pending", o su estructura es diferente a la documentada, es posible que el QR que se intenta leer no es interoperable o existe un problema del lado del comercio.

## Flujo — QR de monto abierto, pago aprobado

```
1. App del pagador escanea QR (código interoperable)
2. GET /qr → Bind PSP consulta al Aceptador (BCRA) la info del QR
   → status="open_amount" → el monto lo ingresa el usuario
   → status="closed_amount" → el monto está fijado por el comercio
   → status="pending" → QR sin orden disponible todavía

3. Si status="open_amount":
   → App muestra campo para que el usuario ingrese el monto

4. Sistema evalúa monitoreo transaccional (anti-fraude)
   → Si rechazado: error, no se debita

5. POST /pagar (monto + datos del QR)
   → Bind PSP DEBITA saldo del CVU del pagador
   → Acredita en cuenta del comercio vía Aceptador
   → Respuesta: COMPLETED

6. EVENT "pago.qr" → webhook a la entidad con resultado

DEVOLUCIÓN (iniciada por el comercio):
  → Comercio solicita devolución parcial o total a su Aceptador
  → Aceptador notifica a Bind PSP
  → Bind PSP ACREDITA saldo al CVU del pagador
  → EVENT "devolucion.qr" → webhook a la entidad
```

## Flujo — QR de monto cerrado, pago rechazado

```
1. GET /qr → status="closed_amount" (o "pending" = sin orden disponible)
2. POST /pagar
   → Monitoreo transaccional rechaza (fraude) → error, sin débito
   ó
   → Aceptador rechaza la transacción → error, sin débito
   ó
   → CVU sin saldo suficiente → error, no se inicia

Si se debitó y la red rechazó:
   → REVERSA automática → saldo devuelto al CVU pagador
```

## Endpoints

| Método | Operación | Archivo |
|--------|-----------|---------|
| `GET` | Leer QR | endpoint_get_leer_qr.md |
| `POST` | Pagar QR interoperable | endpoint_post_pagar_qr.md |
| `GET` | Consultar operación por ID | endpoint_get_consultar_operacion_id.md |
| `GET` | Consultar operación por ID externo | endpoint_get_consultar_operacion_id_ext.md |
| `EVENT` | Aviso de pago QR | endpoint_event_pago_qr.md |
| `EVENT` | Aviso de devolución de pago QR | endpoint_event_devolucion_qr.md |
