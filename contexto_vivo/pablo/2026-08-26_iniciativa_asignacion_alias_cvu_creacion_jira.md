---
id: 2026-08-26_iniciativa_asignacion_alias_cvu_creacion_jira
pm: pablo
fecha_captura: 2026-08-26
fuente: "/idea_jira (creación manual, previa a que la skill existiera formalmente) — jerarquía Jira de `asignacion_alias_cvu`, 2026-08-26"
producto: wallet
tema: "asignacion_alias_cvu — ticket de Ingeniería creado en Jira (IDEA→Epic→Historia), listo para EN APROBACION"
tipo: iniciativa
proyecto: asignacion_alias_cvu
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Novedad de `asignacion_alias_cvu/` (Pablo Gomes): se creó la jerarquía completa en Jira — IDEA PRD-224 (Categoría BAU, Producto Wallet, Cliente SOPORTE, SP estimado 3, prioridad Highest por ser bug productivo urgente, estado `EN APROBACION`), Epic WS-1555 y Historia WS-1556 (US-001, prioridad Highest, contenido completo incluyendo AC-1 a AC-13 y diagrama de flujo). Queda pendiente que el PM mueva la Historia a `Asignado` en Jira tras revisarla.

Nota operativa: el proceso de creación (clasificación de campos, estados, dirección del link IDEA↔Epic) se hizo a mano en esta sesión y expuso un problema real — el link "Polaris work item link" se creó primero en la dirección equivocada y no se pudo borrar (el conector no tiene esa tool), quedando dos links entre PRD-224 y WS-1555. Esto motivó la creación de la skill `/idea_jira`, que formaliza el procedimiento hacia adelante (siempre EN APROBACION en la IDEA, siempre Backlog en las Historias, verificación de `issuelinks` antes de crear el link) para que no se repita.

> Fuente: `1_proyectos/asignacion_alias_cvu/proyecto.md §7/§9`.
