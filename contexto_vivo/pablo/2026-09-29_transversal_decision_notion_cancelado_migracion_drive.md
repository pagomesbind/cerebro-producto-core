---
id: 2026-09-29_transversal_decision_notion_cancelado_migracion_drive
pm: pablo
fecha_captura: 2026-09-29
fuente: "/sync_meetings — reunión \"Productos - Weekly Seguimiento\" (2026-09-29 10:26, compartida por lrudaz), minuta + transcripción Gemini"
producto: transversal
tema: "Cancelación de la suscripción de Notion — fecha límite 10/10/2026 para perder acceso de escritura, migración de documentación de Producto a Google Drive"
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

En la reunión "Productos - Weekly Seguimiento" (10:26, Luciana Rudaz, Pablo Gomes, Nicolás Colón, Matias Alzogaray), Luciana Rudaz informó que **canceló la suscripción de Notion** que usaba el equipo de Producto para documentar (endocs, casos de uso por proyecto). La fecha límite comunicada es el **10 de octubre de 2026**: a partir de ahí, según lo discutido en la reunión, el equipo pierde el **permiso de escritura** sobre lo que tenía en Notion (hubo una contradicción menor dentro de la misma conversación sobre si también se pierde el acceso de lectura — un participante dijo "no lo vas a perder... lo que no vas a poder es escribir", así que se toma la versión más específica: se pierde escritura, no necesariamente lectura).

**Decisión de destino:** migrar la documentación de Producto a **Google Drive**, dentro del espacio compartido de BIND PSP ("producto"), organizada por carpeta de proyecto (ej. "Pagos Effects", lo que cada PM necesite). Se descartó por ahora armar una alternativa más sofisticada (tipo Notion con vista editable vs. compartida) — la decisión quedó en Drive por practicidad y porque ya lo estaban usando de facto ("yo hoy estoy volcando todo en Drive").

**Contexto de uso real:** de ~50 licencias de Notion activas, solo 4-5 personas lo usaban activamente (equipo de Producto). Luciana avisó a Ema (líder) y a los demás líderes; Pablo Gomes indicó en la reunión que no tenía conocimiento previo de la cancelación.

**Relevancia directa para el Cerebro:** las skills `/sync_notion_docs` (motor de sincronización/consolidación desde Notion) y `/sync_customers` (altas/bajas de clientes, que usa Notion como fuente) dependen de acceso de lectura/escritura a Notion. Si el 10/10 se pierde el acceso, ambas skills quedan en riesgo de no poder correr o de quedar desactualizadas — requiere evaluación y posible replanteo de fuente antes de esa fecha.

> Fuente: reunión "Productos - Weekly Seguimiento", 2026-09-29 10:26 (`/sync_meetings`), minuta y transcripción de Gemini (docId `1RJehZTE9KyG5Ru4n-Wp_oUm0JvL1M0cTB0fBrbv6XgM`).
