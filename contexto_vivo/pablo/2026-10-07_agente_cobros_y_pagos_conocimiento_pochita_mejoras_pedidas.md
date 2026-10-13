---
id: 2026-10-07_agente_cobros_y_pagos_conocimiento_pochita_mejoras_pedidas
pm: pablo
fecha_captura: 2026-10-07
fuente: "/sync_mails — mail 'Mejoras Pochitaapp 07.10.26' (threadId 1a116d0481f09339), Maria Eugenia Vila, 2026-10-07"
producto: agente_cobros_y_pagos
tema: Mejoras pedidas a la herramienta interna "Pochita" — perfiles de acceso y filtros/exportación de liquidaciones
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/herramienta_pochita_liquidaciones.md
tipo_destino: actualizar
contradice: "no — complementa el item todavía en_cola 2026-10-06_agente_cobros_y_pagos_conocimiento_herramienta_pochita_liquidaciones (mismo destino, sin mergear todavía)"
confianza: alta
estado: en_cola
merge_commit:
---

María Eugenia Vila pidió a Ana María Moreno (desarrollo) una lista de mejoras puntuales para "Pochita" (la herramienta interna de administración de cuentas/liquidaciones que reemplaza el armado manual del archivo de liquidaciones — ver el item ya capturado el 2026-10-06 sobre su mecánica general, todavía `en_cola`). Mail corto, sin discusión adicional, en forma de lista de pedidos:

**Perfiles de acceso:**
- Agregar un perfil que solo tenga acceso a liquidación para poder generar el proceso — sin acceso a procesos, cuentas, etc. (hoy el acceso parece ser todo-o-nada).

**Liquidaciones:**
- Crear filtro por `CodEntidad`.
- Permitir exportar a CSV filtrando solo por producto, fecha de liquidación y fecha de negocio desde/hasta (o por código de entidad), sin necesidad de generar el proceso completo — para poder controlar las liquidaciones sin disparar la transferencia real.
- Agregar el `IdLiquidación` a la grilla (hoy no es visible ahí).

Sin fecha comprometida ni ticket de Jira asociado en este mail (herramienta interna sin tracking formal, mismo criterio que el item de 2026-10-06).

> Fuente: mail "Mejoras Pochitaapp 07.10.26" (threadId `1a116d0481f09339`), María Eugenia Vila → Ana María Moreno (Pablo Gomes en copia), 2026-10-07.
