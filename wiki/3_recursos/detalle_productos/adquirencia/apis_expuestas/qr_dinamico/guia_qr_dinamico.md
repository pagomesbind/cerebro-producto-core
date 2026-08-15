# Guía: QR Dinámico — Adquirencia

> Extraído el: 2026-06-30
> Fuente: https://psp.bind.com.ar/developers/apis/guia-deuda
> Producto: Adquirencia / Soluciones de Cobro

---

## Descripción

"Esta solución permite crear deudas con distintos montos y vencimientos que pasará a estado pagada al momento en que registre una nueva transacción de cobro asociado a la misma."

"Para cada una de ellas el sistema asociará un código QR que servirá para pagar unívocamente la deuda asociada."

"Una deuda se crea siempre en estado PENDIENTE para que luego recién el sistema de forma asincrónica cree sus medios de pago."

## Flujo — Cobro exitoso con QR dinámico (deuda única)

```
1. POST /deuda (monto + vencimiento + externalRefId + datos comercio/caja)
   → Deuda creada en estado PENDIENTE
   → Sistema genera el QR de forma ASINCRÓNICA (puede tardar unos segundos)

2. Polling: GET /deuda/{id} hasta que estado = PRE-CARGADO
   → Cuando PRE-CARGADO: la respuesta incluye los datos para generar la imagen del QR

3. Entidad renderiza el código QR y lo muestra al pagador (web/checkout/presencial)

4. Pagador escanea el QR con su billetera y paga
   → Bind PSP procesa el pago
   → Deuda pasa a estado PAGADA → QR queda bloqueado (no se puede volver a pagar)
   → EVENT "aviso.qr.deuda" → webhook a la entidad

CASOS ESPECIALES:
  - Si la deuda se elimina (DEL /deuda) → QR no puede pagarse
  - Si la deuda vence sin pagarse → QR no puede pagarse
  - El monto es siempre cerrado (no permite que el pagador modifique el monto)

DEVOLUCIÓN (posterior al cobro):
  POST /devolucion → devolución parcial o total
  GET /devolucion/{id} → consultar estado
  EVENT "aviso.devolucion.qr.din" → webhook cuando se procesa
```

## Características

- QR de un solo uso: cada deuda genera un QR que solo puede usarse una vez.
- Solo admite monto cerrado (closed amount).
- Caso de uso: pagos para web/checkout donde se requiere cobro puntual no recurrente.
- Procesamiento asincrónico de creación del QR.

## ⚠️ Notas y Advertencias del Portal

> "Si se registra una transacción acreditada en un QR de este tipo, la deuda asociada pasará a estado pagada. Entonces, el QR no podrá pagarse nuevamente."

> "Si la deuda se elimina o se expira, el QR asociado a ella no podrá pagarse."

> "Los QR creados bajo esta modalidad sólo admiten monto cerrado."

> "Una deuda se crea siempre en estado PENDIENTE para que luego recién el sistema de forma asincrónica cree sus medios de pago."

## Endpoints Disponibles

| Slug Real | Método | Operación |
|-----------|--------|-----------|
| `./deuda-crear` | POST | Crear una deuda |
| `./deuda-consultar` | GET | Consultar una deuda |
| `./deuda-eliminar` | DEL | Eliminar una deuda |
| `./qr-devolucion-copy` | POST | Crear devolución QR |
| `./consultarcontracargo-copy-copy` | GET | Consultar devolución |
| `./webhook-adqrdeuda` | EVENT | Aviso de transacción QR deuda |
| `./webhook-addevqrdin` | EVENT | Aviso de devolución QR dinámico |
