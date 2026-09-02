---
id: 2026-08-31_iniciativa-bajar-tiempos-pagos-qr-decision-t1-t2
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"Configuración de tiempos de consulta de Pagos QR\" (2026-08-31)"
producto: wallet
tema: Bajar tiempos de Pagos QR (PRD-199) — decisión final de T1/T2 tomada e implementada
tipo: iniciativa
proyecto: bajar-tiempos-pagos-qr
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

El proyecto "Bajar tiempos de Pagos QR" (PRD-199, asignado a Nicolás Colón) resolvió su pendiente principal: en la reunión "Configuración de tiempos de consulta de Pagos QR" (2026-08-31) se decidió e implementó la configuración final de la funcionalidad de doble consulta — T1 = 4,5 segundos, T2 = 2 segundos adicionales desde la respuesta de T1. El valor implementado es más agresivo que la recomendación basada en datos que el propio proyecto había preparado (mantener T1 en 5 seg, T2 ~9-10 seg absolutos) — ver decisión D-001 y riesgo R-001 en la carpeta del proyecto (`1_proyectos/bajar-tiempos-pagos-qr/decisiones.md` y `riesgos.md`). Motivador de negocio: reclamos de los clientes BSF y Global66 por transacciones QR en estado indeterminado (corrección 2026-09-01: registrado originalmente como "TPay", nombre no reconocido por el usuario — ver D-002 en `1_proyectos/bajar-tiempos-pagos-qr/decisiones.md`). Queda pendiente de monitoreo (T-016/T-017 en `tareas.md`) confirmar que no suba el % de caída al StateMonitor por encima de la línea base histórica (2-3%).
