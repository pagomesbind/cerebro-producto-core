---
id: 2026-08-19_decision_api-configuracion-requisito-productos
pm: pablo
fecha_captura: 2026-08-19
fuente: "/sync_meetings — reunión 'Parámetros de entidades', 2026-08-19 11:01 (vía mail de gemini-notes@google.com — ver nota de fuente en el conocimiento asociado 2026-08-19_portal_admin_parametrizacion-manual-entidades)"
producto: transversal
tema: Priorizar orquestador de configuración de entidades vía API sobre modificar el panel admin actual
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

**Decisión acordada (2026-08-19, reunión "Parámetros de entidades"):** frente a los incidentes recurrentes por configuraciones manuales y fragmentadas de entidades entre productos, el equipo priorizó desarrollar un **orquestador de configuración vía APIs** (con ~50 parámetros estandarizados) para automatizar el alta/configuración de entidades, en lugar de invertir en modificar directamente el panel de administración actual. Mientras el orquestador no exista, se documentarán plantillas JSON puntuales para productos de alto volumen que hoy se configuran a mano (ej. Mastercard).

**Impacto en el roadmap/producto:** de cara adelante, todo nuevo producto o funcionalidad de Bind PSP debería incluir una API de configuración como parte de sus requisitos desde el diseño, para evitar reproducir la misma dependencia técnica manual — Pablo Gomes quedó a cargo de llevar este criterio al equipo de productos (ver `1_proyectos/tareas.md` T-022).

**Estado:** Acordado en la reunión — sin fecha de inicio de desarrollo del orquestador todavía definida.
