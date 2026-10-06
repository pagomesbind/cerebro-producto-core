---
id: 2026-10-02_conocimiento-ccl-pruebas-staging-desbloqueadas
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Charla directa con el PM (Nicolás Colón) durante /idea_risks de inter_trazabilidad_ccl (PRD-259), 2026-10-02"
producto: wallet
tema: Las pruebas de punta a punta de Dólar CCL en staging ya no están bloqueadas por errores de Apibank en homologación
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/dolar_ccl.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/wallet/dolar_ccl.md §3.6bis — 'Queda en Stand-by/Parking Lot la corrección definitiva de los errores de Apibank (reportados vía Poison) que bloquean hoy las pruebas end-to-end de CCL en ambientes no productivos'"
confianza: media
estado: en_cola
---

**Qué cambia respecto del canon.** La sección §3.6bis de `dolar_ccl.md` (despliegue de V72, 2026-08-18) dice que los errores de Apibank en homologación **bloquean las pruebas de punta a punta de Dólar CCL en ambientes no productivos** y que su corrección quedó en Stand-by/Parking Lot.

**Dato nuevo (2026-10-02):** Nicolás Colón (PM) confirma que **ese bloqueo está resuelto**. Como evidencia, el 2026-10-01 se generó **en staging** una intención de compra de dólar CCL en el momento, del modelo COMBI (cuenta 276358, `intencionId` 14577), y el GET de intención devolvió el detalle completo con el circuito operando: estado `EN_PROCESO`, ingreso al broker registrado y comprobantes de débito creados.

**Sugerencia para el merge:** actualizar §3.6bis para dejar asentado que el bloqueo de pruebas por Apibank en homologación quedó resuelto. Según el PM ya estaba funcionando al 2026-10-01; no se conoce la fecha exacta de resolución ni el ticket que la cerró. No tomarlo como un bloqueo vigente en análisis de riesgo futuros.

**Confianza media:** es una confirmación verbal del PM. La única evidencia es una intención generada el 2026-10-01, sin fecha ni ticket de resolución, y sin saber si se probó también la pata 2 (día hábil siguiente).
