---
id: 2026-10-09_wallet_conocimiento_ardid_deshabilita_cuenta_wallet
pm: pablo
fecha_captura: 2026-10-09
fuente: "/sync_mails — mail '📣 NOVEDADES PRODUCTO - Wallet ahora deshabilita automáticamente las cuentas que Ardid bloquea' (threadId 1a120a21b617f31a), Nicolás Colón, 2026-10-09, comunicación oficial de Producto a Soporte/Integraciones/Comercial"
producto: wallet
tema: Wallet deshabilita automáticamente la cuenta cuando Ardid bloquea al cliente (publicado en producción W73, 08/10/2026) — webhook de aviso + registro de habilitaciones/deshabilitaciones
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/ardid_integracion.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Comunicación oficial de Producto (Nicolás Colón) a Soporte/Integraciones/Comercial, publicada en producción desde el 08/10/2026 (W73).

**Problema que resolvía:** Ardid podía bloquear a un cliente, pero su cuenta de Wallet seguía *habilitada*. El bloqueo frenaba solo las operaciones que pasan por Ardid (transferencias, Pago QR, transferencias pull), pero la cuenta todavía podía sacar dinero por otros medios que Ardid no monitorea (ejemplo real: compra de dólares en Astropay). Además, la organización no se enteraba del bloqueo — ventana de exposición al fraude y deuda de control interno para el cumplimiento de Bind como PSP.

**Qué se implementó:**
- Cuando Ardid analiza una operación y responde que el cliente está bloqueado o debe bloquearse, Wallet deshabilita la cuenta automáticamente. Una cuenta deshabilitada no puede hacer cashout de ningún tipo — aplica a transferencias salientes y entrantes, Pago QR, DEBIN Recurrente y Pago FX.
- En el mismo momento se avisa a la organización por webhook, con el motivo y la operación que disparó el bloqueo.
- Queda registro de toda habilitación y deshabilitación de cuentas, con su motivo, para que Soporte pueda explicar cada caso.
- La organización puede rehabilitar la cuenta por el endpoint de siempre. Si el cliente sigue bloqueado en Ardid, la próxima operación analizada la vuelve a deshabilitar.

**Qué NO se hizo (alcance explícito):**
- Desbloquear a un cliente en Ardid no rehabilita su cuenta en Wallet — son dos pasos separados.
- No bloquea el cash in: el CVU sigue activo y la cuenta puede seguir recibiendo dinero.
- No impide que la organización rehabilite una cuenta bloqueada por Ardid (puede hacerlo, y queda registrado).
- No hay desbloqueo o rehabilitación automáticos.

**Métricas (antes → ahora):**
- Estado en Wallet de una cuenta bloqueada por Ardid, en su próxima operación analizada: Habilitada → Deshabilitada (al operar).
- Aviso a la organización cuando Ardid bloquea: no existía → webhook nuevo.
- Habilitaciones/deshabilitaciones con registro: 0% → 100%.
- Todavía sin medición estadística formal — el cambio se activó el 08/10/2026 y el efecto se ve a medida que las cuentas bloqueadas intentan operar.

**Impacto operativo conocido — COTO:** COTO des/bloquea a sus usuarios desde el front de Ardid. Con este cambio, además de desbloquear en Ardid, ahora tiene que habilitar la cuenta en Wallet por API — un paso que hoy no está en su flujo y que la organización planteó como un freno al equipo de Producto. Lo mismo aplica a cualquier organización que opere de la misma manera (desbloqueo solo en Ardid, sin tocar Wallet). Soporte/Integraciones tienen una guía para integradores lista para reenviar a clientes con el paso a paso de rehabilitación.

> Fuente: mail "📣 NOVEDADES PRODUCTO - Wallet ahora deshabilita automáticamente las cuentas que Ardid bloquea" (threadId `1a120a21b617f31a`), Nicolás Colón, 2026-10-09.
