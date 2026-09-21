---
id: 2026-09-18_direccion_gap_scope_nsm2_pos_ya_shippeo
pm: pablo
fecha_captura: 2026-09-18
fuente: "/idea_prd (PRD-70, POS con PRISMA) — barrido directo de la Epic AD-430 en Jira, contrastado contra wiki/2_areas/direccion/north_star.md §2"
producto: "contexto fijo"
tema: scope de la métrica de volumen por gateway (NSM #2) no incluye el canal POS pese a que ya se shippeó en su mayor parte
tipo: gap
destino_propuesto: 2_areas/direccion/north_star.md
tipo_destino: actualizar
contradice: "2_areas/direccion/north_star.md §2 — nota del 2026-07-21 que dice 'El POS presente (MPOS) todavía NO pasa por Payway: ese proyecto no se shippeó', usada para excluir el canal POS del scope de medición de la métrica de volumen operado por el gateway Payway/Decidir/Prisma"
confianza: alta
estado: ingestado
merge_commit:
---

## Gap: el scope de medición de la métrica de volumen por gateway no refleja que el POS ya se shippeó en su mayor parte

`north_star.md` §2 registra, con fecha 2026-07-21, que el canal POS presencial (MPOS) queda fuera del scope de medición de la métrica de volumen operado por el gateway Payway/Decidir/Prisma porque "ese proyecto no se shippeó" — refiriéndose al proyecto de habilitar Prisma como segundo procesador de POS desde el Admin (PRD-70, Epic Jira AD-430).

Un barrido directo de esa Epic en Jira (2026-09-18, al rehacer el PRD-70 con las reglas vigentes) confirma que la nota quedó desactualizada:

- La configuración por defecto a nivel Entidad, la habilitación a nivel Comercio y el flujo de cobro adaptado están en Producción desde el **2026-06-24**.
- La jerarquía de reglas de pago Comercio/Entidad está en Producción desde el **2026-08-03**.
- La devolución con el procesador original y la posibilidad de operar un comercio exclusivamente con Prisma ("solo Prisma", capacidad que en el momento de escribir la nota de north_star.md ni siquiera estaba priorizada) están en Producción desde el **2026-08-31**, con cierre formal el 2026-09-08.

Es decir: al momento de esta captura, la mayor parte de la solución lleva entre 3 semanas y 3 meses en Producción — no es un proyecto "no shippeado". Quedan sin resolver solo 2 defectos puntuales de configuración (cambio de prioridad de procesador sin efecto; alta que hereda Prisma sin generar CVU) y una pieza de deuda técnica de reglas por canal, ninguno de los cuales impide que el volumen ya esté circulando por el segundo procesador.

**Por qué esto importa:** la nota original estimaba que sumar el canal POS al scope de esta métrica aportaría aproximadamente +15% al cierre de 2026 (según la propia nota de `north_star.md`). Mientras el scope no se actualice, ese volumen — que ya se está generando — no se refleja en la métrica que sigue la dirección de la empresa.

**No resuelto en esta captura:** quién tiene la potestad de decidir la actualización del scope (¿el propio PM del proyecto, o el CEO, dado que esta métrica está definida por indicación suya?) y en qué momento corresponde aplicarla — es la misma pregunta abierta que ya vive en el backlog personal del PM (`1_proyectos/tareas.md`, tarea sobre PRD-70 sin resolver desde el 2026-08-20). No se decide acá; se deja constancia de la contradicción para que se resuelva con evidencia real en vez de con la nota desactualizada de julio.
