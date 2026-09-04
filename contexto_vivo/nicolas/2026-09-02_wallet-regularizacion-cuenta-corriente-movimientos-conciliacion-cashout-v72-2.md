---
id: 2026-09-02_wallet-regularizacion-cuenta-corriente-movimientos-conciliacion-cashout-v72-2
pm: nicolas
fecha_captura: 2026-09-02
fuente: "Reunión \"Analisis de Riesgo - Emisión V 72.2\" (2026-09-02)"
producto: wallet
tema: Regularización de campos entre cuenta corriente y movimientos completos, y ampliación de la conciliación con Coelsa para incluir transferencias tipo cash out
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Analisis de Riesgo - Emisión V 72.2" (2026-09-02) se aprobaron dos tickets adicionales para el mismo pase a producción (reprogramado a lunes 2026-09-08 8:00hs):

**1. Regularización de cuenta corriente vs. movimientos completos (WS-1554 BIND / DEM-1826 Fintexa, semáforo amarillo — cambio funcional).** El endpoint de cuenta corriente no traía todos los campos que sí tiene el de movimientos completos, generando fricción cuando una entidad migra de uno a otro (ej. si Bind le dice a un cliente "usá el de cuenta corriente" y ese endpoint tiene menos datos, se genera un problema de discrepancia de datos según el propio equipo). Se agregan a las consultas de cuenta corriente y movimientos los campos: **ID de comprobante relacionado, motivo de rechazo, estado externo e importe de operación**. Esto habilita a organizaciones como **GST y Ecocerrado** a vincular y conciliar sus operaciones correctamente. Se notificará a los clientes por el cambio de campos expuestos.

Nota de alcance (aclarada por Juan Pablo Carubelli en la reunión): el ticket toca dos cosas distintas — (a) en cuenta corriente, agrega los campos que ya tenía movimientos (motivo rechazo, estado externo, importe operación); (b) en el GET de movimientos, agrega el **ID de comprobante relacionado** (el identificador, no el detalle del comprobante vinculado — mostrar el comprobante relacionado completo es un tema aparte, todavía en discusión con Nicolás Colón, no incluido en este ticket).

**2. Conciliación de transferencias Cash Out vía Coelsa (WS-1552 BIND / DEM-1806 Fintexa, semáforo verde — no funcional).** El proceso de conciliación con Coelsa contemplaba solo transferencias inmediatas entrantes; se corrige para que también incluya transferencias de **tipo cash out**. Sin impacto en otros elementos según Maria Eugenia Vila (responsable de controlar el funcionamiento post-implementación). Nota aparte: la activación diferida de este cambio para una entidad particular (fuera de alcance de este documento) se pospuso por una dependencia de infraestructura (reinicio de ingreso pendiente, a cargo de Nico Pomponio).

**Excluido de este pase a producción:** el ticket de habilitación de API Buffer, que queda para otra oportunidad.

> Fuente: Reunión "Analisis de Riesgo - Emisión V 72.2" (2026-09-02), minuta Gemini.
