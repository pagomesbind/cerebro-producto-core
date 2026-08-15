# Herramientas Operativas — Botón Simple (Estilo, Canal, Stock y Alta Masiva de CVU)

> Estado: en producción. Reubicado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` en la reestructuración PARA en cascada (2026-08-12).

## 1. Configurar estilo del Botón de Pago (PROD)

1. Obtener JWT desde `http://10.22.0.73/swagger` (credenciales internas — pedir al equipo de Integraciones).
2. Autenticarse en `http://10.22.0.57/swagger`.
3. Buscar el Collector en BD `BotonSimple.Payment.DB` para replicar datos en el endpoint de edición.
4. Consumir por swagger el **PATCH de CollectorBotonSimple**, completando `X-entidad`, `CommerceCode`, `BranchCode`, `CashCode`, `PaymentLinkDuration` (sacados del registro de la BD), `HasOwnStyle = true`, `MainColor`, `SecondaryColor`, `Image` (especificados en la solicitud). Resto de datos vacíos (check "Send empty value").

**Para STG:** ingresar a `https://admin-checkout-staging.epays.services/` (credenciales internas — pedir al equipo). Ir a **Recaudadores**, buscar el comercio (solo muestra el Nro de Sucursal), y editar el botón con color e imagen directamente ahí.

## 2. Crear canal de Botón Simple en PROD (diagnóstico/resolución de errores)

1. Obtener JWT desde `http://10.22.0.73/swagger` (mismas credenciales que §1).
2. Autenticarse en `http://10.22.0.57/swagger`.
3. Endpoint **POST – Crea un recaudador de Botón Simple**.

**Datos del comercio:** `Cuit`, `BranchCode` (código de sucursal con "S"), `CashCode` (código de caja), `CodeComerce` (ej. `C1234`), `EntityCode` (ej. `A132`), `Mcc` (según referencia BCRA/VISA/AFIP).

**Datos del botón:** `BusinessName` (recomendado: razón social), `IsActive=true`, `MainColor`/`SecondaryColor`, `File` (logo PNG).

**Datos del responsable:** `NameOwner`/`LastNameOwner`/`DocumentOwner` — pueden ir vacíos (se usa Decidir).

**Datos bancarios:** `Cbu` (opcional).

**Configuración de pagos:** `PaymentRules`, `CaptionDecidir` (valor fijo `00130250`), `CaptionCybersource` (vacío), `PaymentLinkDuration` (`900`). Resto de campos vacíos.

**Verificación:** el recaudador creado puede verificarse en la base de Botón Simple, tabla `collectors`.

## 3. Stock de CVU para Botón 2.0

**Parámetros obligatorios:** en el path siempre usar `OWNER` dentro del segmento `view`; header `X-ENTIDAD` con el ID del collector correspondiente.

Ejemplo de request: `POST http://10.210.1.23/v1/banks/322/view/owner/cantidad/50/wallet/cvuStock` (el `50` es la cantidad de CVUs a crear, modificable en la URL). Header: `x-entidad: 146`.

Swagger: STG `http://10.210.1.23/swagger/index.html`, Producción `http://10.22.0.31/swagger/index.html`.

## 4. Alta de CVU masivo para BS 2.0 por JMeter (PROD)

Se genera un JMeter para procesar el alta de CVU de manera masiva, en reemplazo del endpoint que los genera en batch, hasta que ese inconveniente esté resuelto.

- Archivos de referencia en Notion: `Alta_CVU_Masiva_BS.jmx` (script JMeter), `AltaCvuBS.csv` (entrada de referencia).
- Respetar mayúsculas y minúsculas en la cabecera (variables) de los archivos que procesa JMeter.
- El `clientId` se toma a partir del último existente en la base para ese collector + 1, correlativo. Si el Collector no tiene ninguna cuenta creada, se puede crear desde `clientId=1`.
- El JMeter ejecuta el endpoint de la **API Financial** para Crear CVU, recibiendo `clientId` (del archivo de entrada), `Cuit` y `Name` (fijos, ingresados desde el Collector).
- En **Header Manager** debe aclararse `x-entidad` con el id del collector correspondiente.
- El archivo de salida devuelve el CVU creado para cada `clientId`; si dio error, devuelve `0`.

## 5. Alta Masiva de Cajas con CVU (PROD)

JMeter (`CVU_Alta_masiva_de_cajas_-_Swagger_(1).jmx`) que crea una caja en Comercio con su CVU y luego le asigna un Alias.

- **Variables**: ruta y nombre del archivo de entrada y salida. Modificar manualmente **Entidad | Comercio | Sucursal** donde se crearán las cajas.
- El CSV requiere columnas `Nombre` y `Alias` (respetando mayúsculas).
- El archivo de salida agrega el **Código de Caja** creado junto con su CVU, más las variables de Nombre y Alias utilizadas.

⚠️ **Antes de ejecutar, informar al área de infraestructura** para monitoreo de recursos.

APIs afectadas: `MiddlewareAggregatorDB`, `SharedComercioDB`. Endpoints: `http://10.22.0.17/api/v1/comercios/{comercio}/sucursales/{sucursal}/cajas` (+ `/{idCaja}`). (Documento de referencia en Notion: `SYO-Alta_Masiva_de_Cajas_con_CVU-300626-125317.pdf`.)

## Ver también
- [configuracion_de_entidades.md](configuracion_de_entidades.md) — creación de la entidad sobre la que operan estas herramientas.
- [detalle_productos/adquirencia/carga_masiva_cajas_rxt.md](carga_masiva_cajas_rxt.md) — carga masiva equivalente para RxT (endpoint dedicado, no JMeter).

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/adquirencia/configuracion_entidades_y_comercios.md` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
