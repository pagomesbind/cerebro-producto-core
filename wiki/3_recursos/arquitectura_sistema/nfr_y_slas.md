# NFR y SLAs Técnicos — Alta Disponibilidad

> Extraído el: 2026-07-02. Fuente: `Fintexa_Arquitectura_Software_v2.1.docx`, sección 10.2. Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §2.5-2.6` en la reestructuración PARA en cascada (2026-08-12). Ver nota de vigencia en [plataforma_y_stack_tecnologico.md](plataforma_y_stack_tecnologico.md).

## 1. Alta Disponibilidad

| Capacidad | Implementación |
|---|---|
| Réplicas mínimas | 3 pods para servicios críticos (BFF, Operaciones, Bind, Cuenta) |
| Health Checks | Liveness y readiness probes en todos los servicios, HealthChecks UI |
| Circuit Breakers | Polly policies para prevenir cascading failures |
| Backups | Snapshots diarios de bases de datos con retención de 30 días, geo-replication |
| Deployment | Blue-Green deployments con zero-downtime, automated rollback ante fallas |

## 2. SLAs Técnicos

| Métrica | Target | Medición |
|---|---|---|
| Uptime | 99.9% | Disponibilidad mensual end-to-end |
| Latencia P95 | <500ms | APIs críticas, percentil 95 |
| Throughput | 1.000 TPS | Transacciones por segundo sostenidas bajo carga normal |
| Error Rate | <0.1% | Porcentaje de requests fallidos sobre total procesado |
| Recovery Time | <5 min | Auto-recuperación ante fallas de pods individuales |

## 3. Exposición externa de salud/latencia a clientes — proyecto formal `salud_api_clientes/` (PRD-262), Gate 4 cerrado (2026-09-28)

> Fuente: reunión "Métricas APIM - vemos MVP de web?" (2026-09-10), minuta Gemini, con Fintexa/Kipi (Hernan Clarich, Juan Pablo Carubelli, Mariano Oscherov).

**Objetivo (Emma Vignoles):** que cualquier cliente pueda consultar la salubridad de las APIs de Bind PSP (uptime, latencia, tipo de error) de forma **100% transparente** — sin ocultar problemas de rendimiento —, cubriendo wallet, cobro y onboarding. Hoy el equipo tiene tableros de Grafana (armados hace unos meses) que muestran uptime (basado en tasa de respuestas ≥500 sobre el total, medido desde APIM) y latencia por API, con capacidad de abrir por producto/funcionalidad. Hernan Clarich (Fintexa) va a extender esto conectando Grafana también con Elastic (para cubrir servicios externos como Coelsa/APIBank, hoy fuera del tablero) y con un conector "Business Table" para consultar métricas de negocio directo desde tablas SQL.

**Se acordó separar en dos capas:** Grafana queda para consumo **interno** del equipo (monitoreo, alertas vía Telegram/Teams cuando se supera un umbral), y el equipo de Kipi (Juan Pablo Carubelli, Mariano Oscherov) va a construir un **servicio/API independiente**, publicado en el APIM, que exponga las mismas métricas a los clientes — con datos cacheados cada 60 segundos (no consulta en tiempo real contra Grafana/Elastic/APIM en cada request de cliente, para no saturar el sistema). Pablo Gomes pidió que la API quede segmentada por producto (un consumer por wallet, cobro, onboarding) para que cada cliente solo pueda consultar sus propias métricas sin necesitar credenciales de otra entidad, y que se evite exponer detalle tan fino que active alarmas por latencias puntuales explicables (ej. Botón Simple 1.0 de Ripsa, que es lento por diseño).

**Estado y próximos pasos:** Hernan Clarich va a producir la especificación técnica completa (alcance + arquitectura) para el equipo de Kipi. Pablo Gomes se comprometió a formalizar el requerimiento en el sistema de gestión de Producto, y Emma Vignoles a notificar a Fintexa (vía Seba) del trabajo planificado. Todavía no existe una IDEA de Jira para esta iniciativa a la fecha de esta captura (2026-09-10).

**Primera especificación técnica concreta (2026-09-24) — Etapa 1.** Hernán Clarich (Fintexa) envió la primera especificación técnica real, basada en estadísticas de APIM (`ApiManagementGatewayLogs`), con 3 adjuntos no procesados automáticamente (`API_Monitor_SLA_Blueprint.pdf`, `Resumen APIs Monitoreo.docx`, `Especificación Arquitectura monitoreo.docx` — pendientes de lectura manual, ver `2_areas/tareas.md` T-104). La especificación cubre un **Background Service Cache** (proceso que pre-calcula y cachea las métricas) y una **API de consumidor** para que clientes consulten disponibilidad/latencia del ecosistema. Puntos que Hernán deja explícitamente abiertos para refinar en conjunto con Pablo Gomes: tecnología de cache a utilizar; ventana de tiempos e intervalos (**Watermarking** vía `LastProcessedTimestamp`, y **Lookback Window** con traslape); upsert e idempotencia en el cache; formato JSON de salida; catálogo de consultas KQL (Kusto Query Language, consistente con la fuente APIM). Pablo Gomes confirmó recepción y lo sumó "al tablero para hacer los requerimientos al equipo en base a esto".

**Discovery formal de Producto cerrado (2026-09-25 a 2026-09-28) — MVP ampliado a terceros.** Este acuerdo técnico nunca había pasado por un discovery formal de Producto — nacía y vivía como nota de arquitectura. El proyecto `salud_api_clientes/` (`/idea_start`, PM Pablo Gomes) lo formalizó con los 4 gates confirmados:
- **Gate 1:** problema esencial confirmado — clientes con integración API directa no tienen forma proactiva de saber cuándo un producto está degradado del lado de Bind, incluyendo cuando la causa es un tercero.
- **Gate 2:** ✅ vale la pena ahora, pese a no encajar en ninguna NSM ni foco estratégico 2026 — sostenido en que el costo de oportunidad real es bajo (desarrollo externo vía Keepit Simple, no ingeniería interna).
- **Gate 3:** abanico de 4 carriles confirmado, incluyendo un carril operativo (formalizar el aviso proactivo de Soporte a clientes de alto volumen) como puente.
- **Gate 4 — el cambio de fondo:** el PM decidió que el MVP debe incluir la visibilidad de terceros (Coelsa, API Bank) **desde el lanzamiento**, no como la "Etapa 2" que Hernán/Keepit tenían planeada. Cita textual: *"El MVP debe comprender todo, incluyendo las externas. No podemos darle a un cliente una API que le diga que está todo bien, aunque Coelsa o el banco estén caídos. Nos matarían."*

IDEA de Jira: [PRD-262](https://bindpsp.atlassian.net/browse/PRD-262), en DISCOVERY.

**Mecanismo técnico de la cobertura de terceros confirmado (2026-09-28, Pablo Gomes ↔ Hernán Clarich):** lo que Hernán ya entregó a Keepit (basado en APIM/Azure Monitor) solo cubre el sistema propio de Bind. Para ver la salud de Coelsa/API Bank, Keepit necesita conectarse también a **Elastic Search** y leer las interacciones de **ingress/egress**; Hernán le pasa a Keepit las consultas de Elastic correspondientes. La conexión técnica en sí ("cómo") la resuelve Keepit junto con Infraestructura y Hernán — no se especifica ese detalle en las historias de usuario, solo el requisito funcional de cobertura. Tamaño/plazo de este desarrollo todavía sin dimensionar. Las alertas proactivas/webhooks (la Etapa 3 del roadmap original de Hernán) quedan explícitamente como candidato a un **proyecto futuro separado**, no parte de este MVP.

**Riesgo técnico identificado, sin resolver:** la definición de "uptime" ya especificada arriba (`ResponseCode 1-499 = éxito`) podría no capturar rechazos de negocio causados por un tercero caído — mismo riesgo de "placebo" señalado en la reunión del 2026-09-10. Queda como pregunta abierta para el análisis funcional-técnico (`/idea_solution`), no resuelta en el discovery.

## Ver también
- [infraestructura_cloud_azure.md](infraestructura_cloud_azure.md) — infraestructura que sostiene estos SLAs.
- [mantenimiento_y_capacidad_aks.md](mantenimiento_y_capacidad_aks.md) — plan de mantenimiento que puede impactar temporalmente estos targets.

---
*Última actualización: 2026-09-29 — `/context_merge`: §3 — discovery formal de Producto cerrado (`salud_api_clientes/`, PRD-262): MVP ampliado a cobertura de terceros (Coelsa/API Bank) desde el lanzamiento, mecanismo técnico confirmado (Elastic Search para ingress/egress), alertas proactivas quedan como proyecto futuro separado (Pablo Gomes).*
*Última actualización anterior: 2026-09-25 — `/context_merge`: §3 — primera especificación técnica concreta (Etapa 1, Hernán Clarich/Fintexa) del Background Service Cache y la API de consumidor de salud/latencia; puntos abiertos a refinar con Pablo Gomes (cache, ventanas de tiempo, KQL). 3 adjuntos técnicos pendientes de lectura manual.*
*Última actualización anterior: 2026-09-18 — `/context_merge`: nueva §3, iniciativa en discovery para exponer salud/latencia de APIs directamente a clientes (Grafana/Elastic interno + API nueva publicada por Kipi en el APIM).*
*Última actualización anterior: 2026-08-12 — Reubicado desde `arquitectura_sistema/seguridad_y_redes.md §2.5-2.6` (reestructuración PARA en cascada). Contenido sin cambios.*
