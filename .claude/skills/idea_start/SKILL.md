---
name: idea_start
description: Shaping estructurado de un proyecto nuevo. Interroga al PM en rondas hasta acordar el problema esencial (cuantificado, con nivel de evidencia), si vale la pena resolverlo (o si es obligatorio aunque no cierre) y el foco. Después abre un abanico de soluciones en 4 carriles (no hacer nada, operativa sin desarrollo, acotada, amplia), cada una con SP grueso por analogía, y recomienda y defiende una para que el PM la apruebe. Crea la carpeta y la IDEA de Jira en DISCOVERY al inicio, y cierra con el artefacto -start.md autocontenido en la descripción de la IDEA. Se activa con /idea_start.
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /idea_start, típicamente cuando trae una idea, un problema, una oportunidad o una solución ya pensada que todavía no tiene proyecto ni IDEA de Jira — o cuando quiere retomar un discovery que había quedado abierto.
disable-model-invocation: true
argument-hint: "[tema o idea en una línea, o nombre de proyecto existente para retomar]"
---

# 🚦 SHAPING DE PROYECTO: /idea_start

## 🎯 Por qué existe esta skill

El vicio más común de un PO es llegar con la solución ya cocinada y sin haber definido el problema. El segundo vicio es casarse con la primera solución que aparece. `/idea_start` existe para frenar los dos. Le da **shape y contorno** al proyecto: el problema esencial, cuantificado, con un foco que no se va por las ramas; un abanico real de formas de resolverlo (de la más amplia a la más barata, incluida la que no requiere desarrollo); y una recomendación que el Cerebro defiende con números y el PM aprueba.

Interroga al PM en rondas (técnica de [`/grilling`](../grilling/SKILL.md): design tree, frontera, rondas numeradas con recomendación) atravesando **4 gates: problema esencial → ¿vale la pena? + foco → abanico de soluciones → recomendación aprobada**. Parte del contexto del Cerebro entero, no solo del producto en cuestión. Su salida es persistente desde el minuto cero: carpeta e IDEA de Jira en DISCOVERY al inicio, así el discovery queda resguardado y visible para el equipo aunque el proyecto no prospere. Un "no vale la pena" bien razonado es tan buen resultado como una solución aprobada.

**Lo que esta skill NO hace:** el diseño de la solución. Nada de endpoints, contratos, esquemas de datos ni análisis de código — eso es [`/idea_solution`](../idea_solution/SKILL.md), que toma la alternativa aprobada acá y la analiza como analista funcional-técnico. Esta skill decide *qué* conviene hacer y *por qué*. `/idea_solution` decide *cómo funciona*.

## Cuándo NO usarla

- Ya hay problema, foco y solución aprobados (existe un `-start.md` en `Aprobado`) y falta el diseño funcional-técnico → [`/idea_solution`](../idea_solution/SKILL.md).
- Ya hay diseño funcional aprobado y falta revisar el impacto por área, los riesgos y especificar para ingeniería → [`/idea_crosscheck`](../idea_crosscheck/SKILL.md) → [`/idea_risks`](../idea_risks/SKILL.md) → [`/idea_prd`](../idea_prd/SKILL.md).
- Es solo una sesión de trabajo libre sobre un proyecto que ya pasó su shaping → `/debrief`.
- Es puro estimador de tamaño sobre una IDEA que ya tiene PRD → `/idea_estimate`.

## ⚖️ Reglas duras

1. **La carpeta se crea al inicio, siempre, sin preguntar.** Nunca se borra una carpeta. Si se abandona, queda con Estado explícito.
2. **La IDEA de Jira nace en DISCOVERY al inicio** (Paso 2), asignada al PM, previa búsqueda de duplicados y con el OK del PM sobre lo que se crea (es visible para todo el equipo). Si el conector falla, se registra una tarea y el discovery sigue — Jira nunca bloquea el shaping.
3. **La solución del PM se estaciona y no se discute hasta la Fase 3.** Si insiste: *"Lo anoté como S3, no se pierde, volvemos en la Fase 3. Ahora: `<pregunta pendiente>`"*. Nunca se debate su mérito antes del Gate 2, ni se toman "decisiones parciales de solución" en el Gate 1. El estacionamiento es una promesa, no un rechazo, y por eso la tabla se le muestra cada vez que se agrega un ítem.
4. **No se cruza un gate sin confirmación literal.** Ni la recomendación de Claude ni el silencio del PM equivalen a un sí.
5. **Los hechos los busca Claude; las decisiones son del PM.** Nunca preguntes lo que la wiki ya responde. Nunca decidas lo que le toca al PM. Esto incluye el material técnico ya cargado en `referencias/`: si la respuesta a una duda técnica está en un documento que ya tenés, es un hecho a buscar, no una pregunta a escalar.
6. **El índice de cada carpeta decide qué leer, no una lista fija.** Los archivos que nombra esta skill son el piso conocido, nunca el techo.
7. **Abrí el índice antes de descartar un módulo.** `2_areas/` completa y las tres vías de `3_recursos/`. Triage rápido sí, descarte a ciegas no. Registrá qué descartaste y por qué, en una línea.
8. **Preguntá siempre a quién más le sirve.** Un pedido de un cliente se clasifica por el producto al que le pega, no por el cliente. Si resuelve el mismo dolor en otros, eso cambia el veredicto del Gate 2 y habilita el carril 3.
9. **El Cerebro siempre propone la magnitud — nunca queda vacía — y cada número lleva su nivel de evidencia.** Orden:
   - (a) **calculado** desde el Cerebro, `sync_metrics`/datasets o `referencias/`, con cita;
   - (b) **estimado por analogía** con un caso, cliente o proyecto parecido, con la analogía citada;
   - (c) **supuesto razonado**, con la cuenta a la vista.

   Se le sugiere al PM, que lo confirma con evidencia o elige no validarlo. Niveles:
   - `✅ Validado` — hay evidencia comprobable;
   - `🔶 Estimado` — analogía;
   - `⚪ Supuesto` — hipótesis sin validar.

   Aplica a medida, impacto y SP. Contradecir al PM con el dato es parte del trabajo.
10. **La incertidumbre le baja el precio al proyecto.** Si un número clave queda en 🔶 o ⚪ porque el PM eligió no validarlo:
    - es una incertidumbre registrada (fila en `gaps.md` con qué evidencia la cerraría y a quién pedírsela);
    - el veredicto del Gate 2 y del Gate 4 se razona sobre el **escenario conservador** del rango;
    - la recomendación dice explícitamente cuánto cambiaría el veredicto si se validara.

    Un proyecto que solo cierra con el supuesto optimista nunca se recomienda como ✅ sin esa aclaración.
11. **Un proyecto obligatorio no se bloquea, pero sí se justifica.** Si no cierra por valor y entra igual, dejá documentado quién lo impone, qué pasa si no se hace y cuál es el alcance mínimo que cumple. "Lo pidió la CEO" o "es normativa" es la atribución: falta la consecuencia.
12. **El foco tiene frontera escrita.** Al cerrar el Gate 2 queda una tabla *Dentro / Fuera / Por qué*. Todo lo que aparezca después y caiga fuera va a la lista 🧺 *Fuera de foco* del anexo — nunca al alcance, salvo que el PM reabra el Gate 2 explícitamente.
13. **El abanico tiene siempre 4 carriles:**
    - **0** no hacer nada / convivir;
    - **1** operativa / manual / sin desarrollo;
    - **2** acotada / mínima suficiente;
    - **3** amplia / generalizable.

    Los cuatro se evalúan. Un carril que no aplica dice `No aplica — <motivo>`, nunca se omite. Si todas las opciones son de un mismo carril, no hubo decisión.
14. **Toda alternativa lleva un tamaño grueso por analogía citada, nunca un número suelto.**
    - Formato: rango o talle S/M/L/XL (S=1 · M=3 · L=7 · XL=15 SP) con "se parece a `<iniciativa>`, que costó X SP reales".
    - Se usa el **tamaño real** de la analogía (`log_iniciativas_producto.md`, `referencia_estimaciones.md`), no su estimación original — el historial muestra subestimaciones de 4→20, 5→87 y 3→29 SP — y el rango se abre hacia arriba.
    - El carril 1 se mide en esfuerzo operativo (horas/semana o por caso de un área) más el SP de cualquier ajuste menor que requiera.
    - Prohibido: dimensionar ítem por ítem, convertir a horas-hombre de desarrollo, o dar precisión que la analogía no sostiene.
    - Es una estimación de shaping, no el sizing de `/idea_estimate` ni el de Ingeniería.
15. **Tope de profundidad: esta skill no diseña la solución.** Nada de endpoints, contratos, esquemas de base, máquinas de estado ni análisis de código. Si una duda técnica hace falta para **discriminar entre alternativas**, se investiga solo hasta el nivel que alcanza para decidir. El resto se anota como *Pregunta para el análisis funcional-técnico* y viaja a `/idea_solution`.
16. **Todo lo que sale de acá es propuesta del Cerebro hasta el Gate 4.** El `-start.md` queda en `Estado: Propuesta` hasta la confirmación literal del PM, y recién ahí pasa a `Aprobado por PM (YYYY-MM-DD)`.
17. **`proyecto.md` es el repositorio vivo; `-start.md` es la foto aprobada.** Nada se escribe duplicado en los dos: `proyecto.md` §1–§4 resumen en pocas líneas y linkean al `-start.md`. El proceso (rondas) vive en el anexo de `proyecto.md`.
18. **Antes de crear, verificá que no exista** — en `1_proyectos/`, en `oportunidades.md` y en Jira. Si existe, leé todo lo que ya tiene antes de preguntar: lo ya acordado se confirma, no se re-interroga.
19. **Pedí el material que probablemente exista, una vez y por nombre.** No bloquees el discovery esperándolo. Si el dato nuevo contradice un gate ya cerrado, decilo y volvé a ese gate. Si convierte un ⚪ en ✅, actualizá el nivel y recalculá el veredicto.
20. **El PM puede seguir contra el veredicto, pero queda escrito.** Si el Gate 2 o el 4 dan 🟡/❌ y el PM decide continuar igual, se registra como decisión propia en `decisiones.md` con su motivo, y la cabecera de `proyecto.md` suma `> **Continuación:** por decisión del PM contra veredicto <🟡/❌> (YYYY-MM-DD) — <motivo>`.

## Modos de arranque

Detectá en qué modo entra el PM y adaptá el arranque — pero convergé siempre al mismo pipeline de 4 gates.

| Modo | Cómo llega | Qué hacés distinto |
|---|---|---|
| **A. Problema + solución** | Trae el dolor y ya sabe qué construir | Caso base: el Paso 0 parte en dos baldes, la solución va al estacionamiento. |
| **B. Solo problema u oportunidad** | Trae el dolor, no propone nada | El estacionamiento arranca **vacío y está bien**. En la Fase 3 el abanico sale entero del Cerebro. |
| **C. Solo solución** | "Hay que hacer un botón de reintentar" y nada más | El más común y el más riesgoso. Ver abajo. |
| **D. Sobre carpeta existente** | Proyecto viejo con info adentro, o discovery parado | Modo *retomar*. Ver abajo. |
| **E. Sin material, lo consigue después** | Se olvidó de cargar minutas, mails, tickets | Pedilo por nombre en el Paso 1.6. |

**Modo C.** No se resuelve pidiéndole al PM que "defina el problema" — si lo tuviera claro lo habría dicho. Se reconstruye el problema hacia atrás desde la solución, sin validarla:
- *"¿Qué pasa hoy, sin esto? Contame el último caso concreto"*
- *"¿A quién se lo mostrarías primero cuando esté listo?"* (sale el segmento)
- *"¿Qué te haría decir en tres meses que esto funcionó?"* (sale la métrica)
- *"¿Qué está haciendo hoy esa gente en vez de esto?"* (sale el workaround: la mejor evidencia del dolor y la semilla del carril 1)
- *"¿Quién te lo pidió y con qué palabras?"* (separa demanda real de intuición)

La solución entera va igual al estacionamiento. Nunca digas "eso es una solución, no un problema": preguntá hacia atrás.

**Modo D.** Se dispara cuando `/idea_start <nombre>` matchea una carpeta existente, o cuando el Paso 1.5 detecta colisión y el PM elige continuar.
- Antes de la primera pregunta, leé todo: `proyecto.md` completo (incluido el anexo), `gaps.md`, `decisiones.md`, `riesgos.md`, `referencias/index.md`, `artefactos/` (incluido un `-start.md` o un `-problem.md` legacy).
- Lo ya acordado se presenta como resumen y se pide solo confirmación de que sigue vigente.
- El anexo reabre como `## 🔍 Discovery en curso — Sesión N`. Se retoma desde el último gate cerrado.
- Si la IDEA de Jira no existe todavía, se crea en este momento (Paso 2).
- Si la carpeta es legacy (`prd-XXX_<slug>/`), **no se renombra**.

## Anatomía de la carpeta

```
wiki/1_proyectos/monitoreo_transaccional/
├─ proyecto.md                                          # repositorio vivo: 9 secciones canónicas + anexo de discovery
├─ gaps.md                                              # on-demand (incluye incertidumbres ⚪/🔶 no validadas)
├─ decisiones.md                                        # on-demand (los 4 gates + descartes)
├─ riesgos.md                                           # on-demand
├─ artefactos/                                          # SOLO artefactos oficiales de producto
│  ├─ monitoreo_transaccional-start.md                  # el shaping aprobado (sale de esta skill)
│  └─ monitoreo_transaccional-solution.md               # lo agrega /idea_solution después
└─ referencias/                                         # material original que aportó el PM
   ├─ index.md                                          # qué es cada doc y QUÉ SE EXTRAJO YA
   └─ monitoreo_transaccional-spec_funcional_mnadalin.md
```

Patrón de nombre dentro de `artefactos/` y `referencias/`: `<nombre_corto>-<titulo>.md`. El guion medio marca el límite del prefijo. `proyecto.md`, `gaps.md`, `decisiones.md` y `riesgos.md` conservan su nombre canónico. `artefactos/`, `gaps.md`, `decisiones.md` y `riesgos.md` nacen cuando hacen falta.

### `proyecto.md` y su anexo de discovery

Las 9 secciones canónicas (1. Resumen ejecutivo · 2. Problema y contexto · 3. Alcance y definición · 4. Entrega · 5. Decisiones del proyecto · 6. Gaps abiertos · 7. Seguimiento PM · 8. Notas de sesiones · 9. Historial de sync) están desde el minuto cero y **no se tocan** en su forma — es lo que `/sync_meetings`, `/sync_mails` y `/debrief` saben leer y escribir. `proyecto.md` es el repositorio vivo del proyecto y sigue creciendo después de esta skill. El discovery vive en un anexo al final, después de §9:

```markdown
## 🔍 Discovery en curso — sesión iniciada YYYY-MM-DD
### 🅿️ Estacionamiento de la solución (congelado hasta la Fase 3)
### Contexto leído del Cerebro
### Ronda N — <fase> (YYYY-MM-DD)
### Tabla de magnitudes y nivel de evidencia
### Tabla de evidencia — ¿vale la pena?
### Frontera del foco
### 🧺 Fuera de foco
### Abanico de soluciones (4 carriles)
### Recomendación del Cerebro
```

Al cerrar, el anexo se disuelve en `## Anexo — Registro del discovery (YYYY-MM-DD)`, que conserva solo lo de valor durable:
- la tabla del estacionamiento con su carril y veredicto final por ítem (prueba el des-sesgo);
- la tabla de magnitudes con su nivel de evidencia;
- la tabla de evidencia del Gate 2;
- la lista 🧺 fuera de foco;
- el registro del barrido (qué se leyó y qué se descartó);
- un resumen de 5 líneas.

Las conclusiones ya migraron al `-start.md` (y en resumen a §1–§4), las definiciones a `decisiones.md`, lo abierto a `gaps.md`.

## 🏃 Pipeline

### Paso 0 — Captura y clasificación

Todo lo que trajo el PM (argumento, conversación, `raw/`, adjuntos) se parte en dos baldes:
- *señal de problema* (síntoma, quién lo sufre, urgencia, evidencia, workaround actual) → alimenta la Fase 1;
- *solución precocinada* (features, endpoints, proveedores, arquitecturas, procesos) → va entera al estacionamiento.

Sin preguntas todavía.

### Paso 1 — Los hechos los busca Claude: barrido con triage desde índices

> El `index.md` de cada carpeta decide qué leer. Lo que se nombra abajo es el piso, nunca el techo. **Abrí el índice antes de descartar.** Registrá en el anexo qué se leyó y qué se descartó con su motivo en una línea.

- **1.a Dirección (siempre, primero):** `direccion/index.md` → `north_star.md` → `estrategia/index.md` → el `foco_<x>.md` que aplique → `estado_actual.md` (KRs y "Restricción de capacidad") → `estacionalidad_metricas.md` si aplica → `oportunidades.md` y `decisiones.md` buscando antecedentes.
- **1.b `2_areas/` completo:** desde `2_areas/index.md`.
  - `overview_empresa/` (equipo, interesados, qué áreas podrían absorber una solución operativa).
  - `procesos/criterios_de_priorizacion.md` y `referencia_estimaciones.md` **siempre**.
  - Del resto de `procesos/`, lo que el triage pida — **y siempre lo que describa cómo opera hoy el área afectada**, porque es la base del carril 1.
  - `clientes/log_clientes.md` + `casos_de_uso_clientes.md` + `patrones_transversales.md` (demanda repetida y a quién más le serviría).
  - `glosario.md` si hace falta; `riesgos.md` y `tareas.md` del tema.
- **1.c `3_recursos/`, las tres vías:**
  - `detalle_productos/` (producto y vecinos).
  - `arquitectura_sistema/` (restricciones que matan o encarecen alternativas).
  - `cumplimiento_normativo/` (obligatorio si toca datos personales, KYC/AML, límites o medios de pago).
  - `datos/`: `log_iniciativas_producto.md` **siempre** (base del SP por analogía) y los stores de `sync_metrics` / `datos_metricas_semanales/` **siempre** (base de la magnitud calculada).
- **1.d Proyecto padre, hermanos y antecedentes:**
  - el `proyecto.md` del padre si aplica;
  - **cualquier otro proyecto o IDEA de `1_proyectos/index.md`** del mismo dominio o proveedor (componentes ya decididos o en construcción son candidatos directos a alternativa);
  - `1_proyectos/tareas.md`;
  - `1_proyectos/contexto_vivo/index.md` (citado como no-canon todavía);
  - `4_archivos/` solo como consulta puntual.

**Cierre del barrido:** 3-6 hechos duros con número y cita. Si no salió ninguno, decilo explícito: el Paso 1.6 tiene que ser más agresivo.

### Paso 1.5 — Chequeo de colisión antes de crear

Contra `1_proyectos/index.md` §1/§2, `oportunidades.md`, `tareas.md` **y Jira**: `searchJiraIssuesUsingJql` sobre el proyecto `PRD`, `issuetype = Idea`, con los términos clave del tema. Si ya existe proyecto, IDEA u `OP-XXX` que lo cubra, no dupliques: continuá el existente (Modo D), reusá o reasigná la IDEA, o promové la oportunidad, según decida el PM.

### Paso 1.6 — Pedido proactivo de material

Inferí qué material probablemente existe y pedilo por nombre, una vez, en bloque:
- minuta si salió de una reunión (*"la levanto con `/sync_meetings`"*);
- mails/contrato/SLA si hay cliente;
- tickets/reclamos si hay dolor operativo;
- documentación del procesador si toca a Fintexa/Payway/Prisma/Coelsa/Worldsys;
- norma o informe de auditoría si hay obligación;
- **el export o el dato que validaría cada magnitud clave**.

Aclará que el discovery arranca igual. Lo que llegue va a `referencias/` y se registra en su índice. Lo pedido y nunca llegado baja a `gaps.md` al cierre.

### Paso 2 — Nombre corto, carpeta e IDEA en DISCOVERY

**Nombre.** Cliente propio con nombre → `<cliente>_<objeto>`. Si no, acción + objeto de negocio en 2-3 palabras snake_case, máx. 24 caracteres, ASCII. El nombre nombra el problema, nunca la solución (`api_pull_v2` ❌ vs `conciliacion_pull` ✅). Se anuncia, no se pregunta: *"Creé `wiki/1_proyectos/<x>/`. Si el nombre no te cierra, decímelo y lo renombro."*

**Carpeta.** Creá de una vez:
- `proyecto.md` (esqueleto de 9 secciones + anexo, `**Estado:** 🔵 En discovery`);
- `referencias/index.md`;
- si el PM ya aportó material, copialo a `referencias/` y dalo de alta con `Extraído = ⬜ No`.

**IDEA en Jira (Regla dura 2).** Con los IDs de [`../idea_jira/references/campos_jira.md`](../idea_jira/references/campos_jira.md):
1. Resolvé el `accountId` del PM desde `pm`/`email` de `identidad.local.md` (`lookupJiraAccountId`), una sola vez.
2. Mostrale al PM qué vas a crear:
   - título (nombra el problema, igual criterio que el nombre corto);
   - Categoría (`BAU`/`BUILD`/`NORMATIVO`, si ya es inferible), Producto, Cliente (si ya se conocen — si no, quedan vacíos y se completan al cierre);
   - descripción mínima: *"Discovery en curso — shaping del problema y de las alternativas de solución. La descripción se completa al cierre del discovery."*
3. Con su OK: `createJiraIssue` (proyecto `PRD`, issuetype Idea) asignada al PM → `transitionJiraIssue` a **DISCOVERY** → verificá el estado con `getJiraIssue`.
4. Registrá la clave en `proyecto.md` (cabecera `> **IDEA:** PRD-XXX`) y en la columna IDEA / Estado Jira de `1_proyectos/index.md` §2 (alta de la fila en este mismo paso: Ubicación, PM, `Origen = discovery propio`, Última actividad).
5. **Si el conector falla:** no reintentes a ciegas. Tarea `T-XXX` en `1_proyectos/tareas.md` ("crear IDEA en DISCOVERY para `<nombre>`"), columna IDEA en `— (pendiente, conector)`, y seguí con la Fase 1.

### Paso 3 — Fase 1: el PROBLEMA ESENCIAL

Design tree con frontera inicial. Formato `grilling` estricto: ronda entera numerada, cada pregunta con su `➡️` recomendado derivado de lo leído. Adaptación de tres baldes por ronda:
- **✅ Resuelto desde fuentes** (con cita, para que el PM confirme);
- **❓ Preguntas al PM** (solo decisiones suyas);
- **📄 Pedidos de dato o material**.

Cada ronda se appendea al anexo.

Ramas del árbol (el orden es una guía, no una regla):

1. **Síntoma vs. problema esencial.** Listá los síntomas que trajo el PM y buscá el problema detrás del problema: 3-5 *"¿por qué pasa esto?"* o *"si resolvemos esto pero X sigue igual, ¿se fue el dolor?"*. El problema esencial es el que, resuelto, hace desaparecer los síntomas. Los síntomas quedan como evidencia, no como alcance. Si aparecen dos problemas esenciales independientes, son dos proyectos: proponé partir.
2. **Afectado** — segmento específico y accionable, nunca "usuarios".
3. **Job story** — *"Cuando [situación], quiero [motivación], para poder [resultado esperado]"*. Nunca preguntes qué feature quiere; si contesta con una, repreguntá la situación o el resultado detrás.
4. **Alternativa actual** — con qué compite hoy la solución: workaround manual, planilla, proceso de otra área, competencia o "nada". Su costo alimenta la medida. **Es la semilla del carril 1 de la Fase 3.**
5. **Fuerzas del cambio** — qué empuja a resolverlo ahora, qué atrae, qué ansiedad genera cambiar, qué inercia frena. Alimenta el "por qué ahora".
6. **Medida del problema** (Regla dura 9) — la magnitud hoy: volumen, frecuencia, tasa, costo, horas. **El Cerebro propone siempre el número** (calculado → estimado por analogía → supuesto razonado), con su nivel ✅/🔶/⚪, y le pide al PM que lo valide o decida no validarlo.
7. **Impacto del problema** — qué cuesta no resolverlo, en negocio y/o áreas internas, mismo tratamiento de nivel de evidencia.
8. **Meta / criterio de éxito** — baseline → target → plazo, sobre la misma métrica de la medida, trazada hasta el resultado del job story.
9. **Dónde termina el problema** — qué no es parte de este problema (semilla de la frontera del foco).

**Tabla de magnitudes** (en el anexo): `Magnitud | Valor o rango | Cómo se obtuvo (cálculo/analogía/supuesto + cita) | Nivel ✅/🔶/⚪ | Evidencia que lo validaría | ¿El PM lo valida?`. Cada fila que quede 🔶/⚪ por elección del PM → entrada en `gaps.md` como incertidumbre (Regla dura 10).

**Gate 1** = enunciado en una frase — **"[Afectado] necesita [necesidad] porque [razón]"**, sin solución adentro — más la medida con su nivel de evidencia y la confirmación literal del PM. Migra resumido a §2.

### Paso 4 — Fase 2: ¿VALE LA PENA? + FOCO

Armá la tabla de evidencia **antes de preguntar nada**. Cada fila lleva cita de archivo y, si lleva número, su nivel ✅/🔶/⚪. Filas:
- encaje NSM (¿el tipo de operación está en el scope?);
- encaje en foco y KR;
- tamaño real (desde la tabla de magnitudes — si está en 🔶/⚪, la fila dice *"a la baja por falta de evidencia"*);
- costo de oportunidad (provisorio, leyendo Restricción de capacidad — se confirma en el Gate 4 con el SP de la alternativa elegida);
- demanda repetida;
- **generalización** (¿a qué otros clientes o productos les serviría? — habilita o descarta el carril 3);
- riesgo de no hacerlo;
- solapamiento con proyectos vivos;
- encaje con `criterios_de_priorizacion.md`.

Presentá la tabla, tu recomendación **razonada sobre el escenario conservador** si hay incertidumbre (Regla dura 10) y las cuatro salidas:

- ✅ **Vale la pena ahora** → sigue a la Fase 3.
- 🟡 **Vale la pena, no ahora** → cierra con Estado `🟡 Diferido — <condición para retomar>` (una condición típica: *"validar la magnitud X"*).
- ❌ **No vale la pena** → cierra con Estado `⚫ Descartado — <motivo>`.
- ⚠️ **No cierra por valor, pero es obligatorio** → sigue a la Fase 3, con el Paso 4.5 primero.

**Gate 2.** Si sale 🟡 o ❌ → Paso 9, salvo override del PM (Regla dura 20). Si sale ✅ o ⚠️, se acuerda el foco y se escribe la **frontera del foco**: tabla `Dentro | Fuera | Por qué` (qué pedazo se ataca primero, qué queda afuera). Desde acá rige la lista 🧺 fuera de foco (Regla dura 12).

### Paso 4.5 — Ronda de obligación (solo camino ⚠️)

No lo bloquees — bloquearlo empujaría al PM a inflar la tabla de evidencia. Pero "me lo pidieron" es una atribución, no una justificación. Relevá:
- quién la impone (nombre y rol);
- de qué tipo es (normativa BCRA/UIF/PCI DSS/Worldsys, cliente en riesgo, directiva de dirección, compromiso comercial, dependencia de tercero, consecuencia de incidente);
- **qué pasa concretamente si no se hace** (sin respuesta es gap 🔴 y el veredicto queda condicionado);
- deadline duro y su fuente;
- qué desplaza;
- cuál es el alcance mínimo que satisface la obligación — **es el piso del carril 2 en la Fase 3**.

Se documenta en la cabecera (`> **Origen:** ⚠️ Obligatorio — <tipo> · <quién> · <deadline>`), en §2 y en `decisiones.md`.

### Paso 5 — Fase 3: el ABANICO DE SOLUCIONES

Recién acá se abre el estacionamiento. Armá el abanico **antes de preguntar nada**, con alternativas que salen de tres fuentes:
- (a) el estacionamiento del PM;
- (b) el canon de `2_areas/`/`3_recursos/`;
- (c) todo `1_proyectos/` — IDEAs hermanas, componentes ya construidos o en construcción, ledgers, `contexto_vivo/`.

Si en `referencias/` hay documentación técnica, agotala antes de convertir una duda en pregunta.

**Los 4 carriles (Regla dura 13):**

| Carril | Qué es | De dónde sale | Se mide en |
|---|---|---|---|
| **0. No hacer nada / convivir** | Línea de base: el costo de seguir igual | Medida + impacto de la Fase 1 | Costo del problema por período |
| **1. Operativa / manual / sin desarrollo** | Proceso o responsabilidad de un área (Soporte, Operaciones, Administración, Integraciones, PLD), configuración de algo existente, política o regla de negocio, acuerdo con un tercero, formalizar el workaround actual | Alternativa actual (Fase 1), `procesos/`, `overview_empresa/` | Esfuerzo operativo (h/semana o por caso, de qué área) + SP de ajustes menores si hay |
| **2. Acotada / mínima suficiente** | Lo mínimo que resuelve el problema esencial dentro del foco, y nada más | Frontera del foco (Fase 2), alcance mínimo si es ⚠️ | SP por analogía |
| **3. Amplia / generalizable** | Solución de plataforma que resuelve también el dolor de otros clientes o productos y abre opcionalidad futura | Fila de generalización (Fase 2), `patrones_transversales.md`, IDEAs hermanas | SP por analogía |

Cada ítem del estacionamiento se **ubica en un carril** (o se marca como fuera del problema). Puede haber más de una opción por carril y **combinaciones secuenciales** (ej.: *carril 1 ya, mientras se construye el carril 2*).

**Ficha corta por alternativa** (5-8 líneas, sin diseño técnico — Regla dura 15):
- qué es, en una o dos frases;
- qué parte del problema esencial cubre (total / parcial — qué queda sin cubrir);
- **tamaño** (Regla dura 14): rango o talle + analogía citada + nivel ✅/🔶/⚪;
- tiempo a valor (cuándo empieza a aliviar el problema);
- quién la ejecuta (equipo de ingeniería, área operativa, tercero);
- dependencias y riesgos principales (regulatorios, terceros — Fintexa, Payway/Prisma, Worldsys, Coelsa — y capacidad);
- escalabilidad y reversibilidad (¿se puede empezar por acá y crecer? ¿se puede deshacer?).

Las dudas técnicas que no hacen falta para elegir entre alternativas van a la lista *Preguntas para el análisis funcional-técnico* del anexo — no se investigan acá.

**Gate 3** = el PM confirma literal que el abanico está completo (no falta ninguna opción que él vea) y que las fichas son correctas. Si agrega una opción, se le arma su ficha y se vuelve a presentar.

### Paso 6 — Fase 4: RECOMENDACIÓN Y DEFENSA

El Cerebro recomienda una alternativa (o una combinación) y **la defiende**, en este formato:

- **Recomendación:** `<alternativa>` — una frase.
- **Por qué resuelve el problema esencial en el foco:** 2-3 líneas.
- **Costo / beneficio:** tamaño vs. medida e impacto del problema, **sobre el escenario conservador** si hay números 🔶/⚪, confirmando el costo de oportunidad provisorio del Gate 2 contra la Restricción de capacidad.
- **Por qué no las otras:** una línea por alternativa descartada, incluido el carril 0.
- **Qué la invalidaría:** la señal que haría cambiar de opción (ej.: *"si el volumen supera N/mes, pasar al carril 3"*).
- **Repuesto:** la segunda mejor opción, si la recomendada se cae.
- **Sensibilidad a la evidencia:** si hay incertidumbre, cuánto cambia la recomendación si el número se valida arriba o abajo.

**Chequeo final "¿conviene?":** si ni la mejor alternativa compensa su costo de oportunidad, la recomendación puede ser 🟡 Diferir o ❌ No hacer — aunque el Gate 2 haya dado ✅. Es el momento en que por primera vez se conoce el costo real.

**Gate 4** = confirmación literal del PM sobre la alternativa elegida, cada ítem del estacionamiento con su veredicto final (✅ Adoptado / 🔧 Adaptado — cómo / ❌ Descartado — motivo / 🟡 Diferido) y el `-start.md` pasa de `Propuesta` a `Aprobado por PM (YYYY-MM-DD)`. Si el PM elige otra alternativa distinta de la recomendada, es su decisión: se registra con su motivo y la defensa del Cerebro queda en `decisiones.md` como opinión discrepante.

### Paso 7 — Encaje en proyecto padre, gaps, decisiones y riesgos

- **Proyecto padre (condicional):**
  - §2bis del `proyecto.md` (qué pedazo entrega / qué hereda ya cerrado / de qué depende);
  - fila en la tabla de miembros del padre;
  - cabecera `> **Proyecto:** [<Nombre>](../proyecto.md) · **KR/Canal:** … · **Slice:** …`.
- **`gaps.md`:**
  - toda pregunta sin responder y **toda incertidumbre ⚪/🔶 no validada**;
  - formato `## [YYYY-MM-DD] — <título>` con `**Severidad:**`/`**Descripción:**`/`**Pregunta para el usuario:**`/`**Estado:**`;
  - en las incertidumbres, además, `**Evidencia que la cerraría:**` y `**Efecto en el veredicto si se valida:**`.
- **`decisiones.md`:**
  - los 4 gates, los descartes del abanico y cualquier override del PM;
  - formato `## [YYYY-MM-DD] — <título>` con `**Contexto/Problema:**`/`**Decisión tomada:**`/`**Impacto en el Roadmap/Producto:**`/`**Estado:**`, orden descendente.
- **`riesgos.md`:** riesgos de la alternativa elegida, específicos del proyecto.

## 📄 Formato de salida

- [`references/TEMPLATE_start.md`](references/TEMPLATE_start.md) — el artefacto `artefactos/<nombre>-start.md`, **autocontenido**: sin links a la wiki, sin nombres de archivo o de skill, sin códigos de ticket usados como si el lector los reconociera. Va a la descripción de la IDEA y lo puede leer alguien sin acceso al Cerebro. Las fuentes se describen por su naturaleza ("minuta de la reunión con Soporte del 2026-09-01", "métricas semanales de volumen de agosto"), no por su ruta.
- [`references/TEMPLATE_proyecto.md`](references/TEMPLATE_proyecto.md) — el esqueleto de `proyecto.md` (9 secciones + anexo).
- [`references/TEMPLATE_referencias_index.md`](references/TEMPLATE_referencias_index.md) — `referencias/index.md`.
- Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para una sesión de punta a punta con los 4 carriles y la recomendación defendida (cifras ilustrativas, no datos reales de Bind).

## ✅ Checklist de calidad

- [ ] El enunciado del problema entra en una frase, nombra un segmento específico y no contiene ninguna solución
- [ ] Se separaron síntomas de problema esencial — los síntomas no quedaron como alcance
- [ ] Toda magnitud tiene número (calculado, estimado o supuesto) con su nivel ✅/🔶/⚪ — ninguna quedó vacía
- [ ] Toda magnitud 🔶/⚪ no validada tiene su incertidumbre en `gaps.md` y el veredicto se razonó sobre el escenario conservador
- [ ] La tabla de evidencia del Gate 2 tiene cita de archivo en cada fila con dato
- [ ] Se leyó `2_areas/` completo y las tres vías de `3_recursos/`, con motivo de descarte en lo que no se abrió
- [ ] Se preguntó a quién más le serviría, no solo al cliente que lo pidió
- [ ] La frontera del foco (Dentro/Fuera/Por qué) quedó escrita y lo que apareció después fuera de foco fue a 🧺, no al alcance
- [ ] El abanico tiene los 4 carriles — los que no aplican dicen `No aplica — <motivo>`
- [ ] Se evaluó al menos una alternativa operativa/sin desarrollo seria (o se explicó por qué no existe)
- [ ] Cada alternativa tiene tamaño con analogía citada (tamaño real, no estimación original) y rango abierto hacia arriba
- [ ] No se diseñó la solución: sin endpoints, contratos, esquemas ni análisis de código — las dudas técnicas quedaron como preguntas para el análisis funcional-técnico
- [ ] La recomendación tiene defensa completa (por qué sí, por qué no las otras, costo/beneficio, qué la invalidaría, repuesto)
- [ ] Cada ítem estacionado tiene carril y veredicto explícito
- [ ] Los 4 gates tienen confirmación literal del PM en el anexo
- [ ] La IDEA existe en Jira en DISCOVERY, asignada al PM, con el `-start.md` en la descripción (o hay una tarea por conector caído)
- [ ] El `-start.md` es autocontenido y está en `Aprobado por PM`
- [ ] `proyecto.md` §1–§4 resumen y linkean al `-start.md` sin duplicarlo; el anexo quedó disuelto
- [ ] `referencias/index.md` no tiene ningún `⬜ No` sin explicación

## Paso 8 — Cierre estándar

1. **`artefactos/<nombre>-start.md`** desde `TEMPLATE_start.md`, en `Aprobado por PM (YYYY-MM-DD)`, versión en frontmatter + historial de revisiones al pie. Si ya existía (Modo D), se reescribe limpio y se suma una entrada al historial.
2. **`proyecto.md`:**
   - §1 Resumen ejecutivo, §2 Problema (enunciado + medida con nivel), §3 Alcance (frontera del foco) y §4 Entrega (alternativa elegida y tamaño) en pocas líneas, cada una linkeando al `-start.md`;
   - §4 Entrega, tabla "Cadena de artefactos": fila del `-start.md` con su versión y estado. Cada skill de la cadena (`/idea_solution`, `/idea_crosscheck`, `/idea_risks`, `/idea_prd`, `/idea_us`) suma o actualiza su fila — así el PM ve de un vistazo qué paso está aprobado y cuál sigue en propuesta;
   - disolver el anexo;
   - entrada en §8 Notas de sesiones y §9 Historial de sync.
3. **Jira** — actualizar la IDEA creada en el Paso 2 (o crearla ahora si había quedado pendiente), con el OK del PM sobre el delta:
   - descripción = el contenido del `-start.md` (autocontenido; si supera el límite práctico de ~28KB del conector, recortar las fichas del abanico a su tabla resumen — nunca la recomendación ni el problema);
   - Categoría/Producto/Cliente completos;
   - `customfield_10389` ("SP estimado") = tamaño de la alternativa elegida (punto medio del rango), dejando explícito en la descripción que es **preliminar de shaping** y que se reemplaza con `/idea_estimate`;
   - la IDEA queda en DISCOVERY.

   Si el conector falla, tarea `T-XXX` con el delta pendiente.
4. **`referencias/index.md`** — sin `⬜ No` inexplicados.
5. **Oportunidad → item `tipo: oportunidad` en `contexto_vivo/`** si corresponde (`destino_propuesto: 2_areas/direccion/oportunidades.md`). Si ya existía una `OP-XXX`, indicalo para que el merge la pase a `Promovida a <nombre_corto>`.
6. **`wiki/1_proyectos/tareas.md`** — próximos pasos del PM: validar las magnitudes 🔶/⚪ que el PM quiera validar, pedidos de material pendientes, definiciones con stakeholders. Si algo es de interés del equipo, además un item `tipo: tarea_equipo`.
7. **`1_proyectos/index.md`** §2 — Estado Jira, Última actividad. Item `tipo: iniciativa` en `contexto_vivo/` (proyecto nuevo con alternativa aprobada = novedad para la cartera).
8. Regenerá `contexto_vivo/index.md` si capturaste items nuevos. **Sin git.**
9. Cerrá sugiriendo el paso siguiente: **[`/idea_solution`](../idea_solution/SKILL.md)** sobre la alternativa aprobada — hereda el `-start.md` y sus *Preguntas para el análisis funcional-técnico*. Si la alternativa elegida es del carril 1 (sin desarrollo), el paso siguiente no es `/idea_solution`: es acordar el proceso con el área dueña (tarea en `tareas.md`) y correr [`/idea_crosscheck`](../idea_crosscheck/SKILL.md) directo sobre el `-start.md` — un cambio de proceso también impacta áreas —; si además hay ajustes menores de desarrollo, sigue `/idea_risks` y un `/idea_prd` liviano.

## Paso 9 — Cierre por parada (abandono / no vale la pena / diferido)

Se dispara desde cualquier gate sin confirmación, desde el Gate 2 en 🟡/❌, o desde el Gate 4 si la recomendación es no hacer o diferir. Misma mecánica del Paso 8, pero:
- **`proyecto.md`:** cabecera `**Estado:** ⚫ Descartado — <motivo>` / `🟡 Diferido — <condición para retomar>` / `⏸️ Discovery interrumpido en Gate N`, y §1 explicando **por qué se paró** — ese es el valor del proyecto, no su fracaso.
- **`-start.md`:** se genera igual, con las secciones que se llegaron a cerrar y `Estado: Cerrado sin avanzar — <motivo>`. Es el registro de por qué no se hizo.
- **Jira:** descripción = ese `-start.md`. Consultá `getTransitionsForJiraIssue` y proponele al PM la transición que corresponda (ej.: PARKING LOT para 🟡). Nunca borres la IDEA.
- Fila del index con el mismo Estado + item `tipo: iniciativa` reportando la parada. Si había una oportunidad candidata, indicá `Descartada (<motivo>)`.
- La carpeta se queda, nunca se borra.
