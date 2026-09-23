---
id: 2026-09-22_iniciativa-ardid-desconocimientos-historias-y-jira-creados
pm: nicolas
fecha_captura: 2026-09-22
fuente: "Sesión propia — corridas de /idea_us y /idea_jira sobre ardid_desconocimientos"
producto: ardid
tema: ardid_desconocimientos — 4 historias de usuario escritas y cargadas en Jira (Epic + 4 historias), con corrección de un dato duro del diseño
tipo: iniciativa
proyecto: ardid_desconocimientos
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

Avance del día sobre `ardid_desconocimientos` (PRD-248), que ya tenía PRD y estimación preliminar (14 SP) cargados:

1. **4 historias de usuario escritas** (una por cada funcionalidad del PRD, a pedido explícito del PM): aviso automático al motor antifraude, detección/alerta de discrepancias (reconciliación), ampliación de la ventana de retención, y pedido formal al proveedor de un mecanismo de carga individual.
2. **Corrección de un dato duro del diseño:** el campo `countRetry` que se envía al motor antifraude se confirmó como un valor fijo en 3, no un contador incremental de reintentos como se había asumido originalmente en el análisis técnico-funcional. Esto elimina la única hipótesis de deduplicación de reenvíos que tenía el diseño — el punto queda más abierto, a validar con el proveedor.
3. **Jira: Epic y 4 historias creadas**, todas bajo el proyecto AD (Adquirencia): Epic AD-1785 "Informar desconocimiento de transacción en Ardid (Contracargo)" (mismo nombre que el PRD) y sus 4 historias hijas AD-1786 a AD-1789 — todas en prioridad **High** por instrucción explícita del PM, sin la diferenciación MoSCoW que se había propuesto originalmente.
4. **Bloqueo de herramienta, no de proceso:** el conector de Jira quedó con un alcance de escritura muy reducido durante la sesión (solo `createJiraIssue` disponible) — la IDEA PRD-248 sigue sin poder transicionarse a EN APROBACION, sin poder subir su prioridad, y sin el link IDEA↔Epic creado. Queda pendiente retomarlo cuando el conector recupere el resto de las herramientas.

Sin novedad de pm_destino — proyecto propio de Nicolás Colón, foco Ardid.
