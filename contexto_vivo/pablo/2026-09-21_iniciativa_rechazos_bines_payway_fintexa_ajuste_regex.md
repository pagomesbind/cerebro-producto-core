---
id: 2026-09-21_iniciativa_rechazos_bines_payway_fintexa_ajuste_regex
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reunión \"Análisis COBRO\", 2026-09-21"
producto: adquirencia
tema: PRD-251 — Fintexa se compromete a un ajuste temporal de payment_methods.json esta semana, posible vía de destrabe del bloqueante de producción
tipo: iniciativa
proyecto: PRD-251
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

Novedad puntual para la cartera de iniciativas: `rechazos_bines_payway` (PRD-251) sigue con el Frente A bloqueado en producción desde el 2026-09-21 (ver iniciativa previa del mismo día), pero Fintexa (Melisa Belpassi, Matias Sassa) se comprometió en la reunión "Análisis COBRO" (2026-09-21) a desarrollar, probar e implementar esta misma semana un ajuste temporal de las expresiones regulares del archivo frontend `payment_methods.json`, dejando a `IssuerIdentification`/Isure como fuente de verdad al confirmar el pago — posible vía de destrabe del bloqueante que impide aplicar el ticket AD-978, aunque todavía sin confirmación formal de que sea la respuesta a las 2 preguntas técnicas pendientes (T-115). Detalle completo en `1_proyectos/rechazos_bines_payway/gaps.md` y `proyecto.md` §7.
