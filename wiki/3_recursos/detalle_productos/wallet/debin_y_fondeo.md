# DEBIN y fondeo de cuenta recaudadora — Wallet

Configuración y capacitación sobre débito recurrente (DEBIN) aplicado a fondeo de la cuenta recaudadora, habilitación de DEBIN recurrente en organizaciones, y procedimientos de fondeo manual en Bantotal (staging).

---

## 1. Introducción — Fondeo de cuenta recaudadora con DEBIN (capacitación interna)

### ¿Qué es?

Solución de APIs para fondear la cuenta recaudadora de la organización de wallet trayendo fondos desde otra CBU mediante un DEBIN recurrente.

El DEBIN es una transferencia de fondos inmediata. A diferencia de una transferencia tradicional, el vendedor (a quien se acredita) genera el pedido y el comprador (a quien se debita) solo debe "aceptar" o autorizar el débito en su home banking (en una transferencia tradicional el comprador es quien crea el pedido). En este caso se usa **DEBIN RECURRENTE**: la aceptación/autorización del débito se hace una única vez al principio mediante la creación de una suscripción y queda permanente; luego los DEBIN se cursan directamente sin pedir aceptación, porque ya está implícita.

### ¿Por qué es importante?

- Herramienta operativa automática para que la organización pueda aumentar los fondos en la cuenta recaudadora y evitar una cuadratura de saldos negativa.

### ¿Qué está alcanzado en este proyecto?

- Endpoint para que la organización consulte el saldo de la cuenta recaudadora.
- Endpoint para que la organización cree un DEBIN.
- Endpoint para que la organización consulte un DEBIN.

### ¿Qué no está alcanzado?

- Una organización no puede usar esta funcionalidad por defecto; requiere configuraciones y no puede configurarse entera sin soporte de Fintexa.
- No hay webhooks.

### ¿Cómo funciona?

- Para crear un DEBIN, la organización invoca el endpoint de crear DEBIN; se registra e inmediatamente se instruye en API Bank. Se devuelve el id registrado para luego consultar el estado.
- Estos DEBIN no son operaciones (no están asociadas a cuentas de wallet ni generan comprobantes); son directos de la organización y se registran en una tabla de la BD de Wallet Cuenta.
- El sistema hace pasamanos con API Bank para esta transacción, mostrando el mismo estado que indica API Bank. No monitorea automáticamente los DEBIN sin estado definitivo, pero cuando la organización fuerza la consulta, se consulta a Coelsa y se actualiza la información antes de responder.
- Los estados posibles del DEBIN son los que indica API BANK (ver documentación de listado de estados de un DEBIN en el apidoc de sandbox).
- La organización puede complementar el uso de esta herramienta con el endpoint de consulta de saldo de la cuenta recaudadora para entender cuándo conviene crear el DEBIN.

### Consideraciones importantes

- Sólo puede realizarse DEBIN a CBU, no a CVU.

### Requisitos para usarlo

- La cuenta recaudadora de la organización debe estar dada de alta en Coelsa como vendedora DEBIN (endpoint de API Bank).
- Se debe haber creado exitosamente la suscripción de adhesión de recurrencia de DEBIN en Coelsa (manual, endpoint de API Bank).
- Debe existir el registro de esta suscripción del comprador asociado a la organización en la tabla de la BD Cuentas (con `CuentaId = NULL`). Se solicita a Fintexa crearlo manualmente.

### Ejemplo — fondeo exitoso

Consultar saldo de la cuenta recaudadora:

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/SaldoCuentaRecaudadora' \
--header 'Authorization: Bearer {{access_token}}'
```

```json
{
    "saldo": 521973087.34
}
```

Crear un DEBIN para fondeo de cuenta:

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/CrearPedidoDebin' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
    "descripcion": "Fondeo Cuenta Recaudadora",
    "cbuOrigen": "3220001823007351860012",
    "monto": 100
}'
```

```json
{
    "id": 236,
    "descripcion": "Fondeo Cuenta Recaudadora",
    "cbuOrigen": "3220001823007351860012",
    "aliasOrigen": null,
    "monto": 100.0,
    "originId": "D00000910_CTZMD",
    "coelsaId": "8D0Q619LY08LYJ327JZ5RG",
    "bindId": null,
    "concepto": "VAR",
    "provision": "Devolucion QR",
    "contraparteCuit": "20322678275",
    "contraparteAlias": null,
    "contraparteCbu": "3220001823007351860012",
    "contraparteNombre": "OTAMENDI NICOLAS",
    "contraparteBancoId": "322",
    "contraparteBancoDescripcion": null,
    "estado": "PENDING",
    "fechaInicio": null,
    "fechaFin": null
}
```

Consultar el DEBIN por id (en progreso):

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Organizacion/GetDebinPedidoById/236' \
--header 'Authorization: Bearer {{access_token}}'
```

Estado intermedio: `"estado": "AWAITING_CONFIRMATION"`. Estado final tras nueva consulta: `"estado": "COMPLETED"`.

---

## 2. Configurar para fondeo de cuenta recaudadora con DEBIN

**Objetivo:** dejar configurada una organización de wallet para que consuma la funcionalidad de fondear la cuenta recaudadora haciéndole DEBINs recurrentes a otra CBU externa.

### Precondiciones

- Tener la organización creada y funcionando correctamente en API Bank (ver `organizaciones_y_configuracion.md`).
- Si es PSP ≠ 184, es posible que no tenga habilitados en API Bank los endpoints necesarios y deba solicitarse la autorización. Endpoints de API Bank involucrados (sandbox.bind.com.ar/apidoc):
  - `Debin-CrearSuscripcionDEBIN`
  - `Debin-CrearDEBIN`
  - `Debin-ObtenerPedidoDebin`
  - `Debin-Alta_BajaCuentaVendedor`

### Configuraciones

(Mismo procedimiento para PSP = 184 o ≠ 184)

- Dar de alta como vendedora a la cuenta recaudadora asociada a la organización, pegándole al endpoint de API Bank con el `account_id`. Por ahora lo hace Pablo Gomes manualmente porque este endpoint no está en el swagger del wrapper contra el Bind.
- Dar de alta la adhesión a la suscripción de recurrencia DEBIN que adhiere la recurrencia del `cbuOrigen` a la cuenta recaudadora, pegándole al endpoint de API Bank con el `account_id`. Igualmente manual por Pablo Gomes por ahora.
- Solicitar a Fintexa crear el registro que indica la suscripción de DEBIN realizada al CBU en `WalletCuentaDB > DebinSuscripciones`.

  **En STAGING** (se usa un CBU de prueba fijo):

  | Atributo | Valor |
  |---|---|
  | OrganizacionId | {{Id de la organización}} |
  | CbuOrigen | 3220001823007351860012 |
  | AliasOrigen | null |
  | Concepto | VAR |
  | Provision | Devolucion QR |
  | Habilitado | 1 |
  | FechaHoraCreacion | {{timestamp del momento de creación}} |
  | FechaHoraModificacion | {{timestamp del momento de creación}} |
  | FechaHoraBaja | null |
  | DebinSuscripcionId | null |
  | JsonResponse | null |
  | DebinState | null |
  | Auditar | 0 |
  | CuentaId | null |

  **En PRODUCCIÓN:**

  | Atributo | Valor |
  |---|---|
  | OrganizacionId | {{Id de la organización}} |
  | CbuOrigen | {{Cbu externo a debitar}} |
  | AliasOrigen | null |
  | Concepto | VAR |
  | Provision | Ingresar dinero |
  | Habilitado | 1 |
  | FechaHoraCreacion | {{timestamp del momento de creación}} |
  | FechaHoraModificacion | {{timestamp del momento de creación}} |
  | FechaHoraBaja | null |
  | DebinSuscripcionId | null |
  | JsonResponse | null |
  | DebinState | null |
  | Auditar | 0 |
  | CuentaId | null |

### Validaciones

- [ ] En `WalletCuentaDB > DebinSuscripciones`, validar que existe un registro asociado a la organización con `CbuOrigen = {{CBU externo desde donde se quieren traer fondos}}` y `CuentaId = NULL`.
- [ ] Validar que el CBU (de la recaudadora) esté dado de alta en Coelsa como vendedor.

### Documentación de referencia

- Ver también "Introducción de fondeo de recaudadora con DEBIN" (sección 1 de este documento).

---

## 3. Habilitar DEBIN Recurrente en una organización PROD

**Objetivo:** dar de alta la especificación que habilita el uso de DEBIN Recurrente para una billetera (Wallet) específica a través de la API, y cómo verificarlo en la base de datos.

### Paso 1: crear la especificación vía Swagger

1. Ingresar al Swagger del ambiente correspondiente, endpoint `POST /api/v1/Especificaciones` (Alta de especificaciones). PROD: `http://10.22.0.43/swagger/index.html`.
2. Clic en **Try it out**.
3. Configurar Headers: `x-entidad` = ID de la organización (ejemplo: `52`).
4. Body (JSON), reemplazando `"id"` por el ID de la organización correspondiente:

```json
{
  "especificaciones": [
    {
      "scope": "Operaciones",
      "tabla": "Organizaciones",
      "id": 52,
      "clave": "ORGANIZACION_HABILITADA_DEBIN_RECURRENTE",
      "valor": "true"
    }
  ]
}
```

5. Clic en **Execute**.

**Respuesta esperada:** código HTTP `201` (Created).

```json
{
  "ids": [
    1179
  ],
  "mensaje": "Se crearon 1 especificaciones exitosamente"
}
```

### Paso 2: verificación en base de datos (SQL)

Conectarse a `WalletCuentaDB` y ejecutar (reemplazando `'52'` por el ID de la organización):

```sql
SELECT [Id]
      ,[Scope]
      ,[Tabla]
      ,[IdTabla]
      ,[Clave]
      ,[Valor]
      ,[FechaCreacion]
      ,[FechaUltimaModificacion]
  FROM [dbo].[Especificaciones]
  WHERE IdTabla = '52' AND Clave = 'ORGANIZACION_HABILITADA_DEBIN_RECURRENTE'
```

**Checklist de verificación:**
- `IdTabla`: debe coincidir con el ID de la organización configurada en el header.
- `Clave`: `ORGANIZACION_HABILITADA_DEBIN_RECURRENTE`.
- `Valor`: `true`.

Con estos dos pasos la organización queda habilitada para operar con DEBIN Recurrente de forma inmediata.

### 3.0 Historial W 68 (2026-03-11) — configuración y datos de DEBIN

> Fuente: Jira bindpsp.atlassian.net, versión W 68, tickets WS-494, WS-612, WS-141.

- **La cuenta recaudadora del DEBIN se lee de `CuentasProcesadores`** ([WS-494](https://bindpsp.atlassian.net/browse/WS-494)): hasta W 68, al hacer un Debin el dato de la recaudadora se tomaba de `dbo.Organizaciones.CuentaBancoId`, que no se podía setear por el alta de organización — había que insertarlo por script. Desde W 68 se toma de `dbo.CuentasProcesadores.Cuenta` (el mismo registro que se crea con el endpoint de Cuenta Procesador del alta, ver §1 de `organizaciones_y_configuracion.md`); si la organización no tiene CuentaProcesador, el Debin responde error explícito.
- **Entidad bancaria en suscripciones DEBIN** ([WS-612](https://bindpsp.atlassian.net/browse/WS-612), reclamo de Arcos Dorados/McDonald's): el campo `entidad` derivado del CBU de origen podía venir incorrecto (ej. "HSBC" para un CBU de ICBC) o `null` (Santander) — corregida la resolución de entidad a partir del CBU.
- **Limitación de homologación (no es bug propio)** ([WS-141](https://bindpsp.atlassian.net/browse/WS-141)): en el ambiente de homologación, la consulta de un DEBIN a cuenta recaudadora podía quedar en `AWAITING_CONFIRMATION` y pasar a `EXPIRED` en vez de completarse — el banco confirmó que **no lo va a reparar en homologación**. Tenerlo presente al probar fondeo con DEBIN en staging: no es un defecto de Bind PSP.

### 3.0.1 Deltas de W 69 (2026-04-29)

- **Datos de contraparte NULL en `AvisoDebinPendienteCVU`** ([WS-725](https://bindpsp.atlassian.net/browse/WS-725), publicado en estado "Con defecto"): tras un cambio de mensajería de Coelsa, cuando la cuenta del vendedor es un **CBU** (no CVU), el bloque `cuenta_virtual` llega null y se registraba NULL como contraparte — ajustado para tomar los datos del bloque `cuenta` cuando `cuenta_virtual` viene vacío. Ojo: quedó publicado "Con defecto".
- **Filtros del wrapper `DebinLista` no funcionaban** ([WS-756](https://bindpsp.atlassian.net/browse/WS-756)): el modelo del swagger estaba mal (los nodos `tipo` y `estado` van DENTRO de `operacion`) y los filtros de Estado y Tipo no se aplicaban — Coelsa devolvía TODO. Corregido; impacta también al proceso de `/ConciliacionCoelsa` que lo consume.

### 3.1 Especificación adicional — habilitar/deshabilitar específicamente Debin Recurrente Crédito

> Fuente: Jira bindpsp.atlassian.net, versión W 70.1 (publicada 2026-06-03), ticket [WS-1043](https://bindpsp.atlassian.net/browse/WS-1043).

Distinta de la especificación manual de arriba (`ORGANIZACION_HABILITADA_DEBIN_RECURRENTE`), esta es una especificación **booleana adicional y auto-creada**, específica para la operatoria de **Debin recurrente crédito**: nace con valor `true` automáticamente al crear cualquier organización nueva, y el endpoint `POST /walletentidad-operaciones/v1/api/v1.201/DebinRecurrenteCredito` valida contra ella antes de permitir la operación — si el valor es `false`, o si la especificación no existe para la organización, responde `422` indicando que la operatoria está deshabilitada. Pensada para que Bind PSP pueda desactivar puntualmente el Debin recurrente crédito de una organización sin tocar el resto de su configuración. (El ticket no especifica la `clave` exacta usada en `WalletCuentaDB.dbo.Especificaciones` — si hace falta el nombre literal para consultarla en base, confirmar con desarrollo.)

---

## 4. Fondear recaudadora staging en Bantotal

**Objetivo:** fondear la cuenta para que el cliente a integrarse pueda realizar pruebas ("INGRESAR PLATA - SALDO").

**Precondiciones:**
- Disponer de una cuenta con acceso a Bantotal Staging y todos los permisos necesarios. URL: `https://bt-pre.bind.com.ar/uat/servlet/com.dlya.bantotal.hwelcome`.
- Organización wallet creada con cuenta procesador habilitada y vinculada.

### Pasos a seguir

1. **Acceder a Ingreso de Operaciones:** menú lateral → Caja → Caja - Transacciones → Ingreso de Operaciones.
2. **Seleccionar la transacción de depósito:** para ingresar dinero, seleccionar una transacción de crédito, ej. "20 Depósito en Efectivo Cta.Cte $".
3. **Confirmar módulo y transacción:** Módulo 20, Transacción 20. Presionar **Confirmar**.
4. **Ingresar datos del depósito** en pantalla "INGRESE DATOS DEL DEPOSITO":
   - CUENTA: número de cuenta asignado (ej: 20-1-735135-34-5, la cuenta es 735135).
   - SUBCUENTA: 34.
   - PESOS A RECIBIR: monto a fondear (ej: 1,000,000.00).
   - SUCURSAL: 1 (CASA CENTRAL).
   Presionar **Validar**.
5. **Continuar con Lavado de Dinero y confirmación:** se abre la pantalla de Lavado de Dinero. Seleccionar **BANCO INDUSTRIAL** como integrante de la cuenta y **BIND PAGOS** como persona seleccionada. Presionar **Continuar** y luego **Confirmar** en la pantalla de confirmación.

Fondeo finalizado.

> Nota: producto(s) de esta fuente: WALLET, AG COBROS Y PAGOS.

---

## 5. DEBIN Recurrente para cash-in personal en la APP Wallet

> Fuente: Notion histórico, Epic **"Debin Recurrente en APP"** (~45 SP). Distinto del fondeo de cuenta recaudadora (§1-4, a nivel organización): acá es el **usuario final** de la app quien vincula un CBU propio para cargar saldo en su propia cuenta.

- **Mecánica**: el usuario asocia un CBU de su titularidad desde la app; luego puede usarlo para traer dinero y cargar saldo, vía DEBIN recurrente procesado contra API Bank.
- **Disponible en producción pero nunca publicada** en los stores al momento del freeze del Notion — quedó habilitada a nivel backend/organización pero pendiente de decisión comercial/coordinación para salir al público.
- **Limitación conocida**: solo funciona a CBU, no a CVU.
- **Bug real con causa raíz confirmada**: al vincular un CBU para hacer un DEBIN, un cliente (TIN) recibía "error al vincular la cuenta" — quedó como defecto validado en staging/validándose en prod, sin causa raíz documentada en el ticket (solo el síntoma).
- **Detalle técnico**: la integración final a BFF se hizo en dos partes (1: suscripción, 2: terminado), con un spike previo de "firmas para desbloquear desarrollo de APP" — indica que hubo trabajo de definición de contratos/firmas de API compartido entre backend y mobile antes de que el equipo de APP pudiera arrancar su desarrollo en paralelo.

## 6. DEBIN Recurrente CVU-CBU por API — gestión de suscripciones

> Fuente: Notion histórico, Epic **"Debin Recurrente CVU-CBU por API"** (~40 SP). Expone por API el ciclo completo de gestión de una suscripción de DEBIN recurrente (alta, consulta, baja), a diferencia de los flujos anteriores donde la suscripción se gestiona manualmente (§2) o ya viene dada (§5).

### 6.1 Alcance

- **Alta de suscripción** (endpoint), **consulta de suscripciones** (endpoint, con bug real: el GET no permitía filtrar por `idCuenta` — corregido), **baja de suscripciones** (endpoint), y **contracargos** de DEBIN recurrente (quedó en refinamiento, sin cerrar en Notion).

### 6.2 Cluster de bugs de idempotencia (aprendizaje real)

Se detectó un patrón recurrente de bugs alrededor del **ciclo de vida de una suscripción ya dada de baja**, todos con el mismo síntoma raíz — el sistema no valida correctamente el estado `eliminada` antes de operar:

- Permitía **eliminar una suscripción ya eliminada** (debería rechazar).
- Fallaba con error al intentar **suscribir nuevamente con los mismos datos** de una suscripción ya eliminada (debería permitirlo, day útil para que un usuario reactive un vínculo que había dado de baja).
- El **DELETE no permitía eliminar por `idCuenta`+`CBUOrigen`** (una de las formas de identificar el recurso).
- **Alta de suscripción no funcionaba si se ejecutaba con CBU** en cierto flujo (marcado "No aplica" tras análisis — comportamiento esperado, no bug).
- **Bug de negocio real confirmado**: se pudo dar de alta una suscripción usando como CBU origen el **mismo número de cuenta de destino** (auto-referencia) — el alta se aceptó y quedó "pendiente de autorización" en el sistema (estado real de Coelsa: `RECURRENCIA PENDIENTE DE AUTORIZACION`), y recién se rechazaba al intentar *ejecutar* el DEBIN, no en el alta de la suscripción — la validación de auto-referencia debería estar en el alta, no en la ejecución.

**Lección general para diseño de APIs de suscripciones**: cuando un recurso tiene un ciclo de vida con soft-delete (`eliminada`), cada operación (crear, actualizar, eliminar, recrear) debe validar explícitamente el estado actual del recurso — varios bugs de esta Epic son variaciones del mismo error de no chequear ese estado antes de actuar.

---

## 7. Consulta DEBIN COELSA directo — contingencia para Astropay (CONFIRMADO construido, ver Jira PRD-45)

> Fuente: Notion histórico, Epic **"Consulta DEBIN COELSA directo"** (tipo Sanidad, definición original) + Jira `bindpsp.atlassian.net` IDEA **PRD-45** "ASTROPAY: Consulta directa a Coelsa para contingencia" (Finalizada) + Epic **WS-3** (27 tickets, mayoría Finalizada). **Gap cerrado (2026-07-06)**: en Notion todos los tickets habían quedado "Listo para desarrollo" sin evidencia de ejecución; Jira confirma que la iniciativa sí se construyó y se lanzó a producción.

### Problema de negocio

Cuando el banco o Bind PSP tienen problemas, las operaciones que **Coelsa ya está procesando correctamente** no quedan registradas ni informadas del lado de Bind — generando reclamos. **Astropay** (cliente de mayor volumen) tenía altos niveles de reclamos por tardanza en impactar transferencias entrantes durante estas ventanas de degradación.

### Qué se construyó (confirmado en Jira)

- **`GET /MovimientosCoelsa`**: endpoint nuevo que consulta directo a Coelsa (`DebinLista`, vía MS SharedDebin) filtrando por `cvu`/`cvuContraparte`/`cuitContraparte` + rango de fechas, devolviendo los movimientos con los nombres de atributo propios de Bind (mapeo de campos Coelsa→Bind).
- **Conciliación automática de faltantes**: si el endpoint detecta movimientos que existen en Coelsa pero no en la tabla `Operaciones`, los crea automáticamente como operaciones nuevas (con su comprobante y webhook correspondiente) — el endpoint deja de responder atributos en `null`, porque toda operación devuelta ya existe en el sistema.
- **`GET /MovimientosCoelsaID`**: endpoint complementario para consultar una operación puntual por `redId` (= `coelsaId`), acotado por tipo de operación y rango de fechas (pensado para performance).
- **Habilitación por organización a nivel INFRA** (no por especificación de negocio): por decisión de producto, el acceso se resuelve directamente en infraestructura y **solo se habilitó a Astropay** — nunca se publicitó ni generalizó a otras organizaciones.
- **Conteo de pegadas por organización**: monitoreo separado del conteo de pegadas a API Bank (header `x-internalclienteId` = `APLICACION+IdOrganizacion`, ej. `WALLET14`), para poder facturar aparte el uso de este endpoint si se vuelve intensivo — guarda al menos 3 meses de historial.
- **Ampliación a movimientos CASHOUT**: además de `TRANSFERENCIA`, el proceso de conciliación pasó a considerar también el tipo de DEBIN `CASHOUT` de Coelsa.
- **Cluster de bugs de estabilización post-lanzamiento**: duplicación de eventos detectada en una prueba productiva con Astropay (06/12/2025) — mejoras técnicas para evitar reprocesar el mismo movimiento dos veces; además, varios ajustes menores sobre `/ConciliacionCoelsa` (interpretación de fechas por defecto, validación de que el CVU pertenezca a la organización, no responder error cuando la conciliación no encuentra movimientos, corrección de `fechaHoraDesde` mal calculada).
- **Parte 2 (Conciliar en línea las operaciones faltantes) seguía "En curso"** al momento de este relevamiento — hay una segunda fase de esta funcionalidad todavía sin cerrar.

### Decisiones de diseño ya vigentes

- **No se publicita ni se generaliza**: aunque la herramienta podría habilitarse para cualquier organización, la decisión de producto fue **acotar su uso solo a Astropay** para no generalizar una dependencia de contingencia.
- **Restricción técnica de Coelsa**: el endpoint de Coelsa es a nivel PSP, no permite filtrar solo los movimientos de una organización — por lo que el diseño obliga a Astropay a **filtrar siempre indicando un CVU propio** (nunca de una contraparte), para no exponer movimientos de otras organizaciones del mismo PSP.
- Riesgo identificado y aceptado: que la organización "abuse" del endpoint por su confiabilidad, generando sobrecarga en los sistemas de Bind durante una caída ya delicada.

### Problema de negocio

Cuando el banco o Bind PSP tienen problemas, las operaciones que **Coelsa ya está procesando correctamente** no quedan registradas ni informadas del lado de Bind — generando reclamos. **Astropay** (cliente de mayor volumen) tenía altos niveles de reclamos por tardanza en impactar transferencias entrantes durante estas ventanas de degradación.

### Solución definida

Endpoint que **bypassea directo a Coelsa** para consultar movimientos cuando Bind reporta inconvenientes — y que el propio sistema cree las operaciones/comprobantes faltantes al detectarlas. Decisiones de diseño relevantes:

- **No se publicita ni se generaliza**: aunque la herramienta podría habilitarse para cualquier organización, la decisión de producto fue **acotar su uso solo a Astropay** para no generalizar una dependencia de contingencia.
- **Restricción técnica de Coelsa**: el endpoint de Coelsa es a nivel PSP, no permite filtrar solo los movimientos de una organización — por lo que el diseño obliga a Astropay a **filtrar siempre indicando un CVU propio** (nunca de una contraparte), para no exponer movimientos de otras organizaciones del mismo PSP.
- Habilitable/deshabilitable por organización; opcionalmente medible en uso para poder facturarlo aparte si el consumo es intensivo.
- Riesgo identificado y aceptado: que la organización "abuse" del endpoint por su confiabilidad, generando sobrecarga en los sistemas de Bind durante una caída ya delicada.
- **Próximo paso previsto** (no confirmado si ocurrió): evolucionar esta herramienta hacia conciliaciones generales internas, más allá del caso puntual de contingencia para Astropay.

### 7.1 Confirmado — se generalizó más allá de Astropay (2026-07-21)

> Fuente: Mail "Consultas transferencias entrantes por CVU" — evignoles@bind.com.ar (2026-07-21).

El "próximo paso previsto" de §7 sí ocurrió: Bind PSP ofreció a **COTO** (no solo Astropay) dos vías de consulta para resolver reclamos puntuales de transferencias entrantes sin ID Coelsa: la consulta por ID Debin ya conocida, y una nueva **consulta directa por CVU**. Documentación de integración: guía Notion *"Documentación Conciliar transferencias entrantes directo a Coelsa"*. Se consume con las mismas credenciales del producto Wallet, disponible en staging y producción. No queda claro por el mail si es el mismo endpoint `GET /MovimientosCoelsa` de §7 reutilizado para otra organización, o un endpoint nuevo con el mismo propósito — a confirmar en un futuro sync si aparece evidencia técnica (Jira/release).

### 7.2 Ofrecida también a Carrefour, y alcance acotado confirmado (2026-07-20/22)

> Fuente: Mail "Caidas Bind" (minuta enviada por grivera@bind.com.ar, 2026-07-22, reunión del 2026-07-20).

La misma guía de integración de §7.1 se envió también a **Carrefour (BSF)** el 20/07, en el contexto de una reunión por las caídas del servicio de julio (ver `casos_de_uso_clientes.md` — Carrefour). La minuta deja explícito el **alcance real** de esta API de conciliación, hasta ahora no documentado: recupera **transferencias entrantes sin notificación recibida en la billetera**, pero **no permite recuperar pagos de código QR salientes ni transferencias salientes rechazadas de forma instantánea** por fallas del banco o de Coelsa — la contingencia de esos dos casos sigue sin resolver por esta vía.

### 7.3 Bug encontrado al probar — conciliación deshabilitada por organización (2026-08-11)

> Fuente: Mail "Re: Caidas Bind" — rodrigo_golini@carrefour.com (2026-08-11).

Carrefour probó el endpoint de §7.1/§7.2 y recibió un error de negocio, no técnico:

```json
{
  "eventId": "0",
  "errores": [{
    "titulo": "Conciliación COELSA deshabilitada para la organización.",
    "detalle": "La organización '69' tiene deshabilitada la conciliación COELSA."
  }]
}
```

Confirma que la API tiene un **flag de habilitación por organización** (no documentado hasta ahora) y que, para la organización 69 (Carrefour/BSF), está deshabilitado — bloqueando justo la mitigación que Bind le había ofrecido como respuesta a las caídas de julio. Sin resolución en el hilo a la fecha de este barrido. Ver tarea T-051 en `2_areas/tareas.md`.

## 8. Validación de titularidad en Suscripciones de Debin (samename)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA [PRD-185](https://bindpsp.atlassian.net/browse/PRD-185) "Validar misma titularidad de Suscripciones de Debin" → Historia [WS-1296](https://bindpsp.atlassian.net/browse/WS-1296) (1 ticket), Finalizada, fixVersion **W 71** (2026-07-15), Fintexa [DEM-1577](https://fintexa.atlassian.net/browse/DEM-1577).

### Problema de negocio

Vulnerabilidad de fraude real: las suscripciones de Debin (débito recurrente, ver §6) podían crearse entre una Cuenta de Wallet y una CuentaComprador de **distinta titularidad** — alguien podía debitar fondos de la cuenta de un tercero sin control. Se detectó por un reclamo real de cliente (comprador y vendedor de la operación eran CUITs distintos). **Emma Vignoles (COO) pidió explícitamente la corrección.**

### Qué se construyó

- `POST /walletentidad-cuenta/v1/api/v1.201/Organizacion/CrearSuscripcionDebin` valida titularidad **antes de invocar al banco**: consulta los titulares del CBU comprador (`apibank getbycbuorcvu`) y compara el CUIT de la cuenta de Wallet contra **todos** los titulares (match con cualquiera — permite cuentas conjuntas/co-titularidad), CUIT normalizado y solo tipos fiscales CUIT/CUIL.
- **Diseño fail-closed explícito:** si el servicio de consulta de titulares cae o da timeout, la suscripción **no se crea** (nunca "a ciegas"). Tres desenlaces: coincide → continúa; no coincide (tercero) → HTTP 422 "La titularidad de las cuentas no coinciden"; no verificable (error/timeout) → se propaga el error, no crea.
- La validación **se omite** cuando no se envía `cuentaId` (fondeo de cuenta recaudadora, ver §1-4 de este documento).
- **Seguridad:** el CUIT nunca se loguea en claro (PII). Cobertura de tests: 14/14 PASS (13 unitarios + 1 integración), 100% del handler.
- Verificación registrada: drift 95 (SHIP), review crítico APPROVE, auditoría forense post-fix 0 críticos/0 high.

### Deuda técnica registrada (no bloqueante)

- Falta rate-limit + log de advertencia en el endpoint — el rechazo 422 podría usarse para "tantear" CBUs por enumeración (sugerido ticket de seguimiento OWASP API4:2023, sin ticket creado a la fecha de cierre).
- `CancellationToken` no propagado al lookup de titulares (limitación preexistente).
- Test E2E HTTP real opcional pendiente; falta métrica/contador del rechazo 422.

### Conexión con contracargos de Debin recurrente

Ejecutada bajo la misma Epic [WS-810](https://bindpsp.atlassian.net/browse/WS-810) que la iniciativa de contracargos de debin recurrente (IDEA PRD-140, documentada en la sección siguiente) — ambas alimentan el mismo frente de robustecimiento de Debin.

## Contracargos de DEBIN Recurrente

> Estado: en producción. Fusionado desde `detalle_productos/wallet/otros_manuales.md §3-3.1` en la reestructuración PARA en cascada (2026-08-12).

**Alcance:** informativo y apto para desarrollo. **Objetivo:** explicar el funcionamiento de contracargos de DEBIN recurrente para que una organización cliente pueda integrar la lógica necesaria para operar y procesar exitosamente este tipo de operación.

Por norma, un usuario tiene hasta **30 días** para desconocer una operación de DEBIN recurrente desde la cuenta compradora (la cuenta desde donde se debitó el dinero). Llegado el caso, la entidad (banco o billetera) dueña de la cuenta compradora crea la operación de contracargo DEBIN en Coelsa, quien se encarga de debitar el dinero de la cuenta recaudadora de la cuenta vendedora (donde se acreditó el DEBIN) y acreditarlo en la cuenta compradora original. **Coelsa lleva a cabo este movimiento arbitrariamente, sin esperar validación de saldo de la entidad vendedora** — un usuario puede contracargar y se le devolverá el dinero aunque no haya saldo suficiente en su CVU.

Flujo resumido de un contracargo entrante:
1. Otro banco instruye un contracargo de DEBIN recurrente con Coelsa.
2. Coelsa debita el saldo de la recaudadora propia, acredita en la recaudadora externa y crea el contracargo exitoso.
3. El Banco Industrial informa el contracargo a Bind PSP.
4. Bind PSP intenta debitar saldo al usuario, registra la operación de contracargo y avisa a la organización.

Según el saldo disponible del usuario al momento del registro:
- **Saldo suficiente:** se debita el total y la operación pasa a estado **Devuelta**.
- **Saldo = 0:** se registra el débito pendiente de recycle y la operación pasa a **Devuelta pendiente**.
- **Saldo insuficiente pero > 0:** se debita lo disponible, se registra el saldo restante como pendiente de recycle, y la operación pasa a **Devuelta parcial**.

Ante cada actualización de estado se envía un webhook (evento `CONTRACARGO_DEBIN_ENTRANTE`) a la organización, con estado `Devuelta`/`Devuelta parcial`/`Devolución pendiente`, `contracargo.coelsaId` y `contracargo.comprobantes[]` (comprobantes de débito creados para recuperar el importe contracargado).

> **Nota de historia (fixes fundacionales, versión W 69.1 Fix, 2026-05-05):** el envío del webhook en todos los escenarios no funcionó así desde el inicio — [WS-1042](https://bindpsp.atlassian.net/browse/WS-1042) corrigió que cuando el contracargo no lograba debitar nada (saldo cero), el webhook directamente no se enviaba; desde ese fix se envía siempre, con `comprobantes: []`. Y [WS-1041](https://bindpsp.atlassian.net/browse/WS-1041) corrigió que el débito parcial no actualizaba el estado a `Devuelta parcial` (matriz completa: parcial en línea o vía Recycle → `Devuelta parcial`; se mantiene ante nuevos débitos parciales; al completar el total → `Devuelta`). Ambos fixes se validaron inicialmente con flujo simulado en STG; la prueba con el flujo productivo real se completó con éxito (confirmado 2026-07-09).

### Corrección de mapeo y endpoint manual (W 71, 2026-07-15)

> Fuente: Jira bindpsp.atlassian.net, versión W 71 (publicada 2026-07-15), tickets WS-1252, WS-816.

- **`CoelsaId` mapeado mal en `dbo.ContracargoDebines`** ([WS-1252](https://bindpsp.atlassian.net/browse/WS-1252)): el webhook de contracargo trae el ID del contracargo en sí en el campo raíz `id` (formato `"DebinContracargo-<coelsaId>"`) y el ID de la operación original DEBIN dentro de `data.id`/`data.transaction_ids[]`. El sistema estaba guardando el ID de la **operación original** en la columna `CoelsaId` de `dbo.ContracargoDebines`, en vez del ID del contracargo. Fix: tomar el `id` del mensaje, quitarle el prefijo `"DebinContracargo-"`, y guardar eso como `CoelsaId` del contracargo.
- **Endpoint para insertar contracargos manualmente** ([WS-816](https://bindpsp.atlassian.net/browse/WS-816)): nuevo endpoint de Wallet pensado para Administración/Soporte, para los casos donde el contracargo no llegó por el webhook del banco. Recibe un ID Coelsa de contracargo, dispara internamente una consulta a Coelsa (`GET .../debins/{id}/psp/{idPsp}`) para obtener la operación DEBIN original (`operacion.detalle.idOperacionOriginal`), valida que esa operación exista en la base de Bind PSP y que el contracargo no esté ya registrado, y si todo es válido replica el flujo normal de contracargo (mismo comportamiento que si hubiera llegado por webhook: débito de saldo disponible, envío a Recycle del remanente si no alcanza, deshabilitación de cuenta si corresponde, webhooks pertinentes). Responde 422 si el contracargo ya existe o si la operación original no se encuentra en la base.

### Fixes de robustez (W 72, publicada 2026-08-18)

> Fuente: Jira bindpsp.atlassian.net, versión W 72, tickets WS-1420, WS-1057. ⚠️ Ambos tickets están bajo el Epic [WS-810](https://bindpsp.atlassian.net/browse/WS-810), el mismo que alimenta el proyecto vivo de `prd-140_contracargos_debin_recurrente` — a cruzar por el PM si corresponde.

- **Endpoint de conciliación manual de contracargos usaba la consulta incorrecta a Coelsa** ([WS-1420](https://bindpsp.atlassian.net/browse/WS-1420), 3 SP): `POST /api/v1/Operaciones/ConciliarContracargoDebin` (el mismo endpoint manual de Soporte/Administración documentado arriba, WS-816) consultaba Coelsa vía `/debins5` (`GetDebin5`) para resolver el `IdOperacionOriginal`, pero ese endpoint de Coelsa trae un código numérico donde el sistema esperaba el `IdCoelsa` alfanumérico de 22 caracteres real del contrato Debin. Resultado: la búsqueda de la operación original en base fallaba con 422 ("operación original inexistente") aunque la operación sí existiera en Wallet. **Fix:** usar `/debins` (`GetDebinById`) en su lugar, que sí trae el ID alfanumérico correcto. Sin cambio de contrato HTTP del endpoint ni de esquema de base.
- **Contracargo perdido si llegaba antes de que la operación original quedara Aprobada** ([WS-1057](https://bindpsp.atlassian.net/browse/WS-1057), 3 SP): el webhook `debin.refunded` de Coelsa podía llegar mientras la operación original todavía estaba en estado `AConsultar` (no `Aprobada` = "2") — el flujo de contracargo exigía ese estado y el aviso se perdía. **Nueva lógica** en `WebhookRefundedDebinCommandHandler`: si el estado ya es Aprobada, flujo normal. Si está en `AConsultar`, reconsulta a Coelsa vía `GetDebin4` — si responde `ACREDITADO`, actualiza la operación a Aprobada y continúa el flujo de contracargo; si responde `INICIADO`/`EN CURSO`, dispara un retry in-process del consumer con backoff **10s/30s/60s** (config de cola `WebhookRefundedDebin-Quorum`, replicada en los 6 `appsettings` de cada ambiente), liberando antes el cache de dedup para que el reintento no se descarte como duplicado; si Coelsa devuelve un estado final rechazado, la operación pasa a `Auditar` con log explícito, sin crear contracargo; si se agotan los reintentos sin `ACREDITADO`, también pasa a `Auditar` (sin ir a cola de error). Idempotencia (RF-004): se verifica que no exista ya un `ContracargoDebin` para la operación antes de crear uno nuevo.

Sin cambios de contrato, endpoint ni esquema de base en ninguno de los dos. Validado en STG por Nicolás Colón el 2026-08-14 (dos caminos: contracargo por webhook simulado y por endpoint conciliador manual, ambos con débito de saldo confirmado).

### Deshabilitación de cuenta por contracargo DEBIN sin saldo

> [WS-1246](https://bindpsp.atlassian.net/browse/WS-1246), versión W 70.2 (2026-06-10).

Cuando un contracargo de DEBIN recurrente entrante no encuentra saldo suficiente y la cuenta queda deshabilitada, se dispara el evento `DESHABILITAR_CUENTA` (motivo `CONTRACARGO_DEBIN_PENDIENTE`). El identificador de cuenta del payload tenía un bug de nomenclatura — viajaba como `IdCuenta` (PascalCase), inconsistente con la convención camelCase del resto de los webhooks de Wallet. Corregido: el campo ahora es `cuentaId`.

## Ver también

- [conciliacion_y_totalizadores.md](conciliacion_y_totalizadores.md) — endpoint de consulta enfocada en conciliar (otro requerimiento de Astropay, mismo cliente de esta contingencia).
- [historial_confiabilidad_transferencias_y_comprobantes.md](historial_confiabilidad_transferencias_y_comprobantes.md) — mismo patrón de confiabilidad de webhooks, aplicado a transferencias y comprobantes.
