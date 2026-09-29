---
id: 2026-09-28_wallet_gap_fci_sin_endpoints_baja_rescate
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_meetings — reunión \"Producto\" (2026-09-28 14:12, compartida por evignoles), minuta Gemini"
producto: wallet
tema: "Fondos Comunes de Inversión (FCI) — sin endpoints automatizados para baja, rescate total ni eliminación de cuenta comitente; proceso 100% manual vía Soporte"
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "no — completa el inventario de superficie de la API Broker (Poincenot/IVSA) ya capturado el 2026-09-28 vía navegación del portal (`2026-09-28_wallet_api_broker_poincenot_pagos_cap_trading_fci`, `..._cuenta_remunerada_detalle`), que releva endpoints existentes pero no señalaba explícitamente esta ausencia operativa."
confianza: alta
estado: en_cola
merge_commit:
---

Pablo Gomes y Nicolás Colón discutieron en la reunión "Producto" la falta de puntos de interfaz (endpoints) automatizados para procesar bajas, rescates totales o la eliminación de cuentas comitentes de Fondos Comunes de Inversión (FCI). Actualmente estas acciones deben atenderse **de forma completamente manual, mediante soporte** — no existe ningún mecanismo self-service ni API para el cliente ni para Bind.

Próximo paso acordado (El grupo): establecer un procedimiento manual formal para la baja de inversiones, el rescate total y la eliminación de cuentas comitentes mientras no existan los endpoints automáticos, y evaluar si el volumen actual justifica el desarrollo de un punto de interfaz dedicado.

> Fuente: reunión "Producto", 2026-09-28 (`/sync_meetings`).
