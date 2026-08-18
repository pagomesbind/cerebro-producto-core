---
name: idea_prd
description: Genera un Product Requirements Document (PRD) completo — qué se va a construir, por qué, y cómo se mide el éxito — para handoff formal a ingeniería. Se activa con /idea_prd.
when_to_use: Se activa cuando el usuario ejecuta /idea_prd, típicamente cuando el problema y la solución ya están alineados y hace falta un documento de especificación formal para coordinar múltiples equipos o para que stakeholders aprueben alcance antes de invertir.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre de la iniciativa a especificar]"
---

<!-- Adaptado de product-on-purpose/pm-skills (deliver-prd), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->

# 📋 PRD FORMAL: /idea_prd

## Por qué existe esta skill

`proyecto.md` en `wiki/1_proyectos/` es el estado vivo de una IDEA — decisiones, gaps, seguimiento PM, todo en evolución constante. Un PRD es otra cosa: un documento de especificación **congelado en un momento dado**, pensado para que ingeniería, QA y stakeholders lean una sola vez y entiendan qué se va a construir, por qué, y dónde están los límites de alcance. Esta skill no reemplaza a `proyecto.md` — lo destila en un artefacto formal de handoff cuando hace falta uno (coordinación multi-equipo, aprobación de stakeholders, documento de referencia durante desarrollo/QA).

## Cuándo NO usarla

- El problema todavía no está enmarcado o está en discusión → usá primero [`/define_problem_statement`](../define_problem_statement/SKILL.md); un PRD asume un problema ya acordado.
- Solo hace falta bajar el trabajo a historias de usuario para un sprint, sin necesidad de un documento de especificación completo → usá directamente [`/idea_us`](../idea_us/SKILL.md).
- Lo que se necesita es registrar una decisión técnica o arquitectónica puntual, no especificar una iniciativa de producto completa.

## ⚖️ Reglas duras

1. **Protocolo de contexto:** aplicá el Paso 0 antes de escribir una sola línea del PRD.
2. **No prescribas implementación.** El PRD define qué debe hacer el sistema y por qué, no el detalle de cómo construirlo — eso lo define ingeniería.
3. **Todo objetivo tiene que ser SMART y medible.** Alguien debería poder verificar en el futuro si se cumplió o no, sin ambigüedad.
4. **Alcance explícito**: qué entra, qué no entra, y qué queda diferido — nunca lo dejes implícito.
5. Legible en menos de 15 minutos. Si no entra, es señal de que el alcance es demasiado grande para un solo PRD.
6. Todo output en español.
7. **Nombrá la solución por lo que efectivamente se construye**, no por una abstracción ambigua que suene a un proceso o servicio ya existente (ej. "nuevas funcionalidades por API para favorecer X", no "el proceso de X"). Aplica sobre todo en el Resumen de la solución planteada y en Funcionalidades.
8. **Si el PRD es para audiencia externa** (un stakeholder fuera de Bind PSP, o interno sin contexto de este sistema — porque el pedido lo pide explícitamente, o porque preguntaste y así te lo confirmaron), el documento tiene que ser autocontenido: sin links a la wiki, sin nombres de archivo o de skill, sin códigos de ticket (PRD-XXX), sin jerga de proceso interno ("gap registrado en...", "según el artefacto..."). Toda afirmación se explica en el propio texto, en prosa que alguien sin contexto de este sistema pueda leer de punta a punta. Si no está claro si es para audiencia interna o externa, preguntá antes de escribir — cambia cómo se redacta cada sección, no es un ajuste de formato al final. El PRD interno por default sí mantiene links (a problem statement, a `proyecto.md`, a decisiones) porque sirven de trazabilidad para quien ya tiene acceso a la wiki.

## 🏃 Pipeline

### Paso 0 — Contexto antes de escribir

1. Resolvé la ruta real de la IDEA en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 — nunca asumas `wiki/1_proyectos/prd-XXX_<slug>/` directo. Leé su `proyecto.md` completo — problema, alcance, decisiones y gaps ya registrados son la base del PRD, no se reinventan acá.
2. **Si es miembro de un proyecto general** (tiene cabecera `> **Proyecto:** [<Nombre>](../proyecto.md)`), leé también el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre — son decisiones ya cerradas a nivel proyecto que el PRD no debe re-litigar ni contradecir sin señalarlo explícitamente.
3. Si existe un problem statement o una hipótesis en `artefactos/`, leelos — el PRD recapitula el problema, no lo redefine.
4. Contexto de producto y estratégico: `wiki/2_areas/overview_productos/overview_<producto>.md`, `wiki/3_recursos/detalle_productos/<producto>/`, `wiki/2_areas/direccion/north_star.md`.
5. Contexto de arquitectura si la iniciativa toca proveedores externos: `wiki/3_recursos/arquitectura_sistema/`.
6. **Definí la audiencia antes de redactar:** ¿el PRD es para uso interno (ingeniería/QA/stakeholders con acceso a esta wiki) o para entregar a alguien externo al sistema (otra área sin contexto del Cerebro, un cliente, un proveedor)? Si el pedido del usuario no lo deja claro (ej. "generá el PRD para enviarlo" sugiere externo, "generá el PRD de la IDEA" sugiere interno), preguntá antes de escribir — condiciona regla dura #8 y cambia cómo se redacta cada sección, no es un ajuste de estilo al final.

### Paso 1 — Problema

Recapitulación breve del problema que se resuelve u oportunidad que se aprovecha, con link al problem statement si existe. El lector tiene que entender el *por qué* antes de llegar al *qué*.

### Paso 2 — Contexto

Por qué atacar esto ahora: de dónde surgió el tema, si es urgente, si es parte de un proyecto más grande estratégicamente. Conectá con el foco/OKR vigente si aplica (`wiki/2_areas/direccion/north_star.md`, `wiki/2_areas/direccion/estrategia/`).

### Paso 3 — Resumen de la solución planteada

Descripción breve de la solución propuesta, de cara al usuario y sin sobre-especificar implementación. Nombrala por lo que efectivamente se construye (regla dura #7) — si el lector no puede deducir de esta sección qué es lo nuevo que va a existir, es señal de que quedó demasiado abstracta.

### Paso 4 — Objetivos

Qué se espera lograr con este proyecto — objetivos y beneficios de negocio y/o operativos, pensados en formato SMART y medibles a futuro para poder validar si la idea implementada funcionó o no.

### Paso 5 — Caso de negocio

Justificación del beneficio monetizado esperado (o link a un archivo de business case si existe), considerando también el costo de construir la solución.

### Paso 6 — Definiciones, suposiciones y límites

Decisiones, limitantes, restricciones, riesgos o situaciones que condicionaron y llevaron a preferir este camino para resolver el problema — incluye restricciones técnicas, regulatorias (BCRA/UIF/PCI DSS) y dependencias de proveedores (Fintexa u otros) cuando corresponda.

### Paso 7 — Funcionalidades y roadmap

Todas las funcionalidades del proyecto, priorizadas con un framework explícito — por default **MoSCoW** (Must/Should/Could/Won't have), salvo que el proyecto ya use otro (ej. horizontes NOW/NEXT/LATER) y tenga sentido conservarlo. **Traducí el roadmap de trabajo ya definido para el proyecto, no inventes una priorización nueva** — cada IDEA/fase/funcionalidad ya tiene un lugar en el roadmap real (`proyecto.md`), este paso solo la vuelca al framework de priorización del PRD. Cada nivel de prioridad lleva un subtítulo que explica **qué significa ese nivel para el negocio**, no una etiqueta genérica — ej. "Must have — MVP, imprescindible para empezar a integrar clientes", no solo "Must have". El nivel "Won't have" incluye la razón del diferimiento si ayuda a entenderlo.

### Paso 8 — Flujos clave y referencias clave

Va **inmediatamente después de Funcionalidades y roadmap** — el lector entiende primero qué se construye y en qué orden, y recién después cómo se materializa en un flujo. El contenido es específico de cada proyecto: diagramas AS-IS/TO-BE, flujos de secuencia, user journey maps, casos de uso paso a paso, taxonomías o conceptos que el lector necesita para entender el resto del documento (ej. tipos de cliente, modalidades de integración) — o links a donde vivan si ya existen. **No hay una subestructura fija que aplique a todos los PRDs**: armá la que corresponda a lo que este proyecto necesita mostrar, no reuses la estructura de un PRD anterior por costumbre.

### Paso 9 — Análisis de impacto en las distintas áreas

Para cada área interesada de Bind PSP (Comercial, Soporte e integraciones, Administración, Fraude, Legales, Clientes externos ya en producción) — **solo incluí las que tengan un impacto real identificado**, no completes las 6 de forma automática. Para cada área que sí incluyas, analizá dos cosas: (1) cómo la afecta el proyecto (impacto Bajo/Medio/Alto y un análisis breve); (2) **si esa área ya tiene lo que necesita para actuar** sobre ese impacto. Si no lo tiene, marcalo explícitamente como gap — y determiná si hay que incorporar una funcionalidad al alcance del proyecto para resolverlo, o si alcanza con una contingencia operativa explícita. La columna de análisis no puede quedar como una descripción pasiva del impacto: tiene que dejar claro si el área puede actuar o no, y qué falta si no puede. Si no tenés información para evaluar alguna área, preguntale al usuario en vez de asumir — no completes "Nulo" por default.

### Paso 10 — Riesgos

Identificá y clasificá los riesgos del proyecto: probabilidad, impacto y mitigación para cada uno. Incluí acá los gaps de capacidad detectados en el Paso 9 que todavía no tengan resolución.

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md) — es el estándar de PRD de la casa. Un PRD completo llena, en este orden: Problema; Contexto; Resumen de la solución planteada; Objetivos; Caso de negocio; Definiciones, suposiciones y límites; Funcionalidades y roadmap; Flujos clave y referencias clave; Análisis de impacto en las distintas áreas; Riesgos.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (cifras ilustrativas).

## ✅ Checklist de calidad

- [ ] El problema y el "por qué ahora" están claramente articulados
- [ ] La solución está nombrada por lo que efectivamente se construye, no por una abstracción ambigua
- [ ] Los objetivos son SMART y medibles a futuro
- [ ] El caso de negocio contempla tanto el beneficio esperado como el costo de construir
- [ ] El alcance es explícito (dentro/fuera/futuro) y prioriza con el mismo framework que ya usa el roadmap real del proyecto
- [ ] Flujos clave va inmediatamente después de Funcionalidades y roadmap
- [ ] El análisis de impacto solo incluye áreas con impacto real, y cada una dice si puede actuar o si hay un gap (alcance o contingencia)
- [ ] Los riesgos tienen probabilidad, impacto y mitigación
- [ ] Si es para audiencia externa: sin links a wiki, sin nombres de archivo/skill, sin códigos de ticket, sin jerga de proceso interno
- [ ] El documento se lee en menos de 15 minutos

## Paso 11 — Cierre estándar

1. **Persistir el entregable** en `artefactos/YYYY-MM-DD_prd_<tema>.md` dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde la sección de entrega de `proyecto.md`.
2. **Decisiones de alcance confirmadas** → `decisiones.md` del proyecto (directo). Si es una decisión de contexto fijo (no específica de esta IDEA), capturala como item `tipo: decision` en `contexto_vivo/` en vez de escribir directo.
3. **Preguntas abiertas** → `gaps.md` de la IDEA/proyecto; `../../../wiki/2_areas/gaps_y_preguntas.md` solo si son de contexto fijo, no del proyecto.
4. **Índices:** tabla maestra de `wiki/1_proyectos/index.md` §2; `wiki/index.md` solo si cambió una sección de nivel PARA.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
7. **Jira:** nunca crear ni editar tickets a partir de este PRD sin confirmación explícita del usuario.
8. Siguiente paso sugerido: [`/idea_us`](../idea_us/SKILL.md) para bajar el PRD a historias de sprint.
