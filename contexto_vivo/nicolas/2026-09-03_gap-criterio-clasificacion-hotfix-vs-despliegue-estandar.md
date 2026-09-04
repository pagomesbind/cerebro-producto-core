---
id: 2026-09-03_gap-criterio-clasificacion-hotfix-vs-despliegue-estandar
pm: nicolas
fecha_captura: 2026-09-03
fuente: "Reunión \"Analisis de riesgo - Fix Contracargo\" (2026-09-03)"
producto: transversal
tema: No hay un criterio explícito y documentado para decidir cuándo un ticket amerita clasificarse como hotfix urgente (fuera del ciclo mensual) vs. esperar a la próxima publicación
tipo: gap
destino_propuesto: 2_areas/procesos/analisis_de_riesgo_de_despliegue.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Analisis de riesgo - Fix Contracargo" (2026-09-03) se generó un debate real y sin resolución formal sobre **cómo clasificar un ticket como hotfix** (pase fuera de ciclo) frente a esperar a la próxima publicación mensual. `2_areas/procesos/analisis_de_riesgo_de_despliegue.md` documenta el proceso de semáforo de riesgo (verde/amarillo/rojo) para tickets **ya incluidos en una versión**, pero no cubre el criterio para decidir si algo amerita salir de ese ciclo como excepción.

Nicolás Colón planteó explícitamente la pregunta sin obtener respuesta cerrada: *"necesito entonces dónde dibujar la línea, qué parámetro tomar para determinar si algo es Hotfix o no"* — había levantado el ticket AD1639 como urgente por el reclamo del cliente histórico Ripsa (que no podía hacer devoluciones), pero Andrea Orsini cuestionó en qué momento y con qué criterio alguien determina que algo es hotfix ("a mí siempre me llegó esto como que era un hotfix... pero ¿en qué momento alguien lo determinó?"). Pablo Antonio Gomes sugirió como heurística consultar primero con el cliente si puede tolerar esperar hasta la próxima implementación antes de escalar como hotfix, y señaló que hay que "bajar los humos" con la urgencia declarada de entrada. Melisa Belpassi aclaró que, en este caso puntual, no se trató de un hotfix improvisado (desarrollo terminado el día anterior, probado en staging la misma mañana, pasado en horario laboral por el canal normal) — pero eso resolvió el caso puntual, no la pregunta de fondo sobre el criterio general.

No se llegó a una definición: quedó como heurística informal ("preguntarle al cliente si tolera esperar") sin plasmarse como criterio del proceso. Vale la pena que `/context_merge` evalúe si esto amerita una sección nueva en `analisis_de_riesgo_de_despliegue.md` o un archivo propio de criterio de hotfix.

> Fuente: Reunión "Analisis de riesgo - Fix Contracargo" (2026-09-03), minuta Gemini.
