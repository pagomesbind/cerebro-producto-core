---
id: 2026-09-03_adquirencia_webhook_alcance_devoluciones
pm: pablo
fecha_captura: 2026-09-03
fuente: "Reunión Análisis COBRO (2026-09-03 12:04), minuta Gemini"
producto: adquirencia
tema: webhook pagos QR — alcance limitado a aprobados/rechazados, endpoint separado para devoluciones
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_webhook_cobro.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
---

# Separación de endpoint: webhook de pagos vs. devoluciones

## Decisión acordada (2026-09-03)
Se acordó que el webhook de pagos QR Tarjeta quede limitado a notificaciones de **pagos aprobados y rechazados solamente**. Un nuevo endpoint separado será creado **específicamente para procesar devoluciones**, ya que la lógica de negocio es distinta y no puede reutilizar el flujo existente.

**Motivo:** La lógica actual del webhook no contemplatxiones de devoluciones por diseño. Las devoluciones son reembolsos posteriores al pago y requieren un tratamiento administrativo diferente (ticket 361, relacionado al 2209).

**Impacto:** Simplifica la lógica del webhook principal; las devoluciones se canalizan por su propia vía sin contaminar el flujo de pagos.

## Detalles técnicos
- **Webhook principal:** pagos aprobados + pagos rechazados (sin devoluciones)
- **Endpoint nuevo:** procesar devoluciones QR Tarjeta (scope separado)
- **Relacionado:** Ticket 361 (diferenciación "desconocimiento" vs. "devolución" en PDF de liquidaciones para Coto)

## Próximos pasos
[Nicolás COLÓN] Crear endpoint nuevo para devoluciones  
[Nicolás COLÓN] Validar alcance con Gono (cambios en configuración de canales para QR Tarjeta)

> Fuente: Reunión "Análisis COBRO" (2026-09-03 12:04), minuta Gemini
