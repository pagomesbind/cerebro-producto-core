---
id: 2026-09-24_onboarding_gap_dueno_validaciones_arca_bcra_produccion
pm: pablo
fecha_captura: 2026-09-24
fuente: "/sync_meetings — reunión 'Revisión OB PJ | Interna' (2026-09-24, 11:01, minuta Gemini, docId 1vVZgqjGCzKNGDhjV-pQ0_8MX59vSpcNX9jFHVkbnow0)"
producto: onboarding
tema: sin dueño confirmado de la decisión de activar las validaciones automáticas de ARCA/BCRA en el onboarding de personas jurídicas
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 2bc1252
---

Durante la capacitación interna del flujo de onboarding PJ (La Virginia, PRD-223), Gonzalo Rivera preguntó sobre las validaciones automáticas de identificación de riesgo (ARCA — deudor/actividad, y BCRA) que el sistema puede correr sobre cada solicitud. Pablo Gomes confirmó que en el ambiente de pruebas (staging) **están todas desactivadas** — el único chequeo activo es la consulta del padrón de actividad de ARCA. Aparentemente el mismo estado (todo apagado) se replica en producción, aunque no se confirmó con certeza.

**Nadie en la reunión pudo confirmar si esas validaciones deberían estar prendidas ni quién tiene la autoridad para decidirlo:**
- Gonzalo Rivera aclaró que nunca participó del diseño de onboarding jurídico, por lo que no sabe qué debería estar activo.
- Adriana Endzeliz (PLD) mencionó haber escuchado al equipo de PLD decir que "hay que validar situación en ARCA" (situación 1/2/3, ligada al apetito de riesgo de la organización), pero no confirmó si eso aplica a los flags que hoy están desactivados en este producto puntual.
- Quedó sin resolver **quién es el responsable de tomar esta decisión** (¿Cumplimiento/PLD? ¿Fraude? ¿el propio PM de Onboarding?).

Este gap es relevante porque, sin esas validaciones activas, la aprobación de nivel 1 (oficial de negocio) y nivel 2 (PLD) del flujo de onboarding PJ dependen enteramente del criterio manual del revisor — no hay ningún filtro automático de riesgo soportando la decisión.

> Fuente: reunión "Revisión OB PJ | Interna" (2026-09-24, 11:01 GMT-03:00), intercambio entre Gonzalo Rivera, Adriana Endzeliz y Pablo Gomes.
