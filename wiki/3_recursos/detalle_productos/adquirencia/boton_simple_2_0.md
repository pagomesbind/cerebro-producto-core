# Botón Simple 2.0 — checkout unificado multi-medio de pago

> Estado: en producción.

> Fuente: Notion histórico, Epics **"Botón Simple 2.0"** (78 tickets — la segunda Epic con más tickets de toda la ingesta, con PRD completo), **"Devoluciones para botón simple"** y **"Cambios DECIDIR Botón por marcas"** (Normativo).

## 1. Qué resuelve (PRD)

**Problema previo**: el link de pago de Bind PSP (Botón Simple 1.0) solo permitía pagar con tarjeta vía checkout con redirección; QRI (QR interoperable) y RxT (Recaudación por Transferencia) existían como **servicios separados**, no integrados al mismo link. Eso fragmentaba la experiencia y obligaba al comercio a integrar varios flujos distintos para ofrecer todos los medios de pago.

**Solución**: evolucionar el link de pago hacia un **checkout integral marca blanca** que soporta, desde un único flujo (monto → selección de medio de pago → confirmación): tarjetas (crédito/débito/prepaga, todas las marcas y bancos), **QRI** y **RxT (transferencia a CVU)**. El link es configurable (qué medios acepta cada uno, URLs de redirección por resultado) y notifica el estado definitivo del pago por webhook.

**Roadmap en 3 fases**: (1) integrar RxT y QRI al link existente — el grueso del desarrollo relevado; (2) mejorar UX/UI del checkout; (3) SDK embebible para evitar la redirección por completo (evolutivo, no confirmado si se construyó).

## 2. Modelo de datos interno: "Deuda"

Internamente, cada link de pago de BS2.0 se modela como una **Deuda** — un objeto con su propio ciclo de vida (`PENDIENTE` → `PAGADA` / `CANCELADA` / `CANCELADO MANUAL`) que puede satisfacerse por **cualquiera de los medios habilitados** (tarjeta, QRI, o transferencia a un CVU asignado a esa deuda). Esto explica por qué el 90% del backlog de bugs de esta Epic gira en torno a la palabra "Deuda": es la abstracción que unifica los tres medios de pago bajo un mismo objeto de negocio.

- **CVU por deuda**: cada deuda que acepta CVU/transferencia tiene un CVU propio asignado desde un **stock/pool de CVUs pre-creados masivamente**. Al pagarse o vencer la deuda, el CVU debe darse de baja para volver (o no) al pool.
- **"Pago único con CVU"**: variante donde una transferencia satisface la deuda si el monto transferido es mayor o igual al esperado (hay tickets separados para el caso `≥` y el caso `<`, este último presumiblemente para pagos parciales/insuficientes).

## 3. Cluster de bugs — ciclo de vida de "Deuda" y del pool de CVUs (aprendizaje central)

Este es, hasta ahora, el cluster de bugs más denso y más consistente temáticamente de todo el proyecto de ingesta — casi todos son variantes de **desincronización entre el estado de la Deuda y las acciones que deberían dispararse** al cambiar ese estado:

- **Gestión del pool de CVUs**: los CVUs se consumían **de más nuevo a más viejo** (debía ser al revés — FIFO, no LIFO); no había un **job que reponga CVUs** dados de baja según cuentas con fecha de cancelación; el vencimiento de un link **no daba de baja su CVU**; el pago completo **tampoco** daba de baja el CVU; y el flujo para volver a dar de alta un CVU ya dado de baja tenía su propio bug.
- **Inconsistencia webhook↔estado real**: el webhook de deuda pagada con tarjeta traía el campo `Codigo de deuda` en vez de `CodigoDeuda` (camelCase roto), otro webhook confundía el estado de "pagoDeuda" con el estado de "deuda" (dos conceptos relacionados pero distintos), y faltaba directamente la notificación de pago exitoso cuando la deuda se pagaba con QR o transferencia — **el medio de pago "nuevo" (QRI/RxT) sistemáticamente no disparaba los mismos eventos que ya andaban bien para tarjeta**, patrón típico de una integración de segundo medio de pago sobre un modelo pensado originalmente para uno solo.
- **Casos de negocio no contemplados**: transferencia de un monto mayor al esperado no generaba transacción ni satisfacía la deuda; una deuda pagada con contracargo rechazado no permitía volver a intentar la devolución; consultar una deuda ya `PAGADA` la pasaba incorrectamente a `CANCELADO`; el estado no pasaba a `CANCELADA` cuando el fallo del pago era por ARDID (motor de riesgo).
- **Devoluciones fragmentadas por medio de pago**: hubo que construir la devolución de una deuda pagada con tarjeta, con transferencia (RxT) y con CVU **como desarrollos separados** (cada uno "en desarrollo" con su propio ticket) — reforzando que unificar el objeto Deuda no unificó automáticamente todas las operaciones sobre ella.

**Lección general reutilizable**: al integrar un segundo/tercer medio de pago sobre un modelo de datos ya construido para uno solo (acá "Deuda" nació pensada para tarjeta), hay que auditar explícitamente **cada efecto secundario del ciclo de vida** (webhooks, liberación de recursos como CVUs, devoluciones) para los medios nuevos — no asumir que "ya funciona" porque el camino feliz de creación del objeto es el mismo.

## 4. Devoluciones para Botón Simple (Epic separada, más chica)

Evolución previa a BS2.0: devoluciones parciales del botón en dos partes, y devoluciones **desde el Admin** — la primera versión de esto solo actualizaba el back office de Possumus (procesador) **sin informar a la Solución de Cobro**, una limitación explícita documentada en el propio ticket (parche parcial, no integración completa).

## 5. Cambios DECIDIR por marcas (Normativo, ~10 SP)

Epic normativa chica y acotada en el tiempo (jul-ago 2025) para adaptar Botón Simple a cambios exigidos por DECIDIR (procesador) según la marca de la tarjeta — sin detalle adicional más allá del spike de análisis y el ticket de implementación.

## 6. APIs para buscar deuda (Impuestos y Servicios) y cobrarla con BS2.0

> Fuente: Notion histórico, Epic **"APIs para buscar deuda y cobrarla con BS2.0"**. Extiende el objeto "Deuda" de BS2.0 (§2) para un caso de uso normativo/comercial concreto: **pago de impuestos y servicios (IyS)** vía **BPG** (BIND Payment Gateway — no confundir con "Botón de Pago Embebible", es el nombre del gateway externo/interno de terceros para deuda de servicios).

- **Mecánica**: la Entidad busca deudas de impuestos/servicios existentes en BPG a través de APIs tipo **pasamanos** de Bind (para no impactar a quien ya estuviera integrado directo a BPG), instruye la generación de un link de pago BS2.0 sobre esa deuda identificada, y **al pagarse correctamente, Bind imputa el pago de vuelta en BPG** — cerrando el círculo con el sistema externo de origen de la deuda.
- **Por qué importa**: es un requerimiento directo de **Pago Fácil** (cliente/caso de uso ya documentado en [pago_facil.md](../servicios/pago_facil.md)) y, a la vez, un producto nuevo en el catálogo de Bind PSP que sienta la base para eventualmente ofrecer pago de impuestos y servicios también desde Wallet.
- **Fuera de alcance explícito**: buscar la deuda desde el propio front del checkout de BS2.0 — la búsqueda de deuda es responsabilidad de la Entidad integradora, no del checkout de Bind.
- **Origen del objeto "Deuda"**: una Epic previa y más chica, **"Deuda QR"** (2024), fue el primer trabajo de esta línea — validó volumen (60.000 operaciones de crear+consultar deuda por día, 5 hilos concurrentes) e integró el concepto de Deuda al QR antes de que BS2.0 generalizara el mismo objeto a los tres medios de pago (§2).

## 7. Multi-credencial / "ThirdPartyStore" — Bind como plataforma pura sin ser comercio de registro

> Fuente: Notion histórico, Epic **"Pago Facil: Multicredencial BS y no liquidar"** (comparte Definiciones con la Epic del punto 6 — ambas nacieron del mismo proyecto ejecutivo con Pago Fácil).

Evolución del botón de pagos para soportar **dos modalidades**:

- **OwnStore** (modelo actual): Bind procesa con sus propias credenciales de adquirente y liquida al comercio — Bind es el comercio de registro ante el procesador.
- **ThirdPartyStore** (nueva): el cliente usa **sus propias credenciales de procesador**, la liquidación va **directo del procesador al cliente** (Bind nunca la recibe), y la transacción **no genera impuestos ni obligaciones fiscales para Bind PSP** ni se suma a sus pendientes de liquidación — se persiste con un tipo de pago distinto (`third_party_store`) solo para conciliación/monitoreo/auditoría.
- **Reconciliación**: archivo de conciliación con la misma estructura que ya usa Bind, agregando el campo `payway_TID` — uno por modalidad y por cliente.
- **Lectura de modelo de negocio**: esta es la primera evidencia en toda la ingesta de que Bind PSP puede operar como **infraestructura pura de pagos sin ser el comercio de registro** — un modelo de "payment facilitator as a service" distinto de todos los demás casos vistos (donde Bind siempre liquida y es responsable fiscal). Relevante si en el futuro se evalúan integraciones similares con otros clientes grandes que ya tengan su propio acuerdo con un procesador.

## 8. QR Tarjeta — aceptar pagos con tarjeta desde wallets vía QR interoperable (cliente: MODO)

> Fuente: Notion histórico, Epic **"QR tarjeta"** (PRD completo + minuta de reunión con Payway). Complementa el rol emisor de PIX ([wallet/pix_rol_emisor.md](../wallet/pix_rol_emisor.md)) desde el lado **aceptador**: acá Bind extiende su QR interoperable para que billeteras de terceros paguen con tarjeta en vez de saldo/transferencia.

- **Primer y único cliente previsto**: **MODO** (billetera interoperable de bancos argentinos) — el PRD asume explícitamente que en el mediano plazo probablemente sea la única billetera que se integre por esta vía.
- **Mecánica MVP**: MODO envía los datos crudos de la tarjeta (`card_data`) y Bind procesa el pago contra **DECIDIR** como si fuera un pago de Botón Simple más — **1 sola cuota sin interés**, sin campañas especiales para MODO en esta etapa (la respuesta de planes se mockea).
- **API Resolve** (la misma que usan las billeteras para leer cualquier QR interoperable) se adapta para indicar si el QR admite pago con tarjeta y qué campos adicionales pide específicamente MODO.
- **Evolución prevista** (no confirmado si se construyó): que **DECIDIR pueda reconocer que el pago viene de una billetera virtual y no de un e-commerce** (mejor tasa de aceptación de marcas), y que MODO pueda enviar un token de marca en vez de los datos crudos de la tarjeta.
- Reutiliza el **PCT** (Point of Contactless/Tarjeta) del comercio para procesar — el comercio debe optar explícitamente por admitir este canal, ya que no todos quieren aceptar pagos con tarjeta originados en un QR.

### 8.1 Definiciones técnicas de desarrollo (reunión "Análisis COBRO", 2026-08-31 — equipo Fintexa + Pablo Gomes/Nicolás Colón/Luciana Rudaz/Matías Alzogaray)

Continuación de la tarea T-010, avanzando el desarrollo de QR Tarjeta priorizado para la versión de septiembre:

- **Post-payments necesita especificación técnica propia, separada de Botón Simple.** Daniela Collia (Fintexa) planteó que "post payments" de QR Tarjeta no puede reutilizar tal cual la configuración/especificación de Botón Simple — los requisitos de configuración de canal no coinciden entre ambos flujos. Pablo Gomes confirmó la separación; Nicolás Colón crea el ticket/especificación nueva, asociándolo a las reglas de QR Tarjeta.
- **API Resolve — Terminal ID: se mantiene el código de comercio.** Quedaba abierto cómo identificar el "terminal" en la API Resolve para este flujo — se había considerado un valor aleatorio. Se acordó mantener el **código de comercio como identificador de terminal**, interpretando que el alta por comercio representa la caja para este propósito — a validar con MODO (la contraparte del caso de uso). Nicolás Colón crea un ticket para dejarlo definido formalmente.
- **Validación de rubro de comercio vs. site ID del canal (no ligado puntualmente a QR Tarjeta, mismo bloque de la reunión).** El rubro del comercio solo se conoce a nivel comercio, no a nivel entidad, lo que complica el filtrado del site ID en el dropdown de configuración de canal (antes no había ningún control cruzado ahí). Se acordó que si el site ID no es compatible con el rubro del comercio, el sistema **no bloquea** — muestra una advertencia/error y deja la corrección manual a cargo del usuario, para no comprometer la integridad de datos sin frenar la operación. Queda para más debate (sin cerrar, a cargo de Nicolás Colón): restringir directamente la configuración de canales para comercios no habilitados.
- **Mejora de UX en Admin:** mover el botón de "guardar" de la configuración de canal a estar dentro de cada sección de canal (en vez de un botón único fuera de las secciones), eliminándolo una vez que la sección ya está configurada — sin ticket propio identificado en la minuta.
- **Webhook de Cobro QR exitoso — nuevos campos de arancel** (ver detalle completo en [webhooks_y_notificaciones.md](webhooks_y_notificaciones.md)): se agrega porcentaje y monto del arancel aceptador, e importe neto, para que las entidades agregadoras no necesiten una consulta adicional a la transacción.
- **Otros endpoints en desarrollo mencionados en la misma reunión** (sin ticket propio en QR Tarjeta): se retoma "get payments" y "get order"; "patch plans" está listo para desarrollo pero bloqueado en stage por un código de billetera que rompe las pruebas generales; "Paymis Notify" debe rediseñarse desde cero. Segunda parte de la mejora de performance de generación de archivos (ticket 1144) retomada, sin fallas críticas reportadas, carácter preventivo. Campo "purpose of payment": solo se incluye cuando es obligatorio para Mastercard; si llega vacío el arreglo de valores soportados sería un caso de error, aunque poco probable.

Próximos pasos a cargo de Nicolás Colón: crear los tickets de post-payments, API Resolve (terminal ID) y herramientas de configuración de pago (dropdown de procesador); implementar la mejora de UI de canal; consultar con "Euge" sobre errores de performance previos.

> Fuente: Reunión "Análisis COBRO" (2026-08-31) — capturado independientemente por Nicolás Colón y Pablo Gomes, ambas versiones consolidadas acá sin contradicción (mismo hecho, distinto nivel de detalle).

## 9. Botón Simple 1.0 y API Deuda — mejoras pedidas por cliente RIPSA (IDEA Jira PRD-87, Finalizada)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA PRD-87 "DESA: Botón cancelar y filtros en apis" (sin PRD redactado en la Descripción — estándar reciente, no aplicaba a esta IDEA) + Epic AD-260 (10 tickets con contenido, 2 Test/Xray excluidos). Cliente que solicitó la mayoría de estos cambios: **RIPSA**, vía ticket de soporte (`bindtm` BP-46021) e interacción directa con Producto.

Mejoras puntuales sobre **Botón Simple 1.0** (el predecesor mencionado en §1) y sobre la API de **Deuda** (§2, §6) que siguen recibiendo pedidos de clientes años después de construido el objeto original:

- **Botón "Cancelar" en BS 1.0**: nuevo atributo opcional `cancelUrl` en la creación del link de pago 1.0 — si viene informado, se renderiza un botón "Cancelar" (estilo secundario) que redirige a esa URL y pasa el Payment a estado Cancelado; si no viene, el comportamiento es el de siempre (sin botón).
- **Link expirado redirige a `errorUrl`**: si un link de BS 1.0 expiró, además de mostrar la pantalla de expirado ya existente, ahora redirige a `errorUrl` si el comercio la informó.
- **Filtros ampliados en `getFilteredPaymentLinks` (BS 1.0)**: se sumó filtro por `codigoComercio` (pedido explícito de RIPSA); quedó pendiente de scope en la misma tanda el pedido de filtrar también por fecha de pago, tipo/nombre de tarjeta, BIN, email y DNI del pagador.
- **Nuevo endpoint `GET /api/v1/Deudas`**: reemplaza/extiende a `GET /api/v1/DeudasPendientes` (§6) agregando paginación (`start`/`length`), filtro por estado, por rango de fecha de creación y por rango de fecha de cobro — pedido puntual de RIPSA para alimentar una grilla de búsqueda de deudas en su propio backoffice.
- **Cluster de bugs encontrados en QA sobre el endpoint nuevo**:
  - Paginación no expuesta en la respuesta (sin metadata de página actual/tamaño/total) — **reportado y corregido dos veces** (AD-858 en versión AD 68, luego reaparece como AD-1217 en AD 70.1; el equipo aclaró en comentarios que el segundo hallazgo "no debería cobrarse" por ser el mismo pedido ya hecho antes — señal de que la corrección original no cubrió todos los endpoints de Deuda).
  - `fechaDePago` no se informaba en la respuesta pese a existir el dato (visible en la tabla `PagoDeuda`).
  - Inconsistencia de `camelCase`: algunos campos nuevos no seguían el estándar; se corrigió selectivamente — un caso se cerró explícitamente como "No aplica" porque, pese a ser un endpoint nuevo, reutiliza la estructura de uno preexistente y romper esa estructura hubiera sido peor que la inconsistencia de estilo.
- **Lectura para estimaciones futuras**: 3 Story Points totales en la IDEA — evidencia de que "agregar un filtro/atributo puntual a una API ya construida" (Deuda, BS1.0) es trabajo chico, pero genera una cola de bugs de QA proporcionalmente mayor a su tamaño (4 de los 10 tickets del lote fueron bugs, no historias) cuando el endpoint toca datos con formato ya estandarizado en otro lado del sistema.
- Ver la documentación técnica final (contrato de API cliente-facing) de estos mismos endpoints en [botones_de_pago_y_qr.md §"nuevos filtros en endpoints de consulta para RIPSA-DESA"](botones_de_pago_y_qr.md).
- **Versiones de publicación** (vía `/sync_releases`): AD-372/AD-262/AD-261 en **AD 67.2** (2026-02-10); AD-858/AD-857 en **AD 68** (2026-03-30); AD-862 en **AD 69** (2026-04-29); AD-1219 en **AD 70.1** (2026-06-24); AD-1217 (segunda reaparición de la paginación no expuesta) también en **AD 70.1**.

## 10. Historial de releases del cluster BS2.0 (vía `/sync_releases`)

> Los tickets Jira que originaron el cluster de bugs de §3 y la mayoría de §9 se publicaron en las siguientes versiones (backfill vía export XML, 2026-07-13). Se listan por versión con atribución de key — el contenido conceptual ya vive en §3/§9, acá queda el mapeo a fecha de producción.

- **AD 65** (2025-11-17, lanzamiento): [AD-23](https://bindpsp.atlassian.net/browse/AD-23) (atributo `medioPagoTarjeta` al crear link).
- **AD 66** (2025-12-16, 13 tickets — el grueso del cluster de §3): [AD-319](https://bindpsp.atlassian.net/browse/AD-319) (pago con tarjeta pasa a DEVUELTA), [AD-259](https://bindpsp.atlassian.net/browse/AD-259)/[AD-257](https://bindpsp.atlassian.net/browse/AD-257) (camelCase `monto`, `CodigoDeuda` vacío), [AD-243](https://bindpsp.atlassian.net/browse/AD-243) (asignar CVU), [AD-194](https://bindpsp.atlassian.net/browse/AD-194) (CANCELADO automático por vencimiento), [AD-140](https://bindpsp.atlassian.net/browse/AD-140) (DevolucionDeuda queda Estado=1), [AD-127](https://bindpsp.atlassian.net/browse/AD-127)/[AD-121](https://bindpsp.atlassian.net/browse/AD-121)/[AD-118](https://bindpsp.atlassian.net/browse/AD-118) (contracargo RxT sin misma lógica que QR, devolución de transferencia no genera contracargo), [AD-106](https://bindpsp.atlassian.net/browse/AD-106) (falta notificación pago exitoso QR/Transferencia — el bug central de §3), [AD-54](https://bindpsp.atlassian.net/browse/AD-54)/[AD-53](https://bindpsp.atlassian.net/browse/AD-53)/[AD-52](https://bindpsp.atlassian.net/browse/AD-52) (UX de espera de pago/transferencia).
- **AD 66.3 HF** (2026-01-20): [AD-539](https://bindpsp.atlassian.net/browse/AD-539) hotfix dedicado — Fletalo, operaciones colgadas en estado 1.
- **AD 67.1** (2026-01-30): [AD-345](https://bindpsp.atlassian.net/browse/AD-345) (no permitir otra devolución si el estado RxT es UNKNOWN), [AD-38](https://bindpsp.atlassian.net/browse/AD-38) (mejorar error al devolver transferencia de otro Collector).
- **AD 67.2** (2026-02-10): cluster denso de DevolucionDeuda — [AD-476](https://bindpsp.atlassian.net/browse/AD-476) (contracargo PENDIENTE/RECHAZADO no se guarda), [AD-475](https://bindpsp.atlassian.net/browse/AD-475)/[AD-474](https://bindpsp.atlassian.net/browse/AD-474)/[AD-471](https://bindpsp.atlassian.net/browse/AD-471)/[AD-470](https://bindpsp.atlassian.net/browse/AD-470) (consultas de DevolucionDeuda inexistente/de otra entidad sin error correcto), [AD-459](https://bindpsp.atlassian.net/browse/AD-459) (registrar guid del link aparte), [AD-457](https://bindpsp.atlassian.net/browse/AD-457) (contracargo parcial de Transferencia siempre rechazado), [AD-428](https://bindpsp.atlassian.net/browse/AD-428) (consulta de contracargo 404), [AD-424](https://bindpsp.atlassian.net/browse/AD-424) (crear Deuda con todos los medios en false), [AD-403](https://bindpsp.atlassian.net/browse/AD-403) (timer del checkout desfasado 3hs — bug de timezone). **[AD-418](https://bindpsp.atlassian.net/browse/AD-418) quedó "Con defecto"**: no existe endpoint para hacer la devolución desde Cobro, solo desde Financial directamente — deuda técnica reconocida, no resuelta a la fecha de esta ingesta.
- **AD 68** (2026-03-30): [AD-670](https://bindpsp.atlassian.net/browse/AD-670) (mensaje de error mal mapeado al devolver monto mayor al pagado), [AD-615](https://bindpsp.atlassian.net/browse/AD-615) (CVU no se da de baja ante vencimiento), [AD-487](https://bindpsp.atlassian.net/browse/AD-487) (consulta de Deuda ya no trae `paymentGuid`), [AD-445](https://bindpsp.atlassian.net/browse/AD-445) (error incorrecto al crear Deuda con todos los medios en false — reaparición de AD-424).
- **AD 69** (2026-04-29): [AD-899](https://bindpsp.atlassian.net/browse/AD-899) (corregir endpoint DELETE Deuda), [AD-587](https://bindpsp.atlassian.net/browse/AD-587)/[AD-467](https://bindpsp.atlassian.net/browse/AD-467) (aviso de pago exitoso no ocurre para pago QR/Transferencia en otra pestaña — variante persistente del bug central de §3), [AD-971](https://bindpsp.atlassian.net/browse/AD-971) (considerar pagos luego del vencimiento de la deuda).

## 11. Parámetro `pago_unico` — definición formal (1 = Botón de Pago, 0 = RxT) y saneamiento de base (2026-08-20)

> Fuente: Reunión "Análisis COBRO" (2026-08-20), minuta Gemini. Continúa el hallazgo ya documentado en [pedidos_de_clientes_y_hallazgos_operativos.md](pedidos_de_clientes_y_hallazgos_operativos.md) (bug de asignación automática de CBU corta sin filtro por `pago_unico`, cliente FAVACARD, 2026-08-06, con actualización 2026-08-13 sobre el análisis técnico completo del atributo en `Facart`).

**Decisión acordada (2026-08-20):** el parámetro **"pago único"** se definió para diferenciar el producto asociado a una cuenta con CBU — **valor 1 = botón de pago**, **valor 0 = RXT**. Objetivo: poder identificar qué colecciones/cuentas corresponden a cada categoría.

**Saneamiento de base acordado:** Daniela Collia (Fintexa) y Nicolás Colón van a coordinar el saneamiento de la base de datos para identificar las cuentas de "pago único" existentes y diferenciarlas correctamente entre RXT y botón simple. Nicolás Colón queda a cargo de analizar qué colecciones corresponden a cada categoría. **Decisión de secuencia:** el saneamiento se ejecuta en conjunto con el despliegue del código correspondiente, para asegurar que quede todo alineado en producción al mismo tiempo (no antes, no después).

**Relación con el hallazgo de FAVACARD:** el bug de asignación automática de CBU corta en Botón Simple 2.0 sin filtro por `pago_unico` (identificado el 2026-08-06) y el análisis técnico posterior del 2026-08-13 (que reveló que el atributo servía a la vez para distinguir RxT/Botón 2.0 y para disparar la baja automática del CBU/identificador, con 159 cajas de comercio afectadas) parecen ser el antecedente directo que motivó esta definición formal y el saneamiento — ver el detalle completo en [pedidos_de_clientes_y_hallazgos_operativos.md](pedidos_de_clientes_y_hallazgos_operativos.md).

## 12. Eliminación del límite de $9.000.000 en creación de links de pago (AD V72, 2026-08-21)

> Fuente: Reunión "Análisis de riesgos AD V72" (2026-08-21), minuta Gemini — sección Decisiones, "Eliminación de límite de pago" y Detalles ([00:42:44]).

En la reunión de riesgo de AD V72 (despliegue 27/08/2026) se aprobó eliminar la validación que hoy limita la creación de links de pago de Botón Simple 2.0 a un monto máximo de **$9.000.000**. Matias Alzogaray lo presentó como un ticket de soporte, sin motivo de negocio específico documentado en la minuta — se retira directamente la restricción, sin reemplazo por un tope configurable. Clasificado con semáforo verde (bajo riesgo).

**Dato relevante para contexto histórico:** este mismo límite de $9M ya había sido señalado como punto sin resolver por un cliente (Provincia NET preguntó en julio si el tope "podía ser más" — ver `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §2`, aunque ese caso es sobre el monto máximo de un QR de pago único, no necesariamente el mismo límite de Botón Simple 2.0; a confirmar si son el mismo control o distinto).

## Ver también

- [botones_de_pago_y_qr.md](botones_de_pago_y_qr.md) — mecánica de órdenes de venta y cajas del Botón Simple "clásico".
- [liquidaciones_y_devoluciones.md](devoluciones_y_contracargos.md) — mecánica general de contracargos/devoluciones, incluye el caso "Desconocimiento" también de Botón Simple.
- [transversal/pago_facil.md — sección Grupo DESA](../servicios/pago_facil.md) — mismo cliente RIPSA/Grupo DESA, pedido anterior (Notion histórico) sobre el motor de Link de Pago (checkout personalizado + reportería) en vez de sobre Botón Simple 1.0/API Deuda.
