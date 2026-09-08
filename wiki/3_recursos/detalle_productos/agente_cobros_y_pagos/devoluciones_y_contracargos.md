# Devoluciones y Contracargos — Agente de Cobros y Pagos

> Estado: en producción (bug confirmado), corrección decidida sin fecha de despliegue confirmada todavía.

## Bug — contracargos de colectores rechazados por validación de ID de caja vs. ID de colector

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-09-07), minuta Gemini.

Para colectores como **Pago Fácil**, las **devoluciones** se procesan correctamente, pero los **contracargos** quedan guardados con estado de rechazo por una validación interna que compara el **ID de caja de la transacción** contra el **ID de caja del colector** — campos que difieren en el ~99% de los casos reales, ya que no tiene por qué coincidir la caja puntual donde se originó la transacción con la caja general configurada del colector.

**Decisión del grupo:** eliminar esa validación mediante una corrección técnica, ya que no aporta control real y bloquea contracargos legítimos.

**Distinto del proyecto de tratamiento de contracargos de Adquirencia:** este bug es específico de contracargos de colectores **RxT/CVUCollect** en Agente de Cobros y Pagos — no debe confundirse con el proyecto de tratamiento de contracargos de tarjetas (PRD-146, prioridad alta, tickets DAD-2209/DAD-2257), que corre en paralelo sobre Adquirencia. Ver [`detalle_productos/adquirencia/devoluciones_y_contracargos.md`](../adquirencia/devoluciones_y_contracargos.md) para ese frente.

## Ver también

- [`detalle_productos/adquirencia/devoluciones_y_contracargos.md`](../adquirencia/devoluciones_y_contracargos.md) — devoluciones/contracargos de Botón Simple y QR (Adquirencia), dominio distinto pese al nombre de archivo compartido.

---
*Creado: 2026-09-08 — `/context_merge`, desde reunión "Weekly - Producto / Operaciones" (2026-09-07).*
