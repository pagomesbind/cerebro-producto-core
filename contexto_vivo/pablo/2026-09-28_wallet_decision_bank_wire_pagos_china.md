---
id: 2026-09-28_wallet_decision_bank_wire_pagos_china
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_meetings — reunión \"Producto\" (2026-09-28 14:12, compartida por evignoles), minuta Gemini"
producto: wallet
tema: Bank Wire (red Swift) adoptado como alternativa provisional para pagos en dólares a China, por restricción de Mastercard con el Banco de Shanghái
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 3492d04
---

Contexto: la operatoria de pagos en dólares a China se ejecuta hoy de forma manual, con dificultades porque el proveedor no envía notificaciones automáticas de cambio de estado. Mastercard homologa con el Banco de Shanghái en China, lo cual genera restricciones para procesar pagos en dólares por esa vía.

**Decisión acordada:** usar temporalmente **Bank Wire** (red Swift) como alternativa para pagos a China, con un costo de **USD 7,50 por transacción**, frente a los **USD 10** del instrumento tradicional (Bank Deposit) — mientras se resuelve la integración oficial de pagos FX para este destino.

Próximo paso (Pablo Gomes): configurar Bank Wire en el ambiente de pruebas (MTF) para validarlo antes de habilitarlo en producción, y solicitar la adenda contractual correspondiente (ver T-148 en `tareas.md`).

> Fuente: reunión "Producto", 2026-09-28 (`/sync_meetings`).
