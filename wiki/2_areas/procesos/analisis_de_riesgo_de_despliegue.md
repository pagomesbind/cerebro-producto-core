# Proceso de Análisis de Riesgo de Despliegue

> Fuente: reuniones "Mati" (2026-06-22, coaching 1:1 Pablo Gomes↔Matias Alzogaray) y "Proceso PM" (2026-06-24), minuta Gemini. Formalizado a partir de estas sesiones y ya en uso en despliegues posteriores (confirmado semáforo verde/rojo aplicado en la reunión de riesgos de AD 70.2, 2026-07-02). Reubicado desde `detalle_productos/transversal/gestion_jira.md §1.8` en la reestructuración PARA en cascada (2026-08-12).

Antes de cada despliegue a producción, el Project Manager (Matias Alzogaray) arma un informe de riesgo con este esquema:

1. **Inventario de tickets de la versión**, clasificados por origen: soporte, pedidos internos, iniciativas técnicas, proyectos — en ese orden de prioridad de exposición.
2. **Clasificación por tipo:** corrección de error, nuevo requerimiento, u optimización.
3. **Semáforo de riesgo por ticket:**
   - 🟢 **Verde** — sin impacto funcional ni operativo.
   - 🟡 **Amarillo** — impacto operativo o de infraestructura (ej. performance, memoria, capacidad de base de datos), pero sin cambio de comportamiento visible al cliente.
   - 🔴 **Rojo** — impacto funcional que puede afectar a clientes externos o internos ya integrados (cambio de firma de API, de formato de respuesta, de comportamiento esperado) — requiere justificar explícitamente el impacto y evaluar si notificarlo.
4. **Filtro temporal:** solo se listan observaciones/errores heredados de versiones anteriores — las detectadas durante el QA de la propia versión en curso no entran al informe (se espera que se corrijan antes del pase).
5. **Reunión de riesgo:** con antelación mínima de 4 días hábiles (evitar convocatorias urgentes desordenadas). Asistentes obligatorios: PM de desarrollo, PM de Producto, líderes de área (Soporte/Fraude/Infra según aplique); Fintexa no necesita estar presente si ya entregó el análisis técnico preparado.
6. **Regla de decisión explícita del PM de Producto:** ante un ticket de bajo valor de negocio pero alto riesgo técnico (ej. actualizar el `Webhook Sender`, que puede cortar el envío de eventos a todos los clientes), se prioriza **no correr el riesgo** aunque eso implique demorar la publicación — "es más caro lo que se puede perder que lo que se puede ganar".

**Contexto de por qué nace:** el PM de Producto detectó baja confianza en la calidad de lo que se pasaba a producción (tickets de "dudosa procedencia", análisis técnico desactualizado en la descripción vs. lo realmente conversado) y decidió instituir este proceso en vez de depender del criterio caso a caso.

## ⚠️ Gap abierto — sin criterio explícito para decidir cuándo un ticket es hotfix

Este proceso cubre el semáforo de riesgo para tickets **ya incluidos en una versión** — no cubre el criterio para decidir si algo amerita salir de ese ciclo como excepción (hotfix urgente, fuera del ciclo mensual/quincenal).

En la reunión "Analisis de riesgo - Fix Contracargo" (2026-09-03, caso Ripsa — ticket AD1639, ver `clientes/casos_de_uso_clientes.md`) se generó un debate real y sin resolución formal sobre este punto. Nicolás Colón lo planteó explícitamente sin obtener respuesta cerrada: *"necesito entonces dónde dibujar la línea, qué parámetro tomar para determinar si algo es Hotfix o no"* — había levantado ese ticket como urgente por el reclamo de un cliente histórico, pero Andrea Orsini cuestionó en qué momento y con qué criterio alguien determina que algo es hotfix. Pablo Gomes sugirió como heurística consultar primero con el cliente si puede tolerar esperar hasta la próxima implementación antes de escalar como hotfix. En ese caso puntual no se trató de un hotfix improvisado (desarrollo terminado el día anterior, probado en staging la misma mañana, pasado en horario laboral por el canal normal) — pero eso resolvió el caso puntual, no la pregunta de fondo.

**Estado:** sin definición — quedó como heurística informal ("preguntarle al cliente si tolera esperar"), sin plasmarse como criterio del proceso. Ver también [gaps_y_preguntas.md](../gaps_y_preguntas.md) si se necesita trackear como pregunta abierta hacia el usuario.

**Propuestas en stand-by (2026-09-28, "MINUTA - Reunión de Pre-despliegue AD 73" del 24/09, minuta completa recibida recién el 28/09) — ninguna aprobada todavía:**

Esta misma minuta explica por qué se canceló el pase de AD V73 del 24/09, además de los errores de liquidaciones ya documentados en `publicaciones_mensuales.md`: entraron tickets de soporte y requerimientos de alta prioridad (BINes) a último minuto, hubo inestabilidad en staging, y el equipo no llegó a cerrar todos los tickets de la versión. Sumar tickets a una versión a pocas horas del pase sobrecarga a QA y obliga a reiniciar las regresiones. Muchos tickets marcados como defecto (sobre todo en Pagos FX) eran en realidad mejoras visuales o componentes despriorizados, no bloqueantes.

De ahí surgieron 3 propuestas, ninguna aprobada formalmente todavía:
1. **Comité de cambios** — revisar cómo se prioriza y definir si los requerimientos urgentes de último momento se tratan como **hotfixes externos** en vez de forzarlos dentro de un versionado ya encaminado. Es exactamente el criterio que le falta al gap de arriba.
2. **Tickets a QA con documentación completa** — que cada ticket llegue a QA con lo necesario para probarlo (endpoints, colección de Postman, etc.), para no perder tiempo buscando información.
3. **Filtro de observaciones de QA** — mejorar el criterio para separar rápido los bloqueos reales de las observaciones que son en realidad requerimientos nuevos o mejoras funcionales.

Acción relacionada (sin resultado conocido en esta fuente): Mariela Marin (Fintexa QA) tenía que evaluar para el 25/09 por qué las ejecuciones de tests previas no detectaron las fallas de liquidación.

## Ver también
- [gestion_jira.md](gestion_jira.md) — estados de ticket sobre los que se arma el inventario (§1).
- [publicaciones_mensuales.md](publicaciones_mensuales.md) — ceremonia de Go/No Go donde se usa este informe.

---
*Última actualización: 2026-10-01 — `/context_merge`: sumadas 3 propuestas en stand-by (comité de cambios, documentación completa a QA, filtro de observaciones de QA) al gap ya abierto sobre criterio de hotfix, desde la minuta completa de la reunión de pre-despliegue AD V73 (24/09) — con permiso explícito del usuario (Nicolás Colón).*
*Última actualización anterior: 2026-08-12 — Extraído como archivo propio desde `detalle_productos/transversal/gestion_jira.md §1.8` (reestructuración PARA en cascada). Contenido sin cambios.*
