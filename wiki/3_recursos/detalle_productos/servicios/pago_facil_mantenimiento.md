# Pago Fácil — mantenimiento post-MVP y ETAPA 2 (producto Servicios)

> Estado: en producción.

> Fuente: Jira `bindpsp.atlassian.net`, espacio **SER** (producto **Servicios**), versión **SER 1** (2026-06-04) — primera y única versión publicada de este espacio a la fecha. 39 tickets. Backfill vía `/sync_releases` (export XML), 2026-07-13.
>
> Este archivo complementa, sin duplicar, dos fuentes ya existentes:
> - PRD-57 (Pago Fácil MVP) — historia de build del **Epic MVP** (SER-1, 31 tickets). Proyecto de Nicolás Colón, vive en su propio Cerebro desde 2026-08-13; ya detallaba los tickets abiertos/relevantes del MVP (SER-37, SER-62, SER-53, SER-60, SER-7, SER-8, SER-63, SER-59).
> - [`transversal/pago_facil.md`](pago_facil.md) — documentación técnica del API cliente-facing (endpoints, request/response), de fuente Notion.
>
> **Acá va lo que ninguna de las dos cubre**: el Epic **"ETAPA 2"** (evolución posterior al MVP, sin IDEA/PRD propio detectado) y una serie de tickets de ajuste fino del MVP (cargo de servicio, forma de pago, homologación con BPG) que no forman parte de los 8 tickets detallados en PRD-57.

## 1. Qué es Servicios / Pago Fácil (aclaración de modelo)

**Servicios** es el nombre de producto que Bind PSP le dio a esta línea de negocio en Jira (PM: Nicolás Colón). **Pago Fácil** es, a la fecha de esta ingesta, su único cliente/caso de uso: una entidad de cobro de servicios (facturas, boletas) que no tiene desarrollo propio y necesita que Bind PSP le resuelva un link de pago completo — desde la búsqueda de la deuda en su sistema externo (**BPG**, ver [boton_simple_2_0.md §6](../adquirencia/boton_simple_2_0.md)) hasta el cobro y la conciliación. La arquitectura interna vive en el producto **DeudaManagement** (ver PRD-57 §3, Cerebro de Nicolás Colón), reutilizando el objeto Deuda de Botón Simple 2.0 de Adquirencia para el cobro efectivo.

## 2. Epic "ETAPA 2" — evolución post-MVP (7 tickets)

Todos publicados en SER 1 (2026-06-04), sin PRD/IDEA propio relevado — parecen haberse gestionado directamente como Epic de seguimiento sobre el mismo tablero.

- **Expirar link de deuda** ([SER-41](https://bindpsp.atlassian.net/browse/SER-41)): el link de pago ahora respeta la `fechaVencimiento` indicada al crear la intención — pasado ese momento, muestra "Este link se encuentra expirado. Por favor, solicitar un nuevo link al proveedor." Si `fechaVencimiento` viene `null`, el link no vence nunca. La fecha de expiración del **checkout de Botón Simple 2.0** subyacente se toma de un parámetro configurado por defecto a nivel Ente.
- **Flujo cuando transfieren un monto no exacto** ([SER-42](https://bindpsp.atlassian.net/browse/SER-42)): decisión de negocio (definida junto con Pago Fácil, con estimación de Pablo Gomes) — ante un pago por un monto **mayor** al de la deuda, se **devuelve el total** y se trata como flujo de rechazo, mostrando "Realizaste un pago por un monto mayor al de la deuda, por lo que procederemos a la devolución del mismo. Pero no te preocupes, ¡podés intentarlo nuevamente!". Se descartó la alternativa de devolver solo el excedente (mayor complejidad, sin beneficio claro para el caso de uso).
- **Mejorar pantalla cuando hay pago parcial y vence el checkout** ([SER-58](https://bindpsp.atlassian.net/browse/SER-58), 3 SP, EN QA a la fecha de esta ingesta): si el checkout vence habiendo un pago parcial ya instruido en devolución, la pantalla debe mostrar el monto insuficiente abonado y el disclaimer "Realizaste un pago por un monto menor al de la deuda y debido a que esta ha vencido, instruimos la devolución del mismo." El botón "Refrescar resultado" debe reflejar el estado una vez confirmada la devolución.
- **Mensaje de error al vencer el checkout** ([SER-57](https://bindpsp.atlassian.net/browse/SER-57)): el mensaje genérico de vencimiento no aclaraba qué pasaba con un pago ya realizado — se agregó texto explícito indicando que, de haberse completado un pago total o parcial, ya se instruyó su devolución.
- **Validación de `fechaVencimiento` ya ocurrida al crear el link** ([SER-56](https://bindpsp.atlassian.net/browse/SER-56)): la creación de intención de pago no rechazaba una `fechaVencimiento` ya pasada — ahora responde `422` con el motivo.
- **Vencimiento de link sin considerar horas/minutos/segundos** ([SER-55](https://bindpsp.atlassian.net/browse/SER-55)): bug de precisión de fecha — una `fechaVencimiento` con horas fraccionarias (ej. `23:59:50`) se evaluaba como ya vencida antes de tiempo; corregido para respetar el timestamp completo.

## 3. Ajustes finos del MVP no cubiertos en PRD-57

- **Cargo de Servicio (`cargoServicio`) en comprobante y resultado del pago** — cluster de 4 tickets: discriminar la Deuda y el cargo de servicio como ítems separados en el checkout ([SER-22](https://bindpsp.atlassian.net/browse/SER-22)), mostrar el cargo antes del pago ([SER-20](https://bindpsp.atlassian.net/browse/SER-20)), sumarlo al monto abonado mostrado y al comprobante — bug corregido ([SER-23](https://bindpsp.atlassian.net/browse/SER-23)), y emitir **dos comprobantes separados** cuando hubo cargo de servicio (el original por el monto de la deuda sin cargo, más uno nuevo `Comprobante-ServiceCharge{IdTransaccion}`) — explícitamente **descartado** en su primera propuesta ("NO REALIZAR EL CASO 2", [SER-43](https://bindpsp.atlassian.net/browse/SER-43) caso 2).
- **Forma de pago informada según método de confirmación en BPG** ([SER-30](https://bindpsp.atlassian.net/browse/SER-30)): al confirmar la transacción, DebtManagement indica el medio de pago real utilizado (tarjeta de crédito/débito) con códigos estándar de BPG.
- **`idItemProveedor` variable por request** ([SER-31](https://bindpsp.atlassian.net/browse/SER-31)): BPG puede tener un mismo Proveedor con más de un `idItemProveedor` — antes exigía credenciales separadas por cada uno; ahora se indica en cada creación de intención de pago. Riesgo aceptado explícitamente por BPG: el dato no es público, pero tampoco está criptográficamente protegido (podría adivinarse por azar).
- **Esquema de reintentos de confirmación de Transacción en BPG** ([SER-39](https://bindpsp.atlassian.net/browse/SER-39)): si BPG no responde en 30 segundos o da timeout, se reintenta la confirmación; tras 2 horas seguidas sin respuesta definitiva, la Operación pasa a estado **AUDITAR**.
- **Instruir devolución ante rechazo de Transacción en BPG** ([SER-38](https://bindpsp.atlassian.net/browse/SER-38)): proceso automático con reintentos que dispara la devolución completa del pago cuando BPG rechaza la transacción, escuchando el webhook de confirmación de devolución de la Solución de Cobro y con fallback de consulta si el webhook nunca llega.
- **Auditoría del flujo de devoluciones ante confirmación rechazada** ([SER-52](https://bindpsp.atlassian.net/browse/SER-52)): esquema de **5 reintentos** con espaciado creciente (inmediato, 2 reintentos rápidos, luego 2 reintentos a intervalos de 2 horas) — si los 5 fallan, la Operación pasa a estado **AUDITAR**; si alguno tiene éxito, pasa a **PAGO DEVUELTO**.
- **Webhook `PAGO_SERVICIOS`** ([SER-54](https://bindpsp.atlassian.net/browse/SER-54), 2 SP): informa a la Entidad el estado de la deuda de Cobro (`IdEstado`/`NombreEstado`: Pago Confirmado, Pago Rechazado) — mismo formato que los webhooks estándar ya enviados por estados definitivos, mismo endpoint de destino configurado.
- **Correcciones de flujos varios post pre-homologación con BPG** — dos tandas ([SER-40](https://bindpsp.atlassian.net/browse/SER-40), [SER-43](https://bindpsp.atlassian.net/browse/SER-43)): 12+3 casos puntuales de UX/datos encontrados en la 5ª pre-homologación con BPG (fechas en UTC-3 en vez de UTC-0, nombre del proveedor visible en comprobante y pantalla de búsqueda, distinguir "no hay deudas pendientes" de "deuda vencida/con errores", mensajes de error sin exponer el detalle crudo de BPG).
- **No validar duplicidad de `codigoEntidad` en el alta** ([SER-44](https://bindpsp.atlassian.net/browse/SER-44)): corregido — todos los entes de Pago Fácil comparten el mismo `codigoEntidad` (el de la Entidad Pago Fácil de Cobro), así que validar duplicados rompía el alta de entes nuevos legítimamente.
- **ReCaptcha — errores en producción** ([SER-64](https://bindpsp.atlassian.net/browse/SER-64)): dos bugs de token de reCaptcha detectados ya en producción — la acción del token generada en la pantalla de vencimiento del link no coincidía con la esperada por el backend ("HOMEPAGE" vs. "procesar_error_pago"), y el polling automático de estado de un pago que queda `INICIADO` no renovaba el token antes de cada consulta, causando fallos de validación.

## 4. Gestión del proyecto — renombre a "Proyecto Servicios" e incorporación al pipeline de Wallet (2026-08-24)

> Estado: en producción (gestión de proyecto en curso, sin cambio de alcance funcional).
>
> Fuente: Reunión "Sincro - Implementación / Proyecto Deuda" (2026-08-24, equipo Fintexa: Pablo Serra, Mariela Marín, Mauricio Campos, Nicolás Pomponio, Pablo Vargas; equipo Bind: Matías Alzogaray, Andrea Orsini, Adriana Endzeliz, Gonzalo Rivera, Nicolás Colón), minuta Gemini.

- **Nombre oficial:** el proyecto (flujo de pago de servicios vinculado a Pago Fácil, documentado en este módulo) pasa a llamarse de forma unificada **"Proyecto Servicios"** — se abandona el nombre histórico "Proyecto Deuda" tanto del lado de Fintexa como de Bind, para evitar confusión con otras iniciativas.
- **Incorporación al pipeline de Wallet:** el proyecto se integra formalmente a la gestión y planificación del equipo de Wallet, a pedido de EMA (12-14 de agosto), para poder disponer de QA y soporte técnico L2/L3. Se advirtió riesgo de superposición de plazos con las prioridades ya vigentes de Wallet.
- **Estado del backlog (2026-08-24):** el tablero tiene ~65 tickets en total, de los cuales menos de 10 quedan pendientes de integrar a producción. El desarrollo data de diciembre 2025 aprox., por lo que se acordó hacer una revisión ("actualización", no auditoría) de arquitectura y seguridad para ponerse al día con lo agregado en los últimos 7-8 meses, más una solicitud de pentest (a cargo de Pablo Vargas, Fintexa).
- Nicolás Colón quedó con la acción de compartir con el equipo el listado de épicas y tickets actuales del proyecto.

## 5. Piloto Productivo Bind-SEPSA — plataforma admin, Billers y puntos operativos abiertos (2026-08-26)

> Estado: en producción (Piloto Productivo en curso).
>
> Fuente: Mail "Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 19-8" — Guillermo Paolucci (Western Union) y Adriana Endzeliz (Bind, Comercial), hilo 2026-08-19 → 2026-08-25.

Hilo de seguimiento comercial/operativo entre Western Union (marca **Pago Fácil**, legal **SEPSA**) y el equipo Comercial de Bind sobre la "Pasarela de Pagos Bind-SEPSA" (Botón de Pago / checkout que corre sobre Botón Simple 2.0, mismo motor documentado en [`pago_facil.md`](pago_facil.md)) — no estaba documentado en el Cerebro el detalle operativo de este frente; este archivo hasta ahora solo cubría el backlog técnico de Jira (espacio SER).

**Plataforma de administración nueva para el Piloto Productivo:** `https://admin.bindpagos.com.ar/`. Permite a Pago Fácil hacer monitoreo transaccional diario, descargar reportes, y — una vez recibida la capacitación — autogestionar el **bloqueo y desbloqueo de comercios** durante el Piloto Productivo.

**Listado de Billers/comercios:** se compartió un adjunto con el mapeo de cada Biller y el comercio asociado en Bind PSP — no procesado en esta ingesta (regla de la skill: adjuntos quedan pendientes de revisión manual).

**Estado de entidades del Piloto (al 2026-08-19):** UAT confirmada para **PRO ACTION**; próximas entidades piloto: **Colegio Ing Cba** y **Marea TV**.

**Puntos operativos abiertos de la minuta del 19/08** (sin confirmación de resolución al 25/08 — a validar en próxima corrida):
- **Tarjeta Prepaga:** se iba a configurar como Tarjeta de Crédito (TC) para pasar por ese flujo del checkout; pasaje a producción estimado semana del 17-ago, pendiente de confirmar fecha real.
- **MODO:** la operatoria entre Bind y MODO se revisaba con Coelsa; status "en espera de validación del administrador", sin novedad.
- **Botón "Flecha"** en el checkout: se evaluaba sacarlo; mientras tanto queda deshabilitado (provisorio) pero visible, con posibilidad de rebautizarlo "FINALIZAR" una vez confirmado. Sacarlo definitivamente requiere protocolo formal y traslado de costos.
- **Identificación de origen de pago:** para pagos con QR y Transferencia se necesita informar a Pago Fácil desde qué billetera se emitió el pago; para pagos con Tarjeta, con qué tarjeta — Comercial coordina reunión con Banco Industrial para resolverlo.
- **Colores del front:** Western Union quedó en validar con su equipo de Marketing la definición de colores para el checkout — pendiente al 25/08.
- **Confirmación online a entidades:** cambios de alcance a coordinar en reunión propia del Proyecto SEPSA (no confundir con el "Proyecto Servicios" de §4 de este archivo — mismo cliente Pago Fácil, frentes distintos: uno es checkout/Botón de Pago con Western Union/Comercial, el otro es DeudaManagement con Fintexa/Wallet).

> Nota: ni Pago Fácil ni Western Union/SEPSA tienen ficha propia en `2_areas/clientes/log_clientes.md` pese a ser cliente en producción — ver gap actualizado en [`2_areas/gaps_y_preguntas.md`](../../../2_areas/gaps_y_preguntas.md) [2026-07-15].

## 6. Restricciones de Coelsa sobre asignación/modificación de alias de CBU (relevante para el checkout de Botón Simple 2.0)

> Estado: en producción (mecánica de plataforma, no exclusiva de Pago Fácil). Fuente: reunión "Daily producto" (2026-08-28).

Hallazgos técnicos sobre el mecanismo de Coelsa aplicables a cualquier CBU de la plataforma, surgidos al analizar un pedido informal de Adriana (comercial) para el cliente Pago Fácil: mostrar el alias del CBU junto al CBU numérico en la opción de transferencia del checkout de Botón Simple 2.0.

- El sistema hoy genera lotes de CBU asociados a una entidad (en este caso, Pago Fácil) que se **reciclan entre todos los comercios de esa misma entidad** — el reciclaje es a nivel entidad, no comercio. En la creación inicial de esos lotes **no se invoca la asignación de alias**.
- **Coelsa exige obligatoriamente un alias para todo CBU**: si la plataforma no lo asigna en un plazo de 5 segundos, Coelsa le asigna uno arbitrario de forma automática (ejemplo real visto en pruebas: `pies.farol`) — mismo plazo de 5 segundos ya documentado para CVU en [`wallet/validaciones_y_alias_cvu.md` §1](../wallet/validaciones_y_alias_cvu.md). No es que falte un alias: ya existe uno (aleatorio, generado por Coelsa) que Bind PSP no persiste en base ni muestra en la interfaz.
- **Restricción de modificación**: no se permite asignar o modificar el alias vinculado a un CBU en un plazo menor a 24 horas desde la última modificación, con un límite de 3 a 10 modificaciones por año (la minuta registra ambos números en distintos pasajes — a confirmar el valor exacto; ver el mismo tope ya documentado con más precisión, 10/año, en `wallet/validaciones_y_alias_cvu.md` §1).
- Alternativa técnica identificada para evitar consumir el cupo de modificaciones de Coelsa: la API de One Bank (`get cuenta cbu corta y cbu larga`) permite **consultar** (no modificar) el alias ya asignado por Coelsa.

**Decisión tomada en la sesión:** el alcance de una eventual solución sería general para toda la plataforma (no exclusivo de Pago Fácil), con parametrización por entidad/comercio para habilitar la visibilidad, consultando el alias vía la API existente al asignar el CBU y persistiéndolo — posponiendo cualquier asignación de alias personalizado/custom. Ver oportunidad relacionada, ya trackeada como iniciativa `alias_cvu_checkout` en [`direccion/iniciativas.md`](../../../2_areas/direccion/iniciativas.md) y como OP-016 en [`direccion/oportunidades.md`](../../../2_areas/direccion/oportunidades.md) — el discovery de ese proyecto ya está completo y listo para ticket de Ingeniería.

## Ver también

- PRD-57 — Pago Fácil MVP — historia de build del MVP, PM y decisiones de alcance. Proyecto de Nicolás Colón, en su propio Cerebro desde 2026-08-13.
- [transversal/pago_facil.md](pago_facil.md) — documentación técnica del API cliente-facing.
- [adquirencia/boton_simple_2_0.md §6-7](../adquirencia/boton_simple_2_0.md) — el objeto Deuda y BPG que este producto reutiliza como motor de cobro.

---
*Última actualización: 2026-09-02 — `/context_merge`: §6 nueva — restricciones de Coelsa sobre alias de CBU (mecánica de plataforma, surgida de un pedido puntual de Pago Fácil).*
*Última actualización anterior: 2026-08-31 — `/context_merge`: §5 nuevo — Piloto Productivo Bind-SEPSA (plataforma admin, Billers, puntos operativos abiertos), del hilo de seguimiento comercial 2026-08-19/25.*
