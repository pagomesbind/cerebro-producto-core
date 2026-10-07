---
id: 2026-10-06_agente_cobros_y_pagos_conocimiento_herramienta_pochita_liquidaciones
pm: pablo
fecha_captura: 2026-10-06
fuente: "/sync_meetings — reunión 'pochita demo' (2026-10-06 14:30, propia), minuta + transcripción completa de Gemini"
producto: agente_cobros_y_pagos
tema: Nueva herramienta interna "Pochita" — admin de cuentas/liquidaciones y transferencias de fondeo
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/agente_cobros_y_pagos/herramienta_pochita_liquidaciones.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

Demo de trabajo (no una reunión de seguimiento, sino una sesión de diseño/pair-review en vivo) entre Ana María Moreno (desarrollo) y Maria Eugenia Vila, con Pablo Gomes, sobre "Pochita": una herramienta interna nueva en desarrollo para reemplazar el armado manual del archivo de liquidaciones y evitar que el equipo operativo toque CBUs/montos a mano. Reemplaza/complementa el proceso manual ya documentado en `liquidaciones_reversas_y_comprobantes.md` (mismo dominio: liquidaciones de Agente de Cobros y Pagos).

**Mecánica de configuración de cuentas por entidad/producto:**
- Pantalla "Cuentas" / ABM de entidades: a cada entidad consultada para liquidación se le asocia una cuenta de origen específica desde la cual se hacen los débitos y transferencias — porque no todas las entidades acreditan en la misma cuenta, ni lo hacen para todos los productos (es por producto, no por entidad en general).
- La carga inicial de esta configuración se hace con un script sobre la base, a partir de un Excel armado por Maria Eugenia Vila (entidad, producto, cuenta, mails) — no hay alta vía UI por ahora para la carga masiva inicial; el alta de una entidad nueva individual sí se hace desde la pantalla.
- Cada entidad se asocia a un "producto" configurable (hoy con las etiquetas "botón simple", "QR", "RxT" cargadas como ejemplo — Pablo Gomes pidió renombrar "botón" a "tarjeta" para generalizar, ya que agrupa todas las formas de pago con tarjeta, no solo Botón de Pagos — puede ser POS también). El nombre es un texto editable en stage, no está hardcodeado.
- Por detrás, la relación real es producto↔formas de pago: por ejemplo "botón simple" (nombre configurable) se asocia a las formas de pago 10/60/80/90. Cuando se consultan liquidaciones por ese producto, el sistema trae todas las entidades/comercios asociadas a esas formas de pago para la fecha de negocio consultada. El agrupamiento real en la tabla de liquidaciones es por forma de pago (y por fecha de negocio + comercio), no por el nombre descriptivo del producto ni por ID de liquidación único.
- Exclusión explícita: clientes de "Agente de Cobros y Pagos" (forma de pago 40, "reporter") no se agregan a "cuentas liquidaciones" porque gestionan sus propios fondos de manera independiente — no se liquidan por este circuito.

**Proceso de liquidación y descarga:**
- Se elige producto + fecha de liquidación → trae las entidades configuradas para ese producto y arma el archivo/proceso de transferencias correspondiente. Los montos son editables antes de confirmar.
- Valores en null/cero observados en stage se atribuyen a que ciertos procesos batch no corren igual en stage que en producción (no es necesariamente un bug, aunque Pablo Gomes marcó que amerita revisión — "¿por qué están en null las liquidaciones? porque anda mal... es un error, no debería pasar", sin resolución en la reunión).
- Detectado en vivo: liquidaciones con el monto neto mal calculado por configuración incorrecta del mínimo de arancel+IVA (ya reportado al equipo según Ana María Moreno, sin ticket identificado en esta reunión).

**Vinculación liquidación↔transferencia (gap de trazabilidad, sin resolver en la reunión):**
- Hoy, una vez creado el proceso de liquidación, no queda visible desde la pantalla de liquidaciones si la transferencia asociada se ejecutó bien o falló — solo se sabe entrando al detalle de "procesos". Pablo Gomes propuso agregar columnas en la grilla de liquidaciones para mostrar el proceso relacionado y el estado real de la transferencia (para detectar fallas rápido sin tener que ir a buscar proceso por proceso, especialmente cuando un proceso agrupa muchas transferencias y solo una falla).
- Se acordó implementarlo: nuevas columnas "proceso relacionado" y "transferencia relacionada"/estado de transferencia en la vista de liquidaciones — se prioriza traer el proceso (no un "estado" propio redundante) y una columna adicional de detalle de qué pasó si falló.
- Maria Eugenia Vila aclaró que hoy el flujo operativo real pasa por "procesos" (Gabi, el operador, está acostumbrado a trabajar desde ahí, no desde liquidaciones) — la idea a futuro es que haya un tercer rol que solo valide/ejecute desde liquidaciones sin tocar "procesos" directamente.

**Límite de transferencia y "movimientos de fondo" (nuevo concepto genérico):**
- Transferencias con monto neto superior a $500 millones superan el límite de PBAN (Banco Industrial) — se acordó como requerimiento que el sistema genere automáticamente múltiples transferencias por el excedente cuando una liquidación lo supere.
- Se definió una tabla de configuración genérica de "movimientos de fondo" (reemplaza el concepto de "producto" específico) para gestionar el fondeo de cuentas (ej. PMC) y los impuestos de Wallet, con cuentas de origen/destino configurables por concepto en vez de por producto — ej. concepto "impuestos wallet".
- Próximo entregable identificado: un atajo para fondear PMC directo desde el total de la liquidación, relacionándolo con los conceptos ya configurados.

**Roadmap de entregables (según lo conversado, sin ticket de Jira asociado — herramienta interna, no un proyecto trackeado en `1_proyectos/`):**
- Esta noche (2026-10-06): pase a producción de las columnas de estado de transferencia en liquidaciones (scripts de base con las nuevas columnas relacionales corridos de noche, prueba al día siguiente en producción).
- Impuestos de Wallet: Ana María Moreno los tiene probados individualmente en local, pendiente de contrastar contra la base real — Maria Eugenia Vila estima que solo falta "sentarse a desarrollar" dado que el punteo ya está cerrado (sin pedidos pendientes a Fintexa). Fecha objetivo: octubre 2026.
- Desdoblar transferencias en liquidaciones + vincular estados de transferencia a liquidaciones: próxima prioridad técnica, antes que pasar a un esquema de ramas de desarrollo más complejo (decisión explícita de Pablo Gomes de posponer la complejidad de branching).
- Migración completa de transferencias al nuevo producto/herramienta: objetivo diciembre de este año (2026) — Pablo Gomes pidió fijar esta fecha para poder comunicarla con tranquilidad a Hernán (Clarich) y a Emma Vignoles, y planificar fechas de prueba.
- Reportería: identificado como mejora futura (ej. "todas las liquidaciones de hoy de todos los productos, ¿cuánto fue y cuánto transferí?"), sin compromiso de fecha — se acordó que no es prioridad inicial frente al objetivo base de eliminar el armado manual del archivo.

> Fuente: reunión "pochita demo" (2026-10-06, 14:30, propia), minuta + transcripción completa de Gemini. Participantes: Ana María Moreno, Maria Eugenia Vila, Pablo Gomes.
