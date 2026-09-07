---
id: 2026-09-06_riesgo-getnet-deadline-30-09-billetera-circuito-interoperable
pm: nicolas
fecha_captura: 2026-09-06
fuente: "Mail \"IMPORTANTE! - Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago\" (hilo 2026-09-03 → 2026-09-05)"
producto: wallet
tema: Getnet deprecará el circuito viejo con el que opera hoy la Billetera Bind Pago como medio de pago (APM) dentro de su red QR interoperable — deadline confirmado 30/09, desarrollo recién arrancando con Fintexa
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Getnet (vía Luisana Noguera, `productoqr@getnet.com.ar`) viene reclamando desde el 2026-09-01 que la Billetera Bind Pago migre del circuito viejo al nuevo circuito tecnológico interoperable (especificación "Interoperabilidad v6 BCRA") para poder seguir operando como medio de pago (APM/socio) dentro de su red de QR — es decir, para que un usuario de la billetera pueda seguir pagando escaneando un QR de un comercio afiliado a Getnet. Según Getnet, Bind Pago ya completó una homologación técnica el 17/04 pero solo hizo pruebas manuales por Postman (confirmado por Alan Martínez, área técnica Bind); nunca hubo integración sistémica real, y el circuito viejo sigue en uso en producción.

**Postura de Getnet (reiterada varias veces, última el 03/09):** el circuito antiguo será deprecado "a finales de Q" y no habrá comunicaciones adicionales — no está dispuesta a mantenerlo indefinidamente pese a los pedidos explícitos de Bind (Alan Martínez) de conservarlo mientras se planifica el desarrollo.

**Escalamiento interno (03/09 → 04/09):** Gonzalo Rivera (Team Leader Integraciones y Soporte) alertó que "nos vamos a quedar sin operar con Getnet" y pidió ayuda para destrabar con Alan. Emma Vignoles pidió tomar el proyecto de inmediato y **confirmó una fecha límite dura: 30/09** ("nos bajan el riel que estamos usando... tenemos que llevarlo a Prod cuanto antes").

**Estado del desarrollo al 2026-09-05:** Agustín Grau (CTO Fintexa) tomó el frente diciendo que ya existía análisis y diseño previo hecho por Fintexa, pendiente de revisión — y el 05/09 confirmó que **ya levantó el ticket de análisis y se lo pasó a Nico Pomponio** (desarrollador Fintexa). No hay todavía fecha de entrega estimada ni confirmación de que el desarrollo (análisis → diseño → implementación → paso a producción) alcance a completarse antes del 30/09.

**Relación con otro riesgo Getnet ya capturado:** existe un item de riesgo separado del 2026-09-04 (`2026-09-04_riesgo-getnet-deprecacion-arquitectura-lectura-qr`, producto adquirencia) sobre el mismo proveedor deprecando arquitectura de sus **dispositivos POS** (provistos por Santander) del lado adquirente/lectura de QR — afectaría ~5% del volumen de QR que lee Bind. Este item nuevo es el **lado billetera/pagador** (Bind Pago como socio/APM de la red interoperable de Getnet): mismo proveedor y ventana de tiempo, pero rol e integración técnica distintos — no se debe fusionar sin confirmar si son o no la misma migración de fondo vista desde dos puntas.

**Sin mitigación ni plan de contingencia confirmado todavía** si el desarrollo no llega a tiempo — el hilo no menciona qué pasaría operativamente con los usuarios de Bind Pago si el circuito viejo se apaga el 30/09 sin el nuevo en producción.

> Fuente: Mail "IMPORTANTE! - Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago" y su hilo previo "Adecuación operativa al nuevo circuito tecnológico - Billetera Bind Pago" (mensajes del 2026-09-01 al 2026-09-05).
