---
name: idea_start
description: Arranque estructurado de un proyecto nuevo. Interroga al PM en rondas hasta acordar el problema, si vale la pena resolverlo (o si es obligatorio aunque no cierre) y el foco a atacar — recién entonces discute la solución que el PM ya tenía pensada. Crea la carpeta del proyecto al inicio, antes de la primera pregunta, y resguarda todo el discovery aunque el proyecto se abandone. Se activa con /idea_start.
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /idea_start, típicamente cuando trae una idea, un problema, una oportunidad o una solución ya pensada que todavía no tiene proyecto ni IDEA de Jira — o cuando quiere retomar un discovery que había quedado abierto.
disable-model-invocation: true
argument-hint: "[tema o idea en una línea, o nombre de proyecto existente para retomar]"
---

# 🚦 ARRANQUE DE PROYECTO: /idea_start

## 🎯 Por qué existe esta skill

El vicio más común de un PO es llegar con la solución ya cocinada y sin haber definido el problema — a veces ni siquiera dice el problema, dice directamente "hay que hacer X". Ninguna skill de la casa frena eso hoy: `/idea_problem` ya asume un problema acordado, y `/debrief` cierra conversación libre sin interrogar.

`/idea_start` es la puerta de entrada que falta. Interroga al PM en rondas (técnica de [`/grilling`](../grilling/SKILL.md): design tree, frontera, rondas numeradas con recomendación) hasta acordar **el problema → si vale la pena (o si es obligatorio igual) → el foco → recién ahí la solución**. Se diferencia de `/grilling` puro en que parte del contexto del Cerebro entero — no solo del producto en cuestión — y en que su salida es persistente: la carpeta se crea al inicio, así el discovery queda resguardado aunque el proyecto no prospere. Un "no vale la pena" bien razonado es tan buen resultado como un PRD.

## Cuándo NO usarla

- El problema ya está acordado y lo que falta es el documento formal → eso es [`/idea_problem`](../idea_problem/SKILL.md), que asume el problema como insumo, no lo interroga.
- Ya hay foco y solución acordados y lo que falta es especificar para ingeniería → `/idea_prd`.
- Es solo una sesión de trabajo libre sobre un proyecto que ya pasó su discovery inicial → `/debrief`.
- Es puro estimador de tamaño sobre una IDEA que ya tiene PRD → `/idea_estimate`.

## ⚖️ Reglas duras

1. **La carpeta se crea al inicio, siempre, sin preguntar.** Nunca se borra una carpeta; si se abandona, queda con Estado explícito.
2. **La solución del PM se estaciona y no se discute hasta la Fase 3.** Si insiste: *"Lo anoté como S3, no se pierde, volvemos en la Fase 3. Ahora: `<pregunta pendiente>`"*. Nunca se debate su mérito antes del Gate 2 — el estacionamiento es una promesa, no un rechazo, y por eso la tabla se le muestra cada vez que se agrega un ítem.
3. **No se cruza un gate sin confirmación literal.** Ni la recomendación de Claude ni el silencio del PM equivalen a un sí.
4. **Los hechos los busca Claude; las decisiones son del PM.** Nunca preguntes lo que la wiki ya responde; nunca decidas lo que le toca al PM. Esto incluye material técnico ya cargado en `referencias/` (Swagger, specs, manuales): si la respuesta a una duda técnica está en un documento que ya tenés, es un hecho a buscar, no una pregunta a escalar.
5. **El índice de cada carpeta decide qué leer, no una lista fija.** Abrí el `index.md` y elegí desde su tabla; los archivos que nombra esta skill son el piso conocido, nunca el techo — si el índice lista algo que la skill no menciona y pinta relevante, abrilo.
6. **Abrí el índice antes de descartar un módulo.** `2_areas/` completa y las tres vías de `3_recursos/`, no solo `direccion/` y la carpeta del producto. Triage rápido sí, descarte a ciegas no. Dejá registrado qué descartaste y por qué, en una línea.
7. **Preguntá siempre a quién más le sirve.** Un pedido de un cliente se clasifica por el producto al que le pega, no por el cliente — y si lo que se va a construir resuelve el mismo dolor en otros, eso cambia el veredicto del Gate 2 y a veces el foco entero.
8. **Todo impacto lleva número, o queda marcado como estimación y baja a `gaps.md`.** Contradecir al PM con el dato es parte del trabajo.
9. **Un proyecto obligatorio no se bloquea, pero sí se justifica.** Si no cierra por valor y entra igual, dejá documentado quién lo impone, qué pasa si no se hace y cuál es el alcance mínimo que cumple. Nunca aceptes "lo pidió la CEO" o "es normativa" como justificación cerrada — eso es la atribución, falta la consecuencia.
10. **Las 9 secciones canónicas son el consolidado; el anexo es el proceso.** Nada se escribe en los dos.
11. **Antes de crear, verificá que no exista.** Y si existe, leé todo lo que ya tiene antes de preguntar: lo ya acordado se confirma, no se re-interroga.
12. **Pedí el material que probablemente exista, una vez y por nombre.** Minutas, mails, tickets, documentación del procesador, normativa, el export que sostiene la cifra. No bloquees el discovery esperándolo — arrancá igual, incorporalo cuando llegue, y si el dato nuevo contradice un gate ya cerrado, decilo y volvé a ese gate.

## Modos de arranque

El PM no siempre llega igual. Detectá en qué modo entra y adaptá el arranque — pero convergé siempre al mismo pipeline de 3 gates.

| Modo | Cómo llega | Qué hacés distinto |
|---|---|---|
| **A. Problema + solución** | Trae el dolor y ya sabe qué construir | El caso base: Paso 0 parte en dos baldes, la solución al estacionamiento. |
| **B. Solo problema u oportunidad** | Trae el dolor, no propone nada | El estacionamiento arranca **vacío y está bien** — no le inventes una solución para tener qué estacionar. En Fase 3 generás opciones desde cero, mínimo dos. |
| **C. Solo solución** | "Hay que hacer un botón de reintentar" y nada más | El más común y el más riesgoso. Ver abajo. |
| **D. Sobre carpeta existente** | Proyecto viejo con info adentro, o discovery parado | Modo *retomar*. Ver abajo. |
| **E. Sin material, lo consigue después** | Se olvidó de cargar minutas, mails, tickets | Pedilo por nombre en el Paso 1.6. |

**Modo C.** No se resuelve pidiéndole al PM que "defina el problema" — si lo tuviera claro lo habría dicho. Se resuelve reconstruyendo el problema hacia atrás desde la solución, sin validarla: *"¿Qué pasa hoy, sin esto? Contame el último caso concreto"* · *"¿A quién se lo mostrarías primero cuando esté listo?"* (sale el segmento) · *"¿Qué te haría decir en tres meses que esto funcionó?"* (sale la métrica) · *"¿Qué está haciendo hoy esa gente en vez de esto?"* (sale el workaround, la mejor evidencia de que el dolor existe) · *"¿Quién te lo pidió y con qué palabras?"* (separa demanda real de intuición). La solución entera va igual al estacionamiento, incluso cuando es todo lo que hay. Nunca digas "eso es una solución, no un problema" — es correcto pero cierra la conversación. Preguntá hacia atrás.

**Modo D.** Se dispara cuando `/idea_start <nombre>` matchea una carpeta ya existente, o cuando el Paso 1.5 detecta colisión y el PM elige continuar. Antes de la primera pregunta, leé todo lo que ya hay: `proyecto.md` completo (incluido el anexo de sesiones previas), `gaps.md`, `decisiones.md`, `referencias/index.md`, `artefactos/`. Lo ya acordado no se vuelve a preguntar — se presenta como resumen y se pide solo confirmación de que sigue vigente, se re-abre únicamente si el PM dice que cambió. El anexo reabre como `## 🔍 Discovery en curso — Sesión N`, lo anterior queda intacto arriba. Se retoma desde el último gate cerrado, no desde cero. Si la carpeta es legacy (`prd-XXX_<slug>/`), **no se renombra** — la convención nueva aplica solo a proyectos nuevos.

## Anatomía de la carpeta

```
wiki/1_proyectos/monitoreo_transaccional/
├─ proyecto.md                                          # 9 secciones canónicas + anexo de discovery
├─ gaps.md                                              # on-demand
├─ decisiones.md                                        # on-demand
├─ artefactos/                                          # SOLO artefactos oficiales de producto
│  ├─ monitoreo_transaccional-prd.md
│  └─ monitoreo_transaccional-us.md
└─ referencias/                                         # material original que aportó el PM
   ├─ index.md                                          # qué es cada doc y QUÉ SE EXTRAJO YA
   └─ monitoreo_transaccional-spec_funcional_mnadalin.md
```

Patrón de nombre dentro de `artefactos/` y `referencias/`: `<nombre_corto>-<titulo>.md`. El **guion medio** marca el límite del prefijo — los guiones bajos ya separan palabras dentro del nombre corto y del título, así que sin el guion medio no se ve dónde termina el prefijo. `proyecto.md`, `gaps.md` y `decisiones.md` conservan su nombre canónico: la carpeta ya los desambigua y todo el Cerebro los resuelve por ese nombre. `artefactos/`, `gaps.md` y `decisiones.md` nacen cuando hacen falta, no vacíos de entrada.

### El anexo de discovery dentro de `proyecto.md`

Las 9 secciones canónicas (1. Resumen ejecutivo · 2. Problema y contexto · 3. Alcance y definición · 4. Entrega · 5. Decisiones del proyecto · 6. Gaps abiertos · 7. Seguimiento PM · 8. Notas de sesiones · 9. Historial de sync) están desde el minuto cero y **no se tocan** en su forma — es lo que `/sync_meetings`, `/sync_mails` y `/debrief` ya saben leer y escribir. El discovery vive en un anexo al final, después de §9:

```markdown
## 🔍 Discovery en curso — sesión iniciada YYYY-MM-DD
### 🅿️ Estacionamiento de la solución (congelado hasta Gate 3)
### Contexto leído del Cerebro
<!-- qué módulos se barrieron, hechos duros con cita, y qué se descartó con motivo en una línea -->
### Ronda N — <fase> (YYYY-MM-DD)
### Tabla de evidencia — ¿vale la pena?
```

Al cerrar, el anexo se disuelve en `## Anexo — Registro del discovery (YYYY-MM-DD)`, que conserva solo lo de valor durable: la tabla del estacionamiento con su veredicto final por ítem (el artefacto que prueba el des-sesgo), la tabla de evidencia del Gate 2, el registro del barrido (qué se leyó y qué se descartó, para no repetirlo), y un resumen de 5 líneas. El ida y vuelta textual de las rondas se descarta — las conclusiones ya migraron a §2/§3/§5, las definiciones a `decisiones.md`, lo abierto a `gaps.md`. Si se retoma el proyecto, el anexo reabre como Sesión N y lo anterior queda intacto.

## 🏃 Pipeline

### Paso 0 — Captura y clasificación

Todo lo que trajo el PM (argumento, conversación, `raw/`, adjuntos) se parte en dos baldes: *señal de problema* (síntoma, quién lo sufre, urgencia, evidencia) alimenta la Fase 1; *solución precocinada* (features, endpoints, proveedores, arquitecturas) va entera al estacionamiento. Sin preguntas todavía.

### Paso 1 — Los hechos los busca Claude: barrido con triage desde índices

> **Cómo se decide qué leer.** El `index.md` de cada carpeta es quien decide, no esta skill. Se abre el índice, se lee su tabla y de ahí sale la lista de archivos a abrir para *este* tema. Lo que se nombra abajo es el piso conocido, nunca el techo: si el índice lista algo que no está acá y pinta relevante, se abre. La regla de oro es **abrir el índice antes de descartar** — descartar rápido está bien, descartar a ciegas es el "descarte por defecto" que el Cerebro prohíbe. Registrá en el anexo qué se leyó y qué se descartó con su motivo en una línea.

- **1.a Dirección (siempre, primero):** `direccion/index.md` → `north_star.md` (2 NSM + scope operativo) → `estrategia/index.md` → el `foco_<x>.md` que aplique → `estado_actual.md` (KRs y "Restricción de capacidad") → `estacionalidad_metricas.md` si aplica → `oportunidades.md` y `decisiones.md` buscando antecedentes.
- **1.b Barrido de `2_areas/` completo:** arrancá por `2_areas/index.md` y bajá a cada subcarpeta por su propio índice — no es opcional, es el overview general de la empresa. Piso conocido: `overview_empresa/` (equipo, interesados); `procesos/criterios_de_priorizacion.md` y `referencia_estimaciones.md` **siempre** (alimentan el Gate 2), el resto de `procesos/` solo si el triage de la idea lo pide; `clientes/log_clientes.md` + `casos_de_uso_clientes.md` + `patrones_transversales.md` (demanda repetida *y* a quién más le serviría); `datasets/metricas_semanales.md` **siempre** — hoy es la única medida del negocio en general que tiene el Cerebro; `glosario.md` si hace falta; `riesgos.md` y `tareas.md` del tema.
- **1.c Barrido de `3_recursos/`, las tres vías:** `3_recursos/index.md` → cada vía por su índice, no solo la carpeta del producto. `detalle_productos/index.md` → `overview_productos/overview_<producto>.md` → `detalle_productos/<producto>/index.md` → temáticos, y mirá también productos vecinos si el tema los toca (ecosistema wallet↔adquirencia, portales, APK). `arquitectura_sistema/index.md` — las restricciones técnicas que en Fase 3 matan o encarecen una solución. `cumplimiento_normativo/index.md` — obligatorio si el tema toca datos personales, KYC/AML, límites o medios de pago; es la fuente que sostiene el camino ⚠️ del Gate 2.
- **1.d Proyecto padre y antecedentes:** si el PM indicó proyecto padre, su `proyecto.md` completo — lo ya cerrado en Definiciones heredadas y Parking lot se cita, no se pregunta. `4_archivos/` solo como consulta puntual, nunca como input.

**Cierre del barrido:** 3-6 hechos duros con número y cita de archivo al anexo. Si no salió ninguno, decilo explícito — señal de que el Paso 1.6 tiene que ser más agresivo.

### Paso 1.5 — Chequeo de colisión antes de crear

Contra `1_proyectos/index.md` §1/§2, `oportunidades.md` y `tareas.md`. Si ya existe proyecto, IDEA u `OP-XXX` que cubra el tema, no dupliques: continuá el existente (Modo D) o promové la oportunidad, según decida el PM.

### Paso 1.6 — Pedido proactivo de material

El PM casi siempre tiene más de lo que cargó. Después de leer el Cerebro, inferí qué material probablemente existe según el tema y pedilo por nombre: minuta si el tema salió de una reunión (*"la levanto con `/sync_meetings`"*) · mails/contrato/SLA si hay cliente involucrado · tickets/reclamos si hay dolor operativo · documentación del procesador si toca a Fintexa/Payway/Prisma/Coelsa/Worldsys · la norma o el informe de auditoría si hay obligación regulatoria · el export si hay una afirmación de volumen. Pedilo una vez, en bloque, con la lista concreta, y aclará que el discovery arranca igual. Lo que llegue a mitad de sesión va a `referencias/`, se registra en su índice, y **puede reabrir un gate ya cerrado** si contradice lo acordado. Lo pedido y nunca llegado baja a `gaps.md` al cierre.

### Paso 2 — Nombre corto y creación

Heurística: cliente propio con nombre → `<cliente>_<objeto>`; si no, acción + objeto de negocio en 2-3 palabras snake_case, máx. 24 caracteres, ASCII sin tildes. El nombre nombra el problema, nunca la solución — `api_pull_v2` ❌ vs `conciliacion_pull` ✅, porque si el nombre lleva la solución adentro el estacionamiento ya está roto. Se anuncia, no se pregunta: *"Creé `wiki/1_proyectos/<x>/`. Si el nombre no te cierra, decímelo y lo renombro."* Creá de una vez `proyecto.md` (esqueleto de 9 secciones, `**Estado:** 🔵 En discovery`), `referencias/index.md` (tabla vacía con cabecera), y si el PM ya aportó material, copialo a `referencias/` y dalo de alta con `Extraído = ⬜ No`.

### Paso 3 — Fase 1: el PROBLEMA

Design tree con frontera inicial: quién lo sufre (segmento específico, no "usuarios") · qué le pasa hoy y qué workaround usa · frecuencia y volumen · qué evidencia hay · costo de no hacer nada · dónde termina el problema. Formato `grilling` estricto: ronda entera numerada, cada pregunta con su `➡️` recomendado derivado de lo leído. Cada ronda se appendea al anexo. **Gate 1** = enunciado de 3-5 líneas + confirmación literal → migra a §2.

### Paso 4 — Fase 2: ¿VALE LA PENA? + FOCO

Armá la tabla de evidencia **antes de preguntar nada**, cada fila con cita de archivo: encaje NSM (¿el tipo de operación está en el scope?) · encaje en foco y KR · tamaño real contrastado contra `metricas_semanales.md` y los datasets · costo de oportunidad (qué se desplaza, leyendo Restricción de capacidad) · demanda repetida · **generalización** (¿a qué otros clientes les serviría lo mismo? un pedido puntual que resuelve el dolor de otros cinco cambia el veredicto, y a veces el foco) · riesgo de no hacerlo · solapamiento con proyectos vivos · encaje con `criterios_de_priorizacion.md`. Presentá la tabla, tu recomendación, y las cuatro salidas:

- ✅ **Vale la pena ahora** → sigue a Fase 3, se acuerda el foco.
- 🟡 **Vale la pena, no ahora** → cierra con Estado `🟡 Diferido — <condición para retomar>`.
- ❌ **No vale la pena** → cierra con Estado `⚫ Descartado — <motivo>`.
- ⚠️ **No cierra por valor, pero es obligatorio** → sigue a Fase 3, con el Paso 4.5 primero.

**Gate 2.** Si sale 🟡 o ❌ → Paso 9. Si sale ✅ o ⚠️, se acuerda el foco: qué pedazo se ataca primero, qué queda afuera y por qué.

### Paso 4.5 — Ronda de obligación (solo camino ⚠️)

Un proyecto puede no cerrar ni económicamente ni por valor de producto y aun así ser innegociable: un cliente grande en riesgo, una directiva de la CEO, una normativa. No lo bloquees — bloquearlo empujaría al PM a inflar la tabla de evidencia para que pase. Pero "me lo pidieron" es una atribución, no una justificación: quién la impone (nombre y rol, nunca "el negocio") · de qué tipo es (normativa BCRA/UIF/PCI DSS/Worldsys, cliente en riesgo, directiva de dirección, compromiso comercial, dependencia de tercero, consecuencia de incidente) · **qué pasa concretamente si no se hace** (la fila que convierte atribución en justificación; sin respuesta es gap 🔴 y el veredicto queda condicionado) · deadline duro y su fuente ("urgente" no es una fecha) · qué desplaza, contra Restricción de capacidad · cuál es el alcance mínimo que satisface la obligación. Se documenta en la cabecera (`> **Origen:** ⚠️ Obligatorio — <tipo> · <quién> · <deadline>`), en §2, y como entrada propia en `decisiones.md`. Si va a `oportunidades.md`, la señal de demanda es la obligación, no demanda de mercado.

### Paso 5 — Fase 3: desestacionar la SOLUCIÓN

Releé la tabla del estacionamiento ítem por ítem contra el problema y el foco ya acordados: *"¿S1 resuelve el problema en el foco acordado? ¿Hay algo más barato que lo logre?"* Obligatorio evaluar al menos una alternativa además de la que trajo el PM — si hay una sola opción, no hubo decisión. Restricciones a chequear: regulatorias, terceros (Fintexa, Payway/Prisma, Worldsys), capacidad.

**De dónde salen las alternativas — dos fuentes, no una.** (a) Contexto fijo de `2_areas/`/`3_recursos/` (ya cubierto en el Paso 1). (b) **Todo lo que ya existe dentro de `1_proyectos/` que pueda servir** — y esto es más amplio de lo que suena: no es solo releer la carpeta de este proyecto. Antes de armar la tabla de alternativas, barré:
- `gaps.md`/`decisiones.md`/`proyecto.md` **del proyecto en curso y de su proyecto padre si es miembro** (ya cubierto en 1.d) — pero también de **cualquier otro proyecto o IDEA de `1_proyectos/index.md`** que toque el mismo dominio técnico o el mismo proveedor, aunque no tenga relación de parentesco formal: un componente, wrapper o patrón ya decidido/construido en una IDEA hermana (ej. un BFF que ya está en desarrollo por otro motivo) es candidato directo a reutilizar, y si no se busca activamente ahí, la alternativa nunca aparece — sale del PM en vez de salir del barrido.
- Los **ledgers generales**: `1_proyectos/tareas.md` (personal) y, si el tema lo amerita, `2_areas/tareas.md`/`2_areas/gaps_y_preguntas.md`/`2_areas/direccion/decisiones.md` — una tarea o decisión ya registrada ahí puede ser exactamente la pieza que resuelve o descarta una alternativa.
- **`1_proyectos/contexto_vivo/index.md`** — puede haber conocimiento ya capturado por una skill de sync (`/sync_mails`, `/sync_meetings`, etc.) todavía sin mergear al canon, pero ya relevante para esta decisión. Citalo marcando que no es canon todavía (mismo criterio que en Paso 1).

Si el material en `referencias/` incluye documentación técnica (Swagger, specs de API, manuales de integración), **agotala antes de convertir una duda técnica en gap o en pregunta al PM** — si la respuesta está en un documento que ya tenés (un endpoint, un código de error, un flujo documentado), buscala ahí primero. Preguntale al PM lo que el documento no responde, no lo que no leíste todavía.

**Gate 3** = cada ítem estacionado con veredicto ✅ Adoptado / 🔧 Adaptado (cómo) / ❌ Descartado (motivo) / 🟡 Diferido.

### Paso 6 — Encaje en proyecto padre (condicional)

Si es miembro de un proyecto general: §2bis (qué pedazo entrega / qué hereda ya cerrado / de qué depende) + fila en la tabla de miembros del padre + cabecera `> **Proyecto:** [<Nombre>](../proyecto.md) · **KR/Canal:** … · **Slice:** …`.

### Paso 7 — Gaps y decisiones

Toda pregunta sin responder → `gaps.md` (nace si no existe), formato `## [YYYY-MM-DD] — <título>` con `**Severidad:**`/`**Descripción:**`/`**Pregunta para el usuario:**`/`**Estado:**`. Los 3 gates y los descartes → `decisiones.md`, formato `## [YYYY-MM-DD] — <título>` con `**Contexto/Problema:**`/`**Decisión tomada:**`/`**Impacto en el Roadmap/Producto:**`/`**Estado:**` (Aprobado/En Revisión), orden descendente.

## 📄 Formato de salida

Usá [`references/TEMPLATE_proyecto.md`](references/TEMPLATE_proyecto.md) para el esqueleto de `proyecto.md` (9 secciones + anexo) y [`references/TEMPLATE_referencias_index.md`](references/TEMPLATE_referencias_index.md) para `referencias/index.md`. Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para una sesión corta de punta a punta con el estacionamiento funcionando y un cierre en 🟡 (cifras ilustrativas, no datos reales de Bind).

## ✅ Checklist de calidad

- [ ] El problema nombra un segmento específico, no "usuarios"
- [ ] El enunciado del problema no contiene ninguna solución
- [ ] La tabla de evidencia del Gate 2 tiene cita de archivo en cada fila con dato
- [ ] Se leyó `2_areas/` completo y las tres vías de `3_recursos/`, no solo dirección y el producto — con motivo de descarte en lo que no se abrió
- [ ] Se preguntó a quién más le serviría la solución, no solo al cliente que la pidió
- [ ] Se leyó la Restricción de capacidad y se dijo qué se desplaza
- [ ] Si el camino fue ⚠️, la fila "qué pasa si no se hace" tiene respuesta o quedó como gap 🔴
- [ ] Cada ítem estacionado tiene veredicto explícito en Gate 3
- [ ] Se evaluó al menos una alternativa a lo que trajo el PM, buscada tanto en `2_areas/`/`3_recursos/` como en otras IDEAs/proyectos de `1_proyectos/`, sus ledgers generales y `contexto_vivo/`
- [ ] Toda duda técnica se buscó primero en los documentos ya disponibles en `referencias/` antes de convertirla en pregunta al PM
- [ ] Ningún `Sin dato` quedó sin su entrada en `gaps.md`
- [ ] `referencias/index.md` no tiene ningún `⬜ No` sin explicación
- [ ] Los 3 gates tienen confirmación literal del PM en el anexo
- [ ] `proyecto.md` no repite contenido del anexo una vez disuelto

## Paso 8 — Cierre estándar

1. **Disolver el anexo** en `## Anexo — Registro del discovery (YYYY-MM-DD)` (ver "El anexo de discovery" arriba).
2. **`referencias/index.md`** — sin `⬜ No` inexplicados.
3. **Oportunidad → item `tipo: oportunidad` en `contexto_vivo/`** — si no hay IDEA de Jira y el proyecto es candidata, `destino_propuesto: 2_areas/direccion/oportunidades.md` (el merge da de alta `OP-XXX` correlativa, dedupe primero; si ya existía una `OP-XXX` para esto, indicalo en el cuerpo del item para que el merge la pase a `Promovida a <nombre_corto>`).
4. **`wiki/1_proyectos/tareas.md`** (personal, directo) — próximos pasos que salieron del discovery, `T-XXX` correlativo. Si algún paso es de interés de todo el equipo, sumá además un item `tipo: tarea_equipo` en `contexto_vivo/`.
5. **`1_proyectos/index.md`** — alta en §2 tabla maestra: Ubicación `<nombre_corto>/`, PM, Estado Jira `—`, `Origen = discovery propio`, Última actividad; y en §1 si es proyecto general. Emití además un item `tipo: iniciativa` en `contexto_vivo/` (proyecto nuevo = novedad para la cartera compartida).
6. Regenerá `contexto_vivo/index.md` si capturaste items nuevos. **Sin git** — lo hace el hook `SessionStart` una vez al día.
7. Cerrá sugiriendo el paso lógico siguiente: `/idea_problem` para formalizar §2, o `/idea_prd` si el foco y la solución ya alcanzan para especificar.

## Paso 9 — Cierre por parada (abandono / no vale la pena / diferido)

Se dispara desde cualquier gate sin confirmación, o desde el Gate 2 en 🟡/❌. Misma mecánica del Paso 8, pero: `proyecto.md` cabecera `**Estado:** ⚫ Descartado — <motivo>` / `🟡 Diferido — <condición para retomar>` / `⏸️ Discovery interrumpido en Gate N`, y §1 Resumen ejecutivo explicando **por qué se paró** — ese es el valor del proyecto, no su fracaso. Fila del index con ese mismo Estado + item `tipo: iniciativa` en `contexto_vivo/` reportando la parada. Si había una oportunidad candidata, el item de cierre indica `Descartada (<motivo>)` para que el merge la marque así. La carpeta se queda, nunca se borra.
