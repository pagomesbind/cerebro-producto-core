---
id: 2026-08-26_transversal_idea_us_slicing_por_frontera_de_equipo
pm: pablo
fecha_captura: 2026-08-26
fuente: "sesión libre con el PM, revisión de las historias de usuario de PRD-202 (/idea_us)"
producto: transversal
tema: Convención de slicing de historias de usuario en /idea_us — corte por frontera de equipo, no por componente técnico
tipo: decision
destino_propuesto: .claude/skills/idea_us/SKILL.md (Paso 3 — "Descomponer por entregable técnico completo")
tipo_destino: actualizar
contradice: "no — refina/precisa el Paso 3 actual de la skill, no lo contradice: sigue siendo corte por entregable técnico completo, pero ancla explícitamente qué cuenta como 'un' entregable"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

## Contexto

Al revisar con el PM la v3.1 de las historias de usuario de PRD-202 (Fase 1, alta de wallet PF mayor de edad validada por Onboarding), el PM notó que el slicing vigente separaba en historias distintas piezas de trabajo que construye el **mismo equipo**: `Wallet-cuentas` y el `KYC-wrapper` son dos servicios desplegables distintos, pero ambos los construye el equipo de Ingeniería de Wallet — al fragmentarlos en historias separadas (ej. "Wallet expone el endpoint" en una historia, "el wrapper reenvía a Onboarding" en otra), el tablero terminaba mezclando trabajo de dos equipos sin que se viera claro quién es dueño de qué, y sin aportar valor real de planificación (a Wallet, como equipo, le da lo mismo si el trabajo cae en el servicio de cuentas o en el wrapper — ambos son su propio backlog/sprint).

El PM pidió explícitamente que este criterio se aplique **siempre que se use `/idea_us`**, no solo en este proyecto.

## Decisión — el criterio de corte

**Una historia de usuario agrupa todo el trabajo que un mismo equipo de ingeniería tiene que construir para sostener una interfaz completa (endpoint, webhook o evento) frente a un consumidor — sin importar cuántos componentes/servicios internos de ese equipo participan para resolverla.**

Reglas concretas:

1. **El corte a una historia nueva ocurre únicamente cuando la interfaz cruza a un equipo de ingeniería distinto** — no en cada salto de red/componente interno dentro del mismo equipo. Si el Equipo A construye 2 servicios (ej. un servicio público + un servicio de orquestación interno) para resolver una sola capacidad de cara a un consumidor, es **una** historia del Equipo A — el salto interno entre sus propios servicios se documenta como parte del contexto/notas técnicas de esa misma historia (con su propio diagrama de secuencia si aporta claridad), no como una historia aparte.
2. **Cuando un flujo cruza una frontera de equipo real, nacen historias espejadas — una por cada lado que la construye.** Ej.: si el Equipo A expone un endpoint que internamente termina llamando a un endpoint que construye el Equipo B, son 2 historias: "Endpoint del Equipo A para que [consumidor] haga X" y "Endpoint del Equipo B para que el Equipo A [u otro consumidor interno] haga Y" — cada equipo puede estimar/construir/testear su lado contra el contrato ya acordado, sin esperar al otro.
3. **Un mismo verbo/acción con distinto consumidor sigue siendo una frontera distinta.** Ej.: un reporte que un equipo construye para un área de negocio (ej. Administración) es una historia aparte de un endpoint que ese mismo equipo construye para otro sistema, aunque ambos lean la misma tabla — el consumidor cambia, así que el criterio de aceptación y el timing de entrega también pueden cambiar.
4. **Dentro del mismo equipo y el mismo consumidor, un verbo/interacción distinto (crear vs. consultar vs. actualizar) sigue mereciendo su propia historia** cuando cada uno es una capacidad independiente y estimable por separado (ej. `POST` y `GET` de un mismo recurso público) — el criterio de "bocado grande" es sobre no fragmentar por *componente interno*, no sobre colapsar verbos HTTP distintos en una sola historia.
5. **Una continuación/reintento sobre la misma capacidad no es una historia aparte** si la resuelve el mismo motor/endpoint que ya construyó el equipo para el caso base (ej. "completar un dato faltante" y "reintentar un documento ilegible" son ambos el mismo endpoint de continuación procesado por el mismo motor — van como AC de la misma historia, no como historias separadas).
6. **Título explícito de alcance:** cada historia nombra la interfaz que construye y aclara qué NO incluye del otro lado de la frontera (ej. "Endpoint Wallet POST /x para organizaciones — no incluye Onboarding") — para que no haya ambigüedad de dueño ni la historia dependa de leer otra para saber dónde termina su propio alcance.
7. **Esto no reduce la profundidad de los criterios de aceptación.** El checklist obligatorio de la skill (contrato de interfaz, validaciones, seguridad/BOLA/BOPLA, errores/resiliencia, versionado si aplica — ver Paso 5 de `/idea_us`) sigue aplicando completo a cada historia, incluidas las de contrato interno entre equipos (no solo las públicas de cara a un cliente externo). "Bocado grande" es sobre la granularidad de cuántas historias nacen, no sobre cuánto detalle lleva cada una.

## Caso aplicado (para referencia del merge)

En PRD-202 (Fase 1), este criterio bajó las historias de 13 a 9 sin perder ningún criterio de aceptación — el detalle completo de la resegmentación (con mapa de equivalencia historia por historia) queda documentado en [`1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/artefactos/onboarding_consolidado-us.md`](../proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/artefactos/onboarding_consolidado-us.md) v4.0, sección "Nota para el PM antes de revisar".

## Propuesta de aplicación a la skill

Al mergear, agregar este criterio como precisión del **Paso 3** de `.claude/skills/idea_us/SKILL.md` ("Descomponer por entregable técnico completo") — hoy ese paso dice que el eje de corte es "el componente técnico completo que hay que construir" pero no ancla explícitamente ese componente a quién lo construye, que es la ambigüedad real que generó la confusión. Sugerencia de redacción a integrar (el PM no pidió un texto literal, esto es una propuesta de partida para que el runner de `/context_merge` la ajuste):

> El eje de corte no es el servicio/componente técnico en sí, sino **el equipo de ingeniería que lo construye frente a un consumidor**. Si un mismo equipo resuelve una capacidad a través de más de un servicio/componente interno propio, es una sola historia — el salto interno se documenta en Contexto/Notas técnicas, no como historia aparte. El corte a una historia nueva ocurre cuando la interfaz cruza a un equipo de ingeniería distinto; ahí nacen historias espejadas, una por cada lado que la construye. Un verbo/interacción distinto (crear vs. consultar vs. actualizar) sobre el mismo consumidor sigue mereciendo su propia historia cuando es una capacidad independiente y estimable por separado; una continuación/reintento que resuelve el mismo motor/endpoint ya construido no lo es — va como AC de la misma historia. El checklist de contrato de API (Paso 5) sigue aplicando completo a cada historia, incluidas las de contrato interno entre equipos.

No se propone cambiar nada del resto de la skill (Pasos 0, 1, 2, 4, 5, 5bis, 5ter, 6, 7, 8 quedan igual) — es una precisión puntual del Paso 3.
