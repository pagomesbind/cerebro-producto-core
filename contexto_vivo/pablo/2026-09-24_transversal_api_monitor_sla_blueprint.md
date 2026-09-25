---
id: 2026-09-24_transversal_api_monitor_sla_blueprint
pm: pablo
fecha_captura: 2026-09-24
fuente: "/sync_mails — mail 'Especificaciones API monitoreo y Background Service Cache', Hernán Clarich (Fintexa), threadId 1a0d3d66f6f8215b, 2026-09-24"
producto: transversal
tema: especificación técnica (Etapa 1) del Background Service Cache y la API de consumidor para monitoreo de disponibilidad/latencia del ecosistema — refina la iniciativa ya conocida de API de salud para clientes
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/index.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

## Qué cambia respecto de lo ya mergeado

El item `2026-09-18_arquitectura_nueva_api_monitoreo_salud_clientes` (ya ingerido al canon en `3_recursos/arquitectura_sistema/`) documentó el **acuerdo** de construir una API de salud/latencia para clientes a partir de los tableros de Grafana, con un servicio dedicado del equipo Kipi. Este mail trae la **primera especificación técnica concreta** (Etapa 1, basada en estadísticas de APIM `ApiManagementGatewayLogs`) de Hernán Clarich (Fintexa), con 3 adjuntos: `API_Monitor_SLA_Blueprint.pdf`, `Resumen APIs Monitoreo.docx` y `Especificación Arquitectura monitoreo.docx` — no procesados automáticamente (pendiente de lectura manual, ver nota de adjuntos).

## Contenido nuevo (cuerpo del mail, sin abrir adjuntos)

La especificación cubre un **Background Service Cache** (proceso que pre-calcula y cachea las métricas) y una **API de consumidor** para que clientes consulten disponibilidad/latencia del ecosistema. Puntos que Hernán deja explícitamente abiertos para refinar en conjunto con Pablo Gomes:

- Tecnología de cache a utilizar (sin definir todavía).
- Definición de ventana de tiempos e intervalos — **Watermarking** (uso del campo `LastProcessedTimestamp` para garantizar continuidad del procesamiento) y **Lookback Window** (ventana con traslape).
- Upsert e idempotencia en el cache (para que reprocesar una ventana no duplique datos).
- Formato JSON de salida de la API de consulta.
- Catálogo de consultas KQL (Kusto Query Language, consistente con que la fuente es `ApiManagementGatewayLogs` de Azure APIM), variables y parámetros.

Pablo Gomes confirmó recepción y lo sumó "al tablero para hacer los requerimientos al equipo en base a esto" (mail de respuesta, mismo día). Destinatarios directos del mail: equipo Kipi (mariano@, gaston.agusti@, juanpablo.carubelli@keepitsimple.com.ar); Pablo Gomes y Emma Vignoles en copia.

## Nota de adjuntos (pendiente)

El detalle técnico real (arquitectura completa, catálogo KQL, formato JSON) vive en los 3 adjuntos, no procesados automáticamente por esta skill. Si se necesita el detalle técnico fino para formalizar el requerimiento a Kipi (T-104, `tareas.md`), hay que abrirlos manualmente.
