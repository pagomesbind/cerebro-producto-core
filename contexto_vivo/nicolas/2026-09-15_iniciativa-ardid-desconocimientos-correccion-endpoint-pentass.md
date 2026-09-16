---
id: 2026-09-15_iniciativa-ardid-desconocimientos-correccion-endpoint-pentass
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Sesión libre de cierre de gaps sobre ardid_desconocimientos (2026-09-15), a partir de la reunión Análisis COBRO (2026-09-14)"
producto: ardid
tema: Corrección de alcance — ardid_desconocimientos sí requiere pedirle un endpoint nuevo a Pentass
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "2026-09-11_iniciativa-ardid-desconocimientos-nuevo-proyecto (en_cola, pendiente de merge) — esa versión decía que se descartaba pedirle un endpoint nuevo a Pentass; esta corrige esa conclusión"
confianza: alta
estado: ingestado
merge_commit:
proyecto: ardid_desconocimientos
---

Corrección sobre el discovery de `ardid_desconocimientos` (PRD-248) ya capturado el 2026-09-11 (item `2026-09-11_iniciativa-ardid-desconocimientos-nuevo-proyecto`, todavía en cola de merge): el Gate 3 original había descartado pedirle a Pentass un endpoint nuevo, asumiendo que el mecanismo de carga masiva ya documentado en el catálogo de Ardid (`UploadChargebackTransactionsFile`) cubría la necesidad.

La reunión "Análisis COBRO" (2026-09-14) reveló que el PM había planteado ahí una propuesta de "desarrollo doble" con un **endpoint de carga individual** en Ardid, distinto del masivo — Daniela Collia (Fintexa) respondió que el equipo se sumaría "una vez que Ardid la tenga disponible", señal de que ese endpoint individual no existe hoy. Consultado el 2026-09-15, el PM confirmó: *"El endpoint para informar desconocimientos en Ardid debería pedirse a Pentass, e incluirlo en el alcance de este PRD"*.

**Qué cambia respecto de lo ya capturado (y pendiente de merge):**
- Se revierte la conclusión "se descartó pedirle nada nuevo a Pentass" — si la fila `ardid_desconocimientos` en `direccion/iniciativas.md` todavía no se mergeó con esa afirmación, debe reflejar en cambio que el pedido a Pentass **sí** va, dentro del alcance del mismo PRD.
- El resto del discovery (problema, Gate 1, Gate 2, y la pieza S1/S2 de automatización + retención) se mantiene sin cambios — ver `1_proyectos/ardid_desconocimientos/proyecto.md` y `decisiones.md` [2026-09-15] para el detalle completo.
- Los otros 2 gaps técnicos que quedaban abiertos (acceso directo al endpoint masivo; dueño del cambio de retención) también se cerraron el mismo día — el proyecto queda sin gaps bloqueantes, listo para estimar.
