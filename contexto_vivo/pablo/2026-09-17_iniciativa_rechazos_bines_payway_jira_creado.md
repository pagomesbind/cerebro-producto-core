---
id: 2026-09-17_iniciativa_rechazos_bines_payway_jira_creado
pm: pablo
fecha_captura: 2026-09-17
fuente: "/idea_jira — rechazos_bines_payway/"
producto: adquirencia
tema: Base de BINes desactualizada ante Payway — creación completa en Jira (Frente B/C)
tipo: iniciativa
proyecto: rechazos_bines_payway
pm_destino:
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: bc79f09
---

## Novedad — IDEA transicionada a EN APROBACION, Epic y 9 Historias creadas en Jira

`rechazos_bines_payway/` (Pablo Gomes) pasó de discovery/PRD a ticket de Ingeniería: la IDEA PRD-251 (ya existía en Jira desde el discovery, categoría BAU, producto Cobro, cliente SOPORTE) se transicionó de `DISCOVERY` a `EN APROBACION`, con prioridad subida a `High` y SP estimado cargado en 20 (estimación preliminar de Producto, Modo Historias, rango de riesgo 20–32). Epic AD-1712 creada en el espacio de Adquirencia con el análisis técnico-funcional completo en la descripción (contrato de integración, mapa de procedencia de datos, camino feliz, errores, máquina de estados, NFR de performance y gaps técnicos, con los 3 diagramas Mermaid embebidos). 9 Historias creadas en `Backlog`, todas asignadas al PM: corrección independiente de una regla de Mastercard mal configurada; ampliación de la resolución de tipo de tarjeta a precisión variable (6 a 11 dígitos, con un hallazgo nuevo — el contrato público hoy solo acepta 6 u 8 dígitos exactos, hay que ampliar esa validación); sus tres consumidores por separado (POS, motor de reglas, checkout de tarjeta no presente — este último bloqueado por una investigación externa pendiente); las tres operaciones de la vía de escritura sobre la base (alta/baja/modificación, sin un endpoint de aplicación en lote — descartado por uso poco frecuente); y el registro de casos de número no encontrado con su canal de origen, para que Soporte y Fraude puedan monitorear por primera vez de forma agregada.

Este proyecto ya tenía una acción operativa urgente ejecutada por fuera de Jira (carga masiva de ~89.700 números de tarjeta sin ambigüedad, vía ticket directo al proveedor tecnológico Fintexa) — esa parte no generó desarrollo ni historia, y ya resolvió el 54,3% de los rechazos y el 66,1% del monto medidos en agosto para el cliente de mayor impacto (Grupo DESA).

> Fuente: `1_proyectos/rechazos_bines_payway/proyecto.md §7/§9`.
