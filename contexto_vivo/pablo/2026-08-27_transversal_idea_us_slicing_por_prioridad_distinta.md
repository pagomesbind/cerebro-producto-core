---
id: 2026-08-27_transversal_idea_us_slicing_por_prioridad_distinta
pm: pablo
fecha_captura: 2026-08-27
fuente: "sesión libre con el PM, revisión de las historias de usuario de PRD-202 (/idea_us) — refinamiento del día siguiente a la convención de frontera de equipo ya mergeada"
producto: transversal
tema: Refinamiento del slicing de /idea_us — una diferencia de prioridad real entre dos variantes del mismo verbo también amerita separarlas en historias distintas
tipo: decision
destino_propuesto: .claude/skills/idea_us/SKILL.md (Paso 3 — precisión del 2026-08-26 sobre frontera de equipo, ya mergeada)
tipo_destino: actualizar
contradice: "no — es un refinamiento adicional a la precisión ya mergeada del 2026-08-26 sobre frontera de equipo (Paso 3), no la contradice"
confianza: alta
estado: ingestado
merge_commit:
---

## Contexto

El criterio de "frontera de equipo" capturado el 2026-08-26 (ya mergeado a `.claude/skills/idea_us/SKILL.md` Paso 3) resolvió el caso de componentes internos del mismo equipo (ej. Wallet-cuentas + KYC-wrapper) — pero dejaba sin resolver un caso relacionado: dos variantes del **mismo verbo HTTP**, del **mismo equipo**, para el **mismo consumidor**, que sin embargo tienen prioridad real distinta.

Caso concreto: en PRD-202, `GET /cuenta/kyc/{codigo}/estado` (consulta liviana, responde con la copia propia de Wallet) y `GET /cuenta/kyc/{codigo}/completo` (consulta completa, pasamanos hacia Onboarding) habían quedado empaquetadas en una sola historia (v4.0 US-2) — ambas son un `GET`, del equipo de Wallet, para el mismo consumidor (la organización). El PM señaló que deberían separarse por dos motivos que coinciden en este caso pero son independientes entre sí:

1. La consulta completa **sí cruza a Onboarding** (otro equipo, vía un endpoint dedicado) mientras que la liviana no — esto ya estaba cubierto por el criterio de frontera de equipo, pero la v4.0 no lo había aplicado con el nivel de detalle correcto dentro de una misma historia con dos variantes de lectura.
2. La consulta completa **ya estaba documentada como "no prioritaria"** desde una decisión del 2026-08-18 (contrato de 4 endpoints confirmado con Wallet y Onboarding: "GET completo... no prioritario, consulta puntual de detalle completo") — dato que la v4.0 tampoco había reflejado en la columna de prioridad (todas las historias del camino P0 habían quedado igualadas a P0).

## Decisión — regla adicional

**Una diferencia de prioridad real entre dos variantes del mismo verbo/interfaz también amerita separarlas en historias distintas, aunque compartan equipo, consumidor y verbo HTTP.** No alcanza con "es un GET del mismo equipo para el mismo consumidor" para mantenerlas juntas si una es núcleo de un camino P0/Must-have y la otra es una consulta puntual de menor uso (P1/Should-have o inferior) — la prioridad distinta ya es señal de que son capacidades independientes, estimables y planificables por separado (una puede lanzarse en un sprint posterior sin bloquear a la otra).

Cuando la variante de menor prioridad además cruza a otro equipo (como en este caso), **la contraparte de ese otro equipo hereda la misma prioridad menor** — es la misma capacidad de cara a los dos lados de la frontera, así que no tiene sentido que un lado sea P0 y el otro P1 para la misma funcionalidad.

Esta regla se suma a las ya mergeadas en Paso 3 (frontera de equipo, verbos distintos, continuación no es historia aparte, título con alcance explícito) — no las reemplaza.

## Caso aplicado (para referencia del merge)

En PRD-202 (Fase 1), este refinamiento subió las historias de 9 a 10 (v5.0 de `onboarding_consolidado-us.md`): la consulta liviana se queda en US-2 (P0), nace US-5 con la consulta completa (P1), y su contraparte de Onboarding (US-4) baja de P0 a P1 para ser consistente. Ver el detalle completo en [`1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/artefactos/onboarding_consolidado-us.md`](../proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/artefactos/onboarding_consolidado-us.md) v5.0, sección "Nota para el PM antes de revisar".

## Propuesta de aplicación a la skill

Agregar como una regla complementaria más dentro del mismo párrafo de precisión del Paso 3 ya mergeado (después de la regla (b) sobre verbos distintos), con una letra nueva:

> (e) una diferencia de prioridad real entre dos variantes del mismo verbo (ej. una consulta liviana de uso frecuente vs. una consulta completa de uso puntual, ya señalada como "no prioritaria" en una decisión previa) también amerita separarlas en historias distintas, aunque compartan equipo, consumidor y verbo HTTP — son capacidades planificables por separado. Si la variante de menor prioridad cruza a otro equipo, la contraparte de ese equipo hereda la misma prioridad.

No se propone cambiar nada más del Paso 3 ni del resto de la skill.
