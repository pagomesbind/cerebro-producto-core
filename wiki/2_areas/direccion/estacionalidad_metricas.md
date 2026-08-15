# Calendario de estacionalidad — métricas semanales (NSM)

> Conocimiento de negocio, no cálculo estadístico. `/sync_metrics` (`pipeline.py`) mide en agregados
> **semanales** — no tiene grano diario, así que no puede saber por sí solo si una caída de volumen
> coincide con un feriado o si un salto es el pico habitual de cobro de servicios de principio de mes.
> Estos patrones viven acá para que, al escribir los hallazgos de cada corrida (Paso 3 de
> [`/sync_metrics`](../../../.claude/skills/sync_metrics/SKILL.md)), se puedan citar como explicación conocida
> en vez de registrarlos como movimiento sin explicar en `../gaps_y_preguntas.md`.
>
> **Regla de uso:** un patrón de acá solo se cita si la semana en cuestión efectivamente cae dentro de su
> ventana (ej. no asumas "está cerca de fin de mes" sin mirar el rango real de la semana). Si una semana
> se mueve fuerte y **no** cae en ninguna ventana de este calendario, sigue yendo a `../gaps_y_preguntas.md`
> como siempre — este archivo reduce falsos gaps, no reemplaza el criterio.

## Confirmado por el usuario (2026-08-04)

### 1 · Primera quincena del mes (días 1 al 10) — pico de cobro de servicios y facturas

**Aplica fuerte a NSM#2 (Adquirencia/Payway — "Cobro").** Muchos comercios de la cartera de Cobro se dedican
específicamente a cobro de servicios, y sus vencimientos concentran en esa ventana — es la explicación
esperable de un salto de volumen (o de una caída si la semana anterior fue la de esa ventana y ésta no).

**Aplica más débil e inconsistente a NSM#1 (Wallet).** El uso de Wallet es diverso (incluye retail y otros
rubros sin esta estacionalidad), así que el mismo patrón **no se puede asumir automáticamente** para
Operaciones/Wallet — si se observa, hay que verificarlo caso a caso, no darlo por sentado como con NSM#2.

**Cómo aplicarlo:** si la `FechaInicioCorte` o `FechaFinCorte` de la semana analizada cae total o
parcialmente entre el día 1 y el día 10 del mes calendario, un salto o sostenimiento alto de NSM#2 (o de
sus palancas — Botón Simple/2.0, medios de pago) tiene esta explicación disponible. Si la semana previa
era la de la ventana 1-10 y la actual ya salió de ella, una caída de NSM#2 vs. esa semana también puede
explicarse por acá — no es necesariamente un problema de negocio.

### 2 · Feriados nacionales de Argentina — caída esperable de volumen transaccional general

Un feriado nacional (o el fin de semana largo que genera) es una explicación válida para una caída de
volumen esa semana, en cualquiera de las dos NSM — menos días hábiles, menos operaciones. **El calendario
de feriados cambia año a año** (fechas trasladables, feriados con fines de turismo) — antes de citar este
patrón en un hallazgo, verificar el calendario oficial vigente para el año en curso (no asumir fechas fijas
de memoria) y confirmar cuántos días hábiles tuvo la semana en cuestión.

### 3 · Fechas comerciales/marketineras (Hot Sale, Cyber Monday, etc.)

Relevante como explicación de picos de volumen en NSM#2 (cobro con tarjeta) — estas fechas concentran
consumo en plazos cortos. **Las fechas exactas cambian año a año** y las anuncia la Cámara Argentina de
Comercio Electrónico (CACE) con poca anticipación — no hay una fecha fija para hardcodear acá. Cuando el
usuario confirme la fecha de una edición concreta (ej. "Hot Sale 2026 fue del X al Y"), registrarla como
una entrada nueva de este archivo con el volumen observado, para tener referencia el año siguiente.

## Pendiente de confirmar

- Fecha o rango específico de pago de sueldos más allá de "días 1 al 10" (ya cubierto por el patrón 1) —
  no se identificó un patrón adicional y distinto de altas de Transferencia Entrante o Pago con QR ligado
  puntualmente al día de cobro de sueldo (distinto del pico de servicios).
- Estacionalidad específica de NSM#1/Wallet, más allá de "más débil e inconsistente que NSM#2" — cuando el
  usuario identifique un patrón concreto por producto/rubro dentro de Wallet, sumarlo acá.

## Historial de revisiones

- **2026-08-04** — creación. Patrones 1-3 confirmados por el usuario en la corrida de `/sync_metrics` de
  la semana 202631, a raíz de una pregunta sobre por qué el reporte no explicaba movimientos estacionales
  conocidos del negocio.
