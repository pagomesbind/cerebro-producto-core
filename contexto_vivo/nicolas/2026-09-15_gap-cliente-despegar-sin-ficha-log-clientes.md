---
id: 2026-09-15_gap-cliente-despegar-sin-ficha-log-clientes
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Reunión 'Daily producto' (2026-09-11)"
producto: wallet
tema: Cliente "Despegar" mencionado con caso de negocio activo (CBU corta, modelo PSI) sin fila en log_clientes.md
tipo: gap
destino_propuesto: "no aplica — para que /sync_customers lo levante en su próximo barrido de Notion"
tipo_destino: "no aplica"
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "Daily producto" (2026-09-11), Luciana Agostina Rudaz mencionó a **Despegar** como cliente al que "el banco le vendió el modelo PSI sin que esté en producción", y que se le asignará una CBU corta bajo un modelo similar al de Andina. No hay ninguna fila para "Despegar" en `2_areas/clientes/log_clientes.md` (200 clientes cargados desde Notion) — no está en ningún estado (producción, integración, negociación, frenado, etc.). Podría ser un cliente nuevo aún no cargado en Notion, o estar registrado bajo una razón social distinta.

No se propone ficha directamente (esta skill no toca `log_clientes.md`) — queda para que `/sync_customers` lo confirme en su próximo barrido de Notion.
