---
id: 2026-10-14_conocimiento-adquirencia-desconocimientos-post-v73-defectos-liquidacion
pm: nicolas
fecha_captura: 2026-10-14
fuente: "Mail \"Re: Minuta: Análisis de riesgo: AD V 73\" (Euge Vila, 2026-10-13)"
producto: adquirencia
tema: Desconocimientos después de V73 — el endpoint falla con transacciones de más de 90 días, la tabla Liquidación no refleja los desconocimientos y los posteriores a la liquidación salen con un IdLiquidación anterior
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/desconocimientos_de_tarjeta.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Contexto.** V73 (pase del 29/09) separó los desconocimientos (contracargos) de las devoluciones en los archivos de liquidación y en los PDF, con códigos distintos (AD-1398 / DAD-2257). Después del pase, Euge Vila (Bind) revisó los desconocimientos en los PDF y en las liquidaciones y encontró errores.

**Defectos reportados (13/10):**
- **(A) Transacción de más de 90 días.** Si un contracargo cargado por JMeter apunta a una transacción de más de 90 días, el endpoint da error, el estado no cambia y no se avisa a la entidad. Tampoco queda registro en la BD transaccional (tabla Contracargo, tipo desconocimiento) con el error.
- **(B1) Desconocimiento o devolución antes de liquidar.** El PDF y el archivo de liquidación a la entidad salen bien. El error está en la tabla **Liquidación**: la diferencia entre `TotalLiquidacion` y `TotalALiquidar`, que corresponde a desconocimientos, no aparece en `TotalDevoluciones` ni en ningún otro campo.
- **(B2) Desconocimiento después de liquidar.** No aparece ni en el PDF ni en la tabla Liquidación. En el archivo a la entidad sale con un **IdLiquidación anterior**, no asociado a la liquidación del día. Ejemplo: se insertó el 30/09 y salió en BOTONLIQ el 08/10, sin una lógica identificable.

**Lo que se había definido para (B2), según el mail:** desconocida una transacción ya liquidada, el día hábil siguiente se informa:
- el contracargo (`{idTransaccion}004/003/002`) en el archivo BOTONLIQ;
- el contracargo en el PDF de la liquidación;
- y se resta el contracargo en el registro de la Liquidación.

**Relación con las versiones:** (B1) y (B2) parecen caer en AD-1837 / DAD-3425 ("desconocimientos no registrados ni separados en la liquidación") y AD-1791 / DAD-3400 ("total a liquidar con devoluciones y desconocimiento en la misma liquidación"). Los dos pasaron a **V75** con todo liquidaciones (reunión "Cerramos alcance AD", 13/10). (A) no tiene un ticket visible en el alcance. Hay que validarlo en T-130, y por eso la confianza es media.

**Evidencia sin descargar:** 4 PDF de liquidación (C16593 del 14, 15 y 16/09; C16590 del 09/10), 3 zip BOTONLIQ (08, 09 y 13/10) y `Control 13.10.26 vAD 1.73 - BD TRANSACCIONAL.xlsx`.

> Fuente: Mail "Re: Minuta: Análisis de riesgo: AD V 73" — Euge Vila (2026-10-13), a Matías Alzogaray, con copia a Fintexa y a los 3 PM.
