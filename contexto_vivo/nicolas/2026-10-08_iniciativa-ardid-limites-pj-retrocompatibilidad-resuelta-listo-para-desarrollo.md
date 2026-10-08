---
id: 2026-10-08_iniciativa-ardid-limites-pj-retrocompatibilidad-resuelta-listo-para-desarrollo
pm: nicolas
fecha_captura: 2026-10-08
fuente: "Mail 'Asignacion de segmentos al crear la cuenta' — Martín Hovanyecz (Keep IT Simple) 2026-10-06 y 2026-10-07; respuesta del PM 2026-10-06"
producto: wallet
tema: PRD-263 (segmentación PJ en Wallet y Ardid) — retrocompatibilidad resuelta y documento funcional final v2; historias listas para desarrollo
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
proyecto: ardid_limites_pj
---

**Novedad de PRD-263 (Segmentación de clientes inicial en Wallet y Ardid, PJ).** Sigue al item `2026-10-06_iniciativa-ardid-limites-pj-pendientes-resueltos-y-retrocompatibilidad` (en_cola).

- **06/10. Retrocompatibilidad resuelta.** El PM aceptó la propuesta de Keep IT Simple: las Organizaciones que ya existían antes de la funcionalidad se pueblan con un **reproceso del alta completa ejecutado a mano vía Swagger por el equipo de Integraciones y Soporte de Bind PSP**. La herramienta entra en el alcance de DEM-2189. Esto revierte en parte la decisión del 23/09, que dejaba el backfill afuera de la puesta en producción.
- **Caso borde aceptado:** el Calculador de Costos no admite dos Segmentos con el mismo nombre, pero Wallet sí admite dos Organizaciones con el mismo nombre. En ese caso el alta de segmentos de la segunda fallaría siempre. No hay casos de negocio así, así que no frena.
- **06/10. Alcance nuevo propuesto:** Keep IT Simple propuso sumar también un **reproceso de cuentas** que hayan fallado en cualquier instancia del alta, para que Ardid, Wallet y el Calculador queden sincronizados en todos los flujos.
- **07/10. Documento funcional final v2 y pase a desarrollo.** Después del refinamiento de esa mañana, Keep IT Simple mandó el documento final con lo analizado y lo decidido (copia a Pablo Gomes y a Nicolás Pomponio de Fintexa) y pasó las historias a **listo para desarrollo**.
- **Por qué importa para la cartera:** el desarrollo arranca mientras la IDEA sigue EN APROBACION en Jira. Si el reproceso de cuentas quedó en el v2, es alcance que no estaba en las historias v1.8 ni en la estimación XL/15 SP. El PM tiene que confirmarlo (T-096).

> Fuente: Mail "Asignacion de segmentos al crear la cuenta" — Martín Hovanyecz (Keep IT Simple), 2026-10-06 y 2026-10-07; respuesta de Nicolás Colón, 2026-10-06.
