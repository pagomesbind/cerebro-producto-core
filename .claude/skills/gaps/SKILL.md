---
name: gaps
description: Barrido diario de los gaps.md de todos los proyectos propios del PM en 1_proyectos/, para resolverlos interactivamente con el PO antes de que se acumulen. Por cada gap todavía abierto, hace una pregunta puntual con el tool de preguntas al usuario — si el gap en realidad es una tarea disfrazada (algo accionable, no una duda que se responde de memoria), ofrece migrarlo al backlog personal (tareas.md) en vez de forzar una resolución. Apto para scheduled action diaria L-V 9:00, antes de /sync_mails y /sync_meetings (9:30), para que ningún gap quede abierto más de un día.
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /gaps, o como scheduled action diaria de lunes a viernes a las 9:00.
disable-model-invocation: true
---

# 🧩 RESOLUCIÓN DIARIA DE GAPS DE PROYECTO: /gaps

## 🎯 Por qué existe esta skill

Los gaps de proyecto (vacíos de información, preguntas abiertas, contradicciones) se registran en el `gaps.md` del proyecto correspondiente — por discovery del PM, o por cualquier skill de sync (`/sync_mails`, `/sync_meetings`, etc., todas siguen el mismo protocolo del CLAUDE.md: gap específico de un proyecto → `gaps.md` de ese proyecto) — y ahí se quedan hasta que alguien los revisa a mano. `/gaps` cierra ese loop: corre una vez por día, encuentra todo lo que sigue abierto, y se lo pregunta al PO en el momento — así una duda queda abierta como máximo un día hábil.

**Es agnóstica de la fuente.** No le importa qué skill escribió el gap — solo lee `gaps.md`. Por eso no hace falta tocar `/sync_mails`, `/sync_meetings` ni ninguna otra skill para que esto funcione.

**Alcance estricto — solo gaps de proyecto, nunca de contexto fijo:**
- ✅ `wiki/1_proyectos/<proyecto>/gaps.md` y `wiki/1_proyectos/<proyecto>/prd-XXX_<slug>/gaps.md` (proyectos propios del PM).
- ❌ `wiki/2_areas/gaps_y_preguntas.md` (canon compartido, global del equipo) — no se toca.
- ❌ items `tipo: gap` en `wiki/1_proyectos/contexto_vivo/` — esos son del pipeline `/context_push` → `/context_merge`, con su propio ciclo de vida (`capturado` → `en_cola` → `ingestado`). Esta skill no los lee ni los escribe.

## ⚖️ Reglas duras

1. **Nunca inventar una resolución.** Si el PO no contesta o dice que no sabe, el gap queda abierto tal cual — se vuelve a preguntar mañana. No hay "auto-resolución" ni supuestos.
2. **Nunca escribir en `2_areas/gaps_y_preguntas.md` ni en `contexto_vivo/`** — fuera de alcance (ver arriba).
3. **Un gap, una pregunta.** No agrupar varios gaps en una sola pregunta aunque sean del mismo proyecto — cada uno tiene su propio contexto y su propia respuesta.
4. **Corrida rápida si no hay nada que preguntar:** si el barrido no encuentra ningún gap abierto, reporte de una línea y fin — no hay que forzar interacción cuando no hace falta.
5. **Dedupe con `tareas.md`:** antes de crear una tarea nueva por migración, revisar que ese gap no haya sido migrado ya en una corrida anterior (buscar su referencia en `tareas.md`).

## 🏃 Pipeline

### Paso 1 — Descubrir gaps abiertos

1. Leer [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §1 y §2 para enumerar todas las carpetas de proyecto propias del PM — buckets top-level y sus slices (`prd-XXX_<slug>/`). Nunca asumir una ruta fija.
2. Sobre esa lista, buscar un `gaps.md` en cada carpeta (proyecto padre y cada slice pueden tener el suyo).
3. En cada `gaps.md` encontrado, parsear las entradas `## [YYYY-MM-DD] — <emoji opcional> <título>`. Una entrada está **abierta** si no tiene una línea final `**Estado:** ✅ Resuelto...` (o equivalente ya cerrado, ej. "reclasificado"). Si la tiene, está cerrada — ignorarla.
4. Si no hay ninguna entrada abierta en todo el barrido → reportar `"Sin gaps pendientes en ningún proyecto — <N> proyectos revisados"` y terminar. No hace falta ninguna pregunta.

### Paso 2 — Triage: ¿duda real, o tarea disfrazada de gap?

Para cada gap abierto, antes de preguntar, clasificar leyendo su "Pregunta para el usuario":

- **Duda/inconsistencia genuina** — el PO puede responderla ahora mismo con su propio criterio: una decisión a tomar, una ambigüedad a resolver, una contradicción a zanjar entre dos fuentes. Ejemplo real ya visto en el Cerebro: *"¿Cuál de las 3 alternativas se definió en la reunión...?"*.
- **Tarea disfrazada de gap** — la pregunta en realidad describe un trabajo pendiente y accionable: hay que ir a buscar un dato externo, pedirle algo a un proveedor, coordinar con alguien, hacer un research. El PO no la puede "contestar" de memoria ahora — alguien tiene que salir a hacer algo. Ejemplo real ya visto en el Cerebro (`proyecto-onboarding-estrategico/gaps.md`, gap "Sin costo documentado de Legajo Digital..."): *"¿Podés conseguir el costo real de cada opción...?"* — terminó reclasificado como tarea (`tareas.md` T-002).

Esta distinción ya está en uso manual en el Cerebro (ver `gaps.md` de `proyecto-onboarding-estrategico`, entradas "reclasificado de gap a tarea" y "reclasificado de gap a alcance") — esta skill la aplica de forma sistemática y diaria en vez de esperar a una sesión de resolución manual.

### Paso 3 — Preguntar, uno por uno

Orden: severidad Alta → Media → Baja: dentro de cada severidad, gap más viejo primero.

Para cada gap, usar el tool de preguntas al usuario (una pregunta por gap, nunca agrupadas):

- **Si es duda genuina:** la pregunta es la propia "Pregunta para el usuario" del gap, con el contexto mínimo necesario (proyecto, fecha de detección, descripción resumida). Si el texto del gap ya sugiere 2-3 resoluciones plausibles, ofrecerlas como opciones — siempre queda disponible la opción de respuesta libre del propio tool para lo que no encaje.
- **Si es tarea disfrazada:** la pregunta ofrece explícitamente tres caminos — *"¿Resolvemos esto ahora, lo pasamos a tu lista de tareas, o lo dejamos abierto?"* con opciones: **Resolver ahora** (el PO de hecho tiene la respuesta a mano) / **Pasar a tareas** (es trabajo pendiente, no una duda) / **Dejar abierto** (todavía no, se pregunta de nuevo mañana).

### Paso 4 — Escribir el resultado

**Si se resolvió (duda genuina o "resolver ahora" de una tarea disfrazada):** en el mismo `gaps.md`, debajo de la entrada, agregar:
```
- **✅ Actualización (YYYY-MM-DD) — resuelto: <resumen fiel de la respuesta del PO>**
**Estado:** ✅ Resuelto — <cómo/por qué, en una frase>
```
Si la respuesta abre además una decisión de proyecto (no solo cierra el gap), registrarla también en el `decisiones.md` del mismo proyecto — escritura directa, nunca vía `contexto_vivo/` (regla del CLAUDE.md).

**Si se migró a tarea:** dos escrituras, ambas directas (nunca vía `contexto_vivo/`):
1. En `gaps.md`, debajo de la entrada:
   ```
   - **✅ Actualización (YYYY-MM-DD) — reclasificado de gap a tarea:** <por qué es tarea y no duda>. Agregada a `1_proyectos/tareas.md` (T-NNN).
   **Estado:** ✅ Resuelto como gap — sigue pendiente como tarea (ver `tareas.md` T-NNN)
   ```
2. En [`wiki/1_proyectos/tareas.md`](../../../wiki/1_proyectos/tareas.md), nueva fila (o actualizar si ya existe por dedupe — regla dura 5): ID correlativo `T-NNN`, la tarea redactada en modo accionable, interesados (`Pablo Gomes (PO)` si es propia, más cualquier tercero que el gap mencione), urgencia heredada de la severidad del gap (Alta→🔴, Media→🟡, Baja→🟢), fecha detectada = hoy, fecha límite = `—` salvo que el gap ya diera una, fuente = `"Sesión de resolución de gaps del proyecto <nombre>, YYYY-MM-DD (gap \`<ruta>/gaps.md\`)"` (mismo formato ya en uso, ver T-002/T-003), estado `Pendiente`. Si el proyecto tiene `proyecto.md` con sección "Seguimiento PM", referenciar la tarea por ID ahí también.

**Si se dejó abierto (explícito o por falta de respuesta):** no tocar el `gaps.md` — se vuelve a presentar en la corrida de mañana tal cual está.

### Paso 5 — Reporte de cierre

Reporte corto en terminal (no hace falta archivo en `outputs/`, es una corrida operativa breve):
1. Gaps resueltos hoy (proyecto + título, una línea cada uno).
2. Gaps migrados a tareas hoy (con su `T-NNN`).
3. Gaps que quedaron abiertos (proyecto + título) — para que el PO sepa qué sigue pendiente si no llegó a contestar todo.
4. Conteo total: `N revisados, R resueltos, M migrados a tareas, A siguen abiertos`.

### Cierre estándar

- No aplica la regla de integridad de índices (esta skill no crea ni mueve archivos, solo edita `gaps.md`/`tareas.md`/`decisiones.md` ya existentes).
- **Sin git.** El commit del repo personal lo sigue haciendo el hook `SessionStart`, una vez por día — esta skill no hace `git add`/`commit`/`push`.

## 📌 Notas operativas

- **Corrida scheduled sin el PO presente:** si la sesión se corta antes de terminar todas las preguntas (nadie contesta), los gaps ya preguntados con respuesta quedan escritos; los que no llegaron a preguntarse o quedaron sin respuesta simplemente se vuelven a intentar en la corrida de mañana — no hace falta ningún manejo especial de error.
- **Relación con el commit diario:** el snapshot del repo personal (`session_sync.ps1`) se dispara en el `SessionStart` de la primera sesión del día (throttle 24h), no a una hora fija. Programar esta skill a las 9:00 (antes que `/sync_mails`/`/sync_meetings` a las 9:30) es best-effort para que sea la primera sesión del día — no una garantía dura. Si algún día no lo es, el gap resuelto simplemente se comitea un día más tarde; no rompe nada.
- **No reemplaza el criterio del PO en discovery:** esta skill resuelve gaps ya registrados, no genera gaps nuevos ni reemplaza una sesión de discovery en profundidad (`/idea_start`, `/debrief`) cuando el tema lo amerita.
