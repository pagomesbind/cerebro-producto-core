---
id: 2026-10-02_iniciativa-inter-fechas-webhook-dolar-ccl-solucion-aprobada
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Sesión de /idea_solution con el PM (2026-10-02) sobre PRD-259"
producto: wallet
tema: Fechas en el webhook de Dólar CCL (Inter) — análisis técnico-funcional aprobado
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: inter_trazabilidad_ccl
---

**PRD-259 — análisis técnico-funcional aprobado (2026-10-02).** El cambio es aditivo: 8 campos de fecha al final del payload del webhook de Dólar CCL.
- Valor y formato idénticos a los del GET de intención, sin normalizar.
- PascalCase como el resto del webhook, una excepción deliberada a la directiva camelCase.
- `null` explícito cuando el dato no existe todavía.
- Aplica a compra y venta, en los modelos Standard y COMBI. No hay eventos ni estados nuevos.

**Riesgo principal:** un operador que valide el esquema de forma estricta podría dejar de recibir avisos, así que hay que avisar a todos los operadores de Dólar CCL antes de publicar.

**Pendientes:** 4 gaps técnicos no bloqueantes que se resuelven en el refinamiento con Ingeniería (el PM descartó consultarlos por mail a Fintexa), la cotización y la definición comercial del cobro a Inter. Siguiente paso: revisión de impacto por área.
