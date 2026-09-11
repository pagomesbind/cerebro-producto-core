---
id: 2026-09-11_transversal_decision_confluence_diferido_limite_jira
pm: pablo
fecha_captura: 2026-09-11
fuente: "Sesión de trabajo sobre PRD-202 (/idea_jira) — hallazgo surgido al corregir AC-15/AC-37 de WS-1560/OB-235"
producto: transversal
tema: Límite de tamaño y falta de adjuntos/diagramas reales en Jira — Confluence quedaría como solución futura, no contratado hoy
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Hallazgo técnico (2026-09-11, durante la sincronización de Jira de PRD-202):** el campo `description` de un ticket de Jira (formato ADF) tiene un techo real de ~28-30KB — por encima de eso, la API rechaza el contenido con `CONTENT_LIMIT_EXCEEDED`. Se confirmó de forma práctica: OB-235 (historia con 38 criterios de aceptación) lo superó incluso comprimiendo tablas markdown a listas, y tuvo que dividirse en descripción + un comentario aparte del mismo ticket. Además, el conector Jira (MCP) usado desde el Cerebro no expone ninguna tool para adjuntar archivos/imágenes a un ticket, y los bloques ` ```mermaid ` embebidos en las descripciones probablemente no rendericen como diagrama real en Jira Cloud estándar (sin verificar si el workspace de Bind tiene un plugin de Mermaid instalado) — quedan como texto plano.

**Alternativa evaluada:** mover el contenido técnico pesado (contrato completo, diagramas) a una página de Confluence —sin ese límite de tamaño, con bloque nativo de Mermaid y soporte real de adjuntos— y dejar en Jira una historia más concentrada que linkea a esa página, en vez de duplicar todo como texto plano en la descripción. Las tools de Confluence ya están disponibles en el conector Atlassian que usa el Cerebro.

**Decisión tomada por el usuario (2026-09-11):** no se contrata Confluence por ahora — la organización no lo tiene licenciado. Queda **pendiente de análisis futuro**, a retomar si en algún momento se evalúa contratar Confluence (o una alternativa equivalente) y/o se revisa en profundidad el diseño de la skill `/idea_jira` (Reglas duras 12/13, que hoy asumen que todo el contenido técnico entra como texto en la descripción/comentarios de Jira).

**Por qué queda anotado como decisión y no solo como gap:** no es una inconsistencia de conocimiento ya documentado — es una limitación de plataforma ya confirmada, con una alternativa concreta ya identificada y deliberadamente pausada por costo/licencia, no por falta de análisis.
