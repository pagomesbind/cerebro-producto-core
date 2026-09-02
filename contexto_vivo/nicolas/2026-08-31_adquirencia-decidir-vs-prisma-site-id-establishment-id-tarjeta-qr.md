---
id: 2026-08-31_adquirencia-decidir-vs-prisma-site-id-establishment-id-tarjeta-qr
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"Análisis COBRO\" (2026-08-27)"
producto: adquirencia
tema: Diferencias de parametrización entre los procesadores Decidir (no presencial) y Prisma (presencial) para la integración de tarjeta QR — continuación del análisis de Daniela Collia (Fintexa)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/pos_multiadquirencia.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 7fd6e3f
---

En la reunión "Análisis COBRO" (2026-08-27, con Daniela Collia/Fintexa, Pablo Gomes, Nicolás Colón y equipo Fintexa) se retomó el análisis del desarrollo de tarjeta QR priorizado para la versión de septiembre (ver tarea T-010 en `tareas.md`, 2026-08-25). Daniela Collia planteó que Decidir se usa para ventas no presenciales y Prisma para presenciales, y que ambos procesadores piden datos distintos:

- **Decidir**: solo requiere un identificador de sitio (*site ID*), descrito como un agrupador de establecimientos. En producción se usa habitualmente el código `00130250`, que agrupa establecimientos por marca de tarjeta — pero ese valor no figura en la tabla de reglas de negocio de Prisma (`Business Rules`, con processor ID 2003) que el equipo venía analizando.
- **Prisma**: requiere múltiples parámetros detallados — terminal y establecimiento (identificador de establecimiento e identificador de terminal, exigidos por Mode).

Al revisar el panel de administración (`configuración procesador`), se confirmó que la configuración actual para el canal presente con Payway tiene esa misma asimetría: Prisma pide terminal+establecimiento, Decidir opera principalmente con site ID + un terminal configurado como código de comercio. Como hipótesis sin confirmar: el site ID actuaría como nivel de agrupación de establecimientos (ejemplo: el rubro/MCC 5541 tiene un único comercio, mientras que el 4813 agrupa varios — 691 y 992).

Quedó pendiente para Nicolás Colón: unirse a la sesión de integración de Decidir para resolver las dudas, definir la configuración exacta (site ID / establishment ID) y contactar a Gono (Gonzalo Rivera) para la información técnica que destrabe el desarrollo — ver tarea T-010 actualizada en `tareas.md`.
