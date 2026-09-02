---
id: 2026-08-31_wallet-reintento-automatico-alias-error-apibank
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"Weekly - Producto / Operaciones\" (2026-08-31)"
producto: wallet
tema: Reintento automático en la creación de alias de cuenta ante error de APIBank
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/validaciones_y_alias_cvu.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

En la reunión "Weekly - Producto / Operaciones" (2026-08-31), Pablo Gomes informó que se implementó un **reintento automático en la creación de alias de cuenta** cuando la operación recibe un error de APIBank, con el objetivo de mitigar los fallos frecuentes de este proceso ("error frecuente en asignación de alias de cuenta automático" — descripto como una regresión nueva, no un error histórico: "antes andaba bien"). No se detalló el mecanismo del reintento (cantidad de intentos, backoff) más allá de la mención en la reunión — a confirmar contra el ticket/desarrollo real si se necesita el detalle técnico.

Complementa la mecánica de alias ya documentada en el archivo destino (ventana de 5s de Coelsa para asignación, bloqueo de reasignación de 24hs, fix de reintento de 700ms para un caso puntual — MDA-292391/Banco Industrial): este es un reintento distinto, a nivel de creación de alias ante error de APIBank, no el mismo mecanismo.
