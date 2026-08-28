---
id: 2026-08-21_cliente_coto_fix_impuestos_qr_wallet
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Análisis de riesgos AD V72' (2026-08-21 14:02, docId 1cuABvOG3eEhMaN3XDQtF5ofpEqHmXewlt85OeXfC7EY)"
producto: adquirencia
tema: Coto — fix de cálculo de impuestos QR no debitados en cuentas de Wallet, semáforo amarillo por criticidad del cliente
tipo: conocimiento
destino_propuesto: wiki/2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

En el lote de despliegue de AD V72 (27/08/2026), el ticket 1458 corrige un caso donde no se debitaban correctamente en las cuentas de cliente los impuestos QR, por configuraciones previas en los comprobantes de Wallet. Matias Alzogaray y Maria Eugenia Vila lo clasificaron con **semáforo amarillo** (no verde, pese a ser un fix acotado) explícitamente por la **criticidad del impacto en clientes como Coto** — requiere controles postimplementación dedicados. Maria Eugenia queda a cargo de controlar el cálculo de impuestos QR/Wallet en base de datos tras el despliegue (ver próximos pasos de la reunión).

Contexto relacionado ya documentado: Coto es un cliente de riesgo/atención alta en Adquirencia — ver el bug histórico del archivo `BOTONLIQ` (2026-07-15) y la discrepancia de saldo por corte bancario (`detalle_productos/adquirencia/devoluciones_y_contracargos.md`) en su ficha actual.

> Fuente: Reunión "Análisis de riesgos AD V72" (2026-08-21), minuta Gemini — Detalles ([00:52:50]-[00:57:02]).
