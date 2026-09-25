---
name: idea_prd
description: Genera un Product Requirements Document (PRD) completo — qué se va a construir, por qué, y cómo se mide el éxito — para handoff formal a ingeniería. Se activa con /idea_prd.
when_to_use: Se activa cuando el usuario ejecuta /idea_prd, típicamente cuando el problema y la solución ya están alineados y hace falta un documento de especificación formal para coordinar múltiples equipos o para que stakeholders aprueben alcance antes de invertir.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre de la iniciativa a especificar]"
---

<!-- Adaptado de product-on-purpose/pm-skills (deliver-prd), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->
<!-- Estructura de Alineación de la solución / Checklist operativo por área adaptada del PRD Template de un Head of Product de Stripe (mayo 2025). -->

# 📋 PRD FORMAL: /idea_prd

## Por qué existe esta skill

`proyecto.md` en `wiki/1_proyectos/` es el estado vivo de una IDEA — decisiones, gaps, seguimiento PM, todo en evolución constante. Un PRD es otra cosa: un documento de especificación **congelado en un momento dado**, pensado para que ingeniería, QA y stakeholders lean una sola vez y entiendan qué se va a construir, por qué, y dónde están los límites de alcance. Esta skill no reemplaza a `proyecto.md` — lo destila en un artefacto formal de handoff cuando hace falta uno (coordinación multi-equipo, aprobación de stakeholders, documento de referencia durante desarrollo/QA).

## Cuándo NO usarla

- El problema todavía no está enmarcado o está en discusión → usá primero [`/idea_start`](../idea_start/SKILL.md); un PRD asume un problema ya acordado.
- El diseño de la solución todavía no existe → usá primero [`/idea_solution`](../idea_solution/SKILL.md); el PRD destila ese análisis en un resumen (Paso 3), no lo inventa desde cero.
- Solo hace falta bajar el trabajo a historias de usuario para un sprint, sin necesidad de un documento de especificación completo → usá directamente [`/idea_us`](../idea_us/SKILL.md).
- Lo que se necesita es registrar una decisión técnica o arquitectónica puntual, no especificar una iniciativa de producto completa.

## ⚖️ Reglas duras

1. **Protocolo de contexto:** aplicá el Paso 0 antes de escribir una sola línea del PRD.
2. **No prescribas implementación de bajo nivel.** El PRD no elige lenguaje, framework, esquema de base de datos ni topología de despliegue — eso lo define ingeniería. Explicar cómo funciona la solución de cara al negocio (quiénes participan, en qué orden pasan las cosas, qué ocurre cuando algo falla) **no es prescribir implementación** — es justo lo que exige el resumen del Paso 3, y es lo que distingue un PRD legible de uno que enumera funcionalidades sin decir cómo se resuelven.
3. **Todo objetivo tiene que ser SMART y medible.** Alguien debería poder verificar en el futuro si se cumplió o no, sin ambigüedad.
4. **Alcance explícito**: qué entra, qué no entra, y qué queda diferido — nunca lo dejes implícito. La Alineación de la solución dibuja el perímetro, no llena el interior: el equipo decide cómo construir dentro de ese borde.
5. Legible en menos de 15 minutos. Si no entra, es señal de que el alcance es demasiado grande para un solo PRD.
6. Todo output en español.
7. **Nombrá la solución por lo que efectivamente se construye**, no por una abstracción ambigua que suene a un proceso o servicio ya existente (ej. "nuevas funcionalidades por API para favorecer X", no "el proceso de X"). Aplica sobre todo en el Resumen de la solución planteada y en Funcionalidades clave.
8. **El PRD siempre es autocontenido, sin excepción.** Es la previa a un documento formal que el PM va a revisar, iterar y en algún momento entregar a alguien sin acceso a este sistema (ingeniería, un stakeholder externo a Bind PSP, otra área sin contexto del Cerebro) — nunca se sabe de antemano si esa instancia llega hoy o en la próxima vuelta, así que el cuerpo del documento se escribe siempre para ese lector. Eso significa: sin links a la wiki, sin nombres de archivo o de skill, sin códigos de ticket (PRD-XXX) usados como si el lector los reconociera, sin jerga de proceso interno ("gap registrado en...", "según el artefacto..."). Toda afirmación se explica en el propio texto, en prosa que alguien sin contexto de este sistema pueda leer de punta a punta. (La trazabilidad hacia la wiki — problem statement, `proyecto.md`, decisiones — vive en el proceso de armado del Paso 0 y en cómo `proyecto.md` referencia al PRD, no en el cuerpo del artefacto.)
9. **En el Checklist operativo por área, ninguna respuesta es un Sí/No pelado.** Toda fila explica por qué en una oración concreta, y una respuesta no se inventa: si no hay información para evaluar una pregunta, la fila queda `Pendiente` con la pregunta abierta, nunca con una explicación fabricada.
10. **Todo movimiento de fondos, comprobante o tipo de operación nuevo analiza junto, no por separado, sus tres impactos operativos: conciliación, monitoreo y fraude.** Es el patrón de causa raíz del incidente de Transferencias Pull de marzo 2026 — la funcionalidad salió sin que Conciliación supiera que tenía que cuadrarla, sin monitoreo de negocio y sin integración al motor antifraude. En el Paso 8, si la fila de **Recaudaciones/Conciliación** responde Sí a que genera un movimiento/comprobante nuevo, revisá en el mismo momento — no en una pasada separada — si eso también dispara una fila Sí en **Fraude** (reglas o parámetros de monitoreo transaccional nuevos, esquema de monitoreo operativo nuevo). Las tres preguntas quedan respondidas juntas o ninguna se da por cerrada.
11. **En el Checklist operativo por área, toda pregunta del catálogo de referencia (Paso 8) se responde siempre, en todas las áreas — nunca se poda en silencio.** El catálogo es un piso, no un menú: si una pregunta no aplica a este proyecto, la fila se arma igual, con respuesta "No aplica" y el motivo en una oración — la ausencia de una fila es indistinguible de un olvido, y el valor del checklist es justamente dejar constancia de que se evaluaron todas. Ampliar el catálogo con una pregunta nueva y específica de este proyecto está bien y se alienta; omitir una que ya está en el catálogo de referencia porque "no parece relevante a primera vista" no.

## 🏃 Pipeline

### Paso 0 — Contexto antes de escribir

1. Resolvé la ruta real de la IDEA en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 — nunca asumas `wiki/1_proyectos/prd-XXX_<slug>/` directo. Leé su `proyecto.md` completo — problema, alcance, decisiones y gaps ya registrados son la base del PRD, no se reinventan acá.
2. **Si es miembro de un proyecto general** (tiene cabecera `> **Proyecto:** [<Nombre>](../proyecto.md)`), leé también el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre — son decisiones ya cerradas a nivel proyecto que el PRD no debe re-litigar ni contradecir sin señalarlo explícitamente.
3. Leé el shaping (`artefactos/{{nombre_corto_proyecto}}-start.md`) — o, en legacy, el problem statement (`-problem.md`) o una hipótesis si existen. El PRD recapitula el problema, el foco y la alternativa elegida (con sus descartes); no los redefine.
4. **Leé `artefactos/{{nombre_corto_proyecto}}-solution.md` completo si existe** — es el insumo del resumen del Paso 3 y de la Alineación de la solución del Paso 7: el PRD destila ese análisis, no lo reinventa. Si no existe todavía, avisá al PM antes de escribir esos pasos a ciegas (ver "Cuándo NO usarla").
5. Contexto de producto y estratégico: `wiki/2_areas/overview_productos/overview_<producto>.md`, `wiki/3_recursos/detalle_productos/<producto>/`, `wiki/2_areas/direccion/north_star.md`.
6. Contexto de arquitectura si la iniciativa toca proveedores externos: `wiki/3_recursos/arquitectura_sistema/`.
7. Contexto de áreas internas para el Paso 8: `wiki/2_areas/overview_empresa/overview_equipo.md` (quién lidera cada área, qué maneja).
8. **Si ya existe `artefactos/{{nombre_corto_proyecto}}-prd.md`** (de una corrida anterior de esta skill), leelo completo antes de escribir — esta corrida lo actualiza in place (ver regla dura #8 y Paso 10), no genera un documento nuevo en paralelo.

### Paso 1 — Problema

Recapitulación breve del problema que se resuelve u oportunidad que se aprovecha, en prosa propia — si existe un problem statement, no lo linkees, resumí acá lo que el lector necesita saber. El lector tiene que entender el *por qué* antes de llegar al *qué*.

### Paso 2 — Contexto

Por qué atacar esto ahora: de dónde surgió el tema, si es urgente, si es parte de un proyecto más grande estratégicamente. Conectá con el foco/OKR vigente si aplica (`wiki/2_areas/direccion/north_star.md`, `wiki/2_areas/direccion/estrategia/`).

### Paso 3 — Resumen de la solución planteada

Qué se construye y cómo funciona, de cara al negocio. Nombrala por lo que efectivamente se construye (regla dura #7) — si el lector no puede deducir de esta sección qué es lo nuevo que va a existir, es señal de que quedó demasiado abstracta.

No alcanza con describir qué es: explicá también **cómo se resuelve el problema** — quiénes participan, en qué orden ocurren las cosas, y qué pasa cuando algo falla (a nivel de consecuencia de negocio, no de manejo técnico del error). Si existe `{{nombre_corto_proyecto}}-solution.md`, destilalo desde ahí sin mencionarlo ni linkearlo (regla dura #8) y sin bajar al detalle que le corresponde a ese documento: nada de contrato de endpoints, tablas de reintentos/backoff, ni mapa de procedencia campo por campo — eso es lo que hace que el lector entienda el enfoque, no que pueda construirlo. Si el lector, después de leer esta sección, no puede explicar con sus palabras cómo se resuelve el problema, quedó incompleta aunque nombre bien la solución.

### Paso 4 — Objetivos

Qué se espera lograr con este proyecto — objetivos y beneficios de negocio y/o operativos, pensados en formato SMART y medibles a futuro para poder validar si la idea implementada funcionó o no.

### Paso 5 — Caso de negocio

Justificación del beneficio monetizado esperado (o link a un archivo de business case si existe), considerando también el costo de construir la solución.

### Paso 6 — Definiciones, suposiciones y límites

Decisiones, limitantes, restricciones, riesgos o situaciones que condicionaron y llevaron a preferir este camino para resolver el problema — incluye restricciones técnicas, regulatorias (BCRA/UIF/PCI DSS) y dependencias de proveedores (Fintexa u otros) cuando corresponda. Si existe `{{nombre_corto_proyecto}}-solution.md`, las decisiones de diseño de su sección 11 son una fuente directa acá — resumidas en prosa, no linkeadas. Sumá también acá cualquier concepto o taxonomía que el lector necesite tener claro para el resto del documento (tipos de cliente, modalidades de integración, estados de una operación) — definilo una vez, no lo repartas.

### Paso 7 — Alineación de la solución

Dibuja el perímetro de la solución: qué la compone, cómo se experimenta, y qué reglas la gobiernan. Tres subsecciones, en este orden:

**Funcionalidades clave.** Todas las funcionalidades del proyecto, priorizadas con **MoSCoW** (Must/Should/Could/Won't have) como etiqueta de cada item, no como header de sección — el documento ya no se organiza por nivel de prioridad, se organiza por dentro/fuera de alcance. **Traducí el roadmap de trabajo ya definido para el proyecto, no inventes una priorización nueva**: cada IDEA/fase/funcionalidad ya tiene un lugar en el roadmap real (`proyecto.md`), este paso solo la vuelca al framework de priorización del PRD. El corte entre 🔴 Must y el resto define el MVP. Desafiá el tamaño del alcance: si un componente puede salir solo, antes que el resto, decilo. Lo que no entra (⚫ Won't have) incluye la razón del diferimiento si ayuda a entenderlo. Si hay algo que se guarda para más adelante y condiciona cómo se construye hoy, sumalo como consideración futura.

**Flujos clave.** La experiencia end-to-end para el cliente: prosa, diagrama de flujo, capturas o exploraciones de diseño — el formato varía según lo que este proyecto necesite mostrar, no reuses la estructura de un PRD anterior por costumbre. No se arma en aislamiento: se valida con diseño e ingeniería si ya intervinieron.

**Lógica clave.** Reglas que guían el diseño y el desarrollo: escenarios comunes y casos borde, en prosa o lista — no es el contrato de endpoints ni el manejo técnico del error, es la regla de negocio que decide qué pasa en cada caso (ej. qué ocurre si el cliente no confirma a tiempo, qué pasa si dos condiciones se dan a la vez).

### Paso 8 — Checklist operativo por área

Para las 7 áreas de Bind PSP (Comercial, Soporte e Integraciones, Recaudaciones/Conciliación, Fraude, Legales, IT, Clientes externos ya en producción) — **recorré las 7 siempre, sin saltear ninguna**: el valor de esta sección es dejar constancia de que se evaluaron todas, no solo las que importan.

**Armá una fila por cada pregunta del catálogo de preguntas de referencia de cada área (ver más abajo) — todas, siempre, sin podar (regla dura #11).** Amplialo si el proyecto toca algo específico que el catálogo no cubre; nunca lo recortes a "las que importan" a tu criterio. Si una pregunta genuinamente no aplica a este proyecto, la fila se arma igual con "No aplica" y el motivo en una oración — nunca se la salta en silencio. Por cada fila:

1. **Respuesta** — nunca Sí/No pelado: siempre con la explicación de por qué, en una oración que alguien de esa área reconozca como su propio problema (ej. "Sí, porque se agrega un estado nuevo de la operación que el cliente tiene que contemplar en su conciliación diaria"). Un No también se explica, y un **No aplica** también — es la respuesta cuando la pregunta del catálogo, tal como está planteada, no tiene sentido para este proyecto puntual (ej. "¿cambia el pricing?" en un proyecto que es pura corrección de datos internos), distinta de un No (la pregunta sí aplica, y la respuesta es que no ocurre). **No inventes la explicación**: si no tenés información para evaluar una pregunta, preguntale al usuario — la fila queda `Pendiente` con la pregunta abierta, no completes por default.
2. **Qué proponemos** — si la respuesta fue Sí, una de tres salidas, siempre explícita (si fue No, va "—"):
   - **Funcionalidad en el alcance** — y cuál, nombrada como aparece en Funcionalidades clave.
   - **Tarea previa al go-live** — algo a hacer antes de salir a producción que no es desarrollo (capacitar a un área, actualizar documentación pública, comunicar a clientes integrados, cargar una configuración, validar un cálculo con el área). Muchas filas caen acá: el área tiene impacto real y no hay nada que construir, hay algo que hacer. Estas filas **no se registran como tarea de Producto** — quedan documentadas acá y las levanta el proceso de preparación del lanzamiento cuando llegue el momento.
   - **Contingencia operativa** — se convive con el impacto; decir cómo y quién lo absorbe.
3. **Estado** — `Pendiente` | `Contemplado pero no validado` | `Contemplado y validado`. "Validado" significa que el área lo confirmó, no que se asumió por cuenta propia.

**Catálogo de preguntas de referencia por área** (adaptar al proyecto, no completar mecánicamente):

- **Comercial** — ¿Cambia el pricing, el packaging o lo que se le puede prometer a un cliente? ¿Hace falta material de preventa o actualizar el perfil del cliente? ¿Hay clientes en pipeline cuya integración cambia por esto?
- **Soporte e Integraciones** — ¿Cambia lo que Soporte tiene que responder o diagnosticar, y hace falta actualizar guías o capacitar? ¿Aparecen errores o estados nuevos que Soporte va a ver en un reclamo y hoy no sabe interpretar? ¿Requiere credenciales, configuración o habilitación nueva por cliente/ambiente? ¿Soporte puede darse cuenta —de forma agregada, no solo cuando llega un reclamo puntual— de que este producto no está funcionando con normalidad, para poder escalarlo a tiempo? (No alcanza con que pueda resolver sin escalar: el mínimo exigible es poder ver que algo anda mal, aunque la resolución dependa de otro equipo.)
- **Recaudaciones/Conciliación** — ¿Genera movimientos de dinero, comprobantes o tipos de operación nuevos? ¿La herramienta de conciliación puede identificarlos y cuadrarlos desde el día 1 del go-live, o hace falta parametrizarla antes? ¿Impacta la liquidación a comercios, o el cálculo e imputación de impuestos? ¿Cambia la facturación o el costo que se le cobra al cliente?
- **Fraude** — ¿Abre un vector de riesgo nuevo o cambia el perfil transaccional que se monitorea? ¿Hacen falta reglas, parámetros o límites nuevos en el motor antifraude? ¿Esta funcionalidad necesita un esquema de monitoreo operativo nuevo (tablero, alerta de anomalía de negocio) que hoy no existe? ¿Cambia la información disponible para responder un reclamo de fraude de otra entidad?
- **Legales** — ¿Requiere cambio contractual, anexo o consentimiento nuevo del cliente o del usuario final? ¿Tiene implicancias regulatorias (BCRA, UIF/PLD, PCI DSS, protección de datos)?
- **IT** — ¿Qué volumen adicional se espera y el sistema está dimensionado (picos, batch, storage)? ¿Requiere accesos, secretos o cambios en la superficie expuesta — seguridad informática? ¿Toca el modelo de datos, requiere migración o retención nueva? ¿Hay tracking/logging nuevo para poder medir los objetivos del Paso 4? ¿Se puede testear en staging con datos representativos? ¿Depende de un desarrollo de un proveedor externo y con qué lead time?
- **Clientes externos en producción** — ¿Es un breaking change para alguien ya integrado, y requiere que el cliente haga algo? ¿Hace falta preaviso, plan de comunicación y ventana de migración? ¿Hay que actualizar la documentación pública?

### Paso 9 — Riesgos

Identificá y clasificá los riesgos del proyecto: probabilidad, impacto y mitigación para cada uno. Incluí acá los gaps de capacidad detectados en el Paso 8 que todavía no tengan resolución (una contingencia operativa sin dueño claro, una pregunta que quedó `Pendiente`), y los gaps técnicos bloqueantes de la sección 12 de `{{nombre_corto_proyecto}}-solution.md` si existe.

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md) — es el estándar de PRD de la casa. Un PRD completo llena, en este orden: Problema; Contexto; Resumen de la solución planteada; Objetivos; Caso de negocio; Definiciones, suposiciones y límites; Alineación de la solución (Funcionalidades clave, Flujos clave, Lógica clave); Checklist operativo por área; Riesgos.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (cifras ilustrativas).

## ✅ Checklist de calidad

- [ ] El problema y el "por qué ahora" están claramente articulados
- [ ] La solución está nombrada por lo que efectivamente se construye, no por una abstracción ambigua
- [ ] El resumen de la solución explica el mecanismo — quiénes participan, en qué orden, y qué pasa cuando algo falla — sin caer en contrato de endpoints ni en el detalle que le corresponde al análisis de solución
- [ ] Los objetivos son SMART y medibles a futuro
- [ ] El caso de negocio contempla tanto el beneficio esperado como el costo de construir
- [ ] Funcionalidades clave marca el perímetro explícito (dentro/fuera/futuro) y cada item tiene su etiqueta MoSCoW
- [ ] Lógica clave cubre los casos borde reales del proyecto, sin bajar a contrato de endpoints
- [ ] El checklist operativo recorrió las 7 áreas, sin saltear ninguna
- [ ] Cada área tiene una fila por cada pregunta de su catálogo de referencia — ninguna se podó en silencio; las que no aplican dicen "No aplica" con el motivo, nunca faltan sin explicación
- [ ] Ninguna fila del checklist tiene un Sí/No/No aplica sin explicación, ni una explicación fabricada donde el dato no se conocía
- [ ] Cada Sí del checklist tiene una propuesta clasificada (funcionalidad en el alcance / tarea previa al go-live / contingencia operativa)
- [ ] Los riesgos tienen probabilidad, impacto y mitigación
- [ ] El documento es autocontenido: sin links a wiki, sin nombres de archivo/skill, sin códigos de ticket, sin jerga de proceso interno
- [ ] El documento se lee en menos de 15 minutos

## Paso 10 — Cierre estándar

1. **Persistir el entregable** en `artefactos/{{nombre_corto_proyecto}}-prd.md` — `{{nombre_corto_proyecto}}` es el nombre corto del proyecto: la carpeta misma si nació de `/idea_start` (sin prefijo `prd-XXX`), o el `<slug>` después de `prd-XXX_` en carpetas legacy (sin fecha en el nombre del archivo — versión en el frontmatter + historial de revisiones al pie, ver regla general de artefactos) dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde la sección de entrega de `proyecto.md`. **Si el archivo ya existe** (corrida anterior de esta skill sobre el mismo tema), esta corrida lo actualiza: reescribí limpio el cuerpo con el estado vigente — nunca dejes texto "actualizado"/"superado" incrustado en el medio — y sumá una entrada al historial de revisiones al pie con qué cambió. No crear un archivo nuevo en paralelo.
2. **Decisiones de alcance confirmadas** → `decisiones.md` del proyecto (directo). Si es una decisión de contexto fijo (no específica de esta IDEA), capturala como item `tipo: decision` en `contexto_vivo/` en vez de escribir directo.
3. **Preguntas abiertas** → `gaps.md` de la IDEA/proyecto; `../../../wiki/2_areas/gaps_y_preguntas.md` solo si son de contexto fijo, no del proyecto.
4. **Índices:** tabla maestra de `wiki/1_proyectos/index.md` §2; `wiki/index.md` solo si cambió una sección de nivel PARA.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
6. **Jira:** nunca crear ni editar tickets a partir de este PRD sin confirmación explícita del usuario.
7. Siguiente paso sugerido: [`/idea_estimate`](../idea_estimate/SKILL.md) en Modo Proyecto para dimensionar la IDEA completa apenas el PRD está cerrado (sin esperar a las historias) si hace falta priorizarla contra otras IDEAs o conversar capacidad con Ingeniería; [`/idea_us`](../idea_us/SKILL.md) para bajar el PRD a historias de sprint; o [`/idea_golive`](../idea_golive/SKILL.md) más adelante para convertir las filas de "tarea previa al go-live" del checklist operativo en un plan de lanzamiento con responsables y fechas.
