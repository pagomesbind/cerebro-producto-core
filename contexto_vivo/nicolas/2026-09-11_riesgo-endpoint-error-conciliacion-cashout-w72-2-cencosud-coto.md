---
id: 2026-09-11_riesgo-endpoint-error-conciliacion-cashout-w72-2-cencosud-coto
pm: nicolas
fecha_captura: 2026-09-11
fuente: "Hilo mail 'Re: Minuta: Analisis de Riesgo - Emisión V 72.2' — Maria Eugenia Vila, 2026-09-10"
producto: por confirmar
tema: Error de endpoint al validar que la conciliación Coelsa incluyó los movimientos de Cashout, post-despliegue W72.2, para organizaciones Cencosud y Coto
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Tras el despliegue en PROD de la versión **W 72.2** (07/09 — HotFixes en microservicios de Operaciones y Cuentas, incluyendo el ajuste de `/ConciliarCoelsa` para integrar operaciones tipo **CASHOUT** en la conciliación de transferencias entrantes, ítem DEM-1806/WS-1552), Maria Eugenia Vila reportó el 2026-09-10 que **no pudo validar que se hayan incluido los movimientos de Cashout porque el endpoint da error al correr el proceso** — trabajado en conjunto con Nicolás Colón, sin resolver todavía ("Hay que revisarlo").

Se generaron procesos para las organizaciones **Cencosud (4)** y **Coto (37)** en el marco de esta validación.

Este era justamente uno de los puntos de acción asignados a María Eugenia Vila en el plan post-despliegue ("Monitorear el correcto funcionamiento de la conciliación Coelsa — transferencias Cashout", deadline 07/09, prioridad Media) — sigue sin poder cerrarse por este error.

En el mismo hilo, otro punto de acción del plan post-despliegue sí se resolvió: Gonzalo Rivera confirmó que **no hay altas de CVU sin alias** luego de la implementación (punto que a él le tocaba verificar).

> Fuente: Mail "Re: Minuta: Analisis de Riesgo - Emisión V 72.2..." — Maria Eugenia Vila (mvila@bind.com.ar), 2026-09-10, 09:48hs; confirmación de Gonzalo Rivera en el mismo hilo, 2026-09-10, 17:02hs.

**Sin producto dueño claro identificado en el canon actual** (afecta microservicios de Operaciones/Cuentas y la conciliación con Coelsa) — `destino_propuesto` es el ledger de riesgos general; a confirmar en el merge si corresponde en cambio a un archivo temático de `detalle_productos/`.
