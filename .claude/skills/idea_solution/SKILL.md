---
name: idea_solution
description: Produce el análisis técnico-funcional de la solución interrogando al PM en rondas — actores, orden de llamadas, contrato de integración, de dónde sale cada dato del request, camino feliz, caminos alternativos, flujos de error controlado, estados y decisiones de diseño. Se activa con /idea_solution.
when_to_use: Se activa cuando el usuario ejecuta /idea_solution, siempre después de que el problema esté enmarcado (/idea_problem) y antes de redactar el PRD — el PRD destila este análisis, no lo reinventa.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre del proyecto a diseñar]"
---

# 🧩 ANÁLISIS TÉCNICO-FUNCIONAL DE LA SOLUCIÓN: /idea_solution

## Por qué existe esta skill

El PRD explica qué se construye y por qué; ninguna skill de la familia explica **cómo funciona**. Esa regla existe a propósito en `/idea_prd` (*"no prescribas implementación"*), pero el vacío que deja no lo llena nadie: `/idea_us` asume que existe *"un análisis de arquitectura/alternativas"* que ninguna skill produce, y termina inventando el detalle técnico historia por historia — sin ver el flujo completo, sin un contrato consolidado, sin una lista única de qué pasa cuando algo falla. Esta skill llena ese hueco: convierte "vamos a integrarnos con el proveedor X" en un diseño funcional verificable — quién llama a quién, en qué orden, con qué datos, y qué hace el sistema cuando algo sale mal.

No reemplaza el diseño de arquitectura de Ingeniería: no elige lenguaje, framework, esquema de base de datos ni topología de despliegue. Diseña el **qué pasa**, no el **con qué se construye**.

## Cuándo NO usarla

- El problema todavía no está enmarcado o en discusión → usá primero [`/idea_problem`](../idea_problem/SKILL.md); este análisis asume un problema ya acordado.
- Ya existe un diseño de solución confirmado y lo que hace falta es el contrato fino de un endpoint puntual para una historia → usá [`/idea_ac`](../idea_ac/SKILL.md) sobre esa historia, no rehagas el análisis completo.
- Lo que se necesita es arquitectura de plataforma no ligada a un proyecto concreto (infraestructura, seguridad, NFR de sistema transversal) → eso es contexto de `wiki/3_recursos/arquitectura_sistema/`, se captura como item en `contexto_vivo/`, no en un proyecto puntual.

## ⚖️ Reglas duras

1. **Nada se inventa — todo dato técnico se cita contra su fuente.** Cada endpoint, campo, código de error y regla de validación sale de material real (`referencias/`, `3_recursos/detalle_productos/<producto>/apis_expuestas/`) o de una confirmación explícita del PM/proveedor registrada en la sesión. **Lo que no tiene fuente va a gaps o a un pedido de material, nunca al contrato.** Esta es la regla más importante de la skill: acá es exactamente donde una alucinación se convierte en un ticket de desarrollo mal especificado.
2. **Cada operación del contrato lleva su nivel de confianza:** `Confirmado` (documentado, con la fuente citada) · `Verbal` (dicho por el proveedor sin documento de respaldo) · `Supuesto` (hipótesis del PM, todavía a validar). Nunca dejar los tres mezclados sin distinguir — quien construye necesita saber cuánto puede confiar en cada dato.
3. **Los hechos son tu trabajo; las decisiones son del PM.** No le preguntes al PM nada que puedas resolver leyendo `referencias/`, la wiki o el material del proveedor — ya sabe que no lo sabe, lo que necesita es que se lo traigas resuelto. Y al revés: no cierres por tu cuenta una decisión de negocio o de alcance solo porque encontraste una opción razonable en la documentación — esa elección es del PM, aunque la sugieras.
4. **Cuando falte material, pedilo explícitamente.** Si un dato no está en el repo ni el PM lo tiene a mano, no lo supongas ni lo dejes como un gap mudo: convertilo en un pedido de material concreto — qué documento, a quién pedírselo, qué pregunta desbloquea, si frena el resto del análisis. Conseguir documentación de un proveedor externo suele tardar días; cuanto antes se identifique el pedido, menos tiempo se pierde después.
5. **Las flechas de todo diagrama nombran la operación real** (`POST /profile/customers`), nunca una descripción genérica ("crear persona"). Sin el nombre real de la operación, el diagrama es decoración, no especificación.
6. **Proporcionalidad, no ceremonia.** Esta skill corre siempre que hay un PRD en preparación, pero el documento escala con el problema real: una sección que no aplica a este proyecto se marca `No aplica — <razón en una línea>`, **nunca se omite en silencio** — la ausencia sin explicar es indistinguible de un olvido.
7. **Declarar todo lo que quedó sin leer.** Si hay un artefacto, adjunto, Swagger o PDF —en `referencias/`, en `artefactos/` propio o de un proyecto hermano— que no se abrió, decilo y registralo. Nunca se da por relevado lo que no se leyó, y nunca se le pregunta al PM algo que ya estaba escrito en su propia carpeta (ver Paso 0).
8. **El documento es siempre autocontenido** — sin links a la wiki, sin nombres de archivo o de skill, sin códigos de ticket usados como si el lector los reconociera, sin jerga de proceso interno. Va a manos de Ingeniería, QA y potencialmente del proveedor externo.
9. **Actualización in place, historial de revisiones al pie, cuerpo limpio** — si ya existe un análisis de una corrida anterior, se reescribe lo que cambió y se suma una entrada al historial, nunca se deja texto "actualizado"/"superado" incrustado en el medio.
10. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto y fuentes

El paso más importante de la skill: **nada de lo que ya se sabe se vuelve a preguntar.** Preguntarle al PM algo que ya está escrito en su propia carpeta es el peor resultado posible — le hace perder tiempo y le baja la confianza en las rondas que siguen. El barrido se hace en tres anillos, cada uno más amplio que el anterior.

**Anillo 1 — piso obligatorio, siempre, en el orden natural:**
1. Resolvé la ruta real en [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 — nunca asumas `prd-XXX_<slug>/` directo.
2. **`proyecto.md` completo** — incluidos el §5 historial de sync y el anexo de discovery de `/idea_start`. El orden de llamadas que dio un proveedor, o una decisión de arquitectura mencionada de pasada, suelen vivir únicamente ahí, sueltos en una entrada del historial de sync.
3. El problem statement (`{{nombre_corto_proyecto}}-problem.md`), si existe.
4. `decisiones.md` y `gaps.md` propios; si es miembro de un proyecto general, también el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre.

**Anillo 2 — inventario completo de artefactos, sin asumir qué existe.** Acá está el riesgo real: la carpeta puede tener material creado fuera del orden normal de la cadena, y la convención de nombres no lo predice.
- **Listá `artefactos/` entero y leé todo lo relevante**, no solo los archivos que la convención `{{nombre_corto_proyecto}}-<sufijo>.md` haría esperar. Incluye artefactos legacy con fecha en el nombre, formatos no-markdown (PDF, PPTX, HTML, specs OpenAPI/JSON), y tipos que la familia `idea_*` no produce pero que igual existen en la práctica — bases de reunión técnica, handoffs a QA, manuales de QA, corridas de test, estimaciones técnicas de un proveedor.
- **`artefactos/` del proyecto general padre**, si es miembro — ahí suelen vivir los análisis transversales a varios slices (arquitectura compartida, riesgos comunes).
- **`artefactos/` de proyectos hermanos** cuando el tema se cruza (mismo producto, mismo proveedor externo) — el análisis técnico más relevante para tu proyecto puede estar en la carpeta de otro. Consultá `index.md` §2 para identificar hermanos por producto antes de descartar esta fuente.
- **`referencias/`**: el `index.md` **y el material crudo mismo**, no solo su descripción. Lo voluminoso (Swagger, PDF largo, hilo de mail extenso) se despacha a un subagente que devuelva lo relevante — no se lee entero inline.

**Anillo 3 — contexto de producto y canon:** `3_recursos/detalle_productos/<producto>/` y su `apis_expuestas/` → `arquitectura_sistema/` → `cumplimiento_normativo/` si el proyecto toca reportería o PLD → `contexto_vivo/index.md` (citando explícitamente lo que hay ahí como no-canon todavía). Si ya existe `{{nombre_corto_proyecto}}-solution.md` de una corrida anterior, leelo completo — esta corrida lo actualiza in place.

**Fechar y contrastar, no tomar por vigente.** Un artefacto encontrado no es verdad actual solo por existir — cruzalo con su fecha, con el historial de sync y con las decisiones posteriores. Un PRD congelado puede convivir con una versión más nueva; un análisis técnico anterior puede estar basado en una versión vieja de la documentación del proveedor y haber quedado superado por una confirmación posterior. Un dato viejo tomado como vigente hace tanto daño como uno inventado.

**Cerrar el Paso 0 mostrando el inventario.** Antes de la primera ronda, presentale al PM qué encontraste, qué leíste, qué quedó sin leer y por qué — así puede decirte "te falta tal cosa" antes de que gastes rondas preguntando algo que ya está resuelto.

### Paso 1 — Armar el árbol de diseño

El documento final tiene 12 secciones (ver más abajo), pero no son un checklist a completar en orden: son las **ramas de un árbol de diseño**, con dependencias reales entre ellas. No tiene sentido preguntar por flujos de error antes de que el contrato esté cerrado, ni por procedencia de datos antes de saber quiénes son los actores.

Instanciá las 12 ramas para este proyecto concreto y marcá el estado inicial de cada una: `resuelta desde fuentes` (ya tenés la respuesta, con cita) / `abierta` (es una decisión real del PM) / `bloqueada por material faltante` (necesitás algo que no tenés). Presentá este mapa al PM antes de la primera ronda de preguntas — le da la chance de corregir el encuadre completo antes de que inviertas rondas de interrogatorio sobre un enfoque equivocado.

Dependencias típicas entre ramas (ajustalas al proyecto real, esto es una guía, no una regla fija):

| Ronda orientativa | Ramas que se pueden abrir | Depende de |
|---|---|---|
| 1 | Alcance del análisis · Actores y sistemas participantes · Disparador y punto de enganche | — |
| 2 | Contrato de integración · Convivencia con lo existente | Actores resueltos |
| 3 | Mapa de procedencia de datos · Camino feliz | Contrato resuelto |
| 4 | Caminos alternativos · Errores y flujos de error controlado · Máquina de estados | Camino feliz resuelto |
| 5 | Decisiones de diseño y alternativas descartadas · NFR y operación · Gaps y reparto por equipo | Todo lo anterior |

Una pregunta cuya respuesta depende de otra todavía abierta pertenece a una ronda posterior, no a esta.

### Paso 2 — Rondas de interrogatorio (repetir hasta que la frontera quede vacía)

Corré el mismo método de [`/grilling`](../grilling/SKILL.md) sobre el árbol armado en el Paso 1: en cada ronda, tomá la **frontera** — toda rama cuyos prerequisitos ya están resueltos — y trabajala completa antes de pasar a la siguiente. Cada respuesta del PM puede reabrir ramas que dependían de ella (si decide "esto va por batch, no online", buena parte de la rama de procedencia de datos cambia) — recomputá la frontera después de cada ronda, no asumas que lo ya presentado sigue vigente.

La adaptación sobre `/grilling` puro: cada ronda no produce solo preguntas, produce **tres cosas**, porque en este dominio buena parte de lo que parece una pregunta en realidad ya tiene respuesta en algún lado:

- **✅ Resuelto desde fuentes** — lo que ya contestaste vos mismo, con la cita concreta (archivo + sección, o "Swagger, endpoint X"). No se lo preguntes al PM — presentáselo como hecho establecido para que lo confirme o corrija si está mal, no para que lo responda desde cero.
- **❓ Preguntas al PM** — solo lo que es genuinamente una decisión suya. Formato de `/grilling`: `❓ **Q1** - **<título>**: <pregunta>` seguido de `➡️ <tu recomendación>` en la línea siguiente. Nunca preguntes algo sin ofrecer tu mejor recomendación primero — le ahorra al PM tener que pensar la respuesta desde cero.
- **📄 Pedidos de material** — lo que no está ni en el repo ni en la cabeza del PM. Cada pedido dice qué documento hace falta, a quién pedírselo (el proveedor, otro equipo interno), qué pregunta del árbol desbloquea, y si es bloqueante para seguir o si el análisis puede avanzar en paralelo con ese punto marcado como pendiente.

Antes de escribir una pregunta, releé qué fuentes puede necesitar esa rama puntual (no todo el barrido del Paso 0 de nuevo — solo lo que esa rama toca) y agotalas primero. Si el material es voluminoso, despachá un subagente y seguí con el resto de la frontera mientras vuelve — no te bloquees esperando.

### Paso 3 — Consolidar el documento

Con la frontera vacía, volcá el árbol resuelto a las 12 secciones del template (Paso siguiente). Nada entra al documento final que no haya pasado por una ronda de esta skill o por una fuente citada del Paso 0 — si algo quedó como pregunta abierta o pedido de material sin resolver, va a la sección 12 (Gaps técnicos), no se completa con una suposición de último momento para no dejar la sección vacía.

### Las 12 secciones del artefacto

1. **Alcance del análisis y estado** — qué se diseña acá, qué queda deliberadamente fuera, y sobre qué versión de la documentación del proveedor se trabajó (fecha, cantidad de endpoints si aplica).
2. **Actores y sistemas participantes** — tabla: sistema/actor · rol en el flujo · dueño · quién construye. Nivel de detalle de un diagrama de contexto: quién existe, no cómo está hecho por dentro.
3. **Disparador y punto de enganche** — qué evento inicia el flujo, quién lo invoca, si es sincrónico, asincrónico o batch, y en qué punto exacto de un flujo ya existente se engancha esta solución.
4. **Contrato de integración** — por cada operación: método, URL, autenticación, headers, request y response reales, códigos de respuesta, idempotencia, ambientes, límites de rate limit, y el nivel de confianza de la regla dura #2.
5. **Mapa de procedencia de datos** — tabla por campo del request: `Campo | Origen (sistema/tabla/pantalla/derivado) | Transformación | Obligatorio | Qué pasa si falta`. Esta es la sección que resuelve la pregunta "¿de dónde sale la información?" — no la des por implícita en el contrato.
6. **Camino feliz** — diagrama de secuencia en Mermaid (`sequenceDiagram`) con la operación real nombrada en cada flecha, más los pasos numerados con un ejemplo concreto de request/response debajo de cada uno.
7. **Caminos alternativos** — cada rama de negocio que no es el camino feliz pero tampoco es un error (ej. "el recurso ya existe, entonces se actualiza en vez de crearse"), numerada igual que el camino feliz.
8. **Errores y flujos de error controlado** — tabla `E1..En`: condición · origen (transporte / regla de negocio / dato faltante) · cómo se detecta · acción del sistema · política de reintento y backoff si aplica · compensación o rollback si aplica · qué ve el usuario final · qué se loguea y qué dispara una alerta.
9. **Máquina de estados** — diagrama Mermaid (`stateDiagram-v2`) de la entidad principal del flujo: transiciones válidas, estados terminales, quién dispara cada transición.
10. **Convivencia con lo existente** — qué mecanismo actual se conserva tal cual, cuál se duplica temporalmente, y cuál se reemplaza — con la fecha o condición de corte si aplica.
11. **Decisiones de diseño, NFR y alternativas descartadas** — por cada decisión relevante: opción elegida, opciones descartadas y por qué, qué la invalidaría a futuro. Sumá acá volumetría, latencia esperada, ventanas horarias, observabilidad y retención **solo si el PM o el PRD ya los definieron** — no inventes SLAs que nadie pidió.
12. **Gaps técnicos, material pendiente y reparto por equipo** — todo lo que quedó como pregunta sin resolver o pedido de material sin responder (con severidad y si es bloqueante), y qué construye cada sistema o equipo involucrado.

### Paso 4 — Revisión final con el PM

**No se da por cerrado el documento en la primera consolidación.** Presentá el documento completo, no solo un resumen. Si el PM corrige algo — un actor que falta, un endpoint mal interpretado, un flujo de error que en la práctica funciona distinto — reescribí esa sección completa reflejando la corrección, nunca agregues una nota "corregido" superpuesta al texto viejo. Repetí el ciclo las veces que haga falta hasta el OK explícito del PM sobre el documento completo; cada vuelta suma una entrada al historial de revisiones, no un documento nuevo.

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md). Para calibrar la profundidad esperada de cada sección, mirá [`flujos_consolidado_tecnico.md`](../../../wiki/1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/artefactos/flujos_consolidado_tecnico.md) — el análisis técnico más completo ya producido en la casa (21 flujos con endpoints nombrados en cada flecha, errores E1–E6, máquina de 8 estados): es la vara con la que se mide si un análisis nuevo quedó a la altura o quedó corto.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (cifras y nombres ilustrativos).

## ✅ Checklist de calidad

- [ ] Toda operación del contrato de integración tiene fuente citada y nivel de confianza (Confirmado/Verbal/Supuesto)
- [ ] El mapa de procedencia de datos cubre todos los campos obligatorios del contrato
- [ ] Todo diagrama de secuencia nombra la operación real en cada flecha, nunca una descripción genérica
- [ ] Hay al menos un flujo de error por cada error conocido del proveedor o del sistema existente
- [ ] El material de `referencias/` y de `artefactos/` que quedó sin leer está declarado explícitamente, no omitido en silencio
- [ ] Cada pedido de material dice qué desbloquea y si es bloqueante
- [ ] Ninguna pregunta hecha al PM tenía su respuesta ya escrita en `proyecto.md`, el problem statement, o un artefacto propio o de un proyecto hermano
- [ ] Las secciones no aplicables dicen `No aplica — <razón>`, nunca faltan sin explicación
- [ ] La frontera del árbol de diseño quedó vacía — ninguna rama asumida en silencio
- [ ] El documento es autocontenido: sin links a wiki, sin nombres de archivo/skill, sin códigos de ticket, sin jerga de proceso interno
- [ ] El PM revisó el documento completo y dio su OK explícito (Paso 4) antes de darlo por terminado

## Paso 5 — Cierre estándar

1. **Persistir el entregable** en `artefactos/{{nombre_corto_proyecto}}-solution.md` — `{{nombre_corto_proyecto}}` es el nombre corto del proyecto: la carpeta misma si nació de `/idea_start`, o el `<slug>` después de `prd-XXX_` en carpetas legacy (sin fecha en el nombre del archivo — versión en el frontmatter + historial de revisiones al pie) dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde `proyecto.md`. **Si el archivo ya existe**, esta corrida lo actualiza: reescribí limpio el cuerpo con el estado vigente y sumá una entrada al historial de revisiones. No crear un archivo nuevo en paralelo.
2. **Decisiones de diseño confirmadas** → `decisiones.md` del proyecto (directo). Si es una decisión de contexto fijo (no específica de esta IDEA), capturala como item `tipo: decision` en `contexto_vivo/`.
3. **Gaps técnicos abiertos** → `gaps.md` de la IDEA/proyecto.
4. **Pedidos de material pendientes** → `wiki/1_proyectos/tareas.md` — son tareas reales del PM, con destinatario (proveedor/equipo) y la pregunta que desbloquean.
5. **Conocimiento reusable del proveedor** (ej. el resultado de destilar un Swagger completo) → item `tipo: conocimiento` en `contexto_vivo/` con `destino_propuesto: wiki/3_recursos/detalle_productos/<producto>/` — nunca escritura directa al canon.
6. **Índices:** tabla maestra de `wiki/1_proyectos/index.md` §2; `wiki/index.md` solo si cambió una sección de nivel PARA.
7. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
8. Siguiente paso sugerido: [`/idea_prd`](../idea_prd/SKILL.md) para destilar este análisis en el resumen que necesita el PRD.
