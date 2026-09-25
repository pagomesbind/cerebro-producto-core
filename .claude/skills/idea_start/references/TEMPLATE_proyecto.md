<!--
Esqueleto de proyecto.md para un proyecto nacido de /idea_start. Reemplazá cada <placeholder>.
proyecto.md es el REPOSITORIO VIVO del proyecto (info general, actualizaciones, ingestas, TODO):
lo siguen escribiendo /sync_meetings, /sync_mails, /debrief y el resto de las skills después del shaping.
El shaping aprobado vive en artefactos/<nombre>-start.md — §1-§4 lo resumen y linkean, no lo duplican.
Las 9 secciones canónicas van desde el minuto cero; el anexo de discovery va DESPUÉS de §9
y se disuelve al cerrar (ver "proyecto.md y su anexo de discovery" en SKILL.md).
-->

# <Título corto y descriptivo del proyecto>

> **Origen:** discovery propio vía `/idea_start` (YYYY-MM-DD) <!-- o "⚠️ Obligatorio — <tipo> · <quién> · <deadline>" -->
> **PM:** <nombre> · **Producto:** <producto dueño> · **Cliente:** <cliente o "— (interno/varios)">
> **IDEA:** <PRD-XXX> (DISCOVERY) <!-- o "— (pendiente, conector)" -->
> **Estado:** 🔵 En discovery
<!-- Si es miembro de un proyecto general:
> **Proyecto:** [<Nombre del padre>](../proyecto.md) · **KR/Canal:** <...> · **Slice:** <...>
Si el PM siguió contra el veredicto:
> **Continuación:** por decisión del PM contra veredicto <🟡/❌> (YYYY-MM-DD) — <motivo>
-->

## 1. Resumen ejecutivo

<3-5 líneas. Al cerrar el Gate 4: problema, foco, solución aprobada y tamaño — con link a
[`artefactos/<nombre>-start.md`](artefactos/<nombre>-start.md).>

## 2. Problema y contexto

<Al cerrar el Gate 1: el enunciado en una frase + la medida con su nivel de evidencia (✅/🔶/⚪).
El detalle vive en el -start.md §2 — no repetirlo.>

<!-- Si es miembro de un proyecto general:
## 2bis. Encaje en el proyecto
- **Qué pedazo entrega:** ...
- **Qué hereda ya cerrado:** ...
- **De qué depende / qué depende de él:** ...
-->

## 3. Alcance y definición

<Al cerrar el Gate 2: la frontera del foco en 2-3 líneas (Dentro / Fuera), link al -start.md §3.
Después la amplían /idea_solution y /idea_prd.>

## 4. Entrega

<Al cerrar el Gate 4: alternativa aprobada, carril y tamaño preliminar de shaping. Después: IDEA,
Epic e Historias de Jira, hitos.>

## 5. Decisiones del proyecto

<Una línea por decisión relevante — el detalle en `decisiones.md`.>

## 6. Gaps abiertos

<Remite a `gaps.md` — incluye las incertidumbres ⚪/🔶 no validadas.>

## 7. Seguimiento PM

<Próximos pasos, riesgos y dependencias no-desarrollo, TODO.>

## 8. Notas de sesiones

<!-- La nota de sesión linkea, nunca copia:
### Sesión YYYY-MM-DD — /idea_start
Shaping inicial. Resultado en [`artefactos/<nombre>-start.md`](artefactos/<nombre>-start.md);
proceso en el [Anexo — Registro del discovery](#anexo--registro-del-discovery-yyyy-mm-dd).
-->

## 9. Historial de sync

- **YYYY-MM-DD** — Creación vía `/idea_start`. IDEA <PRD-XXX> creada en DISCOVERY.

---

<!--
=====================================================================================
A PARTIR DE ACÁ: el anexo vivo durante la sesión. Al cerrar (Paso 8/9) se colapsa en
"## Anexo — Registro del discovery (YYYY-MM-DD)" con solo lo de valor durable.
=====================================================================================
-->

## 🔍 Discovery en curso — sesión iniciada YYYY-MM-DD

### 🅿️ Estacionamiento de la solución — congelado hasta la Fase 3

> Lo que el PM trajo ya resuelto. No se discute hasta el Gate 2. En la Fase 3 cada ítem se ubica en un carril.

| # | Lo que trajo el PM | Textual | Tipo | Carril (Fase 3) | Veredicto (Gate 4) |
|---|---|---|---|---|---|
| S1 | <resumen> | "<cita textual>" | Feature UI / API / Proceso / Proveedor / Arquitectura / Dato | ⬜ | ⬜ Congelado |

### Contexto leído del Cerebro

<!-- Módulos barridos (1.a–1.d), hechos duros con número y cita, qué se descartó con motivo. -->

### Ronda 1 — Problema (YYYY-MM-DD)

```
❓ **Q1** - **<título>**: <cuerpo>

➡️ <respuesta recomendada>
```

<Respuesta real del PM.>

### Tabla de magnitudes y nivel de evidencia

| Magnitud | Valor o rango | Cómo se obtuvo (cita) | Nivel | Evidencia que lo validaría | ¿El PM lo valida? |
|---|---|---|---|---|---|
| Medida | | cálculo / analogía / supuesto | ✅ / 🔶 / ⚪ | | Sí — pedido / No — queda incertidumbre |
| Impacto | | | | | |

### Tabla de evidencia — ¿vale la pena? (Gate 2)

| Dimensión | Qué dice el Cerebro (con cita) | Nivel | Veredicto |
|---|---|---|---|
| Encaje NSM | | | |
| Encaje en foco/KR | | | |
| Tamaño real | | | <"a la baja por falta de evidencia" si ⚪/🔶> |
| Costo de oportunidad (provisorio) | | | |
| Demanda repetida | | | |
| Generalización (¿a quién más le sirve?) | | | |
| Riesgo de no hacerlo | | | |
| Solapamiento | | | |

### Frontera del foco (Gate 2)

| Dentro | Fuera | Por qué |
|---|---|---|

### 🧺 Fuera de foco

<!-- Lo que apareció después del Gate 2 y cae fuera de la frontera. Solo entra al alcance si el PM reabre el Gate 2. -->

### Abanico de soluciones (Gate 3)

| # | Carril | Alternativa | Cubre | Tamaño + analogía | Nivel | Tiempo a valor | Quién |
|---|---|---|---|---|---|---|---|
| A0 | 0 · No hacer nada | | | | | | |
| A1 | 1 · Operativa | | | | | | |
| A2 | 2 · Acotada | | | | | | |
| A3 | 3 · Amplia | | | | | | |

### Preguntas para el análisis funcional-técnico

<!-- Dudas técnicas que no hacen falta para elegir — viajan al -start.md §7 y a /idea_solution. -->

### Recomendación del Cerebro (Gate 4)

<!-- Recomendación, defensa completa, sensibilidad a la evidencia, decisión literal del PM. -->
