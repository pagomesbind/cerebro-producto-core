---
id: 2026-09-28_iniciativa_pos_prisma_mastercard_rechazado_escalado
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_meetings — reunión \"Producto\""
producto: adquirencia
tema: confirmado que todas las transacciones con Mastercard son rechazadas en el canal POS con Prisma
tipo: iniciativa
proyecto: PRD-70
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Novedad puntual:** en el proyecto `prd-70_pos_prisma_finalizar/` (PRD-70, en go-live), Pablo Gomes confirmó mediante pruebas exhaustivas con distintos comercios que **todas las transacciones con Mastercard son rechazadas** en Prisma/Payway (T-118) — deja de ser un caso aislado de la entidad de prueba original, eleva la severidad del bloqueo para el go-live a un cliente real. Próximo paso: escalar formalmente a Payway con ayuda de Adri para determinar si es un problema de habilitación.
