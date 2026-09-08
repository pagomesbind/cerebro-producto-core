# Interoperabilidad QR — Getnet (Bind Pago como socio/APM)

> Estado: en desarrollo (Fintexa), deadline interno 30/09/2026. Ver riesgo asociado en [2_areas/riesgos.md](../../../2_areas/riesgos.md) y el proyecto de producto relacionado `1_proyectos/getnet_oauth2_resolve/` (Pablo Gomes) — ambos referencian el mismo proveedor (Getnet) y ventana de tiempo; **no confirmado todavía si son la misma migración de fondo vista desde dos puntas** (este documento cubre el lado billetera/pagador — Bind Pago como socio/APM dentro de la red interoperable de Getnet; el proyecto de Pablo Gomes cubre la autenticación de la API Resolve que usa Wallet para leer/pagar QR de comercios Getnet — ver nota al final).

## Contexto

Getnet (`productoqr@getnet.com.ar`, Luisana Noguera) documentó el circuito nuevo por el que la Billetera Bind Pago debe operar como socio/APM (medio de pago alternativo) dentro de su red interoperable de QR, en reemplazo del circuito viejo a deprecar.

**Antecedente:** Getnet detectó que Bind Pago ya había hecho una homologación técnica el 17/04/2026, pero según Alan Martínez (área técnica Bind) esa fecha correspondió únicamente a pruebas manuales por Postman (autenticación + validación de interpretación del QR) — nunca hubo integración sistémica real en backend. Al 2026-09-05, Fintexa (Agustín Grau) indica que ya existía análisis y diseño previo del lado de Bind, y levantó el ticket de desarrollo para Nico Pomponio.

## Condiciones previas

- Credencial de socio para acceso (`client_id`/`client_secret`, provistas previamente por Getnet, app registrada como `"Wallet - APM"`).
- Comunicación entre la billetera y la plataforma basada en el archivo de especificación `Interoperabilidad v6 BCRA.yaml`.

## Endpoints permitidos para el acceso externo del socio

- `GET /resolve`
- `PATCH /orders/{order_id}/plans`
- `POST /orders/{order_id}/payments`
- `GET /payments/{payment_id}`
- `POST /payments/tokens`

## Flujo de autenticación (ambiente de Homologación)

1. Antes de cualquier request a la API, debe asociarse una nueva URL externa para la conexión con la interfaz (asegurada por JWT temporal).
2. Se cargan las credenciales (`client_id`/`client_secret`) de la app `"Wallet - APM"`.
3. Se llama a `POST https://api.globalgetnet.com/authentication/oauth2/access_token` con esas credenciales.
4. Getnet devuelve un JWT, que se agrega como bearer token en el header de autorización de cada request posterior.
5. El token dura **1 hora en Homologación**; vencido, hay que generar uno nuevo.
6. Con el JWT vigente, ya se puede operar contra las rutas externas del nuevo circuito:
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/resolve`
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/orders/{order_id}/plans`
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/orders/{order_id}/payments`
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/payments/{payment_id}`
   - `https://api.globalgetnet.com/apm/payment-interoperable/v1/payments/tokens`
7. Con esas rutas resueltas, se realiza la operación de pago por medio del QR.

## Nota — posible superposición con `getnet_oauth2_resolve/`

El proyecto de producto `1_proyectos/getnet_oauth2_resolve/` (Pablo Gomes, IDEA PRD-237) documenta que Getnet migró la autenticación de su API **Resolve** de un `access_token` fijo a **OAuth2 `client_credentials`** — mismo mecanismo de autenticación, mismo dominio (`api.globalgetnet.com`), mismo endpoint `/resolve`, y mismo deadline (30/09/2026) que este documento. No está confirmado si ambos describen la misma migración de fondo (Bind Wallet como pagador, resolviendo/pagando QR de comercios afiliados a Getnet) vista desde dos fuentes — el mail técnico de Getnet a Integraciones (este documento) y el proyecto formal de PM (Jira) — o si son dos alcances técnicos distintos que coinciden en proveedor y ventana de tiempo. Pendiente de confirmación por los PM involucrados (Pablo Gomes / Nicolás Colón).

> Fuente: Mail "Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago", mensajes de Luisana Noguera (Getnet) del 2026-09-01 y 2026-09-02, reenviados internamente el 2026-09-03/04. Capturado por Nicolás Colón, 2026-09-06.
