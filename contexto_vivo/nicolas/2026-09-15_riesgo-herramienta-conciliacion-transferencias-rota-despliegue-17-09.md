---
id: 2026-09-15_riesgo-herramienta-conciliacion-transferencias-rota-despliegue-17-09
pm: nicolas
fecha_captura: 2026-09-15
fuente: "Reunión 'W 72.3 (Pagos FX) y Modificaciones en los Proxys de PRD - Análisis de riesgos' (2026-09-11)"
producto: wallet
tema: Herramienta de conciliación de transferencias entrantes rota — riesgo agravado por el despliegue de proxy/wallet del 17/09
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: PENDIENTE
---

**Fuente:** reunión "W 72.3 (Pagos FX) y Modificaciones en los Proxys de PRD - Análisis de riesgos" (2026-09-11).

Maria Eugenia Vila advirtió que la herramienta que concilia transferencias entrantes está **rota**: hoy el proceso de conciliación depende de que alguien busque manualmente las transferencias y las inserte a mano (no hay automatismo). Pablo Antonio Gomes confirmó: *"tenemos roto una herramienta que concilie... no tendríamos la herramienta para actuar si pasa eso."*

**Por qué es relevante ahora:** el despliegue programado para el jueves 17/09 (actualización de proxy 7:00am + wallet/Pagos Efex 72.3 8:00am) puede generar intermitencias en el tráfico de ingress. Si durante esa ventana se pierden avisos de transferencias entrantes, **no hay herramienta para detectarlo ni resolverlo manualmente** — el riesgo concreto es que transferencias entrantes no se acrediten y los clientes reclamen saldos faltantes, sin que el equipo tenga forma de detectarlo proactivamente.

**Estado:** Gonzalo Damian Rivera pidió el caso (MDA) para tomarlo de inmediato; se acordó no comunicar nada a clientes salvo el aviso estándar de mantenimiento preventivo durante la ventana del despliegue.
