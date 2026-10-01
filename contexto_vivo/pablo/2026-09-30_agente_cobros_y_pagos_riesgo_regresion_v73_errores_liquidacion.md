---
id: 2026-09-30_agente_cobros_y_pagos_riesgo_regresion_v73_errores_liquidacion
pm: pablo
fecha_captura: 2026-09-30
fuente: "/sync_meetings — reunión 'Revisión Pruebas QA' (2026-09-30 16:01, minuta Gemini, docId 1g6Mz2XoHG3J41LD9rFuSpskdPZxlfPEaogLeGyrfXPk), compartida por Matias Alzogaray. Invitados: Pablo Serra, Melisa Belpassi, Nicolás Pomponio (Fintexa), Hernán Clarich, Matias Alzogaray, Andrea Orsini, Pablo Gomes"
producto: agente_cobros_y_pagos
tema: Pruebas de regresión apresuradas revelaron errores no identificados en el área de liquidación
tipo: riesgo
destino_propuesto: wiki/2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: baja
estado: ingestado
merge_commit:
---

<!--
Cuerpo: conocimiento TRABAJADO y COMPLETO, no la transcripción cruda.
No resumir — el detalle completo es lo que hace que "no omitir" sea sostenible.
Citar la fuente donde corresponda (quién lo dijo, en qué reunión/mail/sesión).
-->

**Hallazgo:** en la reunión "Revisión Pruebas QA" del 2026-09-30, Andrea Orsini (QA) informó que las pruebas de regresión del ciclo reciente se corrieron "hasta el último momento" (apuradas) y que el área de **liquidación no se probó con la profundidad necesaria** — como consecuencia, aparecieron errores reportados informalmente por chat, sin que el grupo definiera una solución inmediata en la reunión. Pablo Serra (Fintexa) agregó que "Mauri" le había comentado algo relacionado con "un tipo de pago", sin más precisión.

**Contexto temporal:** la reunión es del 2026-09-30, un día después del despliegue de V73 (martes 29/09, 20:30-23hs — ver `1_proyectos/rechazos_bines_payway/proyecto.md §7`), el mismo despliegue que incluyó el fix de liquidaciones (AD-1791/AD-1822/AD-1835/AD-1837, confirmado bloqueante para V73 — ver `3_recursos/detalle_productos/agente_cobros_y_pagos/liquidaciones_reversas_y_comprobantes.md §2-5`). Es razonable (no confirmado) que los "errores en liquidación" detectados en esta regresión estén relacionados con ese mismo fix recién desplegado, pero la minuta no lo dice explícitamente ni da número de ticket, alcance ni severidad.

**Ambigüedad explícita — no se infiere nada más:** la minuta no identifica qué error puntual apareció, qué tipo de pago está involucrado, ni si hay impacto en producción real o solo en el entorno de pruebas. La reunión termina con la coordinación de otra reunión pendiente (reprogramada para mañana 9:30, posiblemente corrida a viernes) sin que quede claro si esa reunión es donde se va a tratar este hallazgo — no hay acción de Producto identificable ni due owner de la resolución técnica.

**Por qué se registra con `confianza: baja`:** no hay forma de confirmar si esto ya está cubierto por el seguimiento habitual de QA/Fintexa sobre liquidaciones (que viene con bastante actividad reciente, ver archivo de referencia arriba) o si es un hallazgo nuevo sin ticket todavía. Se registra como riesgo transversal de calendario de QA (regresión apresurada en ciclos de despliegue) más que como un bug puntual — si en una próxima reunión/mail aparece el ticket concreto, hay que completar este item (ver paso de revisión hacia atrás de la skill).
