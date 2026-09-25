---
name: idea_estimate
description: Carga una estimación preliminar de esfuerzo por analogía histórica, en dos modos — Proyecto (apenas hay PRD confirmado, sin historias todavía, para dimensionar la IDEA completa) e Historias (SP por historia, una vez que el PM confirmó las historias de /idea_us) — y la registra en el artefacto correspondiente, el PRD y el campo "SP estimado" de la IDEA en Jira. Se activa con /idea_estimate.
when_to_use: Se activa cuando el usuario ejecuta /idea_estimate. Modo Proyecto: apenas el PRD está confirmado, incluso sin historias de usuario todavía — para dimensionar la IDEA completa antes de comprometerla en el roadmap o conversar capacidad con Ingeniería. Modo Historias: después de que el PM haya confirmado las historias de usuario creadas por /idea_us (Paso 5ter de esa skill ya cerrado) — reemplaza o refina la estimación de Modo Proyecto con el detalle real de cada historia.
disable-model-invocation: true
argument-hint: "[PRD-XXX]"
---

# 📐 ESTIMACIÓN PRELIMINAR DE PRODUCTO (SP): /idea_estimate

## Por qué existe esta skill

Antes de que Ingeniería refine y sizee cada historia en su propio espacio de Jira (Wallet/WS, Adquirencia/AD, Onboarding/OB, Ardid/ARD, Servicios/SER), Producto necesita un número de esfuerzo aproximado para dimensionar la IDEA — priorizar contra otras IDEAs, conversar capacidad con Ingeniería, o simplemente saber si "esto es chico o grande" antes de comprometer una fecha. Esa necesidad aparece dos veces en la vida de una IDEA, con distinta precisión disponible según cuánto se avanzó:

- **Apenas el PRD está confirmado**, antes de que existan historias de usuario — la IDEA todavía es una caja negra por dentro, pero ya alcanza para compararla contra proyectos históricos similares (**Modo Proyecto**). Es el momento en que más falta hace un número: es cuando se prioriza contra otras IDEAs y se compromete (o no) una fecha.
- **Una vez que las historias de usuario ya están confirmadas** por el PM — ahí se puede estimar por analogía historia por historia, con mucho más detalle de contrato (**Modo Historias**, el uso original de esta skill).

Ninguno de los dos modos reemplaza el sizing técnico real de Ingeniería: son una **estimación a alto nivel desde Producto**, construida por analogía con el historial de esfuerzo real ya relevado — [`referencia_estimaciones.md`](../../wiki/2_areas/procesos/referencia_estimaciones.md) para piezas de desarrollo puntuales, [`log_iniciativas_producto.md`](../../wiki/3_recursos/datos/log_iniciativas_producto.md) para IDEAs/proyectos completos ya cerrados.

## Cuándo NO usarla

- Ni el PRD ni el proyecto tienen todavía alcance definido → no hay nada para dimensionar por analogía, ni siquiera a nivel proyecto; corré primero [`/idea_prd`](../idea_prd/SKILL.md) o cerrá la definición del proyecto con el PM.
- Lo que se necesita es el sizing técnico real de Ingeniería → ningún modo de esta skill lo reemplaza ni lo anticipa; solo carga la referencia preliminar de Producto. El sizing real se registra en Jira por el propio equipo técnico cuando refina cada historia en su espacio (`customfield_10041` a nivel ticket).
- La IDEA ya tiene un sizing técnico real cargado y confirmado por Ingeniería → no sobrescribas ese número con una estimación de analogía; si el PM igual quiere una referencia de Producto en paralelo, aclarálo explícitamente en el registro para no confundir ambas fuentes.

## ⚖️ Reglas duras

1. **Es una estimación de alto nivel desde Producto, nunca el sizing técnico** — en cualquiera de los dos modos. Todo lugar donde se registre este número (artefacto de historias o `proyecto.md`, PRD, campo de Jira) debe dejarlo explícito.
2. **Estimá siempre por analogía, no de la nada.** Modo Proyecto compara contra IDEAs/Epics históricas completas (`log_iniciativas_producto.md`); Modo Historias compara cada historia contra un desarrollo puntual (`referencia_estimaciones.md`) o, si no hay analogía directa, contra otra historia ya estimada del mismo dominio. Cada número debe poder justificarse con un "se parece a X, que costó Y".
3. **Usá la escala vigente de Bind PSP:** `S = 1 SP · M = 3 SP · L = 7 SP · XL = 15 SP` (confirmada en [`gestion_jira.md` §1.4](../../wiki/2_areas/procesos/gestion_jira.md#14-prioridad-versión-y-story-points)). No inventes otra escala ni mezcles Story Points directos con talles de camiseta sin convertir.
4. **Nunca sobrescribas un sizing técnico real ya cargado** sin que el usuario lo pida explícitamente — si `customfield_10041` (SP real) ya tiene valores en los tickets de desarrollo de la IDEA, avisá y preguntá antes de tocar el campo de la IDEA. Un valor de `customfield_10389` cargado por `/idea_start` (marcado como preliminar de shaping) es del mismo tipo de dato: se sobrescribe sin pedir confirmación, dejando en el historial de revisiones del artefacto de dónde venía.
5. **Gate de entrada por estado, nunca por inferencia.** Modo Proyecto exige el PRD en `estado: Aprobado por PM`; Modo Historias exige el `-us.md` en `estado: Aprobado por PM`. Si el artefacto está en `Propuesta`, pará y ofrecé revisarlo y aprobarlo ahora o volver a la skill que lo produce — nunca estimás sobre una propuesta, aunque el PM tenga apuro por un número. En un artefacto legacy sin campo `estado`, preguntale al PM una sola vez si lo da por aprobado y registralo en su historial. Escribir `sp_estimado`/`sp_estimado_proyecto` en el frontmatter o la estimación en el artefacto **no revoca** su aprobación: es un metadato de esta skill, no un cambio de contenido. `solution.md`, si ya existe, mejora mucho la precisión (deja ver los componentes técnicos principales) pero no es requisito para correr este modo.
6. **Toda estimación — de proyecto o de historia — suma margen explícito por la fricción del gate de CI/CD mandatorio** (revisión formal de PR por arquitecto/par senior + gate de SAST/cobertura bloqueante antes de poder mergear): si la IDEA previsiblemente se va a construir con muchos PR chicos, o toca código crítico (ledger, validaciones antifraude, aprobación/rechazo de operaciones), señalalo en el racional como factor que empuja el talle o el rango de riesgo hacia arriba. No es un ajuste automático de un porcentaje fijo — es una llamada de atención explícita que el PM confirma o descarta en la revisión.
7. **Cuando exista una estimación de Modo Historias, es la que manda.** Si el proyecto ya tenía una estimación de Modo Proyecto cargada, correr Modo Historias la reemplaza (no conviven las dos como si fueran independientes) — dejalo explícito en el historial de revisiones de dónde estaba antes y por qué se reemplaza.
8. **Historial de revisiones, no texto superpuesto** — si se re-estima algo ya estimado antes (una historia, o la IDEA completa), reescribí la fila/sección limpia y sumá una entrada al historial de revisiones del artefacto correspondiente (regla general de artefactos).
9. **Lo que se escribe en el artefacto de historias, en `proyecto.md` y en el PRD es siempre autocontenido** — la tabla o el racional de cada estimación se lee sin necesitar acceso a este sistema: sin links a la wiki, sin nombres de archivo/skill, sin jerga de proceso interno. `referencia_estimaciones.md` y `log_iniciativas_producto.md` son insumos de trabajo para vos, no algo que el artefacto final linkee o mencione por nombre.
10. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Elegir el modo y precondición común

1. Resolvé la ruta real de la IDEA en la tabla maestra de [`wiki/1_proyectos/index.md`](../../wiki/1_proyectos/index.md) §2.
2. Si existe `-us.md` en `Aprobado por PM` (Paso 5ter de [`/idea_us`](../idea_us/SKILL.md) cerrado con el OK del PM) → seguí por **Modo Historias** (Paso 1-H). Es el modo más preciso; si además ya corriste Modo Proyecto antes sobre esta misma IDEA, esta corrida lo reemplaza (Regla dura 7).
3. Si todavía no hay historias aprobadas pero el PRD está en `Aprobado por PM` → seguí por **Modo Proyecto** (Paso 1-P). Si ninguno de los dos está aprobado, aplicá la Regla dura 5.
4. En cualquiera de los dos casos, verificá en Jira si la IDEA ya tiene sizing técnico real acumulado en sus tickets de desarrollo (`customfield_10041`) — si lo tiene, aplicá la Regla dura 4 antes de continuar.

### Modo Proyecto — dimensionar la IDEA completa apenas hay PRD

#### Paso 1-P — Contexto mínimo

1. Leé el PRD aprobado completo (`artefactos/{{nombre_corto_proyecto}}-prd.md`) — Problema, Solución, Alineación de la solución, Impactos por área (las funcionalidades que sumó la revisión cruzada también cuestan), Riesgos.
2. Si existe, leé también `artefactos/{{nombre_corto_proyecto}}-solution.md` — no es requisito (Regla dura 5), pero si ya identifica los componentes técnicos principales (endpoints, pantallas, integraciones) mejora mucho la analogía del Paso 2-P.
3. Leé el `proyecto.md` del miembro (Definiciones, `riesgos.md`, `decisiones.md`) y, si es miembro de un proyecto general, el §4 del padre — dependencias y riesgos compartidos con otros slices pueden empujar el talle hacia arriba.
4. Si existe `artefactos/{{nombre_corto_proyecto}}-start.md`, leé el tamaño preliminar de shaping de la alternativa aprobada (§5-§6) y su analogía. Es el valor previo: esta corrida lo refina con el PRD (y `solution.md` si existe) y dice explícitamente si confirma, sube o baja ese número, y por qué.

#### Paso 2-P — Buscar la analogía a nivel proyecto

1. Recorré [`log_iniciativas_producto.md`](../../wiki/3_recursos/datos/log_iniciativas_producto.md) buscando una o más IDEAs/Epics históricas del mismo tipo de esfuerzo y dominio (ej. "integración nueva con un proveedor de pagos", "motor de reglas de aprobación", "pantalla de configuración con CRUD simple") — no necesariamente del mismo producto.
2. Si `solution.md` ya desglosa los componentes técnicos principales, podés apoyarte además en `referencia_estimaciones.md` para piezas puntuales conocidas (igual criterio que en Modo Historias), sumando esos números como un piso de referencia — sin necesidad de que existan historias redactadas todavía.
3. Si no hay una analogía razonable ni a nivel proyecto ni a nivel componente, decilo explícito — un rango abierto ("entre 20 y 60 SP, sin analogía histórica cercana") es preferible a inventar una precisión que no existe.

#### Paso 3-P — Factores de riesgo del proyecto

Sumá al racional, con una frase cada uno:
- Riesgos ya documentados en `riesgos.md` del proyecto/miembro (y del padre si aplica).
- Dependencias con otros equipos o con otro miembro del mismo proyecto general.
- Complejidad de integración con terceros (Fintexa, Payway, BCRA, procesadores externos) si el PRD la menciona.
- **Fricción del gate de CI/CD** (Regla dura 6) si el PRD anticipa muchos PR chicos o código crítico (ledger, antifraude, aprobación/rechazo de operaciones).

#### Paso 4-P — Total y rango de riesgo

Un número aproximado de SP (o, si ni siquiera alcanza para un número, un talle S/M/L/XL con su conversión) para la IDEA completa, con rango de riesgo si algún factor del Paso 3-P puede empujarlo hacia arriba — sin desglose por historia, porque las historias no existen todavía.

#### Paso 5-P — Revisión con el PM

**No se registra en ningún lado sin el OK del PM sobre el número.** Presentá el talle/SP, el racional de la analogía y los factores de riesgo antes de escribir nada. Si el PM corrige el número (porque conoce un alcance oculto que la analogía no capturó), reescribí el racional reflejando la corrección.

### Modo Historias — SP por historia, con historias ya confirmadas

#### Paso 1-H — Contexto adicional

1. Abrí el artefacto de historias (`artefactos/{{nombre_corto_proyecto}}-us.md`, generado por `/idea_us`). **Verificá su frontmatter: tiene que decir `estado: Aprobado por PM`** (Regla dura 5). Si dice `Propuesta`, avisá al usuario y no sigas hasta que lo apruebe.
2. Leé también el PRD (`artefactos/{{nombre_corto_proyecto}}-prd.md`), `artefactos/{{nombre_corto_proyecto}}-solution.md` si existe, y el `proyecto.md` del miembro — el racional de cada estimación se apoya en el diseño técnico y los riesgos ya documentados ahí (ej. historial de bugs de un endpoint que se vuelve a tocar, complejidad de un wrapper/integración nueva, o un gap técnico bloqueante que puede subir el talle).
3. Si esta IDEA ya tenía una estimación de Modo Proyecto cargada (`sp_estimado_proyecto` en el PRD), tenela a mano — el Paso 4-H la reemplaza explícitamente, no conviven las dos.

#### Paso 2-H — Estimar cada historia por analogía

Para cada historia del artefacto (en el mismo orden en que aparecen):

1. Resumí en una frase qué es la historia en esencia (más allá del enunciado persona/acción/beneficio) — de qué tipo de trabajo se trata: ¿agregar un campo a un contrato existente? ¿una integración nueva con un proveedor? ¿una config sin lógica? ¿un motor de reglas nuevo?
2. Buscá en `referencia_estimaciones.md` el desarrollo histórico más parecido — mismo tipo de esfuerzo (integración nueva, extensión de un flujo maduro, config, mapeo de errores, etc.), no necesariamente mismo producto.
3. Asigná un talle (S/M/L/XL) y su conversión a SP, con el racional de la analogía en una frase.
4. **Si la historia depende de o se apoya en trabajo compartido con otro miembro del mismo proyecto general** (ej. una estructura de datos que también usará otro PRD), señalalo explícitamente en el racional — puede justificar un talle mayor al que tendría la historia aislada.
5. **Si la historia toca de nuevo un endpoint/flujo con historial de bugs documentado** (cluster de bugs conocido, ver `referencia_estimaciones.md` y el `proyecto.md`/PRD de la IDEA), señalalo como riesgo de que el talle real termine siendo mayor — no lo escondas en el número final, decilo en el racional.
6. **Si la historia va a implicar varios PR chicos, o toca código crítico** (ledger, validaciones antifraude, aprobación/rechazo de operaciones), aplicá la Regla dura 6 y señalalo en el racional como factor de fricción del gate de CI/CD.

#### Paso 3-H — Total y rango de riesgo

Sumá los SP de todas las historias para el total de la IDEA. Si alguna historia tiene riesgo real de subir de talle (Paso 2-H, puntos 4 a 6), agregá un rango superior (ej. "19–34 SP") con una frase de qué lo empujaría hacia arriba — no dejes el rango sin justificar.

#### Paso 4-H — Revisión con el PM

**No se registra en ningún lado sin el OK del PM sobre los números.** Presentá la tabla completa (historia | talle | SP | racional) y el total antes de escribir nada. Si el PM corrige un talle (como puede pasar, ej. porque conoce un alcance oculto que la analogía no capturó), reescribí esa fila con el nuevo racional — no dejes el racional viejo compitiendo con la corrección. Si esta IDEA tenía una estimación de Modo Proyecto previa, dejá explícito en la presentación que este número la reemplaza.

## 📄 Formato de salida

**Modo Historias:** tabla markdown `Historia | Talle | SP | Racional`, más una fila de Total con el rango de riesgo si aplica. Ver el ejemplo real en la sección "Estimación preliminar de Producto (SP)" de [`historias_alta_comitente_id_cuenta.md`](../../wiki/1_proyectos/proyecto-remediar-onboarding/prd-208_alta_comitente_id_cuenta/artefactos/historias_alta_comitente_id_cuenta.md#estimación-preliminar-de-producto-sp) (PRD-208, primera IDEA que corrió esta skill).

**Modo Proyecto:** un bloque breve, no tabular (no hay historias que desglosar): talle/SP aproximado de la IDEA completa, racional de la analogía (qué IDEA histórica de `log_iniciativas_producto.md` se usó de referencia), lista de factores de riesgo con una frase cada uno (Paso 3-P), y el rango de riesgo si aplica.

## ✅ Checklist de calidad

- [ ] Se identificó correctamente el modo a correr — Proyecto si no hay historias todavía, Historias si ya están confirmadas (Paso 0)
- [ ] Modo Proyecto: el PRD estaba en `Aprobado por PM` antes de estimar (nunca se estimó sobre una `Propuesta`)
- [ ] Modo Historias: el artefacto de historias estaba en `Aprobado por PM` antes de estimar
- [ ] La historia (Modo Historias) o la IDEA completa (Modo Proyecto) tiene una analogía histórica concreta citada en el racional — nunca un número sin justificar
- [ ] La escala de conversión talle→SP es la vigente (`S=1·M=3·L=7·XL=15`)
- [ ] Se señaló explícitamente si la fricción del nuevo gate de CI/CD (muchos PR chicos, o código crítico como ledger/antifraude) empuja el talle o el rango hacia arriba, cuando aplica (Regla dura 6)
- [ ] Modo Historias: las historias con riesgo de bugs/cola de estabilización lo señalan explícitamente, no solo en el número
- [ ] El PM dio su OK explícito a la estimación completa antes de registrarla en cualquier lado
- [ ] Se verificó que no había sizing técnico real ya cargado en Jira antes de escribir el campo de la IDEA
- [ ] Si existía una estimación de Modo Proyecto previa y esta corrida es Modo Historias, quedó explícito que la reemplaza (Regla dura 7)

## Paso de cierre estándar

### Si corriste Modo Proyecto

1. **`proyecto.md` del miembro:** agregá (o reescribí, si ya existía de una corrida anterior) una sección "Estimación preliminar de Producto (SP) — Modo Proyecto" con el talle/SP, el racional de la analogía (qué IDEA de `log_iniciativas_producto.md` se usó) y los factores de riesgo del Paso 3-P. Sumá una entrada al historial de revisiones al pie, subí la versión del frontmatter.
2. **PRD:** agregá `sp_estimado_proyecto: <total>` al frontmatter — distinto de `sp_estimado`, que se reserva para cuando corra Modo Historias — y completá la línea de "Costo de construir" en la sección Caso de negocio, dejando explícito que es una estimación de proyecto completo, sin historias todavía, sujeta a reemplazo (sin linkear al `proyecto.md` — el PRD tiene que leerse solo). Sumá entrada al historial de revisiones, subí versión.
3. **Jira:** actualizá el campo `customfield_10389` ("SP estimado") de la IDEA con `editJiraIssue` al total calculado, dejando en el comentario o la nota que es una estimación de Modo Proyecto (preliminar, sin historias todavía). Si el campo ya tenía un valor cargado por otra persona (no por esta skill), avisá al usuario antes de sobrescribir. Un valor cargado por `/idea_start` (preliminar de shaping) se sobrescribe sin pedir confirmación (Regla dura 4).
4. **Índices:** verificá igual la regla general de integridad de índices por si el cambio amerita actualizar una descripción.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
6. Siguiente paso sugerido: [`/idea_us`](../idea_us/SKILL.md) para descomponer el PRD en historias. Cuando el PM las apruebe (`-us.md` en `Aprobado por PM`), volvé a correr esta skill en Modo Historias para reemplazar esta estimación por una más precisa (Regla dura 7).

### Si corriste Modo Historias

1. **Artefacto de historias:** agregá (o reescribí, si ya existía de una corrida anterior) la sección "Estimación preliminar de Producto (SP)" con la tabla completa, el total y el rango de riesgo si aplica — inmediatamente después de la tabla de "Resumen de priorización". Completá también el campo "Estimación" de la cabecera de cada historia individual. Sumá una entrada al historial de revisiones al pie con el detalle de la estimación y, si corrigió un número inicial o reemplazó una estimación de Modo Proyecto, qué cambió y por qué. Subí la versión del frontmatter.
2. **PRD:** agregá `sp_estimado: <total>` al frontmatter y completá la línea de "Costo de construir" en la sección Caso de negocio con el total y el rango de riesgo si aplica (sin linkear al artefacto de historias — el PRD tiene que leerse solo) — dejando explícito que es preliminar de Producto, no sizing técnico. Si existía `sp_estimado_proyecto` de una corrida previa de Modo Proyecto, dejalo en el historial de revisiones como reemplazado, no lo borres en silencio. Sumá entrada al historial de revisiones, subí versión.
3. **Jira:** actualizá el campo `customfield_10389` ("SP estimado") de la IDEA con `editJiraIssue` al total calculado. Si el campo ya tenía un valor distinto cargado por una corrida anterior de esta skill (Modo Proyecto o Modo Historias) o por `/idea_start` (preliminar de shaping), sobrescribilo sin pedir confirmación (es el mismo tipo de dato, Regla dura 4); si tenía un valor que no vino de esta skill (ej. cargado a mano por otra persona), avisá al usuario antes de sobrescribir.
4. **Índices:** no suele hacer falta tocar `wiki/1_proyectos/index.md` (no cambia la ruta ni la existencia del artefacto) — verificá igual la regla general de integridad de índices por si el cambio de versión amerita una actualización de descripción.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
6. Siguiente paso sugerido: [`/idea_jira`](../idea_jira/SKILL.md) para crear (o actualizar) la jerarquía IDEA→Epic→Historia en Jira, ahora que la IDEA ya tiene SP estimado — esa skill lo toma del frontmatter del PRD. El sizing técnico real por ticket (`customfield_10041`) lo carga Ingeniería después, en su propio refinamiento; queda disponible en Jira para cuando exista de nuevo una skill que lo recoja (`/sync_jira_ideas` se deprecó el 2026-08-15).
