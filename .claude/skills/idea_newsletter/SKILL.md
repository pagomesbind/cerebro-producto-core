---
name: idea_newsletter
description: Arma y manda el newsletter interno de producto ("Novedades de Producto") para comunicar a toda Bind PSP una idea/proyecto ya finalizado y en producción. Reutiliza la identidad de marca de Bind PSP (mismo espíritu que /pdf_build) en dos formatos — un artifact web para iterar el diseño con el PM, y una versión de mail compatible con clientes de correo reales — y solo manda el envío masivo después de una prueba a la casilla del propio PM y su confirmación explícita. Se activa con /idea_newsletter.
when_to_use: Se activa cuando el usuario ejecuta /idea_newsletter, típicamente cuando un proyecto o IDEA ya está en producción/activo y el PM quiere comunicarlo a toda la empresa (no solo a su equipo) en un formato prolijo y escaneable para audiencia mixta (C-levels, gerentes, soporte, analistas, administrativos).
disable-model-invocation: true
argument-hint: "[nombre del proyecto/IDEA ya finalizada a comunicar]"
---

# 📣 NEWSLETTER DE PRODUCTO: /idea_newsletter

## Por qué existe esta skill

Salió de armar, iterar y mandar el primer newsletter de este tipo (el de
"Mejora de tiempos en operaciones Wallet", disparado por el reclamo de
Pagos QR) con identidad real de Bind PSP en vez del HTML genérico que se
venía usando. Ese proceso — diseñar el artifact, convertirlo a una versión
que sobreviva a un cliente de correo real, y mandarlo — tiene suficientes
detalles no obvios (ver `references/design-notes.md`) como para no
rehacerlos de cero cada vez. Esta skill deja ese trabajo reutilizable para
cualquier PM del equipo (Pablo, Nicolás, Luciana) sobre cualquier idea
nueva que ya haya llegado a producción.

## Cuándo NO usarla

- El proyecto todavía no está activo en producción — esto es para
  comunicar algo ya hecho, no para anunciar un lanzamiento futuro.
- Es una comunicación para un cliente externo, no interna a Bind PSP — para
  eso, `/pdf_build` (documento) es más apropiado, no un newsletter interno.
- Es solo para tu propio equipo o un stakeholder puntual, no para "toda
  Bind PSP" — un mail directo alcanza, no hace falta este formato ni el
  paso de envío masivo.
- Estás cerrando formalmente el proyecto (merge a `detalle_productos/`,
  calibración SP en `log_iniciativas_producto.md`, rotación a
  `4_archivos/`) — eso lo hace `/debrief` en su cierre estándar. Esta
  skill no reemplaza ese proceso ni escribe nada en la wiki; el envío del
  newsletter puede pasar antes, después o en paralelo del cierre formal.

## ⚖️ Reglas duras

1. **Nunca se manda a toda la empresa sin un envío de prueba antes.** El
   flujo siempre es: artifact aprobado → versión de mail → prueba a la
   casilla del propio PM → ajustes si hace falta → recién ahí, con
   confirmación explícita, el envío real.
2. **Nunca se asume la dirección o alias de "todo Bind PSP".** Preguntale
   al PM cuál es (puede ser una lista de distribución, un alias, o una
   lista de destinatarios puntual) — adivinar una dirección de correo para
   un envío masivo es exactamente el tipo de error que no se puede
   deshacer.
3. **La versión de mail nunca es la misma pieza de HTML que el artifact.**
   Se reconstruye entera con `references/template-email-safe.html` —
   tablas, estilos inline, sin CSS grid/flexbox/variables, sin fuente de
   Google, sin SVG (emoji en su lugar). Ver `references/design-notes.md`
   para el porqué de cada restricción.
4. **Las secciones opcionales se omiten enteras si no aplican, nunca se
   rellenan por completar.** "¿Qué no se hizo?", "Más información" e
   "Importante" son opcionales — ver el detalle de cada una en el Paso 3.
5. **Ningún número se inventa.** Si una métrica de "¿Cuánto nos
   beneficia?" no tiene dato real (medido o al menos estimado con base),
   se resuelve en texto cualitativo o se le pregunta al PM — nunca se
   rellena la tabla con un valor inventado.
6. **Después de cada envío (prueba o real), se verifica con
   `get_message`** que el contenido que llegó es el newsletter real y no
   HTML roto o escapado — ver `references/design-notes.md` #12, es un
   error que ya pasó una vez.

## 🏃 Pipeline

### Paso 1 — Resolver qué idea se va a comunicar

Si el usuario pasó un nombre con `/idea_newsletter <nombre>`, resolvé la
carpeta real en `wiki/1_proyectos/index.md` (§1/§2) igual que cualquier
otra skill de esta casa. Si no pasó nada, preguntale cuál. Si el proyecto
ya se cerró y rotó a `wiki/4_archivos/proyectos_finalizados/`, buscalo ahí
— para esta skill es una consulta puntual de una fuente ya conocida, no
"ingesta de `raw/`", así que no aplica la restricción de no leer
`4_archivos/` como input de ingesta nueva.

### Paso 2 — Reunir el contenido fuente

Leé `proyecto.md` completo (resumen ejecutivo, problema y contexto,
alcance, decisiones) y `decisiones.md` si existe. De ahí sale la base de
"¿Por qué se hizo?" y "¿Qué se hizo?". Si el proyecto tiene `artefactos/`
(PRD, historias), revisalos por si tienen datos de impacto ya
cuantificados. Lo que falte, preguntáselo al PM en bloque en vez de
inventarlo — en particular:
- Fecha de publicación en producción y versión, fecha de activación (si
  son distintas — ver `design-notes.md` #8).
- Categoría del cambio (Build / mejora / fix / etc.).
- Si hay un cliente o segmento puntual detrás del pedido (tile
  "Interesados" — opcional, no inventar uno si el cambio no vino de un
  pedido puntual).
- Qué se mide (o se espera medir) para "¿Cuánto nos beneficia?", y si ya
  hay datos reales post-lanzamiento o todavía es una proyección (ver
  `design-notes.md` #9).
- Si queda algo relevante fuera de alcance todavía (¿qué no se hizo?,
  opcional).
- Si hay un caveat o limitación real que avisar (Importante, opcional —
  no crear la sección si no hay nada genuino que avisar).
- Si hay documentación (manual, guía) relevante para una audiencia
  puntual — soporte, integraciones, comercial, etc. (Más información,
  opcional, un botón por link, cada uno con su propia audiencia).

### Paso 3 — Armar el esquema y confirmarlo antes de maquetar

Mismo criterio que `/pdf_build`: no arranques a escribir HTML todavía.
Mostrale al PM qué va a decir cada sección (una frase por sección) y qué
opcionales vas a incluir/omitir, y esperá su confirmación o ajustes.

Estructura fija, en este orden:

| Sección | ¿Siempre? | Contenido |
|---|---|---|
| Header (eyebrow + título + resumen ejecutivo como subtítulo) | Sí | Título en lenguaje llano orientado al resultado, no al nombre técnico del proyecto. El resumen ejecutivo es UNA frase compacta — si el proyecto nació acotado (ej. un reclamo puntual) pero la solución quedó general, decilo ahí. |
| Rótulo (Producto, Categoría, Publicado en producción desde + versión, Activo en producción desde, Interesados) | Sí (Interesados opcional) | Ver `design-notes.md` #8 sobre separar publicado de activo. |
| ¿Por qué se hizo? | Sí | El problema/reclamo que lo disparó. |
| ¿Qué se hizo? | Sí | La solución en términos que entienda alguien sin contexto técnico. |
| ¿Qué no se hizo? | Opcional | Solo si de verdad queda algo relevante afuera del alcance. |
| ¿Cuánto nos beneficia? | Sí | Tabla compacta Métrica/Antes/Ahora (o Esperado)/Cambio + una frase "en criollo" + nota de si es dato medido o proyectado. |
| Más información | Opcional | Un botón por link, con su propia etiqueta de audiencia arriba y la descripción como texto del botón (nunca un párrafo aparte + link genérico). |
| Importante | Opcional, va al final | Solo si hay una limitación o pendiente real que avisar. Ver `design-notes.md` #2 sobre por qué al final. |
| Footer | Sí | "Equipo de Producto de **Bind PSP**" + fecha. |

### Paso 4 — Construir el artifact y iterar con el PM

Copiá `references/template-artifact.html`, reemplazá los tokens `{{...}}`
y borrá los bloques `<!-- OPCIONAL -->` que no apliquen (enteros, no
dejarlos vacíos). Publicalo con la herramienta de Artifact y iterá con el
PM en la conversación — este es el mismo loop de ida y vuelta que ya
funcionó la primera vez: cada pedido de ajuste se aplica con Edit sobre el
mismo archivo y se republica a la misma URL.

### Paso 5 — Construir la versión de mail con el contenido ya aprobado

Recién cuando el PM da por bueno el artifact, copiá
`references/template-email-safe.html` y volcá **el mismo contenido ya
aprobado** (no reescribas la copy de nuevo) reemplazando los mismos
tokens. Prestá atención particular a `references/design-notes.md` #3-#7 —
son los ajustes que salieron de ver la primera versión en una bandeja
real y que no son evidentes mirando solo el código.

### Paso 6 — Envío de prueba

Mandá el mail a la casilla del propio PM (`identidad.local.md` tiene su
dirección) con la herramienta de Gmail (`htmlBody` = el HTML de
`template-email-safe.html` ya completado). Asunto:
`📣 NOVEDADES PRODUCTO - <Título>` (megáfono + mayúsculas fijas +
guion + título en minúscula/oración). Verificá con `get_message` que
llegó bien (ver Regla dura #6). Iterá acá tantas veces como haga falta —
cada ajuste visual se ve mejor en una bandeja real que en el artifact.

### Paso 7 — Envío real a toda Bind PSP

Solo después de que el PM confirme que la versión de prueba quedó bien:
preguntale explícitamente la dirección/alias/lista de destino para "toda
Bind PSP" (Regla dura #2) y pedile confirmación explícita de que sí, mandar
ahora — el envío a toda la empresa es una acción de alcance mucho mayor
que un mail a un colega, tratala con esa seriedad. Mandalo con el mismo
asunto (sin "revisión" ni número de ronda) y verificá igual con
`get_message`.

## 📄 Formato de salida

- [`references/template-artifact.html`](references/template-artifact.html)
  — plantilla del artifact (marca completa, dos temas, componentes
  reutilizados de `/pdf_build`).
- [`references/template-email-safe.html`](references/template-email-safe.html)
  — plantilla de mail (tablas, estilos inline, sin dependencias externas).
- [`references/design-notes.md`](references/design-notes.md) — por qué
  cada plantilla está armada como está, con los bugs concretos ya
  pisados.
- Paleta de marca: siempre la vigente en
  `.claude/skills/pdf_build/references/brand-bind-psp.md` del Cerebro
  activo — no la dupliques de memoria si ese archivo cambió.

## ✅ Checklist de calidad

- [ ] El esquema de secciones se confirmó con el PM antes de maquetar
- [ ] Ninguna sección opcional quedó "rellenada por completar" — las que
      no aplican están borradas enteras, no vacías
- [ ] Ningún número de la tabla de beneficios es inventado; si es
      proyección, la nota lo dice explícito
- [ ] El artifact fue aprobado por el PM antes de construir la versión de
      mail
- [ ] La versión de mail no tiene CSS grid/flexbox/variables, fuente de
      Google, ni SVG — solo tablas, estilos inline, emoji
- [ ] El botón de cada link tiene color/`text-decoration` en el `<a>`
      mismo, no en un hijo
- [ ] No quedó una fila divisoria blanca suelta antes de "Importante" (si
      esa sección está presente)
- [ ] Se mandó un envío de prueba a la casilla del propio PM y se
      confirmó con `get_message` que el contenido llegó bien
- [ ] El PM dio el OK explícito sobre la versión de prueba antes del
      envío real
- [ ] Se preguntó (nunca se asumió) la dirección/alias de destino del
      envío a toda Bind PSP
- [ ] Se confirmó con `get_message` que el envío real también llegó bien

## Historial

Nació en el Cerebro de Pablo Gomes a partir del primer newsletter real de
este tipo (el de "Mejora de tiempos en operaciones Wallet", disparado por
el caso de Pagos QR) y se sumó a `CEREBRO_CORE` para que Nicolás y Luciana
la tengan disponible en su próximo `SessionStart`/pull, igual que el resto
de las skills compartidas.
