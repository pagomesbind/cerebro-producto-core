---
name: idea_golive
description: Genera y mantiene el checklist personal de go-live del PM — todas las tareas relevadas para poder activar un lanzamiento en producción (y las de seguimiento post-lanzamiento), siempre con el PM como responsable y un socio/interesado explícito por tarea. Se activa con /idea_golive.
when_to_use: Se activa cuando el usuario ejecuta /idea_golive — al acercarse un lanzamiento significativo o cross-funcional, y en corridas posteriores para revisar avance hasta el cierre del proyecto. No usar para un cambio chico de un solo equipo sin coordinación real entre áreas.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre del lanzamiento]"
---

# 🚀 CHECKLIST DE GO-LIVE: /idea_golive

## Por qué existe esta skill

Un lanzamiento significativo genera tareas repartidas entre ingeniería, QA, soporte, legal/cumplimiento, operaciones — pero quien tiene que velar que todas se resuelvan a tiempo, sin importar de qué área sean, es el PM. Esta skill no reparte responsables por área: junta en un único listado escaneable todo lo que el PM tiene que hacer o conseguir que se haga antes de (y después de) salir a producción, con quién lo tiene que resolver — el socio/interesado — en cada fila, para no perder un pendiente entre cinco checklists distintos.

## Cuándo NO usarla

- El cambio es chico y de un solo equipo, sin coordinación real entre áreas → trackealo directo como una tarea suelta en `tareas.md`, no hace falta un checklist propio.

## ⚖️ Reglas duras

1. **El responsable de toda tarea es siempre el PM.** Nunca "Ingeniería" o "Soporte" como responsable de una fila — si el trabajo lo ejecuta otra área, esa área es el socio/interesado de la tarea del PM ("conseguir que...", "coordinar con...", "confirmar con..."), no la dueña de la fila.
2. **Toda tarea lleva un socio/interesado explícito** — una persona puntual si se conoce, si no el área/equipo. Sin este dato la tarea no es accionable.
3. **Se listan todas las tareas relevadas para el proyecto, resueltas y pendientes.** Nunca se borra ni se archiva aparte una tarea ya hecha — se marca hecha (con fecha) y se conserva en el mismo listado, para que el checklist sirva también de registro de lo que se fue haciendo.
4. **Orden fijo: primero lo necesario para poder salir a producción (bloqueadores), después el resto de tareas importantes del proyecto** (seguimiento post-lanzamiento, cierres administrativos, deuda diferida que igual se quiere trackear). Dentro de cada grupo, pendientes y resueltas conviven — no hay una sección aparte de "hecho".
5. **Fuente obligatoria, nunca inventada desde cero:** todo bloqueador sale del Checklist operativo por área del PRD (filas "Tarea previa al go-live") y de los riesgos abiertos (tabla Riesgos del PRD + `riesgos.md` del proyecto). Si ninguno de los dos generó nada, decilo explícitamente en vez de inventar bloqueadores. **Áreas regulatorias (BCRA/UIF/PCI DSS) se relevan siempre**, aunque el lanzamiento parezca puramente técnico.
6. **Cada tarea del checklist es una fila de `wiki/1_proyectos/tareas.md`** (mismo ID `T-NNN`, mismo dedupe) — nunca un ID paralelo propio del checklist.
7. **Comentario en Jira: auto-post, sin pedir confirmación**, cada corrida con novedad real (mismo criterio que `/sync_mails`/`/sync_meetings`) — consolida el estado vigente **completo** del checklist, no solo el delta.
8. Todo output en español.

## 🔁 Esta skill no es la única que la mantiene al día

`/sync_mails` y `/sync_meetings` también actualizan este checklist: cuando encuentran una novedad sobre una tarea cuya fuente ya es un `-golive.md`, actualizan esa fila (mismo `T-NNN`) y repostean el comentario de Jira — sin esperar a que el PM corra `/idea_golive` de nuevo. Esta skill sigue siendo la única que arma el listado desde cero o lo reestructura a fondo.

## 🏃 Pipeline

### Paso 0 — Contexto del lanzamiento

1. Resolvé la ruta real en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2. Leé `proyecto.md`, el PRD asociado en `artefactos/`, `gaps.md`, `decisiones.md` y `riesgos.md` si existen. Si es miembro de un proyecto general, leé también el `proyecto.md` del padre.
2. **Si ya existe `artefactos/{{nombre_corto_proyecto}}-golive.md`** de una corrida anterior (propia o actualizada por un sync), leelo completo — esta corrida lo actualiza in place (ver Paso 8), nunca genera un documento nuevo en paralelo.
3. Filtrá `wiki/1_proyectos/tareas.md` por las tareas cuya fuente ya es este proyecto (incluidas las que vienen de una corrida anterior de esta misma skill) — son la base del Paso 3.
4. Si el lanzamiento involucra un proveedor externo (Fintexa u otro), revisá `wiki/3_recursos/arquitectura_sistema/` por dependencias conocidas.

### Paso 1 — Relevar bloqueadores de producción

Recorré, sin saltear ninguna fuente:

- **Checklist operativo por área del PRD** (las 7 áreas) — toda fila marcada "Tarea previa al go-live" en la columna "Qué proponemos" es un bloqueador.
- **Riesgos** (tabla del PRD + `riesgos.md` del proyecto) — todo riesgo abierto cuya mitigación depende de una acción concreta y pendiente, y cuyo impacto no es aceptable dejar para después del pase a producción.
- `gaps.md`/`decisiones.md` del proyecto — pendientes marcados explícitamente como condición de salida a producción.

### Paso 2 — Relevar el resto de tareas importantes del proyecto

Mismo barrido (checklist por área + riesgos + gaps/decisiones), pero para lo que el PM quiere seguir sin que bloquee el pase a producción: seguimiento post-lanzamiento, avisos a otras áreas, cierres administrativos (ej. una aprobación formal pendiente), deuda técnica diferida que igual conviene no perder de vista.

### Paso 3 — Revisar hacia atrás lo que ya estaba trackeado

Para cada tarea de `tareas.md` filtrada en el Paso 0.3 que sigue "Pendiente"/"En curso": ¿hay evidencia nueva (en esta sesión, en Jira, en un sync reciente) de que ya se resolvió? Si sí, marcala hecha con fecha. Si no hay evidencia en ningún sentido, preguntale al PM explícitamente al final de la sesión en vez de asumir que sigue pendiente — es exactamente el caso que esta skill existe para no perder: tareas anotadas como importantes de las que nadie se enteró si se resolvieron.

### Paso 4 — Asignar socio/interesado

Por cada tarea (nueva o ya trackeada), identificá la persona puntual si se conoce (revisá `2_areas/clientes/`, `proyecto.md`, reuniones/mails recientes del proyecto) o, si no, el área/equipo. Nunca lo dejes vacío.

### Paso 5 — Armar el listado único

Un solo listado por lanzamiento, sin secciones separadas de "pendiente"/"hecho": primero los bloqueadores de producción (Paso 1), después el resto (Paso 2) — dentro de cada grupo, tareas pendientes y ya resueltas conviven, cada una con su estado y su fecha si está hecha. Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md).

### Paso 6 — Sincronizar con `tareas.md`

Cada fila del checklist es (o reutiliza) una fila de `wiki/1_proyectos/tareas.md`: ID `T-NNN`, tarea, socio/interesado en la columna Interesados, fuente = este checklist. Dedupe primero — si la tarea ya estaba trackeada desde antes de esta skill, actualizá su fila en vez de duplicar.

### Paso 7 — Comentario en Jira

Posteá en la IDEA de Jira el estado vigente **completo** del checklist (ambos grupos, toda fila con su estado) — redactado como PM, no un volcado de la tabla cruda. Un comentario por corrida, consolidando toda la novedad. Cierre estándar: `— Registrado automáticamente por el Cerebro (checklist de go-live).` **Auto-post, sin pedir confirmación** (regla dura 7).

Instancia `bindpsp.atlassian.net`, cloudId `d07593ee-e5cd-4b6c-a371-d360063c167b`, IDEAs del espacio `PRD` (`addCommentToJiraIssue`; si la tool no está cargada: `ToolSearch query:"select:addCommentToJiraIssue"`).

## 📄 Formato de salida

Ver [`references/TEMPLATE.md`](references/TEMPLATE.md) y [`references/EXAMPLE.md`](references/EXAMPLE.md).

## ✅ Checklist de calidad

- [ ] Toda fila tiene al PM como responsable y un socio/interesado explícito (persona o área)
- [ ] Los bloqueadores de producción están arriba, separados del resto
- [ ] Están todas las tareas relevadas, resueltas y pendientes — ninguna se borró
- [ ] Todo bloqueador viene del checklist operativo por área o de los riesgos — ninguno inventado desde cero
- [ ] Las tareas ya trackeadas en `tareas.md` se revisaron hacia atrás antes de asumir que siguen pendientes
- [ ] Cada fila existe también como `T-NNN` en `tareas.md`
- [ ] El comentario en Jira se posteó sin pedir confirmación

## Paso 8 — Cierre estándar

1. **Persistir el checklist** en `artefactos/{{nombre_corto_proyecto}}-golive.md` — `{{nombre_corto_proyecto}}` es el nombre corto del proyecto: la carpeta misma si nació de `/idea_start` (sin prefijo `prd-XXX`), o el `<slug>` después de `prd-XXX_` en carpetas legacy (sin fecha en el nombre del archivo — versión en el frontmatter + historial de revisiones al pie) dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde `proyecto.md` (sección de entrega y seguimiento PM). **Si el archivo ya existía**, esta corrida lo actualiza: reescribí limpio el estado vigente y sumá una entrada al historial de revisiones — no crear un archivo nuevo en paralelo.
2. **Riesgos/bloqueadores detectados** que no tienen socio/interesado claro → `gaps.md` de la IDEA/proyecto; item `tipo: gap` en `contexto_vivo/` solo si son de contexto fijo, no del proyecto.
3. **Sincronización con `tareas.md`** ya hecha en el Paso 6 — acá solo verificá que ninguna fila del checklist quedó sin su `T-NNN`.
4. **Comentario en Jira** ya posteado en el Paso 7.
5. **Índices:** `wiki/1_proyectos/index.md`.
6. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
