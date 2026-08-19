# Dólar FX (MULC oficial) y Pagos FX — Wallet

> Estado: en producción.

> Fuente: Notion histórico, Epics **"Dolar FX"** (construida, ~100 SP estimados) y **"Pagos FX - deprecado"** (solo analizada, nunca construida — cross-border payments). Distinto del [Dólar CCL](dolar_ccl.md): CCL opera contra bonos en el mercado bursátil (IVSA/Poincenot vía operaciones de compra/venta de títulos); Dólar FX opera contra el **mercado oficial de cambios (MULC)**, regulado por BCRA, vía la misma API Broker de IVSA-Poincenot pero con endpoints y modelo de cuenta distintos.

## 1. Dólar FX (MULC) — construido

### 1.1 Objetivo y modelo de cuenta

Permitir a usuarios de Wallet acceder al dólar oficial (MULC) para compra/venta, consumible tanto por API como desde un front white-label. Requiere dos cuentas nuevas por usuario:

- **CVU** en una cuenta recaudadora en Bind, dependiente de la cuenta recaudadora de IVSA (igual patrón que CCL).
- **CBU en USD "shadow"** (nunca visible al usuario en esta etapa) — es donde "pican" los dólares comprados antes de acreditarse a la cuenta recaudadora en USD de la organización.
- Alta de ambas cuentas ocurre cuando el usuario elige "operar con dólar oficial" y acepta los TyC.

### 1.2 Flujo de compra — diferencia clave con CCL

- **No existe el concepto de "vuelto"**: a diferencia de CCL (que opera bonos con ejecución aproximada, ver [dolar_ccl.md §3.1](dolar_ccl.md)), en FX el precio no es aproximado — es una operación de cambio directa.
- Pasos: consultar horario de mercado MULC → consultar cotización (compra/venta) → crear intención (simula la operación y devuelve gastos, sin comprometer) → aceptar DDJJ FX → ejecutar compra con el id de la intención.
- Al confirmar: se debitan los **pesos de la CVU** del usuario en Bind; los **dólares "pican" en la CBU USD shadow** del usuario y finalmente se acreditan en una **cuenta recaudadora en USD de la PSP** asignada a la organización (proceso transparente para Bind PSP, que solo ve la acreditación final).
- **Experiencia online, transacción asíncrona** (desacoplada) — el usuario confirma en el momento pero la liquidación real ocurre después.

### 1.3 Alcance construido (backlog numerado "US 0 a 13")

Wrapper de integración con API Broker (US 0), consultar cotización FX (US 1), crear intención de compra (US 3), ejecutar compra FX (US 4, el más grande — XL), crear intención de venta (US 5), ejecutar venta FX (US 6), consultar una intención (US 7), monitorear estado de compra/venta (US 8), consultar horarios de mercado (US 9), ajuste de cálculo neto en compra/venta. Toda esta cadena llegó a producción.

**Quedó sin cerrar completamente** (en refinamiento al freeze del Notion): recibir/realizar transferencias en dólares desde/hacia la CBU recaudadora (US 10 y 11 — necesarias para que la organización pueda mover los USD ya acreditados), conciliar esas transferencias (US 12), y consulta de saldo de cuenta en dólares (US 13, "Cuentas multimonedas - Fase 1"). Es decir: el circuito de **comprar y vender** dólar FX está completo, pero el circuito de **mover los dólares una vez obtenidos** (transferir, conciliar, consultar saldo multimoneda) no se terminó de construir según el histórico — verificar estado real en Jira.

### 1.4 Documentación técnica de referencia

Toda la integración se documenta en el portal de API Broker de Poincenot: `apibroker.pcnt.io/#dolar-fx` (marketdata, intención, ejecución) — mismo proveedor que Dólar CCL, pero namespace `/investment-operation-flow/v1/exchange/fx/` en vez del de bonos.

## 2. Pagos FX — analizado, nunca construido ("deprecado")

> Epic con PRD completo (9 documentos de Definiciones: PRD, "Por qué", "Qué", "Cómo", APIs de Mastercard Move, notas y minutas) pero **cero tickets en Backlog** — quedó en fase de discovery/diseño y se marcó deprecada sin pasar a desarrollo. Se documenta igual porque es un análisis de mercado y de solución completo, útil si se retoma la idea.
>
> ⚠️ **Actualización 2026 (vía `/sync_releases`, 2026-07-09):** la idea efectivamente **se retomó** como iniciativa Jira viva (PRD-10 "Pagos FX PRIMER MVP - APIs" + PRD-119 Portal + PRD-183/184) y parte del diseño de esta Epic ya está **construido y en producción**: el **Wrapper de Mastercard Move completo se publicó en W 67.4 (2026-02-19)** — 8 endpoints pasamanos + autenticación OAuth 1.0 vía AuthExternal — y el MS orquestador `Wallet.CrossBorderRouting` en W 68 (2026-03-11). El "nunca construido" de esta sección aplica a la Epic Notion original (el flujo end-to-end de aquel diseño), no al estado actual de la iniciativa — PRD-10 es proyecto de Luciana Rudaz, vive en su propio Cerebro desde 2026-08-13.
>
> **APIs de Pagos FX publicadas en W 70 (2026-05-27), tickets WS-1024/WS-1045/WS-1048:** (1) noveno wrapper de MC Move: **Bank Information Lookup**; (2) nuevo endpoint cliente-facing **Consultar información del Banco Beneficiario** — recibe `idCuenta` + `paisDestino` + `bic`/`nombreBancoDestino` (no pueden ser null en conjunto), valida que la organización esté habilitada por especificación y que el país esté dentro de los **corredores habilitados** para esa organización, y devuelve la información estandarizada del banco según Mastercard, que el front usa para completar `informacionBancoDestino` en el alta de beneficiario (reduce rechazos en la ejecución de pagos); (3) los GET Movimientos y CuentaCorriente agregan `idBeneficiario` y `concepto` dentro del objeto de detalle de Pago FX.

### 2.5 W 68 (2026-03-11): cotización y validación de beneficiarios — el primer tramo de las APIs FX

> Tickets WS-159, WS-219, WS-313, WS-320, WS-321, WS-326 (recuperados del export XML; este grupo era el "hueco" que la API de Jira no dejaba enumerar).

- **Consulta de Cotización FX** ([WS-159](https://bindpsp.atlassian.net/browse/WS-159), 15 SP): cotización **compuesta** — internamente consulta la cotización CCL (ARS→USD) y la Quotes API de MC Move (USD→moneda destino). Modalidades **forward** (fijo el monto origen ARS) y **reverse** (fijo el monto destino), mutuamente excluyentes; moneda/país origen siempre ARS/ARG; USD como moneda de liquidación ante MC; `tipoPago` B2B/B2C/P2B/P2P; permite margen/comisión adicional en la fijación del precio (en el MVP, cargo = fee de MC y X=0). La cotización se persiste (mismo id que después confirma el pago) y **expira a los 15 minutos**; `montoDebito = montoOrigen + cargo`.
- **Corredores habilitados v1** ([WS-219](https://bindpsp.atlassian.net/browse/WS-219)): consulta de pares país+moneda habilitados por organización (en W 69 se amplió con `tipoPago` e `instrumentoPago`, WS-585).
- **DDJJ del pago** ([WS-326](https://bindpsp.atlassian.net/browse/WS-326), 7 SP): endpoint que devuelve el texto legal vigente a aceptar por el titular y un `idDDJJ` (hash que encripta fecha de lectura + código del texto, para trazabilidad ante actualizaciones del legal) — requisito obligatorio para ejecutar el pago. Corregido posteriormente por WS-704.
- **Validar dirección del beneficiario** ([WS-321](https://bindpsp.atlassian.net/browse/WS-321)): adaptador de la Address Validation API de MC — estados Válida / Parcialmente válida / Inválida, devolviendo la dirección estandarizada que el front usa en el alta.
- **Validar cuenta del beneficiario** ([WS-320](https://bindpsp.atlassian.net/browse/WS-320)): orquestador único de las Account Validation APIs — rutea por tipo de instrumento (**IBAN** vs **ASV**/cuenta bancaria, con `beneficiaryDetails` obligatorio si no es IBAN), verifica estructura, cuenta activa y coincidencia de titularidad (`nameMatch`), informando el motivo específico de rechazo según códigos de MC.
- **MS Mastercard** ([WS-313](https://bindpsp.atlassian.net/browse/WS-313)): configuración base del microservicio contra MC (⚠️ el ticket contiene credenciales sandbox pegadas en texto plano — registrado como gap de seguridad).

### 2.6 El core de las APIs de Pagos FX se publicó en W 69 (2026-04-29) — vía `/sync_releases`

La versión W 69 contiene el corazón funcional de Pagos FX, ya en producción:

- **Ejecutar un Pago FX** ([WS-318](https://bindpsp.atlassian.net/browse/WS-318), 15 SP): el endpoint orquestador end-to-end — valida `idCuenta` (org habilitada), `idCotizacion` no expirada, `idBeneficiario` HABILITADO e `idDDJJ` (hash de la Declaración Jurada); retiene fondos ARS con comprobante de débito (`PagoFX`); ejecuta la **compra de CCL en línea** en el broker (si falla, reversa con comprobante `DevolucionFX`); confirma la cotización en Mastercard Move y dispara el pago. Campos agregados por negocio: `concepto` con valores permitidos (HONORARIOS, IMPORTACIONSERVICIOS, IMPORTACIONBIENES, MARKETING, REGALIAS, LICENCIAS, FRANQUICIAS, CAPACITACIONES, LOGISTICA, ARRENDAMIENTO, SUSCRIPCIONES, DIVIDENDOS, HOSTING) y `documentacionRespaldatoria` (pdf/jpg/png). ⚠️ Se publicó habiendo probado el end-to-end **solo con el corredor Canadá / tipo B2B** — la variabilidad de corredores y tipos de pago quedó pendiente de prueba (decisión de negocio por tiempos).
- **Operaciones directas de Investment** ([WS-721](https://bindpsp.atlassian.net/browse/WS-721), 15 SP): endpoint interno de ejecución directa de compra/venta de activos (CCL, cripto a futuro) **a nombre de Bind PSP** para saldar los USD de la operatoria FX — sin "intención de compra" previa (a diferencia del flujo retail), con tabla propia (`OperacionesCCLDirectas`), riel configurable por especificación de la organización y URL de notificación PCNT separada de la de usuarios finales. Decisión de negocio explícita: **no hay webhooks a organizaciones por las compras CCL directas**.
- **Webhook `PAGO_EXTERIOR_RESULTADO`** ([WS-408](https://bindpsp.atlassian.net/browse/WS-408), 15 SP): aviso a la organización del resultado final del pago (SUCCESS/FAILURE) con `redId` (transaction_reference de Mastercard), tasa de cambio, comisiones, beneficiario y `motivoRechazo` (del riel MC o de API Broker según dónde falló). Nota histórica: la recepción de webhooks reales de MC estuvo bloqueada un tiempo por falta del certificado de seguridad que exige Mastercard.
- **Conciliación contra Mastercard** ([WS-720](https://bindpsp.atlassian.net/browse/WS-720)): background service cada 30 minutos consulta los pagos PENDIENTES respetando el **rate limit de MC** (no consultar el mismo pago más de 1 vez cada 30 min; cache del estado en base).
- **Consultas**: pagos FX por `idOperacion`/`idRed`/`idExterno` sobre los endpoints estándar de consulta de operaciones ([WS-373](https://bindpsp.atlassian.net/browse/WS-373)); lista de movimientos FX con filtros y paginado ([WS-717](https://bindpsp.atlassian.net/browse/WS-717)); beneficiario puntual por `idBeneficiario`/`idExterno` ([WS-707](https://bindpsp.atlassian.net/browse/WS-707)); lista de beneficiarios por cuenta ([WS-371](https://bindpsp.atlassian.net/browse/WS-371)); corredores habilitados ahora devuelven también `tipoPago` e `instrumentoPago` ([WS-585](https://bindpsp.atlassian.net/browse/WS-585)).
- **Beneficiarios**: `idExterno` opcional en el alta para conciliación del lado de la organización — **sin validación de unicidad, responsabilidad del cliente** ([WS-627](https://bindpsp.atlassian.net/browse/WS-627)). Décimo wrapper MC Move: **Account Validation Push Notification** ([WS-817](https://bindpsp.atlassian.net/browse/WS-817)).

### 2.6bis Primer PagoFX productivo real (2026-08-14) — sin webhooks de estado del lado de Mastercard

> Fuente: informe semanal de Fintexa "Informe Estado Proyectos Emisión al 14/08/2026" (Nicolás Pomponio). Épica "Mastercard Move (Pagos Crossborder)" — iniciativa de Luciana Rudaz (PRD-10).

**Hito:** se realizó la **primera transacción crossborder de Pagos FX en ambiente PROD**.

**Hallazgo operativo:** no se observó la llegada de webhooks por cambios de estado de pago del lado de Mastercard — se solicitó información al proveedor. El pago terminó resolviéndose por **consulta de estado vía BGS**, no por webhook. Se sigue dando soporte al negocio y analizando resultados del ambiente productivo, detectando ambigüedades y levantando nuevos tickets para el MVP2.

**Avance en STG (MVP2):** se detectaron ajustes al flujo de alta de beneficiario a partir de diferencias observadas en PROD. Fixes en curso: contemplar campos opcionales con obligatoriedad condicional (special notes) en la consulta del Endpoint Guide; obtener datos del sender para asociarlos al alta de beneficiario; excluir `purpose_of_payment` de la validación y persistencia en el alta de beneficiario; validar `purpose_of_payment` en la ejecución de un pago FX.

**Alerta de alcance:** se agregaron 4 nuevas historias de usuario al MVP2 no contempladas en el alcance inicial de la versión W 72.1 — riesgo sobre los plazos comprometidos, señalado explícitamente por el equipo.

**Próximos pasos:** esperar respuesta de Mastercard sobre los webhooks faltantes; colaborar con el front del portal en soporte de configuraciones.

### 2.7 Portal Web de Pagos FX — el perfil (b) del §2.2 se construyó (vía `/sync_releases`, Adquirencia)

> Tickets [AD-966](https://bindpsp.atlassian.net/browse/AD-966) (15 SP, Módulo Operaciones), [AD-965](https://bindpsp.atlassian.net/browse/AD-965) (7 SP, Módulo Gestión Destinatarios) y [AD-703](https://bindpsp.atlassian.net/browse/AD-703) (15 SP, Módulo Pagos al Exterior y Dashboard resumen), Epic **"Pagos FX - Portal Web"**, publicados en **AD 70.1** (2026-06-24) — encontrados en el backfill del espacio **AD** (Adquirencia), no WS. Confirma el perfil (b) descripto en §2.2 ("el que quiere una plataforma web/app lista para cargar beneficiarios, fondear y pagar sin integrarse"): efectivamente se construyó como un portal propio (`commerce-staging.epays.services/fxpagoqa`, login por organización tipo Física), con wizard de "Hacer un pago" (selección de beneficiario → confirmación → pantalla "Transferencia en proceso"), módulo de gestión de destinatarios/beneficiarios, módulo de "Mis Operaciones" (histórico, con opción de "repetir operación") y un dashboard resumen. Bugs de UX menores publicados en la misma tanda ([AD-1251](https://bindpsp.atlassian.net/browse/AD-1251)/[AD-1239](https://bindpsp.atlassian.net/browse/AD-1239)): doble spinner de carga simultáneo, y el cartel de "operación en proceso" desaparecía demasiado rápido (se corrigió consultando el estado real de la operación antes de navegar, en vez de asumir éxito apenas responde la cotización).
>
> **Nota de arquitectura**: este portal corre sobre la infraestructura de **Adquirencia** (`commerce-staging.epays.services`, mismo dominio que el Portal Comercio de Adquirencia — ver [adquirencia/configuracion_entidades_y_comercios.md](../adquirencia/index.md)), aunque el producto de negocio (Pagos FX) es transversal Wallet/Adquirencia. Confirma que el Portal Web/Admin mencionado como reutilizable en §2.2 es efectivamente el stack de Adquirencia.

### 2.1 Problema de negocio

El área de COMEX del banco (Banco Industrial) empezó a derivar a Bind PSP clientes que necesitaban pagos al exterior pero no encajaban en su apetito de riesgo. Paralelamente, PyMEs/importadores/exportadores se acercaban buscando soluciones cross-border. Contexto: fuertes restricciones cambiarias en Argentina, procesos COMEX lentos/burocráticos/caros, y una tendencia de mercado creciente (+100MM USD/año en LatAm según Mastercard).

### 2.2 Propuesta de valor y modelo

- **Dos perfiles de cliente externo**: (a) el que quiere integrarse por API para dar su propia experiencia de pagos FX, y (b) el que quiere una plataforma web/app lista para cargar beneficiarios, fondear y pagar sin integrarse. Más un modelo **B2B2C**: empresas agrupadoras que ofrecen la solución a sus propios usuarios finales.
- **Partners estratégicos definidos**: **API Broker** (misma integración IVSA-Poincenot que CCL/FX) para el lado de cambio de moneda, y **Mastercard Move** como agente pagador/regionalizador en el exterior (cross-border). Reutiliza internamente Wallet Services (cash in), Onboarding (KYC/KYC-C de originantes y beneficiarios) y el Portal Web/Admin.
- **Decisión de arquitectura ya tomada en el PRD**: el cash in se resuelve con **DEBIN recurrente**, y la compra de dólares se hace con **CCL Combi** (ver [dolar_ccl.md §3.8](dolar_ccl.md)) desde una cuenta (Organization) de Bind PSP en API Broker — es decir, Pagos FX iba a **apoyarse en CCL Combi como motor de cambio de moneda**, no en Dólar FX/MULC.
- Requisitos transversales relevados: integración con **ARDID** para monitoreo antifraude punta a punta (originante y beneficiario), DDJJ de no duplicación de vías de pago de importaciones, nueva base de datos para conciliación/auditoría, panel de compliance en tiempo real.

### 2.3 MVP definido (nunca ejecutado)

Alcance MUST HAVE: onboarding de usuario y de beneficiario de pago FX, endpoint de presupuesto, endpoint de confirmación, webhook de aviso aprobado/rechazado — con cash in **exclusivamente por API vía DEBIN**. Evoluciones previstas (no alcanzadas): cash in por DEBIN desde front, cash in con débito de saldo de wallet, y **cobros FX** (dirección inversa, nunca especificada en detalle).

### 2.8 Detalle técnico adicional de "Operaciones directas de Investment" (WS-721) y liquidación con Mastercard

> Fuente: Mail "BIND - MC | mastercard connect" — Luciana Rudaz, 2026-07-17.

Complementa §2.6 (WS-721) con detalle no documentado antes:

- **Modelo de datos:** el endpoint interno de ejecución directa (compra/venta CCL a nombre de Bind PSP, sin "Intención de Compra") persiste en la base **`WalletCrossBorderRoutingDB`**, con tablas dedicadas — entre ellas `dbo.PagosFX`, `dbo.CotizacionPagosFX`, `dbo.EstadosPagosFX`, `dbo.Corredores`/`dbo.CorredoresEspecificaciones`, `dbo.CuentasPagosFXDDJJ`, `dbo.PagosFXBeneficiarios`. Las operaciones directas en sí (`dbo.OperacionesDirecto`, `dbo.EstadosOperacionesDirecto`) viven en una base distinta, **`WalletInvestmentServiceDB`**. ⚠️ **Posible inconsistencia de nomenclatura:** §2.6 documenta la tabla de operaciones directas como `OperacionesCCLDirectas` (vía `/sync_releases`) — no coincide literalmente con `dbo.OperacionesDirecto` de este mail; podría ser el mismo objeto renombrado, o dos capas distintas (tabla de negocio vs. tabla técnica). Sin confirmar — registrado también en `../../../2_areas/gaps_y_preguntas.md`.
  - El sistema valida que el `idCotizacion` (obtenido antes) sea válido y no haya expirado al momento de ejecutar.
  - Al recibir la orden de ejecución/devolución de un Pago FX, Wallet ejecuta la compra/venta de CCL vía la API del Broker con la cotización pactada, y tras confirmar la liquidación de divisas orquesta automáticamente la creación del pago en Mastercard (o la devolución al usuario).
  - Modelo genérico por `idProcesador` (para soportar otros riel a futuro, ej. Cripto) y parametría dinámica por Organización (accountId único de Bind PSP + configuración de qué riel usar).
- **Cuenta prefondeada en Mastercard Move:** Bind PSP mantiene una cuenta prefondeada asignada a su operatoria (símil a las subcuentas que Bind PSP abre a sus propios clientes), desde donde salen los pagos FX. Antes de ejecutar cada pago se consulta en línea el saldo disponible en esa cuenta — si no alcanza, la operación **no se ejecuta** (evita el rechazo posterior de Mastercard por fondos insuficientes). Los dólares comprados en línea por CCL reponen ese fondeo. Al menos en el corto/mediano plazo, es siempre **Bind PSP quien ejecuta a su nombre** los pagos por cuenta y orden de los clientes en el exterior (y por ende las operaciones en IVSA), no un modelo de subcuentas por organización.
- **Archivos diarios de Mastercard para conciliación:** Mastercard entrega 3 archivos por día — **BAR** (todas las transacciones del día que afectaron saldo, agrupadas por divisa), **Status Change Report (SCR)** (transacciones cuyo estado cambió desde el último reporte) y **Daily Transaction Report (DTR)** (detalle de transacciones nuevas del día). La conciliación esperada del equipo de Administración cruza: cuenta banco Bind PSP recaudadora en ARS ↔ Cuenta IVSA ↔ estos archivos de la cuenta de settlement de Bind PSP en Mastercard.
- **Entidad IVSA dedicada "Organización MOVE" (2026-07-28):** para operar este producto, Bind PSP le pide a IVSA crear una entidad nueva en su plataforma (asociada a la cuenta comitente `749049153`), separada de otras organizaciones de Bind PSP en IVSA, con credenciales propias de API Broker (STG y PROD) para consultar cotizaciones y comprar CCL puntualmente para el crossborder de Mastercard Move. Modelo a operar: **senebi (combi)**. Fuente: mail "🔥Nuevas credenciales API Broker para Organización MOVE (Bind PSP)" — Luciana Rudaz, 2026-07-28. Ver también PRD-183 §7 (proyecto de Luciana Rudaz, en su propio Cerebro desde 2026-08-13).
  - **Avance (2026-08-03):** IVSA (Mariano Ferrari, Gastón Degiovanni) confirmó la CBU asociada a la cuenta comitente (`3220001805007490491531`) y que la cuenta se llamará **"BIND PSP - MOVE"** — todavía sin confirmar si la cuenta comitente `749049153` ya existe o la crea IVSA de cero (idas y vueltas sin cerrar en el hilo). En paralelo, Bind (Gonzalo Rivera) compartió con **security@fintexa.tech** las **credenciales de la organización 156 "Pagos FX-QA"** vía enlace cifrado de un solo uso (SendSafely) — a diferencia del incidente de credenciales de MongoDB en texto plano del 2026-07-27 (ver `../../../2_areas/gaps_y_preguntas.md`), acá el canal usado sí es una buena práctica de manejo de secretos.

## Ver también

- [dolar_ccl.md](dolar_ccl.md) — mercado CCL (bonos), incluye el modelo Combi que Pagos FX planeaba reutilizar.
