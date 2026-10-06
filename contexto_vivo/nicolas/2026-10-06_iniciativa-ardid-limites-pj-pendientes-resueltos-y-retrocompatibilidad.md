---
id: 2026-10-06_iniciativa-ardid-limites-pj-pendientes-resueltos-y-retrocompatibilidad
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Hilo de mail 'Asignacion de segmentos al crear la cuenta' — respuesta de Nicolás Colón (2026-10-02 17:47) y de Martín Hovanyecz, Keep IT Simple (2026-10-05)"
producto: ardid
tema: PRD-263 — el PM resolvió los pendientes del análisis funcional final; Keep IT Simple propone un reprocesamiento manual vía Swagger para las Organizaciones preexistentes
tipo: iniciativa
proyecto: ardid_limites_pj
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
---

**Novedad de PRD-263 (Segmentación de clientes inicial en Wallet y Ardid, PJ):**

- **02/10. El PM respondió a Keep IT Simple todos los pendientes del análisis funcional final** (WS-1742/WS-1743). Si Ardid recibe un `ClientBankType` duplicado, devuelve el error `code: 2` ("El ClientBankType ya existe"); un `BankType` duplicado no lo valida. No se manda `personTypeId`. Las Organizaciones existentes usan el nivel de fallback. El nombre que se manda para PJ no cambia. En los 3 casos de cambio de segmento por Fraude (falla a mitad de camino, Wallet no actualiza su copia, desasignar un segmento) va la opción recomendada por Keep IT Simple.
- **Queda una sola duda abierta: la retrocompatibilidad** de las Organizaciones que ya existían antes de la funcionalidad, con sus segmentos actuales en el Calculador de Costos y en Ardid.
- **05/10. Keep IT Simple respondió con un análisis nuevo** (`RETROCOMPATIBILIDAD-DEM-2189-DEM-2188-20261005.html`, sin descargar). Propone **incluir en el alcance de DEM-2189 un reprocesamiento que alguien ejecute a mano desde Swagger** para poblar las Organizaciones anteriores, previo análisis de casuísticas. Falta definir **quién y cómo** lo ejecuta, y eso define el alcance de la historia.
- **Por qué importa para la cartera:** hasta ahora el backfill de Organizaciones existentes era manual y estaba fuera de la puesta en producción (decisión del 23/09). Si el reprocesamiento entra en DEM-2189, eso cambia, y el alcance de una historia ya estimada en XL/15 SP puede crecer. La IDEA sigue EN APROBACION mientras el desarrollo avanza.
