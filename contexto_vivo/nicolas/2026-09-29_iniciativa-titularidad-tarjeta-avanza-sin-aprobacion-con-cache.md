---
id: 2026-09-29_iniciativa-titularidad-tarjeta-avanza-sin-aprobacion-con-cache
pm: nicolas
fecha_captura: 2026-09-29
fuente: "Charla directa con el PM (Nicolás Colón) sobre titularidad_tarjeta (PRD-25), 2026-09-29"
producto: Adquirencia (Botón Simple)
tema: Validación de titularidad de tarjeta — avanza sin esperar aprobación y suma la caché al alcance
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
proyecto: titularidad_tarjeta
---

El PM decidió que el proyecto de validación de titularidad de tarjeta en Botón Simple (PRD-25) avance sin esperar la aprobación de Emma Vignoles (COO, sponsor), porque la espera retrasaba el proyecto. Deja atrás la etapa de aprobación y pasa a planificación de lanzamiento y desarrollo. En Jira, la IDEA sigue en EN APROBACION hasta que el PM la mueva.

En la misma decisión, la caché de validaciones deja de ser opcional y entra en el alcance de esta iteración. Es el mecanismo que evita volver a consultar a MODO una combinación de tarjeta y DNI ya validada. El PM la considera muy provechosa, y según Pablo Gomes a Emma le va a gustar, aunque no pasó por su aprobación. AD-1817 pasa de Low a Medium.

La estimación total del proyecto queda en 10 SP (rango 10–22): 7 SP de la validación con MODO (AD-1815) más 3 SP de la caché (AD-1817). Ya está cargada en Jira.

También quedó confirmado que el llamado a Ardid es síncrono en Botón Simple 1.0 y 2.0, que es lo que sostiene el diseño de retener los datos de la tarjeta en memoria.

Como condiciones del go-live siguen pendientes el contrato con MODO (Legales) y la aprobación del costo operativo proyectado, de unos USD 656.000 por año antes del ahorro de la caché.
