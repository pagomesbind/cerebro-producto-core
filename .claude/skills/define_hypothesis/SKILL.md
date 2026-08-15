---
name: define_hypothesis
description: Convierte un supuesto en una hipótesis testeable, con métrica de éxito y forma de validarla. Se activa con /define_hypothesis.
when_to_use: Se activa cuando el usuario ejecuta /define_hypothesis, típicamente después de enmarcar un problema y antes de comprometerse con una solución, cuando el equipo tiene supuestos distintos sobre el comportamiento de los usuarios, o antes de invertir esfuerzo de ingeniería en algo sin validar.
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre del supuesto a testear]"
---

<!-- Adaptado de product-on-purpose/pm-skills (define-hypothesis), licencia Apache-2.0. https://github.com/product-on-purpose/pm-skills -->

# 🧪 HIPÓTESIS: /define_hypothesis

## Por qué existe esta skill

Muchas features se construyen sobre creencias nunca puestas a prueba ("los usuarios van a preferir X"). Una hipótesis convierte esa creencia en un enunciado falseable — algo que se puede validar o invalidar con evidencia — y deja explícito qué significa "éxito" antes de que el equipo invierta tiempo. Sirve de puente entre [`/define_problem_statement`](../define_problem_statement/SKILL.md) (qué problema hay) y el diseño de la solución o el experimento que lo prueba.

## Cuándo NO usarla

- Ya tenés la hipótesis clara y lo que falta es diseñar el A/B test en sí (variantes, tamaño de muestra, duración) — esta skill enmarca *qué* testear, no *cómo* instrumentarlo.
- El problema todavía no está enmarcado → usá primero [`/define_problem_statement`](../define_problem_statement/SKILL.md).
- Lo que necesitás es organizar muchos supuestos e ideas en una estructura de discovery más amplia, no un único enunciado testeable.

## ⚖️ Reglas duras

1. **Tiene que ser falseable.** Si no hay forma de que la hipótesis resulte falsa, no es una hipótesis — es una afirmación.
2. **Nunca "usuarios" a secas.** El segmento objetivo tiene que ser específico y accionable.
3. **La hipótesis no asume que la solución funciona** — describe qué se espera que pase, no por qué la solución elegida es la correcta.
4. **Toda métrica de éxito lleva baseline y target numérico**, no una dirección vaga ("mejorar").
5. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto antes de escribir

1. Si el argumento o la conversación mencionan una IDEA (`PRD-XXX`) o un proyecto trackeado, resolvé su ruta real en la tabla maestra de [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2 y leé su `proyecto.md` completo — en particular si ya existe un problem statement asociado, es la base de esta hipótesis. Si es miembro de un proyecto general, leé también el §4 "Definiciones y decisiones heredadas" del `proyecto.md` padre — no propongas hipótesis que contradigan una decisión ya cerrada.
2. Contexto de producto: `wiki/2_areas/overview_productos/overview_<producto>.md` y, si hace falta, `wiki/3_recursos/detalle_productos/<producto>/`.
3. Contexto estratégico: `wiki/2_areas/direccion/north_star.md` y `wiki/2_areas/direccion/decisiones.md`.

### Paso 1 — Enunciar la creencia

Formato estructurado: "Creemos que [acción/cambio] para [usuario objetivo] va a lograr [resultado esperado]." Sé específico sobre la intervención — una hipótesis vaga no se puede testear.

### Paso 2 — Identificar el usuario objetivo

Definí a quién aplica esta hipótesis con precisión: "comercios nuevos en su primera semana de alta", "usuarios de Wallet que ya hicieron 10+ transferencias", "comercios que abandonaron el alta y volvieron a intentar".

### Paso 3 — Definir el resultado esperado

¿Qué cambio de comportamiento o resultado se espera? Enmarcalo en términos de acciones del usuario (completa el alta, activa la cuenta, vuelve a los 7 días) más que en métricas internas cuando sea posible.

### Paso 4 — Fijar métricas de éxito

Elegí una métrica primaria que mida directamente el resultado esperado. Sumá métricas secundarias que den contexto y métricas guardrail que aseguren que no se está generando daño en otro lado.

### Paso 5 — Describir el enfoque de validación

¿Cómo se va a testear? A/B test, entrevistas a usuarios, prueba de prototipo, análisis de cohortes. Sé específico sobre tamaño de muestra, duración y requisitos estadísticos si aplica un experimento formal.

### Paso 6 — Documentar riesgos y supuestos

¿Qué podría invalidar esta hipótesis más allá del resultado del test en sí? ¿Qué estás asumiendo como verdadero sin haberlo validado?

## 📄 Formato de salida

Usá el template de [`references/TEMPLATE.md`](references/TEMPLATE.md). Un documento de hipótesis completo llena: Enunciado de la hipótesis; Contexto y fundamento; Segmento de usuario objetivo; Métricas de éxito; Enfoque de validación; Riesgos y supuestos; Cronograma.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (cifras ilustrativas).

## ✅ Checklist de calidad

- [ ] La hipótesis es falseable
- [ ] La métrica de éxito tiene un target numérico específico
- [ ] El segmento de usuario objetivo está claramente definido
- [ ] El enfoque de validación es práctico y tiene plazo
- [ ] Los criterios de pass/fail son inequívocos
- [ ] La hipótesis no asume que la solución funciona

## Paso 7 — Cierre estándar

1. **Persistir el entregable:** si está asociado a una IDEA/proyecto → `artefactos/YYYY-MM-DD_hipotesis_<tema>.md` dentro de la carpeta del miembro (la ruta resuelta en el Paso 0), referenciado desde `proyecto.md`. Si no → `outputs/`.
2. **Decisiones confirmadas** → `decisiones.md` del proyecto (directo) si son específicas de él; item `tipo: decision` en `contexto_vivo/` si son de contexto fijo.
3. **Riesgos/supuestos sin validar** → `gaps.md` de la IDEA (o del proyecto padre) si son relevantes más allá de este documento (directo); item `tipo: gap` en `contexto_vivo/` si son de contexto fijo.
4. **Índices:** `wiki/1_proyectos/index.md` si hay proyecto; `wiki/index.md` solo si cambió una sección de nivel PARA.
5. **Sin changelog y sin git.** El commit del repo personal lo hace el hook `SessionStart` una vez al día.
7. Siguiente paso sugerido: si la hipótesis se valida con una solución concreta, [`/deliver_prd`](../deliver_prd/SKILL.md).
