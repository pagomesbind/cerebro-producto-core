---
id: 2026-08-19_portal_admin_parametrizacion-manual-entidades
pm: pablo
fecha_captura: 2026-08-19
fuente: "/sync_meetings — reunión 'Parámetros de entidades' (mail de gemini-notes@google.com, sin Doc de Drive accesible — la búsqueda de Drive devolvió solo un shortcut sin contenido resoluble), 2026-08-19 11:01"
producto: portal_admin
tema: Incidentes por parametrización manual y fragmentada de entidades — panel admin actual insuficiente
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 5f0974a
---

**Nota de fuente:** esta reunión llegó solo por el detector de Gmail — la búsqueda en Drive devolvió el archivo como un `shortcut` (`application/vnd.google-apps.shortcut`) sin contenido resoluble por las tools disponibles, así que el detalle completo (incluyendo hora exacta de fin y posibles matices de la transcripción) no pudo verificarse contra la minuta original. El contenido de este item viene íntegro del cuerpo del mail de Gemini.

**Problema identificado:** los incidentes frecuentes en producción derivan de configuraciones manuales y fragmentadas entre entidades — no hay una documentación clara y centralizada de qué parámetros hace falta configurar por producto/entidad, lo que complica la gestión operativa y compromete el aseguramiento de calidad (QA).

**Caso concreto mencionado:** Mastercard (integración cross-border/pagos al exterior) es de los productos de alto volumen que hoy se configuran manualmente sin plantilla documentada — mientras no exista una API de configuración, Juan Pablo Carubelli va a elaborar plantillas documentadas con los parámetros necesarios para su configuración manual, como paliativo.

**Estrategia técnica priorizada (ver decisión relacionada):** desarrollar un orquestador vía APIs para automatizar la configuración de entidades, usando ~50 parámetros estandarizados, para eliminar la dependencia técnica manual de hoy — priorizado sobre modificar directamente el panel de administración actual.

**Próximos pasos acordados (grupales):**
- Unificar toda la documentación de configuración de entidades en un repositorio centralizado, para que todos los equipos consulten la misma información técnica.
- Relevar los pasos necesarios para parametrizar cada producto con los referentes de cada área, documentando cada caso de uso específico.
- Definir una rutina estándar de alta de entidades ejecutable por API o interfaz, que orqueste automáticamente las configuraciones necesarias.
- Recopilar los requerimientos operativos por canal y convenio para reducir la complejidad actual.
- Investigar qué falta en el panel de administración actual para poder crear y configurar entidades correctamente en producción.
- Organizar reuniones con Mariela Marin (Fintexa) y Nico Colón (otro PM de Bind PSP) para relevar en detalle las dependencias y mejorar las especificaciones de integración por vertical.

**Seguimiento personal:** Pablo Gomes quedó con la tarea de trabajar con el equipo de productos para que todo nuevo producto/funcionalidad incluya una API de configuración como parte de sus requisitos — ver `tareas.md` T-022.
