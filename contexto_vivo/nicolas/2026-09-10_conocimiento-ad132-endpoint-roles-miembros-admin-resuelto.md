---
id: 2026-09-10_conocimiento-ad132-endpoint-roles-miembros-admin-resuelto
pm: nicolas
fecha_captura: 2026-09-10
fuente: "Reunión \"Análisis COBRO\" (2026-09-10), minuta Gemini"
producto: portal_admin
tema: Ticket histórico AD132 — roles de usuario desaparecían intermitentemente en el Admin por caché defectuosa y endpoint recursivo ineficiente; aprobado el desarrollo de la corrección
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/portal_admin/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Julieta Gimenez (Fintexa) presentó en "Análisis COBRO" (2026-09-10) el ticket antiguo **AD132**, relacionado con la sección de entidades y usuarios del Admin: los **roles de usuario desaparecían intermitentemente**, causado por problemas de caché y un endpoint ineficiente con llamadas recursivas para obtener los roles de miembros.

**Resolución acordada:** optimizar un endpoint exclusivo para la obtención de roles de miembros, eliminando la dependencia de la caché defectuosa (estimación: 3 puntos de historia, tamaño M). El equipo presente (Pablo Gomes, Matías Alzogaray, Nicolás Colón) dio el visto bueno para proceder con el desarrollo.

> Fuente: Reunión "Análisis COBRO" (2026-09-10), minuta Gemini.
