---
name: idea_risks
description: Releva, clasifica y registra los riesgos de un proyecto en dos familias — los de entrega del proyecto (dependencias, proveedores, alcance, capacidad) y los del producto una vez en producción (fraude, operativo, regulatorio, financiero, reclamos) — con probabilidad, impacto, mitigación y dueño. Toma como insumo lo que quedó sin resolver en la revisión cruzada por área y en el análisis de solución, y mantiene al día el riesgos.md del proyecto. Se activa con /idea_risks.
when_to_use: Se activa cuando el usuario ejecuta /idea_risks, después de /idea_crosscheck (`-crosscheck.md` en `Aprobado por PM`) y antes de /idea_prd — el PRD consolida este relevamiento, no lo rehace.
disable-model-invocation: true
argument-hint: "[nombre_corto_proyecto o PRD-XXX]"
---

# ⚠️ RELEVAMIENTO DE RIESGOS: /idea_risks

## Por qué existe esta skill

El Assessment de auditoría del banco posterior al fraude de Transferencias Pull encontró, textual, la "ausencia de evaluación de riesgos previa al lanzamiento de un nuevo producto y técnica". Ese marco hoy vive del lado de Riesgos, sin una instancia donde Producto aporte lo que solo Producto sabe: qué superficie de fraude abre una funcionalidad, a qué tipo de cliente y con qué volumen, qué pasa cuando falla a mitad de camino.

Hasta ahora los riesgos eran una tabla al final del PRD, casi siempre de entrega (se atrasa el proveedor, crece el alcance). Esta skill los releva como paso propio, con dos familias que se evalúan siempre:

- **A — Riesgos de entrega del proyecto:** lo que puede impedir que se construya bien, a tiempo o con el alcance acordado.
- **B — Riesgos del producto en producción:** lo que puede salir mal una vez que esté andando, aunque se haya construido perfecto. Esta familia es el aporte de Producto a la evaluación previa al lanzamiento que pidió la auditoría.

## Cuándo NO usarla

- La revisión cruzada por área todavía no está aprobada → [`/idea_crosscheck`](../idea_crosscheck/SKILL.md) primero. Esta skill toma sus filas `Pendiente` y sus contingencias sin dueño como insumo directo; no las vuelve a descubrir.
- Lo que hace falta es cerrar los riesgos de un proyecto que ya salió a producción → eso es [`/idea_finish`](../idea_finish/SKILL.md), que tiene su propio gate sobre `riesgos.md`.
- Es un riesgo general de la empresa, sin proyecto → item `tipo: riesgo` en `contexto_vivo/`, no esta skill.

## ⚖️ Reglas duras

1. **Gate de entrada.** `-crosscheck.md` tiene que estar en `Aprobado por PM`. Si está en `Propuesta`, pará y ofrecé revisarlo y aprobarlo ahora o volver a `/idea_crosscheck`. Nunca se relevan riesgos sobre una revisión cruzada sin cerrar.
2. **Todo riesgo lleva familia, probabilidad, impacto, mitigación y dueño de la mitigación.** Probabilidad Baja/Media/Alta; impacto Bajo/Medio/Alto; el dueño es una persona o un área, nunca "el equipo". Si todavía no hay mitigación clara, se dice explícito ("Sin mitigación definida — <qué haría falta para tenerla>") — nunca una mitigación de relleno para que la fila quede completa.
3. **Nada se pierde entre skills.** Se traduce en un riesgo (o se justifica en una línea por qué no lo es):
   - toda fila `Pendiente` del crosscheck;
   - toda contingencia operativa del crosscheck sin dueño claro;
   - todo gap técnico bloqueante sin resolver de la Sección 12 del `-solution.md`;
   - todo riesgo de la alternativa elegida que ya dejó registrado el shaping.
4. **Las dos familias se evalúan siempre.** La familia B recorre su catálogo completo (Paso 2), pregunta por pregunta. Si una pregunta no aplica, se dice con el motivo — nunca se omite en silencio.
5. **`riesgos.md` es el registro vivo del proyecto; el `-risks.md` es la foto aprobada.** `/idea_start` ya escribe en `riesgos.md` los riesgos de la alternativa elegida. Esta skill los lee, los actualiza y suma los nuevos — nunca crea una segunda lista paralela. Para actualizar una entrada existente se agrega debajo, con fecha, nunca se reescribe el texto original (mismo formato que usan `/gaps` e `/idea_finish`). Un riesgo que cruza varios slices de un proyecto general va al `riesgos.md` del padre.
6. **Riesgo B alto = candidato a bloqueador de go-live.** Todo riesgo de familia B con probabilidad **o** impacto Alto se marca `🚧 Bloqueador de go-live` salvo que el PM diga explícitamente lo contrario (y se registra su motivo). `/idea_golive` los levanta como bloqueadores.
7. **Los hechos los busca Claude; las decisiones son del PM.** La probabilidad y el impacto se proponen con su razonamiento (y con número si existe: volumen, monto, cantidad de clientes). El PM los confirma o corrige.
8. **Todo queda en `Propuesta` hasta el OK literal del PM** (Paso 4).
9. **El documento es autocontenido** — sin links a la wiki, sin nombres de archivo o de skill, sin jerga interna. El origen de cada riesgo se describe por su naturaleza ("surgió de la revisión con Fraude"), no por el nombre del artefacto.
10. Todo output en español.

## 🏃 Pipeline

### Paso 0 — Contexto y gate de entrada

1. Resolvé la ruta real en [`wiki/1_proyectos/index.md`](../../../wiki/1_proyectos/index.md) §2.
2. **Gate de entrada (regla dura 1):** frontmatter de `artefactos/{{nombre_corto_proyecto}}-crosscheck.md`. En carpetas legacy sin `estado`, preguntale al PM una sola vez si lo da por aprobado y registralo.
3. Leé completos:
   - `-crosscheck.md` — filas `Pendiente`, contingencias, requerimientos nuevos.
   - `riesgos.md` del proyecto (y del padre si es miembro) — lo ya registrado, incluido lo que dejó el shaping.
   - `-start.md` — riesgos y dependencias de la alternativa elegida, incertidumbres ⚪/🔶 no validadas.
   - `-solution.md` — Sección 8 (errores y fallas de proveedores), 10 (convivencia), 11 (decisiones y NFR), 12 (gaps técnicos).
   - `proyecto.md`, `decisiones.md`, `gaps.md`.
4. Contexto general: `wiki/2_areas/riesgos.md` (riesgos de la empresa que tocan este producto — ej. dependencia de proveedores, control del ledger), `wiki/3_recursos/arquitectura_sistema/` si hay proveedor externo, `wiki/3_recursos/cumplimiento_normativo/` si hay riesgo regulatorio, `wiki/1_proyectos/contexto_vivo/index.md` citando como no-canon.
5. **Si ya existe `artefactos/{{nombre_corto_proyecto}}-risks.md`**, leelo completo: esta corrida lo actualiza in place.
6. **Detección de desfasaje:** si el `-risks.md` existente está aprobado pero su `basado_en` apunta a versiones anteriores del `-crosscheck.md` o del `-solution.md`, decile al PM qué cambió y revisá solo los riesgos afectados.

### Paso 1 — Barrido de fuentes (familia A y lo que ya viene de arriba)

Armá la lista de candidatos desde las fuentes de la regla dura 3, más:
- dependencias de proveedores externos (lead time, sandbox inexistente, cambios de contrato);
- dependencias con otros equipos o con otros slices del mismo proyecto general;
- alcance: requerimientos nuevos que sumó el crosscheck, frontera del foco con presión de ampliarse;
- capacidad: lo que el shaping dijo que se desplaza, fricción del gate de CI/CD si toca código crítico (ledger, antifraude, aprobación/rechazo de operaciones);
- incertidumbres del shaping que el PM eligió no validar.

### Paso 2 — Familia B: el producto en producción

Recorré este catálogo completo, una respuesta por pregunta (riesgo identificado, o "sin riesgo" / "no aplica" con el motivo):

- **B1 — Fraude:** ¿qué uso indebido nuevo habilita (suplantación, triangulación, abuso de un límite, un circuito sin control)? ¿Quién lo detectaría y cuánto dinero puede moverse antes de que alguien lo vea?
- **B2 — Operativo:** si deja de funcionar, ¿quién se entera y en cuánto tiempo? ¿Qué queda a medias (una operación iniciada y no terminada, un estado intermedio)? ¿Hay forma de revertir?
- **B3 — Financiero:** ¿qué impacto tiene en saldos, liquidaciones o conciliación si falla a mitad de camino o se duplica? ¿Quién pone la plata si hay un descuadre?
- **B4 — Regulatorio:** si falla o se usa mal, ¿qué obligación incumple Bind (BCRA, UIF/PLD, PCI DSS, datos personales)? ¿Hay plazo de reporte?
- **B5 — Reclamos y reputación:** ¿qué reclamo genera si falla, y de quién (comercio, usuario final, otra entidad)? ¿Puede escalar a BCRA o Defensa del Consumidor?
- **B6 — Dependencia de tercero en producción:** si el proveedor externo falla o cambia algo sin aviso, ¿qué se rompe para el cliente y qué control tiene Bind?

Ampliá el catálogo si el proyecto lo pide; no lo podes.

### Paso 3 — Clasificación

Por cada riesgo: familia, probabilidad, impacto, mitigación, dueño, y estado (`Abierto` / `Mitigado` / `Aceptado` por el PM — con motivo). Proponé los valores con su razonamiento; aplicá la regla dura 6 a los de familia B.

### Paso 4 — Revisión iterativa con el PM

**No se da por cerrado en la primera pasada.** Presentá la tabla completa, destacando los `🚧 Bloqueador de go-live` y los riesgos sin mitigación definida. Si el PM corrige algo, reescribí la fila limpia y sumá una entrada al historial. Si el PM **acepta** un riesgo sin mitigarlo, es una decisión suya: se registra con su motivo en la fila y en `decisiones.md`.

Recién con su confirmación literal el artefacto pasa a `Aprobado por PM (YYYY-MM-DD)`. Ni el silencio ni "dale, seguí" cuentan como aprobación.

## 📄 Formato de salida

Usá [`references/TEMPLATE.md`](references/TEMPLATE.md): frontmatter con `estado` y `basado_en`, **Resumen para el PRD** al tope, tabla de familia A, tabla de familia B, respuestas del catálogo B sin riesgo, historial de revisiones.

Ver [`references/EXAMPLE.md`](references/EXAMPLE.md) para un ejemplo completo (cifras ilustrativas).

## ✅ Checklist de calidad

- [ ] `-crosscheck.md` estaba en `Aprobado por PM` antes de empezar
- [ ] Toda fila `Pendiente`, toda contingencia sin dueño, todo gap técnico bloqueante y todo riesgo del shaping quedó traducido en un riesgo o justificado en una línea
- [ ] Las seis preguntas de la familia B tienen respuesta — ninguna omitida
- [ ] Todo riesgo tiene familia, probabilidad, impacto, mitigación (o "sin mitigación definida" explícito) y dueño
- [ ] Todo riesgo B con probabilidad o impacto Alto está marcado como bloqueador de go-live, o tiene el motivo del PM para no hacerlo
- [ ] Todo riesgo aceptado sin mitigar tiene la decisión del PM registrada
- [ ] `riesgos.md` quedó actualizado sin duplicar entradas ni reescribir texto previo
- [ ] El documento es autocontenido
- [ ] El PM dio su OK literal y el frontmatter dice `Aprobado por PM (YYYY-MM-DD)`, o quedó explícito en `Propuesta`

## Paso 5 — Cierre estándar

1. **Persistir** en `artefactos/{{nombre_corto_proyecto}}-risks.md`, con `version`, `estado` y `basado_en` (versiones del `-crosscheck.md` y del `-solution.md`). Si ya existía, se reescribe limpio con entrada en el historial; si estaba aprobado y cambió el cuerpo, vuelve a `Propuesta` hasta la re-aprobación.
2. **`riesgos.md` del proyecto** (regla dura 5) — nace si no existe. Formato por entrada: `## [YYYY-MM-DD] — <título>` con `**Familia:**`, `**Probabilidad:**`, `**Impacto:**`, `**Mitigación:**`, `**Dueño:**`, `**Estado:**`, `**Bloqueador de go-live:** Sí/No`.
3. **Riesgos aceptados por el PM** → `decisiones.md` del proyecto.
4. **Mitigaciones que son una acción concreta del PM** (conseguir una confirmación, coordinar un tablero con Fraude) → `wiki/1_proyectos/tareas.md` como `T-NNN`, dedupe primero.
5. **Riesgo general de la empresa** que surja y exceda este proyecto → item `tipo: riesgo` en `contexto_vivo/` con `destino_propuesto: 2_areas/riesgos.md`.
6. **`proyecto.md` §4 Entrega** → fila del `-risks.md` en la tabla "Cadena de artefactos". Nota en §8.
7. **Índices:** `wiki/1_proyectos/index.md` §2. Sin changelog y sin git.
8. Siguiente paso sugerido: [`/idea_prd`](../idea_prd/SKILL.md) — consolida el shaping, la solución, la revisión cruzada y este relevamiento en el documento final.
