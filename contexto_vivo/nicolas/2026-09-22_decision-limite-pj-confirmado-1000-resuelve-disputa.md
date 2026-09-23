---
id: 2026-09-22_decision-limite-pj-confirmado-1000-resuelve-disputa
pm: nicolas
fecha_captura: 2026-09-22
fuente: "Reunión \"Ardid - Persona Jurídica\" (2026-09-21), con Rocío Revelli y Pablo Gomes"
producto: ardid
tema: Resolución de la disputa de monto ($1.000 vs $10.000) para el límite operativo de cuentas de persona jurídica sin documentación
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no — resuelve el gap ya archivado 2026-09-10_gap-contradiccion-limite-operativo-personas-juridicas-1000-vs-10000 (wiki/4_archivos/contexto_ingestado/)"
confianza: alta
estado: ingestado
---

Desde el 2026-09-09 había quedado sin resolver una disputa de monto: la decisión ya en el canon (`direccion/decisiones.md`, entrada 2026-09-08) fija el límite operativo de cuentas de persona jurídica sin documentación en **$1.000**, pero dos reuniones independientes del 2026-09-09 ("ARDID" y "Join Soporte Clientes") citaban en cambio **$10.000** — capturado como gap y ya archivado (`2026-09-10_gap-contradiccion-limite-operativo-personas-juridicas-1000-vs-10000`).

**Resolución (reunión "Ardid - Persona Jurídica", 2026-09-21):** Rocío Revelli y Pablo Gomes confirmaron el monto definitivo: **$1.000**, hasta que el cliente presente la documentación requerida por PLD. Es el mismo valor que ya estaba en el canon desde el 2026-09-08 — la cifra de $10.000 de las reuniones del 09-09 queda descartada como error de transcripción o versión provisional superada.

**Contexto adicional aportado por Pablo Gomes en la misma reunión:** volumen real de altas de personas jurídicas es bajo (7-39/mes, pico 108), concentrado en el cliente Consorcio Abierto. Ya existe un precedente de límite excepcional otorgado a Octagon ($300.000.000 vs. los $25.000.000 estándar de personas físicas) — mismo criterio UIF/ROS que la decisión ya documentada en el canon del 2026-07-29.

Este límite de $1.000 se implementa técnicamente como el `ClientBankType` restrictivo de persona jurídica en Ardid, dentro del proyecto `ardid_limites_pj` (`wiki/1_proyectos/ardid_limites_pj/`).

> Fuente: reunión "Ardid - Persona Jurídica" (2026-09-21), documentada en `wiki/1_proyectos/ardid_limites_pj/proyecto.md` §5/§9 y `decisiones.md`.
