---
id: 2026-08-21_riesgo-bd-impuestos-liquidacion-online
pm: nicolas
fecha_captura: 2026-08-21
fuente: "Reunión \"Análisis COBRO\" (2026-08-20), minuta Gemini"
producto: agente_cobros_y_pagos
tema: Saturación de la base de datos de impuestos por CUIT compartido entre entidades comerciales
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Julieta Gimenez (Fintexa) reportó saturación en la base de datos de impuestos: múltiples entidades comerciales comparten el mismo CUIT, lo que vuelve ineficientes las consultas (descripto en la minuta como modelo de "quit repetido"). Se acordó aplicar un filtro por código de comercio para optimizar el proceso, coordinando el cambio con Sergio (Fintexa). En paralelo se identificó un error de lógica de negocio relacionado: las transacciones en línea no procesadas en el día quedaban en una cola de espera incorrecta en vez de liquidarse el mismo día o descartarse (fix ya acordado, ver conocimiento de producto asociado en `3_recursos/detalle_productos/agente_cobros_y_pagos/integracion_procesadores_pago.md`).

Además, para la prueba de carga de Provincia Net (meta: 150.000 registros) se identificó la necesidad de escalar los recursos de la base de datos de 4 a 6, con compromiso de generar el ticket correspondiente antes del lunes 2026-08-24.

Julieta Gimenez se comprometió a elevar por mail la situación de saturación a los interesados relevantes — esa escalación llegó el 2026-08-20 (thread "VISTA - RET_IIBB_REC_ACUM_LOTE - Impuestos Adquirencia", Ariel Profitti de Fintexa), con el detalle técnico de la causa raíz: la vista `RET_IIBB_REC_ACUM_LOTE` hace un `INNER JOIN` de `LIQ_IMP` contra `COMERCIO` por CUIT, y como un mismo CUIT puede pertenecer a hasta ~200 sucursales/comercios distintos, cada transacción real se multiplica en el join (fan-out) — 1 fila real se convierte en 200. Medido: 10 transacciones → 53 scans sobre `COMERCIO` y ~9.810.203 logical reads sobre `LIQ_IMP` (28,4 min reales); estimado a 500 transacciones → ~2.650 scans y ~490.510.150 logical reads (probablemente varias horas). No ocurre en ambientes bajos por no tener ese volumen ni esa repetición de CUITs. Fintexa está evaluando qué filtro agregar al proceso sin romper la lógica de negocio, en línea con el filtro por código de comercio ya acordado.

En el mismo hilo, Ariel Profitti reportó un segundo bug relacionado pero distinto: el proceso `dbo.GEN_LIQ_IMP_LOTE` falla (`Msg 515` — no se puede insertar NULL en la columna `PERC_IIBB_PORC` de `SharedImpuestoDB_prd.dbo.LIQ_IMP`) cuando una transacción no tiene ninguna percepción de IIBB aplicable (el caso más común): el `LEFT JOIN` contra `LIQ_IMP_CALCULAR_LOTE_PERC_IIBB` no encuentra fila y devuelve NULL en vez de 0, y esa columna no admite nulls. Propuso como fix envolver la vista con `ISNULL(PERC_IIBB_BASE, 0)`, `ISNULL(PERC_IIBB_PORC, 0)`, `ISNULL(PERC_IIBB, 0)`. Sin definición ni ticket confirmado todavía sobre este segundo bug al cierre del hilo (2026-08-20).

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini; mail "RV: VISTA - RET_IIBB_REC_ACUM_LOTE - Impuestos Adquirencia" (Ariel Profitti/Fintexa, reenviado por Melisa Belpassi, 2026-08-20).
