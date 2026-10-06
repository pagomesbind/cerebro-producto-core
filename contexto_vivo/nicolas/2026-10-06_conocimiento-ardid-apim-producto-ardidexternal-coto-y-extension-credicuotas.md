---
id: 2026-10-06_conocimiento-ardid-apim-producto-ardidexternal-coto-y-extension-credicuotas
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Mail 'Fwd: Publicación en APIM STG nuevo producto referencia cliente Credicuotas !!!!' — Hernán Clarich a Daniel Zalazar (Fintexa), 2026-10-05, reenviado por Mariana Nadalin"
producto: ardid
tema: Exposición de APIs de Ardid a clientes vía el APIM de Bind — producto ARDIDEXTERNAL (COTO) y su extensión para Credicuotas
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/apis_externas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

**Cómo se exponen hoy las APIs de Ardid a clientes.** Bind PSP publica las APIs de Ardid (Akurtech) a clientes que se integran directo al motor antifraude mediante un **producto del API Management (APIM)**. El producto existente se llama **ARDIDEXTERNAL** y lo usa **COTO**.

**Extensión para Credicuotas (pedido del 2026-10-05).** Credicuotas va a integrarse directo a Ardid para funcionalidades que hoy no están publicadas. Hernán Clarich pidió a Fintexa (Daniel Zalazar) publicar en el APIM de **STG** estas APIs (numeración de la documentación de Ardid):

| Módulo | API |
|---|---|
| Blacklist | `/api/Blacklist/CheckBlacklist` |
| Login | 12.e / Login |
| Pagos con TD | 17.a / Transaction · 17.b / NotRealized |
| Préstamos | 16 API / Loans · 16.a / GetLoanById |

**Cómo se trabaja el pedido:**
- El ticket de referencia está en el service desk de Fintexa: **SI-950**.
- Antes de publicar hay que identificar **qué endpoint de backend de Ardid** corresponde a cada API. Para eso se pidió ayuda a **Pentass** el 01/10. O sea: la numeración de la documentación de Ardid no alcanza para saber qué publicar en el APIM.
- El mail habla de "agregar nuevas APIs" al producto que usa COTO y, en el asunto, de un "nuevo producto". El 01/10 Rocío Revelli había hablado de un producto nuevo en el APIM. **No está claro** si Credicuotas va a tener un producto propio o si se amplía ARDIDEXTERNAL. El merge debería documentarlo como "a confirmar".

> Fuente: Mail "Fwd: Publicación en APIM STG nuevo producto referencia cliente Credicuotas !!!!" — Hernán Clarich / Mariana Nadalin (2026-10-05).
