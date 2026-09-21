---
id: 2026-09-03_adquirencia_gap_limites_pld_extracciones
pm: pablo
fecha_captura: 2026-09-03
fuente: "Reunión Análisis COBRO (2026-09-03 12:04), minuta Gemini"
producto: adquirencia
tema: límites transaccionales PLD para extracciones QR (Pago Fácil) sin especificar
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: pendiente
---

# Gap: Límites transaccionales PLD en extracciones QR

## Problema detectado (2026-09-03)
Durante la reunión de Cobro, Pablo GOMES mencionó que se están evaluando integraciones con Pago Fácil para cobros de facturas y **extracciones de efectivo mediante QR en sucursales**. Surgen requerimientos regulatorios de **PLD (Prevención de Lavado de Dinero)** que exigen:
- Separar operaciones de extracción de efectivo de pagos estándar
- Implementar **límites transaccionales** (por operación y acumulados mensuales por pagador)

**Severidad:** Media — Es un riesgo normativo que podría impactar la autorización regulatoria de la operación si no se implementa, pero todavía no hay IDEA ni ticket asignado.

## Inconsistencia con la wiki
No existe documentación actual en `detalle_productos/adquirencia/` sobre límites de PLD diferenciados para extracciones. El conocimiento sobre PLD/límites generales existe en `cumplimiento_normativo/`, pero no específico a Cobro QR extracciones.

## Contexto
- **Reunión:** Análisis COBRO, 2026-09-03
- **Participantes:** Pablo GOMES (menciona el requerimiento), Nicolás COLÓN (será responsable de documentarlo)
- **Ticket:** Nicolás COLÓN debe analizar requisitos técnicos de alcance

## Próximos pasos
[Nicolás COLÓN] Analizar y documentar requisitos técnicos de límites transaccionales PLD para extracciones QR  
[Compliance/Legales] Confirmar especificación exacta de límites por operación y acumulado mensual  
[PM] Crear IDEA o ticket si el alcance se confirma como necesario para H2 2026

## Actualización (2026-09-07)
Durante el armado del documento de integración técnica para Pago Fácil, el PM confirmó que **la separación de operatorias (pago de servicios vs. extracción) en comercios distintos es una definición estricta y ya vigente del área de Cumplimiento** — ver `2026-09-07_cumplimiento_separacion_comercios_extraccion_pago_pago_facil.md`. Eso cierra la primera mitad de este gap. Lo que sigue abierto: los **límites transaccionales numéricos** (por operación y acumulado mensual) para la operatoria de extracción — sin definición de Compliance/Legales todavía.

> Fuente: Reunión "Análisis COBRO" (2026-09-03 12:04), minuta Gemini. Cita: "Pablo Antonio GOMES menciona conversaciones comerciales para integrar el cobro de facturas y extracción de efectivo mediante QR en las sucursales de Pago Fácil. Se advierte sobre preocupaciones regulatorias de PLD que exigen separar operaciones de extracción de efectivo de pagos estándar e implementar límites transaccionales."
