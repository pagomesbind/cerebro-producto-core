---
id: 2026-10-13_wallet_riesgo_incidente_qr_autoinflingido_war_room
pm: pablo
fecha_captura: 2026-10-16
fuente: "/sync_meetings — reunión 'Wallet - Tiempos de QR' (2026-10-13, 16:00)"
producto: wallet
tema: Caída total de transacciones QR/transferencias/cobro (~14 min) causada por el propio equipo al ajustar tiempos de consulta a Coelsa, War Room abierto
tipo: riesgo
destino_propuesto: 3_recursos/detalle_productos/wallet/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Qué pasó

Durante una reunión de trabajo para bajar los tiempos de respuesta de pagos QR de Wallet (reclamo recurrente del cliente Global66, promedio de respuesta subiendo de ~7,5s a ~10s), Nicolás Colón modificó en caliente las especificaciones de la "doble consulta" a Coelsa (primera consulta bajada de 4,5s a 2,5s, segunda consulta compensada a 4s) directamente en el ambiente de producción. Al borrar y recrear las especificaciones, **el sistema dejó de procesar transacciones por completo durante ~14 minutos** (última operación registrada 16:07hs): sin pagos QR, sin transferencias entrantes ni salientes, sin cobros en Botón Simple 1.0, en **ninguna entidad**. Gonzalo Rivera abrió un canal de War Room para gestionar el incidente.

## Causa técnica

No se identificó una causa de fondo distinta a la manipulación de las especificaciones en sí — el equipo (Nicolás Colón, Juan Pablo Carubelli, Gonzalo Rivera, Pablo Gomes) no logró explicar en la misma sesión por qué borrar/recrear la configuración de tiempos de consulta tira abajo todo el procesamiento transaccional, más allá de confirmar que coincidió exactamente con el momento del cambio.

## Contexto del cambio de tiempos (antes del incidente)

- Global66 reclamaba demoras de pago QR >7,5-9s (Grafana). El 90% de las operaciones llega el webhook de Coelsa ~2,7s antes de que el sistema las consulte.
- Se acordó bajar la primera consulta de 4,5s a 2,5s y subir la segunda de 2s a 4s (manteniendo el total ~6,5s), para no saturar el State Monitor con operaciones que quedan pendientes.
- Se descartó explícitamente usar el aviso directo de Coelsa como confirmación de pago exitoso ("no lo vamos a poner").
- Quedó pendiente un informe comparativo semana 06/10-13/10 vs. 13/10-20/10 para medir el impacto real del cambio (a cargo de Juan Pablo Carubelli y Lautaro Duarte, Keepit Simple).

## Riesgo a registrar

Cambios de configuración operativa sensible (tiempos de consulta a un proveedor externo crítico) se hicieron **en producción, en vivo, durante una reunión de análisis**, sin ventana de mantenimiento ni plan de rollback preparado de antemano — el War Room fue reactivo, no preventivo. No hay evidencia en la minuta de un post-mortem formal posterior a este incidente específico (distinto del post-mortem de certificados del mismo período, ya capturado en `2026-10-13_arquitectura_conocimiento_incidente_certificado_intermedio`).

> Fuente: reunión "Wallet - Tiempos de QR", 2026-10-13 16:00hs (Pablo Gomes, Gonzalo Rivera, Nicolás Colón, Juan Pablo Carubelli, Lautaro Duarte).
