---
name: debrief
description: Cierre de trabajo de producto trabajado en conversación libre con el Cerebro (análisis puntual, discovery no estructurado). Destila ese contexto y lo alimenta al proyecto correspondiente en wiki/1_proyectos/ y al resto de la wiki. Nunca escribe en Jira.
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /debrief, típicamente al cierre (o en un checkpoint) de una sesión de conversación libre sobre una IDEA de producto.
disable-model-invocation: true
argument-hint: "[opcional: PRD-XXX o nombre del proyecto trabajado en la sesión]"
---

# 📝 DEBRIEF DE SESIÓN DE PRODUCTO: /debrief

## 🎯 Por qué existe esta skill

El PM trabaja sesiones de discovery y gestión con el Cerebro como copiloto: analiza problemas, define alcances, prepara comunicaciones, toma decisiones. Sin un cierre disciplinado, ese conocimiento muere en la conversación. `/debrief` es el mecanismo de captura: al invocarlo, el Cerebro repasa **todo lo trabajado en la sesión actual**, lo destila y lo persiste donde corresponde.

**Mantenimiento (2026-08-15):** `/sync_jira_ideas` se deprecó y eliminó — el barrido automático completo del tablero de Jira no tiene reemplazo todavía. Esta skill hereda dos responsabilidades que antes eran de esa skill, acotadas a los proyectos que efectivamente toca en cada sesión: (1) mantener actualizada la fila del proyecto en `wiki/1_proyectos/index.md` §2 (el resolver de rutas), emitiendo la novedad como item `tipo: iniciativa` en `contexto_vivo/`; (2) el flujo de cierre cuando una IDEA finaliza (ver Paso 1bis).

## ⚖️ Reglas duras

1. **Nunca escribe en Jira.** Todo va a la wiki. El PM decide aparte qué publica al equipo.
2. **Delta, no volcado:** antes de escribir, leé lo que el proyecto/archivo destino ya dice. Solo agregá lo nuevo de esta sesión. Nunca dupliques ni reescribas contenido existente.
3. **No inventes conclusiones:** si algo quedó a medio discutir en la sesión, va como gap o como próximo paso, no como definición.
4. **Fuente = la conversación actual.** No barras Jira ni Notion acá (eso es de las skills de sync) — salvo el fetch puntual de la IDEA base cuando falta (ver Paso 1.b).
5. **`2_areas/` y `3_recursos/` nunca se escriben directo.** Todo lo que exceda al proyecto (conocimiento generalizable, decisión de contexto fijo, gap fijo, tarea/oportunidad de todo el equipo) nace como item en `wiki/1_proyectos/contexto_vivo/` — ver Paso 3.

## 🏃 Pipeline

### Paso 0 — Identificar el proyecto

1. Si hay argumento (`PRD-XXX` o nombre), usalo.
2. Si no, inferilo del contexto de la sesión (sobre qué IDEA/tema se trabajó). Si la sesión tocó más de un proyecto, procesá cada uno.
3. Si es ambiguo, preguntá al usuario antes de escribir.
4. Si la sesión no está asociada a ninguna IDEA/proyecto (conocimiento general, procesos, análisis de área), salteá los pasos de proyecto y andá directo al Paso 3 con destino en `2_areas/` o `3_recursos/detalle_productos/` según corresponda.

### Paso 1 — Asegurar la carpeta del proyecto

a. Resolvé la ruta real leyendo la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 — nunca asumas `wiki/1_proyectos/prd-XXX_<slug>/` directo, esa ruta plana no existe desde la reforma del 2026-07-21. Si ya está trackeada, seguí al Paso 2.

b. Si NO existe (típico: **discovery propio del PM**, con o sin IDEA todavía en Jira — para eso está también [`/idea_start`](../idea_start/SKILL.md)):
   1. Resolvé el bucket: ¿es miembro de un proyecto general ya existente (el usuario lo asocia explícitamente, ver la tabla de §1 de `wiki/1_proyectos/index.md`)? Si no, nace como proyecto standalone de primer nivel.
   2. Creá la carpeta ahí con la estructura estándar: `proyecto.md` (10 secciones — usá [`proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/proyecto.md`](../../../wiki/1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/proyecto.md) como referencia de formato si es miembro de un proyecto general, o cualquier `prd-XXX_<slug>/proyecto.md` standalone si no) + subcarpeta `artefactos/`.
   3. Si tiene key de Jira, traé al menos el PRD base con `getJiraIssue` (campos explícitos — `summary`, `description`, `comment`, `status`, `assignee`; nunca `*all`). Si aún no tiene ticket, arrancá el proyecto solo con lo de la sesión.
   4. Registrala en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 y emití un item `tipo: iniciativa` en `contexto_vivo/` (proyecto nuevo = novedad).

c. **Si el usuario pide crear un proyecto general nuevo** (ej. "arranca un proyecto para X"), es la única vía de creación. Usá el template de 9 secciones (Cabecera, Resumen ejecutivo, Problema y contexto, Mapa de descomposición, Definiciones y decisiones heredadas, Riesgos y dependencias compartidos, Parking lot, Seguimiento PM, Notas de sesiones — ver [`proyecto-onboarding-estrategico/proyecto.md`](../../../wiki/1_proyectos/proyecto-onboarding-estrategico/proyecto.md) como referencia) y preguntá qué IDEAs existentes pasan a ser miembros (mudalas con `mv`, corrigiendo sus links relativos).

### Paso 2 — Destilar la sesión hacia el proyecto

Repasá la conversación completa. **Primero decidí la altitud del contenido:** si es específico de la IDEA trabajada, va al `proyecto.md` del miembro; si es una decisión de arquitectura transversal, un cambio de fase, o un riesgo que aplica a varios miembros, va al `proyecto.md` del **proyecto general** (padre) — no lo dupliques en el miembro, referencialo desde su §2bis "Encaje en el proyecto".

Volcá en el `proyecto.md` que corresponda:

- **Avances de discovery y definiciones** → en las secciones estructuradas que correspondan (problema/contexto, alcance, decisiones, seguimiento PM). Actualizá el resumen ejecutivo si la foto cambió.
- **Nota de sesión** → entrada nueva en "Notas de sesiones": `## Sesión YYYY-MM-DD — <tema>` con un resumen corto de qué se trabajó, qué se resolvió y qué quedó abierto. Es el diario del proyecto; las secciones estructuradas son el estado consolidado. No repitas en la nota lo que ya moviste a las secciones — referencialo.
- **Tasks de gestión y próximos pasos del PM** → sección "Seguimiento PM" (comunicaciones pendientes, definiciones a conseguir, áreas a coordinar, riesgos detectados). Marcá los que se completaron en esta sesión.

### Paso 3 — Rutear el conocimiento que excede al proyecto

Todo lo de acá **nace como item en `wiki/1_proyectos/contexto_vivo/`** (frontmatter completo, cuerpo trabajado, nunca resumido) — nunca directo en `2_areas/`/`3_recursos/`:

- **Conocimiento generalizable** (mecánica de producto, contexto de mercado, procesos, aprendizajes que sirven más allá de esta IDEA) → `tipo: conocimiento`, `destino_propuesto` en `wiki/3_recursos/detalle_productos/<producto>/` o el área de `2_areas/` que corresponda (leer índice del producto primero, integrar a archivo temático existente si aplica; nunca `<producto>/apis_expuestas/`, dominio exclusivo de `/sync_web`).
- **Decisiones confirmadas por el usuario, de contexto fijo** (no específicas de esta IDEA — esas quedan en la sección Decisiones del proyecto, directo) → `tipo: decision`, `destino_propuesto: 2_areas/direccion/decisiones.md`.
- **Dudas abiertas / contradicciones**: específicas de la IDEA trabajada → `gaps.md` del miembro (o del proyecto padre si cruza varios), **directo**; de contexto fijo, sin relación con el proyecto → `tipo: gap` en `contexto_vivo/`.
- **Riesgos generales del equipo** (no específicos de la IDEA trabajada — esos van directo a la sección de riesgos del `proyecto.md` correspondiente) → `tipo: riesgo`, `destino_propuesto: 2_areas/riesgos.md`.
- **Acciones/tareas del equipo de Producto** detectadas en la sesión → `wiki/1_proyectos/tareas.md` (personal, **directo**; dedupe primero; si están ligadas a un proyecto vivo, referenciarlas por ID desde su "Seguimiento PM"). Si la tarea es de interés de todo el equipo, sumá además un item `tipo: tarea_equipo`.
- **Candidatas a IDEA nueva** (oportunidad de producto que surgió en la sesión y todavía no tiene IDEA de Jira) → `tipo: oportunidad`, `destino_propuesto: 2_areas/direccion/oportunidades.md`. Cuerpo: oportunidad, producto, origen (`Sesión de trabajo (YYYY-MM-DD)`), señal de demanda, foco estratégico que alimentaría (o `—`). Nunca crea el ticket en Jira (regla dura 1).

### Paso 3bis — Cierre de una IDEA finalizada

Si en la sesión el usuario confirma que una IDEA/proyecto **finalizó** (llegó a producción, se canceló, o se pausa indefinidamente):

1. **Finalizada:** refrescá el `proyecto.md` con el estado final. Capturá un item `tipo: conocimiento` por cada pieza de conocimiento generalizable que deje (mismo criterio que el Paso 3), con `> Fuente: Proyecto <IDEA> "<título>", finalizado YYYY-MM-DD`. Capturá además un item `tipo: iniciativa` marcando `cierre: true` en el cuerpo, con SP estimado (de la IDEA) vs. real (si se conoce) y dónde quedó el conocimiento — el merge lo usa para agregar la fila en `3_recursos/datos/log_iniciativas_producto.md`. Movés vos mismo (directo, no vía merge) la carpeta completa a `wiki/4_archivos/proyectos_finalizados/` — si era miembro de un proyecto general, solo su carpeta, quitando su fila de la tabla de miembros del padre. Sacala de la tabla maestra de `1_proyectos/index.md` §2 y agregala a la lista de Finalizadas del §3.
2. **Cancelada:** mismo archivado a `proyectos_finalizados/` con nota de cancelación al tope del `proyecto.md` (por qué, qué aprendizaje queda). Sin merge de conocimiento. Item `tipo: iniciativa` con `cierre: true` marcado cancelado (sin SP en los totales).
3. **Pausada / stand by:** el proyecto queda en `1_proyectos/`, marcalo ⏸️ en el índice y en la cabecera de `proyecto.md`. No se archiva.

### Paso 4 — Consolidar artefactos

Todo entregable producido en la sesión (PRD, deck, spec, análisis, mockup, documento de trabajo) se guarda en `artefactos/` de la carpeta que corresponda a su altitud — la del miembro (`.../prd-XXX_<slug>/artefactos/`) si es específico de esa IDEA, o la del proyecto general (`proyecto-<slug>/artefactos/`) si es transversal a varios miembros (ej. un análisis de arquitectura, un doc de riesgos compartidos) — con nombre descriptivo y fecha si hay versiones (`YYYY-MM-DD_<nombre>.<ext>`), y se referencia desde la sección correspondiente de `proyecto.md`:

- Si el archivo se generó fuera de la carpeta (scratchpad, raíz, `outputs/`), movelo.
- **Excepción:** entregables NO asociados a ninguna IDEA/proyecto siguen yendo a `outputs/` como siempre.
- Al archivarse un miembro (Paso 3bis), solo su carpeta viaja a `wiki/4_archivos/proyectos_finalizados/` — los artefactos del proyecto general se quedan donde están, salvo que se archive el proyecto entero.

### Paso 5 — Cierre estándar

1. Actualizá la fila del proyecto en la tabla maestra de `wiki/1_proyectos/index.md` §2 (última actividad, estado si cambió) y, si hubo novedad real, emití el item `tipo: iniciativa` en `contexto_vivo/` (ver intro de esta skill).
2. **Integridad bidireccional:** si escribiste en un miembro, verificá que su fila en la tabla de §3.2 del `proyecto.md` padre (si tiene) siga describiéndolo bien. Si escribiste en el `proyecto.md` padre, verificá si algún miembro afectado necesita actualizar su §2bis "Encaje en el proyecto".
3. Regla de integridad de índices: solo aplica a lo que tocaste directo en `1_proyectos/` (índices locales de proyectos, `1_proyectos/index.md`). Los índices de `2_areas/`/`3_recursos/` los actualiza `/context_merge`. Regenerá `contexto_vivo/index.md` si capturaste items nuevos.
4. **Sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día — no lo ejecutes vos.
5. Cerrá con un resumen al usuario: qué se persistió y dónde, qué quedó como item de `contexto_vivo/` pendiente de merge, qué quedó como gap/próximo paso.
