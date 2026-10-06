---
id: 2026-10-05_wallet_fallback_consulta_coelsa_caida_apibank
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Weekly - Producto / Operaciones', 2026-10-05 15:01, minuta Gemini + transcripción (compartida, mnadalin)"
producto: wallet
tema: pagos QR de Wallet quedan en estado pendiente cuando cae APIBank, aunque el pago vaya directo a Coelsa — propuesta de consulta directa por ID
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/conciliacion_y_totalizadores.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Mecanismo confirmado (Gonzalo Rivera, Nicolás Colón, reunión "Weekly - Producto / Operaciones", 2026-10-05):** cuando una entidad de Wallet paga un QR de otro aceptador (pago QR desde Wallet, no cobro), Bind va **directo a Coelsa**, sin pasar por APIBank. Pero si APIBank está caído, el pago igual se ve afectado: Coelsa envía el aviso de confirmación del débito al **banco sponsor (APIBank)**, no directo a Bind — y si APIBank está caído, ese webhook nunca llega. El resultado es que la transacción queda indefinidamente en **estado 4** (pendiente) mientras dure la caída, sin que Bind haga nada para resolverlo activamente.

**Propuesta técnica discutida (sin decisión cerrada):** en vez de esperar pasivamente el webhook del banco sponsor, que Bind **consulte directamente a Coelsa el estado del pago QR por ID** (consulta por "ID Coelsa") para resolver el estado por su cuenta — evitando los ~15-20 minutos que hoy quedan pendientes ante una caída. El equipo había identificado antes que ese endpoint de consulta por ID "no estaba funcionando" contra Coelsa (sin más detalle de causa en esta reunión). Nicolás Colón: "no sé si me expliqué" — Pablo Gomes acordó que se puede analizar, pero condicionado a cuánto cueste construirlo ("si sale dos mangos" vs. "si sale 500.000") — Gonzalo Rivera lo calificó directamente de deuda técnica (un mecanismo que "no anda" resuelto a media máquina). Sin ticket ni responsable asignado al cierre de esta reunión — análisis técnico queda pendiente.

**Relación con gap ya documentado:** este hallazgo es el mismo mecanismo de fondo que el gap abierto en `conciliacion_y_totalizadores.md §5` (tensión sin resolver entre "herramienta rota" y "limitación de rango", capturado 2026-10-01/02) — lo complementa con el detalle de que el punto de falla específico es el webhook de confirmación de Coelsa→banco sponsor→Bind, no solo un rango de conciliación.
