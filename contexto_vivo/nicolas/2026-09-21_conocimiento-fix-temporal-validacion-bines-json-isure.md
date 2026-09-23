---
id: 2026-09-21_conocimiento-fix-temporal-validacion-bines-json-isure
pm: nicolas
fecha_captura: 2026-09-21
fuente: "Reunión 'Análisis COBRO' (2026-09-21)"
producto: adquirencia
tema: Fix temporal acordado para el desfase entre el JSON de validación de BINs del frontend y la base real de Isure
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/validacion_bines_tarjetas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
---

En la reunión "Análisis COBRO" (2026-09-21) se discutió el mecanismo actual de validación de tarjetas en Botón Simple: el sistema valida las tarjetas contrastando un **archivo JSON del frontend** (con ~90.000 números de identificación bancaria/BINs) contra la base de datos de **Isure**, lo que genera rechazos y discrepancias cuando ambas fuentes no coinciden. Matias Sassa (Fintexa) explicó que la validación en el JSON existe por motivos visuales históricos (mostrar si una tarjeta es débito/crédito antes de confirmar), pero entra en conflicto cuando no coincide con Isure, que es la fuente real usada al confirmar el pago.

Pablo Gomes fue explícito en que no se debe eliminar la funcionalidad visual del frontend ni permitir que pasen tarjetas inválidas, pero exigió una **solución rápida esta misma semana** para evitar pérdida de clientes por rechazos de tarjetas válidas, en paralelo a trabajar la solución de raíz.

**Decisión acordada:** Melisa Belpassi y Matias Sassa (ambos de Fintexa) se reunieron inmediatamente después de esta llamada para definir el fix — ajustar temporalmente las expresiones regulares del JSON del frontend, y que **Isure valide en el momento del pago** como fuente de verdad real. Se comprometieron a desarrollar, probar y desplegar esto en la semana, sin que las demoras del control de calidad externo (que recién empezó a probar Pagos FX el viernes anterior) actúen como bloqueante.

Este problema es el mismo trasfondo técnico del tema "BIN 6 vs. 8 dígitos" ya trackeado en `tareas.md` (T-055) desde el 2026-09-14 — la fase 2 de ese frente (ampliar de 6 a 11 dígitos la detección de BIN en POS/checkout) sigue sin fecha, mencionada como prioridad alta en la reunión "Weekly - Producto / Operaciones" del mismo día.

> Fuente: Reunión "Análisis COBRO" (2026-09-21), minuta Gemini.
