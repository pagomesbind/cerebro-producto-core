---
name: idea_estimate
description: Carga una estimación preliminar de Story Points (por analogía con desarrollos históricos similares) sobre las historias de usuario ya confirmadas de una IDEA, y la registra como atributo de referencia en el artefacto de historias, en el PRD y en el campo "SP estimado" de la IDEA en Jira. Se activa con /idea_estimate.
when_to_use: Se activa cuando el usuario ejecuta /idea_estimate, siempre después de que el PM haya confirmado y esté de acuerdo con las historias de usuario creadas por /idea_us (Paso 5bis de esa skill ya cerrado) — nunca antes.
disable-model-invocation: true
argument-hint: "[PRD-XXX]"
---

# 📐 ESTIMACIÓN PRELIMINAR DE PRODUCTO (SP): /idea_estimate

## Por qué existe esta skill

Antes de que Ingeniería refine y sizee cada historia en su propio espacio de Jira (Wallet/WS, Adquirencia/AD, Onboarding/OB, Ardid/ARD, Servicios/SER), Producto necesita un número de esfuerzo aproximado para dimensionar la IDEA — priorizar contra otras IDEAs, conversar capacidad con Ingeniería, o simplemente saber si "esto es chico o grande" antes de comprometer una fecha. Esta skill no reemplaza el sizing técnico real: es una **estimación a alto nivel desde Producto**, construida por analogía con el historial de esfuerzo real ya relevado en [`referencia_estimaciones.md`](../../wiki/2_areas/procesos/referencia_estimaciones.md) — el mismo insumo que ya usa el equipo para estimar desarrollos nuevos comparándolos con desarrollos similares del pasado.

## Cuándo NO usarla

- Las historias de usuario todavía no existen o no fueron confirmadas por el PM → corré primero [`/idea_us`](../idea_us/SKILL.md) y cerrá su Paso 5bis (revisión iterativa con el PM) antes de estimar.
- Lo que se necesita es el sizing técnico real de Ingeniería → esta skill no lo reemplaza ni lo anticipa; solo carga la referencia preliminar de Producto. El sizing real se registra en Jira por el propio equipo técnico cuando refina cada historia en su espacio (`customfield_10041` a nivel ticket).
- La IDEA ya tiene un sizing técnico real cargado y confirmado por Ingeniería → no sobrescribas ese número con una estimación de analogía; si el PM igual quiere una referencia de Producto en paralelo, aclarálo explícitamente en el registro para no confundir ambas fuentes.

## ⚖️ Reglas duras

1. **Es una estimación de alto nivel desde Producto, nunca el sizing técnico.** Todo lugar donde se registre este número (artefacto de historias, PRD, campo de Jira) debe dejarlo explícito — Ingeniería refina y sizea cada historia después, en su propio espacio Jira.
2. **Estimá por analogía, no de la nada.** Cada historia se compara contra un desarrollo histórico similar ya relevado en `referencia_estimaciones.md` (o, si no hay analogía directa, contra otra historia ya estimada del mismo dominio) — cada número debe poder justificarse con un "se parece a X, que costó Y".
3. **Usá la escala vigente de Bind PSP:** `S = 1 SP · M = 3 SP · L = 7 SP · XL = 15 SP` (confirmada en [`gestion_jira.md` §1.4](../../wiki/2_areas/procesos/gestion_jira.md#14-prioridad-versión-y-story-points)). No inventes otra escala ni mezcles Story Points directos con talles de camiseta sin convertir.
4. **Nunca sobrescribas un sizing técnico real ya cargado** sin que el usuario lo pida explícitamente — si `customfield_10041` (SP real) ya tiene valores en los tickets de desarrollo de la IDEA, avisá y preguntá antes de tocar el campo de la IDEA.
5. **Historial de revisiones, no texto superpuesto** — si se re-estima una historia ya estimada antes, reescribí la fila limpia y sumá una entrada al historial de revisiones del artefacto de historias (regla general de artefactos).
6. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto y precondición

1. Resolvé la ruta real de la IDEA en la tabla maestra de [`wiki/1_proyectos/index.md`](../../wiki/1_proyectos/index.md) §2.
2. Abrí el artefacto de historias (`artefactos/historias_<tema>.md`, generado por `/idea_us`). **Verificá que el Paso 5bis de esa skill ya haya cerrado** — el documento tiene que reflejar el estado con el que el PM está de acuerdo (sin `[pendiente revisión]` ni correcciones abiertas). Si no está confirmado, avisá al usuario y no sigas.
3. Leé también el PRD (`artefactos/YYYY-MM-DD_prd_<tema>.md`) y el `proyecto.md` del miembro — el racional de cada estimación se apoya en el diseño técnico y los riesgos ya documentados ahí (ej. historial de bugs de un endpoint que se vuelve a tocar, complejidad de un wrapper/integración nueva).
4. Verificá en Jira si la IDEA ya tiene sizing técnico real acumulado en sus tickets de desarrollo (`customfield_10041` a nivel ticket) — si lo tiene, aplicá la Regla dura 4 antes de continuar.

### Paso 1 — Estimar cada historia por analogía

Para cada historia del artefacto (en el mismo orden en que aparecen):

1. Resumí en una frase qué es la historia en esencia (más allá del enunciado persona/acción/beneficio) — de qué tipo de trabajo se trata: ¿agregar un campo a un contrato existente? ¿una integración nueva con un proveedor? ¿una config sin lógica? ¿un motor de reglas nuevo?
2. Buscá en `referencia_estimaciones.md` el desarrollo histórico más parecido — mismo tipo de esfuerzo (integración nueva, extensión de un flujo maduro, config, mapeo de errores, etc.), no necesariamente mismo producto.
3. Asigná un talle (S/M/L/XL) y su conversión a SP, con el racional de la analogía en una frase.
4. **Si la historia depende de o se apoya en trabajo compartido con otro miembro del mismo proyecto general** (ej. una estructura de datos que también usará otro PRD), señalalo explícitamente en el racional — puede justificar un talle mayor al que tendría la historia aislada.
5. **Si la historia toca de nuevo un endpoint/flujo con historial de bugs documentado** (cluster de bugs conocido, ver `referencia_estimaciones.md` y el `proyecto.md`/PRD de la IDEA), señalalo como riesgo de que el talle real termine siendo mayor — no lo escondas en el número final, decilo en el racional.

### Paso 2 — Total y rango de riesgo

Sumá los SP de todas las historias para el total de la IDEA. Si alguna historia tiene riesgo real de subir de talle (Paso 1.5), agregá un rango superior (ej. "19–34 SP") con una frase de qué lo empujaría hacia arriba — no dejes el rango sin justificar.

### Paso 3 — Revisión con el PM

**No se registra en ningún lado sin el OK del PM sobre los números.** Presentá la tabla completa (historia | talle | SP | racional) y el total antes de escribir nada. Si el PM corrige un talle (como puede pasar, ej. porque conoce un alcance oculto que la analogía no capturó), reescribí esa fila con el nuevo racional — no dejes el racional viejo compitiendo con la corrección.

## 📄 Formato de salida

Tabla markdown: `Historia | Talle | SP | Racional`, más una fila de Total con el rango de riesgo si aplica. Ver el ejemplo real en la sección "Estimación preliminar de Producto (SP)" de [`historias_alta_comitente_id_cuenta.md`](../../wiki/1_proyectos/proyecto-remediar-onboarding/prd-208_alta_comitente_id_cuenta/artefactos/historias_alta_comitente_id_cuenta.md#estimación-preliminar-de-producto-sp) (PRD-208, primera IDEA que corrió esta skill).

## ✅ Checklist de calidad

- [ ] El artefacto de historias tenía el Paso 5bis de `/idea_us` ya cerrado antes de estimar
- [ ] Cada historia tiene una analogía histórica concreta citada en el racional (no un número sin justificar)
- [ ] La escala de conversión talle→SP es la vigente (`S=1·M=3·L=7·XL=15`)
- [ ] Las historias con riesgo de bugs/cola de estabilización lo señalan explícitamente, no solo en el número
- [ ] El PM dio su OK explícito a la tabla completa antes de registrarla en cualquier lado
- [ ] Se verificó que no había sizing técnico real ya cargado en Jira antes de escribir el campo de la IDEA

## Paso 4 — Cierre estándar

1. **Artefacto de historias:** agregá (o reescribí, si ya existía de una corrida anterior) la sección "Estimación preliminar de Producto (SP)" con la tabla completa, el total y el rango de riesgo si aplica — inmediatamente después de la tabla de "Resumen de priorización". Completá también el campo "Estimación" de la cabecera de cada historia individual. Sumá una entrada al historial de revisiones al pie con el detalle de la estimación y, si corrigió un número inicial, qué cambió y por qué. Subí la versión del frontmatter.
2. **PRD:** agregá `sp_estimado: <total>` al frontmatter y completá la línea de "Costo de construir" en la sección Caso de negocio con el total y un link a la tabla detallada del artefacto de historias — dejando explícito que es preliminar de Producto, no sizing técnico. Sumá entrada al historial de revisiones, subí versión.
3. **Jira:** actualizá el campo `customfield_10389` ("SP estimado") de la IDEA con `editJiraIssue` al total calculado. Si el campo ya tenía un valor distinto cargado por una corrida anterior de esta skill, sobrescribilo sin pedir confirmación (es el mismo tipo de dato); si tenía un valor que no vino de esta skill (ej. cargado a mano por otra persona), avisá al usuario antes de sobrescribir.
4. **Índices:** no suele hacer falta tocar `wiki/1_proyectos/index.md` (no cambia la ruta ni la existencia del artefacto) — verificá igual la regla general de integridad de índices por si el cambio de versión amerita una actualización de descripción.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
7. Siguiente paso sugerido: ninguno automático — el siguiente hito natural es que Ingeniería refine y sizee cada historia en su propio espacio Jira (fuera del alcance de esta skill); ese SP real por ticket (`customfield_10041`) queda disponible en Jira para cuando exista de nuevo una skill que lo recoja (`/sync_jira_ideas` se deprecó el 2026-08-15).
