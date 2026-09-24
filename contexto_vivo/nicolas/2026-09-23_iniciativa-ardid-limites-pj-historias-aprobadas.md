---
id: 2026-09-23_iniciativa-ardid-limites-pj-historias-aprobadas
pm: nicolas
fecha_captura: 2026-09-23
fuente: "Sesión /idea_us con el PM (Nicolás Colón), 2026-09-22/23"
producto: ardid
tema: Segmentación de personas jurídicas en Ardid — historias de usuario aprobadas (2 historias), estimación XL se mantiene
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: ardid_limites_pj
---

El proyecto `ardid_limites_pj` tiene sus historias de usuario aprobadas por el PM (2026-09-23). Quedaron **2 historias de desarrollo**, ambas del equipo de Wallet:

1. **Alta de Organización:** creación automática de 3 tipos de titular (persona física adulta, persona física menor, persona jurídica) y 2 niveles cada uno (estándar y restringido) en el motor antifraude, más su réplica en el Calculador de Costos, con persona jurídica en restringido por defecto.
2. **Alta de Cuenta:** clasificación automática del tipo de titular por CUIT y edad, y asignación del nivel por defecto de la Organización, sin bloquear nunca el alta.

Se descartó una tercera historia sobre el cambio puntual de segmento de una cuenta (restringido → estándar): el PM confirmó que esa operación ya existe y ya llega al motor antifraude para cualquier cuenta, siempre que el segmento del Calculador de Costos esté enlazado a su nivel. Queda como ítem de lanzamiento el proceso operativo de ese cambio, todavía sin definir y urgente por el deadline del 1° de octubre.

La estimación de proyecto se mantiene en **XL (15 SP)** pese a la reducción a 2 historias — decisión del PM. Sigue sin IDEA de Jira propia; pendiente la aprobación de Emma Vignoles y una consulta técnica consolidada con Ingeniería/Fintexa.

> Fuente: `wiki/1_proyectos/ardid_limites_pj/artefactos/ardid_limites_pj-us.md` (v1.7, aprobado), `decisiones.md` [2026-09-23].
