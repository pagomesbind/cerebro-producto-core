---
id: 2026-09-22_conocimiento-ardid-transaction-no-recibe-bin-panlast4-hoy
pm: nicolas
fecha_captura: 2026-09-22
fuente: "Confirmación directa del PM durante /idea_solution sobre titularidad_tarjeta (2026-09-17)"
producto: Ardid
tema: El endpoint /Transaction del motor antifraude admite BIN y últimos 4 dígitos como campos opcionales, pero Bind hoy no los envía — solo el hash completo de la tarjeta
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/modulo_pagos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 72d6140
---

Durante el análisis técnico-funcional de `titularidad_tarjeta` se confirmó con el PM un detalle operativo real, no documentado hasta ahora: el endpoint `/Transaction` del motor antifraude (Ardid) tiene los campos `Bin` y `PanLast4` como opcionales en su contrato, pero **Bind PSP hoy no los envía en ningún caso** — solo se envía el hash completo de la tarjeta (campo `HASH`). Consecuencia práctica confirmada en el mismo análisis: el BIN y los últimos 4 dígitos de una tarjeta **no se retienen en ningún punto del flujo de pago más allá del momento en que se calcula ese hash** — se descartan inmediatamente después.

Esto es relevante para cualquier proyecto futuro que necesite datos truncados de la tarjeta (BIN, últimos 4, vencimiento) en el mismo flujo de pago: hoy no están disponibles "de rebote" en ningún llamado existente — hay que extraerlos explícitamente del número de tarjeta en el momento del pago, antes de que se descarten.
