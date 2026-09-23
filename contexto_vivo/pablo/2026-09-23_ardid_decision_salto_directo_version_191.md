---
id: 2026-09-23_ardid_decision_salto_directo_version_191
pm: pablo
fecha_captura: 2026-09-23
fuente: "/sync_meetings — reunión \"Repaso Semanal líderes\" (11:00, minuta de Gemini, docId 1wqm-GkYBl7DzbzbH3hXaEQ6pLP2U7vwlA4alQCqx-j8), 2026-09-22"
producto: ardid
tema: Se acuerda saltar directo a la versión 19.1 de Ardid/Akurtech (omitiendo la 19.0) en staging y luego producción
tipo: decision
destino_propuesto: 3_recursos/detalle_productos/ardid/historico/historial_versiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Decisión acordada en "Repaso Semanal líderes" (22/09/2026):** el equipo acordó **omitir el despliegue de la versión 19.0 de Ardid/Akurtech y saltar directo a la 19.1** en los ambientes. El roadmap ya documentado en el canon (`historico/historial_versiones.md`, actualizado 2026-09-21 vía mail de Lorena Macedo/Pentass) listaba la secuencia 1.19 (sin fix UTC 0) → 1.19.1 (con el fix UTC 0, sin fecha) → 1.20 — esta reunión confirma que **1.19.1 ya está disponible para subir** y que no tiene sentido pasar primero por 1.19 sin el fix.

**Seguimiento operativo acordado en la misma reunión:**
- Mateo Capitanich (Fintexa) crea el ticket para actualizar el ambiente de staging a la 19.1 (saltando la 19.0).
- Andrea Orsini (Bind PSP) coordina la ventana de tiempo para el pase a producción de la 19.1.
- Daniel Zalazar (Fintexa) confirmó en la misma reunión que la versión 19.1 ya se encuentra subida (disponible) del lado del proveedor.

**Por qué es relevante:** la tarea T-114 del PM (pedir a Lorena Macedo el roadmap con fecha estimada de la 1.19.1, que incluye el fix de zona horaria UTC 0 mapeado tras las ráfagas de COTO) queda resuelta de facto por esta decisión — ya no hace falta esperar una fecha de release formal, el salto a 19.1 está decidido y en marcha operativa.
