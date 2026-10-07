---
id: 2026-10-06_adquirencia_conocimiento_rollback_v731_devoluciones_transferencia
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_meetings — reunión 'Repaso Semanal líderes' (2026-10-06 10:59, compartida evignoles), minuta Gemini"
producto: adquirencia
tema: Rollback de la versión 73.1 de adquirencia — devoluciones por transferencia en estado "fail" automático
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/devoluciones_y_contracargos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

Se debió hacer un rollback de la versión 73.1 de adquirencia la noche del 2026-10-05→06. Melisa Belpassi (Fintexa) explicó que las devoluciones por transferencia daban error de forma automática en estado "fail", mientras que los pagos con QR y tarjeta funcionaron correctamente (el rollback afectó específicamente el circuito de devolución por transferencia, no todo el despliegue). Andrea Orsini señaló que el fallo ocurrió con una cuenta específica, aunque a la mañana siguiente esa misma cuenta operó con normalidad — dato que apunta a una causa transitoria/puntual, no un bug determinístico reproducible en el código.

**Causa raíz real, según Gonzalo Damian Rivera (no corregida en el momento):** el error no se revisó directamente en Coelsa antes de decidir el rollback. Rivera señaló que Coelsa indicaba un problema de acreditación en el banco destino (del lado de la transferencia bancaria, no un fallo de código del lado de Bind/Fintexa). Andrea Orsini y Gonzalo Rivera reconocieron una falta de conocimiento operativo sobre el circuito de transferencias en el equipo que tomó la decisión. Matías Alzogaray y Andrea Orsini concluyeron que el rollback se decidió bajo presión de tiempo y cansancio (guardia nocturna), sin mala intención, pero evidenciando una brecha operativa real.

**Estado al cierre de la reunión (2026-10-06):** el redespliegue de la versión 73.1 sigue pendiente — alta prioridad exigida por Gupra (cliente/stakeholder mencionado sin más contexto en la minuta). Melisa Belpassi quedó a cargo de verificar la disponibilidad de la API financiera para definir si el redespliegue se ejecuta de día o de noche (junto con una actualización de seguridad), e informar al equipo el horario definitivo — sin fecha/hora confirmada todavía al cierre de esta reunión.

> Fuente: reunión "Repaso Semanal líderes" (2026-10-06), minuta Gemini. Participantes citados: Melisa Belpassi, Andrea Orsini, Gonzalo Damian Rivera, Matías Alzogaray.
