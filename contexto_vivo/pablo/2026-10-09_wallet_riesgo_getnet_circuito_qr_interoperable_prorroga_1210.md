---
id: 2026-10-09_wallet_riesgo_getnet_circuito_qr_interoperable_prorroga_1210
pm: pablo
fecha_captura: 2026-10-09
fuente: "/sync_mails — hilo 'Re: Re: Re: Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago' (threadId 1a0d4bb12a65e784), Alan Martínez / Getnet (Luisana Noguera), 2026-09-24 a 2026-10-08"
producto: wallet
tema: Migración del circuito QR interoperable de Getnet para Billetera Bind Pago — deprecación del circuito antiguo prorrogada a 12/10/2026, preguntas técnicas sin responder sobre qué dominios inversos mantener
tipo: riesgo
destino_propuesto: 3_recursos/detalle_productos/wallet/integraciones_qr_interoperable.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Importante — no confundir con la migración de la API Resolve de Getnet a OAuth2.0** (proyecto `getnet_oauth2_resolve/`, PRD-237, ya completado en producción el 08/10/2026). Este es un expediente distinto y más antiguo: la migración del circuito tecnológico de interoperabilidad QR para la Billetera Bind Pago, en curso desde abril 2026, con sucesivas prórrogas de la deprecación del circuito viejo pedidas por Bind (falta de desarrollo backend propio para el nuevo esquema).

**Estado al 08/10/2026:**
- Getnet otorgó una nueva prórroga: el circuito antiguo queda operativo hasta el 12/10/2026, fecha en la que se implementa definitivamente el nuevo circuito.
- Bind (Alan Martínez) preguntó explícitamente a Getnet, sin respuesta todavía al cierre de esta corrida:
  - En producción hay dos dominios inversos apuntando al IEP actual de Getnet: `ar.com.globalgetnet` y `com.geopagos`. Piden confirmar si `com.geopagos` corresponde a Getnet o a algún aceptador procesado por ellos — si no, lo dan de baja de su lado.
  - Con la puesta en producción del nuevo circuito del 12/10: qué dominios inversos hay que mantener, y desde qué fecha deja de estar disponible el IEP actual.

**Riesgo:** quedan 3 preguntas técnicas abiertas a días de un corte de circuito con fecha ya comprometida (12/10) — sin respuesta de Getnet, hay riesgo de que la billetera quede con configuración de dominios inversos inconsistente o pierda disponibilidad del circuito en el corte.

> Fuente: hilo "Re: Re: Re: Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago" (threadId `1a0d4bb12a65e784`), Alan Martínez (Bind PSP) / Luisana Noguera (Getnet), mensajes del 24/09 y 08/10/2026.

**Actualización 2026-10-09 (mismo hilo) — el circuito nuevo entró en producción antes de lo previsto, con un incidente menor resuelto el mismo día:**
- 09/10 13:13: Bind (Ana Moreno) confirma que **ese mismo día habilitaron en producción la nueva integración con Getnet para lectura de QR**, con token obtenido por OAuth2 `client_credentials` y credenciales productivas — es decir, el corte no esperó al 12/10, se adelantó.
- 09/10 16:55: Getnet (Luisana Noguera) responde que los primeros pagos de prueba fallaron porque Bind no estaba usando la URL correcta, y comparte las URLs correctas a usar.
- 09/10 17:42: Bind confirma que con la URL indicada **ya completaron en producción la lectura y el pago de un QR estático exitosamente** (ejemplo: operación del 09/10/2026).
- Las 3 preguntas técnicas que seguían abiertas al 08/10 (qué dominios inversos mantener, si `com.geopagos` sigue vigente, desde cuándo deja de estar disponible el IEP viejo) **no se cerraron explícitamente en este intercambio** — se resolvió el bloqueante operativo inmediato (URL incorrecta) pero no hay confirmación por escrito de Getnet sobre el resto.
- **Riesgo actualizado:** de "corte con preguntas sin responder a días de la fecha" pasa a "circuito nuevo ya operativo en producción, con un ajuste de URL ya resuelto"; el riesgo residual es menor pero las 3 preguntas de dominios inversos siguen técnicamente sin confirmación formal de Getnet.

> Fuente: mismo hilo (threadId `1a0d4bb12a65e784`), mensajes del 09/10/2026 (Ana Moreno — Bind, Luisana Noguera — Getnet).

**Actualización 2026-10-13 (mismo hilo) — avanza la prueba del QR dinámico, las 3 preguntas de dominios inversos siguen sin responder:**
- 09/10 (mensaje recuperado en esta corrida, parte del mismo hilo): tras el pago exitoso del QR estático, Bind (Ana Moreno) pide a Getnet un QR dinámico (con monto) para completar las pruebas — el dinámico que tenían ya se había usado en una prueba anterior.
- 13/10 12:26: Getnet (Luisana Noguera) provee un nuevo QR dinámico, sin otro comentario.
- Las 3 preguntas técnicas sobre dominios inversos (`com.geopagos`, qué mantener tras el corte, desde cuándo deja de estar disponible el IEP viejo) **siguen sin confirmación formal de Getnet** — no hubo referencia a ellas en este intercambio.

> Fuente: mismo hilo (threadId `1a0d4bb12a65e784`), mensaje del 13/10/2026 (Luisana Noguera — Getnet).
