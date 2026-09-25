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

- La feature todavía no está especificada → usá primero [`/idea_prd`](../idea_prd/SKILL.md); las historias tienen que trazar a requisitos ya documentados.

No existe una skill separada para profundizar Given/When/Then de una historia puntual (`/idea_ac` se deprecó el 2026-09-09) — esa profundidad es responsabilidad directa del Paso 5 de esta misma skill, apoyada en el catálogo de fallas de `{{nombre_corto_proyecto}}-solution.md` (Sección 8, si existe `/idea_solution` previo) en vez de reinventar los casos de error por historia.

## Por qué esta skill es experta en APIs

Buena parte del negocio de Bind PSP pasa por construir, exponer o consumir APIs (Adquirencia, Wallet, Agente de Cobros y Pagos, Ardid, Siscri, integraciones con Fintexa/Payway/BCRA). Una historia que describe un endpoint mal especificado genera ida y vuelta con Ingeniería y QA, o peor, un desarrollador "elige" el comportamiento no especificado (naming, código de error, estrategia de borrado) y ese criterio ad hoc se vuelve contrato de facto. Por eso, cuando la historia toca un endpoint, esta skill actúa como diseñadora de contrato de API, no solo como redactora de AC — ver el detalle obligatorio del Paso 5.

## Por qué las reglas de negocio transversales importan tanto como el contrato de API

El gate de CI/CD que Infraestructura/Seguridad está mandatorizando (SAST + cobertura mínima + code review formal, ver `2_areas/procesos` una vez mergeado) detecta código riesgoso o mal escrito — no una condición de negocio mal planteada. El incidente de fraude de Transferencias Pull de marzo 2026 lo muestra literal: la causa raíz fue un `if` condicionado sobre la variable equivocada, un error de lógica de negocio que ningún linter ni analizador estático iba a atrapar — solo un AC explícito sobre ese caso borde lo hace. Ese gate cubre la mitad del problema; la otra mitad — que la lógica de negocio esté bien probada, incluidos los caminos de error — sigue siendo terreno exclusivo de Producto al redactar AC. Por eso esta skill no solo pide AC testeables por historia (INVEST), sino que exige mirar el conjunto del proyecto: una regla de negocio que aplica a más de una historia (un límite, una validación de estado, un cálculo compartido) se pierde fácil si cada historia se redacta y revisa de forma aislada, sin nadie mirando el proyecto completo. Ver el inventario del Paso 0 y la revisión cruzada del Paso 5ter.

## ⚖️ Reglas duras

1. **Formato fijo:** "Como [persona], quiero [acción] para [beneficio]." La cláusula de beneficio no es opcional — explica por qué importa y ayuda a priorizar.
2. **Nunca "usuarios" a secas.** Cada historia es para una persona o rol específico — para historias de API, la persona puede ser un rol técnico ("Sistema externo integrador", "Backend de Wallet", "Desarrollador integrador") si no hay un usuario final directo.
3. **Sin detalles de implementación** en el enunciado de la historia — eso es del "cómo", no del "qué". El contrato de API (Paso 5) no es "detalle de implementación": es la interfaz que el consumidor ve, así que sí va explícito y completo.
4. **Aplicá INVEST:** cada historia tiene que ser Independiente, Negociable, Valiosa, Estimable, Chica, Testeable. "Chica" significa acotada a un entregable técnico completo (o a un entregable parcial de ese componente si no entra en un sprint, ver Paso 3) — nunca partir una historia en varias solo porque cubre más de un camino o escenario de uso; eso son AC de una misma historia, no historias distintas. Si una historia no cumple, revisala antes de darla por terminada.
5. **El documento es siempre autocontenido.** Es la previa a un entregable que ingeniería, QA o un tercero van a leer sin acceso a este sistema — nunca links a la wiki, nombres de archivo o de skill, códigos de ticket usados como si el lector los reconociera, ni jerga de proceso interno ("según el gap...", "ver decisiones.md"). "Contexto y antecedentes" recapitula en prosa lo que el PRD u otro artefacto ya estableció, no lo linkea.
6. **No dejar puertas abiertas al desarrollador en una historia de API.** Ante cada decisión de contrato (naming, paginación, estrategia de borrado, código de error, versionado) elegí una opción concreta y documentala — nunca "a definir por el equipo técnico" salvo que sea una Pregunta abierta explícita y consciente.
7. **Una regla de negocio transversal al proyecto se prueba en cada historia que la toca, no solo en la primera donde aparece.** Nunca asumas que "ya se probó en otra historia" alcanza — cada componente técnico que ejecuta esa regla (un endpoint, una pantalla, un job) necesita su propio AC, aunque la lógica de negocio detrás sea idéntica. Ver el inventario del Paso 0 y la revisión cruzada del Paso 5ter.
8. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto de la feature

1. Resolvé la ruta real de la IDEA en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2.
1bis. **Gate de entrada:** el frontmatter del PRD (`artefactos/{{nombre_corto_proyecto}}-prd.md`) tiene que decir `Aprobado por PM`. Si dice `Propuesta`, pará y ofrecé revisarlo y aprobarlo ahora o volver a `/idea_prd`. En un PRD legacy sin campo `estado`, preguntale al PM una sola vez si lo da por aprobado y registralo en su historial. Si ya existe un `-us.md` aprobado cuyo `basado_en` apunta a una versión anterior del PRD, decile al PM qué cambió y qué historias pueden verse afectadas.
2. **Leé todo lo que ya existe antes de escribir una sola historia** — no alcanza con el PRD solo:
   - El PRD formal completo en `artefactos/` (todas las secciones: Problema, Solución, Definiciones, Alineación de la solución — Funcionalidades/Flujos/Lógica clave —, Impactos por área, Riesgos). Si una fila de Impactos por área es una "funcionalidad en el alcance", tiene que terminar cubierta por alguna historia.
   - **`artefactos/{{nombre_corto_proyecto}}-solution.md`, si existe** — es la fuente principal del contrato de API y de los flujos del Paso 5: el orden de llamadas, los endpoints reales, la procedencia de cada dato y los errores conocidos ya están ahí, no se reinventan por historia. Cualquier documento de acceptance criteria ya redactado (`/idea_ac` previo) es la otra fuente a revisar.
   - El `proyecto.md` del miembro completo (no solo el resumen ejecutivo) — Definiciones, Diseño técnico, Seguimiento PM, Historial de sync suelen tener detalle que el PRD todavía no absorbió.
   - Si es miembro de un proyecto general, el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre — las historias no deberían re-litigar una decisión de arquitectura ya cerrada a nivel proyecto.
   - Cualquier otro artefacto de la carpeta (`artefactos/`) que el PM haya referenciado en la sesión — diagramas, docs de validaciones de un proveedor externo, historial de bugs de un endpoint existente, etc. Estos suelen ser la fuente real del detalle fino que hace falta en el Paso 5.
3. Si no hay PRD asociado, confirmá con el usuario cuál es el alcance antes de escribir historias.
4. **Si ya existe `artefactos/{{nombre_corto_proyecto}}-us.md`** de una corrida anterior, leelo completo — esta corrida lo actualiza in place (ver Paso 8), no genera un documento nuevo en paralelo.
5. **Armá el inventario de reglas de negocio transversales del proyecto** — condiciones de validación, cálculo o aprobación/rechazo que aplican a más de un endpoint, pantalla o historia (ej. un límite de monto, una regla de estado, una fórmula compartida, una condición de habilitación) — a partir del PRD, `solution.md` y `proyecto.md` (incluido el §4 del padre si es miembro de un proyecto general). No hace falta un documento aparte: alcanza con tenerlo explícito antes de escribir AC, porque es lo que se contrasta historia por historia en el Paso 5 y en conjunto en el Paso 5ter — el riesgo real es redactar cada historia de forma aislada y perder de vista que una regla compartida terminó sin ningún AC que la cubra, o cubierta de forma inconsistente entre historias distintas.

### Paso 1 — Entender el contexto de la feature

Revisá el PRD o la descripción de la feature. Entendé el objetivo general, los usuarios objetivo y los límites de alcance.

### Paso 2 — Identificar personas de usuario

Determiná qué usuarios interactúan con esta feature. Cada historia se escribe para una persona específica, no para "usuarios" genéricos — features distintas pueden necesitar historias distintas para la misma feature.

### Paso 3 — Descomponer por entregable técnico completo

El eje de corte es el **componente técnico completo** que hay que construir — un endpoint entero (con todos sus casos y validaciones), una pantalla entera (con todos sus estados), un job o una integración completa — no el objetivo o camino de usuario. Una sola historia puede resolver más de una funcionalidad del PRD si todas dependen del mismo componente: no fragmentes en una historia por camino feliz y otra por camino alternativo si ambos son parte del mismo endpoint o pantalla — eso va todo en los AC de una misma historia (ver Paso 5). El enunciado (Paso 4) sigue describiendo lo que el usuario logra, no el componente en sí — pero el alcance real de "terminado" en esa historia es el entregable técnico completo que lo resuelve, así el requerimiento que le llega a Ingeniería queda lo más compactado posible.

Partí una historia en más de una únicamente cuando el componente en sí es demasiado grande para completarse en un sprint. Ahí el corte sigue siendo por **entregable parcial pero igual de completo en su propio recorte** — ej. "endpoint de alta y consulta" separado de "endpoint de baja" del mismo recurso, nunca "endpoint — caso feliz" separado de "endpoint — casos de error" del mismo endpoint. Si existe `{{nombre_corto_proyecto}}-solution.md`, usalo para identificar qué componentes técnicos hacen falta (qué endpoints, qué pantallas), no para cortar una historia por cada camino que documenta — los caminos alternativos son AC dentro de la historia del componente, no historias aparte.

**Precisión (2026-08-26): el eje de corte no es el servicio/componente técnico en sí, sino el equipo de ingeniería que lo construye frente a un consumidor.** Si un mismo equipo resuelve una capacidad a través de más de un servicio/componente interno propio (ej. un servicio público + un servicio de orquestación interno), es **una sola historia** — el salto interno entre sus propios servicios se documenta en Contexto/Notas técnicas, no como historia aparte. El corte a una historia nueva ocurre únicamente cuando la interfaz cruza a un equipo de ingeniería distinto — ahí nacen **historias espejadas**, una por cada lado que la construye (ej. "Endpoint del Equipo A para que [consumidor] haga X" y "Endpoint del Equipo B para que el Equipo A haga Y"), de forma que cada equipo pueda estimar/construir/testear su lado contra el contrato ya acordado. Reglas complementarias: (a) un mismo verbo/acción con distinto consumidor sigue siendo una frontera distinta, aunque ambos lean la misma tabla — el consumidor cambia, el criterio de aceptación y el timing también pueden cambiar; (b) dentro del mismo equipo y el mismo consumidor, un verbo/interacción distinto (crear vs. consultar vs. actualizar) sigue mereciendo su propia historia cuando es una capacidad independiente y estimable por separado — el criterio de "bocado grande" es sobre no fragmentar por componente interno, no sobre colapsar verbos HTTP distintos; (c) una continuación/reintento sobre la misma capacidad, resuelta por el mismo motor/endpoint ya construido, no es una historia aparte — va como AC de la misma historia; (d) cada historia nombra explícitamente la interfaz que construye y qué NO incluye del otro lado de la frontera, para que no haya ambigüedad de dueño; (e) una diferencia de prioridad real entre dos variantes del mismo verbo (ej. una consulta liviana de uso frecuente vs. una consulta completa de uso puntual, ya señalada como "no prioritaria" en una decisión previa) también amerita separarlas en historias distintas, aunque compartan equipo, consumidor y verbo HTTP — son capacidades planificables por separado, estimables y lanzables en sprints distintos sin bloquearse entre sí. Si la variante de menor prioridad cruza a otro equipo, la contraparte de ese equipo hereda la misma prioridad menor — es la misma capacidad de cara a los dos lados de la frontera, no tiene sentido que un lado sea P0 y el otro P1 para la misma funcionalidad. Esto no reduce la profundidad de los criterios de aceptación — el checklist obligatorio (Paso 5) sigue aplicando completo a cada historia, incluidas las de contrato interno entre equipos.

### Paso 4 — Escribir los enunciados

Formato: "Como [persona], quiero [acción] para [beneficio]."

### Paso 5 — Definir criterios de aceptación

Criterios específicos y testeables en formato Given/When/Then. Los criterios de aceptación definen "terminado" — si todos pasan, la historia está completa. Empezá siempre por el camino feliz y sumá después casos borde, estados de error (con su comportamiento de recuperación visible) y criterios no funcionales cuando corresponda — la profundidad de esta sección es responsabilidad de este mismo paso, no de una skill separada.

**Historias que describen un endpoint o contrato de API — nivel de detalle obligatorio.** Cómo se documenta el contrato depende de si esta historia lo define o lo cambia:

- **La historia crea un endpoint nuevo, o modifica el contrato de uno existente** (campo nuevo, código nuevo, cualquier cambio visible en el request/response) — documentá el contrato completo en su propia sección "Contrato de API" (ver template): estilo, método y recurso, autenticación, headers obligatorios, versionado, paginación/filtrado, estrategia de borrado, y los ejemplos de request/response de éxito y de error. Es el caso clásico — un endpoint que antes no existía en esa forma, ahora sí.
- **La historia reutiliza uno o más endpoints ya existentes sin cambiarles el contrato** (el caso típico de un fix interno, una mejora de resiliencia, o cualquier historia donde lo que cambia es el comportamiento del backend, nunca la interfaz pública) — no repitas una sección de contrato aparte. Documentá igual el detalle relevante (qué endpoint, qué caso, qué código y cuerpo exacto) directamente dentro de los criterios de aceptación, arrancando con un resumen breve de qué endpoint(s) están en juego si hay más de uno o más de un desenlace por caso (ej. una tabla de "qué percibe quien integra" antes del primer AC).

**En los dos casos, sin excepción:** los criterios de aceptación siempre llevan ejemplos concretos de request/response como bloque de código JSON en los AC relevantes — nunca alcanza con una descripción en prosa tipo "responde con éxito" o "devuelve un error" sin mostrar el cuerpo real esperado. Es lo que le permite a QA e Ingeniería verificar sin ambigüedad, exista o no una sección de contrato separada arriba.

Cubrí explícitamente los siguientes bloques — vayan en la sección de Contrato de API o repartidos en los AC según el caso de arriba — no todos aplican a toda historia, pero la ausencia de uno debe ser una decisión consciente, no un olvido:

**a) Contrato de interfaz**
- **Estilo:** REST, GraphQL, gRPC, Webhook o WebSocket — explícito, no asumido.
- **Método/verbo y URL del recurso:** `GET`/`POST`/`PUT`/`PATCH`/`DELETE` con la semántica correcta (`POST` crea, `PUT`/`PATCH` actualiza, `DELETE` elimina, `GET` es idempotente y de solo lectura). Recursos REST en sustantivo plural (`/comitentes`, `/cuentas`), nunca verbos en la URL.
- **Naming consistente:** una sola convención por API (`camelCase` o `snake_case`, no mezclar) y campos escalares con unidad explícita en el nombre cuando haya ambigüedad posible (`montoCentavos`, `duracionSegundos`) — nunca un `monto` o `duration` sin unidad.
- **IDs no predecibles** cuando el recurso es sensible (UUID o ID con prefijo tipo `cta_...`, `sol_...`) para no habilitar scraping por incremento secuencial — si el sistema ya usa IDs secuenciales por diseño heredado, dejalo como Nota técnica en vez de inventar un cambio de esquema no pedido.
- **Headers obligatorios:** autenticación, `Content-Type`, cabecera de correlación (`X-Request-ID` o `traceId`) y cualquier header específico del dominio (ej. `Idempotency-Key` — ver bloque de errores/resiliencia).
- **Paginación/filtrado/ordenamiento** si el endpoint lista recursos: cursor-based para feeds/datos que cambian, offset-based para conjuntos estables; filtros por campo explícito (nunca un query param libre tipo "search" que termine armando SQL dinámico).
- **Estrategia de borrado** si el endpoint elimina: soft-delete (qué código devuelve, cómo se distingue un recurso ya borrado en un segundo intento, si hay parámetro `includeDeleted` para listarlos) o hard-delete (`204 No Content`, `404` en llamadas subsiguientes) — elegir una y ser explícito, no dejarlo implícito en el AC de "elimina el recurso".

**b) Validaciones y ejemplos de payload**
- **Validaciones de cada dato del request** — formato, obligatoriedad, valores permitidos/catálogos cerrados, longitudes, caracteres especiales — no un AC genérico de "valida los datos", uno por cada campo o grupo de campos que lo amerite.
- **Ejemplos concretos de request y response en los criterios mismos** (no solo en Notas técnicas), como bloque de código JSON literal — sirven para definir la UX de quien integra la API, no solo para que el desarrollador sepa qué construir. Si el payload real tiene muchos campos, alcanza con un ejemplo representativo por caso (éxito, error de validación, error de negocio) en vez de repetir el objeto completo en cada AC.
- **Validación de existencia y consistencia de recursos referenciados** — si el request trae un ID (`idCuenta`, `idSolicitud`, etc.), un AC cubre qué pasa si no existe, y otro si existe pero en un estado inconsistente para la operación.

**c) Seguridad y autorización** (las fallas de autorización son la causa más común de incidentes de API — OWASP API Top 10)
- **Mecanismo de autenticación** explícito: OAuth 2.0/OIDC, JWT Bearer, API Key o mTLS.
- **Anti-BOLA (Broken Object Level Authorization):** un AC valida explícitamente que un usuario/cliente autenticado no pueda leer ni modificar un recurso de otro usuario cambiando el ID en la ruta o el body — esperado `403 Forbidden`. Obligatorio en todo endpoint que reciba un ID de recurso perteneciente a un titular.
- **Anti-BOPLA (Broken Object Property Level Authorization):** un AC define qué campos del objeto son de solo lectura o no expuestos según el rol de quien llama (evita mass assignment — ej. que el request pueda setear `estado: aprobado` cuando ese campo lo controla el sistema, o que la response exponga campos internos/sensibles que el rol no debería ver).
- **Sanitización de inputs** — cada campo de texto libre tiene su regla de validación (evita inyección SQL/XSS/command injection); nunca confiar en validación solo del lado cliente.

**d) Errores y resiliencia**
- **Códigos de respuesta HTTP explícitos** para cada desenlace: `400` (sintaxis/JSON inválido), `401` (sin credenciales o inválidas), `403` (autenticado sin permiso — BOLA/BOPLA), `404` (recurso inexistente), `409` (conflicto de estado), `422` (falla de regla de negocio/validación), `429` (rate limit, con header `Retry-After`), `500`/`502`/`503`/`504` (error de servidor/gateway) — no dejarlo implícito ni usar un genérico "maneja errores".
- **Formato de error estándar:** `application/problem+json` (RFC 9457) con `type`, `title`, `status`, `detail`, `instance` y, si hay múltiples validaciones fallidas, un arreglo `errors` por campo. Un AC muestra el JSON de ejemplo de al menos un error de validación y uno de negocio.
- **Mensajes de error seguros** — nunca exponer stack trace, nombre de tabla/query ni ruta interna; mensajes neutros en fallas de autenticación ("credenciales inválidas", nunca "el usuario no existe").
- **Caminos no felices** — cada error de negocio o de validación conocido (rechazos del sistema externo, catálogos cerrados que no matchean, recursos incompletos) necesita su propio AC.
- **Idempotencia:** si el endpoint crea un recurso o mueve dinero (`POST` de alta, pago, transferencia), un AC exige soporte de header `Idempotency-Key` — mismo key + mismo body en un reintento devuelve el resultado original sin duplicar el efecto.
- Si la historia consume un sistema externo (broker, proveedor), revisar si hay documentación de validaciones o historial de bugs ya ingerido en la wiki (`3_recursos/detalle_productos/`) antes de inventar el detalle — es la fuente más confiable de qué falla en la práctica.

**e) Versionado y compatibilidad** (solo si la historia modifica un endpoint existente o reemplaza capacidad previa)
- Estrategia de versión del API en juego (`/v1/` en el path, header `Accept-Version`, versión por fecha) — no inventar una nueva si el producto ya tiene una convención, confirmarla en `3_recursos/detalle_productos/<producto>/apis_expuestas/`.
- Marcar si el cambio es **aditivo** (campo opcional nuevo, no rompe clientes existentes) o **breaking** (renombra/elimina campo, cambia tipo) — un cambio breaking casi siempre implica partir en una historia de versión nueva, no parchear la existente.
- Si reemplaza un endpoint/campo previo: AC que exige headers `Deprecation` y `Sunset` con fecha de retiro comunicada.

**f) NFRs relevantes al contrato** (solo si el PRD o el PM los definió — no inventar SLAs)
- Latencia esperada (ej. `p95 < 200ms`), `Cache-Control`/ETags si la respuesta es cacheable, límite de rate limiting/cuotas por cliente si aplica.

**g) Definition of Done técnico** (va en Notas técnicas o Dependencias, no como AC funcional)
- Actualización de la especificación OpenAPI 3.1 (o AsyncAPI si es evento/webhook) del producto como fuente única de verdad — `3_recursos/detalle_productos/<producto>/apis_expuestas/`.
- Pruebas de contrato (OpenAPI/Pact) entre consumidor y proveedor si hay más de un sistema involucrado.
- Mocks/fixtures de datos de prueba sin PII real.
- Pruebas negativas/adversariales: nulos, campos faltantes, tipos erróneos, payloads fuera de rango — no solo el happy path.

**h) Reglas de negocio transversales al proyecto** (contrastar contra el inventario del Paso 0)
- Si esta historia ejecuta una regla que también aplica a otra historia del mismo proyecto, decilo explícito en el AC (ej. "aplica el mismo límite de monto que la historia de alta — ver Contexto y antecedentes") y sumá el AC del caso borde igual, aunque ya esté probado en la otra historia — nunca asumir que alcanza con probarlo una vez.
- No confiar en que el gate automático de calidad (SAST/cobertura) va a atrapar una condición de negocio mal escrita — eso solo lo atrapa un AC explícito sobre el caso borde específico, nunca un "valida correctamente" genérico.

### Paso 5bis — Diagrama de flujo (cuando aplique)

Si el flujo de la historia tiene ramas condicionales, más de un sistema/actor involucrado, reintentos, o estados intermedios que un texto lineal no deja claros a simple vista, agregá un diagrama en Mermaid (`flowchart` para decisiones, `sequenceDiagram` para intercambios entre sistemas) en una sección "Diagrama de flujo" propia dentro de la historia. No es obligatorio para historias simples de un solo paso — es una herramienta para cuando el texto solo no alcanza para que Ingeniería visualice el camino completo sin ambigüedad, especialmente en integraciones con sistemas externos (Fintexa, Payway, BCRA) donde el orden de llamadas y los puntos de fallo importan.

### Paso 5ter — Revisión iterativa con el PM

**No se da por cerrado el documento en la primera pasada.** Antes de considerar el entregable terminado:

1. **Revisión cruzada de reglas de negocio (antes de la primera presentación):** releé el documento completo, todas las historias juntas y no una por una, contra el inventario del Paso 0. Marcá y corregí cualquier regla transversal que quedó sin AC en alguna historia que la toca, o cubierta de forma contradictoria entre historias distintas (ej. dos límites distintos para la misma condición). Este paso es el que compensa el punto ciego de redactar historia por historia — hacelo siempre, no solo cuando sospechás un problema.
2. Presentá el documento completo al PM para revisión — es el estado por defecto, no un paso opcional.
3. Si el PM corrige una historia (dirección de un flujo, alcance, redacción, un AC mal planteado), reescribí esa historia completa reflejando la corrección — no parchear con notas "actualizado" superpuestas al texto viejo (ver regla general de artefactos: cuerpo limpio, historial de revisiones al pie).
4. Repetí el ciclo de revisión las veces que haga falta hasta que el PM esté de acuerdo con las redacciones — cada vuelta suma una entrada al historial de revisiones del documento, no un documento nuevo.
5. Recién con el OK explícito y literal del PM el frontmatter pasa de `estado: Propuesta` a `Aprobado por PM (YYYY-MM-DD)` — ni el silencio ni "dale, seguí" cuentan — y el historial registra qué versión se aprobó. Si una corrida posterior cambia el cuerpo, vuelve a `Propuesta` con versión nueva hasta la re-aprobación (la estimación que escribe `/idea_estimate` no revoca la aprobación). Con el OK se pasa al Paso 8 (persistencia) y, si el PM lo pide aparte, a la creación de tickets en Jira (ver regla dura de Jira más abajo — sigue siendo un paso separado y explícito, no automático).

### Paso 6 — Aplicar criterios INVEST

Validá cada historia contra INVEST: Independiente, Negociable, Valiosa, Estimable, Chica (Small), Testeable. Revisá las que no cumplan.

### Paso 7 — Agregar contexto y notas

Sumá referencias de diseño relevantes, consideraciones técnicas y dependencias que ayuden a quien implementa a entender el panorama completo.

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md). Por cada historia: Encabezado; Enunciado; Contexto y antecedentes; Contrato de API (solo si la historia crea o modifica un endpoint — ver Paso 5; si reutiliza uno existente sin cambios, esta sección se borra y su detalle va embebido en los AC); Criterios de aceptación (siempre con ejemplos concretos de request/response en los AC relevantes); Diagrama de flujo (solo si aplica — ver Paso 5bis); Notas de diseño; Notas técnicas; Dependencias; Fuera de alcance; Preguntas abiertas. En documentos multi-historia, cada historia anida estas secciones bajo su propio título (ver ejemplo).

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo.

## ✅ Checklist de calidad

- [ ] Cada historia sigue el formato "Como... quiero... para..."
- [ ] Las historias son independientes (se pueden construir en cualquier orden)
- [ ] Los criterios de aceptación usan formato Given/When/Then
- [ ] Cada criterio es testeable (se puede verificar pass/fail)
- [ ] Las historias son lo bastante chicas para completarse en un sprint — por entregable técnico completo o parcial (Paso 3), no partidas por camino o escenario de uso
- [ ] No hay detalles de implementación en el enunciado
- [ ] La cláusula de beneficio explica por qué le importa al usuario
- [ ] Si la historia crea o modifica un endpoint: tiene sección "Contrato de API" completa (estilo, método, URL, headers, naming). Si reutiliza uno existente sin cambios, esa sección no está — el detalle equivalente vive en los AC
- [ ] En cualquiera de los dos casos, los AC cubren validaciones por dato, ejemplos concretos de request/response (bloque JSON, nunca solo en prosa), códigos de respuesta explícitos, anti-BOLA/BOPLA, formato de error RFC 9457 e idempotencia si crea/mueve dinero
- [ ] Si el flujo de la historia tiene ramas, reintentos o más de un sistema involucrado: hay diagrama Mermaid en "Diagrama de flujo" (Paso 5bis)
- [ ] Se armó el inventario de reglas de negocio transversales (Paso 0) y se hizo la revisión cruzada de todas las historias contra ese inventario antes de la primera presentación (Paso 5ter, punto 1) — ninguna regla compartida quedó sin AC o con AC contradictorio entre historias
- [ ] El PRD estaba en `Aprobado por PM` antes de empezar (Paso 0.1bis)
- [ ] Toda funcionalidad en el alcance que aparece en Impactos por área quedó cubierta por alguna historia
- [ ] El PM revisó el documento completo y dio su OK explícito a las redacciones (Paso 5ter), y el frontmatter dice `Aprobado por PM (YYYY-MM-DD)` — o quedó explícito en `Propuesta`

## Paso 8 — Cierre estándar

1. **Persistir el entregable** en `artefactos/{{nombre_corto_proyecto}}-us.md` — `{{nombre_corto_proyecto}}` es el nombre corto del proyecto: la carpeta misma si nació de `/idea_start` (sin prefijo `prd-XXX`), o el `<slug>` después de `prd-XXX_` en carpetas legacy (sin fecha en el nombre del archivo — versión en el frontmatter + historial de revisiones al pie, ver regla general de artefactos) dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde `proyecto.md` (§4 Entrega, fila de la tabla "Cadena de artefactos" con versión y estado). Frontmatter: `version`, `estado`, `basado_en: {prd: "<versión>", solution: "<versión>"}`.
2. **Índices:** `wiki/1_proyectos/index.md`; `wiki/index.md` solo si aplica.
3. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
5. **Jira:** nunca crear tickets a partir de estas historias sin confirmación explícita del usuario, aunque el Paso 5ter ya haya cerrado con el OK del PM sobre el contenido — la creación en Jira es una decisión aparte que el PM tiene que pedir explícitamente. Si el alcance cruza más de un sistema/equipo (ej. dos proyectos Jira distintos), evaluá si corresponde partir una historia en dos — una por sistema — en vez de una sola historia con dependencias cruzadas de dueño ambiguo. Cuando el PM confirme que quiere crear en Jira, la creación misma (IDEA/Epic/Historias, clasificación, estados, prioridades) es responsabilidad de [`/idea_jira`](../idea_jira/SKILL.md) — no la repliques acá a mano.
6. Siguiente paso sugerido: [`/idea_estimate`](../idea_estimate/SKILL.md) para cargar una estimación preliminar de SP por analogía histórica una vez que el PM dio su OK sobre las historias (Paso 5ter ya cerrado), [`/idea_jira`](../idea_jira/SKILL.md) para crear la jerarquía en Jira una vez que haya SP estimado, o [`/idea_golive`](../idea_golive/SKILL.md) cuando el conjunto de historias esté listo para lanzar. Si alguna historia quedó fuera de alcance de desarrollo (ej. una carga de datos puntual/backfill), no la fuerces dentro del documento de historias — anotala como ítem del checklist de lanzamiento en vez de como historia de sprint.
