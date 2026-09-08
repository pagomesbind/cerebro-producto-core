---
id: 2026-09-07_transversal_decision_idea_jira_discovery_desde_inicio
pm: pablo
fecha_captura: 2026-09-07
fuente: "/idea_start sobre gestion_riesgo_fraude — instrucción explícita del PM al responder la Ronda 1 (Q2)"
producto: transversal
tema: Momento de creación del ticket de IDEA en Jira
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: d783db8
---

## Decisión

De acá en adelante, el ticket de IDEA en Jira (espacio Producto) se crea **desde el arranque del discovery**, apenas se identifiquen categoría, cliente y producto — aunque la descripción quede vacía hasta avanzar el trabajo — y en estado **DISCOVERY**, asignado al PM que la está trabajando. Si ya existe una IDEA relacionada en backlog (sin dueño claro o parecida), se edita/reasigna esa en vez de crear una nueva.

## Contexto / por qué

Hasta ahora la creación en Jira solía esperar a tener más definición (alcance cerrado, PRD armado) antes de cargar el ticket. Eso generaba dos riesgos: (1) que dos PM/PO trabajaran sobre el mismo tema sin saberlo, porque no había ningún rastro visible en Jira de que alguien ya lo estaba discoveriando; (2) que no quedara claro, para el resto del equipo, quién tenía en curso el discovery de qué tema.

## Cómo se aplicó (primer caso real)

Surgió al procesar el discovery de `1_proyectos/gestion_riesgo_fraude/` (Comunicaciones "A" 8471 y 8473 del BCRA): antes de cerrar el Gate 2, el PM pidió crear la IDEA en Jira ya, asignada a él, en DISCOVERY — sin esperar a tener el alcance ni la solución definidos. Se creó [PRD-238](https://bindpsp.atlassian.net/browse/PRD-238) con Categoría, Producto y Cliente cargados, descripción vacía.

## Impacto

Cambia el paso "creación en Jira" del pipeline de discovery para **todos los PM/PO** que usan `/idea_start` / `/idea_jira`, no solo para este proyecto. Candidato a reflejarse en la propia skill `/idea_jira` (o en `/idea_start`, en el paso de creación de la carpeta) si el equipo que mantiene las skills compartidas lo confirma como estándar.
