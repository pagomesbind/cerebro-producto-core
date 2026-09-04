---
id: 2026-09-02_cliente-global66-latencia-qr-raiz-medicion-mfa-y-transferencias-no-acreditadas
pm: nicolas
fecha_captura: 2026-09-02
fuente: "Reunión \"Bind Global66, proximos pasos\" (2026-09-02)"
producto: wallet
tema: Reunión conjunta Bind/Global66 sobre latencia de Pagos QR — se acota la causa de la discrepancia de medición al lado de Global66; nuevo hallazgo de transferencias entrantes que no se acreditan pese a recibir el webhook correcto
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

Reunión conjunta Bind/Global66 (2026-09-02) — seguimiento del reclamo de latencia de Pagos QR ya trackeado en el proyecto `bajar-tiempos-pagos-qr` (PRD-199). Participantes: Mauro Suppan, Gonzalo Rivera, Nicolás Colón, Franco Gimenez, Emma Vignoles (Bind) y Marco Narvaez, Jonathan Castañeda, Alejandro Lopez Torres, Sebastián Díaz, Agustín Grau (Fintexa, invitado puntual) del lado Global66.

**Avance clave — se acota la causa de la discrepancia.** Bind mide de forma consistente ~6,7-7 segundos desde la creación de la operación hasta la actualización de estado (validado en vivo con un caso puntual: petición recibida y respondida en 6,8 segundos exactos, verificado por Agustín Grau contra logs de infraestructura). Global66 sigue midiendo 15-20 segundos del lado usuario. Al comparar timestamps de una misma operación, se identificó que la medición de Global66 arranca **antes** de que la petición llegue a Bind: Marco Narvaez reconoció que su equipo mide **desde que el usuario presiona el botón de MFA** para autorizar el pago, no desde que la petición sale hacia Bind. Conclusión de la reunión: la latencia adicional que reporta Global66 probablemente ocurre **en su propio flujo, antes de que la petición llegue al servidor de Bind** — queda como tarea de Global66 revisar internamente ese tramo (Marco Narvaez).

**Hallazgo nuevo — transferencias entrantes que no se acreditan pese a webhook correcto.** Por separado, Marco Narvaez reportó casos donde una transferencia figura como existente en el extracto pero no queda insertada/acreditada en el sistema de Global66 en el momento, obligando a una consulta posterior. Gonzalo Rivera y Nicolás Colón aclararon que Bind dispara el webhook únicamente cuando la transferencia ya tiene estado completado/rechazado en su base — por lo que el problema estaría del lado de Global66 al recibir o procesar ese webhook. Alejandro Lopez Torres quedó a cargo de revisar el flujo la próxima semana. **Nota de relación:** esto es un hallazgo separado del ya trackeado en `1_proyectos/tareas.md` T-018 (mapeo erróneo de transferencias salientes como recibidas, Agente de Cobros y Pagos) — mismo dominio (transferencias/webhooks) pero síntoma distinto (transferencias entrantes no insertadas del lado de Global66 vs. mapeo salientes→recibidas); a confirmar si comparten causa raíz cuando Alejandro Lopez Torres tenga el análisis.

**Cierre:** se acordó una reunión de seguimiento la semana del 2026-09-08 para revisar avances sobre latencia y acreditación de transferencias.

> Fuente: Reunión "Bind Global66, proximos pasos" (2026-09-02), minuta Gemini. Ver también proyecto `1_proyectos/bajar-tiempos-pagos-qr/proyecto.md` (actualizado directo con esta reunión).
