# Webhooks y Notificaciones — Mecánica Interna por Canal

> Estado: en producción.

> ⚠️ **Infraestructura compartida con Wallet.** El flujo genérico de disparo de webhooks y el glosario de microservicios (`Pago Externo`, `Workflow`, `Notificaciones`, `Financial`/`CB Collect`) son comunes a todos los canales de cobro, incluyendo el circuito de QR que también sustenta a Wallet (ver [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md)). Un agente en paralelo puebla la porción equivalente en `wiki/3_recursos/detalle_productos/wallet/`.
>
> Fuente original: sesión de capacitación del 2026-01-16 (`wiki/3_recursos/mecanica_interna_productos/webhooks_y_notificaciones.md`). Complementa la política de reintentos de webhooks ya documentada (10 intentos, HTTP 200 esperado) en [`3_recursos/arquitectura_sistema/politica_de_reintentos_de_webhook.md`](../../arquitectura_sistema/politica_de_reintentos_de_webhook.md) — este documento explica **qué dispara el envío** del lado interno.

## Webhook vs API — se invierten los roles

- Una **API** es una puerta de enlace controlada que un servidor abre para que un cliente externo cree, modifique o consulte datos (request/response). En nuestras APIs, **Bind PSP es siempre el servidor**; el cliente que se integra (ej. Astropay) es quien inicia la comunicación.
- Un **Webhook** es una notificación (típicamente un `POST`) que **Bind PSP envía al cliente** para avisar que ocurrió un evento (ej. una transacción se acreditó). Es decir: con los webhooks, **los roles se invierten** — en vez de que el cliente venga a buscarnos, **nosotros vamos a buscar al cliente**.
- Para recibir webhooks, el cliente debe **construir y exponer su propio endpoint receptor** (le llaman coloquialmente "el webhook del cliente") y documentar esa URL en su configuración con Bind PSP. Debe responder **HTTP 200** para confirmar la recepción — es lo que Bind PSP documenta como contrato de confirmación.

## Consistencia de formato — por qué importa tanto

- Los clientes suelen **validar el mensaje** recibido (verificar que ciertos campos existan con el nombre y tipo esperado) antes de procesarlo internamente.
- Un cambio no documentado en el modelo del webhook (ej. renombrar un campo de `cb_corta` a `cbCorta`, o cambiar de minúsculas a mayúsculas) puede hacer que el webhook **se reciba correctamente (200 OK)** pero **rompa el procesamiento interno del cliente**, porque su validación no encuentra el campo esperado con el nombre que espera.
- Por eso el modelo de cada tipo de webhook debe mantenerse **estable y documentado** — es un contrato tan importante como el de una API síncrona, aunque el cliente no lo "pida" explícitamente en cada request.

## Flujo genérico de disparo (patrón común a todos los canales)

Independientemente del canal de cobro, el patrón interno observado es:

1. El canal específico (POS, QR, transferencia, Botón Simple) **resuelve el resultado del pago** con su procesador correspondiente.
2. El resultado se pasa al microservicio **"Pago Externo"**.
3. Pago Externo delega a **"Workflow"**, cuyo único trabajo es **insertar transacciones**.
4. Workflow **consulta convenios** (comisión, plazo de liquidación) antes de insertar, para calcular los valores correctos de la transacción.
5. Se inserta la transacción (acreditada o rechazada) en la tabla de Transacciones.
6. La inserción dispara una notificación hacia el microservicio de **Notificaciones**.
7. Notificaciones consulta la **URL configurada por el comercio/entidad** para el tipo de evento correspondiente, y envía el `POST` del webhook.

### Tipos de evento

| Tipo de evento | Cuándo se dispara |
|---|---|
| **Pago** | Transacción acreditada o rechazada |
| **Devolución / Contracargo** | Se procesa una devolución (gestionada también por el microservicio de Transacciones, que le avisa a Notificaciones) |
| **POS asociado** | Se asocia un POS a una caja, por cualquier vía (ver detalle abajo) |

Cada comercio/entidad puede configurar **URLs distintas por tipo de evento** — ej. una URL para eventos de pago y otra para eventos de contracargo.

> **Evento "POS asociado"** (fuente: Jira IDEA PRD-51 "MOPAGOS: requerimientos específicos", cliente Mopagos/entidad Malaga). La IDEA original pedía 3 cosas puntuales de Mopagos: (1) que sus comercios nacieran con caja `soloOrden=false` por defecto, (2) canal Botón Simple habilitado por defecto, y (3) este webhook de "POS asociado". Solo la (3) llegó a construirse — las otras dos quedaron sin ticket de desarrollo propio. **Mopagos dejó de ser cliente de Bind PSP** (comentario del PM en la IDEA, 2026-01-29: "no hace falta seguir con el soporte de implementación"), pero el evento quedó como funcionalidad genérica disponible para cualquier entidad. Se activa/desactiva por entidad como cualquier otro tipo de evento, con esquema de reintentos estándar. Payload mínimo: `serial` (del POS), `codigoCaja`, `codigoSucursal`, `codigoComercio`, `cuit`, `razonSocial`, `nombreFantasia`, `fechaActualizacion`. Ticket [AD-13](https://bindpsp.atlassian.net/browse/AD-13), Story Points reales = 0 (ajuste menor de mapeo), release AD 65 (2025-11-17).

⚠️ Nota de aclaración registrada en la sesión: hay que distinguir el **webhook que Bind PSP envía al cliente** (lo descripto en este documento) del **webhook/aviso que el banco/Coelsa nos envía a nosotros** (ver el flujo de Coelsa en [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md)) — son conceptualmente similares pero direcciones opuestas y no deben confundirse al leer un diagrama de flujo.

## Detalle por canal

### POS (tarjeta presente)
`Dispositivo POS → GP (Global Processing) → Pago Externo → Workflow → Transacción → Notificaciones`

✅ **Aclarado (2026-07-02):** el disparador del webhook **no depende del canal**, sino del **cambio de estado de la transacción a ACREDITADA o RECHAZADA** (paso 5 del flujo genérico, arriba). Como toda transacción de POS pasa por ese mismo cambio de estado al insertarse en Workflow/Transacción, el webhook se dispara igual que en cualquier otro canal — no hay nada específico de POS que lo omita. Confirmado por el usuario, cerrando la duda que el equipo tenía abierta en la sesión original.

### QR (cobro con Transferencia 3.0/3.1)
`Billetera → Coelsa → microservicio interno "QR" (expone el endpoint que Coelsa consulta) → Workflow → Transacción → Notificaciones`

- Antes de la confirmación final, se crea una transacción en estado **"en proceso"**.
- El disparador real hacia Workflow es el evento **"QR confirma débito"** de Coelsa (ver paso a paso completo en [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md#parte-2--flujo-de-pago-qr-con-coelsa-transferencia-3031)).

### Recaudación por Transferencia
`Banco Industrial avisa transferencia entrante → microservicio "Financial" (también referido como "CB Collect" — crea CVUs y transferencias) → si el CVU tiene un ID caja asociado (collector vinculado a una caja) → Pago Externo → Workflow → Transacción → Notificaciones`

- ⚠️ **Si el comercio no tiene el convenio de "Recaudación por Transferencia" habilitado, la transacción NO se inserta** — queda registrada con estado de error dentro de las tablas del microservicio Financial. Existe (según lo mencionado en la sesión, sin confirmación completa del endpoint exacto) un mecanismo para **reintentar manualmente** la inserción de esas transacciones "atascadas" mediante un endpoint específico.
- **Con QR este reintento manual no aplica** — el flujo de QR no pasa por el mismo punto de control de convenios que la recaudación por transferencia.
- **Distinción importante señalada en la sesión** (con cierta confusión inicial entre los participantes, luego aclarada): la recaudación por transferencia **sin vincular a un collector/caja** ("nace y muere en Financial", sin llegar nunca a Pago Externo si no hay caja asociada) es un concepto distinto del producto **Agente de Cobros y Pagos** — no deben confundirse aunque compartan el mismo microservicio base (`Financial`/`CB Collect`).

#### Mecánica CVUCollect (vínculo Entidad→Collector→Caja→CVU) — Epic histórica "Integración RxT con Centralizador"

Detalle técnico concreto de la vinculación mencionada arriba, relevado de la Epic histórica de Notion (15 tickets, todos Funcional salvo 1 Pendiente sin desarrollar):

- **A nivel Entidad**: se guarda como Especificación (`EspecificacionTipo`) el **`idCollector`** que vincula a la Entidad con CVUCollect — se envía como dato adicional en alta/modificación de Entidad. Sirve para validar en el ABM de cajas si es obligatorio tener CVU.
- **A nivel Caja**: una caja puede tener asociado **un único CVU y un único alias** (ambos opcionales, campos independientes). Reglas de unicidad estrictas: un CVU no puede estar en más de una caja, y viceversa.
  - **Crear CVU para una caja**: Cobro llama a CVUCollect con `xentidad = idCollector` de la entidad, `nombre`/`CUIT` del comercio dueño de la caja, y `clientid = idCaja` (sin el prefijo "B"). El CVU resultante queda guardado asociado a la caja.
  - **Eliminar CVU de una caja**: si CVUCollect no puede eliminarlo, debe devolverse el error tal cual sin borrar el vínculo local (evita quedar desincronizado). Al eliminar una caja completa, debe eliminarse también su CVU asociado — y si falla la eliminación del CVU en CVUCollect, **no debe eliminarse la caja** (mismo principio: no desincronizar).
  - **Asignar/consultar alias**: análogo al CVU — mismo patrón de propagar el error de CVUCollect tal cual si la operación falla.
- **Transferencias entrantes**: CVUCollect notifica a Bind PSP vía un endpoint que distingue dos tipos de transferencia — **monto abierto** (asociada a un código de caja, pago recurrente) y **monto cerrado** (marcada como pago único, con id de orden de deuda). Cada transacción de este canal se registra con forma de pago `"Transferencia"` y plazo de liquidación + comisión configurable **por medio de pago y por comercio** (no es un valor fijo del canal, cada comercio puede tener condiciones distintas).
- **Filtrado de estados no definitivos** (bug de diseño corregido): Cobro **no soporta actualización de estados** de una transacción ya informada por Pago Externo — por eso CVUCollect solo debe informar transferencias en **estado definitivo** (`COMPLETED` → se informa como `ACREDITADO`), nunca en estados transitorios (`IN_PROGRESS`, `AWAITING_CONFIRMATION`, `UNKNOWN`, `GENERIC_ERROR`), sin importar si el dato definitivo llega por webhook del banco o por conciliación posterior.
- El **alias del CVU** que recibió la transferencia se envía a Pago Externo en el campo `identificadorReferencia` del webhook estándar (ver tabla de atributos arriba, §1).
- Prueba de estrés registrada en el histórico: **proceso asíncrono de Pago Externo** validado con 2000 tx/hora sostenidas durante 2+ horas en paralelo sobre dos entidades de prueba, midiendo % de éxito de inserción/cálculo de impuestos y la posibilidad de reprocesar manualmente cualquier transacción que quedara con error (vía endpoint "Pago General") — mismo patrón de validación de robustez usado después en Newpay PMC MVP (ver [liquidaciones_y_devoluciones.md](devoluciones_y_contracargos.md#liquidador-histórico-de-clientes-traditum-y-newpay-pmc)).

##### Cambio de categorización — CBU externo → CBU corto en CBU Collect (AD V72, 27/08/2026)

> Fuente: Reunión "Análisis de riesgos AD V72" (2026-08-21), minuta Gemini — sección Decisiones, "Categorización de transferencias CBU" y Detalles ([01:09:40]).

En el lote de despliegue de AD V72 (27/08/2026) se corrige la catalogación de las transferencias entrantes desde un **CBU externo hacia un CBU corto** en CBU Collect: hoy se registran/notifican como si fueran de CBU largo, y a partir de este cambio se van a registrar (y notificar por webhook) como `transfer.cortau` (`cortau receipt`).

**Es un cambio de contrato del webhook** — Matias Alzogaray advirtió explícitamente que puede afectar a entidades que controlan/filtran por ese campo de tipo, y mencionó como caso concreto al cliente **Jugadón** (Grupo Slots). Se acordó evaluar el impacto y avisar con anticipación a los clientes involucrados antes del pase.

##### Lado Wallet del mismo mecanismo — ciclo de vida del CVU asignado a una deuda

> Fuente: reuniones "Join Soporte Clientes" (2026-06-17), "Canales y BS" (2026-06-18), "rxt" (2026-06-25) y "Análisis COBRO" (2026-07-20), minuta Gemini. Mismo concepto de CVU de arriba, visto desde el lado Wallet/Deuda — reciclaje del CVU una vez pagada la deuda que lo usó.

- **Ciclo de vida:** al pagarse una deuda en su totalidad, el CVU asociado se marca con fecha de baja y queda inhabilitado; tras un **período de espera de 48 horas** vuelve a estar disponible para reasignar, priorizando los CVU con más antigüedad desde la baja. **Con pago parcial, el CVU NO se libera** hasta que la deuda venza o la entidad la cancele manualmente — puede quedar disponible para el usuario un tiempo prolongado, riesgo operativo señalado explícitamente en la sesión.
- **Asignación bajo demanda (Botón Simple 2.0):** para evitar generar CVU innecesarios, el sistema se lo asigna a una deuda **recién cuando el usuario elige la opción "transferencia"** como medio de pago (no al crear la deuda) — valida antes que la deuda no esté ya paga.
- **Bug de creación masiva por lote (detectado 2026-06-17):** la generación de lotes de CVU fallaba por no completar correctamente el código de colector, generando inconsistencia entre el CVU mostrado en la interfaz y el CVU real procesado — afectó a clientes reales (Fabacar, Bupra). Corregido durante la sesión del 06-18.
- **Gap de auditoría (sin ticket, 2026-06-18):** no existe historial que registre qué CVU fue asignado a qué deuda en cada momento — dificulta atender reclamos de clientes. Propuesta discutida (no confirmada como implementada): agregar el ID de deuda a la tabla de medios de pago disponibles.
- **Concurrencia (gap sin ticket, 2026-06-18):** bajo ciertas condiciones (ej. un usuario con QR y transferencia habilitados simultáneamente) el sistema puede asignar el mismo CVU a dos deudas distintas por falta de control de acceso concurrente.
- **Propuesta de negocio discutida (sin decisión, 2026-06-18):** evaluar si el modelo de reciclaje de CBU sirve para todo tipo de cliente, o si para entidades con clientes repetitivos conviene un modelo de asignación fija en vez de reciclado; y si extender la ventana de 48hs (ej. a 15 días) con el costo de los lotes extra trasladado al cliente.
- **🆕 Pedido urgente de cliente (Bupra Ripsa, 2026-07-20):** el webhook que se dispara al crear una deuda no incluye hoy el **motivo de la deuda** (que debe incluir el CUIT de la persona). Bupra Ripsa lo necesita para conciliar correctamente — detectaron discrepancias entre quién debería transferir y quién efectivamente lo hace. Requiere sumar el campo al payload del webhook de creación de deuda; dado que el pedido es urgente, el equipo evalúa un hotfix en vez de esperar la próxima versión. Ver `tareas_producto.md` T-040.

### Botón Simple
`Se crea un registro en la tabla "payments" del microservicio "CardNotPresent" (también nombrado "CarnPresent" en la sesión) → al abrir el link, CardNotPresent consulta las "reglas de pago" del comercio (determina si se muestra débito, crédito, o ambos) → al confirmar el pago, procesa contra el procesador configurado (hoy 100% Decidir — no hay integración con Cybersource en este canal) → si aprueba, actualiza "payments" y pasa el resultado a Pago Externo → Workflow → Transacción → Notificaciones`

- Antes de procesar el pago, el flujo también **consulta a Ardid** (a través de un microservicio intermedio, no una llamada directa) para el análisis antifraude — consistente con lo ya documentado en [adquirencia_overview.md](../../../2_areas/overview_productos/overview_adquirencia.md#integraciones-con-otros-productos) ("se analiza cada intento de cobro con tarjeta no presente... antes de cursarse").
- **Riesgo operativo documentado:** pueden quedar registros en `payments` marcados como acreditados que **no llegan a insertarse como transacción** por fallas de comunicación puntuales entre microservicios (ejemplo citado: "tengo 100 links de pago acreditados en `payments` pero solo 98 transacciones de Botón Simple" en la tabla de Transacciones). No se confirmó en la sesión la existencia de un mecanismo de reconciliación automática para este desajuste.

## Extensibilidad — agregar un nuevo medio de pago

Ejercicio discutido en la sesión (caso hipotético: agregar "Pago Fácil" como nuevo medio de pago):

- Si el nuevo canal **resuelve el pago correctamente y se lo pasa a Pago Externo** con el formato esperado, **no hace falta modificar Workflow, Transacción ni Notificaciones** — el webhook se dispara automáticamente con el **mismo modelo de atributos**, cambiando solo los valores específicos (ej. el identificador de procesador pasa de "Coelsa" a "Pago Fácil").
- La única causa real por la que un webhook **no llegaría a enviarse**, una vez que la transacción se acredita correctamente, es que **la URL de notificación configurada para ese comercio/evento sea inválida** (mala configuración del lado del comercio, no un problema del disparador interno).

## Glosario de microservicios internos mencionados

| Microservicio | Rol |
|---|---|
| **Pago Externo** | Punto de entrada común que recibe el resultado de pago de cualquier canal y lo pasa a Workflow. |
| **Workflow** | Único trabajo: insertar transacciones, previa consulta de convenios (comisión, plazo de liquidación). |
| **Notificaciones** (también referido como "WF Sender" en el diagrama de la sesión) | Dispara los webhooks salientes hacia los comercios/clientes, consultando la URL configurada por tipo de evento. |
| **Financial** (también llamado **CB Collect**) | Gestiona transferencias entrantes, creación de CVUs, y la lógica de Recaudación por Transferencia / Agente de Cobros y Pagos. |
| **CardNotPresent** (también "CarnPresent" / Botón Simple 2.0) | Gestiona los links de pago de Botón Simple (tabla `payments`), reglas de pago del comercio, y la integración con Decidir. |
| **QR** (nombre no confirmado con certeza en la sesión) | Microservicio que expone el endpoint que Coelsa consulta durante el flujo de pago QR. |
| **GP (Global Processing)** | Procesador de pagos con tarjeta presente (canal POS). |

## Modernización de Webhook Sender (Wallet V71.2, 2026-07-21) y mecanismo de contingencia manual

> Fuente: Reunión "Emisión V 71.2 - Análisis de riesgos" (minuta Gemini, 2026-07-21). Complementa el gap de `tareas_producto.md` T-007 (procedimiento de reenvío manual de eventos "botón rojo").

- **Motivo del cambio:** el componente Webhook Sender actual está obsoleto y genera errores constantes — comparado en la reunión con "actualizar de Windows 7 a Windows 10/11". La nueva versión fue probada en entornos de prueba durante más de 6 meses; el despliegue es parcial (reinicio gradual de nodos) para minimizar riesgo de interrupción.
- **Riesgo confirmado, sin mitigación automática:** durante el reinicio de los microservicios puede haber **pérdida de notificaciones salientes** — no existe hoy un mecanismo automático de contingencia para retransmitirlas.
- **Mecanismo de recuperación manual (esto es lo que resuelve el gap T-007):** los mensajes quedan persistidos en la base de datos de notificaciones; ante pérdida, se recuperan **editando manualmente los estados en la tabla correspondiente** para forzar el reenvío. Validación post-despliegue: comparar los registros de notificaciones enviadas contra los datos de WebhookSender **5 minutos después** de completada la actualización, vía consultas SQL preparadas de antemano.
- **Hallazgos técnicos puntuales del mismo despliegue:**
  - **API de Feriados:** se cambia la invocación para apuntar directo a la IP del balanceador interno en vez de pasar por APIM — mejora de bajo riesgo.
  - **Conciliación de transferencias entrantes:** fix que corrige la obtención de datos del comprador validando correctamente los campos CVU/CBU — bajo riesgo.
  - **Reportes de movimientos (código PSP0):** los archivos se generaban correctamente pero en una ubicación incorrecta — requiere atención durante el despliegue para que el microservicio de reportes los procese bien.
  - **Estado de auditoría de PagosQR:** el bug venía de interpretar datos **nulos como distintos de cadenas vacías** provenientes de Coelsa — fix implementado, se mantiene vigilancia sobre la calidad del dato entrante.
  - Propuesta a evaluar (no implementada): bajar el timeout del monitor de pagos de 7s a un valor menor para reducir la tasa de fallos.

## Webhook de Cobro QR exitoso — nuevos campos de arancel aceptador (acordado 2026-08-31)

> Fuente: reunión "Análisis COBRO" (2026-08-31). Ver también [boton_simple_2_0.md §8.1](boton_simple_2_0.md) para el resto de las definiciones de la misma reunión (QR Tarjeta post-payments).

Se acordó agregar al webhook de transacción exitosa de **Cobro con QR** tres campos nuevos: **arancel aceptador (porcentaje)**, **arancel aceptador (importe)** e **importe neto** (tras aplicar el arancel). Objetivo explícito: que el consumidor del webhook no tenga que hacer una llamada adicional de consulta de la transacción para obtener estos datos — hoy solo vienen en el detalle vía API, no en el evento. Sin ticket específico identificado en la minuta más allá del compromiso genérico del equipo. Pendiente de definir si va dentro del objeto de mensaje de pago o como info adicional, para no romper integraciones existentes (mencionado en el item de fuente de `boton_simple_2_0.md §8.1`).

También en la misma reunión: se retoma la segunda parte de las mejoras de performance para la generación de archivos (liquidación/rendiciones), tras haber cerrado la primera parte en una corrida anterior — Nicolás Colón consulta con "Euge" si las demoras/errores detectados están relacionados con el rendimiento de la API antes de avanzar. Sin detalle técnico adicional en la minuta sobre qué archivo/proceso puntual.

---
*Ver también: [mecanica_qr_coelsa.md](mecanica_qr_coelsa.md) para el detalle específico del canal QR que alimenta este flujo de notificaciones.*
*Última actualización: 2026-09-02 — `/context_merge`: nuevos campos de arancel aceptador en el webhook de Cobro QR exitoso.*
*Última actualización anterior: 2026-08-27 — `/context_merge`: nueva sección en la mecánica CVUCollect (cambio de categorización CBU externo→CBU corto como `transfer.cortau`, AD V72, cliente Jugadón).*
