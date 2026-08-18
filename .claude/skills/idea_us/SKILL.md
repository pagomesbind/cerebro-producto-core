---
name: idea_us
description: Genera historias de usuario en formato persona/acción/beneficio a partir de un PRD o descripción de feature, con criterios de aceptación. Se activa con /idea_us.
when_to_use: Se activa cuando el usuario ejecuta /idea_us, típicamente después de aprobar un PRD, al armar el backlog de un sprint, o cuando hace falta comunicar alcance a ingeniería en formato de ticket.
disable-model-invocation: true
argument-hint: "[PRD-XXX o feature a descomponer en historias]"
---

<!-- Adaptado de product-on-purpose/pm-skills (deliver-user-stories), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->

# 📝 HISTORIAS DE USUARIO: /idea_us

## Por qué existe esta skill

Un PRD describe una iniciativa completa; una historia de usuario es la unidad de trabajo que un equipo puede estimar y entregar en un sprint. Esta skill descompone una feature ya especificada en historias chicas, independientes y con valor propio — sin perder de vista por qué le importa al usuario, que es lo que después ayuda a priorizar.

## Cuándo NO usarla

- Necesitás cobertura de criterios de aceptación mucho más profunda (Given/When/Then exhaustivo) para una sola historia o slice → usá [`/idea_ac`](../idea_ac/SKILL.md) sobre esa historia puntual.
- La feature todavía no está especificada → usá primero [`/idea_prd`](../idea_prd/SKILL.md); las historias tienen que trazar a requisitos ya documentados.

## ⚖️ Reglas duras

1. **Formato fijo:** "Como [persona], quiero [acción] para [beneficio]." La cláusula de beneficio no es opcional — explica por qué importa y ayuda a priorizar.
2. **Nunca "usuarios" a secas.** Cada historia es para una persona o rol específico.
3. **Sin detalles de implementación** en el enunciado de la historia — eso es del "cómo", no del "qué".
4. **Aplicá INVEST:** cada historia tiene que ser Independiente, Negociable, Valiosa, Estimable, Chica, Testeable. Si una historia no cumple, revisala antes de darla por terminada.
5. **El documento es siempre autocontenido.** Es la previa a un entregable que ingeniería, QA o un tercero van a leer sin acceso a este sistema — nunca links a la wiki, nombres de archivo o de skill, códigos de ticket usados como si el lector los reconociera, ni jerga de proceso interno ("según el gap...", "ver decisiones.md"). "Contexto y antecedentes" recapitula en prosa lo que el PRD u otro artefacto ya estableció, no lo linkea.
6. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto de la feature

1. Resolvé la ruta real de la IDEA en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2.
2. **Leé todo lo que ya existe antes de escribir una sola historia** — no alcanza con el PRD solo:
   - El PRD formal completo en `artefactos/` (todas las secciones: Problema, Solución, Definiciones, Funcionalidades, Riesgos, Flujos).
   - Cualquier documento de acceptance criteria ya redactado (`/idea_ac` previo) o análisis de arquitectura/alternativas asociado.
   - El `proyecto.md` del miembro completo (no solo el resumen ejecutivo) — Definiciones, Diseño técnico, Seguimiento PM, Historial de sync suelen tener detalle que el PRD todavía no absorbió.
   - Si es miembro de un proyecto general, el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre — las historias no deberían re-litigar una decisión de arquitectura ya cerrada a nivel proyecto.
   - Cualquier otro artefacto de la carpeta (`artefactos/`) que el PM haya referenciado en la sesión — diagramas, docs de validaciones de un proveedor externo, historial de bugs de un endpoint existente, etc. Estos suelen ser la fuente real del detalle fino que hace falta en el Paso 5.
3. Si no hay PRD asociado, confirmá con el usuario cuál es el alcance antes de escribir historias.
4. **Si ya existe `artefactos/historias_<tema>.md`** de una corrida anterior, leelo completo — esta corrida lo actualiza in place (ver Paso 8), no genera un documento nuevo en paralelo.

### Paso 1 — Entender el contexto de la feature

Revisá el PRD o la descripción de la feature. Entendé el objetivo general, los usuarios objetivo y los límites de alcance.

### Paso 2 — Identificar personas de usuario

Determiná qué usuarios interactúan con esta feature. Cada historia se escribe para una persona específica, no para "usuarios" genéricos — features distintas pueden necesitar historias distintas para la misma feature.

### Paso 3 — Descomponer por objetivo de usuario

Descomponé la feature en objetivos de usuario distintos. Cada historia debe entregar una capacidad completa y valiosa — algo que el usuario puede efectivamente hacer cuando la historia está terminada.

### Paso 4 — Escribir los enunciados

Formato: "Como [persona], quiero [acción] para [beneficio]."

### Paso 5 — Definir criterios de aceptación

Criterios específicos y testeables en formato Given/When/Then. Los criterios de aceptación definen "terminado" — si todos pasan, la historia está completa. (Para cobertura más profunda por historia, ver [`/idea_ac`](../idea_ac/SKILL.md).)

**Historias que describen un endpoint o contrato de API — nivel de detalle obligatorio.** Si la historia implica construir, modificar o consumir un endpoint, los criterios de aceptación tienen que llegar al nivel de detalle que necesitan QA e Ingeniería para no tener que volver a preguntar, cubriendo explícitamente:

- **Validaciones de cada dato del request** — formato, obligatoriedad, valores permitidos/catálogos cerrados, longitudes, caracteres especiales — no un AC genérico de "valida los datos", uno por cada campo o grupo de campos que lo amerite.
- **Ejemplos concretos de request y response en los criterios mismos** (no solo en Notas técnicas) — sirven para definir la UX de quien integra la API, no solo para que el desarrollador sepa qué construir. Si el payload real tiene muchos campos, alcanza con un ejemplo representativo por caso (éxito, error de validación, error de negocio) en vez de repetir el objeto completo en cada AC.
- **Códigos de respuesta HTTP explícitos** para cada desenlace (éxito, error de validación, error de negocio, recurso no encontrado) — no dejarlo implícito.
- **Validación de existencia y consistencia de recursos referenciados** — si el request trae un ID (`idCuenta`, `idSolicitud`, etc.), un AC cubre qué pasa si no existe, y otro si existe pero en un estado inconsistente para la operación.
- **Caminos no felices** — cada error de negocio o de validación conocido (rechazos del sistema externo, catálogos cerrados que no matchean, recursos incompletos) necesita su propio AC, no un genérico de "maneja errores".
- Si la historia consume un sistema externo (broker, proveedor), revisar si hay documentación de validaciones o historial de bugs ya ingerido en la wiki (`3_recursos/detalle_productos/`) antes de inventar el detalle — es la fuente más confiable de qué falla en la práctica.

### Paso 5bis — Revisión iterativa con el PM

**No se da por cerrado el documento en la primera pasada.** Antes de considerar el entregable terminado:

1. Presentá el documento completo al PM para revisión — es el estado por defecto, no un paso opcional.
2. Si el PM corrige una historia (dirección de un flujo, alcance, redacción, un AC mal planteado), reescribí esa historia completa reflejando la corrección — no parchear con notas "actualizado" superpuestas al texto viejo (ver regla general de artefactos: cuerpo limpio, historial de revisiones al pie).
3. Repetí el ciclo de revisión las veces que haga falta hasta que el PM esté de acuerdo con las redacciones — cada vuelta suma una entrada al historial de revisiones del documento, no un documento nuevo.
4. Recién con el OK explícito del PM se pasa al Paso 8 (persistencia + changelog) y, si el PM lo pide aparte, a la creación de tickets en Jira (ver regla dura de Jira más abajo — sigue siendo un paso separado y explícito, no automático).

### Paso 6 — Aplicar criterios INVEST

Validá cada historia contra INVEST: Independiente, Negociable, Valiosa, Estimable, Chica (Small), Testeable. Revisá las que no cumplan.

### Paso 7 — Agregar contexto y notas

Sumá referencias de diseño relevantes, consideraciones técnicas y dependencias que ayuden a quien implementa a entender el panorama completo.

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md). Por cada historia: Encabezado; Enunciado; Contexto y antecedentes; Criterios de aceptación; Notas de diseño; Notas técnicas; Dependencias; Fuera de alcance; Preguntas abiertas. En documentos multi-historia, cada historia anida estas secciones bajo su propio título (ver ejemplo).

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo.

## ✅ Checklist de calidad

- [ ] Cada historia sigue el formato "Como... quiero... para..."
- [ ] Las historias son independientes (se pueden construir en cualquier orden)
- [ ] Los criterios de aceptación usan formato Given/When/Then
- [ ] Cada criterio es testeable (se puede verificar pass/fail)
- [ ] Las historias son lo bastante chicas para completarse en un sprint
- [ ] No hay detalles de implementación en el enunciado
- [ ] La cláusula de beneficio explica por qué le importa al usuario
- [ ] Si la historia describe un endpoint/API: los AC cubren validaciones por dato, incluyen ejemplos de request/response, especifican códigos de respuesta y cubren caminos no felices (recurso inexistente/inconsistente, error de negocio)
- [ ] El PM revisó el documento completo y dio su OK explícito a las redacciones (Paso 5bis) antes de darlo por terminado

## Paso 8 — Cierre estándar

1. **Persistir el entregable** en `artefactos/historias_<tema>.md` (sin fecha en el nombre — versión en el frontmatter + historial de revisiones al pie, ver regla general de artefactos) dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde `proyecto.md`.
2. **Índices:** `wiki/1_proyectos/index.md`; `wiki/index.md` solo si aplica.
3. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
5. **Jira:** nunca crear tickets a partir de estas historias sin confirmación explícita del usuario, aunque el Paso 5bis ya haya cerrado con el OK del PM sobre el contenido — la creación en Jira es una decisión aparte que el PM tiene que pedir explícitamente. Si el alcance cruza más de un sistema/equipo (ej. dos proyectos Jira distintos), evaluá si corresponde partir una historia en dos — una por sistema — en vez de una sola historia con dependencias cruzadas de dueño ambiguo. Si el PM pide crear en Jira y no hay un Epic que agrupe las historias todavía, creá también el Epic (o un Epic por proyecto Jira involucrado) y asociá tanto el Epic como las historias a la IDEA, replicando el patrón de enlace ya usado por otras IDEAs del mismo Jira (revisar con `getJiraIssue` cómo está linkeada una IDEA hermana antes de asumir el tipo de enlace).
6. Siguiente paso sugerido: [`/idea_ac`](../idea_ac/SKILL.md) para profundizar criterios de una historia puntual, [`/idea_estimate`](../idea_estimate/SKILL.md) para cargar una estimación preliminar de SP por analogía histórica una vez que el PM dio su OK sobre las historias (Paso 5bis ya cerrado), o [`/idea_golive`](../idea_golive/SKILL.md) cuando el conjunto de historias esté listo para lanzar. Si alguna historia quedó fuera de alcance de desarrollo (ej. una carga de datos puntual/backfill), no la fuerces dentro del documento de historias — anotala como ítem del checklist de lanzamiento en vez de como historia de sprint.
