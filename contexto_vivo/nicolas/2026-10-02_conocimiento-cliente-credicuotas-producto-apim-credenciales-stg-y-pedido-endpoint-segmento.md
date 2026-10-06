---
id: 2026-10-02_conocimiento-cliente-credicuotas-producto-apim-credenciales-stg-y-pedido-endpoint-segmento
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Hilo de mail 'Consultas integración' — mensajes del 2026-09-30 (Juan Ignacio Bigourdan, Credicuotas), 2026-10-01 (Bigourdan; Rocío Revelli, Bind PSP; Gonzalo Santos, Credicuotas)"
producto: wallet
tema: Credicuotas — credenciales STG de Ardid vía un producto nuevo en el APIM (estimado antes del 06/10), pedido de un endpoint de consulta de segmento y pregunta por la API de pagos
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Complementa la sección `## CREDICUOTAS` de `casos_de_uso_clientes.md` (para "Particularidades / cronología"). Sigue la integración de Credicuotas con el motor antifraude Ardid/Akurtech (ticket BP-52914, cargado por Credicuotas el 25/09).

- **2026-09-30. Pedido nuevo, un endpoint de consulta de segmento.** Juan Ignacio Bigourdan (PM de Credicuotas) preguntó si Bind tiene un endpoint para **consultar el segmento de una cuenta**. Credicuotas quiere usar más segmentos para monitoreo y armar reglas específicas por segmento, pero hoy no puede leer ese dato. Nadie de Bind contestó esa pregunta en el hilo hasta el 01/10.
- **2026-10-01. Presión por la demora.** Bigourdan volvió a pedir novedades y una fecha para BP-52914 ("necesitamos avanzar con esto").
- **2026-10-01. Respuesta de Bind (Rocío Revelli).** La demora se debe a que se está **creando un producto nuevo en el API Management (APIM)** para el consumo de Credicuotas. Cuando se publique, se le asocian las credenciales de consumo y se informan los endpoints de STG. Estimación: **resuelto antes del martes 06/10**. Hernán Clarich hace el seguimiento.
- **2026-10-01. Pedido de alcance.** Gonzalo Santos (Head de Producto de Credicuotas) preguntó si la **API de pagos** de las sesiones con Pentass (Lorena Macedo) también va a entrar en ese producto del APIM. Sin respuesta todavía.

**Lectura:** es el primer caso en que un cliente pide consumir APIs de Ardid/Akurtech a través del APIM de Bind PSP, con un producto armado para él. El alcance que Hernán Clarich identificó el 23/09 es Login (12.e), Transaction y NotRealized de pagos con TD (17.a/17.b) y Loans/GetLoanById (16/16.a). Onboarding sigue sin referencia en la documentación. El pedido de segmento se cruza con el proyecto de segmentación PJ (PRD-263), que define los segmentos de cada cuenta en Wallet y Ardid.

> Fuente: Mail "Re: Consultas integración" — Juan Ignacio Bigourdan (2026-09-30, 2026-10-01), Rocío Revelli (2026-10-01), Gonzalo Santos (2026-10-01).
