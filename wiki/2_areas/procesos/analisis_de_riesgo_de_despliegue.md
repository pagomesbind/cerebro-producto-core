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

## Ver también
- [gestion_jira.md](gestion_jira.md) — estados de ticket sobre los que se arma el inventario (§1).
- [publicaciones_mensuales.md](publicaciones_mensuales.md) — ceremonia de Go/No Go donde se usa este informe.

---
*Última actualización: 2026-08-12 — Extraído como archivo propio desde `detalle_productos/transversal/gestion_jira.md §1.8` (reestructuración PARA en cascada). Contenido sin cambios.*
