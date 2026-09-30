---
id: 2026-09-29_conocimiento-liquidaciones-v74-criterios-y-observaciones-pago-unico
pm: nicolas
fecha_captura: 2026-09-29
fuente: "Reunión 'Análisis COBRO' (2026-09-28) — resumen del mail de Gemini (Drive no disponible, sin minuta detallada)"
producto: adquirencia
tema: Liquidaciones Cobro/Botón — criterios de aceptación validados con ejemplos rumbo a V74 (mostrar transacción y devolución en el comprobante, devolución de impuestos corregida en el ticket padre); observaciones de pago único AD-1845/AD-1849 declaradas no bloqueantes
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/desconocimientos_de_tarjeta.md
tipo_destino: actualizar
contradice: "no — continúa el item en_cola 2026-09-26_conocimiento-liquidaciones-ad73-definiciones-registro-y-regeneracion"
confianza: media
estado: ingestado
---

En "Análisis COBRO" del 28/09 (víspera del pase de AD V73) se repasaron los tickets prioritarios y los criterios de aceptación de las liquidaciones de Cobro/Botón. El equipo validó los criterios con ejemplos concretos de ventas y devoluciones.

**Definiciones:**
- **Transacción y devolución se muestran las dos en el comprobante** (PDF de liquidación). Confirma el comportamiento esperado de AD-1361 que motivó el defecto bloqueante AD-1822: una venta devuelta antes de liquidarse tiene que aparecer junto con su reversa, no solo la reversa descontada.
- Las correcciones de errores y la **devolución de impuestos** se detallaron en el **ticket padre**. No se aclara cuál: probablemente AD-1361. Está alineado con la regla de deducciones en reversas: impuestos y arancel se devuelven solo en reversa total del mismo día (item en_cola `2026-09-26_conocimiento-regla-deducciones-arancel-impuestos-en-reversas`).
- **AD-1845 y AD-1849** son observaciones sobre pagos de **pago único** y control de accesos/permisos. Se determinó que **no son bloqueantes** para la versión. Julieta Gimenez (Fintexa) va a dejar en el "ticket 15" y en los propios tickets un comentario con la justificación. La minuta habla de "tickets de dualidad", sin más contexto.
- **AD-1822** sigue abierto con un análisis nuevo de Daniela Collia (Fintexa) que Nicolás tiene que revisar.
- **AD-1856** se abre para **analizar y sanear el entorno**. Queda pendiente de que Producto lo asigne al equipo.
- Los scripts de implementación posteriores a la V73 necesitan la **aprobación del DBA**.
- Flavia Salmeron, Matías Alzogaray y "Luar" (nombre dudoso en la transcripción) se reúnen para ordenar el **tablero de observaciones de pagos** y cerrar lo que quede pendiente.
- El grupo arma, con un listado compartido en el chat, los tickets que entran en la **V74**.

> Fuente: Reunión "Análisis COBRO" (2026-09-28), resumen del mail de Gemini. Sin minuta detallada: el contenido exacto de los criterios validados (ejemplos numéricos) no está disponible. El prefijo "AD-" de los tickets se infiere del contexto (la minuta cita solo el número).
