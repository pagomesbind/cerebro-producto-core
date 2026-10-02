# Devoluciones y Contracargos — Agente de Cobros y Pagos

> Estado: en producción (bug confirmado), corrección decidida sin fecha de despliegue confirmada todavía.

## Bug — contracargos de colectores rechazados por validación de ID de caja vs. ID de colector

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-09-07), minuta Gemini.

Para colectores como **Pago Fácil**, las **devoluciones** se procesan correctamente, pero los **contracargos** quedan guardados con estado de rechazo por una validación interna que compara el **ID de caja de la transacción** contra el **ID de caja del colector** — campos que difieren en el ~99% de los casos reales, ya que no tiene por qué coincidir la caja puntual donde se originó la transacción con la caja general configurada del colector.

**Decisión del grupo:** eliminar esa validación mediante una corrección técnica, ya que no aporta control real y bloquea contracargos legítimos.

**Distinto del proyecto de tratamiento de contracargos de Adquirencia:** este bug es específico de contracargos de colectores **RxT/CVUCollect** en Agente de Cobros y Pagos — no debe confundirse con el proyecto de tratamiento de contracargos de tarjetas (PRD-146, prioridad alta, tickets DAD-2209/DAD-2257), que corre en paralelo sobre Adquirencia. Ver [`detalle_productos/adquirencia/devoluciones_y_contracargos.md`](../adquirencia/devoluciones_y_contracargos.md) para ese frente.

## Devoluciones de más de 30 días habilitadas por entidad, hasta 6 meses (pedido del Ministerio de Justicia)

> Fuente: Reunión "Análisis COBRO" (2026-10-01), resumen del mail de Gemini (Drive invalidado, sin minuta completa).

El portal no deja devolver una transferencia pasado el plazo estándar de 30 días. En la reunión "Análisis COBRO" del 2026-10-01 se acordó resolverlo con una **especificación por entidad** que habilita devoluciones de **hasta 6 meses** — no cambia la regla general de 30 días, solo se abre para las entidades que tengan la especificación activa.

**Origen del pedido:** el **Ministerio de Justicia**, uno de los casos de "ministerios y Rifsa" que ya pedían devolver fuera de plazo (reunión "Weekly - Producto / Operaciones", 2026-09-14).

**Calendario acordado:** desarrollo de la corrección por el grupo; pruebas el 2026-10-02; pase a producción el **lunes 2026-10-05 por la noche**.

**A confirmar (sin precisión en la minuta disponible):** el nombre técnico de la especificación, si el plazo de 6 meses es fijo o configurable por entidad, y si alcanza a transferencias, a QR o a ambos.

## Ver también

- [`detalle_productos/adquirencia/devoluciones_y_contracargos.md`](../adquirencia/devoluciones_y_contracargos.md) — devoluciones/contracargos de Botón Simple y QR (Adquirencia), dominio distinto pese al nombre de archivo compartido.

---
*Última actualización: 2026-10-02 — `/context_merge`: nueva sección de devoluciones hasta 6 meses por entidad (pedido Ministerio de Justicia, pase a producción 2026-10-05) (Nicolás Colón).*
*Creado: 2026-09-08 — `/context_merge`, desde reunión "Weekly - Producto / Operaciones" (2026-09-07).*
