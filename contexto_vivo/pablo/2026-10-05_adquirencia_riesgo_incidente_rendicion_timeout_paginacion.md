---
id: 2026-10-05_adquirencia_riesgo_incidente_rendicion_timeout_paginacion
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_mails — mail \"RE: Informe Semanal Adquirencia\" (threadId `19f716b9523ce741`, mensaje `1a0fe4998606d688`), Melisa Belpassi (Fintexa), 2026-10-02"
producto: adquirencia
tema: Incidente de timeout de paginación en Rendición — liquidaciones incompletas/NULL desde el 23/09
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no — riesgo nuevo, sin entrada previa en el canon sobre este incidente puntual"
confianza: alta
estado: ingestado
merge_commit: c0d6964
---

**Mecanismo:** a partir del 23/09/2026, la consulta de Rendición (microservicio `PaymentAcceptor.Rendicion`, que trae las transacciones de a 50 por página) empezó a superar el límite de 30 segundos en sus últimas páginas de consulta. El costo de procesamiento crece sobre la última página de la consulta al histórico de la tabla `Transacción` (a confirmar con el plan de ejecución) — no está relacionado con el volumen diario ni con el despliegue de la versión 73.

**Impacto:** al excederse el timeout, el proceso de Rendición interpretó que no había más transacciones y continuó, dejando liquidaciones incompletas o directamente en `NULL`, sin que se detectara en el momento. Ya ocurrió 3 veces: 23/09, 30/09 y 01/10. El 29/09 se sumó un problema adicional por un reinicio de la corrida con fecha en UTC, agravando el cuadro.

**Riesgo de pérdida de datos:** sigue abierta la posibilidad de pérdida de datos real el 23/09 (primera ocurrencia), todavía sin confirmar/descartar.

**Estado del plan de corrección (al 02/10, informe semanal de Adquirencia):**
- Cerrar los registros NULL pendientes.
- Revisar la posible pérdida de datos del 23/09.
- Establecer un control diario de contención.
- Plan de corrección en varios pasos: ajuste de la lógica de paginación, manejo de reintentos y alertas, optimización de índices y paginación por clave en la consulta, y evaluación de archivado del histórico (sujeto a validación).

Sin fecha de cierre confirmada a la fecha de esta captura.

> Fuente: mail "RE: Informe Semanal Adquirencia" (Melisa Belpassi, Fintexa), informe al 02/10/2026.
