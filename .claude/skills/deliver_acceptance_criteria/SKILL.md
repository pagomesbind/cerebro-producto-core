---
name: deliver_acceptance_criteria
description: Genera criterios de aceptación Given/When/Then estructurados para una historia de usuario o slice de feature, cubriendo happy path, escenarios de falla y expectativas no funcionales. Se activa con /deliver_acceptance_criteria.
when_to_use: Se activa cuando el usuario ejecuta /deliver_acceptance_criteria, típicamente cuando una historia de usuario o sección de PRD ya existe y hace falta profundizar en condiciones de pass/fail verificables para handoff a ingeniería y sign-off de QA.
disable-model-invocation: true
argument-hint: "[historia o slice de feature a detallar]"
---

<!-- Adaptado de product-on-purpose/pm-skills (deliver-acceptance-criteria), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->

# ✅ CRITERIOS DE ACEPTACIÓN: /deliver_acceptance_criteria

## Por qué existe esta skill

Los criterios de aceptación definen el comportamiento observable que tiene que cumplirse para dar una historia por terminada. [`/deliver_user_stories`](../deliver_user_stories/SKILL.md) ya incluye algunos criterios básicos por historia; esta skill profundiza uno puntual — happy path, casos borde, estados de error y expectativas no funcionales — en escenarios Given/When/Then que ingeniería y QA pueden verificar sin adivinar la intención.

## Cuándo NO usarla

- Necesitás las historias de usuario en sí, no profundizar criterios de una que ya existe → usá [`/deliver_user_stories`](../deliver_user_stories/SKILL.md).
- Todavía no hay ninguna historia o slice a la cual atar los criterios → escribí primero la historia o el PRD correspondiente.

## ⚖️ Reglas duras

1. **Solo lenguaje Given/When/Then.** Cada criterio tiene que ser testeable de forma independiente, sin detalles de implementación.
2. **Happy path primero, después excepciones.** Empezá por el flujo principal de éxito, y sumá casos borde y estados de error que sean probables o costosos si se pasan por alto.
3. **Todo estado de falla describe recuperación.** Qué ve o puede hacer el usuario cuando una validación falla, una dependencia no está disponible, o una acción no se puede completar.
4. **Un criterio, un resultado.** Si dos criterios describen el mismo comportamiento, fusionalos o separalos hasta que la intención sea clara.
5. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Confirmar el alcance de la historia o feature

Identificá el slice exacto de trabajo. Si el alcance no está claro, pedí la historia de usuario, sección de PRD o descripción de feature antes de escribir criterios — no lo inventes.

### Paso 1 — Separar happy path de excepciones

Empezá por el flujo principal de éxito, y sumá casos borde y estados de error relevantes.

### Paso 2 — Escribir cada criterio como escenario observable

Solo lenguaje Given/When/Then. Cada criterio independientemente testeable, sin detalles de implementación.

### Paso 3 — Cubrir comportamiento de recuperación y falla

Describí qué ve o puede hacer el usuario cuando una validación falla, una dependencia no está disponible, o una acción de guardado no puede completarse.

### Paso 4 — Incluir expectativas no funcionales

Sumá criterios de performance, accesibilidad, seguridad, confiabilidad o auditoría cuando le importen a la historia — particularmente relevante en flujos que tocan datos regulados (KYC/AML, pagos).

### Paso 5 — Evitar duplicación y solapamiento

Cada criterio testea un solo resultado.

### Paso 6 — Revisar testeabilidad

Un revisor tiene que poder aprobar o rechazar cada criterio sin interpretación. Si un enunciado es subjetivo, reescribilo como resultado medible.

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md). Una respuesta completa:

- Recapitula el contexto de la feature o historia
- Agrupa criterios en happy path, casos borde, estados de error y criterios no funcionales
- Usa enunciados Given/When/Then explícitos por criterio
- Anota supuestos o preguntas abiertas cuando el contexto esté incompleto

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo.

## ✅ Checklist de calidad

- [ ] Los criterios mapean a una historia o slice específico
- [ ] El happy path está cubierto primero
- [ ] Los casos borde son explícitos, no implícitos
- [ ] Los estados de error incluyen comportamiento de recuperación visible al usuario
- [ ] Se incluyen criterios no funcionales cuando corresponde
- [ ] Cada criterio es testeable y tiene un resultado claro
- [ ] No hay detalles de implementación filtrados en los criterios

## Paso 7 — Cierre estándar

1. **Persistir el entregable**: si profundiza una historia ya guardada en `artefactos/`, actualizá ese mismo archivo (no dupliques); si es nuevo, resolvé la ruta real de la IDEA en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 y guardalo en `artefactos/YYYY-MM-DD_criterios_aceptacion_<tema>.md` dentro de su carpeta.
2. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
4. Siguiente paso sugerido: [`/deliver_launch_checklist`](../deliver_launch_checklist/SKILL.md) cuando la feature esté lista para coordinar el lanzamiento.
