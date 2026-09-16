---
id: 2026-09-15_iniciativa-titularidad-tarjeta-gate3-cerrado-modo-vs-ardid
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Discovery /idea_start, sesión 2026-09-10 a 2026-09-15 (varias reuniones intermedias: Daily producto 2026-09-11, Análisis COBRO 2026-09-14)"
producto: Adquirencia (Botón Simple) / Ardid
tema: Cierre de discovery de validación de titularidad de tarjeta (PRD-25) — MODO después de Ardid
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: cb58cfd53c7f3d391017622178663faa33c1c2b8
proyecto: titularidad_tarjeta
---

Discovery de `/idea_start` sobre [PRD-25](https://bindpsp.atlassian.net/browse/PRD-25) "Validar titular de tarjeta" cerró sus 3 gates: (Gate 1) el problema es que Bind no valida hoy la titularidad de la tarjeta en Botón Simple, generando contracargos por "tarjeta no propia" — iniciativa impulsada por Emma Vignoles (COO); (Gate 2) vale la pena ahora, foco = todo comercio de Botón Simple por igual, sin discriminar por segmento; (Gate 3, cerrado 2026-09-15) la solución adoptada es validar con la API VaTa de MODO **después** de que Ardid analice la transacción, y solo si Ardid no la rechaza por motivos propios (~10% de rechazo propio medido por el PM) — esto ahorra ≈USD 73.000/año frente a validar el 100% de las transacciones (USD 656.139/año vs. USD 729.043/año, sobre una base de 506.280 transacciones/mes de agosto 2026), sin resignar el objetivo de evitar contracargos, porque una transacción que Ardid ya rechaza nunca llega a cobrarle a nadie. Diseño de resiliencia acordado: ante timeout/caída de MODO, 2 reintentos y luego fail-open (no se frena la operatoria); ante una respuesta 409 de "titular inválido/tarjeta deshabilitada/tarjeta expirada" se rechaza la transacción, el resto de los 409 y los códigos 400/401/404 continúan la operatoria normalmente.

Queda un gap técnico abierto antes de poder especificar el desarrollo en detalle: no se pudo confirmar con la documentación pública de MODO si la respuesta 409 permite distinguir cuál de los 6 motivos de rechazo ocurrió (necesario para el diseño de manejo de respuestas acordado). Sin proyecto padre — es un proyecto propio, transversal, sin relación de dependencia confirmada con PRD-146 ("Tratamiento de contracargos de tarjeta", mismo PM, EN CURSO en Jira) pese a compartir dominio de "contracargos de tarjeta".

Paso siguiente sugerido: `/idea_prd` para formalizar la especificación técnica, una vez resuelto el gap del 409 con MODO.
