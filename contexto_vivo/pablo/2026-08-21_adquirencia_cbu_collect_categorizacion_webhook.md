---
id: 2026-08-21_adquirencia_cbu_collect_categorizacion_webhook
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Análisis de riesgos AD V72' (2026-08-21 14:02, docId 1cuABvOG3eEhMaN3XDQtF5ofpEqHmXewlt85OeXfC7EY)"
producto: adquirencia
tema: CBU Collect — cambio de categorización de transferencias entrantes desde CBU externo hacia CBU corto (webhook)
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/adquirencia/webhooks_y_notificaciones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

En el lote de despliegue de AD V72 (27/08/2026) se corrige la catalogación de las transferencias entrantes desde un **CBU externo hacia un CBU corto** en CBU Collect: hoy se registran/notifican como si fueran de CBU largo, y a partir de este cambio se van a registrar (y notificar por webhook) como `transfer.cortau` (`cortau receipt`).

**Es un cambio de contrato del webhook** — Matias Alzogaray advirtió explícitamente que puede afectar a entidades que controlan/filtran por ese campo de tipo, y mencionó como caso concreto al cliente **Jugadón** (Grupo Slots). Se acordó evaluar el impacto y avisar con anticipación a los clientes involucrados antes del pase (ver item de cliente asociado, `2026-08-21_cliente_jugadon_alerta_webhook_cbu_collect`).

> Fuente: Reunión "Análisis de riesgos AD V72" (2026-08-21), minuta Gemini — sección Decisiones, "Categorización de transferencias CBU" y Detalles ([01:09:40]).
