---
id: 2026-09-03_adquirencia-fix-contracargo-query-id-referencia-tx-cliente-ripsa
pm: nicolas
fecha_captura: 2026-09-03
fuente: "Reunión \"Analisis de riesgo - Fix Contracargo\" (2026-09-03)"
producto: adquirencia
tema: Fix del ticket AD1639 — timeout al hacer contracargo desde el portal por una query que busca por un ID de referencia de transacción demasiado grande (guarda el stream completo del QR)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Analisis de riesgo - Fix Contracargo" (2026-09-03) se presentó y aprobó el fix del ticket **AD1639**: al intentar hacer un contracargo desde el portal, la operación fallaba con **timeout** y el contracargo no quedaba registrado (no se podía confirmar si se había procesado, cancelado o quedado en estado intermedio). Nicolás Colón explicó la causa raíz encontrada al revisar la consola del navegador (F12): la consulta buscaba por el **ID de referencia de transacción**, un dato que almacena el **stream completo del código QR** (ID de transacción de QR + el stream del QR en sí) — un valor demasiado grande que hacía tirar timeout a la búsqueda. El fix consistió en mejorar esa consulta puntual para que no falle al hacer el contracargo.

Matias Sassa aclaró que el cambio **solo afecta el `GET` filtrado por ID de referencia de transacción**, y no toca el `GET` general por ID de deuda (son dos queries distintas, aunque bifurcadas del mismo origen) — por lo que no hay riesgo de impacto colateral sobre el componente de deuda pese a que el despliegue coincidió con día 2-3 del mes (plena época de vencimientos). Andrea Orsini validó con pruebas exitosas de botón 2.0, pagos QR de deuda individuales, y contracargos parciales/totales antes del pase.

El caso concreto que disparó el ticket fue el cliente **Ripsa**, que no podía hacer devoluciones desde el admin — Franco Gimenez confirmó que, según lo que había visto, el problema afectaba únicamente a este caso particular (no a todos los contracargos), aunque Nicolás Colón señaló la duda abierta de si, al ser un problema de fondo en la query, podría haber otros clientes con el mismo síntoma sin haberlo reportado todavía.

> Fuente: Reunión "Analisis de riesgo - Fix Contracargo" (2026-09-03), minuta Gemini.
