---
id: 2026-10-02_cumplimiento_bcra_anexo_b_cronograma_auditoria_ciclo_vida_software
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Revisión Pruebas QA', 2026-10-02 15:00, Drive docId 16r7p9ju0LLiqe6S0oU9t39Gl_kAbznyrvOB4njR8NUc"
producto: transversal
tema: BCRA auditará el ciclo de vida completo del software (Anexo B) — cronograma de 2 etapas y pedido de métricas estandarizadas
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/gestion_riesgo_tecnologia_seguridad_a7724.md
tipo_destino: actualizar
contradice: "no — complementa el archivo ya existente sobre Anexo B/Com. A7724 (conformación de Comités de TI/Seguridad en curso desde 2026-09-30/10-01) con el cronograma concreto de auditoría y el detalle de qué va a pedir el BCRA sobre ciclo de vida de software"
confianza: alta
estado: ingestado
merge_commit: c0d6964
---

**Contexto (reunión "Revisión Pruebas QA", Bind PSP + Fintexa, 2026-10-02):** Hernán Clarich (Fintexa, gobierno de tecnología/sistemas) confirmó que, a partir de ahora, el **BCRA audita el ciclo de vida completo del software hasta la puesta en producción**, incluyendo segregación de ambientes y trazabilidad de punta a punta — esto es parte del marco de Anexo B ya referenciado en `gestion_riesgo_tecnologia_seguridad_a7724.md` (Com. "A" 7724), no un requisito nuevo separado.

**Cronograma de 2 etapas:**
1. **Este año (2026):** el BCRA pide una "foto" del estado actual — qué procesos existen hoy, cuáles están en curso, y cuál es el gap de todo lo que falta regularizar. No es todavía una auditoría formal, es el primer relevamiento de scope.
2. **El año que viene (2027, sin fecha exacta):** inspección formal.

**Motivo adicional citado:** el BCRA viene mirando este proceso específicamente a raíz de un incidente ya reportado anteriormente (ocurrido en abril, según la minuta) — van a revisar de nuevo procesos de seguridad, gestión de vulnerabilidades y gestión de backlog, buscando "debilidades en la gobernanza y la gestión".

**Qué van a pedir — métricas de gestión:** cantidad y forma de los "baros" [sic, posible error de transcripción — podría referirse a "pasajes"/releases], cómo están segregados los ambientes, cómo son las pruebas, el ciclo de vida de punta a punta (incluye evolutivos). Esto alcanza también la relación con terceras partes (Fintexa como proveedor) — el BCRA pone foco especial en el control que Bind PSP ejerce sobre lo que delega a terceros. Matías Alzogaray (PM Bind) se compromete a presentar un primer boceto de métricas estandarizadas el viernes siguiente (2026-10-09), en paralelo con sus propias métricas de ciclo de ticket (tiempo desde asignación hasta cierre) y el trabajo ya en curso de equiparar story points entre el Jira de Bind y el de Fintexa.

**Nota de trazabilidad:** existe ya una tarea abierta de Pablo Gomes sobre este mismo tema — `tareas.md` T-161 (evaluar la planilla de 38 requisitos mínimos BCRA, insumo para el Anexo B) — este item aporta el cronograma de auditoría que faltaba (foto 2026 / inspección formal 2027) y la conexión explícita con el semáforo de riesgo de versiones (ver item de decisión de la misma reunión sobre registro formal de aceptación de riesgo, que alimenta directamente el "apetito de riesgo" que el BCRA va a pedir).
