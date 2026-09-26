---
id: 2026-09-26_conocimiento-ardid-1-19-pase-staging-29-09-riesgo-amarillo
pm: nicolas
fecha_captura: 2026-09-26
fuente: "Reunión 'Análisis de riesgo - Ardid V 1.19.0' (2026-09-25, ~16:00) — solo resumen + próximos pasos del mail de Gemini (Google Drive invalidado, sin minuta detallada ni transcripción)"
producto: ardid
tema: Ardid 1.19.x — pase a staging agendado martes 29/09 8-10hs (riesgo amarillo, separado del pase de Wallet a staging del lunes 28/09 9-11hs); el título de la reunión dice "V 1.19.0" pese a la decisión del 22/09 de saltar directo a la 1.19.1
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/ardid/historico/historial_versiones.md
tipo_destino: actualizar
contradice: "3_recursos/detalle_productos/ardid/historico/historial_versiones.md — 'Decisión (22/09/2026, \"Repaso Semanal líderes\"): se salta directo a esta versión [1.19.1], omitiendo la 1.19'. La reunión de análisis de riesgo del 25/09 se titula 'Ardid V 1.19.0'. Puede ser solo el nombre del evento (versión mayor/menor) y no la versión efectiva — no verificable sin la minuta detallada."
confianza: media
estado: en_cola
---

**Análisis de riesgo del pase de Ardid 1.19.x a staging (ambiente de pruebas) — reunión del 2026-09-25.**

> Fuente: Reunión "Análisis de riesgo - Ardid V 1.19.0" (2026-09-25), resumen del mail de Gemini. Drive no disponible: no se leyó la minuta detallada.

Qué se definió:
- **Fechas de pase a staging separadas para no superponer despliegues:**
  - **Wallet → staging: lunes 28/09, 9 a 11 hs.**
  - **Ardid 1.19.x → staging: martes 29/09, 8 a 10 hs.**
  - Ventana estimada de **~2 horas** por pase, incluyendo las pruebas de regresión en staging.
  - Se avisa a los clientes del mantenimiento y de la posible intermitencia del ambiente de pruebas en esos horarios (acción grupal).
- **Riesgo del despliegue clasificado como AMARILLO**, con planes de rollback revisados.
- **Alcance funcional mencionado:** la versión trae **nuevas reglas de pagos y de comercios** — Rocío Revelli arma un set de pruebas específico para validar su impacto. (El canon atribuye las "reglas interentidades" a la 1.20; no queda claro si estas reglas son las mismas u otras — a confirmar.)
- **API externa:** Luis hace un repaso exhaustivo para confirmar que **no hay cambios en los endpoints de la API externa** de Ardid y reporta cualquier hallazgo.
- **Hotfix de producción pendiente:** Osmel Mata (Fintexa, SRE) envía por mail la consulta pendiente sobre fecha y horario de un hotfix de producción (sin más detalle en el resumen; posible relación con el parche manual de `PENDING` de `despliegues_y_operacion.md` §3, no confirmado).

Seguimiento: Andrea Orsini ejecuta las regresiones de Wallet y Ardid tras cada pase (flujos de servicios y botones); Matías Alzogaray distribuye la minuta con el plan de acción post pase a staging.

**Pendiente de aclarar (ver `contradice`):** si la versión que se sube a staging el 29/09 es la 1.19.0 o la 1.19.1 (la que trae el fix UTC 0, según la decisión del 22/09). También si la fecha de Wallet (28/09) es la V73 de Wallet — cuyo pase a producción se corrió a "el 8" según el item `2026-09-25_conocimiento-v73-adquirencia-y-wallet-reprogramadas` — y si "martes 29/09 8-10hs" en staging choca con el pase a producción de AD V73 del mismo martes a las 20:30 (no se superponen en horario).
