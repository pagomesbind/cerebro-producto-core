---
id: 2026-09-01_arquitectura_api_bank_errores
pm: pablo
fecha_captura: 2026-09-01
fuente: "Portal público de developers API BANK — https://sandbox.bind.com.ar/apidoc/#api-Errores"
producto: transversal
tema: API BANK (Banco Industrial) — Errores — catálogo completo de códigos
tipo: conocimiento
destino_propuesto: 3_recursos/arquitectura_sistema/api_bank/errores.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: d783db8
---

## Contexto

Grupo **Errores** de API BANK: no son endpoints operativos, sino documentación de referencia — el formato estándar de error y el catálogo completo de códigos usados por todas las APIs del banco (Cuenta, Billetera, Transferencia, TransferenciaMEP, Debin, Alta_De_Cuenta, Webhooks, Cheques, etc.). Es la referencia cruzada a consultar ante cualquier `code` recibido en un error 409/503/401 de cualquier otro grupo de esta API.

---

## 1. Errores controlados — `Formato`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Errores-Formato

Todos los errores controlados de la API retornan HTTP `409` o `503` con el siguiente formato de respuesta:

| Campo | Descripción |
|-------|-------------|
| `code` | Código de error (obligatorio). |
| `message` | Descripción del mensaje (obligatorio). |
| `moreInfo` | Link a una página web con información más detallada del problema (opcional). |
| `process` | Identificador del proceso, usado para seguimiento del error (obligatorio). |

### Ejemplos

```json
// HTTP 409 Conflict
{ "code": "GE500", "message": "Error genérico", "moreInfo": "http://unaurl/public-wiki/apibank/wikis/ge500", "process": "1234" }

// HTTP 503 Service Unavailable
{ "code": "GE503", "message": "En este momento el estado de las redes no permite ejecutar la transferencia", "moreInfo": "", "process": "1701" }
```

---

## 2. Códigos de error — `CodigosDeError`

> Fuente: https://sandbox.bind.com.ar/apidoc/#api-Errores-CodigosDeError

Listado de todos los posibles códigos de error de todas las APIs expuestas por API BANK. Cada error, en el portal, enlaza a una wiki con detalle y posible solución (URLs con placeholder `@@URL_PUBLIC_WIKI/<code>`, no resueltas en el JSON fuente).

### GE — Errores generales

| Código | Descripción |
|--------|-------------|
| `GE001` | MOCK_FILE_READ_ERROR (interno). |
| `GE002` | No implementado. |
| `GE003` | Campo requerido con valor nulo. |
| `GE004` | Estado civil inválido. |
| `GE005` | Género inválido. |
| `GE006` | Fecha inválida. |
| `GE007` | Fecha de nacimiento inválida. |
| `GE008` | Tipo de identificación inválido. |
| `GE009` | País inválido. |
| `GE010` | Tipo de archivo inválido. |
| `GE011` | Tipo de documentación inválida. |
| `GE012` | Provincia inválida. |
| `GE013` | Email inválido. |
| `GE014` | Archivo inválido. |
| `GE015` | El total informado debe ser mayor a cero. |
| `GE016` | El total informado no coincide con la cantidad de elementos enviados. |
| `GE017` | Tipo de dirección inválida. |
| `GE018` | URL inválida. |
| `GE019` | La URL informada en header(location) es inválida. |
| `GE020` | Número de lote inválido. |
| `GE021` | Tipo de contribuyente inválido. |
| `GE022` | Longitud inválida. |
| `GE023` | `origin_id` duplicado en el mismo lote. |
| `GE401` | Token inválido o el usuario no existe. |
| `GE403` | Error de permisos. |
| `GE500` | Error general. |
| `GE503` | (HTTP 503) Estado de las redes no permite ejecutar la operación. |
| `GE700` | Endpoint no habilitado. |
| `GE999` | Problema de conexión — consultar el resultado con el `origin_id` enviado o el servicio de consulta histórica. |

### PA — Errores de parámetros de URL / cuenta

| Código | Descripción |
|--------|-------------|
| `PA001` | Código de banco en URL inválido. |
| `PA002` | Código de vista en URL inválido. |
| `PA003` | Código de vista inválido para el usuario logueado. |
| `PA004` | CUIT inválido. |
| `PA005` | CBU inválido. |
| `PA006` | Alias de CBU/CVU inválido. |
| `PA007` | Tipo de transacción inválida. |
| `PA008` / `PA009` | CUIT existente. |
| `PA010` | Email existente. |
| `PA011` | Alias de CBU/CVU inexistente. |
| `PA012` | CVU inválido. |
| `PA013` | Error al crear CVU. |
| `PA015` | El campo titular no cumple con el formato requerido. |

### AC — Errores de cuenta

| Código | Descripción |
|--------|-------------|
| `AC001` | Persona inexistente. |
| `AC002` | Cuenta inválida. |
| `AC500` | Error general en la API de cuentas. |

### FI — Errores de filtros de listados

| Código | Descripción |
|--------|-------------|
| `FI001` | Valor del filtro `sort_by` inválido. |
| `FI002` | Valor del filtro `sort_direction` inválido. |
| `FI003` | Valor del filtro `limit` inválido. |
| `FI004` | Valor del filtro `offset` inválido. |
| `FI005` | Valor del filtro `from_date` inválido. |
| `FI006` | Valor del filtro `to_date` inválido. |
| `FI007` | `to_date` inferior a `from_date`. |

### CH — Errores de Cheques (grupo `Cheques`, fuera del alcance detallado de esta ronda)

`CH001`–`CH037`, `CH053`, `CH054`: validaciones de filtros de fecha (`obp_payment_from/to_date`, `obp_issued_from/to_date`, `obp_deposit_from/to_date`), de acción (`obp_mode`, `obp_status`, `action`), y de datos del cheque (cmc7, motivo, monto, librador, beneficiario, referencia). Catálogo extenso — ver `api_data.json` del portal para el detalle completo si se necesita documentar el grupo `Cheques` en profundidad.

### TX — Errores de transacciones (Transferencia / Billetera / Debin / TransferenciaMEP)

| Código | Descripción |
|--------|-------------|
| `TX001` | No se indicó la cuenta destino. |
| `TX002` | No se indicó el monto y moneda. |
| `TX003` | No se indicó el monto. |
| `TX004` | No se indicó la moneda. |
| `TX005` | Se debe indicar un beneficiario (por ID) o un CBU/CVU o un alias destino. |
| `TX006` | El beneficiario no existe. |
| `TX007` | Solo se puede indicar el beneficiario, o el CBU/CVU, o el alias — no varios a la vez. |
| `TX008` | El CBU/CVU no es correcto. |
| `TX009` | El alias de CBU/CVU no es correcto. |
| `TX010` | Debe indicar el concepto. |
| `TX011` | El monto debe ser numérico, mayor a cero, hasta 2 decimales. |
| `TX012` | La moneda indicada no es válida. |
| `TX013` | El concepto ingresado no es válido. |
| `TX014` | Debe indicar la expiración del DEBIN (máximo 4320 minutos). |
| `TX015` | La expiración ingresada no es válida (máximo 4320). |
| `TX016` | Se debe indicar un CBU/CVU destino o un alias. |
| `TX017` | Solo se puede indicar el CBU/CVU o el alias, no ambos. |
| `TX018` | DEBIN no encontrado. |
| `TX019` | Transferencia inexistente. |
| `TX020` | Estado de la transacción inválido. |
| `TX021` | Origen de la transacción inválido. |
| `TX022` | La cuenta destinataria no está habilitada para recibir DEBIN. |
| `TX023` | Se debe indicar la prestación. |
| `TX024` | Se debe indicar la referencia para la prestación. |
| `TX025` | Se debe indicar la descripción de la solicitud. |
| `TX026` | La prestación indicada no existe — verificar el nombre con el Banco. |
| `TX031` | Error al crear una suscripción de DEBIN. |
| `TX032` | Suscripción de DEBIN no encontrada. |
| `TX033` | El campo Id debe ser menor a 15 caracteres. |
| `TX034` | El campo Id ya fue utilizado. |
| `TX035` | La descripción supera el tamaño máximo permitido (100 caracteres). |
| `TX036` | Debe indicar la cuenta billetera virtual origen (CVU o alias de CVU). |
| `TX037` | El alias de CVU de la cuenta origen no es válido. |
| `TX038` | El CVU de la cuenta origen no es un CVU válido. |
| `TX039` | Solo se puede indicar el CVU o el alias de CVU de la cuenta origen, no ambos. |
| `TX040` | La moneda indicada no es válida — esta operación solo acepta ARS. |
| `TX041` | La moneda de las cuentas origen y destino deben ser la misma. |
| `TX042` | El CBU/CVU o alias indicado se encuentra inhabilitado. |
| `TX043` / `TX044` | El CUIT de la cuenta origen no es válido. |
| `TX045` | El valor de `currency` no se corresponde con la moneda de la cuenta. |
| `TX046` | El monto a transferir excede el límite diario disponible para la cuenta origen. |
| `TX080` | Servicio actualmente no disponible para operar. |
| `TX081` | Error de datos de la operación. |
| `TX082` | Error de cuenta virtual del vendedor. |
| `TX083` | Banco vendedor no habilitado para transacciones. |
| `TX084` | Sin garantía. |
| `TX085` | Titular mal formulado. |
| `TX086` | Debe indicar el código de operatoria MEP. |
| `TX087` | `origin_id` requerido. |
| `TX088` | CBU destino requerido. |
| `TX089` | CUIT destino requerido. |
| `TX090` | Error interno al consultar el backend que resuelve la transferencia. |
| `TX500` | Error genérico de transferencia (mensaje variable). |

### DD — Errores de débitos directos por lote (funcionalidad no cubierta en el resto de los grupos relevados — sugiere un endpoint de "débitos directos en lote" no incluido entre los 87 endpoints tabulados; posible sección adicional no indexada o en otro proyecto de apidoc)

| Código | Descripción |
|--------|-------------|
| `DD001` | El importe debe ser numérico, mayor a cero, hasta 2 decimales. |
| `DD002` | Importe totalizado inválido para importes de primer vencimiento. |
| `DD003` | La cantidad máxima de débitos directos a enviar por lote es de 1000. |
| `DD004` | La fecha del primer vencimiento debe ser ≥ 2 días respecto a la fecha de operación. |
| `DD005` | La fecha del segundo vencimiento debe ser superior a la del primer vencimiento. |
| `DD006` | La fecha del tercer vencimiento debe ser superior a la del segundo vencimiento. |
| `DD007` | La fecha original del débito debe ser menor a la del primer vencimiento. |
| `DD008` | La fecha no puede ser fin de semana o feriado. |
| `DD009` | El débito no puede editarse. |

### EP — Errores de webhooks (endpoints)

| Código | Descripción |
|--------|-------------|
| `EP001` | El valor de `url` no puede estar vacío. |
| `EP002` | El valor de `url` debe ser una URL válida. |
| `EP003` | El valor de `description` no puede estar vacío. |
| `EP004` | El valor de `enabled` no puede estar vacío. |
| `EP005` | El valor de `code` no puede estar vacío. |
| `EP006` | El valor de `events` no puede estar vacío. |
| `EP007` | La lista de `events` debe tener eventos válidos. |
| `EP008` | Endpoint no encontrado. |

### IN — Errores de inversiones (funcionalidad no cubierta en los grupos relevados — sugiere endpoints de fondos comunes de inversión/cuotapartes no incluidos entre los 87 tabulados)

| Código | Descripción |
|--------|-------------|
| `IN001` | Legajo existente. |
| `IN002` | Legajo inválido. |
| `IN003` | Cuenta no habilitada. |
| `IN004` | Cuenta existente. |
| `IN005` | Cuenta inválida. |
| `IN006` | Tipo de cuenta inválido. |
| `IN007` | Tipo de identificación tributaria inválido. |
| `IN008` | El importe debe ser numérico, mayor a cero, hasta 2 decimales. |
| `IN009` | La cantidad debe ser numérica, mayor a cero, hasta 13 decimales. |
| `IN010` | Solo se debe informar el importe o la cantidad de cuotapartes. |
| `IN011` | La operación es inválida. |
| `IN012` | Fondo de inversión inválido. |
| `IN013` | Importe totalizado inválido. |
| `IN014` | Cantidad de cuotapartes totalizada inválida. |
| `IN015` | Error al crear la cuenta de inversión. |
| `IN016` | Tipo de relación del operador inválida. |
| `IN017` | Tipo de sociedad inválida. |
| `IN018` | Error al agregar un operador. |
| `IN020` | Error al eliminar un operador. |

### VW — Errores de Billetera virtual (CVU)

Ver detalle funcional completo en `2026-09-01_arquitectura_api_bank_billetera`. Códigos: `VW001`–`VW016` (id de cliente inválido, PSP sin código, cuenta recaudadora errónea, CVU ya existente, CVU no pertenece a la billetera, CVU inexistente, alias en uso, no se pudo asignar alias, CUIT erróneo para CVU, alias ya asignado, alias modificado hace menos de 24hs, id de cliente asociado a otro CUIT, no se pudo crear/eliminar el CVU, combinación CVU/CUIT/billetera no encontrada, no se pudo consultar la cuenta recaudadora).

---

## Nota de relevamiento

Grupo completo (2/2 endpoints — en realidad páginas de referencia, no endpoints operativos) relevado desde `https://sandbox.bind.com.ar/apidoc/api_data.json`. Este catálogo es transversal a **todos** los grupos de API BANK, incluidos los no cubiertos en esta ronda (`Cheques`, `Persona`, `Referencias`). Los prefijos `CH` (Cheques) e `IN` (Inversiones/fondos) apuntan a funcionalidad más amplia que la tabulada en los 87 endpoints del índice del portal — posible indicio de que existen endpoints de cheques/inversiones documentados en otra sección del portal no visible desde el índice principal, o que esos códigos son legado de otra versión de la API. Marcado como punto a confirmar si se profundiza en esos grupos.
