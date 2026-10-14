---
id: 2026-10-14_conocimiento-ad-v74-alcance-detallado-por-olas-mail-09-10
pm: nicolas
fecha_captura: 2026-10-14
fuente: "Mail \"Alcance AD Versión 74\" (Matías Alzogaray, 2026-10-09)"
producto: adquirencia
tema: AD V74 — alcance detallado por olas (tickets DAD↔AD) según la propuesta de Fintexa del 09/10; las fechas del mail quedaron superadas por la reunión del 13/10
tipo: conocimiento
destino_propuesto: 2_areas/procesos/publicaciones_mensuales.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Qué completa.** Este item da el **detalle de tickets** que le falta al item hermano de hoy, `2026-10-14_conocimiento-ad-v74-cronograma-staging-16-10-prod-22-10-liquidaciones-a-v75` (de `/sync_meetings`, reunión "Cerramos alcance AD" del 13/10). Ese item es **la fuente vigente para fechas y reparto**: V74 sale a staging el 16/10 y a producción el 22/10, y liquidaciones pasa a V75. También resuelve dos dudas de items anteriores: el ticket "3425" es DAD-3425 = AD-1837, y **DAT-2578 y DAT-3347 no figuran** en el alcance.

**Lo que decía el mail del 09/10 (superado):** el pase a PROD era el lunes 26/10 a la noche. Fintexa proponía sacar el módulo de liquidaciones y pasarlo en una versión intermedia la semana del 2 al 5/11, porque es lo más complejo, todavía tenía tickets en curso y no necesita pase nocturno. Según Fintexa, aunque cayera entre el 1 y el 10 del mes no traía problemas, porque solo afecta las rendiciones. El 13/10 se terminó mandando liquidaciones a V75. Que el reparto final por olas sea el de abajo **no está confirmado**, porque el resumen de la reunión no da el detalle por ticket. Por eso la confianza es media.

**Alcance propuesto (Fintexa DAD → Bind AD):**

*Ola 1, prioritarios*
- 1a, entrega individual: DAD-2304 / AD-1444, caché para SharedComisionesDB (throttling en convenios).
- 1b, liquidaciones (entrega única; **pasó a V75**): DAD-1893 / AD-1144, performance en la generación de archivos de liquidaciones · DAD-2215 / AD-1383, SISCRI: tiempos de liquidación con plazo = 0 · DAD-2280 / AD-1431, BOTONLIQ: la devolución parcial no se ve cuando la tarjeta se devuelve completa · DAD-3396 / AD-1803, discrepancia en LIQE-Entidad QRTR-3/8 · DAD-3400 / AD-1791, total a liquidar con devoluciones y desconocimiento en la misma liquidación · DAD-3418 / AD-1835, PDF de liquidación: arancel completo en cada devolución parcial · DAD-3425 / AD-1837, desconocimientos no registrados ni separados en la liquidación · DAD-3501 / AD-1932, PDF de liquidación: tratamiento de impuestos y desconocimientos · DAD-3525 / AD-1959, mejoras en la generación de archivos de rendición.

*Ola 2, webhooks (ronda única)*: AD-1273, webhook de Cobro QR con datos mal mapeados · AD-1416, POS: transacción rechazada con motivo = null en el webhook · AD-1633, el webhook de pago no informa CodigoProducto · AD-1634, el webhook de pago omite el array Productos cuando el código o la descripción son largos · AD-1629, BS2.0: webhook de QR con CodigoExterno entre comillas dobles · AD-1628, BS2.0: webhook de transferencia y tarjeta con codigoDeuda dentro de CodigoExterno.

*Ola 3, resto por bloque*
- Botón Simple 2.0 / Pago Fácil: AD-1149, actualizar medioDePago con CVU al asociarlo a la deuda · AD-1357, pagos con tarjeta y QR después del vencimiento no satisfacen la deuda · AD-1415, DevolucionDeuda registra mal las devoluciones simultáneas · AD-1461, no se informa NotRealized cuando falla el pago · AD-1513, Pago Fácil: contracargo acreditado en Coelsa figura RECHAZADO · AD-1679, alias de la cuenta visible en el checkout de Pago Fácil.
- POS / Prisma / Admin: AD-1341, QR desde POS duplica los productos asociados · AD-1386, propiedades adicionales guardadas dos veces en transacciones POS · AD-1456, el reporte de transacciones no trae la información completa · AD-1578, desasignar una entidad de un grupo de reglas afecta a otra entidad · AD-1449, POS ofrece cuotas en pagos con débito · AD-1643, no cambia la prioridad de procesadores (GP → Payway) · AD-1660, el alta de comercio con POS Prisma no genera el CVU · AD-1839, zona horaria incorrecta en las fechas de transacciones del Admin · AD-1844, un comercio que solo tiene Payway orquesta con GP · AD-1846, mensaje de error genérico sin parámetros Prisma para una marca.
- Cobro / Coelsa / Eco Cerrado: AD-1151, la devolución RxT debe responder IdContracargo e IdCoelsa · AD-1369, Eco Cerrado: el endpoint de contracargo no informa el motivo real del rechazo · AD-1457, RazonSocialComprador mal mapeada en RxT · AD-1498, Tienda Nube: transferencia saliente con tipo "recibida" · AD-1673, IdCoelsa en el comprobante de Cobro QR en Wallet · AD-1863, registrar el DEBIN al crearlo (carrera con el aviso de Coelsa) · AD-1937, insertar transacciones de botón de pagos al 09/09/26.
- Técnicos, solo QA de Fintexa: AD-1428, quitar el log override de EF Core en Shared.PagoExterno · AD-1427, logging INFO de request y response en Shared.PagoExterno.
- Pagos FX: AD-1738, alta de beneficiario: la fecha de expiración del DNI acepta texto.
- Sin testing: AD-1495, mapeo de 422 a 500 en PagoExterno, flujo QR · AD-1514, librería Zero-Downtime v74 · AD-1681, archivo TRIBBLEX-260831 vacío · DAD-3376 (sin AD), colas Quorum v74 · AD-1957, quitar referencias a la URL de apibank.

**Lectura PM:** con liquidaciones en V75 también quedan para V75 AD-1837 y AD-1791, que deberían cubrir los desconocimientos que siguen fallando después de V73. Ver `2026-10-14_conocimiento-adquirencia-desconocimientos-post-v73-defectos-liquidacion`.

> Fuente: Mail "Alcance AD Versión 74" — Matías Alzogaray (2026-10-09), a Nicolás Colón y Pablo Gomes, con copia a Emma Vignoles.
