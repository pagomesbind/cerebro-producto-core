# Referencia técnica — API DEBIN de Coelsa (MPO / COELSA.PAYMENTS)

> Estado: en producción (documentación de referencia — Bind opera contra esta API; no es la API pública de Bind). Fuente: documentación pública de Coelsa (VPN habilitada), https://documentacion.coelsa.com.ar/debin/ (Novedades, Introducción, Componentes, Buenas Prácticas, API Autenticación, Ambientes, Datos, Escenarios, APIs, Servicio de Mensajería), sitio completo. Consultada 2026-09-11.
>
> **Distinción importante:** [debin_y_fondeo.md](debin_y_fondeo.md) documenta muy bien la **historia de implementación de Bind** sobre DEBIN (fondeo de recaudadora, suscripciones, contracargos, bugs reales) — este archivo cubre la **referencia técnica de la API de Coelsa en sí**: qué endpoints expone Coelsa, cuáles debe implementar la entidad (Bind/API Bank) del lado "banco", cómo se autentica, y cómo son los circuitos completos. Cruzar ambos archivos al investigar bugs o mejoras de integración.
>
> **Dato operativo:** [debin_y_fondeo.md §9](debin_y_fondeo.md) documenta una iniciativa en curso ("Transferencias Pull en Homologación", ticket Coelsa #456632, `2_areas/tareas.md` T-011) para reactivar Transferencia Pull. Este documento trae el **detalle técnico completo** de esa operatoria (JWT `X-TRX-PULL`, los 4 circuitos CBU/CVU, catálogo de errores) en la §7 — útil como base para esa iniciativa.

## 1. Autenticación

OAuth2 tipo *password grant* contra `/apiAuthV1/auth`:

```
POST https://<AMBIENTE>/apiAuthV1/auth
Authorization: Basic <client_id:secret en base64>
Content-Type: application/x-www-form-urlencoded

grant_type=password&username=<username>&password=<password>
```

Devuelve `{ scope, access_token, token_type: "Bearer", expires_in: 1800 (30 min), client_id }`. Credenciales incorrectas → HTTP 403. Todas las llamadas posteriores llevan `Authorization: Bearer <token>`.

Response real:
```json
{
  "scope": "https://auth.coelsa.com.ar/apiAuthV1/auth/.*",
  "access_token": "<Token>",
  "token_type": "Bearer",
  "expires_in": 1800,
  "client_id": null
}
```

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
- **Timeouts de las APIs**: mínimo 15s de espera antes de asumir un timeout (HTTP 504). Timeout por endpoint que Coelsa llama a la entidad: `AvisoDebinPendiente`/`AvisoDebinPendienteCVU`/`AvisoOperacionFinalizada`/`AvisoAdhesionRecurrencia`/`AvisoCVU`/`AvisoDeContracargo` = 15s; `Credito`/`CreditoCVU` = 10s; `Debito` = 15s; `QRConfirmaDebito`/`QRIntencionPago` = 10s; `QRReverso`/`QROperacionFinalizada` = 15s.
- **Reintentos**: ante falla de comunicación, el banco originante reintenta con el mismo id de origen; Coelsa responde "id existente" si ya se procesó. Recomendación oficial: no usar consulta GET por ID en flujos síncronos de la transacción (solo post-mortem) — el uso indebido puede derivar en bloqueos.
- **Conciliación diaria**: archivo de conciliación (versiones 5.0/5.2/6.0) es la fuente de verdad final si no hubo confirmación online (mandatorio incluso con comunicación online exitosa). También existe "Generación Parcial de Archivo" (Archivo Parcial vs. On Hold, ver [coelsa_prevent_scoring_y_on_hold.md](../../cumplimiento_normativo/coelsa_prevent_scoring_y_on_hold.md)) y API de Consulta de Saldos/Garantías.
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

## 5. APIs que Bind invoca sobre Coelsa (COMPRADOR / VENDEDOR / DEBIN)

**Comprador:** `POST Comprador/Adhesion`, `GET Comprador/Comprador/{cuit}`, `POST Comprador/BajaCuenta`, `POST [Comprador|Vendedor]/AdherirRecurrencia` (alta/baja de una recurrencia; valor `1` en baja = definitiva, solo el comprador puede reactivar tras una baja definitiva), `GET/POST Comprador/Recurrencia/{id}`, `POST [Comprador|Vendedor]RecurrenciaLista` (filtros: CUIT comprador obligatorio, CUIT vendedor y CBU comprador opcionales), `POST Comprador/SolicitudContraCargo` (síncrono — dentro de los días que marca la norma BCRA para contracargo de un DEBIN preautorizado).

**Vendedor:** `POST Vendedor/Adhesion`, `GET Vendedor/Vendedor/{cuit}`, `POST Vendedor/ListadoVendedores`, `POST Vendedor/BajaCuenta`, `POST Vendedor/AdherirRecurrencia`, `GET/POST Vendedor/Recurrencia/{id}`, `POST Vendedor/Prestacion` (alta de "prestaciones"/servicios recurrentes), `GET Vendedor/Prestacion/{cuit}`, `DELETE Vendedor/DeletePrestacion/{cuit}/{prestacion}`, `POST Vendedor/VendedorRecurrenciaLista`, `POST Vendedor/Devolucion` (solo para TRANSFERENCIA/CASHOUT, una única devolución por operación, la original debe estar en "ACREDITADO").

**DEBIN:** `POST Debin/Debin` (crear — soporta `ori_trx_id` idempotente), `POST Debin/ConfirmaCredito` / `ConfirmaDebito` (respuestas del banco), `GET Debin/Debin/{id}` (y variantes `Debin2`/`Debin3` para nuevas búsquedas por id propio), `POST Debin/Lista` (consulta batch, ⚠️ ver bug histórico de filtros rotos ya documentado en [debin_y_fondeo.md §3.0.1](debin_y_fondeo.md)), `POST Debin/TransferenciaPull` (ver §7).

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

El comprador solicita la devolución de un débito ya ejecutado dentro del plazo normado por BCRA (30 días, ver también [debin_y_fondeo.md](debin_y_fondeo.md) "Contracargos de DEBIN Recurrente" para el detalle operativo de Bind del lado receptor). Documento de referencia oficial adicional (no descargado, requiere VPN): "MPO CONTRACARGO".

## 9. Scoring y rechazos automáticos (integración con Prevent)

Cada operación recibe un `evaluacion.puntaje` (0-99) y `evaluacion.reglas` en la respuesta de creación/confirmación de DEBIN — es el mismo motor de scoring de **COELSA PREVENT** (ver [coelsa_prevent_scoring_y_on_hold.md](../../cumplimiento_normativo/coelsa_prevent_scoring_y_on_hold.md) y [coelsa_cpf_central_prevencion_fraude.md](../../cumplimiento_normativo/coelsa_cpf_central_prevencion_fraude.md)). El "Servicio de Rechazos Automáticos" (nov. 2024) permite a la entidad configurar un umbral desde el que las operaciones se rechazan solas — la configuración de ese umbral **no está en la API DEBIN**, sino en la web de COELSA.PREVENT.

## Changelog conocido de Coelsa (Novedades del sitio DEBIN, hasta la fecha de esta ingesta)

Solo el sitio **DEBIN** tiene página de "Novedades" (Comercio/CVU/Prevent/CPF no la tienen — para detectar cambios ahí hay que re-comparar el contenido completo contra esta ingesta). Resumen cronológico descendente conocido a 2026-09-11:

- **2026-09**: Manual Procesamiento CCT actualizado (endpoints plan de pagos, avisos, cuentas de comisiones, consultas por ID); se agrega impuesto SIRTAC al Manual de Pagos con Transferencia PCT.
- **2026-08**: nueva funcionalidad **REVERSAL** (regularización excepcional de fondos por transacciones no deseadas).
- **2026-07**: se elimina la sección "Security" del manual PCT; mejoras a Archivo Parcial de Conciliación / Monitor de Garantías ("Archivo Parcial vs. On Hold — MPV1"); renombrado el manual de COELSA.PAY COBRANZA.INMEDIATA.
- **2026-06 / 2026-05**: mejoras a mensajería de avisos de CCT (más datos de préstamo, fecha de negocio); se incorpora consulta `GET api/v1/payment/{reverse_domain}/{qr_id_trx}`; se incorpora Manual PCT (info NFC) y Manual COELSA.PAY COBRANZA.INMEDIATA.
- **2026-04**: documentos funcionales nuevos — "Comercios CBU en PCT", "Cuenta Concentradora", "Propuesta NFC"; actualización del funcional de PAGO QR.
- **2026-02**: "Múltiple Endpoint con Subtipo"; actualización de Versionado de Mensajería.
- **2025-09 y anteriores**: incorporación progresiva de PAGO QR, CASHOUT (incl. variante cross-border), Diccionario COELSA.PAYMENTS, Prerequisitos, Múltiple Endpoint, Debin Programado, Scoring (nov. 2024), Monitor de Garantías (oct. 2024), API Saldos (may. 2024).

## Anexo — payloads reales

Ver [coelsa_debin_api_payloads.md](coelsa_debin_api_payloads.md) — request/response literales de la documentación (API Bancos, avisos/webhooks de Coelsa, API Comprador/Vendedor, y la secuencia completa de un DEBIN SPOT CBU→CVU paso a paso). Separado en archivo propio por umbral de fisión (este archivo + el anexo superaban ~300 líneas combinados).

## Confianza y gaps

- Confianza **alta**: contenido leído directamente de la documentación oficial vigente.
- **No verificado en esta ingesta**: si Bind ya usa o planea usar `REVERSAL` (nueva func. ago-2026) o el "Servicio Multiple Endpoint" — quedan como oportunidades a evaluar, no como gap (no hay contradicción con nada documentado, solo falta de decisión de producto).

---
*Creado: 2026-09-11 — `/context_merge`, desde ingesta manual de documentación pública de Coelsa (Pablo Gomes).*
