---
proyecto: <nombre_corto>
idea_jira: <PRD-XXX o "pendiente">
version: 1.0
estado: Propuesta  # → "Aprobado por PM (YYYY-MM-DD)" en el Gate 4, o "Cerrado sin avanzar — <motivo>"
fecha: YYYY-MM-DD
pm: <nombre>
---

<!--
Artefacto de shaping de /idea_start. AUTOCONTENIDO: lo lee alguien sin acceso al Cerebro
(va tal cual a la descripción de la IDEA en Jira). Sin links a la wiki, sin nombres de
archivo ni de skill, sin códigos de ticket usados como si el lector los conociera.
Las fuentes se describen por su naturaleza, no por su ruta.
Niveles de evidencia en todo número: ✅ Validado · 🔶 Estimado (analogía) · ⚪ Supuesto.
-->

# <Título del proyecto — nombra el problema, no la solución>

## 1. Resumen

<4-6 líneas: el problema esencial y a quién afecta, cuánto pesa (con nivel de evidencia),
el foco, la solución recomendada y su tamaño, y el estado (propuesta / aprobada por el PM).>

## 2. Problema esencial

**Enunciado:** <[Afectado] necesita [necesidad] porque [razón] — una sola frase, sin solución.>

- **Afectado:** <segmento específico y accionable>
- **Job story:** Cuando <situación>, quiero <motivación>, para poder <resultado esperado>.
- **Cómo se resuelve hoy (alternativa actual):** <workaround / proceso manual / "nada" — y su costo>
- **Por qué ahora:** <fuerzas del cambio en 2-3 líneas>
- **Síntomas observados** (evidencia, no alcance): <lista corta>

### Magnitud

| Magnitud | Valor o rango | Cómo se obtuvo | Evidencia |
|---|---|---|---|
| Medida del problema | <ej. ~15 casos/semana> | <cálculo / analogía / supuesto + fuente descripta> | ✅ / 🔶 / ⚪ |
| Impacto | <ej. ~3 h/semana de Soporte · $X/mes> | | |

- **Meta:** <métrica> de <baseline> a <target> en <plazo>.
- **Incertidumbres que afectan la decisión:** <por cada número 🔶/⚪: qué evidencia lo validaría y cómo cambiaría el veredicto — o "Ninguna: todas las magnitudes clave están validadas".>

## 3. Foco

| Dentro | Fuera | Por qué |
|---|---|---|
| | | |

## 4. ¿Vale la pena?

| Dimensión | Qué dice la evidencia | Veredicto |
|---|---|---|
| Encaje con la estrategia y las métricas norte | | |
| Tamaño real (escenario conservador si hay ⚪/🔶) | | |
| Costo de oportunidad | | |
| Demanda repetida / a quién más le sirve | | |
| Riesgo de no hacerlo | | |
| Solapamiento con otros proyectos | | |

**Veredicto:** ✅ Vale la pena ahora / ⚠️ Obligatorio (<tipo · quién · deadline · qué pasa si no se hace>) — <una línea>.

## 5. Alternativas de solución

| # | Carril | Alternativa | Cubre del problema | Tamaño (analogía) | Tiempo a valor | Quién la ejecuta |
|---|---|---|---|---|---|---|
| A0 | 0 · No hacer nada | Convivir con el problema | — | Costo del problema: <valor/período> | — | — |
| A1 | 1 · Operativa / sin desarrollo | | | <h/semana de <área>> + <SP de ajustes> | | |
| A2 | 2 · Acotada / mínima | | | <S/M/L/XL · rango SP> | | |
| A3 | 3 · Amplia / generalizable | | | <rango SP> | | |

<!-- Un carril que no aplica: fila con "No aplica — <motivo>". Puede haber más de una fila por carril
y combinaciones (ej. "A1 ya + A2 después"). -->

### Fichas

**A1 — <nombre>.** <qué es · qué cubre y qué no · tamaño y "se parece a <iniciativa descripta>, que costó X" · dependencias y riesgos · escalabilidad y reversibilidad — 5-8 líneas.>

<!-- una ficha por alternativa -->

> Los tamaños son estimaciones gruesas de shaping, por analogía con iniciativas ya cerradas (tamaño real, no estimado). No son el dimensionamiento del equipo técnico: se refinan en la especificación.

## 6. Solución recomendada

**Recomendación:** <alternativa o combinación> — <una frase>.

- **Por qué resuelve el problema esencial en el foco:** <2-3 líneas>
- **Costo / beneficio:** <tamaño vs. medida e impacto, sobre el escenario conservador>
- **Por qué no las otras:** <una línea por alternativa, incluida "no hacer nada">
- **Qué la invalidaría:** <señal concreta>
- **Repuesto:** <segunda mejor opción>
- **Sensibilidad a la evidencia:** <si los números inciertos se validan arriba/abajo, qué cambia>

**Decisión del PM:** <Aprobada tal cual / Aprobada con ajuste: … / Eligió <otra alternativa> porque …> — YYYY-MM-DD.

## 7. Preguntas abiertas para el análisis funcional-técnico

<Las dudas técnicas que no hicieron falta para elegir y que tiene que resolver el diseño de la solución. Lista numerada.>

## 8. Fuentes consultadas y material incorporado

<Lista descriptiva: "métricas semanales de volumen (agosto 2026)", "minuta de reunión con Soporte (2026-09-01)",
"documentación técnica del procesador X (versión …)". Qué material se pidió y no llegó.>

## Historial de revisiones

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | YYYY-MM-DD | Versión inicial del shaping |
