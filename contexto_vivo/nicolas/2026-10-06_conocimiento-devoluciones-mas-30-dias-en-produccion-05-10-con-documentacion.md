---
id: 2026-10-06_conocimiento-devoluciones-mas-30-dias-en-produccion-05-10-con-documentacion
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Mail 'Documentación Para Integraciones' — Melisa Belpassi (Fintexa), 2026-10-05 17:24"
producto: agente_cobros_y_pagos
tema: Devoluciones de más de 30 días por entidad — Fintexa anuncia el pase del 05/10 a las 21:15 y manda a Integraciones la documentación de configuración
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

Completa los items `2026-10-02_conocimiento-devoluciones-hasta-6-meses-por-entidad-ministerio-justicia` (en_cola) y `2026-10-06_conocimiento-devoluciones-mas-30-dias-ad-1948-config-bd-y-pase-ad-73-1` (capturado, de la reunión "RxT - Devolución de transacciones + 30 dias" del 05/10). El merge debería fusionar los tres en una sola actualización.

- **Pase anunciado, no confirmado.** A las 17:24 del lunes 2026-10-05, Melisa Belpassi (PM de Fintexa) avisó que la funcionalidad para configurar entidades que hagan **devoluciones de más de 30 días** "sale a producción hoy 05/10/2026 a las 21:15 hs". El mail es anterior al pase, así que no confirma que se haya hecho. La reunión del mismo día lo dejaba sujeto a la verificación de APIBank y a los errores de transferencias salientes.
- **Versión: el mail dice "71.3 de Adquirencia".** La reunión del mismo día habla de la **73.1** (AD-1948). Lo más probable es un error de tipeo en el mail (71.3 por 73.1), porque AD V73 ya salió el 29/09. El merge debería documentar 73.1.
- **Documentación para Integraciones.** El mail trae un PDF, `AD-Modificar entidad para que pueda devolver con plazo mayor a 30 días.-051026-182958.pdf`, con el procedimiento para configurar una entidad. Por el nombre, parece exportado del ticket AD (probablemente AD-1948). **No se descargó.** Puede responder lo que siguen sin cerrar los otros dos items: el nombre técnico de la especificación, si el plazo es fijo o configurable, si alcanza a QR y cómo es hoy la carga manual en la base.
- **Destinatarios:** Integraciones (Gonzalo Rivera), los 3 PM, Matías Alzogaray y Mariana Nadalin. Mariana Nadalin reaccionó al mail. Nadie hizo preguntas en el hilo.

> Fuente: Mail "Documentación Para Integraciones" — Melisa Belpassi, Fintexa (2026-10-05).
