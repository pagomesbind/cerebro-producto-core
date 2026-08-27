# Cuenta remunerada — FCI

Configuración, consulta y capacitación sobre la funcionalidad de cuenta remunerada por Fondo Común de Inversión (FCI) en Wallet, sustentada en API Broker (IVSA / Poincenot).

---

## 0. Contexto de producto y clientes (PRD, Notion histórico)

> Fuente: Notion histórico, Epic **"FCI - Cuentas Remuneradas - APIs"** (~165 SP estimados, ~49 tickets — la Epic más grande relevada hasta ahora en Wallet).

- **Objetivo estratégico**: reforzar el posicionamiento de Bind PSP como "Fintech as a Service" — que sus clientes wallet ofrezcan a sus propios usuarios inversión automática en FCI sin esfuerzo de integración, para ganar principalidad de uso (evitar ser "solo transaccional") y fidelizar.
- **Clientes objetivo del producto**: **Astropay, WICO, TIN, CENCO, Globant (La Virginia)**.
- **Modelo de negocio**: la organización puede llevarse una comisión extra sobre el rendimiento real del FCI (por encima de la comisión que ya cobra Poincenot/IVSA, incluida en el valor de cuotaparte).
- **Riesgos identificados en el diseño**: caída de API Broker en cotización o en suscripción/rescate, errores de grabación de saldos, fallas por reglas de negocio (cuenta comitente no habilitada, topes de rendimiento), y **actividad de arbitrajistas** — mitigado con reglas de monitoreo en ARDID (que, según la capacitación de abajo, **nunca se llegó a construir** para esta operatoria).
- **Roadmap**: MVP acotado a Onboarding de Personas Físicas, alta de cuenta comitente para mayores de edad, API + App. **Fuera de scope del MVP**: resumen mensual por email, Onboarding de Personas Jurídicas, cuentas de menores (13-17), reservas, y FCI en moneda extranjera.
- **Casos de uso soportados por diseño**: organización con Onboarding propio de Bind PSP; organización con Onboarding propio/de terceros; organización externa con cuentas y CVU en otro PSP (caso real: **CENCO con SBS**) que se integra a Bind PSP solo para la funcionalidad de FCI.

## 1. Introducción — Cuentas remuneradas por FCI (capacitación interna)

### ¿Qué es?

Solución de APIs para invertir los fondos de las cuentas de la organización en un Fondo Común de Inversión (FCI) y, así, remunerar las mismas acreditando rendimientos diarios sobre los saldos.

### ¿Por qué es importante?

- Diferenciación de mercado: permite usar esta funcionalidad a las organizaciones prácticamente sin esfuerzos de integración de su parte.
- Favorece mayores saldos en las cuentas.
- La organización puede obtener una comisión extra sobre el rendimiento real del FCI.

### ¿Qué está alcanzado en este proyecto?

- Proceso automático que realiza todo lo necesario por día y se activa por organización.
- Endpoint para que la organización cree las cuentas comitentes.
- Endpoint para que la organización consulte los datos generales de un proceso.
- Nuevo tipo de evento de webhook que notifica por cada comprobante creado por pago de rendimiento en cada cuenta.
- Mecanismos para atender fallas al momento de suscribir/rescatar.
- Mecanismos de conciliación por posibles diferencias entre la confirmación de suscripciones/rescates de API Broker hasta confirmación de liquidación.

### ¿Qué no está alcanzado?

- No integrada/desarrollada aún en la app marca blanca de wallet ni en el portal comercio.
- No hay herramientas en Ardid para monitorear esta operatoria (posibles fraudes o desarbitrajes de fondos).

### ¿Cómo funciona?

- La organización instruye la creación de la cuenta comitente para cada cuenta que quiere remunerar. El sistema va directo a API Broker a crear la cuenta con los datos que pasa la organización. Cada cuenta comitente está a nombre del titular de la cuenta de wallet.
- Todos los días hábiles, automáticamente, por cada organización habilitada, sobre las cuentas con cuenta comitente asociada:
  1. **Paso 1 (9hs\*):** consulta los valores del fondo de hoy.
  2. **Paso 2 (tras paso 1):** calcula cuánto pagar de ganancias por cuenta, viendo el saldo en la comitente y el aumento del precio de la cuotaparte entre ayer y hoy.
  3. **Paso 3 (tras paso 2):** paga la ganancia a cada cuenta según lo calculado. Inserta un comprobante de crédito por cuenta y dispara un webhook a la organización con el nuevo tipo de evento por cada uno.
  4. **Paso 4 (16hs\*):** registra una foto del saldo actual de todas las cuentas wallet (CVU).
  5. **Paso 5 (tras paso 4):** calcula cuánto suscribir o rescatar de cada cuenta comitente, viendo el saldo en la comitente que quedó de ayer vs. el saldo actual de la cuenta wallet (foto paso 4). Puede no haber movimientos en alguna/s cuenta/s.
  6. **Paso 6 (tras paso 5):** envía las suscripciones y rescates por API a API Broker, armando paquetes. API Broker solo confirma recepción (id de paquete), sin indicar estado definitivo todavía. Al finalizar el envío, se avisa a API Broker el fin de envío.
  7. **Paso 7** (API Broker avisa por webhook que procesó cada paquete, o se esperan 2hs y luego se consultan los estados hasta que estén procesados): calcula y registra el saldo final que quedó en cada cuenta comitente según el resultado de la suscripción/rescate.
  - Fin del proceso. Al próximo día hábil comienza un nuevo proceso que usará estos datos para comparar y pagar ganancias.

  *(\*) Los horarios pueden cambiar según lo requiera el negocio/administración/operaciones.*

- La organización recibe un webhook por cada crédito de rendimiento pagado.
- Puede consultar el TNA actual.
- Puede consultar un resumen del proceso de un día en general.
- Puede consultar listados de rendimientos filtrando comprobantes por el tipo de comprobante de rendimiento.
- El equipo de Administración de Bind PSP concilia, compensa y transfiere a IVSA por el neto suscripto todos los días (si los rescates superaron a las suscripciones, Bind PSP recibiría una transferencia desde IVSA).

### Requisitos para usarlo

- **Comerciales:** en producción debe acordarse con Bind Inversiones qué fondo se usará y las condiciones comerciales; cada nueva organización debe ser creada y configurada específicamente por IVSA.
- **Técnicos:** en producción, API Broker debe indicar la "organization" a utilizar y sus credenciales (dependencia de Poincenot). Deben configurarse parámetros especiales en la organización de Wallet (responsabilidad del equipo de integraciones).

### Consideraciones especiales

- En staging existe una única "Organization" en API Broker ("BPSP") para el ambiente de prueba. Cualquier organización de wallet que use esta funcionalidad debe configurarse con esta organization y credenciales. Esto limita el ambiente: solo se puede correr el proceso de una organización por día, ya que para API Broker es una sola organización aunque para Bind sean distintas.
- En staging, API Broker no procesa automáticamente los paquetes enviados; hay que solicitarles soporte para que los procesen y así poder cerrar un proceso completo de prueba.

---

## 2. Configurar organización para FCI Cuenta Remunerada

**Objetivo:** dejar operativa la funcionalidad FCI cuenta remunerada en una entidad, de modo que pueda crear cuentas comitentes que automáticamente sean consideradas para suscribir/rescatar saldos y se les paguen rendimientos.

### Precondiciones

- Para producción, conocer con qué credenciales la organización consumirá API Broker.
  - Si usará sus propias credenciales, deben solicitarse a IVSA/PCNT (usuario, contraseña, organization), enviarlas por email a `security@fintexa.tech` y crear un Jira a Seguridad Informática de FINTEXA solicitando guardar estos secretos para ser usados contra API Broker para la organización {{nombre}} en el ambiente {{ambiente}}.
- Para producción, IVSA/PCNT debe indicar el código de fondo a usar para la organización.

### Configuraciones

- Crear registro en `WalletCuentaDb > Especificaciones` para indicar con qué código de fondo debe consultar a API Broker por esta organización.

  **En staging:**

  | Scope | Tabla | IdTabla | Clave | Valor |
  |---|---|---|---|---|
  | FCI | Organizaciones | {{organizacionId}} | CODIGO_FCI | IAHAHPE AR |

  **En producción:**

  | Scope | Tabla | IdTabla | Clave | Valor |
  |---|---|---|---|---|
  | FCI | Organizaciones | {{organizacionId}} | CODIGO_FCI | {{código de fondo indicado por IVSA/PCNT}} |

- Crear registro en `WalletCuentaDb > Especificaciones` para indicar cuántos días de proceso se considerarán para calcular el promedio de rendimientos y el TNA del fondo:

  | Scope | Tabla | IdTabla | Clave | Valor |
  |---|---|---|---|---|
  | FCI | Organizaciones | {{organizacionId}} | DIAS_RENTABILIDAD_FCI | 5 |

- Crear registro en `WalletCuentaDb > Especificaciones` para indicar que la organización puede crear cuentas comitentes:

  | Scope | Tabla | IdTabla | Clave | Valor |
  |---|---|---|---|---|
  | Cuentas | Organizaciones | {{organizacionId}} | CUENTA_COMITENTE_IVSA_HABILITADA | true |

- Crear registro en `WalletInvestmentServiceDB > ParametrosOrganizaciones` para asociar la organización a sus credenciales contra API Broker.

  **En staging:**

  | OrganizacionId | PspOwner | Entidad | Procesador | CanalOperacion |
  |---|---|---|---|---|
  | {{OrganizacionId}} | BIND_INTE | BPSP | POICENOT | CCL |

  **En producción:**

  | OrganizacionId | PspOwner | Entidad | Procesador | CanalOperacion |
  |---|---|---|---|---|
  | {{OrganizacionId}} | {{nombre de la organización}} | {{Organization indicada por IVSA/PCNT}} | POICENOT | CCL |

- Solicitar que se incluya la organización en el AppSettings de investment para que pueda operar FCI.
- Crear registros en `NotificacionesParametros` para asociar `NotificacionEventoId=16` (evento `RENDIMIENTOS_FCI`, se envía cada vez que se crea un comprobante de pago de un rendimiento en una cuenta) con la URL del webhook.
- Crear registros en `NotificacionesParametros` para asociar `NotificacionEventoId=20` (evento `RESUMEN_OPERACIONES_FCI`, resumen de todo lo que pasó al finalizar un proceso) con la URL del webhook.

### Solicitud de ejecución en producción

Una vez realizadas las configuraciones y validaciones, se debe solicitar la ejecución del script productivo para habilitar FCI Cuenta Remunerada.

> **Caso real aplicado — Coppel (organización ID 43) en producción:** este procedimiento completo se ejecutó para Coppel vía [WS-1159](https://bindpsp.atlassian.net/browse/WS-1159), publicado como hotfix dedicado **W 69.4 HF (Coppel)** el 2026-05-20 (`CODIGO_FCI=1484`, `DIAS_RENTABILIDAD_FCI=5`, `PspOwner=BIND_COPPEL`, `Entidad=COPP`, procesador `POICENOT`, canal `CCL`). Dato operativo: el `PspOwner` debe coincidir con el valor configurado en el secreto de credenciales guardado por Seguridad de Fintexa.

**Datos a incluir en la solicitud:**
- Ambiente: Producción
- Base de datos: `SharedRemuneraDB`
- Instancia SQL: `sql-wallet-prd-001.database.windows.net`
- Script a ejecutar: `SharedRemuneraDB.sql`
- Organización: `{{organizacionId}}`
- Referencia Jira: `EM-590`

**Ejemplo de solicitud:**

> Ejecutar script en producción Coppel FCI EM-590
> Por favor solicitamos ejecutar el script `SharedRemuneraDB.sql` en la instancia `sql-wallet-prd-001.database.windows.net`, base `SharedRemuneraDB`.
> La ejecución corresponde a la habilitación de FCI Cuenta Remunerada para la organización 43, a solicitud de @Nicolas Pomponio.
> `https://fintexa.atlassian.net/servicedesk/customer/portal/34/EM-602`

---

## 3. Consultar directo datos de FCI a IVSA y correr procesos

Para verificar si el fondo tiene los datos actualizados en IVSA: ir a `http://10.210.1.81/swagger/index.html`, buscar el fondo IAMAHPE AR.

```bash
curl -X 'GET' \
  'http://10.210.1.81/api/v1/MarketData/Price/Fund?code=IAMAHPE%20AR&date=2026-04-14' \
  -H 'accept: application/json' \
  -H 'x-owner: INTER' \
  -H 'x-organización: BPSP'
```

Esto debe devolver una fecha y un precio. Luego, para generar los procesos: `http://10.210.1.129/swagger/index.html`.

**Horarios de proceso (STG):**

| Paso | Horario |
|---|---|
| Paso 2 (cálculo ganancias) | 00:00 hs |
| Copia de saldos (infra) | 14:00 hs |
| Paso 4 (foto de saldo) | 15:00 hs |
| Consulta de paquetes | 4 hs a partir del aviso de fin de procesamiento |
| Duración consulta de paquetes | 2 hs |
| Fin procesamiento (Paso 7) | 6 hs — si no se resuelve en ese tiempo, queda en ERROR |

---

## 4. Mantenimiento post-lanzamiento y ajustes de cálculo (IDEA Jira PRD-103)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA [PRD-103](https://bindpsp.atlassian.net/browse/PRD-103) "FCI Cuenta remunerada" → Epic [WS-1](https://bindpsp.atlassian.net/browse/WS-1) "FCI Cuentas remuneradas: Ajustes finales Poincenot" (62 tickets, 58 retenidos tras excluir Tests). A diferencia de las demás IDEAs de Jira ingeridas hasta ahora, esta Epic **no es una entrega puntual**: es el historial casi completo de mantenimiento de la funcionalidad desde su lanzamiento (release W 65, 2025-11-17) hasta junio 2026 — la Epic más grande de toda la ingesta Jira de este proyecto. Story Points reales sumados ≈87 vs. 5 SP estimados en la IDEA (~17x), coherente con que agrupa 7-8 meses de bugs y ajustes, no una sola feature.
>
> Clientes reales confirmados operando FCI en este período: **Coppel** (organización ID 43, alta en producción documentada en §2 más arriba, `CODIGO_FCI=1484`, procesador `POINCENOT`, `CanalOperacion=CCL`).

### 4.1 Cálculo de ganancias, TNA y saldos — bugs de fórmula

- **Fórmula de ganancia mal aplicada** ([WS-154](https://bindpsp.atlassian.net/browse/WS-154)): se calculaba `B[t] = C[t-1] × (A[t]/A[t-1])` en vez de `B[t] = C[t-1] × (A[t]/A[t-1] - 1)` — sin restar 1, la ganancia diaria salía inflada al valor completo de la posición. Corregido W 65.2.
- **TNA no contempla GAP de fin de semana/feriados** ([WS-301](https://bindpsp.atlassian.net/browse/WS-301)): la TNA se anualizaba asumiendo siempre 1 día entre procesos, inflando el rendimiento anualizado cuando había un feriado/fin de semana de por medio entre el proceso actual y el anterior. Debe ponderarse por la cantidad real de días corridos (`Δd`) entre valuaciones.
- **Fórmula de monto a suscribir/rescatar** ([WS-270](https://bindpsp.atlassian.net/browse/WS-270)): el cálculo original (`FotoSaldoHOY - SaldoComitenteAYER`) terminaba suscribiendo la ganancia del día junto con el movimiento real, porque `FotoSaldoHOY` ya incluye la ganancia acreditada. Corregido a `FotoSaldoHOY - cantCpComitenteAYER × precioHOY`.
- **Cálculo de `cpCantidadSaldo`** ([WS-81](https://bindpsp.atlassian.net/browse/WS-81)): debía calcularse como `cpCantidadSaldoAnterior ± (importeOperado/precioVcp)`, no como una simple suma del importe operado.
- **Redondeos y precisión decimal** ([WS-297](https://bindpsp.atlassian.net/browse/WS-297), [WS-311](https://bindpsp.atlassian.net/browse/WS-311), [WS-331](https://bindpsp.atlassian.net/browse/WS-331)): API Broker/PCNT rechazaba paquetes con `INVALID_TOTAL_AMOUNT_INFORMED` por diferencias de centavos entre la sumatoria calculada con 5 decimales en BD y el total esperado con 2. Se estandarizó a **guardar 2 decimales en todos los resultados de cálculo**, salvo el precio de cuotaparte (`price` del CP) que se amplió a **10 decimales** para no perder precisión cuando el proveedor informa más de 5.
- **Rescate sin validar fondos suficientes** ([WS-167](https://bindpsp.atlassian.net/browse/WS-167)): al no validarse "fondos insuficientes", el sistema forzó un rescate de $37,69 sobre una cuenta con solo $0,90 de saldo real, generando un **saldo de cuotapartes negativo** (`-0.95249`) — bug de regresión encontrado en staging, no confirmado si tiene fix propio o quedó como hallazgo de investigación.
- **Comprobantes de $0,00** ([WS-194](https://bindpsp.atlassian.net/browse/WS-194)): ganancias de valor ínfimo (ej. $0,001368) generaban igual un comprobante visible en $0,00 — se dejó de generar el comprobante en esos casos.
- **Piso de $100 para suscripción/rescate** ([WS-204](https://bindpsp.atlassian.net/browse/WS-204)): API Broker rechaza montos menores a $100 — se agregó validación para no enviarle a PCNT suscripciones/rescates por debajo de ese piso (quedan sin operar ese día, no como error).
- **Control de precio de CP descendente** ([WS-252](https://bindpsp.atlassian.net/browse/WS-252)): si el precio de cuotaparte del día es menor al del proceso de referencia anterior, el proceso debe fallar en el paso 1 con error descriptivo (prioridad baja: igual rompería más adelante al no poder generar un débito por "ganancia negativa").
- **`GetTNA` promediaba procesos en estado ERROR** ([WS-1243](https://bindpsp.atlassian.net/browse/WS-1243), publicado W 70.2 2026-06-10): el endpoint de consulta de TNA incluía en el promedio los procesos diarios que habían terminado en estado ERROR, inflando/distorsionando el valor informado. Regla corregida: solo se consideran para el promedio los procesos en `FINALIZADO_OK` o `INICIADO`; los `ERROR` se excluyen. Precondición para que el cálculo dé el valor esperado: debe existir la especificación `DIAS_RENTABILIDAD_FCI` (valor 5) en la tabla `especificaciones` de `CuentasDB` para la organización consultada.
- **`GetTNA` sin procesos devolvía 500** ([WS-510](https://bindpsp.atlassian.net/browse/WS-510), publicado W 68 2026-03-11): consultar la TNA de una organización sin procesos FCI daba `500 "Sequence contains no elements"` — corregido a `422` con mensaje claro de que no existen procesos para la entidad.

### 4.2 Robustez del proceso diario (pasos 1-7)

- **Copia de saldos**: bugs de regresión donde el paso de copia de saldos no se ejecutaba y el proceso tomaba los saldos del día anterior ([WS-91](https://bindpsp.atlassian.net/browse/WS-91)), o remuneraba una cuenta que no debía porque el estado de "ya rescatada" no se actualizaba entre procesos ([WS-90](https://bindpsp.atlassian.net/browse/WS-90)). Se ajustó además para que **solo copie saldos de cuentas efectivamente habilitadas a remunerar** ([WS-386](https://bindpsp.atlassian.net/browse/WS-386)) y para no considerar cuentas sin saldo ([WS-200](https://bindpsp.atlassian.net/browse/WS-200), no corregido — "No aplica").
- **Paso 4 no continuaba si todas las ganancias daban $0** ([WS-232](https://bindpsp.atlassian.net/browse/WS-232)) — encontrado en una prueba real de producción, tuvieron que insertar el paso a mano.
- **Feriados no evaluados correctamente** ([WS-198](https://bindpsp.atlassian.net/browse/WS-198), no corregido): el proceso rechaza fechas no hábiles pero deja un estado inconsistente que bloquea el día siguiente hábil (no encuentra "proceso anterior FINALIZADO_OK"). Mitigación parcial: [WS-409](https://bindpsp.atlassian.net/browse/WS-409) agregó la posibilidad de **indicar manualmente qué proceso tomar como anterior** (campo `procesoAnteriorFecha`) para destrabar manualmente estos casos.
- **Resiliencia del paso 6 (informe de lotes a PCNT) ante errores 502** ([WS-1374](https://bindpsp.atlassian.net/browse/WS-1374), W 72, 3 SP, Epic WS-54): se detectaron en producción errores `502 BadGateway` de PCNT al generar los paquetes (Suscripciones y Rescates) en el paso 6. Dos problemas de fondo, distintos del cluster de bugs de fórmula/robustez de §4.1: (1) sin reintentos — un error en el paso 6, tanto en Suscripción como en Rescate, no tenía lógica de reintento; (2) pérdida de traza cruzada — el registro de `FCIPasosDetalles` se generaba para el **par** Suscripción/Rescate junto, así que si la Suscripción se informaba OK pero el Rescate fallaba, el registro completo quedaba marcado como ERROR, perdiéndose la traza de que la Suscripción sí se había procesado correctamente en Poincenot. **Refactor:** se separó la clasificación de operaciones (suscripciones/rescates/no-aplican) desde `InformarLoteOperacionesCommand` hacia `CalcularOperacionesCommand`, que ahora arma lotes separados por tipo y publica eventos `InformarLoteOperacionesEvent` que corresponden solo a un tipo (con discriminador agregado al evento); `InformarLoteOperacionesCommand` pasa a informar un único tipo por evento, así una falla al informar rescates ya no descarta la información de suscripciones ya persistida en `FCIProcesoCuenta`/`FCIPasoDetalle`; se incorporó configuración de reintentos de RabbitMQ (`UseMessageRetry`) para el consumo de `InformarLoteOperacionesEvent`, sumada al reintento transitorio existente (do-while) que se mantiene sin cambios. QA no pudo reproducir el 502 directamente (dependiente del proveedor); se validó por regresión general del flujo el 2026-08-07.
- **Reprocesamiento del paso 7** ([WS-387](https://bindpsp.atlassian.net/browse/WS-387), publicado W 68 2026-03-11): se agregó la posibilidad de reprocesar el paso 7 (consulta de paquetes liquidados) las veces que sea necesario para destrabar un proceso — vía el endpoint de ejecución de pasos, con campo `ReconsultaSolicitadaFechaHora` en `FCIProcesos` y parámetro de horas máximas de reconsulta antes de marcar ERROR.
- **Fórmula de `SALDO_MONTO` del paso 7** ([WS-440](https://bindpsp.atlassian.net/browse/WS-440), publicado W 67.4 2026-02-19, SOPORTE): corregido el cálculo a `SALDO_MONTO = SALDO_CP × VALORCP` — aplica también a cuentas que no operaron ese día (transacción "N").
- **"Proceso 0"** ([WS-972](https://bindpsp.atlassian.net/browse/WS-972)): al habilitar FCI en una organización nueva (o con todos sus procesos anteriores en ERROR), ahora puede correr su primer proceso sin necesitar un proceso de referencia previo, simplificando el cálculo (todo el saldo actual se suscribe, sin pago de ganancia).
- **Parámetros del proceso por BD, no por settings** ([WS-354](https://bindpsp.atlassian.net/browse/WS-354), publicado W 67 2026-01-27): horarios de corrida y configuraciones del proceso diario pasaron de appsettings (cambio = deploy riesgoso) a una tabla de parámetros modificable por script.
- **Documentación técnica de FCI entregada como ticket** ([WS-391](https://bindpsp.atlassian.net/browse/WS-391), W 67, 3 SP): Fintexa entregó "FCI - Diagrama de componentes.pdf" y "FCI - Escenarios de error.pdf" (adjuntos en el ticket, no accesibles por API). 📌 Lectura de gestión — queja explícita del PM en el ticket: *"este ticket nunca debió ocurrir: gastamos 3 SP en documentar algo que debió estar implícito en los cientos de SP de tickets de desarrollo de FCI"*.
- **Consulta de paquetes a destiempo** ([WS-82](https://bindpsp.atlassian.net/browse/WS-82)): originalmente el sistema arrancaba a consultar todos los paquetes apenas llegaba el webhook del **primero** procesado por PCNT, ignorando el resto. Se corrigió para esperar el webhook del **último** paquete antes de empezar a consultar.
- **Nuevo paso: registrar liquidación final IVSA** ([WS-80](https://bindpsp.atlassian.net/browse/WS-80)): se agregó el registro de la información final de liquidación de los bundles (montos y cantidades ya liquidados por IVSA, distinto del importe originalmente operado) para poder conciliar diferencias.
- **Error de clave primaria duplicada en el paso 7 (copia de saldos)** ([WS-1234](https://bindpsp.atlassian.net/browse/WS-1234), W 70.1, cerrado "No aplica"): violación de constraint de PK al insertar en la tabla temporal `#CuentasAProcesar` (`SP_InsertarSaldosFCI`), atribuido a un proceso de duplicación de cuentas — no quedó registrado un fix de código confirmado, solo la atribución de causa.
- **`SaldosHistoricos` — mejora de uso de memoria en el DELETE de reprocesos** ([WS-950](https://bindpsp.atlassian.net/browse/WS-950), W 70.1, publicado aún en estado "EN QA"): el borrado de registros existentes ante un reproceso de saldos históricos (`AddSaldoHistoricoCommandHandler`) demandaba memoria excesiva y provocaba errores OOM (Out of Memory) — mejorado el `DeleteAsync`.
- **Incidente de producción por deploy desalineado de EasyNet** ([WS-616](https://bindpsp.atlassian.net/browse/WS-616), publicado W 70 2026-05-27): la migración del evento `AddComprobanteFCIEvent` a la librería EasyNet quedó desplegada **a medias** entre los micros de Comprobantes y Remunera (componentes desalineados) y provocó un incidente de FCI en producción. No se detectó antes porque **Astropay había dejado de operar en PROD** y no había procesos FCI activos que lo evidenciaran. Causa raíz reconocida por Fintexa: la US no tenía el tag de versión para validar dependencias en el deploy. Se corrigió incorporando la US completa a W 70 (decisión de riesgo asumida explícitamente por Fintexa/Nico Pomponio en el War Room, con acuerdo de Pablo Gomes).

### 4.3 Webhooks — formato y contenido

- **Inconsistencia de casing en el campo `evento`**: el webhook de impuestos lo mandaba como `"Evento"` (mayúscula) en vez de `"evento"` como el resto ([WS-269](https://bindpsp.atlassian.net/browse/WS-269)).
- **Webhook de resumen (`RESUMEN_OPERACIONES_FCI`, evento id=20)**: le faltaban los campos estándar `mensajeId` y `evento` presentes en el resto de los webhooks de Wallet ([WS-307](https://bindpsp.atlassian.net/browse/WS-307)); no se disparaba en absoluto cuando un proceso no tuvo operatoria ese día ([WS-393](https://bindpsp.atlassian.net/browse/WS-393)); y los contadores `CantidadCPOperadasSuscripciones`/`...Rescates` quedaban siempre en 0 en vez de reflejar el total real operado ([WS-984](https://bindpsp.atlassian.net/browse/WS-984), luego expuesto también en el GET del resumen — [WS-610](https://bindpsp.atlassian.net/browse/WS-610)).

### 4.4 Cuenta Comitente — endurecimiento del endpoint de alta (`POST .../CuentaYCVUConCuentaComitente`)

> Ver también [otros_manuales.md §4](index.md) — documentación de referencia para integradores externos sobre las validaciones del objeto `cuentaComitente` (fuente Notion). Lo que sigue acá es la otra cara: el historial interno de bugs de QA encontrados sobre ese mismo endpoint durante 2025-2026, no la referencia de integración.

Cluster denso de bugs (11 tickets) sobre el mismo endpoint de alta de CVU + cuenta comitente, todos convergiendo en el rediseño de validaciones de [WS-234](https://bindpsp.atlassian.net/browse/WS-234) (estado "Con defecto" — el rediseño en sí quedó con hallazgos abiertos):

- **Regla de diseño acordada**: si se envía un `idCuenta` existente, el endpoint **no debe re-validar** datos ya presentes en esa cuenta (nombre, apellido, cuitCuil, razonSocial, email, password) — debe usar los de la cuenta existente y no crear una cuenta nueva. Los datos del objeto `cuentaComitente{}` no deben validarse localmente; que los rechace API Broker si corresponde.
- **Bugs encontrados violando esa regla** (todos con `idCuenta` enviado, y aun así creando una cuenta nueva en vez de reusar la existente): faltaba `password` ([WS-245](https://bindpsp.atlassian.net/browse/WS-245)), faltaba `email` ([WS-244](https://bindpsp.atlassian.net/browse/WS-244)), `email` distinto al de la cuenta ([WS-243](https://bindpsp.atlassian.net/browse/WS-243)), `cuit` distinto ([WS-242](https://bindpsp.atlassian.net/browse/WS-242)), faltaba `razonSocial` ([WS-241](https://bindpsp.atlassian.net/browse/WS-241)), exigía `CuitCuil` igual si ya se pasaba `idCuenta` ([WS-238](https://bindpsp.atlassian.net/browse/WS-238)), exigía `nombre`/`apellido` igual ([WS-248](https://bindpsp.atlassian.net/browse/WS-248)).
- **`idTercero` forzado como obligatorio** ([WS-251](https://bindpsp.atlassian.net/browse/WS-251)): el campo `thirdPartyId` de PCNT es solo un identificador externo — debía generarse automáticamente a partir del `idCuenta` si no se enviaba, no exigirse.
- **Mapeo interno inconsistente del bloque `bancos`** ([WS-247](https://bindpsp.atlassian.net/browse/WS-247)): enviar `{"tipo":"CUENTA_BANCARIA","identificacion":"{{dni}}"}` terminaba mandándose a PCNT como `{"type":"CVU","identification":"<cvu>"}` — el backend remapea el dato sin que el cliente lo pida ni pueda predecirlo.
- **`estadoCivil` mal resuelto** ([WS-246](https://bindpsp.atlassian.net/browse/WS-246), no corregido): el endpoint ignora el valor enviado en el body y usa el de la cuenta comitente existente sin fallback claro; se definió la regla correcta (priorizar BD, usar el del body solo si BD está vacío, mapear `Soltero→SINGLE`/`Casado→MARRIED`) pero quedó "No aplica" — revisar si se implementó en otro ticket.
- **Validación de `nombreCvu` ausente** ([WS-223](https://bindpsp.atlassian.net/browse/WS-223)): un `nombreCvu` con caracteres inválidos no devolvía error, sino una creación parcial (HTTP 206) silenciosa.
- **Formato de respuesta inconsistente** ([WS-411](https://bindpsp.atlassian.net/browse/WS-411), publicado W 68 2026-03-11): cuando el alta de la cuenta comitente fallaba, la respuesta mezclaba PascalCase (`CvuCreado`, `CuentaComitenteCreado`) con el camelCase del caso exitoso — unificado a camelCase.
- **No validar `cuitCuil` cuando se envía `cuentaId`** ([WS-478](https://bindpsp.atlassian.net/browse/WS-478), publicado en el hotfix dedicado **W 67.2 HF**, 2026-01-30): enviando `cuentaId` el CUIT se toma de la cuenta existente, pero el endpoint igual validaba el atributo `cuitCuil` ausente del body y rechazaba con 400 — primera aparición del principio "con `idCuenta` no re-validar datos ya presentes" que después consolidó WS-234/WS-238 (arriba).
- **Error de negocio pero la comitente se creaba igual** ([WS-445](https://bindpsp.atlassian.net/browse/WS-445), publicado W 69 2026-04-29): el endpoint respondía `MAX_BANKS_ACCOUNT_SUPPORTED` (u otro error) pero la cuenta comitente quedaba creada de todos modos en `CuentasComitentes` — corregido: si hay error, no se crea.
- **Formato de `motivoError` estandarizado** ([WS-731](https://bindpsp.atlassian.net/browse/WS-731), publicado W 69): el `motivoError` de este endpoint no seguía el formato definido ("Error en alta Comitente (...)"/"Error en alta cvu (...)"); se mapeó ante cualquier evento de error de Poincenot. El resto de los mensajes sin formato se canalizó en WS-892 para una solución general.
- **Falta de trazabilidad en la tabla `CuentasComitentes`** ([WS-31](https://bindpsp.atlassian.net/browse/WS-31)): no se registraba fecha/hora de alta de la relación cuenta↔comitente — se agregaron campos de alta/modificación/baja e historificación de la tabla vía script (alcance solo interno, sin afectar a Lirium/PCNT).

### 4.5 Nuevo endpoint: Liquidaciones por Usuario (`Settlement/Info`) — en desarrollo, con defectos abiertos

Historia [WS-730](https://bindpsp.atlassian.net/browse/WS-730) (7 SP, estado "Con defecto", release W 71 sin fecha aún) agrega un endpoint en Investment (`GET .../investment/settlement/info` consumido de API Broker) para que la organización consulte las liquidaciones de un usuario por rango de fechas, paginado — pensado para reportes normativos e información al usuario final sobre suscripciones/rescates.

**Defectos de contrato — 2 de los 5 cerrados en W 72 (2026-08-18), 3 siguen abiertos:**
- **✅ Cerrado (W 72) — no validaba que la cuenta estuviera habilitada para FCI antes de responder** ([WS-1317](https://bindpsp.atlassian.net/browse/WS-1317), 1 SP): el endpoint devolvía 200 con datos aunque la organización enviada en `x-entidad` no tuviera la funcionalidad de remuneración habilitada, o el `IdCuentaComitente` no perteneciera siquiera a esa organización. Fix: validación de organización habilitada (los campos `FechaHoraBaja`/`Habilitada` de `OrganizacionesParametros` solo son editables manualmente por BD hoy — no hay endpoint de gestión) + validación de que la cuenta comitente exista. Validado por Ana (QA) el 2026-08-07/10.
- **✅ Cerrado (W 72) — defecto nuevo, no estaba en la lista original** ([WS-1315](https://bindpsp.atlassian.net/browse/WS-1315), 0.5 SP): con una cuenta comitente que pertenece a una organización **distinta** de la del header `x-entidad`, el endpoint respondía `200 OK` con resultado vacío (`totalRecords: 0`) en vez de señalar el problema — Nicolás Colón pidió originalmente 403, se resolvió con validación equivalente sin exponer si la cuenta existe o no en otra organización. Validado por Ana (QA) el 2026-08-07/10.
- El parámetro `Sort` es case-sensitive (solo acepta `ASC`/`DESC` en mayúsculas) ([WS-1306](https://bindpsp.atlassian.net/browse/WS-1306)) — **sigue abierto**.
- `IdCuentaComitente` no valida que sea numérico (acepta strings alfabéticos) ([WS-1305](https://bindpsp.atlassian.net/browse/WS-1305)) — **sigue abierto**.
- Inconsistencia de formato de fecha (`YYYYMMDD` en este endpoint vs. `YYYY-MM-DD` en el resto de la API de FCI) ([WS-1304](https://bindpsp.atlassian.net/browse/WS-1304)) — **sigue abierto**.
- Nomenclatura de parámetros mezclando PascalCase/camelCase y español/inglés (`IdCuentaComitente`, `From`, `To`, `Sort` vs. `fechaProceso`, `paso`) — se propuso unificar a camelCase en español para este endpoint ([WS-1303](https://bindpsp.atlassian.net/browse/WS-1303)) — **sigue abierto**, salvo que un barrido posterior indique lo contrario.

> Nota: este cluster de bugs de contrato (nomenclatura, formato de fecha, validación de tipos) repite el mismo patrón ya visto en el endpoint de totalizadores CBU/CVU de Coelsa (ver [conciliacion_y_totalizadores.md §3.1](conciliacion_y_totalizadores.md#31), IDEA PRD-56) — parece un punto ciego recurrente de QA de contrato en endpoints nuevos de Wallet, no exclusivo de FCI.

### 4.6 Estado operativo agosto 2026 — MVP2, webhook faltante y duplicados (W 71)

> Fuente: informe semanal de Fintexa "Informe Estado Proyectos Emisión al 14/08/2026" (Nicolás Pomponio) + mail "Consultas sobre webhook de FCI y finalización de procesamiento de paquetes" (Franco Gimenez, Soporte BIND, 2026-08-14) + Jira WS-1284 (release W 71, 2026-07-15).

**Avance del MVP2:** en curso, con entrega en PROD estimada para fines de agosto 2026 (MVP1 se publicó el 10/12/25). Se repitieron problemas productivos por cambio de IP de los servicios de Poincenot (mismo patrón de incidente ya documentado en este archivo) — se lograron salvar sin impacto. Desarrollo en curso: orquestador para alta de nuevos clientes desde Soporte, nueva forma de iniciar los procesos de FCI para todas las organizaciones con remuneración de cuentas, mejoras complementarias de configuración de organizaciones por API, y análisis de alertas ante fallas de los procesos.

**Webhook de FCI nunca recibido en PROD (pregunta abierta, sin resolver al cierre de esta ingesta):** BIND nunca recibió de parte de Poincenot el webhook de FCI en ambiente productivo — pendiente que indiquen qué hay que configurar del lado de BIND o qué coordinar para recibirlo correctamente.

**Finalización de procesamiento desalineada entre organizaciones:** para **La Virginia**, el proceso de FCI siempre queda en estado "Pendiente" salvo que Soporte avise por Telegram a Poincenot para que lo finalicen manualmente. **Coppel** suele finalizar correctamente solo (alrededor de las 17:00/17:30), mientras que La Virginia normalmente termina 1-2 horas después. Se pidió ajustar el proceso para que todas las organizaciones finalicen aproximadamente al mismo horario — el problema va a crecer porque se sigue sumando entidades (próxima: **HIPO**), y sin alineación la brecha de horarios se agranda con cada organización nueva. BIND ofreció coordinar una reunión con Infra si hace falta. Bloqueo/alerta activa reportada en el mismo informe semanal: hay que controlar diariamente el proceso de Coppel y La Virginia en PROD.

**Registros duplicados en `FCICuentasRemuneradas` por condición de carrera** ([WS-1284](https://bindpsp.atlassian.net/browse/WS-1284), estado "EN QA" al momento del release, publicado igual en W 71): dos PODs del microservicio `Shared.Remunera` consumen el mismo mensaje de cola y ambos insertan un registro en `FCICuentasRemuneradas` para el mismo `IdCuenta`, generando duplicados. Objetivo del fix: evitar la duplicación (constraint o lock a nivel de `IdCuenta`).

> Atribución de versión: [WS-730](https://bindpsp.atlassian.net/browse/WS-730) (§4.5), [WS-1306](https://bindpsp.atlassian.net/browse/WS-1306)/[WS-1305](https://bindpsp.atlassian.net/browse/WS-1305)/[WS-1304](https://bindpsp.atlassian.net/browse/WS-1304)/[WS-1303](https://bindpsp.atlassian.net/browse/WS-1303) (defectos de contrato del endpoint de Liquidaciones, §4.5) confirman `releaseDate` **2026-07-15** (W 71) — ya documentados acá vía `/sync_meetings`, sin contenido nuevo.

## 5. Validaciones del dato Cuenta Comitente (referencia de integración)

> Estado: en producción. Fusionado desde `detalle_productos/wallet/otros_manuales.md §4` en la reestructuración PARA en cascada (2026-08-12).

**Alcance:** informativo y apto para desarrollo. **Objetivo:** dar al desarrollador de la organización que integra el endpoint de crear cuentas comitentes una herramienta adicional para enviar los datos según lo requiere el proveedor externo (IVSA/Poincenot). Sólo se hace referencia al objeto `cuentaComitente` del request body. Validaciones testeadas en Producción.

> 📌 En todos los casos de error de esta sección, la API responde HTTP **206** porque la cuenta queda parcialmente completa (sólo falta la cuenta comitente). "No aplica" significa que no habrá problemas para el integrador por ser un valor lógico o fijo.

### Validaciones de datos (resumen por atributo)

| Atributo | Nota | Valores permitidos (ejemplos) | Valores no permitidos (ejemplos) | Código de error |
|---|---|---|---|---|
| `persona.nombre` / `persona.apellido` | Solo string max 80 caracteres, sin caracteres especiales | "Luciana Agostina", "Rudaz" | con símbolos o números | INVALID_NAME / INVALID_LASTNAME |
| `persona.nacionalidad` / `paisResidencia` / `paisIdentificacion` / `lugarNacimiento` | País ISO 2, no valida realmente | "AR", "BR", "ZM" | No aplica | No aplica |
| `persona.tipoIdentificacion` | Documentado solo "DNI"; admite "CUIT" pero luego no acepta el valor del CUIT → no debe usarse | "DNI" | otros | INVALID_IDENTIFICATION_TYPE |
| `persona.identificacion` | Solo admite DNI válido | "41355086" | CUIT, texto | INVALID_IDENTIFICATION |
| `persona.estadoCivil` | Solo valores documentados, no admite null/vacío | SINGLE/WIDOWED/MARRIED/DIVORCED/CONCUBINAGE/OTHER | otro string, null, "" | INVALID_MARIAL_STATE_TYPE / 400 |
| `persona.fechaNacimiento` | Solo mayores de edad, formato datetime válido | "2000-01-12" | menor de edad, formato inválido | PERSON_IS_NOT_LEGAL_AGE / GENERAL_ERROR |
| `persona.genero` | Solo femenino/masculino | "F", "M" | otro | INVALID_GENDER_TYPE |
| `persona.informacionFiscal.actividadComercial` | No admite vacío. Códigos ARCA de 6 caracteres, o código de ocupación (7=Jubilado … 13=Agricultura Familiar) | "7"…"13", "939030" | vacío/null, formato inválido | REQUIRED_FIELD_WITH_NULL_VALUE / INVALID_BUSINESS_ACTVITY |
| `persona.informacionFiscal.inscripcionIngresos.tipo` | Solo EXE/INS/NOINS, no admite null/vacío | "EXE", "INS", "NOINS" | null, "" | 400 |
| `persona.informacionFiscal.condicionIva` | No admite vacío. RI/RNI/EX/RM/CF | "RI", "RNI", "EX", "RM", "CF" | null, otro | 400 / INVALID_IVA_CONDITION_TYPE |
| `persona.informacionFiscal.fatca`/`ocde`/`sujetosObligados` | Booleans + campos anidados, mayormente admiten null/vacío salvo `fatca.ssn` que no admite null | ver detalle en fuente | — | — |
| `direccion.tipo` | LEGAL/HOME/WORK | — | otro, null | INVALID_ADDRESS_TYPE |
| `direccion.calle` / `localidad` | Admite números, puntos y acentos; no admite otros especiales ("-") | "San Martín", "RUTA 12" | "Gral - San martin" | INVALID_STREET_CHARACTERS / INVALID_LOCALITY_CHARACTERS |
| `direccion.numero` | Admite números y letras, no null/vacío, máx 5 caracteres | "12345", "ABC" | "-", 6+ caracteres | INVALID_NUMBER_LENGTH |
| `direccion.piso`/`departamento`/`bloque`/`sector`/`torre` | Letras/números sin especiales, admite null/vacío, máx 5, sin espacios | "1", "piso1", null, "" | "$$$", "P 1" | INVALID_*_LENGTH |
| `direccion.codigoPostal` | Admite CP o CPA | "1407", "C1407PO" | null, "", formato inválido | INVALID_ZIP_CODE |
| `direccion.provincia` | Documentado con código ISO (AR-C…AR-T) pero no valida nada realmente | cualquier valor | — | No aplica |
| `contacto.codigoArea` | Solo números, códigos de área de Argentina sin el 0, no vacío | "11", "221" | "12345", vacío | INVALID_AREA_CODE_PHONE / REQUIRED_FIELD_WITH_NULL_VALUE |
| `contacto.correoElectronico` | Email válido, no null ni vacío | "hola@gmail.com" | formato inválido, vacío | INVALID_EMAIL / REQUIRED_FIELD_WITH_NULL_VALUE |
| `contacto.telefono` | Admite números, letras y especiales, máx 10 caracteres, no vacío | "6855673322" | 11+ caracteres, vacío | INVALID_PHONE_NUMBER / REQUIRED_FIELD_WITH_NULL_VALUE |
| `verificacionIdentidad.Id` | Admite números, letras, especiales, no null ni vacío | "ABC123" | null, "" | 400 / REQUIRED_FIELD_WITH_NULL_VALUE |
| `bancos.tipo` / `identificacion` | Valor fijo "CVU" / número de CVU | "CVU" / "0000184305010032338573" | No aplica | No aplica |

### Validaciones de negocio conocidas

> 📌 En todos estos casos, la API responde HTTP 206 (cuenta parcialmente completa, sólo falta la cuenta comitente).

| Código de error | Descripción |
|---|---|
| HIT_ON_BLACK_LIST_15 / _37 / _41 | Hit contra lista negra número 15 / 37 / 41. |
| MAX_BANKS_ACCOUNT_SUPPORTED | El CUIT tiene más de 30 cuentas en Argentina. |

> Ver también §4.1-4.4 arriba — historial interno de bugs de QA encontrados sobre este mismo endpoint (`CuentaYCVUConCuentaComitente`) durante 2025-2026 (IDEA Jira PRD-103), complementario a esta referencia de integración.
