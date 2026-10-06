---
id: 2026-10-06_conocimiento-cliente-credicuotas-pedido-publicacion-apim-stg-y-minuta-consumo-datos
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Mail 'Fwd: Publicación en APIM STG nuevo producto referencia cliente Credicuotas !!!!' (Hernán Clarich → Fintexa 2026-10-05, reenviado por Mariana Nadalin) y mail 'RE: Consumo de datos | Ardid Credicuotas' (Rocío Revelli 2026-10-05, Paula Lamarca/Pentass 2026-10-06)"
producto: ardid
tema: Credicuotas — pedido formal a Fintexa de publicar en el APIM de STG las APIs de Ardid que necesita, y minuta de la reunión de consumo de datos del 01/10
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Complementa la sección `## CREDICUOTAS` de `casos_de_uso_clientes.md` ("Particularidades / cronología"). Sigue al item `2026-10-02_conocimiento-cliente-credicuotas-producto-apim-credenciales-stg-y-pedido-endpoint-segmento` (capturado).

- **2026-10-05. Pedido formal de publicación en el APIM de STG.** Hernán Clarich le pidió a Daniel Zalazar (Fintexa) que publique en el APIM de STG las APIs de Ardid que Credicuotas necesita para **integrarse directo a Ardid**. Copiados: Pablo Vargas (Fintexa), Emma Vignoles, Mariana Nadalin, Rocío Revelli y Luis Mancilla (Pentass). Ticket de referencia en el portal de Fintexa: **SI-950**.
- **Base de la publicación.** Ya existe en el APIM un producto llamado **ARDIDEXTERNAL**, que usa COTO. Para Credicuotas hay que sumarle APIs nuevas:
  - Blacklist: `/api/Blacklist/CheckBlacklist`
  - Login: 12.e / Login
  - Pagos con TD: 17.a / Transaction y 17.b / NotRealized
  - Préstamos: 16 API / Loans y 16.a / GetLoanById
- **Falta identificar los endpoints de backend de Ardid.** El jueves 01/10 se le pidió ayuda a Pentass para determinarlos. Por eso el plazo que había dado Rocío Revelli ("antes del martes 06/10") queda en duda: al 05/10 el pedido recién llegaba a Fintexa.
- **Responde a medias la pregunta de Gonzalo Santos (01/10)** sobre si la "API de pagos" de las sesiones con Pentass entra en el producto del APIM: los endpoints de **pagos con TD (17.a/17.b) están en el pedido**.
- **2026-10-05. Credicuotas pide novedades sobre consumo de datos.** Rocío Revelli le pidió a Pentass la minuta de la reunión "Consumo de datos | Ardid Credicuotas" (01/10) porque Credicuotas reclamaba un update.
- **2026-10-06. Minuta de Pentass (Paula Lamarca).** Lo específico de Credicuotas: el área de **Fraudes** de Credicuotas necesita analizar operaciones y rechazos. Hoy solo los recibe por CSV, sin acceso directo a tablas. La salida propuesta es exponer esos datos con **APIs del back de Ardid**. Hay un ticket abierto para identificar el endpoint. Pentass propone una nueva reunión con **Lorena Macedo** (volvió de vacaciones) porque "se generaron dudas al retransmitirlo". Lo técnico de la minuta (vistas, ventanas de consulta e histórico) va en un item aparte: `2026-10-06_conocimiento-ardid-consumo-de-datos-vistas-ventana-45-dias-e-historico`.

**Lectura:** Credicuotas pasa a ser el segundo cliente que consume Ardid directo a través del APIM (después de COTO con ARDIDEXTERNAL), y el primero que pide datos de operaciones y rechazos para su propio equipo de fraude.

> Fuente: Mail "Fwd: Publicación en APIM STG nuevo producto referencia cliente Credicuotas !!!!" — Hernán Clarich / Mariana Nadalin (2026-10-05); Mail "RE: Consumo de datos | Ardid Credicuotas" — Rocío Revelli (2026-10-05), Paula Lamarca, Pentass (2026-10-06).
