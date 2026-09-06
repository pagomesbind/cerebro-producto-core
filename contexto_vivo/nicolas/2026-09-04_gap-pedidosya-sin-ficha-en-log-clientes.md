---
id: 2026-09-04_gap-pedidosya-sin-ficha-en-log-clientes
pm: nicolas
fecha_captura: 2026-09-04
fuente: "Reunión \"Producto - Prioridades\" (2026-09-04)"
producto: transversal
tema: PedidosYa (PeYa) aparece como cliente activo con requerimientos de producto en curso (PRD-228/AD-1644, y discovery de norma 8432 ya documentado en detalle_productos/adquirencia/psp_as_a_service_normativa_8432.md), pero no tiene fila propia en 2_areas/clientes/log_clientes.md
tipo: gap
destino_propuesto: 2_areas/clientes/log_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

En la reunión "Producto - Prioridades" (2026-09-04), Luciana Rudaz gestionó un requerimiento activo de **PedidosYa (PeYa)** — arancel neto en cobro QR, PRD-228/AD-1644 (ver item de conocimiento relacionado de esta misma reunión). PeYa ya es un cliente con historia de discovery en el Cerebro: `3_recursos/detalle_productos/adquirencia/psp_as_a_service_normativa_8432.md` documenta la evaluación de modelos aceptador/agrupador bajo la norma 8432 BCRA hecha específicamente con este cliente.

Pese a esa actividad sostenida, no se encontró ninguna fila para "PedidosYa" ni "PeYa" en `2_areas/clientes/log_clientes.md` (verificado por búsqueda de texto sobre las ~200 filas del log). Mismo patrón que el gap de Pago Fácil/Western Union detectado el 2026-09-03 (ver `4_archivos/contexto_ingestado/` o el manifiesto correspondiente una vez mergeado) — puede ser que el legajo de Notion use otro nombre canónico, o que el cliente todavía no esté cargado en el barrido de `/sync_customers`. Se deja para que esa skill lo confirme en su próximo barrido — mientras tanto no corresponde proponer ficha nueva en `casos_de_uso_clientes.md` sin confirmar el cliente en el log maestro.

> Fuente: Reunión "Producto - Prioridades" (2026-09-04), minuta Gemini + cruce con `3_recursos/detalle_productos/adquirencia/psp_as_a_service_normativa_8432.md`.
