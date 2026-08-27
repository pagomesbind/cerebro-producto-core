---
id: 2026-08-27_arquitectura_repaso_semanal_zero_downtime_vs_sentinela
pm: pablo
fecha_captura: 2026-08-27
fuente: "/sync_mails — mail 'Repaso Semanal líderes: Mar, 25 de ago de 2026' (minuta directa de Matías Alzogaray por mail, no Gemini), 2026-08-25 (threadId `1a03a1edad15f8f1`)"
producto: arquitectura_sistema
tema: "Estado de despliegues Wallet 7.2/AuthExternal v2.0 + prioridad técnica pendiente: Zero Downtime vs. Sentinela"
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

## Repaso Semanal líderes (25/08) — despliegues confirmados + decisión de arquitectura pendiente

**Despliegues técnicos recientes confirmados como exitosos y sin reportes de problemas:**
- Versión **7.2 de Wallet** completada y desplegada.
- Migración de **AuthExternal a la versión 2.0** finalizada de forma limpia, sin reportes de incidentes — corrobora, desde una fuente distinta, el cierre de la migración ya capturado el 2026-08-26 vía `/sync_releases` (`2026-08-26_wallet_authexternal_v2_etapa3_cierre_migracion`).
- Pruebas en desarrollo de **Zero Downtime** (escalar/desescalar microservicios sin pérdida de mensajes) superadas con éxito.

**Decisión de arquitectura pendiente (Parking Lot, sin resolver todavía):** queda como decisión técnica central priorizar entre **Zero Downtime** (aplicarlo a microservicios críticos) vs. **Sentinela** (para resolver problemas recientes con comprobantes) — postergada a la reunión de Arquitectura del jueves siguiente (2026-08-27), donde también se iba a ejecutar el análisis post-mortem de un incidente ocurrido el viernes anterior (2026-08-21) — el Cerebro no tiene hoy detalle de ese incidente ni de a qué "problemas recientes con comprobantes" se refiere Sentinela; queda como punto a confirmar en el próximo barrido si hay minuta de esa reunión de Arquitectura.

**Prueba de carga de Wallet 7.2 (contexto ampliado para Juan Pablo Carubelli, dueño de la ejecución):** motivada por el aumento esperado de generación de comprobantes por la salida a producción de clientes de alto volumen — **Arcos Dorados** (septiembre 2026) y la futura integración de QR en los slots del **Hipódromo de Palermo**. Postergada dos veces (cierre de la versión 72, luego prioridad del propio despliegue), queda activa para ejecutarse la semana del 25/08 con métricas reales de producción (no cargas genéricas), foco en el comportamiento del sistema ante creación simultánea y masiva de comprobantes/vouchers.

**Otras decisiones operativas de la misma minuta, menores:**
- Onboarding jurídico La Virginia se integra directo al pipeline de QA del equipo (decisión nueva) — ver actualización directa en `1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md`.
- Ventana de mantenimiento nocturna (2:00-6:00) a coordinar con el DBA para eliminar comprobantes/operaciones pesadas — corrobora, desde otra fuente, la depuración periódica de bases ya capturada el 2026-08-21 (`2026-08-21_arquitectura_purga_bases_apibank_ventana_mantenimiento`).

> Fuente: mail "Repaso Semanal líderes: Mar, 25 de ago de 2026 a las 11:00am – 11:45am (GMT-03)", Matías Alzogaray, 2026-08-25 (minuta directa por mail, no la síntesis automática de Gemini que ya cubrió `/sync_meetings` el 2026-08-26 sin encontrar novedad de fondo en esta reunión).
