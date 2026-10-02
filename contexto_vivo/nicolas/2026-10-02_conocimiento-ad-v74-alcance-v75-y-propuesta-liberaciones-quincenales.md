---
id: 2026-10-02_conocimiento-ad-v74-alcance-v75-y-propuesta-liberaciones-quincenales
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Reunión \"Análisis COBRO\" (2026-10-01), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: adquirencia
tema: Cierre del alcance de AD V74, arranque de la planificación de V75 y propuesta de liberaciones quincenales para no saturar QA
tipo: conocimiento
destino_propuesto: 2_areas/procesos/publicaciones_mensuales.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Propuesta: liberaciones quincenales (no aprobada todavía).** En "Análisis COBRO" del 2026-10-01 se propuso liberar cada quince días en vez de cada mes, para que el equipo de pruebas no se sature. La minuta lo deja como **propuesta**, sin decisión. Si se aprueba, cambia la cadencia que describe `publicaciones_mensuales.md`. No hay que registrarla como regla hasta que alguien la confirme.

**Alcance de V74.** Matías Alzogaray y Andrea Orsini cuentan los tickets del tablero el 2026-10-01 por la tarde para cerrar el alcance. El cierre es en una reunión el 2026-10-02 por la mañana. Matías arma además el plan de lanzamiento de la versión.

**Ticket 1738.** Se le cambia la etiqueta para que entre en V74. La minuta no dice de qué tablero es: puede ser AD-1738, o WS-1738, que es la Epic de PRD-259 (`inter_trazabilidad_ccl`, hoy en discovery). Que esa Epic entre en una versión de Adquirencia sería raro, así que lo más probable es AD-1738. **Confirmado en Jira (2026-10-02):** es [AD-1738](https://bindpsp.atlassian.net/browse/AD-1738) ("[OBS] [Portal Pagos FX] Alta Beneficiario, formulario de datos: En fecha de expiración del DNI permite ingresar texto"), que tiene fixVersion **AD 74** (estado "No aplica" al momento de la consulta). WS-1738 no tiene versión asignada y sigue en Backlog.

**V75.** Alguien del equipo (en la minuta, "alguien en 7D, Plaza San Martín") empieza a planificar los contenidos de V75 y a analizar qué tareas requieren pruebas y qué tan complejas son.

**Pagos QR.** Se mencionó bajar la cantidad de pasos de las transacciones QR para que respondan más rápido. No queda claro si es parte de PRD-199 (`bajar-tiempos-pagos-qr`) o un cambio aparte.

> Fuente: Reunión "Análisis COBRO" (2026-10-01), resumen del mail de Gemini.
