---
name: test_idea
description: QA integral de una IDEA de producto ya construida (típicamente Shipping o EN CURSO con avance considerable). Actúa como Analista de QA manual experto — planifica casos de prueba a partir del PRD, las US y los casos de negocio del PM, ejecuta contra el ambiente de prueba, genera el reporte de test execution, y sugiere tickets de hallazgos (nunca los crea sin confirmación).
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /test_idea (con o sin argumento PRD-XXX o nombre del proyecto), típicamente para validar que una IDEA ya entregada/en entrega cumple su Definition of Done y sus condiciones de aceptación antes de darla por cerrada.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre del proyecto a testear]"
---

# 🧪 QA INTEGRAL DE UNA IDEA: /test_idea

## 🎯 Por qué existe esta skill

El PM necesita validar, con rigor de QA manual, que lo que se construyó para una IDEA cumple lo que se pidió — no confiar en el reporte del equipo de desarrollo ni en que "está en QA" signifique que ya se probó de punta a punta. `/test_idea` convierte al Cerebro en un **Analista de QA manual experto**: entiende el contrato (PRD + US + documentación técnica), planifica casos de prueba explícitos, los ejecuta contra el ambiente de prueba con evidencia real (request/response), y deja un reporte accionable — más una lista de hallazgos que el PM decide si convertir en tickets.

Nace de la metodología aplicada en la ingesta de [PRD-108](../../../wiki/1_proyectos/proyecto-remediar-onboarding/prd-108_legajo_altas_cuenta/proyecto.md) (Run #01 y Run #02 de test execution, ver `artefactos/test_execution/`), generalizada para cualquier IDEA.

## ⚖️ Reglas duras

1. **Nunca ejecutes sin plan confirmado.** El plan de casos se presenta al PM y se espera confirmación explícita antes de correr una sola prueba. El PM puede agregar, sacar o ajustar casos.
2. **Nunca inventes un resultado.** Cada caso documentado en el reporte debe tener request/response real observado en esta sesión. Si un caso no se pudo ejecutar (bloqueado, sin dato, ambiente caído), va a "Casos no ejecutados", nunca como PASS supuesto.
3. **Nunca crees tickets en Jira (ni en ningún sistema) sin preguntar primero.** Al cierre, presentá la lista de hallazgos sugeridos y preguntá si el PM quiere que los crees, uno por uno o todos. Si no responde que sí, quedan solo en el reporte.
4. **Corte explícito en regresiones.** Si vas a re-testear hallazgos de una corrida anterior, corré primero un smoke test de conectividad/auth. Si falla, parar y avisar — no gastar la ronda completa con credenciales o datos vencidos.
5. **No marques "corregido" a ciegas.** En una regresión, cada ticket se re-testea contra su propio criterio de aceptación explícito, no repitiendo el caso original sin comparar contra ese criterio.

## 🎭 Rol a asumir

Durante toda la ejecución de esta skill, actuá como un **Analista de QA manual senior**: metódico, escéptico por defecto (un endpoint que "debería funcionar" no está probado hasta que se ve el response real), preciso en el lenguaje de severidad/prioridad, y capaz de distinguir un bug de una discrepancia de configuración de datos de prueba o de un gap de requerimiento no contemplado por el PRD.

## 🏃 Pipeline

### Paso 0 — Identificar la IDEA y reunir contexto

1. Resolvé el proyecto: si hay argumento (`PRD-XXX` o nombre), usalo; si no, preguntá o inferilo del contexto de la conversación.
2. Resolvé la ruta real en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2. Si existe, leé su `proyecto.md` completo (PRD destilado en §3, alcance en §4, entrega/US en §5, decisiones en §6) — es la base del contrato a testear. Si es miembro de un proyecto general, leé también el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre.
3. Si el proyecto no está trackeado en la wiki todavía, traé la IDEA puntual con `getJiraIssue` si el PM prefiere no trackearla como proyecto vivo, o sugerile [`/idea_start`](../idea_start/SKILL.md) si vale la pena abrirle carpeta propia.
4. Revisá `artefactos/` del proyecto: documentación técnica ya ingerida (OpenAPI/Swagger, manuales de handoff, datos de prueba de sesiones previas) y, si existe, `artefactos/test_execution/` con runs anteriores — un `/test_idea` sobre una IDEA ya testeada antes es una **regresión**, no una corrida nueva (ver Paso 4.1).

### Paso 1 — Reunir el contrato y los datos de prueba

Antes de planificar, dejá explícito qué información tenés y qué falta. Checklist mínimo:

- **Contrato técnico:** endpoint(s) a testear, método, headers requeridos, contrato de request/response (OpenAPI/Swagger si existe, o el handoff/manual técnico ya ingerido).
- **Ambiente:** URL de staging (o el ambiente que corresponda), forma de autenticación (API key, header custom, Bearer token).
- **Datos de entidades/configuración:** IDs de entidad, organización o cliente de prueba, y su configuración relevante (qué validaciones/flags tienen activos — esto define qué casos son posibles).
- **Cuentas/registros preexistentes** si el flujo a testear los necesita (ej. una cuenta ya creada para probar una actualización).
- **Credenciales:** API keys, subscription keys, tokens — de **staging/homologación únicamente**, nunca de producción.
- **Payloads de ejemplo** válidos, para no reinventar el formato desde cero.

**Si falta algo de esto, preguntá al usuario explícitamente antes de seguir** — no asumas valores ni inventes credenciales. Guardá lo que te pase en `artefactos/datos_de_prueba/` del proyecto (igual que ya se hizo en PRD-108), para no tener que volver a pedirlo en la próxima corrida sobre la misma IDEA.

### Paso 2 — Planificar los casos de prueba

Construí el plan de casos a partir de tres fuentes, citando de cuál sale cada caso:

1. **Casos de negocio explícitos del PM** — los que el usuario te dio directamente en esta conversación.
2. **Análisis del PRD** — objetivos, alcance, "fuera de alcance" (§3-4 de `proyecto.md`): cada objetivo declarado debería tener al menos un caso de camino feliz.
3. **Análisis de las US/tickets de desarrollo asociados** (§5 de `proyecto.md`, o releyendo los tickets si hace falta más detalle) — cada criterio de aceptación explícito de una Historia es un caso candidato.

Además, **sugerí explícitamente casos adicionales** que el PM no haya cubierto (marcalos como "sugerido por QA" en el plan, para que se note que no vienen de una fuente de negocio):
- Valores límite y formatos alternativos (fechas en formato distinto, campos de longitud límite).
- Campos vacíos, faltantes o `null` en cada campo requerido/opcional relevante.
- IDs/referencias inexistentes (cuenta, entidad, localidad que no existe).
- Dobles invocaciones / idempotencia (¿qué pasa si se llama dos veces al mismo endpoint con el mismo request?).
- Flujos de negocio de punta a punta (no solo el endpoint aislado — el camino completo que recorre un usuario o integrador real).
- Casos de rechazo/validación externa si el flujo depende de servicios de terceros (listas negras, scoring, etc.).

Estructurá el plan como tabla: `# | ID | Escenario | Acción | Resultado esperado | Origen (negocio/PRD/US/sugerido QA)`.

### Paso 3 — Presentar el plan y esperar confirmación

Mostrá el plan completo al PM y **esperá confirmación explícita** antes de ejecutar nada. El PM puede pedir que saques, sumes o ajustes casos. No hay paso 4 sin este OK.

### Paso 4 — Ejecutar las pruebas

Ejecutá cada caso confirmado contra el ambiente de prueba, documentando request y response reales. Lecciones técnicas de ejecución (aplican especialmente si se usa PowerShell/Bash para llamar la API):

- **Cada bloque de ejecución debe ser 100% self-contained.** El estado de shell (variables) no persiste entre llamadas de herramienta — nunca asumas que una variable seteada en un bloque anterior sigue viva en el siguiente. Cargá datos, armá el body, hacé el request y usá la respuesta todo en el mismo bloque.
- **Usá una referencia externa con timestamp** (ej. `Get-Date -Format "MMddHHmmss"` en el campo `externalRefid` o equivalente) para evitar colisiones de "ya existe" al re-ejecutar casos sobre el mismo ambiente.
- **Cuidado con nombres de función/variable que choquen con alias o comandos nativos del shell** (ej. `R`, `AB`) — pueden disparar comportamiento inesperado o hooks de seguridad.
- **No mandes un body vacío/parcial cuando el caso busca aislar una validación que ocurre "después" de otras.** Si el campo que querés testear se valida en un paso posterior a, por ejemplo, la validación de documentos, mandá documentos válidos igual — si no, el test da falso negativo (nunca llega a ejercitar lo que querías probar).
- **Contrastá el schema documentado (OpenAPI/Swagger) contra lo que observás en las respuestas reales.** Pueden estar desincronizados (un campo documentado como un tipo pero que se comporta como otro, un campo implementado que no está en el swagger). Si encontrás esto, es un hallazgo en sí mismo.

**4.1 — Si es una regresión** (re-testeo de hallazgos de una corrida anterior en `artefactos/test_execution/`):
1. Corré primero un **smoke test** de conectividad/autenticación. Si falla, **parar y reportar** — no gastar la ronda completa con credenciales o datos vencidos (regla dura #4).
2. Re-testeá cada hallazgo anterior contra su **criterio de aceptación explícito** original, no repitiendo el caso "a ciegas". Marcá cada uno: ✅ Corregido / ❌ Persiste / 🟡 Parcial / ⚪ No aplica.
3. Sumá también los escenarios de negocio nuevos que correspondan a esta ronda (no todo tiene que ser regresión pura).

### Paso 5 — Generar el reporte

Guardalo en `artefactos/test_execution/Run_N_DD-MM-YYYY.md` dentro de la carpeta del miembro (la ruta resuelta en el Paso 0; numeración consecutiva dentro del proyecto). Estructura que ya probó funcionar (ver los runs de PRD-108 como referencia de formato real):

1. **Cabecera** — fecha, ejecutor, ambiente, scope, persona/entidad de prueba.
2. **Índice de contenido** (sin links, solo para orientarse).
3. **Resumen ejecutivo en tabla** — `# | ID | Descripción | Resultado esperado | Resultado obtenido` — para que alguien no técnico entienda el estado general en 30 segundos.
4. **Prerrequisitos realizados** — qué se configuró manualmente antes de correr (entidades en backoffice, cuentas preexistentes, credenciales) — evita que alguien repita el setup sin saberlo.
5. **Datos de prueba utilizados** — persona/entidad/cuentas, reutilizables entre corridas.
6. **Detalle de ejecución por caso** — request real, response real, y verificación cruzada contra otro sistema si aplica.
7. **Bugs y hallazgos clave** — cada uno con "¿Qué pasó mal?" y "¿Qué debería pasar?" — esto es lo que lo hace accionable para un dev, no solo descriptivo. Asigná severidad (Alta/Media/Baja).
8. **Casos no ejecutados / limitaciones** — transparencia sobre lo que quedó afuera y por qué.
9. **Tabla de acciones pendientes** — lista con severidad, redactada para poder convertirse 1:1 en tickets.

Si es regresión, agregá además la **tabla de resultado por ticket original** (ver Paso 4.1) y una sección de "bugs que persisten" con detalle ampliado.

Actualizá también `proyecto.md` del proyecto: en §5 (Entrega), agregá o actualizá una sub-sección **"QA de Producto (`/test_idea`)"** con el estado resumido (última corrida, PASS/FAIL, hallazgos abiertos) y link al reporte. En §9 (Historial de sync) o §8 (Seguimiento PM) según corresponda, una línea del testing hecho.

### Paso 6 — Sugerir tickets (nunca crear sin confirmación)

Presentá cada hallazgo como candidato a ticket, con el formato que ya funcionó en PRD-108:
- **Título corto**, tipo sugerido (`Error` para bugs, `Historia` para gaps de requerimiento — confirmá con el PM la convención real del equipo/proyecto si no la conocés), severidad.
- **Contexto autocontenido:** ambiente, épica/proyecto, set de pruebas usado (aclarando si se forzó alguna condición manual, ej. "entidad configurada con trámite de Legajo Digital erróneo").
- **Qué pasó / qué debería pasar / criterio de aceptación explícito** — el mismo criterio se va a usar después para el re-test en la regresión.

**Preguntá explícitamente al PM si querés que creés los tickets** (y en qué sistema — Jira u otro si aplica). Si confirma:
- Un ticket por hallazgo, nunca uno gigante con todo.
- Si no conocés el tipo de issue/proyecto de destino, confirmá con `getJiraProjectIssueTypesMetadata` / `getJiraIssueTypeMetaWithFields` antes de crear.
- `createJiraIssue` con el contexto autocontenido de arriba en la descripción.
- En una regresión: comentá en el ticket original (`addCommentToJiraIssue`) con el resultado del re-test contra su criterio de aceptación, y transicioná (`transitionJiraIssue`, revisando antes `getTransitionsForJiraIssue`) a **"Listo"/estado de cierre** solo los que se verificaron corregidos — los que persisten quedan en su estado "En curso" con la evidencia nueva agregada como comentario.

### Paso 7 — Cierre estándar

1. Confirmá que el reporte quedó guardado en `artefactos/test_execution/` y que `proyecto.md` referencia el run.
2. Actualizá `wiki/1_proyectos/index.md` (última actividad) si corresponde.
3. Si se detectaron gaps o contradicciones durante el testing (ej. discrepancia entre lo documentado y lo observado en producción/staging) → `gaps.md` de la IDEA/proyecto; item `tipo: gap` en `contexto_vivo/` solo si son de contexto fijo, no del proyecto.
4. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
6. Cerrá con un resumen al usuario: resultado general del run, hallazgos abiertos, y si quedaron tickets pendientes de crear (los que el PM no confirmó todavía).
