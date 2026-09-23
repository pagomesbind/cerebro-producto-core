---
id: 2026-09-23_ardid_riesgo_performance_actualizacion_causa_raiz
pm: pablo
fecha_captura: 2026-09-23
fuente: "/sync_meetings — reunión \"Repaso Semanal líderes\" (11:00, minuta de Gemini, docId 1wqm-GkYBl7DzbzbH3hXaEQ6pLP2U7vwlA4alQCqx-j8), 2026-09-22"
producto: ardid
tema: Actualización del riesgo de performance de Ardid (persiste 1,5 semanas) — causa raíz atribuida a optimización de consultas de backend, sesión de revisión acordada
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Actualiza el item ya capturado `2026-09-21_ardid_riesgo_performance_afecta_ventas_coto_desa`** (en_cola, todavía sin merge al momento de esta captura) — mismo riesgo de negocio (problemas de performance de Ardid afectando la venta del servicio a Coto/Grupo DESA), con desarrollo nuevo un día después.

**Novedad (reunión "Repaso Semanal líderes", 22/09/2026):** Mariana Nadalin reportó que los problemas de performance en Ardid **persisten desde hace semana y media** — la descarga de reportes y las consultas de transacciones fallan intermitentemente. A diferencia de la reunión del 21/09 (donde Fintexa y Penta se derivaban mutuamente la responsabilidad, sin causa confirmada), esta vez Hernán Clarich (Arquitectura, Fintexa) **atribuyó el inconveniente a la optimización de consultas en el backend y de recursos** — una causa técnica más concreta que el desvío de responsabilidad reportado el día anterior, aunque no se detalla si esto zanja o no la disputa Fintexa↔Penta.

**Acción concreta acordada:** Emma Vignoles instruyó a Mateo Capitanich (Fintexa) cargar el ticket de la actualización a la versión 19.1 en staging (ver decisión `2026-09-23_ardid_decision_salto_directo_version_191`) y revisar los tiempos de respuesta de las consultas, para evitar que la latencia de Ardid degrade la eficiencia de los pagos QR. Mateo Capitanich ofreció además realizar una sesión de trabajo con Mariana Nadalin para revisar específicamente el funcionamiento de la bajada de reportes en el frontend — sin fecha confirmada en la minuta.

**Estado:** sigue sin ticket formal de seguimiento ni fecha de resolución confirmada — el salto a la versión 19.1 es la principal palanca en curso, pero no está confirmado explícitamente en la minuta que resuelva el problema de performance reportado (son dos hallazgos relacionados pero no declarados como el mismo).
