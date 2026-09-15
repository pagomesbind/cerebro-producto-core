---
id: 2026-09-11_iniciativa-ardid-desconocimientos-nuevo-proyecto
pm: nicolas
fecha_captura: 2026-09-11
fuente: "Discovery /idea_start sobre PRD-248 (2026-09-10/11)"
producto: ardid
tema: Nuevo proyecto — automatizar el aviso de desconocimientos a Ardid
tipo: iniciativa
destino_propuesto: 2_areas/direccion/iniciativas.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: PENDIENTE
proyecto: ardid_desconocimientos
---

Proyecto nuevo en el foco Ardid de Nicolás Colón, a partir de [PRD-248](https://bindpsp.atlassian.net/browse/PRD-248) "Informar desconocimiento de transacción en Ardid (Contracargo)". Discovery completo (Gates 1-3 cerrados en la misma sesión, 2026-09-10/11):

- **Problema:** Bind PSP no bloquea automáticamente en Ardid las tarjetas de un "desconocimiento" (contracargo fraudulento) de Botón Simple — depende de una carga manual semanal que hace Rocío Revelli (equipo de Fraude), señalada como no escalable por Mariana Nadalin (jefa de Operaciones). Mientras no se avisa, la tarjeta sigue operando sin bloqueo. Volumen alto: 355 desconocimientos en los primeros 11 días de septiembre 2026.
- **Gate 2:** ✅ Vale la pena ahora — riesgo real de fraude sin control (con precedente de costo: multa de $75M ya pagada por fallas de bloqueo de Ardid), sponsor interno activo. Debilidad: compite por capacidad del foco Ardid con `titularidad_tarjeta/` (discovery cerrado el mismo día) y PRD-191 (ráfagas, EN CURSO).
- **Gate 3 — hallazgo relevante para el canon:** el planteo inicial incluía pedirle a Pentass (proveedor de Ardid) un endpoint nuevo para informar contracargos (talle S, ~US$1.000). El catálogo técnico de Ardid (`3_recursos/detalle_productos/ardid/apis_externas.md`) ya documentaba dos endpoints que cumplen esa función (`POST /api/FilProcess/Process` y `POST /FileProcessController/UploadChargebackTransactionsFile`), y el PM confirmó que el proceso manual actual ya es, mecánicamente, subir un archivo — coincide con el segundo. Se descartó pedirle nada nuevo a Pentass; el trabajo pasa a ser 100% interno (automatizar el armado de datos que hoy se arma a mano).
- **Alcance final:** un solo proyecto con 3 piezas codependientes (definidas así por el PM) — automatizar el aviso, ampliar la ventana de retención de Ardid (hoy 45 días, contracargos llegan hasta 120 — hay volumen real ya fuera de esa ventana), y confirmar el mecanismo técnico exacto de integración.
- **Quedan 2 gaps técnicos** (documentados en `1_proyectos/ardid_desconocimientos/gaps.md`, no van al canon) antes de poder estimar: cuál endpoint usa hoy el front y si Bind puede invocarlo directo; quién es dueño del cambio de retención (Infra propia de Bind vs. Pentass).

Detalle completo del discovery en `1_proyectos/ardid_desconocimientos/proyecto.md`.
