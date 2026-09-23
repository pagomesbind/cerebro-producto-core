---
id: 2026-09-23_transversal_riesgo_fraude_inter_seguridad_informatica
pm: pablo
fecha_captura: 2026-09-23
fuente: "/sync_mails — mail 'MINUTA: Repaso Semanal líderes: Mar, 22 de sept de 2026' (threadId 1a0c9d3d2408a8b0), Matías Alzogaray, 2026-09-22, + respuesta de Hernán Clarich el mismo día; completado por /sync_meetings con la minuta de Gemini de la misma reunión (docId 1wqm-GkYBl7DzbzbH3hXaEQ6pLP2U7vwlA4alQCqx-j8), 2026-09-23"
producto: transversal
tema: Riesgo de fraude en el lanzamiento de INTER por volumen de altas — refuerzo urgente de seguridad informática, y ticket de infraestructura para destrabar el acceso de Penta a la Central de Prevención de Fraude
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

**Riesgo detectado en la MINUTA de Repaso Semanal líderes del 22/09/2026 (minuta directa de Matías Alzogaray, no Gemini):** el equipo identificó una necesidad crítica de reforzar la seguridad informática ante un alto riesgo de fraude en el lanzamiento de INTER — se registraron **7.600 altas en menos de 30 días**, un volumen que el TL;DR de la minuta describe explícitamente como "métricas alarmantes". Las acciones acordadas para mitigarlo: exigir todos los comprobantes de las operaciones y agilizar los bloqueos inmediatos de cuentas sospechosas. Ya se ejecutó una limpieza/depuración nocturna en las bases de datos de comprobantes y operaciones como primera medida.

**Completado con la minuta de Gemini de la misma reunión (2026-09-23):** Emma Vignoles detalló la cifra completa que motiva la alarma — del lanzamiento de INTER el 3 de septiembre, sobre **10.200 cuentas creadas, solo 100 realizaron alguna transacción**, y **7.600 de esas cuentas se dieron de alta antes de los 30 días** (es decir, antes del 22 de agosto) — la combinación de altísimo volumen de altas con actividad transaccional casi nula (0,98%) es la señal de riesgo de fraude que motiva las medidas del párrafo anterior. Emma Vignoles enfatizó además, sin acción puntual asignada en la minuta: priorizar seguridad informática, aplicar reglas estrictas, exigir el paso de todos los comprobantes, remediar las incidencias críticas de pruebas de penetración pendientes, y otorgar cuanto antes el acceso a la Central de Prevención de Fraude (ver ticket INF-1647 abajo).

**Ticket de infraestructura relacionado (misma minuta, respuesta de Hernán Clarich):** Hernán Clarich abrió el ticket [INF-1647](https://fintexa.atlassian.net/browse/INF-1647) para "desbloquear el proxy de infraestructura para dar acceso a Penta a la Central de Prevención de Fraude" — sin fecha límite definida todavía ("[DEFINIR FECHA LÍMITE]"). Esto es relevante para el gap ya capturado `2026-09-22_ardid_proyecto_asegurar_todo_pase_por_ardid` (proyecto de Nicolás Colón para que todo pase por Ardid, en QA) — Fintexa (Agustín Grau) había preguntado si el comportamiento pasa a fail-closed si Ardid cae, pregunta que sigue sin respuesta formal (ver T-116 de Pablo Gomes); este ticket de acceso de Penta a la Central de Prevención de Fraude parece ser un prerrequisito técnico para esa integración, corre en paralelo sin fecha límite.

**Otras decisiones de la misma minuta (contexto, sin riesgo asociado):** se priorizó el despliegue a producción de AD versión 73 (jueves 24/09) y de Wallet 73 (miércoles 30/09), posponiendo la regresión de la versión 65 de POS; se aprobó saltar directamente a Ardid versión 19.1, omitiendo la 19.0; se acordó eliminar la validación de bines desde el front-end.
