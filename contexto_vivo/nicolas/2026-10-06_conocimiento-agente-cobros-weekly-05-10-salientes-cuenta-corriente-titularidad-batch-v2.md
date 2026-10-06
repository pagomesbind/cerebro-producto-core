---
id: 2026-10-06_conocimiento-agente-cobros-weekly-05-10-salientes-cuenta-corriente-titularidad-batch-v2
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Reunión \"Weekly - Producto / Operaciones\" (2026-10-05), solo resumen del mail de Gemini (Drive invalidado, sin minuta completa)"
producto: agente_cobros_y_pagos
tema: Frentes abiertos del Agente de Cobros y Pagos al 05/10 — corrección de transferencias salientes, mejoras de cuenta corriente y movimientos, consulta de titularidad, archivos batch v2, consulta de ID contra Coelsa
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

**Estado al 2026-10-05 de los frentes del Agente de Cobros y Pagos ("Core Pagos" en la minuta):**

- **Transferencias salientes.** Hay una corrección en curso de las transferencias salientes. Falta confirmar si quedó resuelta o si siguen los problemas. Seguimiento a cargo de Nicolás Colón. Se relaciona con el mapeo erróneo de salientes como recibidas (T-018) y con los errores de salientes que aparecieron en pruebas antes del pase de la 73.1 (ver item `2026-10-06_conocimiento-devoluciones-mas-30-dias-ad-1948-config-bd-y-pase-ad-73-1`).
- **Obtener cuenta corriente y movimientos.** Hay mejoras pendientes de cierre sobre los servicios de consulta de cuenta corriente y de movimientos (Nicolás Colón).
- **Consulta de titularidad para agentes de cobros y pagos.** Se va a implementar a partir de un **mapeo ya hecho** (Nicolás Colón). La "consulta de cuentas" del agente de cobros pasa a gestionarla **Luciana Rudaz**, con el ticket asignado a ella.
- **Archivos batch v2.** Pablo Gomes analiza actualizar los archivos batch a una **versión 2** que sume los **datos del pagador**, que hoy faltan en los reportes.
- **Consulta de ID contra Coelsa.** Pablo Gomes evalúa implementar una consulta por ID contra Coelsa. El objetivo es acortar los tiempos de resolución cuando falla el banco (caídas de APIBank). La minuta no aclara si se aplica a salientes, a entrantes o a ambas. Si es para entrantes, se cruza con el proyecto `conciliacion_entrantes` (PRD-240).
- **Conciliación y contracargos.** La minuta dice "eliminar la conciliación manual diaria" y "extender contracargos hasta octubre", sin más contexto. No queda claro qué conciliación ni qué se extiende (¿un plazo? ¿una vigencia?). Hay que confirmarlo antes del merge.
- **Alias.** Pablo Gomes cierra el reporte sobre la corrección de un error frecuente en la asignación de alias.
- **Bajas de cuentas.** Mariana Nadalin coordina con "Ro" (probablemente Rocío Revelli) bajas y ajustes de cuentas pedidos por mail.

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-10-05), resumen del mail de Gemini.
