# Proceso de Publicaciones Mensuales — Ceremonias Clave

> Contenido completo transcrito desde `wiki/3_recursos/conocimiento_interno/proceso/proceso_publicaciones_mensuales.md` (ingesta original), reubicado desde `detalle_productos/transversal/procesos_internos.md §1` en la reestructuración PARA en cascada (2026-08-12) — es un proceso interno del equipo, no conocimiento de producto.

A continuación se describen las ceremonias clave a llevar a cabo por cada versión mensual.

## Cierre de alcance

**Fecha:** Segundo lunes de cada mes.

**Objetivo:** Acordar el alcance propuesto de la versión a publicar a fin de mes.

**Tareas del PM:**
- [ ] Crear la publicación principal del mes.
- [ ] Asignar a la versión del mes a todas las US y BUG que se encuentren en estado `FINALIZADO`, `CON DEFECTO`, `EN QA`, `EN CURSO` y que no tengan una versión asignada sin publicar.
- [ ] Analizar con Fintexa y con el negocio los tickets en estado `EN CURSO` asignados a la versión, cuyo esfuerzo por terminar es mucho y no se llegarán a entregar en una semana, y desasignarlos de la versión.
- [ ] Analizar con el negocio si hay que asignar a la versión tickets muy importantes (Prioridad Highest) que estén `LISTO PARA DESARROLLO`, `ASIGNADO` o `BACKLOG` y que no tengan una versión asignada sin publicar.
- [ ] Organizar meet con stakeholders internos (QA, PRODUCTO y OPERACIONES) y con los PM de Fintexa y facilitar la discusión y cierre del alcance.

## Corte de desarrollos

**Fecha:** Tercer lunes de cada mes.

**Objetivo:** Ajustar al alcance final de la versión.

**Tareas del PM:**
- [ ] Validar que todos los tickets dentro del alcance acordado están en estado `EN QA` o `CON DEFECTO` o `FINALIZADO`.
- [ ] Organizar meet con los PM de Fintexa y facilitar la discusión y cierre del alcance.
- [ ] Negociar qué hacer con los tickets del alcance acordado que aún siguen en estado `BACKLOG`, `ASIGNADO`, `LISTO PARA DESARROLLO` o `EN CURSO`. Por defecto, los tickets en este estado deben ser desasignados de la versión.
- [ ] Empezar seguimiento de tareas de QA asignadas al equipo (regresiones y test unitarios).

## Go / No Go

**Fecha:** Cuarto lunes de cada mes.

**Objetivo:** Evaluar aprobación del pasaje a producción de la versión.

**Tareas del PM:**
- [ ] Confirmar pasaje a producción de todos los tickets que están asignados a la versión del mes y están en estado `FINALIZADO`
- [ ] Negociar qué hacer con los tickets del alcance acordado que aún no están en estado `FINALIZADO`. Por defecto, estos tickets deben ser desasignados de la versión.
- [ ] Confirmar forma y fecha de pasaje a producción.
- [ ] Comunicar a Bind PSP sobre el pasaje a producción planificado.

## Pasaje a prod

**Fecha:** Martes y miércoles de la última semana de cada mes.

**Objetivo:** Pasar a producción la versión.

**Tareas del PM:**
- [ ] Monitorear pasaje y documentar el resultado.
- [ ] Si hubo algún problema o exepción durante el pasaje a producción, desasignar de la versión a los tickets que finalmente no fueron publicados.

## Ver también

- [gestion_jira.md](gestion_jira.md) — estados de ticket de desarrollo sobre los que operan estas ceremonias (`FINALIZADO` es el nombre real y único del estado terminal).
- [analisis_de_riesgo_de_despliegue.md](analisis_de_riesgo_de_despliegue.md) — informe de riesgo que se arma antes de cada despliegue, complementario a estas ceremonias.
- [requerimientos_al_equipo_tecnico.md](requerimientos_al_equipo_tecnico.md) — cómo entra un pedido al backlog que luego pasa por este ciclo mensual.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/procesos_internos.md §1` (reestructuración PARA en cascada). Contenido sin cambios; corrección `HECHO`→`FINALIZADO` ya aplicada en la fuente (2026-07-04).*
