---
id: 2026-09-06_wallet-especificacion-circuito-interoperable-qr-getnet
pm: nicolas
fecha_captura: 2026-09-06
fuente: "Mail \"Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago\" (Getnet → Bind, 2026-09-01/02)"
producto: wallet
tema: Especificación técnica del nuevo circuito interoperable QR de Getnet (Interoperabilidad v6 BCRA) que la Billetera Bind Pago debe integrar como socio/APM
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/interoperabilidad_qr_getnet.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

Getnet (`productoqr@getnet.com.ar`, Luisana Noguera) documentó el circuito nuevo por el que la Billetera Bind Pago debe operar como socio/APM (medio de pago alternativo) dentro de su red interoperable de QR, en reemplazo del circuito viejo a deprecar (ver riesgo asociado `2026-09-06_riesgo-getnet-deadline-30-09-billetera-circuito-interoperable`, deadline 30/09).

**Condiciones previas:**
- Credencial de socio para acceso (`client_id`/`client_secret`, provistas previamente por Getnet, app registrada como `"Wallet - APM"`).
- Comunicación entre la billetera y la plataforma basada en el archivo de especificación `Interoperabilidad v6 BCRA.yaml`.

**Endpoints permitidos para el acceso externo del socio:**
- `GET /resolve`
- `PATCH /orders/{order_id}/plans`
- `POST /orders/{order_id}/payments`
- `GET /payments/{payment_id}`
- `POST /payments/tokens`

**Flujo de autenticación (ambiente de Homologación):**
1. Antes de cualquier request a la API, debe asociarse una nueva URL externa para la conexión con la interfaz (asegurada por JWT temporal).
2. Se cargan las credenciales (`client_id`/`client_secret`) de la app `"Wallet - APM"`.
3. Se llama a `POST https://api.globalgetnet.com/authentication/oauth2/access_token` con esas credenciales.
4. Getnet devuelve un JWT, que se agrega como bearer token en el header de autorización de cada request posterior.
5. El token dura **1 hora en Homologación**; vencido, hay que generar uno nuevo (Getnet documentó el código de error de token caduco pero el mail no incluye el detalle textual, solo capturas de pantalla no legibles desde el cuerpo del mail).
6. Con el JWT vigente, ya se puede operar contra las rutas externas del nuevo circuito:
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/resolve`
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/orders/{order_id}/plans`
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/orders/{order_id}/payments`
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/payments/{payment_id}`
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/payments/tokens`
7. Con esas rutas resueltas, se realiza la operación de pago por medio del QR.

**Antecedente relevante:** Getnet detectó que Bind Pago ya había hecho una homologación técnica el **17/04/2026**, pero según Alan Martínez (área técnica Bind) esa fecha correspondió únicamente a pruebas manuales por Postman (autenticación + validación de interpretación del QR) para confirmar el flujo — nunca hubo integración sistémica real en backend. Al 2026-09-05, Fintexa (Agustín Grau) indica que ya existía análisis y diseño previo del lado de Bind, y levantó el ticket de desarrollo para Nico Pomponio.

> Fuente: Mail "Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago", mensajes de Luisana Noguera (Getnet) del 2026-09-01 y 2026-09-02, reenviados internamente el 2026-09-03/04.
