---
id: 2026-09-08_conocimiento-facard-cu-collect-pago-unico-y-modo-completado
pm: nicolas
fecha_captura: 2026-09-08
fuente: "Mail \"Análisis COBRO: Lun, 7 de sept de 2026 a las 12:00pm – 1:00pm (GMT-03)\" — malzogaray@bind.com.ar (2026-09-07)"
producto: adquirencia
tema: Requerimiento de Facard (PRD-235/ticket 1512) de pago único vía CU Collect/Botón Simple 2.0 mantenido en máxima prioridad; integración con MODO confirmada completa
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: d7e1ccf
---

En "Análisis COBRO" (2026-09-07) se repasó el requerimiento del cliente **Facard** (ticket 1512 / PRD-235) para la funcionalidad de **CU Collect y Botón Simple 2.0 de pago único** — decisión: se mantiene en máxima prioridad en el colector del equipo dado su nivel avanzado de desarrollo. La historia de usuario 1512 ya fue enviada por Nicolás Colón a Mati (Fintexa) el 2026-09-07 (action item marcado "Enviada", sin seguimiento pendiente).

**Corrección (2026-09-07, misma corrida):** "Facard" no matchea ningún cliente de `2_areas/clientes/log_clientes.md`. El nombre real casi con certeza es **FAVACARD** (POS, Botón de Pago, QRI — Adquirencia, ficha ✅ en `casos_de_uso_clientes.md`), consistente con el mismo cliente mencionado como "Fabacar" en la reunión "Weekly - Producto / Operaciones" del mismo día (convivencia de reporter con botón simple, mismo tema de PRD-235/ticket 1512) — mismo patrón de error de transcripción de Gemini ya visto con otros nombres de cliente. Reemplazar "Facard" por FAVACARD al mergear a `boton_simple_2_0.md`.

Además, se confirmó que los trabajos vinculados a la integración del **proyecto MODO** (QR Tarjeta — pago con tarjeta desde wallets terceras, ya documentado en `boton_simple_2_0.md`) **se encuentran completados**.

> Fuente: Mail "Análisis COBRO: Lun, 7 de sept de 2026 a las 12:00pm – 1:00pm (GMT-03)" — malzogaray@bind.com.ar (2026-09-07).
