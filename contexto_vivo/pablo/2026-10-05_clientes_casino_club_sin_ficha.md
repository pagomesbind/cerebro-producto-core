---
id: 2026-10-05_clientes_casino_club_sin_ficha
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_meetings — reunión 'Weekly - Producto / Operaciones', 2026-10-05 15:01, minuta Gemini (compartida, mnadalin)"
producto: transversal
tema: cliente Casino Club mencionado sin ficha en log_clientes.md
tipo: gap
destino_propuesto: 2_areas/clientes/log_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Cliente mencionado sin ficha:** Casino Club apareció en la reunión "Weekly - Producto / Operaciones" (2026-10-05) como cliente que hoy opera con Agente de Cobros y Pagos y necesita validar la titularidad de las transferencias que recibe (ver ítem relacionado `2026-10-05_agente_cobros_y_pagos_iniciativa_consulta_titularidad_casino_club`, mismo meeting). No figura en `wiki/2_areas/clientes/log_clientes.md` — no se pudo verificar contexto comercial previo (segmento, volumen, fecha de alta).

**Contexto de la mención:** Gonzalo Rivera explicó que Casino Club hoy valida la titularidad de quien transfiere antes de aceptar un pago (para asegurarse de que sea la misma persona), y que al pasar a Agente de Cobros y Pagos no van a tener CBU corta — operarían directo contra el agente, lo que hoy obligaría a darles dos credenciales distintas (poco prolijo).

Per regla de la skill (3a-bis): no se propone ficha nueva directamente — este gap es para que `/sync_customers` lo levante en su próximo barrido de Notion y confirme si ya existe como cliente comercial con otro nombre o segmento.
