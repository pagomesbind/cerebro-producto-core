---
name: idea_problem
description: Genera un problem statement — documento breve y acotado que enmarca un problema (qué, quién, por qué) con su medida e impacto cuantificados, usando /grilling para no cerrar hasta tener foco real y números. Se activa con /idea_problem.
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /idea_problem, típicamente al arrancar una IDEA/iniciativa nueva, cuando un proyecto se desvió de su intención original, o para comunicar prioridades a liderazgo antes de saltar a "cómo" resolver algo.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre del problema a enmarcar]"
---

<!-- Adaptado de product-on-purpose/pm-skills (define-problem-statement), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->

# 🎯 PROBLEM STATEMENT: /idea_problem

## Por qué existe esta skill

Es fácil saltar directo a "cómo lo resolvemos" sin haber acordado primero "qué problema estamos resolviendo, para quién, y por qué importa ahora" — o peor, quedarse con un problema tan amplio que cualquier solución "encaja". Un problem statement es un documento corto que fuerza ese orden: condensa el problema en una sola frase (qué, quién, por qué), usando Jobs-to-be-Done para llegar a la necesidad y la razón reales del afectado en vez de la primera respuesta superficial, y no se da por cerrado hasta tener un número que mida qué tan grave es hoy y qué impacto tiene resolverlo o no resolverlo — **antes** de comprometer a un equipo con una solución. Sirve de base para todo lo que viene después (discovery, PRD, roadmap).

Encaja como el segundo eslabón de la cadena de discovery de la casa: [`/idea_start`](../idea_start/SKILL.md) es la hoja en blanco (kick-off del proyecto); esta skill profundiza y cuantifica el **POR QUÉ** (el problema, pulido y con número); [`/idea_solution`](../idea_solution/SKILL.md) resuelve el **QUÉ** y el **CÓMO** (la forma de construirlo); `/idea_prd` consolida todo lo aprendido en el artefacto final.

## Cuándo NO usarla

- Ya se evaluó si el problema vale la pena atacarlo y con qué foco → eso ya lo resolvió [`/idea_start`](../idea_start/SKILL.md) en su Fase 1-2; esta skill no vuelve a abrir esa decisión, solo profundiza medida e impacto para el documento formal.
- Lo que hace falta es comparar y proponer distintas soluciones → eso es un solution brief, no un problem statement.
- El "problema" en realidad es un supuesto sin validar → primero hay que enmarcarlo como hipótesis y probarlo antes de comprometer un equipo (ver `../../../wiki/2_areas/gaps_y_preguntas.md`).

*(Estos son deslindes conceptuales, no apuntan a otras skills de la casa — si en el futuro se suman skills equivalentes para PRD, solution brief o hipótesis, se puede linkear acá.)*

## ⚖️ Reglas duras

1. **El enunciado del problema siempre entra en una sola frase** — "[Afectado] necesita [necesidad] porque [razón]". Si la frase prescribe una solución (una feature, una pantalla, un endpoint) o el afectado es genérico, el problema todavía no está acotado: se vuelve a la rama correspondiente del árbol, nunca se fuerza el cierre.
2. **Necesidad y Razón se exploran con la filosofía completa de Jobs-to-be-Done, no solo para armar una frase.** El job story ("Cuando [situación], quiero [motivación], para poder [resultado esperado]") es el punto de partida, no el final: la sesión también releva con qué compite hoy la solución (un workaround, "nada") y qué fuerzas empujan o frenan el cambio (ver Paso 1). Nunca preguntes directamente qué feature quiere — si el PO contesta con una, repreguntá la situación o el resultado esperado detrás.
3. **Nada de "usuarios" genérico.** El segmento afectado tiene que ser específico y accionable: "comercios adherentes dando de alta una cuenta", no "usuarios".
4. **La Medida del problema y el Impacto del problema llevan siempre un número.** Si falta el dato, la rama no se cierra con `[pendiente]` sin antes intentar conseguirlo: pedile al PO el dato concreto (volumen, tasa, costo, horas) y, si no lo tiene a mano, quién más podría tenerlo. Recién si ninguna de las dos vías resuelve el número, se documenta como pregunta abierta — "no sé" sin haber preguntado antes quién sabe no es una respuesta válida.
5. **No inventes conclusiones de negocio ni cifras.** Un número estimado por vos sin marcarlo como estimación ni citar de dónde sale es tan dañino como uno inventado.
6. **El documento es siempre autocontenido.** Es la previa a un documento que puede terminar en manos de alguien sin acceso a este sistema (liderazgo, otra área, un tercero) — sin links a la wiki, sin nombres de archivo o de skill, sin códigos de ticket (PRD-XXX) usados como si el lector los reconociera, sin jerga de proceso interno. Toda afirmación se explica en el propio texto.
7. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto antes de escribir

1. **Resolver la asociación a proyecto:** si el argumento o la conversación mencionan una IDEA (`PRD-XXX`) o un proyecto trackeado, resolvé su ruta real en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 (nunca asumas `1_proyectos/prd-XXX_<slug>/` directo) y leé su `proyecto.md` completo antes de empezar. Si es miembro de un proyecto general, leé también el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre. **Si ya existe `artefactos/{{nombre_corto_proyecto}}-problem.md`** de una corrida anterior, leelo completo — esta corrida lo actualiza in place (ver Paso 4 de cierre), no genera un documento nuevo en paralelo.
2. **Si el proyecto pasó por [`/idea_start`](../idea_start/SKILL.md):** releé el anexo de su Fase 1 (grilling del problema) en el `proyecto.md`. No repitas esas rondas de cero — arrancá el árbol del Paso 1 dando por resueltas las ramas que ya confirmó ahí (Afectado, Necesidad, Razón), mostrándolas en la primera ronda como "✅ resuelto desde `/idea_start`" para que el PO las confirme o corrija, y enfocá el interrogatorio en profundizar Medida e Impacto del problema — esa fase no llega a cuantificarlos a fondo.
3. Si el problema **no** está asociado a ningún proyecto trackeado, preguntá si esto arranca un discovery propio nuevo (en ese caso seguí el Paso 1.b de [`/debrief`](../debrief/SKILL.md) para crear la carpeta) o si es exploración suelta sin proyecto → el destino final es `outputs/`.
4. **Contexto de producto:** leé el overview del producto afectado en `wiki/2_areas/overview_productos/overview_<producto>.md` y, si hace falta profundidad, navegá desde `wiki/index.md` hacia `wiki/3_recursos/detalle_productos/<producto>/` (progressive disclosure — nunca cargar toda la wiki).
5. **Contexto de clientes:** si el problema involucra clientes concretos, leé sus fichas en `wiki/2_areas/clientes/`.
6. **Contexto estratégico:** consultá `wiki/2_areas/direccion/north_star.md` y `wiki/2_areas/direccion/decisiones.md` para saber si este problema ya conecta con un OKR o foco vigente.
7. Solo después de tener este contexto, arrancá el árbol del Paso 1 — nunca le preguntes al PO algo que la wiki ya responde.

### Paso 1 — Armar el árbol de diseño

El documento final tiene 6 secciones (ver Paso "Formato de salida"), pero no son un checklist a completar en orden: son las ramas de un árbol de diseño con dependencias reales — no tiene sentido cuantificar el impacto de negocio antes de saber quién es el afectado y qué necesita, ni fijar una meta antes de tener la medida actual.

Instanciá las ramas para este problema concreto y marcá el estado inicial de cada una: `resuelta desde fuentes` (ya tenés la respuesta, con cita) / `abierta` (es una decisión o un dato real del PO) / `bloqueada por dato faltante` (necesitás una cifra que no tenés). Presentá este mapa al PO antes de la primera ronda de preguntas.

**Las ramas Necesidad y Razón se arman con la filosofía completa de Jobs-to-be-Done, no solo el job story.** El objetivo no es llenar una plantilla de frase — es forzar que la sesión piense más allá de lo primero que dice el PO. Cubrí, en este orden:

1. **Job story** — situación (qué dispara el problema, en qué contexto aparece), motivación (qué está tratando de lograr el afectado, el "job" real) y resultado esperado (qué mejora espera si lo logra): "Cuando [situación], quiero [motivación], para poder [resultado esperado]".
2. **Alternativa actual** — con qué compite hoy la solución: un workaround manual, una planilla, un proceso tercerizado, un producto de la competencia, o directamente "nada" (el afectado convive con el problema). Casi siempre revela el verdadero tamaño y la verdadera naturaleza del problema — si el workaround tiene un costo medible (horas, plata, reintentos), alimenta la Medida del problema; si no, al menos matiza la descripción del Afectado.
3. **Fuerzas del cambio** — qué empuja al afectado a buscar algo distinto ahora (la situación actual que ya no tolera), qué lo atrae de resolverlo (la mejora que imagina), qué ansiedad le genera cambiar su forma de trabajar, y qué hábito o inercia lo mantiene en el status quo. Sin esto, el Impacto del problema queda sin urgencia real detrás — alimenta directamente el "por qué ahora".
4. **Resultado deseado medible** — la métrica que el propio afectado usaría para juzgar si mejoró, no solo la métrica de negocio elegida desde afuera. Esto es lo que ancla la Meta / criterio de éxito en el job real: la métrica primaria de esa tabla tiene que trazarse hasta acá, no aparecer de la nada en el Paso 1 de Meta.

Evitá que el PO conteste con una feature ("necesita un botón para X") en cualquiera de estos cuatro puntos: repreguntá la situación o el resultado esperado detrás de ese pedido, nunca lo tomes como la respuesta final. Alternativa actual y Fuerzas del cambio se preguntan en la misma ronda que el job story salvo que dependan de un dato todavía no resuelto.

Dependencias típicas entre ramas (ajustalas al problema real, esto es una guía, no una regla fija):

| Ronda orientativa | Ramas que se pueden abrir | Depende de |
|---|---|---|
| 1 | Afectado · Necesidad · Razón | — |
| 2 | Medida del problema | Afectado y Razón resueltos |
| 3 | Impacto del problema | Medida resuelta |
| 4 | Meta / criterio de éxito · Restricciones | Medida e Impacto resueltos |

Una pregunta cuya respuesta depende de otra todavía abierta pertenece a una ronda posterior, no a esta.

### Paso 2 — Rondas de interrogatorio (repetir hasta que la frontera quede vacía)

Corré el mismo método de [`/grilling`](../grilling/SKILL.md) sobre el árbol del Paso 1: en cada ronda, tomá la **frontera** — toda rama cuyos prerequisitos ya están resueltos — y trabajala completa antes de pasar a la siguiente. Cada respuesta del PO puede reabrir ramas que dependían de ella (si redefine quién es el afectado, la Medida que ya habías armado puede dejar de aplicar) — recomputá la frontera después de cada ronda.

La misma adaptación de tres baldes que usa [`/idea_solution`](../idea_solution/SKILL.md), porque acá también buena parte de lo que parece una pregunta ya tiene respuesta en algún lado:

- **✅ Resuelto desde fuentes** — lo que ya contestaste vos mismo (wiki, `/idea_start`, datasets de `wiki/3_recursos/datos/`), con la cita concreta. No se lo preguntes al PO — presentáselo como hecho establecido para que lo confirme o corrija.
- **❓ Preguntas al PO** — solo lo que es genuinamente una decisión suya (qué segmento priorizar, qué razón pesa más). Formato de `/grilling`: `❓ **Q1** - **<título>**: <pregunta>` seguido de `➡️ <tu recomendación>` en la línea siguiente. En las ramas Necesidad y Razón, la pregunta va en formato job story (situación / motivación / resultado esperado), nunca "¿qué necesitás?" a secas.
- **📄 Pedido de dato concreto** — el balde por default en las ramas de Medida e Impacto cuando no hay cifra en la wiki ni en los datasets: pedí el número puntual (volumen mensual, tasa de abandono, costo unitario, horas de soporte) y, si el PO no lo tiene a mano, a quién más se le puede pedir (otro equipo, un dashboard, el proveedor). La rama no se cierra con "no tenemos ese dato" sin haber hecho este pedido primero.

Antes de escribir una pregunta, releé qué fuentes puede necesitar esa rama puntual y agotalas primero. Si el material es voluminoso, despachá un subagente y seguí con el resto de la frontera mientras vuelve.

### Paso 3 — Redactar el enunciado

Con la frontera vacía, condensá el job story de Necesidad y Razón (situación, motivación, resultado esperado) junto con el Afectado en una sola frase: **"[Afectado específico] necesita [necesidad u outcome, no una solución] porque [razón: el dolor o la oportunidad que lo explica]"**. Si no entra en una oración sin perder claridad, o si al escribirla aparece una solución escondida, el problema todavía no está acotado — es señal de volver a alguna rama del Paso 1, no de forzar el cierre. El job story completo (situación → motivación → resultado esperado) queda disponible como respaldo del enunciado en el template cuando agrega claridad que la frase sola no capta.

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md). Un problem statement completo llena las 6 secciones: Enunciado del problema; Afectado; Medida del problema; Impacto del problema; Meta / criterio de éxito; Restricciones y preguntas abiertas.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (abandono en el alta de comercios de Adquirencia — cifras ilustrativas, no datos reales de Bind).

## ✅ Checklist de calidad

Antes de dar el problem statement por terminado, verificá:

- [ ] El enunciado entra en una sola frase y no prescribe una solución
- [ ] Necesidad y Razón vienen de un job story (situación / motivación / resultado esperado), no de un pedido de feature tomado tal cual
- [ ] Se relevó la alternativa/workaround actual del afectado (con qué compite la solución, aunque sea "nada")
- [ ] Se relevaron las fuerzas del cambio (qué empuja a resolverlo ahora, qué frena — hábito o ansiedad al cambio)
- [ ] El afectado es un segmento específico (no "todos los usuarios")
- [ ] La Medida del problema tiene un número real o un pedido de dato explícito registrado — nunca una suposición sin marcar
- [ ] El Impacto del problema está cuantificado, en negocio y/o áreas internas
- [ ] La Meta tiene baseline y target sobre la misma métrica de la Medida, con plazo, y esa métrica se traza hasta el resultado deseado del job story
- [ ] Las preguntas abiertas y pedidos de dato sin resolver quedaron registrados
- [ ] El documento es autocontenido: sin links a wiki, sin nombres de archivo/skill, sin códigos de ticket, sin jerga de proceso interno

## Paso 4 — Cierre estándar

1. **Persistir el entregable:**
   - Si está asociado a una IDEA/proyecto trackeado → `artefactos/{{nombre_corto_proyecto}}-problem.md` — `{{nombre_corto_proyecto}}` es el nombre corto del proyecto: la carpeta misma si nació de `/idea_start` (sin prefijo `prd-XXX`), o el `<slug>` después de `prd-XXX_` en carpetas legacy (sin fecha en el nombre del archivo — versión en el frontmatter + historial de revisiones al pie) dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde `proyecto.md` (secciones "Problema y contexto" y "Seguimiento PM"). **Si el archivo ya existía**, esta corrida lo actualiza: reescribí limpio el estado vigente y sumá una entrada al historial de revisiones — no crear un archivo nuevo en paralelo.
   - Si no está asociado a ningún proyecto → `outputs/<tema_corto>-problem.md`, con el mismo criterio de actualizar in place si ya existe uno sobre el mismo tema.
2. **Decisiones confirmadas por el PO durante la sesión** → `decisiones.md` del proyecto si son específicas de él (directo); item `tipo: decision` en `contexto_vivo/` si son de contexto fijo.
3. **Preguntas abiertas y pedidos de dato sin resolver del Paso 2** → `gaps.md` de la IDEA/proyecto (severidad según impacto) si son específicos de él (directo); item `tipo: gap` en `contexto_vivo/` si son de contexto fijo.
4. **Índices:** actualizá `wiki/1_proyectos/index.md` (última actividad) si hay proyecto; `wiki/index.md` solo si cambió una sección de nivel PARA.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
6. Siguiente paso sugerido: [`/idea_solution`](../idea_solution/SKILL.md) para diseñar cómo funciona la solución antes de redactar el PRD, o `/debrief` si el trabajo de esta sesión excede el alcance del documento.
