---
name: idea_problem
description: DEPRECADA el 2026-09-25 — absorbida en /idea_start (Fase 1, problema esencial). No usar; redirige a /idea_start.
when_to_use: No usar. Si el usuario ejecuta /idea_problem, explicale que se absorbió en /idea_start y ofrecé correr /idea_start sobre el proyecto (Modo D si ya existe la carpeta).
disable-model-invocation: true
argument-hint: "[PRD-XXX o nombre del proyecto] — redirige a /idea_start"
---

# ⛔ /idea_problem — DEPRECADA (2026-09-25)

Esta skill se absorbió en [`/idea_start`](../idea_start/SKILL.md). Su Fase 1 ("el problema esencial") cubre todo lo que hacía `/idea_problem`: el enunciado en una frase, el job story, la alternativa actual, las fuerzas del cambio, la medida y el impacto cuantificados (ahora con nivel de evidencia ✅/🔶/⚪ y descuento por incertidumbre) y la meta. El documento autocontenido que producía (`-problem.md`) lo reemplaza el artefacto `-start.md`.

**Si el usuario la invoca:**
1. Avisale que está deprecada y por qué, en una línea.
2. Resolvé el proyecto en `wiki/1_proyectos/index.md` §2.
   - Si ya existe la carpeta, ofrecé `/idea_start <nombre>` en Modo D: retoma desde el último gate cerrado, y si el problema ya estaba acordado, solo profundiza la magnitud.
   - Si no existe, ofrecé `/idea_start` desde cero.
3. No generes un `-problem.md` nuevo.

**Legacy:** los `artefactos/*-problem.md` ya existentes siguen siendo válidos y los leen `/idea_solution` y `/idea_prd` cuando no hay `-start.md`. `references/TEMPLATE.md` y `references/EXAMPLE.md` quedan como consulta histórica.
