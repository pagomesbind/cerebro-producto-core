---
id: 2026-10-02_conocimiento-devoluciones-hasta-6-meses-por-entidad-ministerio-justicia
pm: nicolas
fecha_captura: 2026-10-02
fuente: "Reunión \"Análisis COBRO\" (2026-10-01), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: agente_cobros_y_pagos
tema: Devoluciones de más de 30 días habilitadas por entidad, hasta 6 meses (pedido del Ministerio de Justicia), con pase a producción el lunes 05/10
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 75ba8d792351add07011499b503adabf55d5e4bd
---

**Qué se definió.** Hoy el portal no deja devolver una transferencia después de un mes (plazo estándar de 30 días, ver T-053 del 2026-09-14). En la reunión "Análisis COBRO" del 2026-10-01 se acordó cómo resolverlo: una **especificación por entidad** que habilita devoluciones de **hasta 6 meses**. No cambia la regla general: solo se abre para las entidades que tengan la especificación activa.

**Origen del pedido.** Lo pidió el **Ministerio de Justicia**. Es uno de los casos de "ministerios y Rifsa" que ya pedían devolver fuera de plazo (reunión "Weekly - Producto / Operaciones", 2026-09-14).

**Calendario acordado:**
- desarrollo de la corrección por el grupo;
- pruebas el 2026-10-02 ("mañana", según la minuta);
- pase a producción el **lunes 2026-10-05 por la noche**.

**Lo que la minuta no dice:** el nombre técnico de la especificación, si el plazo de 6 meses es fijo o se configura por entidad, y si alcanza a transferencias, a QR o a ambos. El resumen de Gemini no lo aclara y la minuta completa no se pudo leer (Google Drive invalidado). Hay que confirmarlo antes del merge, o documentarlo como "a confirmar".

> Fuente: Reunión "Análisis COBRO" (2026-10-01), resumen del mail de Gemini.
