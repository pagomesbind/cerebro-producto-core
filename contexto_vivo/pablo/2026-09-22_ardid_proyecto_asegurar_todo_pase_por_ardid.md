---
id: 2026-09-22_ardid_proyecto_asegurar_todo_pase_por_ardid
pm: pablo
fecha_captura: 2026-09-22
fuente: "/sync_mails — hilo Gmail `19ef5149ee3e44b8` (\"Re: MINUTA: Repaso Semanal líderes\"), mensajes del 2026-09-21 entre Agustín Grau (CTO, Fintexa) y Pablo Gomes"
producto: ardid
tema: Proyecto de Nicolás Colón para que todas las operaciones pasen por Ardid — pregunta abierta sobre comportamiento fail-closed si Ardid cae
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

**Contexto:** en una minuta de "Repaso Semanal líderes" del 2026-06-23 había quedado un action item para Pablo Gomes: "Crear ticket para gestionar la conexión y desconexión manual de Ardid" (switch on/off para poder operar aunque Ardid esté caído). El 2026-09-21, Agustín Grau (CTO de Fintexa) retomó el hilo preguntando por el estado de ese ticket.

**Respuesta de Pablo Gomes (2026-09-21):** ese requerimiento puntual no se ticketeó por separado — lo absorbió Nicolás Colón dentro de un proyecto más amplio de Ardid ("el proyecto de asegurarnos que todo pase por Ardid", en construcción, con ese requerimiento específico ya en QA del lado de Bind). No hay más detalle en este hilo sobre el nombre/PRD de ese proyecto de Nicolás Colón — no se identificó en `1_proyectos/` de Pablo porque es un proyecto de otro PM.

**Pregunta sin responder (Agustín Grau, misma fecha):** "¿el switch para encender/apagar la conexión con Ardid ya no sería necesario? ¿Siempre se rechazarán todas las operaciones si Ardid no funciona?" — es decir, Fintexa interpreta que el proyecto de Nico podría estar moviendo el comportamiento de Ardid hacia **fail-closed** (rechazar todo si Ardid no responde) en vez de mantener la posibilidad de desconectarlo manualmente y seguir operando sin control antifraude. Pablo no respondió esta pregunta en el hilo.

**Dato adicional aportado por Agustín Grau:** el pedido que finalmente quedó vigente del lado de Fintexa es un ticket propio (no de Bind), "[US] Habilitación de análisis global y por operación en Ardid" — `https://fintexa.atlassian.net/browse/DEM-1791`.

**Por qué es un gap y no solo conocimiento:** el comportamiento de Ardid ante una caída (fail-open vs. fail-closed) es una definición de riesgo de negocio con impacto directo en disponibilidad transaccional, y hoy no hay ninguna respuesta ni documentación en el Cerebro que confirme cuál de las dos alternativas rige — ni si el proyecto de Nicolás Colón formalizó esa decisión o es un efecto colateral no evaluado. Ver tarea T-116 en `1_proyectos/tareas.md` para el seguimiento de la respuesta pendiente a Fintexa.
