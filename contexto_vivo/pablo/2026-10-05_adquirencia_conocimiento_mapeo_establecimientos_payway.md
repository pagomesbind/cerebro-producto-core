---
id: 2026-10-05_adquirencia_conocimiento_mapeo_establecimientos_payway
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Weekly - Producto / Operaciones', 2026-10-05 15:01, minuta Gemini (compartida, mnadalin)"
producto: adquirencia
tema: Payway exige número de establecimiento (no el identificador de sitio interno) para gestionar reclamos — propuesta de tabla centralizada de mapeo
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/integracion_prisma_conexion_directa.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

**Hallazgo operativo (Gonzalo Rivera, reunión "Weekly - Producto / Operaciones", 2026-10-05):** al gestionar reclamos con Payway, Payway exige el **número de establecimiento** propio de su sistema — no el **identificador de sitio** que usa internamente Bind PSP — lo que obliga hoy a cruces manuales complejos entre bases de datos y reglas de negocio cada vez que hay que atender un reclamo.

**Propuesta discutida (sin decisión formal ni ticket asignado en esta reunión):** configurar una **tabla centralizada** donde cada identificador de sitio interno relacione su(s) establecimiento(s) y marca(s) de tarjeta correspondientes en Payway, para evitar el cruce manual.

**Nota:** Payway es el mismo procesador que el Admin de Bind muestra como "Payway" y que en Transacciones aparece como "PlusPagos" — mismo procesador documentado en `integracion_prisma_conexion_directa.md` y `pos_multiadquirencia.md` (Prisma por Conexión Directa). Confianza media porque la minuta no precisa si este mapeo aplica solo a POS/Conexión Directa o también a Botón Simple/checkout.
