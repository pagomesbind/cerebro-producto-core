---
id: 2026-09-25_conocimiento-v73-adquirencia-y-wallet-reprogramadas
pm: nicolas
fecha_captura: 2026-09-25
fuente: "Reuniones 'Reunión de Pre-despliegue AD 73' y 'W 73 - Impacto de temas' (2026-09-24) — resumen del mail de Gemini (Drive no disponible, sin minuta detallada); mail 'Re: Minuta: Análisis de riesgo: AD V 73' — Gonzalo Rivera (2026-09-24)"
producto: transversal
tema: Calendario de septiembre — AD V73 cancelada el 24/09 y reprogramada al martes 29/09 20:30; Wallet V73 corrida de 28/09 a "el 8" (probable 08/10)
tipo: conocimiento
destino_propuesto: 2_areas/procesos/publicaciones_mensuales.md
tipo_destino: actualizar
contradice: "2_areas/procesos/publicaciones_mensuales.md §Snapshot septiembre 2026: 'Adquirencia V 73: 24/09' y 'Wallet — versión 73: 28/09'"
confianza: media
estado: en_cola
---

Actualización del snapshot del calendario de despliegues de septiembre 2026 (sección "Confirmadas") — las dos V73 se corrieron.

**Adquirencia V73 — pase cancelado el mismo 24/09, reprogramado al martes 29/09 a las 20:30hs.**
- En la "Reunión de Pre-despliegue AD 73" (2026-09-24, tarde) se canceló el paso a producción previsto para esa noche. Motivos que registra la minuta: retrasos en el control de calidad, requerimientos que llegaron tarde, impacto de cambios de alcance sobre la carga del equipo, y **errores críticos detectados en liquidaciones**.
- Acuerdo formal: posponer el despliegue al **martes (29/09) a las 20:30hs**.
- ⚠️ Inconsistencia dentro de la misma minuta: la acción asignada a Gonzalo Rivera dice "notificar a los clientes el cambio de fecha del despliegue a producción para **el lunes por la noche**", mientras el resumen dice "martes a las 8:30 de la noche". No se puede resolver sin la minuta detallada — tomar el martes (acuerdo formal del resumen) como dato principal, a confirmar.
- **Evidencia adicional por mail (agregada por `/sync_mails` 2026-09-25) — refuerza "lunes 28/09":** en el hilo "Re: Minuta: Análisis de riesgo: AD V 73" (2026-09-24 17:03 ART, horas después de la reunión de pre-despliegue), Gonzalo Rivera le propone a Matías Alzogaray (resto del equipo en copia) el texto del aviso a clientes: *"AVISO DE IMPLEMENTACION - ADQUIRENCIA + AGENTE DE COBROS Y PAGOS"*, implementación el **lunes 28/09 a las 21:00hs**, con dos contenidos comunicables: (1) archivos de liquidación y PDFs — separación de desconocimientos (contracargos) y devoluciones con códigos distintos, más corrección de archivos y registros de liquidaciones; (2) correcciones en portal comercio — mejora en listados de transacciones y en creación de usuarios. Lo plantea como borrador ("si les parece lo mando"), sin confirmación de envío en el hilo. Con esto quedan **dos fuentes para lunes 28/09 21:00** (acción de la minuta + borrador de Gonzalo) contra una para martes 29/09 20:30 (resumen de la minuta) — sigue sin resolverse, pero el lunes gana peso. Nota: el aviso incluye también a **Agente de Cobros y Pagos**, no solo Adquirencia.
- Acciones de seguimiento acordadas: Andrea Orsini agiliza el cierre de tickets marcados con defecto con QA; Melisa Belpassi (Fintexa) reorganiza análisis funcional, tickets de infraestructura y scripts, revisa definiciones faltantes de tickets pendientes y corrige las observaciones antes del plazo del día siguiente; Matías Alzogaray y Gonzalo Rivera actualizan y validan el análisis de riesgos del despliegue y lo distribuyen por mail; Mariela Marin revisa las ejecuciones de test previas para entender por qué los fallos no se detectaron antes.
- Relevante para el ensayo de "ventana de despliegue anticipada" (`comunicacion_de_lanzamientos.md`, propuesta a probar con la v73): esta corrida de último momento es evidencia de que la v73 no se pudo sostener en la fecha comunicada.

**Wallet V73 — corrida de 28/09 a "el 8".**
- En "W 73 - Impacto de temas" (2026-09-24) se acordó **fijar "el 8" para el pase a producción de Wallet** (la minuta no dice el mes; por contexto —antes figuraba 28/09— es muy probablemente el 08/10). Motivo: retrasos de infraestructura que impiden cumplir las fechas previstas.
- Pablo Gomes informará al cliente una nueva fecha de lanzamiento "programada para el 12" (probable 12/10) — no queda claro en el resumen qué cliente/funcionalidad es (el snapshot listaba soporte de Getnet y alta de comitente recuperando de onboarding).
- Se hará una reunión de análisis de riesgo (25/09) para evaluar la viabilidad del pase el 8. Mariana Nadalin consultará a Mariano Varela el nivel de riesgo técnico de modificar los flujos de pago QR. Matías Alzogaray revisará las fechas de cierre de versión.
- Contexto técnico mencionado: "nuevos modelos de aceptadores requieren activaciones controladas" (sin más detalle en el resumen).

> Fuente: Reuniones "Reunión de Pre-despliegue AD 73" y "W 73 - Impacto de temas" (2026-09-24), resumen del mail de Gemini. Confianza media: sin acceso a la minuta detallada (conector de Drive invalidado en esta corrida).
