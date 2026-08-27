---
id: 2026-08-21_cliente_jugadon_alerta_webhook_cbu_collect
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Análisis de riesgos AD V72' (2026-08-21 14:02, docId 1cuABvOG3eEhMaN3XDQtF5ofpEqHmXewlt85OeXfC7EY)"
producto: adquirencia
tema: Jugadón (Grupo Slots) — riesgo de ruptura por cambio de categorización del webhook de CBU Collect en AD V72
tipo: conocimiento
destino_propuesto: wiki/2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

En la reunión de riesgo de AD V72 (27/08/2026), al revisar el cambio de categorización de transferencias entrantes de CBU externo→CBU corto en CBU Collect (pasan a notificarse como `transfer.cortau` en vez de CBU largo — ver item de producto asociado), Matias Alzogaray mencionó específicamente a **Jugadón** (marca de Grupo Slots, RxT fondea el saldo virtual del jugador) como cliente que podría verse afectado si filtra/valida por ese campo de tipo en el webhook. Se acordó evaluar el impacto puntual y avisarle con anticipación antes del pase a producción del 27/08.

A la fecha de esta captura no hay confirmación de que la evaluación/aviso ya se haya hecho — a sumar a "Particularidades / cronología" de la ficha de Jugadón como alerta abierta, no como hecho cerrado.

> Fuente: Reunión "Análisis de riesgos AD V72" (2026-08-21), minuta Gemini — Detalles ([01:09:40]).
