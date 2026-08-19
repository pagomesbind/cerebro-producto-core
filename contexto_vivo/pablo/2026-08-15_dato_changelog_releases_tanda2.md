---
id: 2026-08-15_dato_changelog_releases_tanda2
pm: pablo
fecha_captura: 2026-08-15
fuente: "/sync_releases — barrido incremental 2026-08-15, tanda 2/2"
producto: transversal
tema: Entradas de changelog de producto — cierre completo del barrido 2026-08-15
tipo: dato
destino_propuesto: 3_recursos/datos/changelog_releases.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: capturado
merge_commit:
---

Prepend (orden cronológico inverso, van ANTES de las entradas de la tanda 1 por ser de versiones más viejas — insertar en la posición cronológica correcta según fecha, no todas al principio):

## 2026-08-10 — W 71.7 FIX (Wallet)

**Nuevos requerimientos:** alta de una nueva organización (PAFX) en producción.

---

## 2026-08-06 — W 71.6 FIX (Wallet)

**Nuevos requerimientos:** segunda etapa de la migración de autenticación externa (AuthExternal V2) a producción, cubriendo los servicios de Wallet.BIND y transferencias compartidas (SharedDebin).

---

## 2026-07-31 — W 71.5 FIX (Wallet)

**Mejoras funcionales:** ajuste de configuración menor en la app de demostración interna.

---

## 2026-07-30 — W 71.4 FIX (Wallet)

**Arreglos de errores:**
- El monto obtenido en una compra de Dólar CCL ahora se actualiza siempre que la operación se confirme, incluso cuando eso pasa el mismo día.
- Los comprobantes de cargo de Dólar CCL ahora quedan mejor identificados y expuestos correctamente en las consultas de la API.

**Nuevos requerimientos:** primera etapa de la migración de autenticación externa (AuthExternal V2) a producción.

---

## 2026-07-28 — W 71.3 FIX (Wallet)

**Nuevos requerimientos:** alta de 2 nuevas organizaciones en producción (HAPSA y una app de demostración interna para pruebas productivas de Bind PSP).

---

## 2026-07-23 — W 71.2 FIX (Wallet)

**Arreglos de errores:**
- Los reportes de movimientos ya no muestran el código de PSP en 0.
- Mejoras de infraestructura para distribuir mejor la carga entre servidores y reducir la sobrecarga de algunos nodos.

**Mejoras de rendimiento:** la consulta interna de días feriados dejó de pasar por un gateway externo, reduciendo errores de conexión y latencia.

**Nota técnica:** se llevó a producción una actualización mayor del componente que envía notificaciones (webhooks) a las organizaciones — incluye la base para soportar colas de mensajería más resilientes a futuro (todavía no activadas).

---

## 2026-07-16 — W 71.1 FIX (Wallet)

**Arreglos de errores:** mejora de resiliencia en el procesamiento de transferencias entrantes ante fallas de conexión internas.

---

## 2026-07-15 — W 71 (Wallet)

**Arreglos de errores:**
- Corregido el flujo de venta de Dólar CCL: ahora primero se acredita el monto obtenido y después se debita la comisión (antes exigía saldo disponible innecesariamente), y la comisión se calcula correctamente sobre el monto real obtenido.
- Mejorada la interpretación de errores del proveedor de cambio de moneda en compras y ventas de Dólar CCL, evitando que operaciones rechazadas queden mal clasificadas.
- Corregido el mapeo del identificador de contracargos de DEBIN, que guardaba el dato incorrecto.
- Corregido que eliminar una cuenta ahora también la deshabilita correctamente, evitando inconsistencias al intentar reactivarla.
- Las transferencias saliente ya no quedan "atascadas" en estado de espera indefinida cuando el banco responde que no encuentra la operación: pasado un margen de tiempo se rechazan automáticamente.
- Corregido un bug de duplicación de registros en el proceso de cuentas remuneradas (FCI).

**Nuevos comportamientos:**
- Nuevo endpoint para que Soporte pueda registrar manualmente un contracargo de DEBIN cuando no llegó por el canal automático.
- La consulta de cuenta por CBU/CVU/alias ahora puede devolver todos los cotitulares de la cuenta, no solo el primero.
- Los comprobantes ahora pueden crearse y consultarse también por su código, además de por su identificador interno — pensado para clientes que operan en varios ambientes con configuraciones distintas.
- El endpoint de totalizadores de Coelsa ahora también está disponible para el flujo de onboarding.

**Mejoras funcionales:** control de duplicidad reforzado para evitar comprobantes de Cobro QR interoperable repetidos.

---

## 2026-05-21 — Portal 2.0 V1 y V2, Adquirencia (rollout de mayo, ingestado retroactivamente el 2026-08-15 por un gap del backfill anterior)

**Arreglos de errores (rollout de Portal 2.0, incluye variante Mayorista):**
- Login bloqueado incorrectamente por reCAPTCHA para usuarios con VPN activa, pese a tener credenciales válidas.
- Usuarios recién creados con rol Administrador no obtenían el menú completo esperado.
- En el perfil Mayorista: no se podía asignar caja a un usuario Operador, la sección Transacciones no cargaba datos ni permitía devoluciones, y la sección QR daba error de carga.
- Transferencias con concepto distinto de "Varios" eran rechazadas incorrectamente.
- El saldo no se actualizaba después de un cobro con QR, impidiendo procesar la devolución correspondiente.
- Los PDF de liquidaciones exportados no podían abrirse.
- La columna de fecha de devolución quedaba vacía al exportar transacciones a Excel.
- En el Portal Web de Pagos al Exterior: la etiqueta de tipo de cuenta bancaria del beneficiario no distinguía correctamente entre los distintos formatos internacionales (IBAN vs. BAN), y el filtro de país en la búsqueda de beneficiarios quedaba pegado entre sesiones.

**Mejoras funcionales:** ocultar detalles de comisión/neto/retención en las vistas de perfil Mayorista (esa información no corresponde a ese nivel de usuario); a pedido de un cliente con gran volumen de sucursales, el filtro de sucursales ahora puede ordenarse alfabéticamente.
