# Ardid/Akurtech — Catálogo de APIs Externas

> Estado: en producción.

> Fuente: `ARDID_Documentacion_ApisExternas_V1.18.1.pdf` — "DOCUMENTO DE INTEGRACIÓN DE AKURTECH" (170 páginas). Extracción y estructuración vía agente de investigación (2026-07-02). Ver [index.md](index.md) para contexto general.
> **Nota de fidelidad**: el texto fuente proviene de extracción automática de un PDF con muchas tablas; hay ruido de formato (comillas tipográficas, columnas mezcladas, numeración repetida). Cuando el contenido es ambiguo o parece cortado por la extracción, se marca explícitamente como **[fragmento poco claro en la fuente]**. No se completó ni infirió ningún dato ausente — ver también los gaps consolidados en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md).
>
> **Nota importante de alcance**: este catálogo documenta las APIs **internas del proveedor Ardid/Akurtech** (Pentass) — el conjunto de endpoints que Bind PSP (u otra entidad integradora) consume para comunicarse con la plataforma de monitoreo transaccional. Esto es distinto de la **API pública de Bind PSP** documentada en `<producto>/apis_expuestas/` de cada producto — Ardid no tiene API pública propia en ese portal; su integración es directa proveedor↔entidad.

## 1. Historial de Revisiones

La tabla de historial de revisiones del documento aparece **vacía** en la fuente. El pie de página de todas las páginas indica de forma constante: **"Última revisión: 0"**.

## 2-4. Objetivo, Objeto y Alcance (según el documento)

- **Objetivo**: "Instruir al desarrollador de la Entidad que quiere integrarse a la solución de Bind Pagos."
- **Objeto**: "Este documento aplica sólo para la solución de Monitoreo transaccional."
- **Alcance**: "El alcance del presente documento es sólo informativo."

## 5. Base URL

⚠️ **Gap de completitud del documento fuente**: la tabla de Base URL por ambiente (STAGING/PRODUCCIÓN) está **vacía** — dice literalmente "A definir" para los 23 grupos de API, sin excepción. Las únicas rutas relativas explícitas (sin host) que aparecen en todo el documento son:
- `15.e. UploadBlackList`: `POST /api/blacklist/UploadBlackList`
- `15.f. CheckBlacklist`: `POST /api/blacklist/CheckBlacklist`
- `15.g. CreateGroupOfCommerce`: `POST api/Commerce/CreateGroupOfCommerce`
- `15.h. DeleteGroupOfCommerce`: `POST api/Commerce/DeleteGroupOfCommerce`
- `15.i. AssignCommerceToGroup`: `POST api/Commerce/AssignCommerceToGroup`
- `15.j. DeleteCommerceOfCommerceGroup`: `POST api/Commerce/DeleteCommerceOfCommerceGroup`
- `17.d. Process` (FileProcessController): `POST /api/FilProcess/Process`

## 6. Mecanismo de Autenticación

Sección **22. API /Authentication**, con dos endpoints: `AuthenticUser` (login, genera token + refresh token vía `guid`+`secret`, no usuario/password tradicional) y `RenewAccessTokenFromRefreshToken`. El token dura **1 día**; el refresh token dura **7 días**.

El JWT decodificado del ejemplo tiene `"aud": "Ardid"` como audiencia — **confirma que el nombre técnico interno del sistema/token sigue siendo "Ardid" pese al rebranding comercial a "Akurtech"** en el título del documento (ver [index.md](index.md#nota-ardid--akurtech)).

⚠️ El documento no declara explícitamente en una sección de "convenciones generales" si el resto de los endpoints requieren header `Authorization: Bearer <token>` — se infiere de la existencia del módulo `/Authentication`, pero no está garantizado documentalmente.

## 7. Convenciones Generales Observadas

- **Formato de respuesta estándar** (mayoría de los módulos 6–21): objeto JSON con `message` (o `messageEs`/`messageEn` en los módulos más nuevos), `code` (entero, semántica de negocio, no HTTP), y `data` (payload o `null`).
- **Formato de respuesta alternativo** (motores de reglas — `/Transfer/Analize`, `/Transaction`, `/ClientType/Login`): estructura con `Code`, `HttpCode`, `Status` (`APPROVED`/`NOT_APPROVED`/`BLOCKED`/`REALIZED`/`REJECTED`/`ERROR`/`PENDING`), `Reason` (string tipo enum), `Message`.
- **Health check**: patrón repetido `/health/db` (Entity, Product, Transfer, Transaction) — valida conexión a SQL. 200: `"Conexión a DB exitosa."`; 500: `"No se puede conectar a la base de datos."`
- **Bilingüismo progresivo**: módulos más nuevos (Commerce/Blacklist avanzado, CreateFullClient, Authentication, FileProcessController) devuelven `messageEs`/`messageEn`; módulos más antiguos solo `message` en español.
- **`CoinType`/`Coin`**: 1 = Pesos, 2 = Dólares, 3 = Euros.
- **`BankType`**: ⚠️ inconsistencia entre módulos — "1 – empresa 2-individuo" en `/ClientBankType`, vs "1 Cliente 2 Empresa" en `/ClientType`.
- **`TransferPermission`** (ClientProduct): 1 = Opera, 2 = NoOpera, 3 = NoOperaSaliente, 4 = NoOperaEntrante.

## 8. Índice general de APIs documentadas

| # | Módulo / Grupo | Endpoints incluidos |
|---|---|---|
| 6 | `/Entity` | Create, CreateFirstAdUser (AD), CreateFirstAdUser (local), health/db |
| 7 | `/Product` | CreateProduct, GetProducts, GetProductById, DeleteProduct, UpdateProduct, health/db |
| 8 | `/ProductType` | CreateProductType, GetProductTypeById, GetProductTypeList, UpdateProductType, DeleteProductType |
| 9 | `/ProductCategory` | CreateProductCategory, GetProductCategory, GetProductCategories, UpdateProductCategories, DeleteProductCategory |
| 10 | `/ClientBankType` | CreateClientBankType, GetClientBankList, GetClientBankById, UpdateClientBank, DeleteClientBankById |
| 11 | `/ClientCreationMode` | CreateClientCreationMode, GetClientCreationModeList, GetClientCreationModeById, UpdateClientCreationMode, DeleteClientCreationMode |
| 12 | `/ClientType` | CreateClientType, GetClientTypeList, GetClientTypebyID, UpdateClientType, Login, UpdateEmail, UpdateDevice, ChangeUsualSchedule, UpdateTypeClient, SetClientRiskProfile, ChangeSegmentationClient, ChangeDatePassword |
| 13 | `/ClientProduct` | CreateClientProduct, GetClientProductList, GetClientProductbyID, UpdateClientProduct, DeleteClientProduct |
| 14 | `/Transfer` | Analize, NotRealized, UpdateExternalTransfer, ChargeCSV, health/db |
| 15 | `/Blacklist` (+ Commerce) | BlacklistIp, BlacklistDevice, BlacklistIdentification, BlacklistCBU, UploadBlackList, CheckBlacklist, CreateGroupOfCommerce, DeleteGroupOfCommerce, AssignCommerceToGroup, DeleteCommerceOfCommerceGroup |
| 16 | `/Loans` | GetLoanById, CreateLoan, DeleteLoans, UpdateLoans, GetAllLoans, GetLoanBySearch |
| 17 | `/Transaction` (+ FileProcessController) | Transaction, NotRealized, Returns, Process, health/db |
| 18 | `/PersonType` | CreatePersonType, UpdatePersonType, DeletePersonType, GetPersonTypeById, GetAllPersonTypeByEntity, GetBankTypeRels, GetPersonTypeTripleRel, CreateSegmentation, AssingPersonTypeToRel, UnassingAllRel (no usar), UnassignPersonTypeToRel, UnassignPersonTypeToTripleRel, GetSegmentationEntity, AssignPersonTypeToTripleRel |
| 19 | `/BankTypes` | CreateBankType, UpdateBankType, DeleteBankType, GetBankTypeById, GetAllBankTypeByEntity, GetBankTypeRels, GetBankTypeTripleRel, CreateSegmentation, AssingBankTypeToRel, UnassingAllRel (no usar), UnassignBankTypeToRel, UnassignBankTypeToTripleRel, GetSegmentationEntity, AssignBankTypeToTripleRel |
| 20 | `/ClientCard` | CreateCard |
| 21 | `/CreateFullClient` | CreateFullClient |
| 22 | `/Authentication` | AuthenticUser, RenewAccessTokenFromRefreshToken |
| 23 | `/FileProcessController` | UploadChargebackTransactionsFile |

## 9. Detalle de cada API

### 6. API `/Entity`

#### 6.a. `/Create` (POST)
**Objetivo**: "La creación de nuevas entidades bancarias."

**Request**: `Code` (string, SI) — Identificador de la Entidad; `Description` (string, SI).

**Response**:
```json
200 - Entidad creada:
{ "message": "Entidad Bancaria Agregada", "code": 1, "data": null }
409 - Bad request:
{ "message": "La entidad Bancaria ya existe", "code": 2, "data": null }
409 - Parámetros incorrectos:
{ "message": "Complete los campos correctamente", "code": 2, "data": null }
```

#### 6.b. `/CreateFirstAdUser` (POST) — variante autenticación AD
**Objetivo**: "La creación del primer usuario utilizando autenticación por AD."

**Request**: `UserId` (string, SI, por defecto 1), `Username` (string, SI), `Domain` (string, SI), `Name` (string, SI), `LastName` (string, SI), `Description` (string, SI), `Email` (string, SI), `ProfileId` (int, SI, por defecto 1), `Enabled` (bool, SI, por defecto `true`), `Sid` (string, SI), `Banks` (string, SI, por defecto 0).

**Response**: éxito (código 1); ya existe usuario (código 2); faltan campos obligatorios (email, nombre, descripción, apellido); email/username ya existentes; caso particular — **"No se encontraron las claves para encriptar/desencriptar en base"**.

#### 6.c. `/CreateFirstAdUser` — variante autenticación local
> El título de esta subsección repite literalmente "CreateFirstAdUser" pero el objetivo textual aclara que es para autenticación local — posible error de copy/paste en el documento original.

**Objetivo**: "La creación del primer usuario utilizando autenticación local."

**Request**: `Name`, `LastName`, `Username`, `Email`, `Password`, `RepeatPassword` (todos string, SI), `ProfileId` (int, SI, por defecto 1), `Description` (string, SI), `Banks` (string, SI, por defecto 0).

**Response** (además de los casos del punto anterior): username requerido, contraseña requerida, repetición requerida, formato de email inválido, contraseñas no coinciden, validación de fortaleza: **"La contraseña debe tener al menos 6 caracteres, incluir mayúsculas, minúsculas y caracteres especiales."**

#### 6.d. `/health/db` (POST)
Sin campos de request. 200: `"Conexión a DB exitosa."`; 500: `"No se puede conectar a la base de datos."`

---

### 7. API `/Product`

#### 7.a. `/CreateProduct` (POST)
**Objetivo**: "Poder crear un producto."

**Request**: `entityCode` (String, SI), `productType` (String, SI), `productCategory` (String, SI), `Name` (String, SI), `Description` (String, SI), `Number` (String, SI), `Coin` (Int, SI — 1 Pesos, 2 Dólares, 3 Euros).

**Response**:
```json
200: { "message": "Producto Creado Correctamente", "code": 1, "data": { "idProduct": 3 } }
```
409: entidad bancaria no asociada (code 2); producto ya existe (code 3); no existe tipo/categoría asociada o fue eliminada (code 4); campos vacíos (code 5); Coin fuera de rango 1-3 (code 6).

#### 7.b. `/GetProducts` (GET)
**Request**: `entityCode` (String, SI). **Response** 200: lista de productos con `id`, `entitycode`, `productTypeId`, `productCategoryId`, `name`, `description`, `number`, `coin`, `dateCreate`, `dateUpdate`, `entity`, `productCategory`, `productType`, `clientProducts` (array). 409: no se encontraron productos.

#### 7.c. `/GetProductById` (GET)
**Request**: `idProduct` (int, SI). **Response** 200: objeto producto. 409: id incorrecto/producto no encontrado.

#### 7.d. `/DeleteProduct` (POST)
**Request**: `idProduct` (int, SI). **Response**: 200 éxito; 409 inexistente; 409 id negativo; 409 producto asociado a un `ClientProduct` (no se puede borrar).

#### 7.e. `/UpdateProduct` (POST)
**Request**: `Id` (Int, SI), `entityCode` (String, SI), `ProductType` (String, SI), `ProductCategory` (String, SI), `Name` (String, SI), `description` (String, SI), `Number` (String, SI), `Coin` (int, SI).

**Response**: 200 éxito; 409 producto inexistente; 409 campos vacíos; 409 Coin fuera de rango; 409 tipo/categoría/entidad bancaria no existe.

#### 7.f. `/health/db` (POST) — duplicado del health check.

---

### 8. API `/ProductType`

#### 8.a. `/CreateProductType` (POST)
**Request**: `Entitycode`, `Name`, `Description` (String, SI). **Response**: 200 con `data.productTypeId`; 409 ya existe; 409 EntityCode no encontrado; 409 campos vacíos.

#### 8.b. `/GetProductTypeById` (GET)
**Request**: `productTypeId` (Int, SI). **Response** 200: objeto con `id`, `entityId`, `name`, `description`, `dateCreate`, `dateUpdate`, `entity`, `auditRestrictions[]`, `products[]`, `restrictions[]`. 409 id incorrecto/no encontrado.

#### 8.c. `/GetProductTypeList` (GET)
**Request**: `entitycode` (String, SI). **Response** 200: array `id`, `entityCode`, `name`, `description`, fechas. 409 sin registros.

#### 8.d. `/UpdateProductType` (POST)
**Request**: `entitycode`, `IdProductType`, `Name`, `Description`. **Response**: 200 éxito; 409 inexistente; 409 entidad no existe; 409 campos vacíos.

#### 8.e. `/DeleteProductType` (POST)
**Request**: `IdProductType` (int, SI). **Response**: 200 éxito; 409 en uso (asociado a producto); 409 inexistente; 409 id negativo.

---

### 9. API `/ProductCategory`

#### 9.a. `/CreateProductCategory` (POST)
**Request**: `entitycode`, `Name`, `Description`. **Response**: 200 con `data.ProductCategoryId`; 409 existente; 409 campos vacíos; 409 código de entidad inválido/no existe.

#### 9.b. `/GetProductCategory` (GET)
**Request**: `ProductCategoryId` (int, SI). **Response** 200: `{ name, description }`. 409 id negativa/no encontrada.

#### 9.c. `/GetProductCategories` (GET)
**Request**: `EntityCode` (Int, SI). **Response** 200: array `{ProductCategoryId, name, description}`. 409 sin registros.

#### 9.d. `/UpdateProductCategories` (POST)
**Request**: `Id`, `entitycode`, `Name`, `Description`. **Response**: 200 éxito; 409 no encontrada; 409 campos vacíos; 409 entidad no existe.

#### 9.e. `/DeleteProductCategory` (POST)
**Request**: `ProductCategoryId` (int, SI). **Response**: 200 éxito; 409 no encontrada; 409 id negativa; 409 asociada a un producto.

---

### 10. API `/ClientBankType`

#### 10.a. `/CreateClientBankType` (POST)
**Request**: `entityCode` (String, SI), `ClientTypeId` (Int, SI), `BankType` (Int, SI — 1 empresa, 2 individuo), `Name` (String, SI), `Description` (String, SI), `PersonTypeId` (Int, SI).

**Response**: 200 con `data.ClientBankTypeId`; 409 ya existe; 409 PersonType no existe; 409 entidad no existe; 409 campos vacíos; 409 BankType fuera de {1,2} o ClientTypeId negativo.

#### 10.b. `/GetClientBankList` (GET)
**Request**: `EntityCode` (String, SI). **Response** 200: array `{id, bankType, clientTypeId, name, description, entityCode}`. 409 lista no encontrada.

#### 10.c. `/GetClientBankById` (GET)
**Request**: `ClientBankTypeId` (Int, SI). **Response** 200: `{Entitycode, name, description}`. 409 id menor a 0; 409 no encontrada.

#### 10.d. `/UpdateClientBank` (POST)
**Request**: `entityCode`, `Id`, `BankType`, `ClientTypeId`, `Name`, `Description`, `PersonTypeId`. **Response**: 200 éxito; 409 no encontrado; 409 PersonType no existe; 409 entidad no existe; 409 campos vacíos; 409 BankType/ClientTypeId inválidos.

#### 10.e. `/DeleteClientBankById` (POST)
**Request**: `ClientBankTypeId` (Int, SI). **Response**: 200 éxito; 409 no encontrado; 409 id menor a 0.

---

### 11. API `/ClientCreationMode`

#### 11.a. `/CreateClientCreationMode` (POST)
**Request**: `entityCode`, `Name`, `Description`. **Response**: 200 con `data.ClientCreationModeId`; 409 ya existe; 409 entidad no existe; 409 campos vacíos.

#### 11.b. `/GetClientCreationModeList` (GET)
**Request**: `entityCode` (String, SI). **Response** 200: array `id, entityId, name, description, fechas`. 409 sin registros.

#### 11.c. `/GetClientCreationModeById` (GET)
**Request**: `ClientCreationModeId` (Int, SI). **Response** 200: `{id, name, desciprion}` (sic typo en la fuente). 409 id menor a 0; 409 sin registros.

#### 11.d. `/UpdateClientCreationMode` (POST)
**Request**: `ClientCreationModeId`, `EntityCode`, `Name`, `Description`. **Response**: 200 éxito; 409 campos vacíos; 409 entidad no existe; 409 id menor a 0; 409 no encontrado.

#### 11.e. `/DeleteClientCreationMode` (POST)
**Request**: `ClientCreationModeId` (Int, SI). **Response**: 200 éxito; 409 no existe; 409 id menor a 0.

---

### 12. API `/ClientType`

#### 12.a. `/CreateClientType` (POST)
**Objetivo**: "Crear un nuevo registro de un tipo de cliente general."

**Request**:
| Campo | Tipo | Req | Descripción |
|---|---|---|---|
| entitycode | String | SI | Código de la entidad |
| CuilCuit | String | SI | Cuil/Cuit del cliente |
| DescripctionCuilCuit | String | SI | Descripción del Cuil/Cuit |
| ClientBankTypeId | String | SI | Tipo de cliente del banco |
| BankType | Int | SI | 1 Cliente, 2 Empresa |
| AmountMonthly | decimal | NO | Monto de haber mensual |
| TransactionalProfile | decimal | NO | Transacción del perfil |
| DateCreateAccount | datetime | SI | Fecha de creación de cuenta |
| Email | string | NO | Email del cliente |
| Mac | string | NO | Atributo de identificación de dispositivo |
| IP | string | NO | Ip del cliente |
| CreationModeId | Int | SI | Id de CreationMode |
| Status | int | NO | Estados a definir (ej: 0 bloqueado, 1 habilitado) |

**Response**: 200 con `data.ClientypeID`; 409 entidad inexistente (code 2), campos vacíos (code 3), AmountMonthly/TransactionalProfile negativo (code 3), ClientBankType no existe (code 7), CreationMode no existe/no pertenece a la entidad/eliminado (code 8), email inválido (code 9), ClientGeneralType ya existe (code 10).

#### 12.b. `/GetClientTypeList` (GET)
**Request**: `entityCode`, `cuit`. **Response** 200: array con `id`, `entityCode`, `clientGeneralDataId`, `clientBankTypeId`, `bankType`, `amountMonthly`, fechas, `email`, `mac`, `ip`, `creactionModeId` (sic), `status`. 409 parámetros incorrectos.

#### 12.c. `/GetClientTypebyID` (GET)
**Request**: `ClientypeID` (string, SI), `Cuit` (String, SI). **Response** 200: objeto con los mismos campos que GetClientTypeList (singular). 409 id menor a 0; 409 no encontrado.

#### 12.d. `/UpdateClientType` (POST)
**Request**: `entitycode`, `CuilCuit`, `BankType`, `AmountMonthly` (NO), `TransactionalProfile` (NO), `Email` (NO), `Mac` (NO), `IP` (NO), `Status` (NO), `ClientBankType` (SI).

**Response**: 200 éxito; 409 campos vacíos (code 2); 409 TransactionalProfile/AmountMonthly negativo (code 4); 409 email inválido (code 6); 409 entidad no existe (code 7); 409 no encontrado (code 8); 409 CuilCuit no existe (code 9); 409 ClientBankType asociado no encontrado (code 8).

#### 12.e. `/Login` (POST)
**Objetivo**: "Recibir los intentos de logueo de un usuario." Es el endpoint central del módulo [modulo_login.md](modulo_login.md).

**Request**: `EntityCode` (String, SI), `ItsLoginFailed` (Bool, SI), `Identification` (String, SI), `IPAddress` (String, SI), `Device` (String, SI).

**Response**: formato `{ message, code, reason, status }` (a veces `points`/`restrictionName`). Casos: errores de entrada (`INVALID_ENTITY`, `ENTITY_NOT_FOUND`, `INVALID_IDENTIFICATION`, `CLIENT_NOT_FOUND`, `GEOLOCALIZATION_ERROR`); motor **ReputationalRules** (rechazo por puntaje, bloqueo de cuenta/login, login sin reglas, pedido de 2FA); motor **StandardRules** (`LOGIN_BLOCK_ACCOUNT`, `LOGIN_REJECTED`, `LOGIN_WITHOUT_RESTRICTION`, `LOGIN_REALIZED_REQUEST_2FA`, `LOGIN_REALIZED_ALERT`); motor **StandardRulesWithScoring** (variantes con `points`); caso especial `status: "FAILED_LOGIN_OK"` (code 8, `reason: FAILED_LOGIN_PROCESSED`) — el registro del intento fallido se guardó bien, no implica que el login haya sido exitoso.

#### 12.f. `/UpdateEmail` (POST)
**Request**: `EntityCode`, `Identification`, `NewMail`. **Response**: 200 éxito; 409 varios casos (información sumaria inexistente, entidad/cliente/ClientGeneralType no existe, formato de email inválido).

#### 12.g. `/UpdateDevice` (POST)
**Request**: `EntityCode`, `Identification`, `NewDevice`. **Response**: análogo a UpdateEmail.

#### 12.h. `/ChangeUsualSchedule` (POST)
**Objetivo**: "Establecer el horario habitual de conexión." Alimenta la Regla IA "Día y Horario habitual" (ver [modulo_transferencias.md](modulo_transferencias.md#52-reglas-ia-entrantes-y-salientes)).

**Request**: `newRangersHoursDto` (List, SI — parámetros Day/From/To), `identification` (String, SI), `entityCode` (String, SI).

**Response**: 200 éxito; 409 campos vacíos; 409 entityCode no existe; 409 ClientGeneralType no encontrado; 409 día inválido — **solo se permiten abreviaciones: "l", "m", "x", "j", "v", "s", "d"**.

#### 12.i. `/UpdateTypeClient` (POST)
**Nota explícita del documento**: "no usar para actualizar el ClientBankType, consultar o usar ChangeSegmentationClient."

**Request**: `idRestriction` (int, SI), `idClientBankTypeId` (int, SI). **Response**: 200 éxito; 409 `idClientBankTypeId` no existe; 409 `idRestriction` no existe en tabla Restriction.

#### 12.j. `/SetClientRiskProfile` (POST)
**Request**: `Cuil` (String, SI), `DateUpdate` (DateTime, SI), `Pep` (Bool, NO), `So` (Bool, NO), `Terrorista` (Bool, NO). **Response**: 200 éxito; 409 Cuil debe tener 11 dígitos; 409 Cuil no existe.

#### 12.k. `/ChangeSegmentationClient` (POST)
**Nota**: "Esta se cambia siempre trabajando dentro de la misma entidad bancaria."

**Request**: `Cuil` (String, SI), `DateUpdate` (DateTime, SI), `Pep`/`So`/`Terrorista` (String, NO — ⚠️ tipados como String aquí, a diferencia de `SetClientRiskProfile` donde son Bool). **Response**: 200 éxito; 409 EntityCode vacío; 409 entidad no encontrada; 409 clientBankType no encontrado; 409 ClientGeneralType no encontrado.

#### 12.l. `/ChangeDatePassword` (POST)
**Request**: `Identification`, `EntityCode`, `LastPasswordChangeDate`. **Response**: 200 éxito; 409 campos vacíos; 409 fecha inválida/mayor a la actual; 409 entidad inexistente; 409 cliente no encontrado.

---

### 13. API `/ClientProduct`

#### 13.a. `/CreateClientProduct` (POST)
**Request**: `entitycode`, `CuilCuit`, `productid`, `cbucvunumberproduct`, `TransferPermission` (NO). **Response**: 200 con `data.ClientProductId`; 409 ya existe; 409 ClientGeneralType/CuitCuil/Product no existe; 409 campos vacíos; 409 TransferPermission negativo (válidos: Opera=1, NoOpera=2, NoOperaSaliente=3, NoOperaEntrante=4).

#### 13.b. `/GetClientProductList` (GET)
**Request**: `entityCode`, `cuit`. **Response** 200: array `id`, `clientGeneralTypeId`, `productId`, `cbuCvuNumerProduct`, fechas, `clientGeneralType`, `product`.

#### 13.c. `/GetClientProductbyID` (GET)
**Request**: `ClientProductId` (string, SI), `cuit`. **Response** 200: objeto único. 409 id menor a 0; 409 no encontrado.

#### 13.d. `/UpdateClientProduct` (POST)
**Request**: `entitycode`, `CuilCuit`, `productid`, `cbucvunumberproduct` (nuevo), `oldCbuCvuNumberProduct` (actual), `TransferPermission` (NO). **Response**: 200 éxito; 409 campos vacíos/menores a 0; 409 no encontrado; 409 ClientGeneralType/Product no existe.

#### 13.e. `/DeleteClientProduct` (POST)
**Request**: `ClientProductID` (Int, SI). **Response**: 200 éxito; 409 no encontrado; 409 id menor a 0.

---

### 14. API `/Transfer`

#### 14.a. `/Analize` (POST)
**Objetivo**: "El análisis de las transferencias." Es el endpoint central del módulo [modulo_transferencias.md](modulo_transferencias.md).

**Request**:
| Campo | Tipo | Req | Descripción |
|---|---|---|---|
| entitycode | String | SI | Código de la entidad |
| DeviceId | String | SI | Id del dispositivo |
| IpOrigen | String | SI | Ip Origen |
| TransferTransactionId | String | SI | Id de transacción de transferencia |
| TransferType | Int | SI | Tipo de transferencia |
| Scope | Int | SI | Scope |
| TrnDateCreate / TrnDateUpdate | Datetime | SI | Fecha creación/actualización |
| CuitCuilOrigin | String | SI | CuitCuil del origen |
| CoinType | Int | SI | Tipo de moneda |
| Amount | Decimal | SI | Monto |
| CuitCuilReceiver | String | SI | Cuit/Cuil del receptor |
| CbuCvuReiver | String | SI | Cbu/Cvu del receptor (sic) |
| AccountTypeReceiver | Int | SI | Tipo de cuenta del receptor |
| Proccesor | int | SI | Procesador |
| TxProccesorId | String | SI | Id de Procesador |

**Response**: formato `{ Code, HttpCode, Status, Reason, Message }`. Casos de aprobación (`APPROVED`): sin restricciones/reglas ML/reputacionales, con excepción, pedido de 2FA. Alerta con aprobación: dispositivo en blacklist genera alerta. Casos de bloqueo (`BLOCKED`, 409): `BLOCK_TRANSFER_`, `BLOCK_USER_`, blacklist de dispositivo/alias/CBU/CVU/IP/email/CUIT bloquea usuario o transferencia, `ReputatonalRules`+nombre de acción. Errores: cliente no existe (`CLIIENT_NOT_EXISTS_FOR_TRANSFER`, code 6), geolocalización por IP mal formada (code 8), ML bloqueado (code 2), `TRANSFER_ID_ALREADY_EXIST` (code 7, duplicado).

#### 14.b. `/NotRealized` (POST)
**Request**: `EntityCode`, `TransferTransactionId`. **Response**: 200 informada; 409 entidad/transferencia no encontrada, transferencia tipo 2, ya informada, ya rechazada. *(Nota: mensajes de esta sección en inglés, a diferencia del resto del documento.)*

#### 14.c. `/UpdateExternalTransfer` (POST)
**Request**: `BankEntityId`, `TransferTransactionId`, `TransferType`, `CuitCuil` (NO), `CbuCvu` (NO). **Response**: 200 "Transfer updated successfully"; 409 sin CBU/CVU ni CUIT/CUIL; 409 transferencia no encontrada; 409 CBU/CVU mal formado (22 caracteres numéricos); 409 CUIT/CUIL mal formado (8-11 caracteres numéricos).

#### 14.d. `/ChargeCSV` (POST) — carga masiva
**Request** (multipart): `File` (binario, SI), `EntityCode` (String, SI), `Mode` (String, SI — dejar 'asj'), `isOfuscate` (Bool, SI — dejar `false`), `sizeBatch` (Int, SI — dejar 1000).

**Response**: 200 "Carga terminada" con estimado de registros y tiempo. 409: sin archivo/vacío; entityCode nulo; modo mal ingresado; entidad no encontrada; fecha de procesamiento faltante; archivo >50MB; extensión ≠ .csv; sin encabezado/ilegible; delimitador inválido (`;` o `,`); encabezados requeridos faltantes.

#### 14.e. `/health/db` (POST)

---

### 15. API `/Blacklist` (incluye submódulo Commerce)

Ver también [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md) para el uso funcional de estos endpoints.

#### 15.a. `/BlacklistIp` (POST)
**Request**: `ListBlacklist` (Array&lt;String&gt;, SI), `Action` (String, SI — Agregar/Eliminar), `MotivoId` (Int, SI — 13 = IP sospechosa, 14 = IP válida), `EntityId` (Int, SI). **Response**: 200 completado; 409 lista vacía/acción inválida/error de procesamiento/motivo inválido/IPs inválidas.

#### 15.b. `/BlacklistDevice` (POST)
**Request**: análogo, `MotiveId` — 21 = Dispositivo válido, 22 = Dispositivo sospechoso.

#### 15.c. `/BlacklistIdentification` (POST)
**Request**: análogo, `MotiveId` — 10 = Identificación inválida, 11 = sospechosa, 12 = válida.

#### 15.d. `/BlacklistCBU` (POST)
**Request**: análogo, `MotiveId` — 19 = Cuenta sospechosa, 20 = Cuenta válida.

#### 15.e. `/UploadBlackList` (POST) — `POST /api/blacklist/UploadBlackList`
**Request** (query): `typeBlackList` (int, SI), `code` (string, NO — si se omite, inserta en todas las entidades). **Request** (multipart): `blacklistCsv` (file, SI).

**Response**: 200 "Archivo procesado con éxito."; 400 CSV faltante/extensión inválida/`typeBlackList` faltante; 500 error de procesamiento.

#### 15.f. `/CheckBlacklist` (POST) — `POST /api/blacklist/CheckBlacklist`
**Request** (todos opcionales, se verifica solo lo enviado): `Card`, `CBU_CVU_Alias`, `Commerce`, `Device`, `Domain`, `Geolocalization`, `Identification`, `Ip`, `Email` (string, NO).

**Response** 200: `{ message, Code: 1, Data: { Card, CBU, Commerce, Device, Domain, Geolocalization, Identification, Ip, Email: bool } }`. 409 error al verificar (Code 2).

#### 15.g. `/CreateGroupOfCommerce` (POST) — `POST api/Commerce/CreateGroupOfCommerce`
**Request**: `EntityCode` (String, SI), `GroupName` (String, SI), `GroupCode` (String, SI — debe ser solo numérico). **Response**: 200 bilingüe; 409 validación (dto nulo, campos vacíos); 409 entidad no encontrada; 409 grupo ya existe; 400 error interno.

#### 15.h. `/DeleteGroupOfCommerce` (POST) — `POST api/Commerce/DeleteGroupOfCommerce`
**Objetivo**: elimina lógicamente (`IsDeleted=true`) un Grupo de Comercio, elimina enlaces en CommercesGroups y marca transacciones relacionadas como eliminadas.

**Request**: `groupCode` (string, SI), `EntityCode` (String, SI). **Response**: 200 éxito; 409 GroupCode/EntityCode vacío; 409 grupo no encontrado; 400 error interno.

#### 15.i. `/AssignCommerceToGroup` (POST) — `POST api/Commerce/AssignCommerceToGroup`
**Objetivo**: asigna una lista de comercios a un Grupo existente, evitando duplicados.

**Request**: `GroupCode` (String, SI), `ComerceIdentificationList` (Array&lt;Int&gt;, SI), `EntityCode` (String, SI). **Response**: 200 agregados; 409 grupo no encontrado; 409 todos ya existen/inválidos (retorna `errorList`/`repeatsList`); 409 código de grupo vacío; 409 entidad no encontrada; 409 grupo eliminado lógicamente; 400 error interno.

#### 15.j. `/DeleteCommerceOfCommerceGroup` (POST) — `POST api/Commerce/DeleteCommerceOfCommerceGroup`
⚠️ El documento fuente **no completó la descripción de este endpoint** (dice literalmente "descripcion" como placeholder). Por el nombre y campos, elimina comercios de un grupo.

**Request**: `GroupCode`, `ComerceIdentificationList`, `EntityCode`. **Response**: 200 removidos; 409 grupo/entidad no encontrada; 409 grupo sin comercios; 409 todos inválidos; 400 error interno.

---

### 16. API `/Loans`

#### 16.a. `/GetLoanById` (POST)
**Request**: `id` (Long, SI). **Response** 200: `{id, bankEntityId, clientTypeId, createDate, Importe, Cbu}`. 409 id negativo/no encontrado.

#### 16.b. `/CreateLoan` (POST)
**Request**: `BankEntityID`, `CBU`, `Importe`, `CreateDate`, `ClientTypeId`. **Response**: 200 "Se agrego el nuevo prestamo a la bd"; 409 parámetros incorrectos; 409 error de CBU; 409 entidad no existe.

#### 16.c. `/DeleteLoans` (POST)
**Request**: `idLoan` (Long, SI). **Response**: 200 eliminado; 409 id no existe.

#### 16.d. `/UpdateLoans` (POST)
**Request**: `idLoan` + mismos campos que CreateLoan. **Response**: 200 actualizado; 409 parámetros incorrectos; 409 error de CBU; 409 id no existe.

#### 16.e. `/GetAllLoans` (POST)
Lista todos los préstamos (sin parámetros documentados). **Response** 200: lista con `Id`, `BankEntity`, `ClientTypeId`, `FechaCreacion`, `Importe`, `CBU`. 409 "No hay registros a mostrar".

#### 16.f. `/GetLoanBySearch` (POST)
**Request**: `search` (string, SI — busca por id/bankentityid/Cbu), `pageIndex` (NO), `pageSize` (NO). **Response** 200: mismo formato que GetAllLoans. 409 search debe ser numérico; 409 sin resultados.

---

### 17. API `/Transaction` (+ submódulos NotRealized, Returns, Process)

#### 17.a. `/Transaction` (POST)
**Objetivo**: "Procesar las transacciones, registrando los resultados del análisis y devolviendo respuestas para cada caso. Si la transacción es aprobada, se guarda en la base de datos." Es el endpoint central del módulo [modulo_pagos.md](modulo_pagos.md).

**Request**:
| Campo | Tipo | Req | Descripción |
|---|---|---|---|
| TransactionId | string | SI | Id de la transacción |
| CommerceId | int | SI | Id del comercio |
| TxIdCommerce | string | NO | Id de la transacción del comercio |
| TimeTxStart | DateTime | SI | Tiempo de inicio |
| PayCode | String | NO | Código de pago |
| Bin | String | NO | Número de identificación bancaria |
| PanLast4 | String | NO | Últimos 4 dígitos |
| PlasticName | String | NO | Nombre de la tarjeta |
| DNI | String | SI | Documento nacional de identidad |
| ExpirationMonth / ExpirationYear | String | NO | Vencimiento |
| Email | String | NO | Correo electrónico |
| Amount | Decimal | SI | Monto |
| TransactionStatusId | Int | SI | Id del estado de la transferencia |
| TxIp | String | NO | Dirección IP |
| Quota | Int | NO | Cuota |
| EnteId | Int | NO | Id de la entidad |
| EntityCode | Int | SI | Código de entidad bancaria |
| PayChannelCode | Int | SI | Código del canal de pago |
| PayTypeCode | Int | NO | Código del tipo de pago |
| CountRentry | Int | SI | Cantidad de intentos |
| CoinTypeId | Int | SI | Id de la moneda |
| TxDevice | String | NO | Dispositivo de la transacción |
| HASH | String | NO | Hash de la tarjeta de pago |
| CardTypeCode | Int | NO | Código del tipo de tarjeta |
| CommerceCuit | String | NO | Número de CUIT del comercio |

**Response**: `{ Code, HttpCode, Status, Reason, Message, StatusTransactionId, [Points] }`. Es el endpoint con más casuística del sistema, organizado por motor: sin reglas (`TRANSACTION_WITHOUT_*`), pedido de 2FA/alerta, **ReputationalRules/BehaviorRules/MachineLearning/ClientStandardRule/CardStandardRule** (aprobado con puntaje, pedido de 2FA), pago pendiente (`Code=12`, `Status=PENDING`, `StatusTransactionId=5` — "tarjeta pendiente de habilitación"), excepción (`TRANSACTION_WITH_EXECEPTION`), errores de validación (409, `INVALID_AMOUNT`/`INVALID_BIN`/`INVALID_IDENTIFICATION`/`ENTITY_NOT_FOUND`/`PAY_CHANNEL_NOT_FOUND`/`PAY_TYPE_NOT_FOUND`/`CARD_TYPE_NOT_FOUND`), transacción repetida (`TRANSACTION_REPEATED`), datos incompletos (`INCOMPLETE_DATA`), rechazos (`CLIENT_BLOCKED`, tarjeta vencida/bloqueada/en blacklist/inválida, `SAME_OWNERSHIP` — "no es posible realizar pagos a comercios registrados bajo la misma titularidad del usuario").

#### 17.b. `/NotRealized` (POST)
**Request**: `TransactionId`, `EntityCode`, `Hash` (NO), `CountRetry`, `Motive`. **Response**: 409 transacción/cliente/tarjeta inexistente; 409 ya rechazada/devuelta. Casos 200 (rechazo según motivo — Aprobado/Bloqueo/Inválido/Sospecha → códigos de reason correspondientes).

#### 17.c. `/Returns` (POST)
**Request**: `TransactionId`, `EntityCode`, `Hash` (NO), `ExpiratonMonth`/`ExpirationYear` (NO), `AmountToReturned`, `TimeTxStart`/`TimetxUpdate` (NO). **Response**: 409 transacción inexistente/ya retornada/rechazada; 409 errores de monto (mayor al pendiente, o ya existe devolución parcial); 409 tarjeta no encontrada/inválida/vencimiento no coincide; 409 transacción no realizada; 409 datos incompletos. 200: devolución parcial (`TRANSACTON_PARTIALY_RETURNED`, sic) o total (`TRANSACTON_RETURNED`, sic).

#### 17.d. `/Process` (POST) — `POST /api/FilProcess/Process`
**Objetivo**: "Procesar archivos y registrar contracargos en el sistema."

**Request** (query): `UserId` (int, SI), `EntityCode` (string, SI). **Request** (body, lista de objetos):
```json
[{ "transactionId": "string", "countRetry": 0, "fraudulentOrReliable": 0, "motiveId": 0, "comment": "string" }]
```
`fraudulentOrReliable`: 1 = fraudulenta, 2 = confiable.

**Response**: 200 "Contracargo/s procesado/s... Cantidad de inserciones: {n}. Cantidad de errores: {n}"; 409 lista vacía; 409 entidad/usuario no encontrado.

#### 17.e. `/health/db` (POST)

---

### 18. API `/PersonType`

#### 18.a. `/CreatePersonType` (POST)
**Request**: `Name`, `entityCode`. **Response**: 200 éxito; 404 nombre vacío / entidad no encontrada / segmentación incorrecta / entidad no segmentada / EntityCode vacío.

#### 18.b. `/UpdatePersonType` (POST)
**Request**: `PersonTypeId`, `Name`. **Response**: 200 éxito; error nombre vacío/registro no encontrado/id menor a cero.

#### 18.c. `/DeletePersonType` (POST)
**Request**: `PersonTypeId`. **Response**: 200 éxito; 404 id incorrecto/no encontrado/relacionado en tabla de relaciones/relacionado con un Cliente.

#### 18.d. `/GetPersonTypeById` (GET)
**Request**: `PersonTypeId`. **Response**: 200 encontrado; 409 id negativo/sin registros.

#### 18.e. `/GetAllPersonTypeByEntity` (GET)
**Request**: `EntityCode`. **Response**: 200 datos encontrados; 404 sin registros/entidad no encontrada.

#### 18.f. `/GetBankTypeRels` (GET) — dentro de PersonType
**Request**: `personId` (INT, SI), `EntityCode` (INT, SI). **Response**: 200 encontrado; 404 tipo de persona no encontrado/sin registros.

#### 18.g. `/GetPersonTypeTripleRel` (GET)
**Request**: `EntityCode`, `personTypeId`, `bankTypeId` (todos String, SI). **Response**: 200 encontrado; 404 sin registros/id inválido.

#### 18.h. `/CreateSegmentation` (POST) — dentro de PersonType
**Request**: `Segmentation` (json, SI) — ej. `{"BankTypeSegmentation": true, "ClientTypeSegmentation": true, "PersonTypeSegmentation": false}`; `EntityCode` (INT, SI). **Response**: 200 creada; 404 entidad no encontrada/ya segmentada.

#### 18.i. `/AssingPersonTypeToRel` (GET)
**Request**: `PerosonTypeId` (sic), `EntityCode`. **Response**: 200 creada; 404 tipo de persona no existe/segmentación incorrecta/relación ya existe.

#### 18.j. `/UnassingAllRel` (GET) — ⚠️ **"(no usar)"**
El propio título del método indica explícitamente **"no usar"**. Borra toda relación asociada a un tipo de Persona (doble o triple), sin modificar la segmentación de la entidad.

**Request**: `PerosonTypeId`. **Response**: 200 eliminada; 404 sin datos relacionados.

#### 18.k. `/UnassignPersonTypeToRel` (GET)
Elimina la relación simple entre tipo de persona y entidad. **Request**: `PerosonTypeId`, `EntityCode`. **Response**: 200 "Relacion Eliminada"; 404 no se encontró relación.

#### 18.l. `/UnassignPersonTypeToTripleRel` (GET)
**Request**: `PerosonTypeId`, `BankTypeId`, `EntityCode`. **Response**: 200 relación eliminada; error no se encontró relación.

#### 18.m. `/GetSegmentationEntity` (GET) — dentro de PersonType
**Request**: `EntityCode`. **Response**: 200; 404 entidad no encontrada.

#### 18.n. `/AssignPersonTypeToTripleRel` (GET)
**Request**: `BankTypeId`, `PersonTypeId`, `EntityCode`. **Response**: 200 relación creada; 404 segmentación incorrecta/ya existe relación.

---

### 19. API `/BankTypes`

Estructura idéntica (mirror) al módulo 18 `/PersonType`, aplicado a "tipo de banca":

| Endpoint | Equivalente en PersonType |
|---|---|
| `/CreateBankType` (POST) | 18.a |
| `/UpdateBankType` (POST) | 18.b |
| `/DeleteBankType` (POST) | 18.c |
| `/GetBankTypeById` (GET) | 18.d |
| `/GetAllBankTypeByEntity` (GET) | 18.e |
| `/GetBankTypeRels` (GET) | 18.f (invertida: lista personas asociadas a un tipo de banca) |
| `/GetBankTypeTripleRel` (GET) | 18.g |
| `/CreateSegmentation` (POST) | 18.h |
| `/AssingBankTypeToRel` (GET) | 18.i |
| `/UnassingAllRel` (GET) — ⚠️ **"(no usar)"** | 18.j |
| `/UnassignBankTypeToRel` (GET) | 18.k |
| `/UnassignBankTypeToTripleRel` (GET) | 18.l |
| `/GetSegmentationEntity` (GET) | 18.m |
| `/AssignBankTypeToTripleRel` (GET) | 18.n |

Todos con los mismos códigos y patrones de request/response que su equivalente en `/PersonType`, sustituyendo "tipo de persona" por "tipo de banca". Nota de fidelidad: varios mensajes de respuesta de este módulo (ej. `CreateBankType`, `GetBankTypeById`) dicen literalmente "tipo de persona" en el texto — indicio de copy/paste del módulo PersonType no corregido por el proveedor.

---

### 20. API `/ClientCard`

#### 20.a. `/CreateCard` (POST)
**Objetivo**: "Poder reportar las tarjetas que tiene emitida un cliente."

**Request**: `Identification`, `Entitycode`, `EmissionDate` (todos String, SI), `Hash` (NO), `ExpirationMonth`/`ExpirationYear` (NO).

**Response**: 200 "Tarjeta asociada con éxito."; 409 identificación/fecha de emisión/código de entidad incorrecto; 409 entidad/cliente no existe; 409 tarjeta ya existe.

---

### 21. API `/CreateFullClient`

#### 21.a. `/CreateFullClient` (POST)
**Objetivo**: orquestador que crea un cliente de punta a punta.

**Request**: `CsvDataEntry` (json, SI) — ejemplo:
```json
{
  "CUIT": "201111111191", "NOMBRE": "PEDRO JUANEZ",
  "PRODUCTO_TIPO": "CUENTA CORRIENTE", "FECHA_ALTA": "2025-02-15",
  "FECHA_BAJA": null, "MONEDA": "1",
  "PRODUCTO_CATEGORIA": "CUENTA EMPRESARIAL",
  "CBU": "1110590940090418135201", "TIPO_BANCA": "EMPRESA",
  "TIPO_PERSONA": "FISICA", "TIPO_CLIENTE": "VIP",
  "ENTITY_CODE": "FT881", "PRODUCT_NAME": "CUENTA CORRIENTE EN PESOS",
  "PRODUCT_NUMBER": "000123456789", "CREATIONMODE_NAME": "ONLINE",
  "EMAIL": "juan.perez@mail.com"
}
```

**Nota de negocio importante**: este endpoint **orquesta internamente** — resuelve/crea en cascada, si no existen: `PersonType`, `BankType`, `Segmentacion`, `ProductType`, `ProductCategory`, `CreationMode`, `ClientGeneralData`, `ClientBankType`, `ClientGeneralType`, `ClientGeneralEmail`, `Product`, `ClientProduct`. El mensaje 200 de éxito describe, para cada entidad, si fue "existente" (reusada) o "creada".

**Response**: 409 entidad bancaria no encontrada para la combinación Identificación+EntityCode; faltantes de campos obligatorios (CUIT, CBU, NOMBRE, etc.); formato incorrecto (CUIT/CBU/IMPORTE solo dígitos); email inválido; longitud máxima excedida (65 genérico, 20 CUIT, 25 CBU); fechas no pueden superar hoy; formatos de fecha aceptados: `yyyy-MM-dd HH:mm:ss`, `yyyy-MM-ddTHH:mm:ss`, `dd/MM/yyyy HH:mm:ss`, `MM/dd/yyyy HH:mm:ss`, `yyyy-MM-dd HH:mm`, `yyyy-MM-ddTHH:mm`, `dd/MM/yyyy HH:mm`, `MM/dd/yyyy HH:mm`, `yyyy-MM-dd`, `dd/MM/yyyy`, `MM/dd/yyyy`.

---

### 22. API `/Authentication`

#### 22.a. `/AuthenticUser` (POST)
**Objetivo**: "Poder loguearse y crear un token para las APIs externas." Token dura 1 día, refresh token dura 7 días.

**Request**: `guid` (String, SI), `secret` (String, SI).

**Response** 200:
```json
{
  "message": "Inicio de sesión correcto", "messageEs": null, "messageEn": null,
  "code": 1,
  "data": { "id": 1, "token": "<JWT>", "refreshToken": "<JWT>", "lastLogin": "2025-09-26T15:58:25.0420798Z" }
}
```
El JWT de ejemplo incluye claims `nameid`, `jti`, `iat`, `expired`, `tempToken`, `nbf`, `exp`, `iss: "Localhost"`, **`aud: "Ardid"`**. 409: guid/secret incorrectos.

#### 22.b. `/RenewAccessTokenFromRefreshToken` (POST)
**Request**: `Token` (String, SI — el RefreshToken). **Response** 200: nuevo `token`, `refreshToken: null`, `lastLogin`. 409: token no enviado / refresh token inválido.

---

### 23. `/FileProcessController`

#### 23.a. `/UploadChargebackTransactionsFile` (POST)
**Objetivo**: "Subir archivos csv para guardar en mongo, y que el servicio de carga masiva procese el mismo."

**Request**: `File` (IFormFile, SI), `EntityId` (string, SI). **Response**: 200 "Archivo cargado exitosamente"; 409 archivo no es CSV; 409 EntityId inválido/entidad no encontrada; 409 error procesando; 409 formato de carga masiva no definido/no respetado.

---

## 10. Observaciones y gaps detectados (resumen — ver detalle en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md))

1. **Base URL no definida** en ningún endpoint (salvo 7 rutas relativas parciales).
2. **Historial de revisiones vacío** — solo "Última revisión: 0" en 170 páginas.
3. **Mecanismo de autorización no explicitado** fuera del módulo `/Authentication`.
4. **Inconsistencia de convención `BankType`**: "1=empresa,2=individuo" (`/ClientBankType`) vs. "1=Cliente,2=Empresa" (`/ClientType`).
5. **Objetivos de endpoint reutilizados/copiados incorrectamente** entre secciones distintas (12.c, 13.b, 13.c, 16.e, 16.f, 18.k, 18.m, 19.a, 19.d, 19.m).
6. **Endpoint sin descripción** (15.j `DeleteCommerceOfCommerceGroup`).
7. **Métodos marcados explícitamente "(no usar)"**: `18.j`/`19.j UnassingAllRel` — nota operativa relevante para cualquier integración futura de Bind PSP.
8. **Nomenclatura Ardid vs Akurtech confirmada por el JWT**: título del documento dice "AKURTECH", pero el JWT de ejemplo del login tiene `"aud": "Ardid"` — confirma el rebranding comercial sobre el mismo sistema técnico.
9. **Posible inconsistencia de tipos**: `Pep`/`So`/`Terrorista` son `Bool` en `SetClientRiskProfile` pero `String` en `ChangeSegmentationClient`.

---
*Ver también: [index.md](index.md) para el mapa completo del módulo, y los archivos de cada funcionalidad ([modulo_transferencias.md](modulo_transferencias.md), [modulo_pagos.md](modulo_pagos.md), [modulo_login.md](modulo_login.md), [blacklist_whitelist_rafagas.md](blacklist_whitelist_rafagas.md)) para el contexto funcional de estos endpoints.*
