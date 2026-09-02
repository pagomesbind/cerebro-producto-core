---
id: 2026-08-31_cumplimiento-domicilio-real-y-actividad-afip-altas-2024
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"Weekly - Producto / Operaciones\" (2026-08-31)"
producto: transversal
tema: Nuevas necesidades regulatorias planteadas para 2024 — domicilio real en alta de cuenta y consulta de actividad AFIP en altas de wallet
tipo: conocimiento
destino_propuesto: 3_recursos/cumplimiento_normativo/requisitos_kyc_altas_wallet.md
tipo_destino: crear
contradice: "no"
confianza: baja
estado: en_cola
---

En la reunión "Weekly - Producto / Operaciones" (2026-08-31) se mencionaron, sin mucho detalle, dos necesidades regulatorias que el equipo va a integrar en su planificación de cumplimiento:

- Obligación de **capturar el domicilio real** de los usuarios finales (personas humanas) en el request de alta de cuenta (CBU/Postcuenta).
- Necesidad de **consultar la actividad ante AFIP** durante las altas en wallets.

La minuta las etiqueta como "requerimientos regulatorios para 2024" sin más contexto (norma/comunicación de origen, fecha límite, quién lo pidió, alcance exacto — todo o nuevas altas). Dato de baja confianza por lo escueto de la mención; capturado igual porque toca directamente el flujo de alta de cuenta ya documentado en `wallet/organizaciones_y_configuracion.md` (que además tiene un gap normativo abierto relacionado: "CPA no se completa en el 72% de cuentas con domicilio", §0). Si el usuario tiene más contexto sobre esta obligación, conviene precisarlo antes de este merge.
