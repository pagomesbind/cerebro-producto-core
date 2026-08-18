---
name: idea_problem
description: Genera un problem statement — documento breve que enmarca un problema (quién lo sufre, impacto de negocio, criterios de éxito) antes de proponer una solución. Se activa con /idea_problem.
when_to_use: Se activa cuando el usuario ejecuta el comando de barra /idea_problem, típicamente al arrancar una IDEA/iniciativa nueva, cuando un proyecto se desvió de su intención original, o para comunicar prioridades a liderazgo antes de saltar a "cómo" resolver algo.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre del problema a enmarcar]"
---

<!-- Adaptado de product-on-purpose/pm-skills (define-problem-statement), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->

# 🎯 PROBLEM STATEMENT: /idea_problem

## Por qué existe esta skill

Es fácil saltar directo a "cómo lo resolvemos" sin haber acordado primero "qué problema estamos resolviendo, para quién, y por qué importa ahora". Un problem statement es un documento corto que fuerza ese orden: enmarca el problema, conecta su impacto en usuarios con el impacto de negocio, y define cómo se va a medir el éxito — **antes** de comprometer a un equipo con una solución. Sirve de base para todo lo que viene después (discovery, PRD, roadmap).

## Cuándo NO usarla

- El problema ya está acordado y lo que falta es el spec para ingeniería → eso es un PRD, no esta skill.
- Lo que hace falta es comparar y proponer distintas soluciones → eso es un solution brief, no un problem statement.
- Lo que se quiere capturar es la motivación del usuario en sus propias palabras (jobs-to-be-done) más que el problema de negocio → es un ejercicio distinto.
- El "problema" en realidad es un supuesto sin validar → primero hay que enmarcarlo como hipótesis y probarlo antes de comprometer un equipo (ver `../../../wiki/2_areas/gaps_y_preguntas.md`).

*(Estos son deslindes conceptuales, no apuntan a otras skills de la casa — si en el futuro se suman skills equivalentes para PRD, solution brief o hipótesis, se puede linkear acá.)*

## ⚖️ Reglas duras

1. **Describe el "qué" y el "para quién", nunca el "cómo".** Si el draft empieza a prescribir una solución, es una señal de que se está mezclando con otro artefacto — cortá y marcalo como fuera de alcance.
2. **Nada de "usuarios" genérico.** El segmento afectado tiene que ser específico y accionable: "comercios adherentes dando de alta una cuenta", no "usuarios".
3. **Todo impacto y toda métrica llevan número o estimación razonable**, nunca una afirmación sin sustento. Si no hay dato, marcalo como pregunta abierta en vez de inventarlo.
4. **No inventes conclusiones de negocio ni cifras** — si el usuario no las tiene a mano, dejalas como `[pendiente]` y anotá el gap.
5. **El documento es siempre autocontenido.** Es la previa a un documento que puede terminar en manos de alguien sin acceso a este sistema (liderazgo, otra área, un tercero) — sin links a la wiki, sin nombres de archivo o de skill, sin códigos de ticket (PRD-XXX) usados como si el lector los reconociera, sin jerga de proceso interno. Toda afirmación se explica en el propio texto.
6. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto antes de escribir

1. **Resolver la asociación a proyecto:** si el argumento o la conversación mencionan una IDEA (`PRD-XXX`) o un proyecto trackeado, resolvé su ruta real en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 (nunca asumas `1_proyectos/prd-XXX_<slug>/` directo) y leé su `proyecto.md` completo antes de empezar. Si es miembro de un proyecto general, leé también el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre. **Si ya existe `artefactos/problem_statement_<tema>.md`** de una corrida anterior, leelo completo — esta corrida lo actualiza in place (ver Paso 7), no genera un documento nuevo en paralelo.
2. Si el problema **no** está asociado a ningún proyecto trackeado, preguntá si esto arranca un discovery propio nuevo (en ese caso seguí el Paso 1.b de [`/debrief`](../debrief/SKILL.md) para crear la carpeta) o si es exploración suelta sin proyecto → el destino final es `outputs/`.
3. **Contexto de producto:** leé el overview del producto afectado en `wiki/2_areas/overview_productos/overview_<producto>.md` y, si hace falta profundidad, navegá desde `wiki/index.md` hacia `wiki/3_recursos/detalle_productos/<producto>/` (progressive disclosure — nunca cargar toda la wiki).
4. **Contexto de clientes:** si el problema involucra clientes concretos, leé sus fichas en `wiki/2_areas/clientes/`.
5. **Contexto estratégico:** consultá `wiki/2_areas/direccion/north_star.md` y `wiki/2_areas/direccion/decisiones.md` para saber si este problema ya conecta con un OKR o foco vigente.
6. Solo después de tener este contexto, preguntale al usuario lo que falte. Nunca preguntes algo que la wiki ya responde.

### Paso 1 — Identificar el segmento de usuario

Preguntá quién sufre este problema. Sé específico sobre la persona, el rol o el segmento — "comercios chicos que cobran con QR", "analistas de PLD revisando alertas de KYC", "usuarios de Wallet enviando su primera transferencia" — nunca "usuarios" a secas.

### Paso 2 — Entender los puntos de dolor

Explorá qué fricción, frustración o necesidad insatisfecha vive ese segmento. Buscá evidencia real: research de usuarios, tickets de soporte, datos de comportamiento, quejas recurrentes en reuniones con clientes. Si no hay evidencia todavía, decilo explícitamente en vez de asumirla.

### Paso 3 — Establecer el contexto de negocio

Conectá el problema del usuario con el impacto de negocio: ¿cómo afecta ingresos, retención, crecimiento, cumplimiento regulatorio (BCRA/UIF/PCI DSS) o algún OKR/foco estratégico vigente? ¿Por qué invertir en esto ahora y no después?

### Paso 4 — Definir métricas de éxito

Identificá qué métricas se van a mover si el problema se resuelve. Establecé baseline actual y target, con fecha. Sé específico — nada de "mejorar la experiencia" sin un número atrás.

### Paso 5 — Relevar restricciones y consideraciones

Anotá limitaciones técnicas, dependencias de proveedores externos (ej. Fintexa, procesadores), requisitos regulatorios (BCRA, UIF, PCI DSS) o de capacidad de equipo que van a condicionar el espacio de soluciones.

### Paso 6 — Capturar preguntas abiertas

Documentá lo que todavía no se sabe: qué supuestos hay que validar, qué research adicional falta. Esto alimenta `../../../wiki/2_areas/gaps_y_preguntas.md` en el cierre (Paso 7.4).

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md). Un problem statement completo llena las 6 secciones: Resumen del problema; Impacto en usuarios; Contexto de negocio; Criterios de éxito; Restricciones y consideraciones; Preguntas abiertas.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (abandono en el alta de comercios de Adquirencia — cifras ilustrativas, no datos reales de Bind).

## ✅ Checklist de calidad

Antes de dar el problem statement por terminado, verificá:

- [ ] El problema es específico a un segmento definido (no "todos los usuarios")
- [ ] El impacto está cuantificado con datos o estimaciones razonables
- [ ] Las métricas de éxito tienen baseline y target
- [ ] El problema describe el "qué" sin prescribir el "cómo"
- [ ] El contexto de negocio explica por qué esto importa ahora
- [ ] Las preguntas abiertas quedaron registradas para seguimiento
- [ ] El documento es autocontenido: sin links a wiki, sin nombres de archivo/skill, sin códigos de ticket, sin jerga de proceso interno

## Paso 7 — Cierre estándar

1. **Persistir el entregable:**
   - Si está asociado a una IDEA/proyecto trackeado → `artefactos/problem_statement_<tema>.md` (sin fecha en el nombre — versión en el frontmatter + historial de revisiones al pie) dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde `proyecto.md` (secciones "Problema y contexto" y "Seguimiento PM"). **Si el archivo ya existía**, esta corrida lo actualiza: reescribí limpio el estado vigente y sumá una entrada al historial de revisiones — no crear un archivo nuevo en paralelo.
   - Si no está asociado a ningún proyecto → `outputs/`, con el mismo criterio de actualizar in place si ya existe uno sobre el mismo tema.
2. **Decisiones confirmadas por el usuario durante la sesión** → `decisiones.md` del proyecto si son específicas de él (directo); item `tipo: decision` en `contexto_vivo/` si son de contexto fijo.
3. **Preguntas abiertas del Paso 6** → `gaps.md` de la IDEA/proyecto (severidad según impacto) si son específicas de él (directo); item `tipo: gap` en `contexto_vivo/` si son de contexto fijo.
4. **Índices:** actualizá `wiki/1_proyectos/index.md` (última actividad) si hay proyecto; `wiki/index.md` solo si cambió una sección de nivel PARA.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
7. Cerrá sugiriendo el paso lógico siguiente: llevar este problem statement a discovery/PRD (con las skills correspondientes cuando existan) o a `/debrief` si el trabajo de esta sesión excede el alcance del documento.
