---
id: 2026-09-24_direccion_oportunidad_inter_cash_in_usd_bind_inversiones
pm: pablo
fecha_captura: 2026-09-24
fuente: "/sync_mails — mail 'Fwd: Inter | Cash-IN en USD', Gastón Degiovanni (BIND Inversiones) → Pablo Gomes/Emma Vignoles, 2026-09-23 (threadId 1a0ce72ce203b943; reenvío de un mail original de Degiovanni a Emma Vignoles del 2026-08-27)"
producto: transversal
tema: propuesta de BIND Inversiones para que INTER ofrezca Cash-IN en USD (conversión MEP→CCL) usando infraestructura de cuenta comitente de BIND Inversiones
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
---

## Origen

Gastón Degiovanni (Líder de Negocios Digitales, BIND Inversiones) comparte con Pablo Gomes y Emma Vignoles un PRD y un flujo (Google Docs, no descargados — solo el resumen en el cuerpo del mail) para que **INTER AR** pueda ofrecer a sus usuarios el ingreso de dólares (Cash-IN USD) usando la infraestructura de BIND Inversiones para la conversión MEP→CCL ("dólar cable"). El pedido original es de Josefina (Inter), reenviado por Degiovanni a Emma Vignoles el 2026-08-27 y ahora reenviado a Pablo el 2026-09-23. Pablo respondió solo "Recibido. Lo analizamos y te comento." — sin análisis de producto todavía, es una propuesta recién llegada a la mesa de Pablo.

## Propuesta (resumen del flujo compartido)

**Objetivo:** permitir que los usuarios de INTER AR ingresen USD desde cualquier banco y los envíen a su cuenta de INTER US (o los conserven en INTER AR, o los devuelvan a una cuenta a su nombre), usando la infraestructura de BIND Inversiones. Mismo titular en cash-in y cash-out (same-name).

**Flujo a alto nivel:**
1. El usuario inicia la operación en la app de Inter AR: copia el alias de una subcuenta dedicada a Inter USD (ej. `Inter.USD.IVSA`).
2. Al ingresar los USD, Inter recibe un webhook para mostrarle al usuario un push notification ("Recibiste USD 5.000").
3. El usuario puede custodiar los USD en su cuenta comitente, enviarlos a su cuenta de Inter US (MEP→CCL) o devolverlos a una cuenta bancaria en USD de su misma titularidad.
4. El envío a Inter USD arranca en dólar MEP para resultar en dólar cable (CCL).

**Productos/integraciones nuevas que requeriría para Inter:**
1. Fondeo de cuenta recaudadora en USD (provista por BIND Inversiones, alias dedicado).
2. Integración de webhook de cash-in USD (notifica la acreditación para disparar el push al usuario).
3. Integración de API de consulta de saldos (USD en recaudadora/comitente).
4. Integración de API de validación de CBU (para validar la cuenta destino antes de la transferencia saliente en USD).
5. Variante de API "Operar D1C" — soporte de la operación AL30D/AL30C y viceversa.
6. Instrucción de transferencias salientes — desde BIND Inversiones a la CBU USD del usuario.

## Por qué es una oportunidad, no un proyecto todavía

- No tiene IDEA en Jira ni discovery iniciado — es una propuesta técnica ya armada por BIND Inversiones (no por Bind PSP/Producto) a partir de un pedido de Inter, que recién ahora llega formalmente a la mesa del PM de Wallet/Adquirencia.
- **Relación con otros proyectos INTER activos:** distinto del riesgo `2026-09-23_transversal_riesgo_fraude_inter_seguridad_informatica` (seguridad/fraude del lanzamiento) y del riesgo `2026-09-23_wallet_riesgo_combi_spread_viabilidad_comercial` (producto Dólar COMBI vía Mastercard Move/PagosFX, de Luciana Rudaz) — este Cash-IN USD es un mecanismo distinto (MEP↔CCL vía BIND Inversiones/cuenta comitente), no una variante del Combi. A confirmar con el PM si hay solapamiento de negocio/canibalización entre ambas iniciativas de dólares para Inter.
- Requiere evaluación de producto (discovery) antes de convertirse en candidata seria: no está claro el driver de negocio para Bind PSP (vs. BIND Inversiones, que es quien arma la propuesta), ni el esfuerzo de las 6 integraciones nuevas listadas arriba.
