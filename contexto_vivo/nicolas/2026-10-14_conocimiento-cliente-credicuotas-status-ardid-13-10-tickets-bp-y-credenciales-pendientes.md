---
id: 2026-10-14_conocimiento-cliente-credicuotas-status-ardid-13-10-tickets-bp-y-credenciales-pendientes
pm: nicolas
fecha_captura: 2026-10-14
fuente: "Mail \"[Ardid - CC] Status y Next Steps\" (Rodrigo Novas, Credicuotas, 2026-10-13) + mail \"Re: Consultas integración\" (Juan I. Bigourdan, Credicuotas, 2026-10-14)"
producto: ardid
tema: Credicuotas — estado al 13/10 de los 7 frentes con Ardid (tickets BP), credenciales de Akurtech todavía sin entregar y pedido de fecha para el endpoint de pagos
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

**Qué completa.** Sigue a `2026-10-09_conocimiento-cliente-credicuotas-respuestas-pentass-blacklist-y-lista-15-pendiente` y a `2026-10-06_conocimiento-cliente-credicuotas-pedido-publicacion-apim-stg-y-minuta-consumo-datos`. Va a la cronología de la ficha de Credicuotas.

**Estado de los frentes con Ardid según Credicuotas** (repaso de la sync del martes 06/10, enviado el 13/10 antes de la sync de las 10hs):

| Frente | Ticket | Qué quiere Credicuotas | Estado que declara Credicuotas |
|---|---|---|---|
| Credenciales para login, onboarding y pagos | BP-52914 | Credenciales de Akurtech para integrar esos eventos a Ardid y aplicarles reglas | Pendiente |
| Changelog y fechas de versiones de Ardid | — | Recibir el detalle y la fecha de cada versión nueva para anticipar los cambios (acordado en la sync) | Pendiente |
| Consumo de datos de Ardid vía API | BP-52939 | Obtener el 100% de transacciones y alertas por API y dejar de descargarlas a mano | Pendiente: faltan exponer los endpoints |
| Segmentos de clientes con préstamo | BP-53564 | Que quien recibe un préstamo no quede frenado por el tope de $1,5M. Hoy el cambio de segmento es manual y no escala | Ticket del endpoint cargado. Faltan los casos de uso de ejemplo (Samira Aouada, Pentass) y que se disponibilice el endpoint |
| IP e installation ID en las transacciones | BP-53565 | Ardid ya puede usar estos campos en las reglas, pero la API de Bind PSP todavía no los manda | Ticket cargado. Falta confirmar si incluye QR |
| Comprobantes internos | — | Mandar a Ardid los movimientos internos (préstamos, línea de crédito, pagos de servicios, recargas), que hoy no se pueden informar. Para Credicuotas es la solución de fondo de los segmentos | Bloqueado hasta la versión que los soporte, estimada para **fines de noviembre** |
| Transferencias aprobadas vs. rechazadas | — | Que las reglas de cantidad de Ardid distingan aprobadas de rechazadas (hoy no lo hacen) | Pendiente: falta definir la versión con Pentass |

Fulvio Vacca (Credicuotas) respondió "muy claro".

**Credenciales (BP-52914) al 14/10:** Juan I. Bigourdan pregunta si se generaron las credenciales, que según entendía se compartían "ayer" (13/10). Rocío Revelli había estimado el 01/10 que el producto nuevo del APIM quedaba publicado "antes del martes" (06/10). Además pide **fecha estimada para disponibilizar el endpoint de la API de pagos**. Es la misma pregunta que hizo Gonzalo Santos el 01/10 (¿entra la API de pagos en el APIM?), que sigue sin respuesta en el hilo.

**Bloqueo relacionado:** según Hernán Clarich (09/10), para salir con Credicuotas en STG antes hay que regularizar los paths de los endpoints de Ardid en el APIM de STG. Ver `2026-10-14_conocimiento-ardid-apim-stg-paths-distintos-a-prod-regularizar-antes-de-credicuotas`.

**Lectura PM:** "segmentos con préstamo" (BP-53564) es el mismo pedido del endpoint de consulta y cambio de segmento (T-097 y oportunidad del 2026-10-02). Credicuotas lo plantea como parche hasta que existan los comprobantes internos. En "IP e installation ID" queda abierta la duda de si los pagos QR mandan esos campos.

> Fuente: Mail "[Ardid - CC] Status y Next Steps" — Rodrigo Novas (2026-10-13); Mail "Re: Consultas integración" — Juan I. Bigourdan (2026-10-14).
