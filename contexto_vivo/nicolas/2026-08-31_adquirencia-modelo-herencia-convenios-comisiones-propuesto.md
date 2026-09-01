---
id: 2026-08-31_adquirencia-modelo-herencia-convenios-comisiones-propuesto
pm: nicolas
fecha_captura: 2026-08-31
fuente: "Reunión \"Análisis COBRO\" (2026-08-27)"
producto: adquirencia
tema: Presentación de un modelo de herencia entidad→comercio para convenios/comisiones con excepciones a nivel comercio — posible resolución del gap ya documentado y en disputa
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/gestion_convenios_comisiones.md
tipo_destino: actualizar
contradice: "Revisar contra el gap ya documentado en gestion_convenios_comisiones.md (⚠️ en disputa con configuracion_de_entidades.md §4 y mejoras_admin_backoffice_prd88.md §2, escalado a 2_areas/gaps_y_preguntas.md) — este item podría ser la resolución de ese gap o una propuesta adicional todavía no confrontada con el contrato real de API ya documentado (Convenio maestro + ComercioConvenio con override opcional y flag FromCommerce)."
confianza: media
estado: en_cola
---

En la reunión "Análisis COBRO" (2026-08-27, con Daniela Collia/Fintexa, Pablo Gomes, Flavia Salmeron, Nicolás Colón) Pablo Gomes presentó un prototipo/propuesta de gestión de comisiones y plazos por medio de pago y canal, en reemplazo del concepto de "convenio" por configuraciones directas:

- Las **entidades** establecen parámetros generales (ejemplo: botón simple débito con 2% de comisión y 3 días de plazo) que se **heredan automáticamente** por los nuevos comercios que se crean bajo esa entidad.
- Al modificar un parámetro puntual en un comercio (ejemplo: cambiar la comisión de tarjeta de crédito de 1,3% a 99% en un comercio específico), se crea una **regla específica que prevalece sobre la entidad** para ese comercio. Al intentar desactivar esa regla puntual, el sistema alerta y ofrece volver al valor heredado de la entidad o desactivar el canal completo.
- Las modificaciones a nivel comercio **no impactan** a la entidad matriz ni a otros comercios (que mantienen su herencia intacta). Para un cambio global hay que modificarlo a nivel entidad: si se elimina un medio de pago en la entidad, los comercios sin excepciones lo pierden; los que tienen configuración propia la conservan.
- Daniela Collia advirtió que, aunque el panel visual muestra la edición de una sola línea, el backend genera un **nuevo registro por cada modificación** (crecimiento de datos, trazabilidad/auditoría). Pablo Gomes respondió que el volumen actual (~50 entidades operativas) mitiga el riesgo de escala y que los estados anulados conservan el historial.

**Por qué esto es relevante para el canon:** `gestion_convenios_comisiones.md` ya documenta el contrato real de API (modelo Convenio maestro + ComercioConvenio con override opcional y flag `FromCommerce`) y señala un gap "en disputa" sobre la herencia de convenios entidad→comercio (contradicción con `configuracion_de_entidades.md §4` y `mejoras_admin_backoffice_prd88.md §2`, escalada a `gaps_y_preguntas.md`). Esta reunión describe un modelo de herencia con excepciones que suena consistente con el flag `FromCommerce` ya documentado — pero no queda claro si es una re-explicación del mismo diseño existente o una propuesta nueva todavía no confrontada contra el contrato real de API. No resuelvo el gap: lo dejo capturado para que `/context_merge` lo confronte con el contenido ya existente y decida si cierra la disputa o la actualiza.
