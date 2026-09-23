---
id: 2026-09-23_iniciativa_rechazos_bines_payway_fintexa_decision_eliminar_validacion
pm: pablo
fecha_captura: 2026-09-23
fuente: "/sync_meetings — reunión \"Repaso Semanal líderes\" (11:00, minuta de Gemini, docId 1wqm-GkYBl7DzbzbH3hXaEQ6pLP2U7vwlA4alQCqx-j8), 2026-09-22"
producto: adquirencia
tema: PRD-251 — Fintexa decide eliminar la validación de bines del frontend (no sincronizarla) e incluirla en el despliegue de v73, previsto jueves 24/09
tipo: iniciativa
proyecto: PRD-251
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

**Novedad puntual para `direccion/iniciativas.md`:** en la reunión "Repaso Semanal líderes" del 22/09/2026, Fintexa (representada por Melisa Belpassi) decidió la resolución de fondo del bloqueo que tenía frenado el Frente A de `rechazos_bines_payway` (PRD-251) desde el 2026-09-21: en vez de sincronizar el archivo estático del frontend (`payment_methods.json`) con la base real `IssuerIdentification`, se acordó **eliminar la validación de bines del frontend directamente**, empaquetado dentro del despliegue de la versión 73 (previsto para el jueves 24/09/2026, según decisión de priorización de la misma reunión — v73 pasa por delante de la regresión de la APK 65 de POS).

Para acotar las pruebas antes del despliegue, Melisa Belpassi está usando un listado de los BINs con mayor tasa de falla (aportado por "Maru") en lugar de evaluar los 80.000 BINs completos. El ticket queda en manos de QA externo. Los scripts para completar la carga de los 80.000 bines faltantes se correrían el jueves o viernes posteriores al despliegue de v73, una vez medido el tiempo real de proceso.

Esta decisión responde de facto a la pregunta 2 de la tarea T-115 del PM ("¿conviene migrar el checkout para que valide solo contra `IssuerIdentification` vía API?") — sin confirmación formal todavía por escrito de parte de Fintexa, pero con dirección y fecha ya decididas en la reunión. Desbloquea, con la fecha del despliegue de v73, tanto T-101 (aplicar el ticket AD-978) como el propio Frente A del proyecto.

Actualizado directo en `1_proyectos/`: `rechazos_bines_payway/proyecto.md` (encabezado + §7 + §9), `tareas.md` (T-101, T-115), `1_proyectos/index.md` (fila PRD-251). Comentario consolidado posteado en Jira PRD-251 el mismo día.
