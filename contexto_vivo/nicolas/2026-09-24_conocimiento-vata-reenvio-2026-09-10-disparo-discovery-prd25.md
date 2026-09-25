---
id: 2026-09-24_conocimiento-vata-reenvio-2026-09-10-disparo-discovery-prd25
pm: nicolas
fecha_captura: 2026-09-24
fuente: "Actualización local del 2026-09-15 al item 2026-09-11_conocimiento-modo-api-validacion-titularidad-tarjetas-vata (nunca repusheada al core antes del merge del 2026-09-23) + proyecto titularidad_tarjeta/proyecto.md + tarea T-046 (resuelta 2026-09-15)"
producto: Adquirencia (Botón Simple)
tema: VATA de MODO — el reenvío del 2026-09-10 fue el disparador del discovery de PRD-25 (no una llegada independiente a la misma solución)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/integracion_modo_vata.md
tipo_destino: actualizar
contradice: "integracion_modo_vata.md §'Por qué es relevante ahora' — dice que PRD-25 diseñó la integración con VaTa 'de forma independiente', 'sin que quede confirmado en ninguna fuente si el equipo retomó conscientemente esta propuesta de 2025'"
confianza: alta
estado: ingestado
merge_commit: 2bc1252
---

**Qué corrige.** El archivo canon `adquirencia/integracion_modo_vata.md` (creado por `/context_merge` el 2026-09-23, corrida 2, commit `25b8e37`) se redactó a partir de la versión del item `2026-09-11_conocimiento-modo-api-validacion-titularidad-tarjetas-vata` que estaba en el core. Esa versión era la original: `producto: por confirmar`, `confianza: baja`, "sin producto dueño claro". El 2026-09-15 el item se actualizó en el install de Nicolás, pero esa actualización no se volvió a subir al core antes del merge. Por eso el canon no la tiene.

**Qué se sabe (actualización del 2026-09-15, confirmada por el propio PM):**
- El reenvío que Pablo Gomes le hizo a Nicolás Colón el **2026-09-10** del mail de enero 2025 sobre VATA **fue lo que disparó** el discovery propio (`/idea_start`, del 2026-09-10 al 2026-09-15) sobre la IDEA de Jira que ya existía, [PRD-25](https://bindpsp.atlassian.net/browse/PRD-25) "Validar titular de tarjeta". No fue un aviso sin acción, y `titularidad_tarjeta` no llegó a VaTa por su cuenta: el proyecto retomó a propósito la propuesta de MODO a partir de ese reenvío.
- Las 3 gates del proyecto cerraron con producto dueño Adquirencia/Botón Simple y con esta solución: validar con MODO (VaTa) después de Ardid, y solo si Ardid no rechaza la transacción por sus propios motivos. Esto ya está reflejado en el canon.
- **Lo que sigue sin confirmarse (dato de color, no bloquea nada):** por qué Pablo reenvió el mail justo ahora, 18 meses después del original. La tarea T-046 se cerró el 2026-09-15 sin preguntarle, porque para el proyecto no era necesario.

**Cambio sugerido en el canon.** En `integracion_modo_vata.md`, reemplazar "diseñó de forma independiente ... sin que quede confirmado en ninguna fuente si el equipo retomó conscientemente esta propuesta de 2025 o llegó a la misma solución de forma independiente" por: el discovery de PRD-25 se abrió a partir del reenvío del 2026-09-10, así que retomó a propósito la propuesta de 2025. Queda abierto solo el motivo del reenvío. El pendiente sobre si el contrato de 2025 (`PDSA - Acuerdo VATA`) sigue vigente se mantiene como está.
