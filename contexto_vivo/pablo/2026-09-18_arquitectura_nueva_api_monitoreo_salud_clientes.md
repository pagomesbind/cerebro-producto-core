---
id: 2026-09-18_arquitectura_nueva_api_monitoreo_salud_clientes
pm: pablo
fecha_captura: 2026-09-18
fuente: "/sync_meetings — reunión 'Métricas APIM - vemos MVP de web?' (2026-09-10), minuta Gemini, con Fintexa/Kipi (Hernan Clarich, Juan Pablo Carubelli, Mariano Oscherov)"
producto: transversal
tema: nueva API dedicada de salud/latencia expuesta a clientes, a partir de los tableros internos de Grafana
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/index.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## Qué se decidió

Emma Vignoles estableció el objetivo: que cualquier cliente pueda consultar la salubridad de las APIs de Bind PSP (uptime, latencia, tipo de error) de forma **100% transparente** — sin ocultar problemas de rendimiento —, cubriendo wallet, cobro y onboarding. Hoy el equipo tiene tableros de Grafana (armados hace unos meses) que muestran uptime (basado en tasa de respuestas ≥500 sobre el total, medido desde APIM) y latencia por API, con capacidad de abrir por producto/funcionalidad. Hernan Clarich (Fintexa) va a extender esto conectando Grafana también con Elastic (para cubrir servicios externos como Coelsa/APIBank, hoy fuera del tablero) y con un conector "Business Table" para consultar métricas de negocio directo desde tablas SQL.

**Se acordó que esto se separe en dos capas:** Grafana queda para consumo **interno** del equipo (monitoreo, alertas vía Telegram/Teams cuando se supera un umbral), y el equipo de Kipi (Juan Pablo Carubelli, Mariano Oscherov) va a construir un **servicio/API independiente**, publicado en el APIM, que exponga las mismas métricas a los clientes — con datos cacheados cada 60 segundos (no consulta en tiempo real contra Grafana/Elastic/APIM en cada request de cliente, para no saturar el sistema). Pablo Gomes pidió que la API quede segmentada por producto (un consumer por wallet, cobro, onboarding) para que cada cliente solo pueda consultar sus propias métricas sin necesitar credenciales de otra entidad, y que se evite exponer detalle tan fino que active alarmas por latencias puntuales explicables (ej. Botón Simple 1.0 de Ripsa, que es lento por diseño).

## Estado y próximos pasos

Hernan Clarich va a producir la especificación técnica completa (alcance + arquitectura) para el equipo de Kipi antes del viernes de la semana siguiente al 10/09 (Hernan está ocupado con informes de directorio/auditorías hasta el martes). Pablo Gomes se comprometió a formalizar el requerimiento en el sistema de gestión de Producto con esa información, y Emma Vignoles a notificar a Fintexa (vía Seba) del trabajo planificado. Todavía no existe una IDEA de Jira para esta iniciativa — es una novedad reciente sin ticket formal a la fecha de esta captura.
