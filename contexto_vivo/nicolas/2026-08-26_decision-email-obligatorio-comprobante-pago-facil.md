---
id: 2026-08-26_decision-email-obligatorio-comprobante-pago-facil
pm: nicolas
fecha_captura: 2026-08-26
fuente: "Charla directa con el usuario (2026-08-26); confirmación del cliente Guillermo Paolucci (Western Union/Pago Fácil) sobre el ticket SER-66"
producto: servicios
tema: Pago Fácil confirma que el email para envío del comprobante de pago será obligatorio en la pantalla de confirmación de datos
tipo: decision
destino_propuesto: 3_recursos/detalle_productos/servicios/pago_facil.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: c4148e7
---

**Contexto:** ticket [SER-66](https://bindpsp.atlassian.net/browse/SER-66) (Proyecto Servicios, no definitivo aún) pide dos cosas al equipo keepit sobre el flujo de Link de Pago de Pago Fácil (`pago_facil.md`): (1, front) agregar un campo de email en la pantalla de "Confirmar datos" del checkout, y (2, backend) enviar automáticamente el comprobante de pago a esa casilla al finalizar el proceso exitosamente. La captura de email se descartó explícitamente del checkout de Botón Simple 2.0 (que hubiera sumado costo cross-equipo) a favor de esta pantalla, propia del dominio de Pago Fácil/keepit — ver [[2026-08-26_pago-facil-sepsa-piloto-productivo-admin-y-pendientes]] y la wiki de Botón Simple 2.0 (`detalle_productos/adquirencia/boton_simple_2_0.md`) para el contexto del motor de checkout que no se toca.

**Punto que quedaba pendiente de definir con el cliente:** si el campo email debía ser obligatorio u opcional para poder avanzar con el pago. Quedó registrado como tarea T-013 en `1_proyectos/tareas.md`, con seguimiento de un hilo de mail directo con Guillermo Paolucci (Western Union/Pago Fácil).

**Decisión:** el cliente confirmó que el email **es obligatorio** — el usuario no puede avanzar de la pantalla de confirmación de datos sin completarlo.

**Impacto en las validaciones ya definidas para el ticket** (ver historia de usuario trabajada en este mismo hilo, no persistida aún como artefacto):
- Front: campo requerido, con manejo de error inline (recuadro/mensaje de error) si el usuario intenta avanzar sin completarlo o con formato inválido — no alcanza con deshabilitar el botón sin feedback.
- Se actualizó el mockup de referencia (basado en la captura real de la pantalla "Confirmar datos" de Pago Fácil, `raw/5e977560-92f9-410a-9287-9eebf49f3c5c.png`) agregando el estado de error visual (recuadro rojo) sobre el campo, para que quede claro en el ticket que el campo bloquea el avance si está vacío.

**Estado:** Aprobado por el cliente. No afecta la decisión ya tomada de mantener el envío del comprobante como asíncrono/best-effort en backend (eso no depende de si el campo es obligatorio o no).
