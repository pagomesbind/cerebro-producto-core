---
id: 2026-08-18_wallet_contracargo_recurrente_produccion_trazabilidad_recycle
pm: pablo
fecha_captura: 2026-08-18
fuente: "/sync_meetings — reunión \"Productos - Weekly Seguimiento\" (2026-08-18)"
producto: wallet
tema: Contracargo de débito recurrente pasa a producción + fix de trazabilidad en Recycle
destino_propuesto: 3_recursos/detalle_productos/wallet/recycle_cobro_automatico.md
tipo: conocimiento
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: capturado
merge_commit:
---

**Contracargo de débito recurrente — pruebas finalizadas, pasa a producción la semana del 2026-08-18** (según "Productos - Weekly Seguimiento"). Se decide el criterio de cuándo pasar una funcionalidad a "shipping": recién cuando esté **enteramente en producción** (no cuando solo falte el propio pase), a diferencia del criterio anterior que la marcaba shipping con trabajo pendiente del lado de Bind PSP.

**Hallazgo de trazabilidad (encontrado durante las pruebas):** existe una especificación de Wallet que habilita el aviso de "reciclado" (Recycle) en operaciones — Recycle se usa normalmente para impuestos, cuyas operaciones no tienen una operación relacionada. Con el contracargo de débito recurrente, en cambio, **sí existe una operación original relacionada** al momento del cobro. Sin esta especificación habilitada, cuando Recycle cobraba el contracargo, **no le avisaba a la operación original que debía cambiar de estado** — se perdía la trazabilidad entre el contracargo y la operación que lo originó. Ya se dio de alta esa especificación en **todas las organizaciones en producción** (no solo la nueva) para resolverlo de forma retroactiva.

**Decisión de comunicación:** no hace falta avisar a los clientes del contracargo en sí — el aviso relevante es interno (Comercial/todo el equipo), para que sepan que ya se le puede ofrecer a cualquier organización, con el riesgo estándar de contracargo ya conocido (qué pasa cuando no se puede cobrar, etc.).

> Fuente: minuta de Gemini de "Productos - Weekly Seguimiento" (2026-08-18, docId `1HjXi7R_F1esr-ExW4DELmvZgckdaFRl5ahRGYnO4W7A`), detalle "Contracargo de bien recurrente".
