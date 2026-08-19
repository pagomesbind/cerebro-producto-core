# Organizaciones y configuración — Wallet

> Estado: en producción.

Manuales operativos para dar de alta y configurar una organización de Wallet: creación de la organización (PSP=184 y PSP≠184), webhooks, impuestos (SISCRI), subcuentas Bantotal usadas como cuenta recaudadora, y gap normativo abierto de CPA en domicilios de cuenta.

---

## 0. Gap normativo abierto: CPA (Código Postal Argentino) no se completa en la mayoría de las cuentas

> Fuente: Notion histórico, Epic **"Alimentar CPA en cuentas wallet"** (Normativo, quedó en **Discovery — nunca entró a desarrollo**, sin tickets de Backlog). Se documenta como discovery real y gap abierto, no como funcionalidad construida.

- **Mecánica actual**: al crear una cuenta con datos de domicilio, Wallet consulta a la **API Posicionamiento** interna para resolver el CPA. Esa API busca primero en bases internas y, si no lo encuentra, consulta a un proveedor externo — **pero solo a uno por defecto, sin orquestar fallback entre proveedores** (los dos disponibles son OpenStreetMaps y Google Maps).
- **Hallazgo de la investigación**: el consumo de Google Maps **no estaba funcionando** (error de autorización o de facturación) al momento del análisis — y como no hay fallback automático a OpenStreetMaps, las consultas que dependían de Google Maps simplemente fallaban en silencio.
- **Dato adicional no aprovechado**: el endpoint no envía el id de localidad al proveedor de geocoding, solo provincia + CP + calle + número — con el id de localidad se podría reforzar la búsqueda tanto interna como externa.
- **Magnitud real del problema** (medida sobre cuentas creadas desde julio 2025): el **85% de las cuentas de Wallet no tiene domicilio cargado en absoluto**; de las que sí lo tienen, el **72% no logra obtener CPA**. El problema está **fuertemente concentrado en la Provincia de Buenos Aires** (código 2): representa 52% de los domicilios sin CPA vs. solo 43% de todos los domicilios registrados — desproporción que apunta a un problema específico de esa jurisdicción, no a un problema aleatorio de calidad de datos.
- **Estado**: quedó en fase de discovery, con el diagnóstico completo pero sin desarrollo iniciado ni priorizado. Gap normativo real y medible, no solo teórico.

---

## 1. Crear organización de Wallet — PSP = 184 (Bind PSP)

**Objetivo:** dejar operativa una nueva organización de wallet con sus funcionalidades básicas (crear CVU, transferencias y pago QR) siendo PSP 184 (Bind PSP).

**Precondiciones:** ninguna.

### Configuraciones

- [ ] Reservar un código del proxy en el excel de control (SharePoint Fintexa — sheet de códigos de proxy).
- [ ] Crear el registro de la organización en `WalletCuentaDB > Organizacion.dbo` usando el endpoint **Crear una nueva organización** `POST /api/v1/Organizacion` del swagger de WalletCuenta (STG: XXXX / PRD: `http://10.22.0.43/swagger/index.html`) con el body:

```json
{
  "nombre": "string", //nombre de la organizacion
  "codigo": 999, //código del proxy
  "billeteraId": 0, //En STG=20230621 En PROD=184
  "urlRedirectEnrolamiento": null, //siempre null
  "codigoEntidad": "string", //que no se repita con otra orga
  "pspId": 1 //siempre 1 para psp=184
}
```

> ⚠️ El nombre no puede repetir los mismos 4 caracteres que otros nombres de otras organizaciones.

- [ ] Solicitar creación del consumer en Jira Service Management indicando: Ambiente = STG/PRD, Producto = WALLET, Nombre Cliente = Nombre organización, Id Organización = XX, email (STG: mail de integraciones / PRD: mail del cliente).
- [ ] Reservar cuenta recaudadora para asociar a la organización en el excel de control de cuentas (Google Sheets — planilla de cuentas recaudadoras).
  - ⚠️ En staging, si no hay más cuentas libres, hay que crear nuevas desde el backoffice Bantotal UAT (ver sección "Crear subcuentas en Bantotal" más abajo).
  - ⚠️ En producción sí o sí la tiene que indicar Administración porque tiene que estar exenta de impuestos.
- [ ] Solicitar con un MDA al banco para que habilite a la cuenta en ApiBank/Coelsa.
- [ ] Crear el registro de la cuenta recaudadora en `WalletCuentaDB > CuentasProceadores.dbo` usando el endpoint **Crea una cuenta procesador** `POST /api/v1/CuentaProcesador` del swagger de WalletCuenta con el body:

```json
{
  "procesadorId": 1, // siempre 1 = apibank (2 = coelsa)
  "cuenta": "string", // account_id del banco que indica la subcuenta (Ej: XX-X-XXXXXX-XXX-X)
  "bancoId": "322", // siempre 322
  "actual": true, // siempre true. Significa que esta queda activa.
  "cbu": "string" // cbu de la cuenta (en stg no hace falta)
}
```

Y en `X-ENTIDAD` va el ID de Organización.

- [ ] Fondear cuenta recaudadora para empezar a operar.
  - ⚠️ En staging: fondear por Bantotal (ver "Fondear recaudadora staging en Bantotal" en `debin_y_fondeo.md`) o hacerle una transferencia al CBU desde otro lado.
  - ⚠️ En producción: explicarle al cliente que debe fondear la CBU.
  - ⚠️ En todos los casos, la organización luego debe fondear las cuentas que quiere usar con un comprobante de un tipo de comprobante tipo "ajuste de saldo" o "fondeo".
- [ ] Avisar a Worldsys que se creó una nueva organización en el excel de control (Google Sheets). Solo en Producción.
- [ ] Si la organización ya conoce la URL para configurar webhooks, realizar la configuración necesaria (ver sección "Configurar webhooks" más abajo).
- [ ] Si la organización usará la funcionalidad de lectura y pago QR, realizar la configuración necesaria (mecánica QR/Coelsa vive en `wiki/3_recursos/detalle_productos/adquirencia/`).
- [ ] Si la organización creará cuentas a través de nuestro onboarding, realizar la configuración necesaria.
- [ ] Si la organización calculará impuestos wallet, realizar la configuración necesaria (ver sección "Configurar impuestos" más abajo).
- [ ] Registrar en el drive de integraciones el `client_id` y el `client_secret`.
- [ ] Sólo luego de realizar las validaciones, enviar toda la información al cliente.
- [ ] Habilitar pagos QR en Ardid: en el panel de Ardid, ir a `Parametrías > Parametrías de entidad`, buscar la entidad recién creada, editar. En la pestaña **Transferencias > Ámbitos**, activar el switch **4 - Pagos QR** y **Guardar**.

### Validaciones

- [ ] En staging: ejecutar regresión automática.
- [ ] Revisar que el `idOrganización` creado tenga todo bien en `WalletCuentaDB > Organizacion.dbo`.
- [ ] Revisar que tenga asociados registros en `WalletCuentaDB > CuentaProcesadores.dbo`.
- [ ] Si usa lectura y pago QR, revisar que tenga asociados registros en `WalletOperacionesDB > IEPsAceptadores.dbo`.
- [ ] Validar que se creó todo lo necesario para que la operatoria pase por Ardid. Claves a verificar:

| Clave | Valor |
|---|---|
| ARDID_ENTITY_CODE | concatenado: WA{{IdOrganización}} |
| EVENTO_ALTA_CVU_HABILITADO | true |
| ALTA_CUENTAS_ARDID_HABILITADO | true |
| OPERACIONES_ORGANIZACION_HABILITADA_ARDID_TRANSFERENCIAS_ENTRANTES | true |
| OPERACIONES_ORGANIZACION_HABILITADA_ARDID | true |
| ARDID_BANK_TYPE_ID | Id de tabla Banktype de Ardid asociado al EntityCode |
| ARDID_CLIENT_BANK_TYPE | Id de tabla ClientBanktype de Ardid asociado al EntityCode |
| ARDID_CREATION_MODE_ID | Id de tabla CreationMode de Ardid asociado al EntityCode |
| ARDID_PRODUCT_ID | Id de tabla Product de Ardid asociado al EntityCode |
| OPERACIONES_ORGANIZACION_HABILITADA_ARDID_DEBIN_RECURRENTE | true |

> Fuente: Jira bindpsp.atlassian.net, versión W 70.2 (publicada 2026-06-10), ticket [WS-1242](https://bindpsp.atlassian.net/browse/WS-1242). Hasta esa versión, `OPERACIONES_ORGANIZACION_HABILITADA_ARDID` **no se creaba automáticamente** al dar de alta una organización — quedaba faltante y había que cargarla a mano. Corregido: el alta automática ahora incluye esta especificación.
>
> **Misma familia de bug, spec distinta:** [WS-840](https://bindpsp.atlassian.net/browse/WS-840) (W 70.1, publicada 2026-06-03) corrigió el mismo problema pero para `OPERACIONES_ORGANIZACION_HABILITADA_ARDID_DEBIN_RECURRENTE` (la fila siguiente de esta tabla) — tampoco se creaba automáticamente en el alta antes de esa versión.
>
> **Confiabilidad del alta de cuenta+CVU vs. timeouts de Ardid** — Fuente: ticket [WS-1139](https://bindpsp.atlassian.net/browse/WS-1139), publicado también en W 70.2. Se detectó que cuentas y sus CVUs de Wallet no quedaban dadas de alta en Ardid cuando el evento de alta (`AddArdidCuentaCommandHandler`) fallaba por timeout, sin reintento efectivo. Se ajustó el esquema de reintentos (la definición original pedía 3 intentos cada 5 min fijos; lo finalmente aprobado en QA fueron 3 intentos espaciados en 15/30/60 segundos — hay una versión intermedia mencionada en los comentarios del ticket con 5 intentos incrementales que no coincide con lo aprobado, tomar el dato de 3/15-30-60s como el vigente) y se amplió el criterio de qué códigos/excepciones se consideran transitorios. **Deuda técnica reconocida y abierta**: si la caída de Ardid se extiende más allá de la ventana de reintentos, el esquema actual no alcanza — falta un mecanismo de redelivery de mayor alcance temporal.
>
> **Bug histórico corregido — alta automática de organizaciones nunca funcionó en PROD** ([WS-990](https://bindpsp.atlassian.net/browse/WS-990), W 70.1, 2026-06-03): el flujo automático de alta de organizaciones **nunca creó organizaciones correctamente en producción** (sí funcionaba en STG) por una diferencia de `baseUrl` entre ambientes para las APIs de Entity y de Product que no estaba contemplada. Corregido replicando el patrón usado por el resto de las APIs; STG no tuvo cambios.
>
> **Discrepancia de estado de CVU entre Wallet y Apibank** ([WS-900](https://bindpsp.atlassian.net/browse/WS-900), W 70.1, 2026-06-03): si un CVU es propio, Wallet no vuelve a consultar Apibank para saber su estado real — puede quedar `activo=true` en `WalletCuentaQuerys` mientras Apibank ya lo tiene `activo=false` (caso detectado: una baja en Apibank que no se registró correctamente del lado Wallet). Dirección de la mejora: reforzar la robustez de la eliminación de CVU consultando el estado a Apibank después del pedido de baja. Mensaje de error acordado para cuando no se puede determinar el resultado real: *"Error al procesar baja de CVU en Bind. Por favor intente nuevamente más tarde."*

| Clave | Valor |
|---|---|
| ALTA_CUENTA_SISCRI_HABILITADA | true |
| CALCULO_IMPUESTOS_HABILITADO | true |
| ID_TIPO_COMPROBANTE_RECYCLE | 413 |
| ID_TIPO_COMPROBANTE_RECYCLE | 372 |
| ID_TIPO_COMPROBANTE_RECYCLE | 373 |
| ID_TIPO_COMPROBANTE_RECYCLE | 374 |

---

## 2. Crear organización de Wallet — PSP ≠ 184

**Objetivo:** dejar operativa una nueva organización de wallet (crear CVU, transferencias, pago QR) siendo un PSP distinto al 184, es decir que usará su propia licencia de PSP.

> ℹ️ Es altamente probable que el PSP no esté lista para pagos QR como billetera interoperable hasta que homologue con Coelsa.

**Precondiciones:**
- Contar con las credenciales de API BANK propias del PSP.
  - ℹ️ Si el cliente no conoce los datos o no está avanzado como cliente de API Bank, se puede adelantar su integración configurando su organización en STAGING como si usara el PSP 184 (idPSP=1), para adelantar los trabajos de desarrollo.

### Configuraciones

- [ ] Reservar un código del proxy en el excel de control (mismo excel que PSP=184).
- [ ] Crear el registro del PSP en `WalletCuentaDB > PSPs.dbo` solicitando por Jira a FINTEXA, enviando:
  - CUIT: cuit del PSP
  - Nombre: razón social del PSP
  - BCRAId: sale del registro de billeteras digitales interoperables del BCRA
  - CoelsaId: id PSP en Coelsa (varía por ambiente)
- [ ] Enviar a FINTEXA las credenciales de API bank de este PSP por email a `security@fintexa.tech`, indicando asunto "Credenciales Api bank - WALLET - Ambiente XX" y mensaje con Psp Id = X, ambiente XX y credenciales.
- [ ] Crear el registro de la organización en `WalletCuentaDB > Organizacion.dbo` usando `POST /api/v1/Organizacion` con el body:

```json
{
  "nombre": "string",
  "codigo": 999, //código del proxy
  "billeteraId": 9999, //Fijo 9999 a menos que el PSP ya haya homologado QRi. Si no, poner billeteraId correspondiente
  "urlRedirectEnrolamiento": null,
  "codigoEntidad": "string",
  "pspId": X // X = psp recién creado en el primer paso
}
```

> ⚠️ El nombre no puede repetir los mismos 4 caracteres que otros nombres de otras organizaciones.

- [ ] Solicitar creación del consumer en Jira Service Management (mismos datos que PSP=184).
- [ ] Solicitar al cliente el CBU y el `account_id` de la cuenta recaudadora, asegurándose de que esté habilitada en ApiBank/Coelsa.
  - ⚠️ Es probable que esta información haya que solicitarla directo al BIND por MDA.
- [ ] Crear el registro de la cuenta recaudadora en `WalletCuentaDB > CuentasProceadores.dbo` (mismo endpoint y body que PSP=184).
- [ ] Fondear cuenta recaudadora para empezar a operar (mismas consideraciones que PSP=184).
- [ ] Si la organización ya conoce la URL de webhooks / usará QR / usará onboarding / calculará impuestos: realizar las configuraciones correspondientes (ver secciones relacionadas).
- [ ] Registrar en el drive de integraciones el `client_id` y el `client_secret`.
- [ ] Sólo luego de realizar las validaciones, enviar toda la información al cliente.
- [ ] Habilitar pagos QR en Ardid (mismo procedimiento que PSP=184: Parametrías > Parametrías de entidad > Transferencias > Ámbitos > 4 - Pagos QR).
- [ ] ⚠️ **Credenciales del PSP en la config de Wallet.Bind** ([WS-1289](https://bindpsp.atlassian.net/browse/WS-1289), hotfix W 70.3 HF 2026-06-25, caso Cencosud/PSP 406): un PSP nuevo requiere además el alta de su entrada `PSPCoelsaId`/`Owner` en el array `Bind:PSPCredentials` de `appsettings.Production.json` de `Wallet.Bind.Api` — si falta, las consultas (ej. `CuentaCVUByCbuCvuOrAlias`) fallan con 500/código 19004 "PSPCredentialsOptions Owner by psp". Si el pod del cliente levanta con otro environment, replicar la entrada allí. (Deuda preexistente señalada en el ticket: esa config hardcodea EncryptionKey y password de RabbitMQ — candidato a Key Vault.)
  - Contexto del PSP de Cenco: el alta del PSP **CencoPAY** en PROD fue el hotfix **W 68.3 HF** del 2026-04-14 ([WS-911](https://bindpsp.atlassian.net/browse/WS-911) — CUIT 30590360763, BCRA ID 3463, Coelsa ID **470**; ⚠️ el hotfix posterior WS-1289 referencia PSP **406** — discrepancia de IDs sin aclarar en los tickets). El mismo hotfix configuró el flujo onboarding→wallet de dos organizaciones nuevas: **Coop Unión Justiniano Posse** (org 60, código POSSE) y **GST** (org 59) ([WS-913](https://bindpsp.atlassian.net/browse/WS-913)/[WS-912](https://bindpsp.atlassian.net/browse/WS-912)).

### Validaciones

- [ ] En staging: ejecutar regresión automática.
- [ ] Revisar `WalletCuentaDB > Organizacion.dbo` y `CuentaProcesadores.dbo`.
- [ ] Si usa QR, revisar `WalletOperacionesDB > IEPsAceptadores.dbo`.
- [ ] Validar configuración de Ardid (mismas claves que la tabla de PSP=184, sin la fila de DEBIN recurrente listada explícitamente en este instructivo).

---

## 3. Configurar webhooks a organización Wallet

**Objetivo:** configurar las URLs donde el cliente recibirá las notificaciones del producto Wallet Service (WS). Se trabaja sobre **Wallet Cuenta**, tanto en Swagger como en la base de datos.

- **URL Swagger STG:** `http://10.210.1.31/swagger/index.html?urls.primaryName=v1`
- Los endpoints están en el apartado **"Organización"**.

**Precondiciones:**
- Conocer el ID de Organización y las URLs correspondientes a cada evento y ambiente.
- Verificar si ya existen webhooks configurados: `SELECT * FROM NotificacionesParametros WHERE OrganizacionId = @IdOrganizacion` (ej: `WHERE OrganizacionId = 34`).

### Alta (creación) de webhook

Endpoint: `POST /api/v1/NotificacionesParametros`.

| Nombre | Ubicación | Descripción | Ejemplo |
|---|---|---|---|
| `x-entidad` | Header | Identificación del request | ID de organización (ej: `34`) |

Body de ejemplo:

```json
{
  "notificacionTipoId": 1, // Siempre es 1 = Webhook
  "notificacionEventoId": 15, // Se verifica en la tabla NotificacionesEventos de WalletNotificacionesDB
  "destinoPrincipal": "https://pagbrasil.com/bind/return",
  "destinoAuxiliar": "https://pagbrasil.com/bind/return"
}
```

Verificación: la respuesta debe ser 200 y el registro debe aparecer en `NotificacionesParametros` de `WalletCuentaDB` para el `OrganizacionId` correspondiente.

### Modificación de webhook

Endpoint: `PUT /api/v1/NotificacionesParametros/{id}`.
- `id` (path): ID del parámetro en `NotificacionesParametros`.
- `x-entidad` (header): ID de la organización.
- Completar el body igual que en el alta, con los valores modificados.

### Baja (eliminación) de webhook

Endpoint: `DELETE /api/v1/NotificacionesParametros/{id}`.
- `id` (path): ID del registro a eliminar.
- `x-entidad` (header): ID de la organización correspondiente.

### Validaciones (pruebas funcionales)

Una vez verificados los registros en `NotificacionesParametros`, probar desde Postman (colección: `https://github.com/psalto-bind/integraciones-bind-psp/tree/main/collections`):

- Ejecutar una transferencia saliente usando el consumer de la organización.
- Pagar un QR usando el consumer de la organización.
- Simular una transferencia entrante a una CVU de una cuenta de la organización (transferir con un consumer de otra entidad).

Verificar en `WalletNotificacionesDB > Notificaciones` que se hayan disparado los webhooks correspondientes (ej: `WHERE OrganizacionId = 118`), revisando la columna `EstadoId`:

| EstadoId | Nombre |
|---|---|
| 1 | PENDIENTE |
| 2 | ENTREGADA |
| 3 | NO ENTREGADA |
| 4 | CANCELADA |

### Endpoints wrapper en API Bank (ABM de webhooks a nivel PSP)

> Fuente: Jira bindpsp.atlassian.net, versión W 70.1 (publicada 2026-06-03), ticket [WS-722](https://bindpsp.atlassian.net/browse/WS-722), pedido/probado del lado Fintexa.

Más allá del ABM de `NotificacionesParametros` de arriba (nivel organización de Wallet), existe un ABM de webhooks a nivel **PSP** sobre el wrapper de Bind de API Bank: `PUT`/`GET /v1/webhooks`, `DELETE /v1/webhooks/code/:code`, y `POST /v1/webhooks/testSendMessage` (útil para probar que un webhook configurado efectivamente llega). Documentado en `https://sandbox.bind.com.ar/apidoc/#api-Webhooks-AltaModificacionWebhook`.

---

## 4. Configurar impuestos (SISCRI) en organización Wallet

**Objetivo:** dejar andando el cálculo de impuesto en la creación de comprobantes de una organización de Wallet, con sus respectivos webhooks, e ingresar en proceso de recycle a los impuestos cuyo débito online falló.

**Precondiciones:** organización creada en wallet.

### Configuración de especificaciones y webhooks

1. Obtener el ID de la organización a configurar.
2. En Swagger (`http://10.22.0.43/swagger/index.html`), sección **Especificaciones de organización**, completar:
   - Scope: `Recycle`
   - Tabla: `Organizaciones`
   - IdTabla: ID de la organización
   - Clave: `ID_TIPO_COMPROBANTE_RECYCLE`
   - Valor: `{IdTipoComprobanteImpuestos}` — valores posibles: `372`, `373`, `374`, `413`

Ejemplo de request:

```json
{
  "especificaciones": [
    {
      "scope":"Recycle",
      "tabla":"Organizaciones",
      "id":16,
      "clave":"ID_TIPO_COMPROBANTE_RECYCLE",
      "valor":"372"
    }
  ]
}
```

3. Configurar webhooks desde el mismo Swagger (`Nueva Notificación / Agregar Notificación`):

```bash
curl -X 'POST' \
'http://10.22.0.43/api/v1/NotificacionesParametros' \
-H 'accept: application/json' \
-H 'x-entidad: 16' \
-H 'Content-Type: application/json-patch+json' \
-d '{
  "notificacionTipoId": 1,
  "notificacionEventoId": 22,
  "destinoPrincipal": "URL_DEL_WEBHOOK_DEL_CLIENTE",
  "destinoAuxiliar": "URL_DEL_WEBHOOK_DEL_CLIENTE"
}'
```

> ⚠️ Deben configurarse dos eventos de webhook: `notificacionEventoId = 21` y `notificacionEventoId = 22`. El header `x-entidad` debe coincidir con el ID de la organización.

### Registros de especificaciones a crear en `WalletCuentaDB > Especificaciones.dbo`

- Scope `Siscri`, Tabla `Organizaciones`, Clave `ALTA_CUENTA_SISCRI_HABILITADA`, Valor `true` — para que el alta de CVUs cree automáticamente las personas en SISCRI.
- Scope `Impuestos`, Tabla `Organizaciones`, Clave `CALCULO_IMPUESTOS_HABILITADO`, Valor `true` — para que la creación de comprobantes de un tipo con impuestos habilitado se mande a SISCRI.
- Scope `Recycle`, Tabla `Organizaciones`, Clave `ID_TIPO_COMPROBANTE_RECYCLE`, Valor `591` (STG) / XX (PROD) — Ret Imp al débito.
- Scope `Recycle`, Tabla `Organizaciones`, Clave `ID_TIPO_COMPROBANTE_RECYCLE`, Valor `590` (STG) / XX (PROD) — Ret Imp al crédito.
- Scope `Recycle`, Tabla `Organizaciones`, Clave `ID_TIPO_COMPROBANTE_RECYCLE`, Valor `592` (STG) / XX (PROD) — Ret SIRCUPA.
- Scope `Recycle`, Tabla `Organizaciones`, Clave `ID_TIPO_COMPROBANTE_RECYCLE`, Valor `798` (STG) / XX (PROD) — Ret IIBB Tucumán.
- Registro para que la organización reciba webhooks de impuestos: `NotificacionEventoId = 21`.
- Registro para que la organización reciba webhooks de recycle: `NotificacionEventoId = 22`.

### Validaciones

- [ ] Chequear que se haya creado la organización en SISCRI: debe existir en `SharedImpuestosWalletDB > Organizacion.dbo` con `COD_ORGANIZACION = id de la organización`. Depende de configuración en app settings; al crear una organización debe crearse automáticamente en SISCRI.
- [ ] Chequear que al crearse el CVU de una cuenta se cree la persona correspondiente en `SharedImpuestosWalletDB > Persona.dbo`.
- [ ] Chequear que todas las cuentas+CVU existentes tengan persona creada en SISCRI. Si alguna no está, ya no se creará automáticamente (la especificación sólo actúa en el momento de creación); si falta, el cálculo de impuestos fallará. Puede solicitarse crear las personas faltantes manualmente.
- [ ] Chequear que cada cuenta tenga en `WalletCuentaDB` el campo `FechaAltaSiscri` con la fecha correspondiente; si está en NULL, el cálculo de impuestos fallará aunque tenga la persona creada en SISCRI.
- [ ] Chequear que al crearse un comprobante de un tipo que genera impuesto:
  1. Se genera un registro en `ComprobanteDB > ComprobantesImpuestos.dbo` (se enviará a SISCRI para calcular).
  2. Se genera un registro en `SharedImpuestosWalletDB > LOTE_PERS_ING.dbo` (ingresó en un lote de SISCRI).
  3. Se genera un registro en `SharedImpuestosWalletDB > LOTE_PERS_EGR.dbo` (finalizó el lote de SISCRI).
  4. Se genera un registro en `LIQ_IMP_PERSONA`.
  5. Se actualiza el registro en `ComprobanteDB > ComprobantesImpuestos.dbo`.
- [ ] Chequear que todos los tipos de comprobante deseados de calcular impuesto estén habilitados en `WalletComprobanteDB > TiposComprobante.dbo`.

### Hotfixes 67.x (enero-febrero 2026) — alta de wallet e impuestos

> Fuente: Jira bindpsp.atlassian.net, versiones **W 67.1 HF** (2026-01-29) y **W 67.2 HF** (2026-01-30).

- **Alta de wallet vía onboarding con CVU fantasma** ([WS-472](https://bindpsp.atlassian.net/browse/WS-472), W 67.2 HF, SOPORTE/OB-47): una solicitud de onboarding podía confirmarse como "correcta" con la wallet creada pero **sin CVU real** (`cvu = null`, `id = 0` y sin embargo `cvuCreado = true`). Fix: validación de que `cvu`/`id` sean válidos; si el CVU no se creó, la solicitud queda en **estado de error de alta y permite reintento** (mismo tratamiento que un timeout) en vez de continuar como exitosa.
- **Demoras de hasta 1 hora en el cálculo de impuestos** ([WS-486](https://bindpsp.atlassian.net/browse/WS-486), W 67.1 HF, reclamo de Consorcio Abierto, org 48): hotfix dedicado de performance del circuito de cálculo — sin detalle técnico del fix en el ticket.

### Historial W 66 (2025-12-15) — Ardid: segmentación y alta de CVU

> Fuente: Jira bindpsp.atlassian.net, versión W 66, tickets WS-53, WS-44, WS-186, WS-36.

- **Segmentación de clientes en Ardid** ([WS-53](https://bindpsp.atlassian.net/browse/WS-53), 15 SP, Epic "Cuentas para menores: MVP Arcos"): se creó el segmento `externalClientTypeId=1` ("Standard {Entity} menor") con **graduación automática diaria a los 18 años** (el cliente pasa de segmento menor a estándar sin intervención manual) — ver también [cuentas_menores_y_eco_cerrado.md](cuentas_menores_y_eco_cerrado.md).
- **Endpoint de Crear Segmento sin responder el ID creado** ([WS-44](https://bindpsp.atlassian.net/browse/WS-44)): el nuevo endpoint de integración Wallet↔Ardid para crear segmentos no devolvía el `IdSegmento` recién creado en la response — corregido.
- **CVUs no se daban de alta en Ardid** ([WS-186](https://bindpsp.atlassian.net/browse/WS-186)): regresión que impedía el alta de CVUs en Ardid — mismo dominio de acoplamiento no obvio Wallet↔Ardid señalado en WS-147 (W 67, abajo).
- **Reversa de impuestos** ([WS-36](https://bindpsp.atlassian.net/browse/WS-36)): se agregó la capacidad de reversar (dar de baja) impuestos ya calculados/liquidados — antecedente directo de la reversa condicional documentada para Eco Cerrado en [cuentas_menores_y_eco_cerrado.md §3.1](cuentas_menores_y_eco_cerrado.md).

### Historial W 67 (2026-01-27) — robustez del alta y del circuito de impuestos

> Fuente: Jira bindpsp.atlassian.net, versión W 67, tickets WS-147, WS-316, WS-353, WS-357, WS-403.

- **El alta en SISCRI depende de la configuración de Ardid** ([WS-147](https://bindpsp.atlassian.net/browse/WS-147)): cuentas creadas en dos organizaciones no se daban de alta en SISCRI — la causa no era SISCRI sino que **las organizaciones no tenían las especificaciones de Ardid configuradas** (`ARDID_ENTITY_CODE`, `ALTA_CUENTAS_ARDID_HABILITADO`, etc., ver tabla del §1). Acoplamiento no obvio a tener presente cuando "no impacta en SISCRI".
- **CUIL duplicado por concurrencia** ([WS-316](https://bindpsp.atlassian.net/browse/WS-316)): dos solicitudes de alta simultáneas con el mismo CUIL podían crear cuentas duplicadas — se agregó un bloqueo del CUIL por caché ante una solicitud en curso.
- **Devolución de transferencia sin devolver el impuesto** ([WS-353](https://bindpsp.atlassian.net/browse/WS-353)): al devolverse una transferencia con impuestos calculados, se devolvía el principal pero no se generaba el comprobante de devolución del impuesto — corregido.
- **BANZA: onboarding sin alias** ([WS-357](https://bindpsp.atlassian.net/browse/WS-357)): los usuarios creados por onboarding no recibían alias de CVU — el "modo asignar alias" no estaba activo en la configuración de la organización. Chequeo a sumar al alta de organizaciones con onboarding.
- **Vencimiento de credenciales de Ardid** ([WS-403](https://bindpsp.atlassian.net/browse/WS-403)): el `clientSecret` del host Ardid venció y provocó fallas de conexión (Cuenta/Operaciones/StateMonitor) — las credenciales de Ardid en appsettings **tienen vencimiento** y hay que renovarlas proactivamente.

### Historial W 69 (2026-04-29) — impuestos correctos y robustez

> Fuente: Jira bindpsp.atlassian.net, versión W 69, tickets WS-692, WS-726, WS-708, WS-918.

- **⚠️ Breaking change comunicado a clientes: `cuit_destino` obligatorio en transferencias salientes** ([WS-692](https://bindpsp.atlassian.net/browse/WS-692)): SISCRI no cobra impuestos entre cuentas de **misma titularidad**, pero el CUIT destino solo puede venir del request de la organización (Wallet no tiene forma de saberlo) — al ser opcional, las orgs mandaban solo el CBU y SISCRI recibía `cuitDestino = null`, interpretaba distinta titularidad y **cobraba impuestos cuando no correspondía**. Desde W 69: `cuit_destino` requerido (400 si falta/vacío/≠11 caracteres, sin instruir ni SISCRI ni Apibank). No se valida que el CUIT corresponda realmente a la cuenta destino (se confía en el cliente). Gono comunicó la obligatoriedad a los clientes con un mes de aviso. **Se excluyó `/TransferirConCostos` del cambio por impacto en la APP.**
- **Alta de Tipo de Comprobante en SISCRI por evento** ([WS-726](https://bindpsp.atlassian.net/browse/WS-726), 7 SP): igual que el alta de Persona (WS-500, W 68), el alta de tipos de comprobante en SISCRI pasó de HTTP online a evento asíncrono con reintentos — no penaliza el flujo online del alta en Wallet. (En QA se observaron tipos de comprobante de Wallet ausentes en SISCRI — motivo por el que la integridad de este circuito sigue siendo un punto a vigilar.)
- **Cuenta y Domicilio en la misma transacción** ([WS-708](https://bindpsp.atlassian.net/browse/WS-708), SOPORTE EM-362): el alta insertaba Cuentas y CuentasDomicilios por separado — unificado en una transacción atómica.
- **Saldos mal calculados bajo ráfagas** ([WS-918](https://bindpsp.atlassian.net/browse/WS-918), SOPORTE EM-472, reclamo de Consorcio Abierto): tras ráfagas de transferencias salientes, los comprobantes de impuestos dejaban el saldo mal calculado (diferencias visibles entre comprobantes consecutivos). Fix: generación de comprobantes con **concurrencia optimista transaccionada** para impuestos — capítulo intermedio de la saga de concurrencia de impuestos (WS-480 en W 68 → WS-918 en W 69 → WS-1082 en W 70.1).

### Historial W 68 (2026-03-11) — robustez del circuito Wallet→SISCRI

> Fuente: Jira bindpsp.atlassian.net, versión W 68, tickets WS-462, WS-474, WS-500, WS-501.

- **Unicidad de tipos de comprobante en SISCRI** ([WS-462](https://bindpsp.atlassian.net/browse/WS-462)): al dar de alta un Tipo de Comprobante en Wallet, a SISCRI se enviaba el `Código` (texto, ej. "COMPDEB") como clave — como SISCRI no recibe `IdOrganizacion`, dos organizaciones con el mismo código chocaban por duplicado. Desde W 68 se envía el `Id` interno numérico de Wallet (único global) como `CodTipoComprobante`, y el `Nombre` como `Descripcion`.
- **Comprobantes de sistema sin organización** ([WS-474](https://bindpsp.atlassian.net/browse/WS-474)): el endpoint de configuración de impuestos exigía `organization_id`, lo que impedía habilitar el cálculo sobre comprobantes de sistema (sin organización) — caso real MAX PAY (org 42): solo se retenían impuestos en transferencias entrantes y no en salientes, con **riesgo de incumplimiento ante ARCA**. Regla de negocio explícita del fix: **las devoluciones NO calculan impuestos**.
- **Alta de persona en SISCRI por eventos** ([WS-500](https://bindpsp.atlassian.net/browse/WS-500)): el alta de persona pasó de HTTP directo (sin reintentos ante fallo → personas faltantes en SISCRI) a un evento `AltaPersonaSiscriEvent` con consumer y lógica de reintentos, mejorando la integridad de las altas.
- **Persona Jurídica sin razón social** ([WS-501](https://bindpsp.atlassian.net/browse/WS-501)): una cuenta PJ creada sin `razonSocial` fallaba silenciosamente al darse de alta en SISCRI. Desde W 68 el alta de cuenta valida: si el CUIT **empieza con 3**, `razonSocial` es obligatoria (decisión explícita del PM: validar el prefijo "3" genérico y no solo 30/33/34, para cubrir prefijos futuros que ARCA pueda agregar).

### Asignar/limpiar `FechaAltaSiscri` por cuenta — endpoint de Soporte

> Fuente: Jira bindpsp.atlassian.net, versión W 70.1 (publicada 2026-06-03), tickets [WS-880](https://bindpsp.atlassian.net/browse/WS-880) y [WS-1202](https://bindpsp.atlassian.net/browse/WS-1202).

Antes de esta versión, cuando una cuenta nacía sin `FechaAltaSiscri` (ver validación arriba), Soporte tenía que abrir un ticket a Fintexa para que lo cargaran manualmente. Ahora `PATCH /api/vi/ActualizarDatosCuenta/{id}` en API WalletCuenta acepta el campo `fechaAltaSiscri` (camelCase) y lo asigna directamente al registro de la cuenta — si ya tenía un valor, lo pisa con el nuevo. El endpoint **también admite pasar el campo como `null`**, para el caso inverso (evitar que se calculen impuestos en SISCRI para una cuenta que no lo requiere) — confirmado funcionando en QA.

---

## 5. Crear subcuentas en Bantotal para integraciones

**Objetivo:** asignar un producto (Cuenta Corriente Pesos para Personas Jurídicas) a una cuenta y desbloquearla para su uso, generando así una subcuenta disponible como cuenta recaudadora.

**Precondiciones:** disponer de una cuenta con acceso a Bantotal Staging y todos los permisos necesarios. URL: `https://bt-pre.bind.com.ar/uat/servlet/com.dlya.bantotal.hwelcome`.

### I. Asignación del producto (cuenta corriente)

1. **Navegar a Mantenimiento de Cuentas:** menú lateral → Cuentas → Mantenimiento de Cuentas → Apertura / Cierre / Detalle.
2. **Buscar la cuenta:** en "Paquetes/Productos por Cliente", campo **Desde Cuenta**, ingresar el número de cuenta asignado (ej: 735135). Presionar **Filtrar**.
3. **Acceder a Productos:** seleccionar la cuenta en el listado (ej: 735135 BIND PAGOS). Clic en **Productos**.
4. **Agregar producto (Cuenta Corriente):** en "Producto a Agregar" ingresar:
   - Módulo: 20 (Cuenta Corriente)
   - T. Operación: 5 (CUENTAS PERSONAS JURÍDICAS)
   - Moneda: 80 (Pesos)
   - Papel: 1
   Clic en **Agregar**, confirmar con **Sí**.
5. **Confirmar SubCuenta:** aparece ventana con datos de la SubCuenta: SubCuenta 1, Nombre PESOS. Marcar **Cobrar Comisión de Apertura** si es necesario. Presionar **Confirmar** y **Sí**.

### II. Desbloqueo de la cuenta

Al darse de alta, la cuenta queda en estado "Bloqueado" (BLOQ) y debe desbloquearse a "Normal" (NORMA).

1. **Navegar a Ingreso de Operaciones (Transacciones):** menú lateral → Transacciones → Ingreso de TRNs.
2. **Ingresar la transacción de desbloqueo:** Módulo 20, Transacción 700, Fecha Valor Contable actual. Presionar **Confirmar**.
3. **Seleccionar la cuenta a desbloquear:** en "Selección de Operaciones" ingresar Cuenta (ej: 735135) y Moneda 80 (Pesos). Presionar **Filtrar**, seleccionar la línea de la cuenta corriente y **Seleccionar**.
4. **Confirmar el desbloqueo:** de vuelta en "Ingreso de Operaciones", presionar **Confirmar**.
5. **Verificar el estado (opcional):** volver a Cuentas → Mantenimiento de cuentas → Apertura/Cierre/Detalle, buscar la cuenta, clic en **Productos**, y verificar que el campo **Estado** diga **NORMA**.

---

## 6. ABM interno de Especificaciones y Aceptadores QR, y mensajes de error en alta de cuenta (IDEA Jira PRD-88)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA [PRD-88](https://bindpsp.atlassian.net/browse/PRD-88) "Mejoras para integraciones y soporte" → Epics [WS-171](https://bindpsp.atlassian.net/browse/WS-171) "ABM de organizaciones" (17 tickets, 7 retenidos) y [WS-210](https://bindpsp.atlassian.net/browse/WS-210) "Poder dar soporte en altas cuenta" (7 tickets, 5 retenidos, todos fetched). Motivación de negocio de la IDEA madre: reducir el ~50% de capacity de desarrollo que se gastaba en tareas de soporte manual (objetivo: 30% para abril 2026) dándole al equipo de integraciones herramientas de autoservicio desde el Admin/backoffice en vez de depender de scripts ad-hoc.

### 6.1 ABM genérico de Especificaciones (por lote)

Antes de esta IDEA, crear un registro nuevo en `WalletCuentaDb > Especificaciones` (el mecanismo de configuración usado en toda esta wiki — ver ejemplos en §1-2 de este archivo y en `wallet/cuenta_remunerada_fci.md §2`) requería un script manual. Ahora existe un endpoint genérico interno (no consumible directamente por organizaciones) para:
- Crear una o varias Especificaciones de una sola vez indicando `Scope`/`Tabla`/`IdTabla`/`Clave`/`Valor` — útil para dejar configurada de punta a punta una funcionalidad completa (ej. todas las especificaciones de Impuestos/Recycle de una organización en una sola llamada).
- Valida que no exista ya una Especificación con el mismo `Scope`+`Tabla`+`IdTabla`+`Clave` antes de insertar.
- Consultar y eliminar Especificaciones (estos dos últimos quedaron en estado "No aplica" — no confirmado si se implementaron por otra vía).

**Bugs encontrados**: si en un lote de creación alguna Especificación ya existía, el endpoint debía rechazar todo el lote sin insertar nada — en la práctica insertaba parcialmente las que no existían y solo fallaba en la que colisionaba (corregido — el fix transaccional todo-o-nada con rollback es [WS-506](https://bindpsp.atlassian.net/browse/WS-506), **publicado en producción en W 68, 2026-03-11**; decisión de diseño acordada PM↔Fintexa para que quien usa el endpoint solo deba ocuparse de las especificaciones con error). El endpoint de actualizar una Especificación quedó expuesto en APIM (accesible externamente si un cliente obtuviera la URL) y no exige indicar el Id de la Especificación a modificar — bug no corregido al momento de esta ingesta.

### 6.2 ABM de Aceptadores QR

Los "Aceptadores" son las entidades que pueden leer los QR generados por Bind PSP. Se agregaron endpoints de alta/baja/modificación/consulta de Aceptadores, con la regla de que **un Aceptador nuevo nace habilitado por defecto para todas las organizaciones** (y una baja lo deshabilita para todas) — evita tener que habilitar manualmente aceptador por aceptador en cada organización nueva. *(Atribución de release vía `/sync_releases`: la regla "todas las orgs leen todos los QR por defecto" salió en W 67/WS-216, 2026-01-27; los endpoints ABM de aceptadores en W 68/WS-274, 2026-03-11.)*

### 6.3 Mensaje de error explícito (`motivoError`) en alta de cuenta Wallet

Los endpoints de alta de cuenta Wallet (cuenta+CVU, cuenta+CVU+cuenta comitente, cuenta+CVU+Lirium) antes devolvían solo `null` en los sub-objetos que no llegaron a crearse (`cuentaCvu`, `cuentaComitente`) sin explicar la causa — dejando a Onboarding/soporte sin poder diagnosticar sin acceso a logs internos. Se agregó el campo `motivoError` en la respuesta con el detalle real del proveedor externo que falló, por ejemplo:

```json
{ "motivoError": "Error en APIBANK: GE500 - Error general" }
{ "motivoError": "Error en APIBROKER: INVALID_NAME - Nombre de la persona invalido general" }
```

**Bugs encontrados en la propia estandarización**: el formato de `motivoError` en el endpoint de alta de cuenta comitente no coincidía con el usado en alta de cuenta Wallet (corregido, debían unificarse); el mensaje aparecía en inglés en vez de español para fallas de alta CVU+Lirium; y se detectó un caso de alta "exitosa" (HTTP 2xx) con `cvu=null`, `id=0` pero `cvuCreado=true` — bug de validación (no solo de mensaje): debía tratarse como error reintentable, igual que un timeout, no como éxito. *(Atribución de release: `motivoError` salió en W 67/WS-211+WS-212, 2026-01-27 — naming "Error en alta cvu (...)"/"Error en alta Comitente (...)" definido por el PM; el fix del CVU fantasma en el hotfix W 67.2 HF/WS-472.)*

> Ver también [wallet/cuenta_remunerada_fci.md §4.4](cuenta_remunerada_fci.md) — mismo endpoint de alta de cuenta comitente, cluster de bugs de validación de datos (distinto ángulo: formato de campos vs. mensaje de error).

---

## 7. Historial de altas de organización y migraciones — tramo W71

> Fuente: Jira bindpsp.atlassian.net, tickets WS-1432+WS-1431 (W 71.3 FIX), WS-1470 (W 71.7 FIX), WS-1429 (W 71.4 FIX), WS-1444 (W 71.6 FIX). Continúa el patrón de §1-2 con casos reales.

- **HAPSA (org 62, [WS-1432](https://bindpsp.atlassian.net/browse/WS-1432), W 71.3 FIX):** configuración de app setting `x-entidad` para que el onboarding exitoso de HAPSA cree CVU directamente en la organización 62.
- **App Android de demo en PROD (org 64, [WS-1431](https://bindpsp.atlassian.net/browse/WS-1431), W 71.3 FIX):** se crea una app "DEMO" en producción para que Bind PSP haga demos/pruebas productivas — apunta a una organización creada solo para ese fin, nunca se publica en las app stores. Alcance funcional: todo excepto viaje QR e ingresar dinero con TIN en puestos físicos; sí incluye lo más nuevo (DEBIN recurrente, ingresar dinero con tarjetas).
- **Organización 66 — PAFX ([WS-1470](https://bindpsp.atlassian.net/browse/WS-1470), W 71.7 FIX):** alta de app setting del WalletBFF en PRODUCCIÓN para la organización PAFX (`AltaUsuarioWallet: false`, `UsuarioMail: false`, versiones `APIPAFX`/`APKPAFX`/`IPAPAFX`) — nueva organización habilitada en prod, sin más contexto de negocio en el ticket.
- **Pasaje a PROD de AuthExternal V2, por etapas ([WS-1429](https://bindpsp.atlassian.net/browse/WS-1429) relevamiento/soporte técnico W 71.4 FIX; [WS-1444](https://bindpsp.atlassian.net/browse/WS-1444) etapa 2/3 W 71.6 FIX):** migración de autenticación externa en curso, por microservicios. La etapa cubierta en esta ingesta migra **Wallet.BIND** y **SharedDebin**. Sin detalle de qué etapas ya pasaron ni cuántas faltan — gap de visibilidad del roadmap completo de esta migración.
