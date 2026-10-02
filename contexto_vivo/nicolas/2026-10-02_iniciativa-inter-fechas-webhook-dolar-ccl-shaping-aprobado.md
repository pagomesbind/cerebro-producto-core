---
id: 2026-10-02_iniciativa-inter-fechas-webhook-dolar-ccl-shaping-aprobado
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Sesión de /idea_start con el PM (2026-09-30 → 2026-10-02) sobre PRD-259"
producto: wallet
tema: Fechas en el webhook de Dólar CCL (pedido de Inter) — shaping aprobado
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: inter_trazabilidad_ccl
---

**Proyecto nuevo con shaping aprobado: [PRD-259](https://bindpsp.atlassian.net/browse/PRD-259) "Agregar fechas a los webhooks de la operatoria de Dólar CCL"** (PM Nicolás Colón, Wallet, cliente Inter, BAU). Epic de desarrollo ya creada: WS-1738 (Backlog, vacía).

- **Problema:** el webhook de Dólar CCL no trae ninguna fecha (20 campos, cero timestamps), así que Inter consulta el GET de intención después de cada notificación para reconstruir la operación. El volumen de Inter en Dólar CCL creció de 24 a 158 operaciones por trimestre en 2026 (calculado sobre `fact_operaciones`), y Inter espera que siga creciendo.
- **Solución aprobada (2026-10-02):** agregar al webhook las 8 fechas que ya expone el GET de intención (creación, vencimiento, ingreso al broker, última modificación, último cambio de estado, fin de la intención, fin esperado en el mercado, aceptación de la DDJJ), para **todos los operadores** (modelos INTE y COMBI comparten el payload). Queda fuera el momento de envío del webhook.
- **Tamaño preliminar de shaping:** S–M (1–3 SP), 2 SP en Jira. **Lo paga Inter**, bajo la política de cobro de desarrollos personalizados del 2026-09-21. Si no acepta el precio, no se hace.
- **Novedad para la cartera:** beneficia también a otros operadores activos de Dólar CCL (PagBrasil) sin costo extra. Coinbase está inactivo en Dólar CCL desde la semana 202605. Pendientes: cotización de Fintexa y definición comercial de cómo cobrar un cambio compartido.
- **Riesgo técnico detectado:** 2 de las 8 fechas del GET vienen sin offset de zona horaria (`ddjjAceptadaFechaHora`, `fechaHoraFinalizacion`), la misma familia de bugs de PRD-81 y WS-448.
