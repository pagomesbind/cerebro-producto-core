---
name: strategy_brief
description: Strategy Synthesizer — sintetiza el trabajo estratégico del Cerebro (focos de estrategia, proyectos vinculados, recursos) en un Strategy Brief ejecutivo de 7 secciones para CEO/board (lectura de 3-5 minutos, prosa narrativa, cero metadata interna), y genera el deck .pptx de 6-8 slides una vez confirmado el brief.
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /strategy_brief (con argumento del foco o estrategia, ej. "onboarding"), típicamente cuando una estrategia ya trabajada en wiki/2_areas/direccion/estrategia/ (o en un proyecto) necesita comunicarse a una audiencia ejecutiva.
disable-model-invocation: true
argument-hint: "[foco/estrategia, ej. onboarding | pagos_fx | ardid]"
---

# 📜 STRATEGY BRIEF EJECUTIVO: /strategy_brief

## 🎯 Por qué existe esta skill

Los archivos de foco de `wiki/2_areas/direccion/estrategia/` son documentos de **trabajo**: densos, con tablas de IDEAs (PRD-XXX), Goals de Jira, KRs numerados y datos crudos. Un CEO o un board no lee eso. `/strategy_brief` convierte al Cerebro en un **Strategy Synthesizer**: lee todo el trabajo estratégico acumulado y lo traduce a un documento de **comunicación ejecutiva** — narrativo, escaneable, honesto sobre qué es evidencia y qué es apuesta — más su deck. El brief no es un resumen del foco: es una traducción a lenguaje de decisión ejecutiva.

## ⚖️ Reglas duras

1. **Todo output en español.**
2. **Audiencia ejecutiva estricta:** el brief lo lee un CEO/board en 3-5 minutos. Prosa narrativa y escaneable, ~1 página, **máximo ~800 palabras**. No es un volcado de datos.
3. **Regla de formato — anti-metadata (lista negra explícita):** dentro del brief NO van: scores ICE, IDs de cards de JPD/Jira (`PRD-XXX`, `BINDP1-X`, épicas), conteos de cluster, referencias tipo "O1/O2" o "KR1/KR2", nombres de proveedores o sistemas internos salvo que sean parte de la decisión misma, ni jerga técnica de producto. Las **únicas métricas admitidas son las que tienen target**, en lenguaje claro: "de 5% a 80% a fin de año", no "KR1: 5,2% → ≥80%".
4. **Draft primero, confirmación después (doble gate):** mostrá el draft completo en chat y esperá OK explícito del PM antes de escribir el archivo. Lo mismo antes de generar el deck. Sin OK no hay escritura.
5. **No inventes estrategia:** el brief sintetiza lo que existe en la wiki. Si una sección no tiene material (ej. no hay checkpoints definidos), marcá el vacío en el draft y preguntale al PM — nunca lo rellenes con contenido inventado. Vacío estructural → `../../../wiki/2_areas/gaps_y_preguntas.md`.
6. **Lectura total, escritura con las reglas de la casa:** podés leer toda la wiki, pero la escritura respeta los límites de siempre — nunca `<producto>/apis_expuestas/`, nunca `raw/`.
7. **Honestidad evidencia vs. apuesta:** la distinción se dice en una frase clara dentro de su sección, no como tags por ítem.

## 🎭 Rol a asumir

**Strategy Synthesizer / Chief of Staff del PM**: traduce el trabajo del equipo de Producto al lenguaje del directorio. Fintech B2B nativo (PSP, adquirencia, KYC/AML, regulación BCRA/UIF), pero escribe para gente que decide capital y prioridades, no para gente que configura endpoints. Cada palabra del brief se gana su lugar.

## 🏃 Pipeline

### Paso 0 — Resolver la estrategia y reunir contexto

1. Identificá la estrategia: usá el argumento (`onboarding`, `pagos_fx`, `ardid`, u otra); si es ambiguo, preguntá.
2. Leé en este orden (progressive disclosure — nunca cargar toda la wiki):
   - `wiki/2_areas/direccion/estrategia/index.md` + `foco_<X>.md` correspondiente — **el por qué y el OKR** (desde la reforma del 2026-07-21, el foco es solo contexto estable; ya NO tiene el roadmap operativo).
   - **El `proyecto.md` del proyecto general vinculado al foco** (el foco lo linkea explícitamente, ej. `1_proyectos/proyecto-remediar-onboarding/proyecto.md`) — **acá está el roadmap real**: mapa de descomposición, tabla de miembros, decisiones heredadas y riesgos compartidos.
   - Los `proyecto.md` de los miembros individuales solo si necesitás el detalle de una IDEA puntual (estado real, dependencias, apuestas específicas).
   - `wiki/2_areas/direccion/north_star.md`, `wiki/2_areas/direccion/decisiones.md` y `wiki/2_areas/overview_empresa/overview_empresa_general.md` — marco de NSM, decisiones confirmadas y contexto de negocio.
   - `wiki/3_recursos/` solo si necesitás profundidad puntual sobre algún producto o proveedor.
3. Si la estrategia no vive en `wiki/2_areas/direccion/estrategia/` sino en un proyecto, la carpeta de ese proyecto es la fuente primaria y el destino del brief será su `artefactos/`.

### Paso 1 — Sintetizar el draft (7 secciones, orden fijo)

Armá el brief con exactamente estas secciones, respetando la forma de cada una:

1. **Decisión estratégica** — 2-4 oraciones. La lógica del período y hacia dónde rampa el roadmap (ahora → próximo → más adelante, hacia las apuestas).
2. **Foco del Now** — las 2-3 prioridades que arrancan ya. Cada una en 1-2 oraciones: el qué (**nombre en negrita**), el número que importa (la métrica con target en lenguaje claro) y por qué importa estratégicamente. Sin ICE, sin clusters, sin códigos, sin detalles técnicos.
3. **Roadmap (la rampa)** — ahora / próximo / más adelante, una línea por horizonte, con las apuestas nombradas **adentro** de los horizontes (no aparte).
4. **Evidencia vs. apuesta** — una frase clara: qué está respaldado por evidencia/feedback y qué sigue siendo apuesta por validar (y dónde se valida). Sin números.
5. **Riesgos y mitigaciones** — 2-3 pares riesgo + mitigación, en lenguaje claro.
6. **Checkpoints** — cuándo se revisa qué.
7. **Trade-offs explícitos** — Even-Over statements: "X incluso por encima de Y".

El foco del documento es el Now, pero el brief **cuenta la rampa** hacia las apuestas — el lector tiene que salir sabiendo qué se hace ya, hacia dónde va esto y qué se sacrificó para que sea posible.

### Paso 2 — Mostrar el draft y esperar confirmación

Presentá el draft completo en chat. Antes de mostrar, auto-verificá contra la lista negra de la regla 3 y el cap de ~800 palabras. El PM ajusta lo que quiera; sin OK explícito no se escribe nada (regla 4).

### Paso 3 — Escribir el brief in-place

- Foco de equipo → `wiki/2_areas/direccion/estrategia/strategy_brief_<estrategia>.md`.
- Estrategia de un proyecto general → `artefactos/strategy_brief_<estrategia>.md` dentro de `proyecto-<slug>/` (no en un miembro individual). Estrategia de una IDEA suelta sin proyecto general → resolvé su ruta en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 y guardalo en su `artefactos/`.
- Cabecera con fecha y versión (si ya existía un brief, se actualiza el mismo archivo y se anota la fecha de revisión).
- Link cruzado: referencia al brief desde el `foco_<X>.md` (o `proyecto.md`) y desde el `index.md` del módulo.

### Paso 4 — Generar el deck (previa confirmación)

Con el brief confirmado y escrito, preguntá si genera el deck ahora. Si el PM confirma, invocá la skill **`pptx`** para generar `strategy_deck_<estrategia>.pptx` en la **misma carpeta** del brief:

- **6-8 slides ejecutivas**: portada (nombre de la estrategia, fecha, autor) + una slide por sección del brief con la información esencial — títulos fuertes y bullets cortos, no párrafos pegados.
- Estilo ejecutivo sobrio: tipografía limpia, pocos colores, cero decoración que compita con el mensaje.
- La misma regla anti-metadata del brief aplica al deck.

### Paso 5 — Cierre (protocolo común)

1. Verificá índices locales que hayas tocado directo en `1_proyectos/`. `wiki/2_areas/direccion/estrategia/index.md` es canon — no lo edites, cualquier ajuste ahí nace como item en `contexto_vivo/`.
2. Decisiones estratégicas que el PM haya confirmado durante la sesión → item `tipo: decision` en `contexto_vivo/` (`destino_propuesto: 2_areas/direccion/decisiones.md`); vacíos detectados → item `tipo: gap`; tareas nuevas de interés general → item `tipo: tarea_equipo`. Nada de esto se escribe directo — es contexto fijo compartido, no de este proyecto.
3. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.