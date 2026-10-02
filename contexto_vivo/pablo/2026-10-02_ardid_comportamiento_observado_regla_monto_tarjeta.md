---
id: 2026-10-02_ardid_comportamiento_observado_regla_monto_tarjeta
pm: pablo
fecha_captura: 2026-10-02
fuente: "análisis propio de las transacciones con tarjeta de julio a octubre (1.821.393 filas, 01/07–02/10 14:41, POS y checkout) aportadas por el PM en rechazos_bines_payway (PRD-251)"
producto: ardid
tema: Ardid empezó a rechazar por monto el 01/09 a las 07hs en checkout, con un tope de $500 mil que pasó a $1,2 M el 15/09 y se aflojó el 23/09
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/modulo_pagos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

## Qué se observó

En el cobro con tarjeta del checkout, el rechazo "Rechazada por Ardid (1001)" sumó 83.756 rechazos entre julio y el 02/10 (23,7% de todos los rechazos, ARS 35.406 M, 37,9% del monto rechazado). Casi no ocurre en POS (0 casos). Su comportamiento cambia de forma abrupta en septiembre y es consistente con una regla de monto por transacción:

- **Julio y agosto:** Ardid no distinguía por monto; rechazaba entre 2% y 3% de las transacciones en todos los tramos de importe.
- **Desde el 01/09 a las 07hs:** en checkout rechaza entre 90% y 99% de las transacciones de $500 mil a $1,2 M y de 96% a 99% de las de más de $1,2 M; por debajo de $500 mil, ~4–6%. El 31/08 el tramo $500 mil a $1,2 M rechazaba 3%; el 01/09 sube a 70% a las 07hs, 84% a las 08hs y 90% o más desde las 09hs. Tope práctico: $500 mil.
- **Desde el 15/09:** el tramo $500 mil a $1,2 M baja a 1–14% por día, mientras que por encima de $1,2 M sigue en 95–100%. El tope pasó a $1,2 M.
- **Desde el 23/09:** también se afloja por encima de $1,2 M (59% el 23/09, 25% el 24/09, 7% el 25/09, 3% el 26/09) y queda un residuo de 18–29% por día entre el 27/09 y el 02/10.
- **Peso:** en septiembre Ardid explica el 40,0% de los rechazos y el 68,9% del monto rechazado (ARS 31.927 M de ARS 46.367 M). Con importes desde $500 mil, 28.216 rechazos por ARS 27.333 M, el 59% del monto rechazado del mes. En el mismo período "Tarjeta denegada (5)" (rechazo del emisor) baja de ~6% a ~3% de las transacciones, porque Ardid corta antes los importes altos.
- Hay además BINs donde Ardid rechaza una fracción alta de sus transacciones (por ejemplo 483188, 417309, 423001, 517230, 433810, 555889), consistente con una regla por grupo de BIN.

## Límites

La existencia de una regla de monto, su umbral y las fechas de cambio son una inferencia a partir de los datos, no un hecho confirmado por Fraude/Ardid (tarea T-163 del proyecto). El módulo de pagos de Ardid sí documenta reglas por tarjeta parametrizables (monto acumulado diario y mensual, frecuencia, grupos de BIN y de comercio), consistentes con lo observado. Detalle y gráficos en el reporte HTML de `1_proyectos/rechazos_bines_payway/artefactos/` (sección 8).
