---
id: 2026-08-20_adquirencia_hotfix_localidades_codigo_postal
pm: pablo
fecha_captura: 2026-08-20
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-08-20 12:05, docId 1Q3PZO-WuwDNq5HOyW-eoww1KEVJBvwL7-NP9nT3WMkE)"
producto: adquirencia
tema: Hotfix de validación de localidades/códigos postales en alta y edición de comercio — endpoint modificado para devolver lista
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/configuracion_de_entidades.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 75959e2
---

**Problema:** inconsistencias en las validaciones de localidad y código postal durante la creación y edición de comercios/entidades, que causan errores de validación (Daniela Collia, Fintexa, presentó el análisis).

**Discusión:** se evaluó estandarizar el formato de los datos y cambiar la respuesta del endpoint de localidades para que devuelva una lista de localidades en lugar de una sola.

**Decisión acordada (2026-08-20):**
- El **endpoint de localidades se modifica** para retornar una lista de localidades en vez de una sola — esta tarea se separa en un ticket de menor prioridad (no es parte del hotfix inmediato).
- El **alcance del hotfix se mantiene limitado** a corregir las validaciones actuales de código postal/localidad — se posterga la reestructuración de la respuesta de la API a un ticket futuro, al no considerarse una urgencia funcional para los usuarios actuales.
- Nicolás Colón queda a cargo de crear el ticket para el ajuste de la lista de localidades y códigos postales, una vez documentado el alcance (Daniela Collia debe indicar explícitamente en el ticket 789 que el cambio de respuesta de localidades queda fuera de alcance de este hotfix).

**Confianza media:** no hay contexto previo documentado en la wiki sobre el endpoint de localidades específico ni el ticket 789 — el destino propuesto (`configuracion_de_entidades.md`, manuales de alta/configuración de comercio) es el mejor candidato por temática, a confirmar en el merge si existe un archivo más específico o si conviene crear uno nuevo.

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini.
