---
id: 2026-09-03_adquirencia_webhook_pagos_qr_decimales
pm: pablo
fecha_captura: 2026-09-03
fuente: "Reunión Análisis COBRO (2026-09-03 12:04), minuta Gemini"
producto: adquirencia
tema: webhook pagos QR — inclusión comisiones Coelsa con preservación de decimales
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_webhook_cobro.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: f230716c54a5ca6600a2bce4e46bf0292d56a58c
---

# Inclusión de comisiones en webhook de pagos QR

## Decisión acordada (2026-09-03)
Se acordó incluir las comisiones de Coelsa directamente en el webhook de pagos QR (aprobados/rechazados), manteniendo la cantidad original de decimales (7) que proporciona Coelsa.

**Motivo:** Actualmente, el webhook solo envía el importe neto; las entidades deben consultar comisiones por otra vía. Centralizar esta información en el webhook mejora la conciliación y evita consultas adicionales.

**Impacto:** El campo de comisiones en el webhook de Cobro QR / Pagos QR facilitará cálculos de rentabilidad en las billeteras y portales de administración.

## Detalles técnicos
- **Campo nuevo:** comisiones de Coelsa en webhook (mantener 7 decimales)
- **Alcance:** Solo webhooks de pagos **aprobados y rechazados**, no devoluciones (que tienen endpoint separado)
- **Formato:** Decimales completos de Coelsa (7 dígitos), no truncar a 2

## Próximos pasos
[Daniela Collia/Fintexa] Confirmar especificación de decimales con documentación de Coelsa  
[Nicolás COLÓN] Implementar inclusión en webhook tras confirmación

> Fuente: Reunión "Análisis COBRO" (2026-09-03 12:04), minuta Gemini
