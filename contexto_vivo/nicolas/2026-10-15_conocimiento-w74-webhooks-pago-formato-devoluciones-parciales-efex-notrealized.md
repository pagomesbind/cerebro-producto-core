---
id: 2026-10-15_conocimiento-w74-webhooks-pago-formato-devoluciones-parciales-efex-notrealized
pm: nicolas
fecha_captura: 2026-10-15
fuente: "Reunión \"W 74 - QA+Producto\" (2026-10-14), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: adquirencia
tema: Revisión QA+Producto de la versión 74 — cambio de formato de los webhooks de pago (avisar a clientes), devoluciones parciales que no se ven en el archivo, Pagos Efex a la regresión automática, NotRealized de Ardid para los rechazos de Botón Simple con prioridad máxima
tipo: conocimiento
destino_propuesto: 2_areas/procesos/publicaciones_mensuales.md
tipo_destino: actualizar
contradice: "no"
confianza: baja
estado: en_cola
---

**Qué completa.** Sigue al item `2026-10-14_conocimiento-ad-v74-cronograma-staging-16-10-prod-22-10-liquidaciones-a-v75`: esta es la reunión del 14/10 sobre Wallet y Cobros que había convocado Andrea Orsini. El título dice "W 74", pero se tocaron temas de Wallet y de Cobros (Adquirencia).

**Hallazgos de la revisión (reunión "W 74 - QA+Producto", 2026-10-14):**
- **Webhooks de pago:** se analizaron errores y **cambia el formato de los datos** que se envían. Hay que avisar a los clientes integrados antes del pase (T-134). El resumen no detalla qué campos cambian.
- **Devoluciones parciales:** se resolvió un problema de visualización, pero hay un reporte de que **las devoluciones parciales no aparecen en el archivo**. El resumen no dice qué archivo (¿liquidación o reporte de transacciones?). Queda a investigar (T-133).
- **Post y comprobantes:** hubo ajustes, sin detalle en el resumen.
- **Botón Simple, máxima prioridad:** se priorizó **avisar a Ardid las transacciones fallidas de Botón Simple con `NotRealized`** (ver `3_recursos/detalle_productos/ardid/apis_externas.md`, 17.b). Hoy Botón Simple es el único producto de Cobro que informa a Ardid. El canon no dice si los rechazos ya se informan.
- **Regresión:** Andrea Orsini suma los endpoints de **Pagos Efex** a las pruebas de regresión automáticas del próximo pase.

> Fuente: Reunión "W 74 - QA+Producto" (2026-10-14), resumen del mail de Gemini.
