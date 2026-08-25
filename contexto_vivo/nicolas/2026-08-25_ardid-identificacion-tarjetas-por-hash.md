---
id: 2026-08-25_ardid-identificacion-tarjetas-por-hash
pm: nicolas
fecha_captura: 2026-08-25
fuente: "Reunión \"ARDID\" (2026-08-24), minuta + transcripción Gemini"
producto: ardid
tema: Identificación de tarjetas en Ardid — hash de los 16 dígitos completos, no DNI ni coincidencia parcial
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/modulo_pagos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

En la reunión "ARDID" (2026-08-24), Nicolás Colón le aclaró a Rocío Revelli (Soporte) el criterio real de identificación de tarjetas que usa Ardid, a raíz de una consulta de un cliente (Maru, vía Payway) sobre una tasa alta de rechazos que atribuía a límites diarios por tarjeta.

**Decisión/definición acordada:** la identidad de una tarjeta en Ardid se determina **únicamente por el hash de los 16 dígitos completos** del número de tarjeta — nunca por el DNI del pagador, ni por coincidencia parcial de los primeros seis/últimos cuatro dígitos (formato típico que entregan los procesadores como Payway). Dos operaciones con los mismos primeros/últimos dígitos pero distinto tramo medio son, para Ardid, tarjetas distintas con hashes distintos — y por lo tanto las reglas de límite diario (ej. "máximo 3 pagos por día") se evalúan por hash, no por esos datos parciales. En la sesión se validó esto en vivo contra Mongo (vía Cosmos Connect, colección `transaction`): al filtrar por el hash real de una tarjeta puntual solo aparecieron 2 operaciones en ~45 días de retención, mientras que el archivo que había armado Payway con datos parciales mostraba muchas más operaciones "coincidentes" que en realidad correspondían a tarjetas distintas (confirmado además por DNIs y emails distintos entre esas operaciones).

**Dato adicional relevante:** el DNI y el email que se cargan en el botón de pagos son datos de completado libre (no hace falta que sean del titular de la tarjeta/deuda) — no se usan para la identidad de la tarjeta. Ardid sí tiene una función para validar que una tarjeta, la primera vez que se usa, quede asociada a un DNI y exigir que las siguientes veces venga con el mismo DNI — pero está **deshabilitada** para evitar bloqueos por errores de tipeo del usuario final. Nicolás Colón mencionó un proyecto próximo provisto por Modo que permitirá validar los 16 números de tarjeta contra el DNI de la persona usuaria.

> Fuente: Reunión "ARDID" (2026-08-24), minuta + transcripción Gemini.
