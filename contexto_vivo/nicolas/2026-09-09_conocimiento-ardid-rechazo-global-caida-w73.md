---
id: 2026-09-09_conocimiento-ardid-rechazo-global-caida-w73
pm: nicolas
fecha_captura: 2026-09-09
fuente: "Mail \"RE: Version W 73 Wallet Service\" — Nicolas Pomponio (Fintexa), 2026-09-08 20:59"
producto: ardid
tema: W73 confirma el rechazo global de operaciones cuando Ardid está caído, sin el State Monitor que hoy lo contendría — riesgo funcional advertido por el propio proveedor
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/integracion_con_productos_bind.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

El mail "RE: Version W 73 Wallet Service" (Fintexa, 2026-09-08) confirma qué parte del discovery de robustez de Ardid ya documentado en `integracion_con_productos_bind.md` (§6.1 mapeo de motivos de rechazo, §14 diseño de State Monitor — ambos de reuniones de agosto, marcados como "no construido") entra efectivamente en la versión **W73**, y qué queda afuera:

**Dentro de W73:**
- Mapeo del motivo de rechazo (cierra el §6.1, tarea abierta desde la reunión "Producto" del 2026-08-18).
- Habilitación global de operaciones.
- **Rechazo de todas las operaciones cuando Ardid está caído o no responde.**
- Deshabilitación automática de cuentas bloqueadas.

**Queda afuera, pasa a W74:** el **State Monitor de Ardid** (§14) — "se sigue analizando; no bloquea al resto de los desarrollos de Ardid".

**Riesgo funcional explícito señalado por el propio Fintexa:** habilitar el rechazo global de operaciones cuando Ardid está caído **sin** el State Monitor que hoy las contendría tiene impacto funcional — puede rechazar transacciones legítimas durante una caída de Ardid, no solo las fraudulentas. Fintexa se comprometió a avisar con anticipación a Soporte y hacer un análisis de riesgo antes de habilitarlo en producción. Este es un riesgo a monitorear antes del despliegue de W73 (entrega a QA Externo 21/09).

> Fuente: Mail "RE: Version W 73 Wallet Service" (hilo 2026-09-03 → 2026-09-09), mensaje del 2026-09-08 20:59 de Nicolas Pomponio (Fintexa).
