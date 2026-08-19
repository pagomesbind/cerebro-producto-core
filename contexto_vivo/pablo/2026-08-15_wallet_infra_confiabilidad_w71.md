---
id: 2026-08-15_wallet_infra_confiabilidad_w71
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versiones W 71 (2026-07-15), W 71.2 FIX (tickets WS-1417/WS-1413), W 71.1 FIX (WS-1387/WS-1388)"
producto: wallet
tema: Infraestructura y confiabilidad — Redis, migración EasyNet, anti-affinity, WebhookSender a PROD
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/historial_confiabilidad_transferencias_y_comprobantes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: capturado
merge_commit:
---

Nueva sección "10. Infraestructura y confiabilidad — tramo W71 (jul-ago 2026)" a continuación de §9:

- **Errores de conexión a Redis en MS Comprobantes (WS-1280, W 71):** casos elevados en producción de `Connect to server timeout` contra `redis-bind-prd-001.redis.cache.windows.net:6380` (cache). Se abre análisis de causa raíz, sin cierre técnico documentado en el ticket — más bien un item de investigación que un fix puntual.
- **Migración a EasyNet del evento de transferencia entrante en MS BIND (WS-1387, W 71.1 FIX):** a raíz de un incidente el 2026-07-14 (POD de MS BIND con error `Channel unusable due to continuation timeout` de conexión a RabbitMQ, causado por mala gestión de MassTransit), se migra el evento `ProcesarTransferenciaEntranteEvent` a EasyNet — mecanismo que reintenta automáticamente en otro POD si el actual falla. **Deuda técnica reconocida:** la migración debería extenderse al resto del flujo de transferencias entrantes en MS Operaciones y MS Comprobantes (`BindWebHookTransferEvent`, `ComprobanteDeOperacionCreadoEvent`, `OperacionSinComprobanteEvent`) — todavía no migrados.
- **Anti-affinity en los MS de WalletOperaciones (WS-1417, W 71.2 FIX):** cambio de infraestructura desplegado junto con la versión 71.2 — distribuye los PODs de WalletOperaciones de forma más pareja entre nodos para evitar sobrecarga de puertos de un servicio en un mismo nodo. Riesgo/impacto bajo, ticket de origen Fintexa (INF-1401).
- **Relevamiento de pasaje a PROD de WebhookSender (WS-1298, W 71.2 FIX, generado por IA de análisis técnico):** documenta lo que efectivamente cambió al llevar `staging` a `main` (142 commits adelante / 22 detrás, contenido de staging superset de main). Cambios reales: migración runtime **.NET 6 → .NET 8**, el worker de Policy pasa de código embebido a paquete NuGet versionado (`Fintexa.Policy 8.0.16`), nuevo endpoint `POST /Webhooks/Async` (respuesta 202 + CorrelationId, publicación async a cola). **Colas Quorum quedan publicadas pero LATENTES** — el código las soporta pero la decisión fue no activarlas en prod todavía (`QueueType:quorum` solo en Development; activarlas después requeriría recrear las colas, no es cambio en caliente). **Deuda de seguridad heredada, no introducida por este pase** (de un `/freview` previo): SSRF en `UrlDestino` (CWE-918), logging de Body/Headers/Autenticación (CWE-532), entidad de dominio expuesta en `POST /Webhooks`, endpoints sin `[Authorize]`, JWT sin validar issuer/audience — sugerido abrir ticket de remediación P0. Sin cambios de base de datos.

**Ruido — solo registro, sin contenido de producto (config/logging/técnico puro):** WS-1309 y AD-774 (activar `SelfLog` de Serilog para diagnosticar por qué a veces no loguea — mismo Epic WS-564 infra, ver también nota en el log de AD 71.2 FIX (PNET)), WS-1413 (bump de nivel de log a Debug en MS Operaciones por alerta de capacidad de memoria de logs), WS-1364 (cambiar el consumo interno de la API de Feriados de vía APIM a IP interna directa, por errores de SSL y latencia — sin cambio de lógica), WS-1388 (reemplazar instanciación manual de `HttpClient` por factory en MS Operaciones — cambio técnico puro).
