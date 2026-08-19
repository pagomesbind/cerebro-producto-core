# Manifiestos de merge

Un archivo por cada corrida de `/context_merge`, nombrado `YYYY-MM-DD.md`. Cada uno documenta: qué items se ingirieron (de qué PM, a qué destino), qué permisos se pidieron sobre `2_areas/` no-ledger, qué contradicciones quedaron abiertas, y qué novedades cross-PM quedaron dirigidas a otro PM. Lo lee `/context_pull` desde cada instalación personal.

| Fecha | Items ingeridos | Pendientes | Notas |
|---|---|---|---|
| [2026-08-19](2026-08-19.md) | 39 (todos de pablo, en 2 corridas) | 0 | Corrida 1 (37 items): bug de `/context_push` detectado (items llegaron `capturado` en vez de `en_cola`) — sorteado con permiso del usuario, ver nota de proceso en el manifiesto. 2 permisos de régimen D otorgados. Corrida 2 (2 items): sin permisos ni contradicciones. |
