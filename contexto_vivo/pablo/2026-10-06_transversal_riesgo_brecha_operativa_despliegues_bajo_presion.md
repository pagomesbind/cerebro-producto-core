---
id: 2026-10-06_transversal_riesgo_brecha_operativa_despliegues_bajo_presion
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_meetings — reunión 'Repaso Semanal líderes' (2026-10-06 10:59, compartida evignoles), minuta Gemini"
producto: transversal
tema: Riesgo de decisiones operativas erróneas durante despliegues (brecha de conocimiento del circuito de transferencias + presión/cansancio) — mitigación acordada de guardia pasiva
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

A raíz del rollback erróneo de la versión 73.1 de adquirencia (ver item de conocimiento relacionado sobre la mecánica del incidente, mismo día/reunión), el equipo de liderazgo reconoció un riesgo operativo estructural, no puntual de este incidente: el equipo que toma decisiones de guardia durante un despliegue nocturno puede no tener el conocimiento operativo suficiente de circuitos técnicos externos (ej. la API de Coelsa) para diagnosticar correctamente un error antes de decidir un rollback, y la presión de tiempo/cansancio de una guardia nocturna agrava ese riesgo.

**Mitigación acordada en la misma reunión (2026-10-06):** se acordó implementar una guardia pasiva — turnos de soporte vía WhatsApp con un representante designado por área, para brindar soporte y guiar al equipo de guardia ante imprevistos durante cada despliegue a producción. Pablo Serra había propuesto además sumar una persona con conocimiento operativo avanzado para acompañar las implementaciones; se definió que Matías Alzogaray organiza internamente la guardia pasiva y el canal de WhatsApp.

Riesgo abierto hasta que la guardia pasiva esté operativa: no hay fecha confirmada de implementación en esta reunión.

> Fuente: reunión "Repaso Semanal líderes" (2026-10-06), minuta Gemini.
