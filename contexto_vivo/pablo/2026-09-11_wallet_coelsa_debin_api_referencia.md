---
id: 2026-09-11_wallet_coelsa_debin_api_referencia
pm: pablo
fecha_captura: 2026-09-11
fuente: "Ingesta manual de documentación pública de Coelsa (VPN habilitada) — https://documentacion.coelsa.com.ar/debin/ — lectura completa del sitio (Novedades, Introducción, Componentes, Buenas Prácticas, API Autenticación, Ambientes, Datos, Escenarios, APIs, Servicio de Mensajería). Consultado 2026-09-11."
producto: wallet
tema: Referencia técnica de la API DEBIN de Coelsa (MPO / COELSA.PAYMENTS) — auth, ambientes, catálogo de endpoints, ciclo de vida, contracargo, transferencia pull con consentimiento
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/wallet/coelsa_debin_api_referencia.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Por qué este documento

`wiki/3_recursos/detalle_productos/wallet/debin_y_fondeo.md` documenta muy bien la **historia de implementación de Bind** sobre DEBIN (fondeo de recaudadora, suscripciones, contracargos, bugs reales), pero no existe hasta ahora una **referencia técnica de la API de Coelsa en sí** — qué endpoints expone Coelsa, cuáles debe implementar la entidad (Bind/API Bank) del lado "banco", cómo se autentica, y cómo son los circuitos completos. Este item cubre exactamente ese vacío, para que el PM pueda razonar sobre bugs o mejoras de integración sin depender de la VPN de Coelsa cada vez. **Cruzar con [debin_y_fondeo.md](../../3_recursos/detalle_productos/wallet/debin_y_fondeo.md)** — ese archivo tiene el historial de bugs/fixes reales sobre esta misma superficie de API.

**Dato operativo importante para el PM:** `debin_y_fondeo.md §9` menciona una iniciativa en curso ("Transferencias Pull en Homologación", ticket Coelsa #456632, `2_areas/tareas.md` T-011) para reactivar Transferencia Pull. Este documento trae el **detalle técnico completo** de esa operatoria (JWT `X-TRX-PULL`, los 4 circuitos CBU/CVU, catálogo de errores) — útil como base para esa iniciativa.

## 1. Autenticación

OAuth2 tipo *password grant* contra `/apiAuthV1/auth`:

```
POST https://<AMBIENTE>/apiAuthV1/auth
Authorization: Basic <client_id:secret en base64>
Content-Type: application/x-www-form-urlencoded
grant_type=password&username=<username>&password=<password>
```

Devuelve `{ scope, access_token, token_type: "Bearer", expires_in: 1800 (30 min), client_id }`. Credenciales incorrectas → HTTP 403. Todas las llamadas posteriores llevan `Authorization: Bearer <token>`.

## 2. Ambientes

| Ambiente | Conectividad | Autenticación | DEBIN | Admin credenciales |
|---|---|---|---|---|
| Prueba (test) | Internet, sin VPN | `testauth.coelsa.com.ar` | `testmpo.coelsa.com.ar` | `testadmin.coelsa.com.ar/CoelsaAdmin` |
| Homologación | VPN + certificado cliente HTTPS | `homoauth.coelsa.com.ar/auth` | `homompo.coelsa.com.ar` | `homoauth.coelsa.com.ar/CoelsaAdmin/` |
| Producción | VPN + certificado cliente HTTPS | `auth.coelsa.com.ar/auth` | `debin.coelsa.com.ar` | `auth.coelsa.com.ar/auth/CoelsaAdmin/` |

Componentes del producto: **WEB de Seguridad/CoelsaAdmin** (alta de usuarios/clientes con permisos), **WEB de Monitoreo** (control de garantías), **API Autenticación**, **API DEBIN** (la expone Coelsa), **API BANCOS** (la expone cada entidad — ver §4).

## 3. Estructura de datos y ciclo de vida

- **CBU/CVU**: 22 dígitos, bloque 1 = 3 (banco) + 4 (sucursal) + 1 verificador; bloque 2 = 13 (cuenta) + 1 verificador. El CVU usa el mismo formato — banco `"000"`/sucursal `"0000"` en las operaciones.
- **DEBIN**: `id` alfanumérico de hasta 22 posiciones. Tiene `fecha` de creación y `fechaExpiracion` (después de la cual no se puede ACEPTAR/RECHAZAR). Formato de fechas: `YYYY-MM-DDThh:mm:ss[.nnnnnnn]Z` (UTC).
- **Idempotencia**: si la entidad envía `ori_trx_id` al crear un DEBIN, reenviar el mismo `ori_trx_id` no duplica la operación — Coelsa valida repetidos solo dentro de una ventana de ~45 días corridos; la entidad decide cuándo generar un id nuevo vs. reutilizar uno.
- **Timeouts de las APIs**: mínimo 15s de espera antes de asumir un timeout (HTTP 504). Tabla de timeout por endpoint que Coelsa llama a la entidad: `AvisoDebinPendiente`/`AvisoDebinPendienteCVU`/`AvisoOperacionFinalizada`/`AvisoAdhesionRecurrencia`/`AvisoCVU`/`AvisoDeContracargo` = 15s; `Credito`/`CreditoCVU` = 10s; `Debito` = 15s; `QRConfirmaDebito`/`QRIntencionPago` = 10s; `QRReverso`/`QROperacionFinalizada` = 15s.
- **Reintentos**: ante falla de comunicación, el banco originante reintenta con el mismo id de origen; Coelsa responde "id existente" si ya se procesó. Recomendación oficial: no usar consulta GET por ID en flujos síncronos de la transacción (solo post-mortem) — el uso indebido puede derivar en bloqueos.
- **Conciliación diaria**: archivo de conciliación (versiones 5.0/5.2/6.0) es la fuente de verdad final si no hubo confirmación online (mandatorio incluso con comunicación online exitosa). También existe "Generación Parcial de Archivo" (Archivo Parcial vs. On Hold, ver Prevent) y API de Consulta de Saldos/Garantías.
- **Créditos "forzados"**: cualquier código de respuesta de un `/Credito` distinto de `03`/`04`/`06` se asume error temporal de la entidad — la operación queda compensada igual (NO hay reverso), y se espera que la entidad aplique el crédito por su cuenta vía reintentos propios o el archivo de conciliación. Notificación de créditos forzados disponible por suscripción a "Notificación de Créditos Forzados" con reintentos (15s, multiplicador x2, timeout 5s) hasta las 17hs del día de negocio.

## 4. API BANCOS — lo que Bind debe implementar como entidad (recibe llamadas de Coelsa)

Endpoints administrativos que la entidad expone a Coelsa (gestión de configuración):

| Método | Endpoint | Función |
|---|---|---|
| POST | `/apiDebinV1/Bancos/CuentaEspecial` | Alta de cuenta recaudadora para concepto particular (ej. Plazo Fijo — `PLF`) |
| GET | `/apiDebinV1/Bancos/CuentaEspecial` | Listar cuentas especiales de la entidad |
| POST | `/apiDebinV1/Bancos/ModoBanco` | Cambiar estado Online/Offline de la entidad (permite endpoints alternativos para offline) |
| POST | `/apiDebinV1/Bancos/PostEndPoint` / `PostEndPoint2` | Alta de endpoint (con variante extendida) |
| PUT | `/apiDebinV1/Bancos/PutEndPoint/{id}` | Modificar endpoint |
| DELETE | `/apiDebinV1/Bancos/DeleteEndPoint` | Eliminar endpoint |
| GET | `/apiDebinV1/Bancos/GetEndPoint/{id}`, `GetEndPoint2/{id}`, `GetEndPoint3/{id}`, `GetEndPointLista` | Consultas de endpoint(s) |
| GET | `/apiDebinV1/Bancos/EstadoBanco/{banco}` | Consultar si una entidad está activa |

**Endpoints (avisos/webhooks) que Coelsa invoca sobre la entidad** — el nombre real (`[EPBanco]`) es el configurado vía `PostEndPoint`:

| Endpoint | Cuándo | Respuesta esperada |
|---|---|---|
| `POST [EP]/AvisoDebinPendiente` / `AvisoDebinPendienteCVU` | Nuevo DEBIN creado, aviso al banco/PSP comprador | HTTP 200 |
| `POST [EP]/Credito` / `CreditoCVU` | Coelsa pide acreditar al vendedor | Síncrono: código éxito o error (03/04/06 = rechazo real; cualquier otro = "forzado", ver §3) |
| `POST [EP]/Debito` | Coelsa pide debitar al comprador | Síncrono: éxito/error |
| `POST [EP]/AvisoOperacionFinalizada` | Cierre de operación (incluye reversos) | HTTP 200 |
| `POST [EP]/AvisoAdhesionRecurrencia` | Nueva adhesión a recurrencia registrada | HTTP 200 |
| `POST [EP]/AvisoCVU` | Aviso a PSP o banco cuando el crédito/débito involucra una CVU (push y pull) | HTTP 200 |
| `POST [EP]/AvisoDeContracargo` | Contracargo ya validado/procesado por Coelsa (solo informativo, Coelsa ya movió garantías) | HTTP 200 |
| `POST [EP]/AvisoEcho` | Chequeo de conectividad | HTTP 200 (marcado "En desuso" en la doc actual) |

Endpoints opcionales configurables por separado: `creditoti` (crédito por transferencia inmediata) y `contracargo` (aviso de contracargo), si no se configuran usan el endpoint default.

**Multiplicidad de endpoints**: una entidad puede configurar más de un endpoint (ej. distinto operador para clientes individuos vs. corporativos) — el endpoint aplicable se fija en el momento de adhesión de cada cuenta. Existe un endpoint de recovery/contingencia (solo activo si Coelsa lo indica explícitamente).

## 5. APIs que Bind invoca sobre Coelsa (API COMPRADOR / VENDEDOR / DEBIN)

**Comprador:** `POST Comprador/Adhesion`, `GET Comprador/Comprador/{cuit}`, `POST Comprador/BajaCuenta`, `POST [Comprador|Vendedor]/AdherirRecurrencia` (alta/baja de una recurrencia; valor `1` en baja = definitiva, solo el comprador puede reactivar tras una baja definitiva), `GET/POST Comprador/Recurrencia/{id}`, `POST [Comprador|Vendedor]RecurrenciaLista` (filtros: CUIT comprador obligatorio, CUIT vendedor y CBU comprador opcionales), `POST Comprador/SolicitudContraCargo` (síncrono — dentro de los días que marca la norma BCRA para contracargo de un DEBIN preautorizado).

**Vendedor:** `POST Vendedor/Adhesion`, `GET Vendedor/Vendedor/{cuit}`, `POST Vendedor/ListadoVendedores`, `POST Vendedor/BajaCuenta`, `POST Vendedor/AdherirRecurrencia`, `GET/POST Vendedor/Recurrencia/{id}`, `POST Vendedor/Prestacion` (alta de "prestaciones"/servicios recurrentes), `GET Vendedor/Prestacion/{cuit}`, `DELETE Vendedor/DeletePrestacion/{cuit}/{prestacion}`, `POST Vendedor/VendedorRecurrenciaLista`, `POST Vendedor/Devolucion` (solo para TRANSFERENCIA/CASHOUT, una única devolución por operación, la original debe estar en "ACREDITADO").

**DEBIN:** `POST Debin/Debin` (crear — soporta `ori_trx_id` idempotente), `POST Debin/ConfirmaCredito` / `ConfirmaDebito` (respuestas del banco), `GET Debin/Debin/{id}` (y variantes `Debin2`/`Debin3` para nuevas búsquedas por id propio), `POST Debin/Lista` (consulta batch, ⚠️ ver bug histórico de filtros rotos ya documentado en `debin_y_fondeo.md §3.0.1`), `POST Debin/TransferenciaPull` (ver §7).

## 6. Escenarios operativos DEBIN (spot)

Flujo estándar "orden de pago": el vendedor (a través de su banco) crea el DEBIN → Coelsa valida adhesión del vendedor (si no está adherido, error inmediato) → aviso `AvisoDebinPendiente` al banco/PSP comprador → el comprador acepta en su home banking → banco comprador confirma vía `ConfirmaDebito` → Coelsa mueve garantías → `Credito` al banco vendedor → `AvisoOperacionFinalizada` a ambos.

Casos especiales documentados: comprador no adherido (igual se ejecuta el DEBIN por el endpoint default), confirmación fuera de la vigencia (error, sin re-chequear la expiración si ya estaba vigente al recibir la confirmación), banco offline (usa el endpoint secundario/alternativo configurado), sin garantía suficiente en el banco comprador (el DEBIN no se completa, el banco comprador debe reversar el débito ya aplicado a su cliente).

## 7. Transferencia Pull con consentimiento (JWT `X-TRX-PULL`)

Habilita transferencias "pull" **sin ser un DEBIN recurrente clásico**: requiere que la cuenta esté enrolada/haya dado consentimiento explícito (solo personas físicas). El flujo es casi idéntico a DEBIN recurrente, pero `POST /apiDebinV1/Debin/TransferenciaPull` recibe un header adicional `X-TRX-PULL: Bearer <JWT>` (la palabra "Bearer" es opcional) con este payload (definición técnica de PwC / mesas técnicas BCRA):

```json
{
  "exp": 1674308677,
  "iss_bcra_id": "00998",
  "iat": "2022-09-21T10:44:37.397-03:00",
  "jti": "BZyYc",
  "user_cuit": "20000000990",
  "aud_bcra_id": "00999",
  "scope": "accounts.debit",
  "accounts": "9986968700000000001003",
  "Trace_id": "A000000000000003"
}
```

- Cuando la operación la inicia una billetera de **otro** administrador (no Coelsa), ese administrador es responsable de validar el token — Coelsa solo aporta el canal.
- Ventana total de la operación: **25 segundos** (incluye avisos de débito y crédito).
- **4 circuitos** según origen/destino CBU o CVU (CBU-CBU, CBU-CVU, CVU-CBU, CVU-CVU) — en los casos con CVU en alguno de los extremos, el `X-TRX-PULL` se reenvía en el header del `AvisoDebinPendienteCVU`/`AvisoDebinPendiente` correspondiente para que el PSP valide el consentimiento.
- **17 códigos de error específicos** (HTTP 403), todos con prefijo de validación del JWT: `0159` header inválido, `0160` payload inválido, `0161` issuer inválido, `0162` public key no encontrada, `0163` `exp` inválido, `0164` firma/expiración inválida, `0165` `sub` inválido, `0166` `aud` inválido, `0167` `iat` inválido, `0168` `scope` inválido, `0169`/`0171` `accounts` inválido/no coincide con el request, `0170`/`0173` `trace_id`/CUIT comprador-vendedor no coinciden, `0172` `sub` no coincide con el request, `0174` tiempo de vida del token inválido, `0175`/`0176` `bcra_id` no coincide con `iss`/`aud`.
- Requiere vincular previamente una **clave pública (Base64)** a un usuario en CoelsaAdmin para poder validar la firma del JWT.

## 8. Contracargo (DEBIN preautorizado)

El comprador solicita la devolución de un débito ya ejecutado dentro del plazo normado por BCRA (30 días, ver también `debin_y_fondeo.md` "Contracargos de DEBIN Recurrente" para el detalle operativo de Bind del lado receptor). Documento de referencia oficial adicional (no descargado, requiere VPN): "MPO CONTRACARGO".

## 9. Scoring y rechazos automáticos (integración con Prevent)

Cada operación recibe un `evaluacion.puntaje` (0-99) y `evaluacion.reglas` en la respuesta de creación/confirmación de DEBIN — es el mismo motor de scoring de **COELSA PREVENT** (ver item separado sobre Prevent/CPF). El "Servicio de Rechazos Automáticos" (nov. 2024) permite a la entidad configurar un umbral desde el que las operaciones se rechazan solas — la configuración de ese umbral **no está en la API DEBIN**, sino en la web de COELSA.PREVENT (ver item de Prevent).

## Changelog conocido de Coelsa (Novedades del sitio DEBIN, hasta la fecha de esta ingesta)

Solo el sitio **DEBIN** tiene página de "Novedades" (Comercio/CVU/Prevent/CPF no la tienen — para detectar cambios ahí hay que re-comparar el contenido completo contra esta ingesta). Resumen cronológico descendente conocido a 2026-09-11:

- **2026-09**: Manual Procesamiento CCT actualizado (endpoints plan de pagos, avisos, cuentas de comisiones, consultas por ID); se agrega impuesto SIRTAC al Manual de Pagos con Transferencia PCT.
- **2026-08**: nueva funcionalidad **REVERSAL** (regularización excepcional de fondos por transacciones no deseadas).
- **2026-07**: se elimina la sección "Security" del manual PCT; mejoras a Archivo Parcial de Conciliación / Monitor de Garantías ("Archivo Parcial vs. On Hold — MPV1"); renombrado el manual de COELSA.PAY COBRANZA.INMEDIATA.
- **2026-06 / 2026-05**: mejoras a mensajería de avisos de CCT (más datos de préstamo, fecha de negocio); se incorpora consulta `GET api/v1/payment/{reverse_domain}/{qr_id_trx}`; se incorpora Manual PCT (info NFC) y Manual COELSA.PAY COBRANZA.INMEDIATA.
- **2026-04**: documentos funcionales nuevos — "Comercios CBU en PCT", "Cuenta Concentradora", "Propuesta NFC"; actualización del funcional de PAGO QR.
- **2026-02**: "Múltiple Endpoint con Subtipo"; actualización de Versionado de Mensajería.
- **2025-09 y anteriores**: incorporación progresiva de PAGO QR, CASHOUT (incl. variante cross-border), Diccionario COELSA.PAYMENTS, Prerequisitos, Múltiple Endpoint, Debin Programado, Scoring (nov. 2024), Monitor de Garantías (oct. 2024), API Saldos (may. 2024).

## Anexo — payloads reales (request/response literales de la documentación)

> Se preservan tal cual figuran en la fuente (valores de prueba de Coelsa), quitando solo el JWT de ejemplo de los headers `Authorization` (irrelevante, es de testing). Sirven como referencia directa para debugging o para armar un mock de pruebas.

### Autenticación

```
POST https://<AMBIENTE>/apiAuthV1/auth
Authorization: Basic <base64(client_id:secret)>
Content-Type: application/x-www-form-urlencoded

grant_type=password&username=<username>&password=<password>
```

Response:
```json
{
  "scope": "https://auth.coelsa.com.ar/apiAuthV1/auth/.*",
  "access_token": "<Token>",
  "token_type": "Bearer",
  "expires_in": 1800,
  "client_id": null
}
```

### API BANCOS (Bind expone, Coelsa invoca para gestión)

**Alta Cuenta Recaudadora Concepto Particular** — `POST /apiDebinV1/Bancos/CuentaEspecial`
```json
{
  "cuenta": { "cbu": "9980025700000000000284", "cuit": "20333048494" },
  "activo": true
}
```

**Aviso de Contracargo a Entidad del Vendedor** — `POST [EP]/AvisoDeContracargo`
```json
{
  "operacionOriginal": {
    "id": "MRD06ZO9WEWKXJX95GP7XY",
    "tipo": "debin",
    "detalle": { "importe": 45.0, "moneda": "80", "motivo": "razon" }
  },
  "id": "123",
  "fechaNegocio": "2019-12-20T19:22:02.204Z",
  "comprador": { "cuit": "30576124275", "cuenta": { "cbu": "1980001730000000568679" } },
  "vendedor": { "cuit": "33711585619", "cuenta": { "cbu": "1980001730000001136251" } }
}
```
Response esperada del banco: HTTP 200 (solo confirma recepción — Coelsa ya movió las garantías, este mensaje es informativo).

**Establecer Estado Online/Offline** — `POST /apiDebinV1/Bancos/ModoBanco`
```json
{ "estado": { "codigo": "ON" } }
```

**Crear Endpoint** — `POST /apiDebinV1/Bancos/PostEndPoint`
```json
{
  "EndPointAlta": {
    "Id": "TEST330",
    "Descripcion": "TESTING330",
    "Primario": "https://testdebin.coelsa.com.ar/apiDebinV1/CoelsaTest/",
    "Secundario": "https://testdebin.coelsa.com.ar/apiDebinV1/CoelsaTest/",
    "Red": "COELSA",
    "Default": false,
    "creditoti": null,
    "contraCargo": null,
    "aviso_cvu": null,
    "tic": null
  }
}
```

**Eliminar Endpoint** — `DELETE /apiDebinV1/Bancos/DeleteEndPoint`
```json
{ "EndPointBaja": { "Id": "CLIENTES PABLO" } }
```

### API COELSA — avisos/webhooks que Coelsa envía y Bind debe responder

**`POST [EPBanco]/AvisoDebinPendiente`** — nuevo DEBIN, aviso al banco del comprador:
```json
{
  "operacion": {
    "comprador": {
      "cuenta": { "banco": "999", "sucursal": "2798", "alias": "|", "cbu": "9992798100000000001003", "esTitular": 0, "moneda": "032", "tipo": "20" },
      "codigo": "", "titular": "PRUEBA PostMan - CoelsaTest 20000000990", "cuit": "20000000990"
    },
    "vendedor": {
      "cuenta": { "banco": "999", "sucursal": "9226", "terminal": "", "alias": "", "cbu": "9999226600000000000031", "esTitular": 0, "moneda": "032", "tipo": "20" },
      "codigo": "", "titular": "PRUEBA PostMan - CoelsaTest 20000000990", "cuit": "20000000990"
    },
    "detalle": {
      "fecha": "2019-12-20T17:58:07.307Z", "fechaExpiracion": "2019-12-20T17:58:07.307Z",
      "concepto": "ALQ", "idUsuario": 0, "idComprobante": 0, "moneda": "032", "importe": 1000.0, "mismoTitular": 0
    }
  },
  "debin": {
    "id": "80V1JXON1733JY1NZ64EL7",
    "estado": { "codigo": "00", "descripcion": "PERSISTIDO" },
    "estadoComprador": { "codigo": "00", "descripcion": "ADHERIDO" }
  },
  "preautorizado": false,
  "evaluacion": { "puntaje": 0, "reglas": "" }
}
```
Response esperada: HTTP 200 — luego el banco debe pedir la autorización al cliente y, una vez obtenida, debitar.

**`POST [EP]/AvisoOperacionFinalizada`** — cierre de operación (éxito o reversa):
```json
{
  "resultado": { "codigo": "string", "descripcion": "string" },
  "operacion": {
    "estado": { "codigo": "string", "descripcion": "string" },
    "ori_trx": "string", "ori_terminal": "string", "ori_adicional": "string", "tipo": "string", "id": "string"
  },
  "comprador": { "cuit": "string", "cbu": "string" },
  "vendedor": { "cuit": "string", "cbu": "string" }
}
```

**`POST [EP]/AvisoAdhesionRecurrencia`**:
```json
{
  "recurrencia": {
    "id": 115,
    "vendedor": { "cuit": "20000000192" },
    "comprador": { "cuit": "27375575847", "cbu": "9982879600000000000338", "estado": "00" },
    "debin": {
      "moneda": "032", "detalle": "prueba", "concepto": "ALQ",
      "prestacion": "PRUEBA PostMan - CoelsaTest", "referencia": "prueba recurrencia"
    }
  }
}
```
Response esperada: HTTP 200.

**`POST [EP]/Credito`** — Coelsa pide acreditar al vendedor (síncrono):
```json
{
  "objeto": { "tipo": "transferencia", "ori_trx_id": 51616187 },
  "credito": {
    "cuit": "20333048494", "banco": "998", "sucursal": "8851",
    "cuenta": { "cbu": "9988851800000000000628" }, "titular": "PAYLINK PRUEBA"
  },
  "debito": {
    "cuit": "20000000141", "banco": "999", "sucursal": "2589",
    "cuenta": { "cbu": "9992589300000000000154" }, "titular": null
  },
  "concepto": "ALQ", "descripcion": null, "idUsuario": 0, "idComprobante": 0,
  "importe": { "moneda": "032", "importe": 7.77 },
  "mismoTitular": 0, "ori_trx": "", "ori_terminal": "", "ori_adicional": "20191001",
  "datosGenerador": {
    "ipCliente": "", "tipoDispositivo": "", "plataforma": "", "imsi": "", "imei": "",
    "ubicacion": { "lat": 0, "lng": 0, "precision": 0 }
  }
}
```
`CreditoCVU` usa exactamente el mismo esquema — se distingue solo por el endpoint (`/CreditoCVU`) que la entidad configuró para operaciones destino-CVU.

**`POST [EP]/Debito`** — Coelsa pide debitar al comprador (síncrono):
```json
{
  "objeto": { "tipo": "DEBIN", "id": "X76V4MR2Z1J5MO8NDEZOL1", "preautorizado": false },
  "credito": { "cuit": "20333048494", "banco": "998", "sucursal": "0000", "cuenta": { "cbu": "9984353300000000000017" } },
  "debito": { "cuit": "27375575847", "banco": "998", "sucursal": "2879", "cuenta": { "cbu": "9982879600000000000338" } },
  "importe": { "moneda": "032", "importe": 500000.0 },
  "fechaHora": "2019-12-20T18:57:38.990Z", "fechaNegocio": "2019-12-20T18:57:38.990Z",
  "ori_trx": "string", "ori_terminal": "string", "ori_adicional": "string",
  "evaluacion": { "puntaje": 0, "reglas": "" }
}
```

**`POST [EP]/AvisoCVU`** — aviso a PSP/banco cuando interviene una CVU:
```json
{
  "operacionCVU": {
    "tipo": "PENDIENTE", "id": "EZ4K6DVNOGM7PE495J8LQ7", "cbu": "9988851800000000000628",
    "fecha_negocio": "2019-12-20T19:15:01.254Z", "moneda": "032", "importe": 7.77,
    "id_psp": 4, "cuit_psp": "20333048494", "cvu": "0000004800000000014461", "cuit_cvu": "20000014452",
    "titular_cvu": "PRUEBA PostMan - CoelsaTest",
    "url_psp": "https://muxiplacetest.firstdata.com.ar:9443/muxigateway/v1/notifications/"
  }
}
```

### API COMPRADOR (Bind invoca sobre Coelsa)

**Adhesión** — `POST /apiDebinV1/Comprador/Adhesion`:
```json
{
  "comprador": {
    "cuenta": { "cbu": "9983560600000000000024" },
    "contacto": { "email": "pabloabecasis@gmail.com" },
    "cuit": "20333048494",
    "endpoint": "localhost"
  }
}
```

**Baja Cuenta** — `POST /apiDebinV1/Comprador/BajaCuenta`:
```json
{ "comprador": { "cuit": "20000000117", "cuenta": { "cbu": "9981595600000000000123" } } }
```

**Adhesión a Recurrencia** — `POST /apiDebinV1/[Comprador|Vendedor]/AdherirRecurrencia`:
```json
{
  "recurrencia": {
    "vendedor": { "cuit": "20000000583" },
    "comprador": { "cuit": "27375575847", "cbu": "9984788700000000000420" },
    "debin": {
      "moneda": "032", "detalle": "pruebarecurrencia", "concepto": "ALQ",
      "prestacion": "PruebasMica", "referencia": "string"
    },
    "id": 127, "activo": true, "tipo_adhesion": 0
  }
}
```

**Solicitud de Contracargo Comprador** — `POST /apiDebinV1/Comprador/SolicitudContraCargo` (síncrono):
```json
{
  "operacionOriginal": {
    "id": "WORD6LEN8QGDRE09M1Y30V", "tipo": "debin",
    "detalle": { "importe": 10560.00, "moneda": "840", "motivo": "inicia" }
  },
  "comprador": { "cuit": "27375575847", "cuenta": { "cbu": "9984788700000000000420" } },
  "vendedor": { "cuit": "20000000583", "cuenta": { "cbu": "9985188000000000000611" } }
}
```
Secuencia completa: banco débito llama `SolicitudContraCargo` → Coelsa responde 200-OK al banco débito y en paralelo llama `POST [EP]/AvisoDeContraCargo` al banco crédito/vendedor → se debita dentro de garantías al banco crédito y se acredita dentro de garantías al banco débito.

### API VENDEDOR (Bind invoca sobre Coelsa)

**Adhesión** — `POST /apiDebinV1/Vendedor/Adhesion`:
```json
{
  "vendedor": {
    "cuit": "20309267789", "sucursal": "8056", "nombre_fantasia": "EmilianoMior",
    "rubro": "VARIOS", "endpoint": "TESTING ALE",
    "cuenta": { "cbu": "9998056600000000000109" },
    "contacto": { "email": "emior@coelsa.com.ar" }
  }
}
```

**Alta de Prestaciones** — `POST /apiDebinV1/Vendedor/Prestacion`:
```json
{
  "vendedor": {
    "cuit": "30000000015",
    "prestaciones": { "nombre": "Prestacion02", "ayuda_referencia": "Prestacion02Referencia01", "min": 0, "max": 0 }
  }
}
```

### Secuencia completa — DEBIN SPOT origen CBU destino CVU (ejemplo de flujo paso a paso)

1. Banco Vendedor: `POST /apiDebinV1/Debin/Debin` (destino = una CVU) → Coelsa valida CVU, PSP y cuenta recaudadora del PSP.
2. Coelsa → PSP Comprador (Billetera): `POST [EPPSP]/AvisoDebinPendienteCVU` (mismo esquema que `AvisoDebinPendiente` de arriba). Plazo de aprobación por el usuario: 1 minuto a 3 días (según `fechaExpiracion`); pasado ese plazo, el DEBIN pasa a `VENCIDO`.
3. Usuario acepta en la Billetera → Billetera: `POST /apiDebinV1/Debin/ConfirmaDebitoCVU`.
4. Coelsa → Banco Comprador: `POST [EPBanco]/AvisoDebinPendiente` (genera un DEBIN Recurrente interno para mover fondos de la CBU origen a la CBU recaudadora de la CVU destino).
5. Banco Comprador responde: `POST /apiDebinV1/Debin/ConfirmaDebito` → Coelsa mueve garantías y llama `POST [EP]/Credito` al Banco Vendedor.
6. Ante error en cualquier paso, se dispara `AvisoOperacionFinalizada` a los actores ya notificados hasta ese punto (vendedor+PSP si falló el paso 2; vendedor+comprador+PSP si falló desde el paso 4 en adelante).

(Los otros 3 circuitos — DEBIN recurrente CBU-CVU, SPOT/recurrente CVU-CBU, SPOT/recurrente CVU-CVU — siguen la misma lógica de pasos, cambiando solo qué actor es CBU vs. CVU en cada punta; documentados con el mismo nivel de detalle en la fuente original si hace falta reconstruirlos.)

## Confianza y gaps

- Confianza **alta**: contenido leído directamente de la documentación oficial vigente.
- **No verificado en esta ingesta**: si Bind ya usa o planea usar `REVERSAL` (nueva func. ago-2026) o el "Servicio Multiple Endpoint" — quedan como oportunidades a evaluar, no como gap (no hay contradicción con nada documentado, solo falta de decisión de producto).
