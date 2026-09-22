---
id: 2026-09-21_adquirencia_conocimiento_deteccion_reuso_cbu_corta
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reunión \"Weekly - Producto / Operaciones\" (14:58, con Gonzalo Rivera, Nicolás Colón, Mariana Nadalin, Matías Alzogaray), 2026-09-21"
producto: adquirencia
tema: Método para detectar cuándo un pago de Botón Simple 2.0 falla porque el pagador reutilizó un CBU corto agendado de un pago anterior (caso Fabacar); auditoría formal asignada a v74/octubre
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Problema recurrente:** en Botón Simple 2.0 (Do), un usuario que ya transfirió una vez a un CBU corto de Bind PSP puede tenerlo agendado en su app bancaria. Si vuelve a pagar una deuda distinta (mes siguiente, otro comprobante) usando ese CBU agendado en vez de generar el pago desde el link/QR vigente, el pago llega igual por CBU corto pero puede no imputarse a la deuda correcta — genera inconsistencias que a la entidad le cuesta mucho diagnosticar. Gonzalo Rivera citó como ejemplo concreto un caso reciente con **Fabacar**, donde costó bastante entender que el reclamo de "inconsistencia en el pago" era por esta causa.

**Método de detección explicado por Nicolás Colón (Wallet), a partir del registro de transacciones:**
1. Filtrar todas las transacciones que llegaron a un CBU corto determinado.
2. Para cada una, comparar los datos del pagador (nombre, apellido y CBU de origen).
3. Si el mismo CBU/pagador aparece en **dos deudas distintas** (dos `ID deuda` diferentes) contra el mismo CBU corto, es muy probable que el segundo pago haya sido por reutilización del CBU agendado en la app del pagador, no por un pago nuevo generado desde el link/QR correspondiente a esa segunda deuda.
4. No hace falta que las dos deudas sean de meses distintos — alcanza con que el `ID deuda` cambie y el pagador se repita.

**Auditoría formal ya pedida, sin ejecutar todavía:** existe un pedido ya cursado de auditoría de CBU corto vinculada a las deudas asignadas (para poder aplicar este método de forma sistemática, no caso a caso) — Nicolás Colón confirmó que quedó asignada a la **versión 74** (sin fecha confirmada todavía, estimada octubre 2026, ya que la v74 todavía no tiene fecha cerrada).

**Impacto/uso:** hoy este análisis es manual y reactivo (se hace cuando un cliente reclama, como con Fabacar) — la auditoría de v74 lo convertiría en una herramienta proactiva/sistemática para Soporte.
