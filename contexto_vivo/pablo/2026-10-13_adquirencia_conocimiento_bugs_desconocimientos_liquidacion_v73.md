---
id: 2026-10-13_adquirencia_conocimiento_bugs_desconocimientos_liquidacion_v73
pm: pablo
fecha_captura: 2026-10-13
fuente: "/sync_mails — hilo 'Re: Minuta: Análisis de riesgo: AD V 73' (threadId 1a0b604212500a77), Mariana Vila (Bind), 2026-10-13"
producto: adquirencia
tema: Bugs detectados en la separación de desconocimientos (contracargos) de devoluciones en liquidaciones, validando la V73 ya en producción
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/desconocimientos_de_tarjeta.md
tipo_destino: actualizar
contradice: "wiki/3_recursos/detalle_productos/adquirencia/desconocimientos_de_tarjeta.md — no contradice el diseño ya documentado (separación de desconocimientos/devoluciones confirmada para AD V73), pero reporta 2 defectos concretos de implementación encontrados al validar datos reales en producción, que ese archivo no registra todavía"
confianza: alta
estado: en_cola
merge_commit:
---

Mariana Vila (Bind) reporta, revisando los desconocimientos en los PDF y en las liquidaciones ya en producción (post-deploy V73), dos errores concretos:

**A) Contracargos de "trx desconocida" con antigüedad >90 días:** al insertarlos (probado vía jmeter), el endpoint da error — no cambia el estado de la transacción, no notifica a la entidad, y tampoco se inserta el registro en la tabla `Trx Contracargo Tipo desconocimiento`. Es decir, un desconocimiento de una transacción de más de 90 días queda completamente perdido (ni error visible al usuario del endpoint, ni rastro en BD).

**B) Inconsistencia en la tabla de Liquidación y en los archivos/PDF, según cuándo ocurre el desconocimiento respecto de la liquidación:**

- *Si se desconoce/devuelve **antes** de liquidarse la transacción:* se informa correctamente en el PDF y en el archivo de liquidación a la entidad. Pero en la tabla `Liquidacion` existe una diferencia entre `TotalLiquidacion` y `TotalALiquidar` que corresponde exactamente al monto de los desconocimientos — esa diferencia no se refleja en el campo `TotalDevoluciones` ni en ningún otro campo de la tabla (queda "flotando", sin explicación visible).
- *Si se desconoce/devuelve **después** de liquidada:* no se informa ni en el PDF ni en la tabla de liquidación del día. En el archivo de liquidación a la entidad se informa, pero asociado a un `IdLiquidación` **anterior**, no al de la liquidación del día en que se procesa el desconocimiento.
  - **Lo que estaba definido** para este caso: el día hábil siguiente a desconocerse la transacción ya liquidada, se informa (1) el contracargo (`{{idTransaccion}}004/003/002`) en el archivo BOTONLIQ, (2) el contracargo en el PDF de esa liquidación, y (3) se resta el contracargo del registro de la Liquidación.
  - **Lo que no se pudo explicar:** Mariana no logró identificar la lógica real con la que el sistema inserta el desconocimiento en la liquidación — ejemplo concreto: un desconocimiento se insertó el 30/09 pero recién se informó en el archivo BOTONLIQ el 08/10 (9 días de diferencia, sin que el "día hábil siguiente" definido explique ese desfasaje).

Se adjuntaron a este mail (no procesados por esta skill) varios PDFs de liquidación reales (`20260914_Liquidacion_C16593_403288.pdf`, `20260915_...`, `20260916_...`, `20261009_Liquidacion_C16590_406167.pdf`), 3 ZIPs de archivos BOTONLIQ (`A132BOTONLIQ081026.zip`, `A132BOTONLIQ091026.zip`, `A132BOTONLIQ131026.zip`) y un Excel de control (`Control 13.10.26 vAD 1.73 - BD TRANSACCIONAL.xlsx`) — quedan como evidencia sin leer automáticamente, pendientes si se necesita el detalle fila por fila.

Este hallazgo es el seguimiento directo de la minuta "Análisis de riesgo: AD V 73" (17/09/2026), donde ya se había decidido la separación de desconocimientos/devoluciones por código en los reportes (AD-1398/DAD-2257) — ahora, un mes después del pase a producción (28/09) y con el circuito ya operando, aparecen estos 2 defectos concretos de esa implementación. Sin respuesta del resto del equipo (Matías Alzogaray y co.) al cierre de esta corrida.

> Fuente: hilo "Re: Minuta: Análisis de riesgo: AD V 73: Jue, 17 de sept de 2026" (threadId `1a0b604212500a77`), mensaje de Mariana Vila (Bind) del 13/10/2026 21:47.
