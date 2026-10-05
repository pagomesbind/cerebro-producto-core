---
id: 2026-10-02_transversal_decision_semaforo_priorizacion_tickets_y_riesgo_formal
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Revisión Pruebas QA', 2026-10-02 15:00, Drive docId 16r7p9ju0LLiqe6S0oU9t39Gl_kAbznyrvOB4njR8NUc"
producto: transversal
tema: Semáforo de priorización de tickets por complejidad de prueba dentro de una versión + registro formal de aceptación de riesgo cuando se reduce el testing
tipo: decision
destino_propuesto: 2_areas/procesos/analisis_de_riesgo_de_despliegue.md
tipo_destino: actualizar
contradice: "no — complementa el semáforo de riesgo de despliegue general ya documentado en analisis_de_riesgo_de_despliegue.md con un criterio más granular (a nivel ticket, dentro de una versión ya cerrada), en respuesta directa al riesgo de regresión apresurada ya capturado el 2026-09-30 (item de la misma serie de reuniones 'Revisión Pruebas QA')"
confianza: alta
estado: en_cola
merge_commit:
---

**Contexto (reunión recurrente "Revisión Pruebas QA", Bind PSP + Fintexa, 2026-10-02):** en las últimas 4 semanas hubo entre 1 y 2 versiones semanales más tickets urgentes de negocio; en septiembre se gestionaron **16 pasajes a producción** (entre versiones y hotfix), de los cuales **14 requirieron pruebas exhaustivas** — evidencia cuantitativa de la alta carga operativa que ya había motivado el item de riesgo del 2026-09-30 sobre regresión apresurada en liquidaciones.

**Decisiones acordadas:**

1. **Semáforo de priorización de tickets dentro de una versión (rojo/amarillo/verde):** cuando una versión está cerrada y no alcanza el tiempo para testear todo con la misma profundidad, Matías Alzogaray (PM) se compromete a mediar con Comercial/Producto para indicar explícitamente **cuáles tickets son el compromiso real con el cliente** (deben pasar sí o sí con test completo) y cuáles pueden pasar con testing reducido — en vez de que QA decida esto sola por complejidad técnica. Mariela Marin (Fintexa) planteó que el criterio de prioridad no debería ser la complejidad de la prueba sino el compromiso de entrega al cliente (ejemplo citado: un bug de Portal FX en producción sin uso real de un cliente es menos crítico que un error en liquidaciones).
2. **Registro formal de la aceptación de riesgo:** cuando se decide pasar un ticket a producción con testing reducido (solo regresión, sin cobertura funcional completa de la contraparte), **debe quedar registrado explícitamente qué ticket se pasó con ese riesgo** — Hernán Clarich (Fintexa) remarcó que el problema no es tomar el riesgo en sí (nada es infalible) sino no dejarlo documentado: "cuando lo dejamos pasar sin registrar es un fantasma, no sabés qué hicieron". Esto alimenta además el "apetito de riesgo" que se le va a tener que reportar a la auditoría del BCRA (ver item de conocimiento sobre Anexo B de la misma reunión).
3. Independiente del semáforo de riesgo: **Melisa Belpassi (Fintexa)** prioriza la entrega de tickets a QA por **complejidad de prueba** (lo más complejo primero), dejando para el final lo que no requiere testing funcional de Bind. Andrea Orsini (QA, Bind) remarcó que esto ayuda pero no resuelve el problema de fondo: el equipo de QA suele estar todavía testeando la versión anterior (ej. Wallet) cuando llegan los tickets de la siguiente (ej. AD), por lo que no puede atacarlos aunque los tenga con anticipación — la solución pasa por organizar el *compromiso* del lado de Producto/Comercial, no solo por el orden de entrega de QA.

**Pendiente (no es un gap, es trabajo de proceso en curso):** Matías Alzogaray coordina con Daniel Romano (Fintexa) la definición de criterios del semáforo (reunión de 30 min a agendar) y una retrospectiva post-implementación de la versión 74.
