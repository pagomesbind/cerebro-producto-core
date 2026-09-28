---
id: 2026-09-28_arquitectura_discovery_salud_api_clientes_cerrado
pm: pablo
fecha_captura: 2026-09-28
fuente: "/idea_start sobre salud_api_clientes, 2026-09-25 a 2026-09-28"
producto: transversal
tema: Cierre del discovery de exposición de salud/latencia a clientes — alcance del MVP ampliado a terceros
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/nfr_y_slas.md
tipo_destino: actualizar
contradice: "3_recursos/arquitectura_sistema/nfr_y_slas.md §3 — la nota vigente dice que la iniciativa sigue 'en discovery desde 2026-09-10' y que la cobertura de terceros vía Elastic es una extensión futura sin cerrar; el discovery formal de Producto ya cerró y decidió que esa cobertura de terceros es parte del MVP, no una fase posterior"
confianza: alta
estado: en_cola
---

## Qué cambia respecto de lo ya mergeado

El §3 de `nfr_y_slas.md` ("Exposición externa de salud/latencia a clientes") describe el acuerdo técnico del 2026-09-10 entre Hernán Clarich/Fintexa y el equipo externo Keepit Simple (Grafana interno + servicio dedicado publicado en el APIM, caché de 60s), con la cobertura de terceros (Coelsa/API Bank vía Elastic) como una extensión todavía en curso, sin fecha. Ese acuerdo nunca había pasado por un discovery formal de Producto — nace y vive como nota de arquitectura.

## Contenido nuevo

El discovery formal de Producto (`/idea_start`, proyecto `salud_api_clientes/`, 2026-09-25 a 2026-09-28) se cerró con los 4 gates confirmados por el PM (Pablo Gomes):

- **Gate 1:** problema esencial confirmado — clientes con integración API directa no tienen forma proactiva de saber cuándo un producto está degradado del lado de Bind, incluyendo cuando la causa es un tercero.
- **Gate 2:** ✅ Vale la pena ahora, pese a no encajar en ninguna NSM ni foco estratégico 2026 — sostenido en que el costo de oportunidad real es bajo (desarrollo externo vía Keepit Simple, no ingeniería interna).
- **Gate 3:** abanico de 4 carriles confirmado, incluyendo un carril operativo (formalizar el aviso proactivo de Soporte a clientes de alto volumen) como puente.
- **Gate 4 — el cambio de fondo:** el PM decidió que el MVP debe incluir la visibilidad de terceros (Coelsa, API Bank) **desde el lanzamiento**, no como la "Etapa 2" que Hernán/Keepit tenían planeada. Cita textual: *"El MVP debe comprender todo, incluyendo las externas. No podemos darle a un cliente una API que le diga que está todo bien, aunque Coelsa o el banco estén caídos. Nos matarían."* Esto reabre el roadmap técnico ya acordado y todavía no tiene dimensionamiento (Hernán/Keepit deben especificar esa parte).

También quedó identificado un riesgo técnico concreto sobre la definición de "uptime" ya especificada (`ResponseCode 1-499 = éxito`): podría no capturar rechazos de negocio causados por un tercero caído — mismo riesgo de "placebo" que Pablo Gomes había señalado en la reunión del 2026-09-10. Queda como pregunta abierta para el análisis funcional-técnico (`/idea_solution`), no resuelta en este discovery.

IDEA de Jira creada: [PRD-262](https://bindpsp.atlassian.net/browse/PRD-262), en DISCOVERY.

## Actualización (2026-09-28, mismo día — conversación Pablo Gomes ↔ Hernán Clarich)

Hernán confirmó el mecanismo técnico para la cobertura de terceros: lo que ya entregó a Keepit (basado en APIM/Azure Monitor) solo cubre el sistema propio de Bind. Para ver la salud de Coelsa/API Bank, Keepit necesita conectarse también a **Elastic Search** y leer las interacciones de **ingress/egress**; Hernán le va a pasar a Keepit las consultas de Elastic correspondientes. La conexión técnica en sí (el "cómo") la resuelve Keepit junto con el área de Infraestructura y Hernán — no se va a especificar ese detalle en las historias de usuario, solo el requisito funcional de cobertura. Además, Hernán confirmó que las alertas proactivas/webhooks (la Etapa 3 de su roadmap original) pueden tratarse como un proyecto futuro separado, no como parte de este MVP — coincide con la frontera de foco que ya había cerrado el discovery.

## Sugerencia de actualización para `nfr_y_slas.md §3`

Reemplazar "(en discovery desde 2026-09-10)" por una referencia al proyecto formal `salud_api_clientes/` (PRD-262) y su estado (Gate 4 cerrado, MVP ampliado a terceros vía conexión a Elastic Search para ingress/egress — mecanismo confirmado por Hernán Clarich, tamaño/plazo todavía pendiente de dimensionar), y anotar que los webhooks/alertas proactivas quedan explícitamente como candidato a un proyecto futuro separado.
