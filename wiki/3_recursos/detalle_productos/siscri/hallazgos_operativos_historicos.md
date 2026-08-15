# Hallazgos Operativos Históricos — Siscri

> Estado: mezcla de en producción (ya corregidos) y pendientes (marcado por ítem). Consolidado en la reestructuración PARA en cascada (2026-08-12) desde 2 archivos-cola de `detalle_productos/transversal/` (`dolores_soporte_y_administracion.md`, `mejoras_e_iniciativas_tecnicas.md`).

## Sincronización con comercios

- Actualizar SISCRI automáticamente cuando se actualiza un comercio (antes quedaban desincronizados).
- **Bug de dato hardcodeado**: cuando un Onboarding no informaba actividad económica, SISCRI daba de alta el comercio con provincia "Santa Fe" por defecto — bug silencioso de impuestos mal calculados por jurisdicción incorrecta.

## Certificados y reportes

- Generar certificados de retenciones para todas las entidades (Pendiente).
- Generar CSV para transferir a PMC.

## Spikes de investigación (mejoras técnicas)

- Spike de por qué no se creaban comercios ni entidades en SISCRI.
- Spike de reintentos fallidos de aviso de cálculo de impuestos por problemas de RabbitMQ.

---
*Fuente: Epics Notion "Dolores de Soporte y administración" y "Mejoras e Iniciativas Técnicas" — ingesta 2026-07-06.*
*Última actualización: 2026-08-12 — Creado en la reestructuración PARA en cascada, consolidando las secciones de Siscri de 2 archivos-cola de `detalle_productos/transversal/`.*
