# Conciliación y totalizadores — Wallet

> Estado: en producción.

Generación de archivos de movimientos/saldos, conciliación de transferencias entrantes directo a Coelsa por CVU, consulta de totalizadores de cuentas CBU/CVU por CUIT (normativa BCRA vía Coelsa), y endpoint dedicado de conciliación en línea (Epic histórica "Endpoint Wallet: Consulta enfocada en conciliar").

---

## 0. Endpoint dedicado de consulta para conciliación en línea (Astropay)

> Fuente: Notion histórico, Epic **"Endpoint Wallet: Consulta enfocada en conciliar"**. Pedido explícito de **Astropay** (cliente de mayor volumen, mismo cliente detrás de la contingencia Coelsa de [debin_y_fondeo.md §7](debin_y_fondeo.md#7-consulta-debin-coelsa-directo--contingencia-definida-no-confirmado-si-se-construyó)): necesitaba conciliar operaciones **en línea, aproximadamente cada hora**, durante todo el día — el endpoint genérico de movimientos no estaba optimizado para ese patrón de uso intensivo.

- **Endpoint nuevo**, acotado a devolver solo los campos necesarios para conciliar (no el detalle completo de movimientos): `idOperacion`, `idExterno` de la organización, `idTipoOperacion`, cuenta, `Coelsa_ID`, id de transacción del banco, CBU/CVU contraparte, fechas de creación/actualización, `idEstado`, importe.
- Filtros: fecha y hora desde/hasta, `idEstado`, `idTipoOperacion`; ordenamiento asc/desc por id de operación.
- **Paginado**: el endpoint genérico de movimientos tenía tope de 100 por página; para este caso se buscó soportar hasta 500 por página, dado el volumen de Astropay.
- Se corrigió en el camino un bug relacionado: el endpoint general de movimientos **filtraba mal por `OperacionTipoId`** y no incluía el tipo de operación 7 por defecto — ambos corregidos como parte de esta Epic.

---

## 1. Generar archivos MOVIMIENTOS Y SALDOS en STG

### Generación de archivos — Saldos y Movimientos

Ingresar al Swagger: `http://10.210.1.28/swagger/index.html` y ejecutar el endpoint correspondiente. La generación debe realizarse **día por día**.

El último día que se generó fue el **22/10**; a partir de ahí hay que continuar de forma secuencial.

> 📌 Importante:
> - Si se necesitan archivos de **Saldos**, es necesario estar al día con los saldos históricos, ya que se generan de manera acumulativa y requieren que existan los días previos.
> - Si fuera solo **Movimientos**, no habría inconveniente en generarlos directamente.

### Validación de generación

```sql
select top100 *
from saldoshistoricos
order by id desc
```

Deberían visualizarse los registros generados correctamente.

### Generación de reportes

Acceder a `http://10.210.1.74/swagger/index.html` y ejecutar el endpoint correspondiente a **Reportes**.

⚠️ A tener en cuenta con la fecha: el endpoint debe ejecutarse con la **fecha del día posterior** al que se necesita el archivo. Por ejemplo, para los archivos del martes 6, ejecutar el proceso con fecha 7.

---

## 2. Configurar totalizadores Coelsa (para organización de Wallet)

**Objetivo:** dejar configurada una organización de wallet para que consuma la funcionalidad de Coelsa de Totalizadores de cuentas CBU/CVU.

### Contexto

Esta funcionalidad de Coelsa es nueva y tiene la particularidad de que el BCRA obliga por normativa a que todos los PSP la consuman para algo. Es posible que organizaciones de wallet que usen su propia PSP se vean especialmente interesadas y la pidan con más prioridad.

No se indica explícitamente cómo usarla, pero se entiende que los PSP deben considerar no abrirle cuentas a personas que tengan muchas CBU/CVU, para evitar fraude.

### Precondiciones

- Si PSP = 184: tener la organización creada (ver `organizaciones_y_configuracion.md`).
- Si PSP ≠ 184: tener la organización creada, y contar con las credenciales de Coelsa brindadas por el banco para usar la funcionalidad de totalizadores con ese PSP.

### Configuraciones

- Si PSP = 184: no hace falta configurar nada especial, ya que el sistema tiene configuradas las credenciales de Coelsa con las que Bind PSP consume los endpoints de totalizadores. Cualquier organización con PSP 184 puede usar esta funcionalidad sin problemas.
- Si PSP ≠ 184:
  - [ ] Enviar a FINTEXA (`security@fintexa.tech`) las credenciales de Coelsa totalizadores, indicando para qué son y que son para un nuevo PSP = "X".
  - [ ] Crear un ticket de nueva solicitud a FINTEXA > Emisión para que creen en AuthExternal los registros necesarios para asociar las nuevas credenciales de Coelsa al nuevo PSP.

### Validaciones

- [ ] En la BD `SharedAuthExternalService`, tabla `dbo.ServiceAuthentication`, validar que existe un registro con `Aplicacion = "APITOTALIZADORCUENTACBU"` para el `OWNER = {{nombre del PSP}}`. Ejemplo: para PSP=184 se verifica el registro correspondiente.

---

## 3. Introducción — Consulta totalizadores Coelsa CBU/CVU (capacitación interna)

### ¿Qué es?

Nueva funcionalidad de Coelsa que permite consultar todas las cuentas activas asociadas a un CUIT (CBU o CVU). Ofrece un endpoint para consulta online, y también emite esta información diariamente en batch, disponibilizada por SFTP a cada PSP.

### ¿Por qué es importante?

- Es una funcionalidad normativa: el BCRA obliga a todos los PSP a usar este servicio y a demostrar que lo consumen, para poder aplicar reglas antifraude.
- Fomenta el cash in en las cuentas por su simplicidad de uso.
- La funcionalidad actual equivalente (DEBIN recurrente) está limitada a CBU; transferencia pull permite CBU o CVU.

### ¿Qué está alcanzado en este proyecto?

- Endpoint para consultar cantidad de CBU y/o CVU para un CUIT.
- Configurable para PSPs que no sean Bind PSP.

### ¿Qué no está alcanzado?

- No hay herramientas en Ardid para monitorear esta operatoria (fraude/desarbitraje de fondos).
- No integrada aún en la app marca blanca de wallet ni en el portal comercio.
- No hay esquemas automáticos para tratar contracargos (desconocimientos) de transferencia pull.

### Consideraciones importantes

- El BCRA sólo obliga a usar esta funcionalidad, pero no norma el cómo usarla (por ahora).

### Requisitos para usarlo

- PSP = 184: no se necesita nada, ya tiene configuradas las credenciales de APIDEBIN Coelsa de Bind PSP.
- PSP ≠ 184: deben gestionarse con el Banco Industrial las credenciales de Coelsa de API DEBIN para ese PSP específico, y solicitar a Fintexa que las configure en el sistema.

*(Nota: los ejemplos de request/webhook de esta fuente de capacitación replican los de transferencia pull; ver `otros_manuales.md` si se agrega ese contenido, o la documentación de API pública para el detalle funcional de transferencia pull.)*

### 3.1 Origen normativo preciso, multi-PSP y cluster de bugs (Jira PRD-56, Finalizada)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA **PRD-56** "Consulta totalizadores CBU/CVU Coelsa - APIs" → Epic **WS-57** "CONSULTA POR CUENTA" (8 tickets: 5 con desarrollo real, 3 "No aplica" — WS-92/93 quedaron unificados en WS-58, WS-589 fue un duplicado de WS-590). Precisa y confirma con más detalle la introducción normativa ya documentada en §3.

- **Norma exacta**: **COM A 8298 del BCRA**, que exige totalizadores de CBU/CVU por persona (CUIT/CUIL), provistos por la **CEC-BV**, para detectar y frenar fraude en el esquema de pagos minoristas (apertura masiva/injustificada de cuentas, uso de cuentas "mulas", evasión de controles de debida diligencia vía altas/bajas recurrentes).
- **Compromisos de fecha reales con el BCRA** (registrados en comentarios de la IDEA por Producto): consulta por cuenta comprometida para el **30/11**; consulta masiva (archivo batch) para el **23/12**. En la práctica, el archivo batch se pudo descargar del banco sponsor por SFTP y pasó a producción el **23/12/2025**; el consumo por APIs pasó a producción recién el **28/02/2026** — es decir, la fecha real de API quedó ~2 meses después del compromiso original.
- **Multi-PSP confirmado con clientes reales**: además de Bind PSP (PSP 184), se gestionaron credenciales de Coelsa para **Cencosud, Max Pay y ArgPagos (Global66)** — cada uno con su propio ticket de solicitud de credenciales en el Jira de Soporte (`bindtm`). `WS-596` fue el desarrollo específico para poder configurar por Setting estos PSPs adicionales dentro del microservicio `TotalizadoresCoelsa` (antes solo soportaba el owner "BIND").
- **Alcance explícito de la Primera Etapa** (lo que cubre este documento): homologación directa con las credenciales del banco a los 3 servicios de Coelsa (`GET /api/totalCBU/{cuit}`, `GET /api/totalCVU/{cuit}`, `GET /api/totalizador/{cuit}`) + archivo batch. **Fuera de alcance de esta etapa** (Segunda Etapa, no confirmado si se construyó): ingesta diaria de estos datos a una base propia, y alimentar con ellos nuevas reglas de monitoreo en ARDID.
- **Cluster de bugs — mismo patrón camelCase/PascalCase encontrado 2 veces por separado**: los query params del endpoint (`Cuit`, `FormaConsulta`) se entregaron en PascalCase en vez de camelCase — reportado una vez sobre el endpoint específico de Wallet (`WS-590`) y una segunda vez de forma independiente sobre el mismo problema (`WS-589`, cerrado como duplicado). Mismo tipo de inconsistencia de formato que ya aparece en otros endpoints nuevos de esta wiki (ver `crypto.md §1.3`).
- **Story Points reales por ticket** (campo `customfield_10041` a nivel de Historia/Error, distinto del SP a nivel de IDEA): `WS-58` (endpoint unificado CBU+CVU) = 7 SP, `WS-59` (wrapper de homologación multi-PSP) = 7 SP, `WS-275` (configuración AuthExternal/Egress contra Coelsa) = 3 SP, `WS-596` (config. de PSPs adicionales) = 3 SP, `WS-590` (bug camelCase) = 0,25 SP — total ~20,25 SP de desarrollo real (excluyendo los 3 tickets "No aplica"/duplicados).

---

## 4. Documentación — Consulta totalizadores CBU/CVU (documentación para clientes / API)

**Alcance:** informativo y apto para desarrollo. Aplica sólo al producto Wallet Services.

**Objetivo:** instruir al desarrollador de la Entidad que quiere integrarse a la solución de Bind PSP para utilizar la funcionalidad dispuesta por Coelsa que devuelve la cantidad total de CBU o CVU activos de una persona física.

### Consultar totalizadores cuentas por CUIT

Utiliza la funcionalidad de Totalizadores de Coelsa para devolver cuántas cuentas activas en Argentina tiene una persona. Coelsa ofrece 3 modalidades (solo CBU, solo CVU, o ambos); el endpoint permite elegir la modalidad desde un parámetro.

> 📌 El consumo de este servicio en Coelsa debe realizarse con las credenciales correspondientes de cada PSP. Debe configurarse en el sistema según corresponda.

#### Endpoint

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/GetTotalizadoresCoelsa?cuit=&formaConsulta=` |
| PRODUCCIÓN | GET | `https://api.bindpagos.com.ar/walletentidad-cuenta/v1/api/v1.201/GetTotalizadoresCoelsa?cuit=&formaConsulta=` |

#### Request — query params

| Atributo | Tipo | REQ/OPC | Descripción |
|---|---|---|---|
| `cuit` | string | REQUERIDO | CUIT a consultar. |
| `formaConsulta` | string | REQUERIDO | `cbu` (solo cantidad de CBU) / `cvu` (solo cantidad de CVU) / `cbucvu` (ambos). |

Ejemplo de request:

```bash
curl -v -X GET "https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/GetTotalizadoresCoelsa?cuit=2037431275&formaConsulta=cbucvu" -H "Cache-Control: no-cache" -H "Authorization: Bearer {{access_token}}"
```

#### Response

| Atributo | Tipo | Descripción |
|---|---|---|
| `cuit` | string | CUIT consultado. |
| `cantidadTotalCVU` | string | Cantidad total de CVU activos con esta titularidad. `0` si no tiene CVUs asociados. |
| `cantidadTotalCBU` | string | Cantidad total de CBU activos con esta titularidad. `0` si no tiene CBUs asociados. |

Ejemplo — HTTP 200:

```json
{
  "cuit": "20374312759",
  "cantidadTotalCVU": "0",
  "cantidadTotalCBU": "2"
}
```

Ejemplo — HTTP 422 (error de negocio):

```json
{
  "eventId": "string",
  "detalle": "string",
  "correlationId": "string",
  "errores": [
    {
      "codigo": "string",
      "titulo": "string",
      "detalle": "string"
    }
  ]
}
```

| `errores.codigo` | `errores.titulo` | Descripción |
|---|---|---|
| `BadRequest` | Error en consulta a Coelsa | Error externo en Coelsa; el detalle indica el error exacto que respondió Coelsa. |
| `400` | — | Error en algún valor enviado en el request. |
| `11000` | Organización no encontrada. | Error en la organización con la que se está autenticando para consumir este endpoint. |

HTTP 500 — Error desconocido: mismo formato de body que el 422.

### 4.1 El endpoint también se expone en el BFF de Onboarding (W 71)

> Fuente: Jira bindpsp.atlassian.net, versión W 71 (publicada 2026-07-15), ticket [WS-1277](https://bindpsp.atlassian.net/browse/WS-1277).

El endpoint `GET /walletentidad-cuenta/v1/api/v1.201/GetTotalizadoresCoelsa?cuit={cuit}&formaConsulta={formaConsulta}` documentado arriba ahora también se expone en el **BFF que consume el onboarding**, autenticando con el header `x-entidad` = Id de organización — permite que el flujo de onboarding consulte totalizadores sin pasar por el BFF de Wallet estándar.

### 4.2 Límite de 30 iteraciones en producción y exclusión de CUITs (V72)

> Fuente: reunión de PRE-Despliegue de Emisión V72 (2026-08-18, 14:30), minuta Gemini.

Dentro de "Configuraciones Técnicas y Endpoints" del despliegue V72 (desplegado 2026-08-19 06:30-07:30), se definió: la validación de Totalizadores (CBU, CVU larga y CVU corta) se habilita en producción con un **límite estricto de 30 iteraciones**. En la misma sección se registró una decisión relacionada: se descartó incorporar CUITs a la lista blanca (whitelist) de esta validación — la regla aplica exclusivamente a personas físicas, no a personas jurídicas.

---

## 5. Documentación — Conciliar transferencias entrantes directo a Coelsa por CVU

> **Origen (Jira):** IDEA `bindpsp.atlassian.net` **PRD-105** "ASTROPAY: Consulta directa a Coelsa por un solo id Coelsa o cvu" (Finalizada) → Epic **WS-271** → historias WS-272 (fallback a Coelsa cuando no se encuentra por `coelsaId`) y WS-273 (conciliar por `cvuDestino`, documentado abajo). Mismo cliente y motivación que la contingencia de [debin_y_fondeo.md §7](debin_y_fondeo.md#7-consulta-debin-coelsa-directo--contingencia-para-astropay-confirmado-construido-ver-jira-prd-45): Astropay tenía alto % de fallas conciliando solo por `coelsaId` porque no siempre lo tenía a mano; se agregó la alternativa por CVU destino.

**Alcance:** informativo y apto para desarrollo. Aplica sólo al producto Wallet Services.

**Objetivo:** dar al desarrollador de la Entidad una herramienta para dar frente a reclamos de clientes puntuales por falta de transferencias entrantes.

### Crear proceso de conciliación con Coelsa por CVU

Crea un proceso de conciliación de transferencias entrantes en estado pendiente.

> 📌 Enviar un CVU destino específico hace la consulta a Coelsa y la conciliación mucho más performante.
> 📌 Indicando un valor en CVU destino se admite un plazo de conciliación de hasta 24 horas.
> 📌 Si se indica CVU destino y las fechas de inicio/fin vacías, por defecto concilia transferencias del día de hoy.

#### Endpoint

| Ambiente | Método | URL |
|---|---|---|
| STAGING | POST | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operaciones/ConciliacionCoelsa` |
| PRODUCCIÓN | POST | `https://api.bindpagos.com.ar/walletentidad-operaciones/v1/api/v1.201/Operaciones/ConciliacionCoelsa` |

#### Request body

| Atributo | Tipo | REQ/OPC | Descripción |
|---|---|---|---|
| `fechaHoraDesde` | datetime | OPCIONAL | Fecha/hora de comienzo del rango. Puede ser `null` si se indica CVU destino. |
| `fechaHoraHasta` | datetime | OPCIONAL | Fecha/hora de fin del rango. Puede ser `null` si se indica CVU destino. |
| `tipoOperacionId` | int | REQUERIDO | Único valor permitido: `2` = Transferencias entrante. |
| `cvuDestino` | string | OPCIONAL | CVU de la cuenta de la organización donde tuvo que haber llegado la transferencia. |

Ejemplo de request:

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/Operaciones/ConciliacionCoelsa' \
--header 'Content-Type: application/json-patch+json' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}' \
--data '{
    "fechaHoraDesde": null,
    "fechaHoraHasta": null,
    "tipoOperacionId": 2,
    "cvuDestino": "0000532609180006487586"
}'
```

#### Response

| Atributo | Tipo | Descripción |
|---|---|---|
| `procesoId` | int | Identificador del proceso creado. |
| `fechaHoradesde` | datetime | Fecha/hora de comienzo del rango. |
| `fechaHoraHasta` | datetime | Fecha/hora de fin del rango. |
| `operacionTipoId` | string | `2` = Transferencias entrante. |
| `estado` | string | `PENDIENTE`, `EN_PROCESO` (consulta a Coelsa, compara con operaciones existentes, inserta diferencias), `FINALIZADO` (completó, no más cambios), `ERROR` (hubo error, ya no se completará). |

Ejemplo — HTTP 200:

```json
{
    "procesoId": 13,
    "fechaHoraDesde": "2025-11-20T13:00:00",
    "fechaHoraHasta": "2025-11-20T16:00:00",
    "tipoOperacionId": 2,
    "estado": "PENDIENTE"
}
```

### Consultar proceso de conciliación

Consulta el estado y resultados de un proceso de conciliación previamente creado.

#### Endpoint

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/MovimientosConciliadosCoelsa?procesoId=` |
| PRODUCCIÓN | GET | `https://api.bindpagos.com.ar/walletentidad-operaciones/v1/api/v1.201/MovimientosConciliadosCoelsa?procesoId=` |

#### Request query param

| Atributo | Tipo | REQ/OPC | Descripción |
|---|---|---|---|
| `procesoId` | int | REQUERIDO | Identificador del proceso. |

Ejemplo:

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-operaciones/v1/api/v1.201/MovimientosConciliadosCoelsa?procesoId=13' \
--header 'Cache-Control: no-cache' \
--header 'Authorization: Bearer {{access_token}}'
```

#### Response

| Atributo | Tipo | Descripción |
|---|---|---|
| `procesoId` | int | Identificador del proceso. |
| `fechaHoradesde` | datetime | Fecha/hora de comienzo. |
| `fechaHoraHasta` | int | Fecha/hora de fin. |
| `operacionTipoId` | string | `2` = Transferencias entrante. |
| `estado` | string | `PENDIENTE` / `EN_PROCESO` / `FINALIZADO` / `ERROR`. |
| `opEncontradas` | int | Cantidad de operaciones encontradas en Coelsa. Puede cambiar mientras `EN_PROCESO`. |
| `opDiferencias` | int | Cantidad de operaciones encontradas en Coelsa pero no en nuestro sistema (se intentarán conciliar). |
| `diferencias` | array of objects | Un objeto por cada diferencia encontrada. |
| `diferencias[{}].cvu` | string | CVU de destino de la transferencia con diferencia. |
| `diferencias[{}].coelsaId` | string | Identificador de Coelsa de la transferencia con diferencia. |
| `opConciliadas` | int | Cantidad de operaciones ya conciliadas. |
| `conciliadas` | array of objects | Un objeto por cada transferencia conciliada. |
| `conciliadas[{}].cvu` | string | CVU de destino de la transferencia conciliada. |
| `conciliadas[{}].coelsaId` | string | Identificador de Coelsa de la transferencia conciliada. |

Ejemplo de response:

```json
{
    "procesoId": 13,
    "fechaHoraDesde": "2025-11-20T13:00:00",
    "fechaHoraHasta": "2025-11-20T16:00:00",
    "operacionTipoId": 2,
    "estado": "FINALIZADO",
    "opEncontradas": 4,
    "opDiferencias": 4,
    "diferencias": [
        { "cvu": "0000532609180006487586", "coelsaId": "WZ0KV87941GG4K49PEYDX4" },
        { "cvu": "0000532609180006487586", "coelsaId": "0WGRXJE27ZEE4GL97MYQL3" },
        { "cvu": "0000532609180006487586", "coelsaId": "YZ6OLMDN31MM53Y9E7RQ5X" },
        { "cvu": "0000532609180006487586", "coelsaId": "8PDX4OGNY7RR6RY20L6EY5" }
    ],
    "opConciliadas": 4,
    "conciliadas": [
        { "cvu": "0000532609180006487586", "coelsaId": "WZ0KV87941GG4K49PEYDX4" },
        { "cvu": "0000532609180006487586", "coelsaId": "0WGRXJE27ZEE4GL97MYQL3" },
        { "cvu": "0000532609180006487586", "coelsaId": "YZ6OLMDN31MM53Y9E7RQ5X" },
        { "cvu": "0000532609180006487586", "coelsaId": "8PDX4OGNY7RR6RY20L6EY5" }
    ]
}
```

### Anexo: análisis de casos de uso

| CASO | `estado` | `opEncontradas` | `opDiferencias` | `diferencias` | `opConciliadas` | `conciliadas` |
|---|---|---|---|---|---|---|
| Proceso finalizó OK. Encontró en Coelsa transferencias entrantes para esa cuenta en ese plazo y alguna/s no están en nuestro sistema → concilió las diferencias. | "FINALIZADO" | ≠ null | ≠ null | ≠ null | ≠ null | ≠ null |
| Proceso finalizó OK. Encontró transferencias en Coelsa pero también están todas en nuestro sistema → no concilió nada. | "FINALIZADO" | ≠ null | = null | null | null | null |
| Proceso finalizó OK. No encontró en Coelsa ninguna transferencia entrante para esa cuenta en ese plazo → no conciliará nada. | "FINALIZADO" (\*1) | = 0 (\*2) | = null | = null | = null | = null |
| Proceso finalizó con algún error. Debe reintentarse. | "ERROR" | = null | = null | = null | = null | = null |

(\*1) y (\*2): ✅ **Confirmado publicado en producción en W 68 (2026-03-11)** vía ticket [WS-509](https://bindpsp.atlassian.net/browse/WS-509) — el caso "sin movimientos" ya no responde `ERROR` sino `FINALIZADO` con `opEncontradas = 0` (bug reportado por Astropay en producción).

### Origen de la consulta directa a Coelsa (W 65.1 → W 66.1, nov-dic 2025) — atribución de releases

> La funcionalidad documentada en §5 (construida para Astropay, IDEA PRD-45) se publicó así: **W 65.1** (2025-11-26) trajo los 3 tickets fundacionales — el endpoint de consulta de movimientos directo a Coelsa vía DEBIN Lista ([WS-15](https://bindpsp.atlassian.net/browse/WS-15)), la consulta de operación por `redId` ([WS-17](https://bindpsp.atlassian.net/browse/WS-17)) y la **conciliación en línea** de faltantes ([WS-18](https://bindpsp.atlassian.net/browse/WS-18), 15 SP; su "parte 2" [WS-104](https://bindpsp.atlassian.net/browse/WS-104) se publicó en la misma versión ⚠️ en estado "En curso"). **W 66** sumó los tipos **CASHOUT** a la conciliación ([WS-195](https://bindpsp.atlassian.net/browse/WS-195)) y mejoras por **duplicación de eventos** detectada en una prueba productiva con Astropay ([WS-196](https://bindpsp.atlassian.net/browse/WS-196)). **W 66.1** integró la consulta Coelsa al endpoint `/ConciliarTransferencia` como fallback cuando Api Bank no tiene la operación — solo si la organización tiene la especificación ([WS-272](https://bindpsp.atlassian.net/browse/WS-272)) — y corrigió que la contraparte se insertara con los datos de la empresa que respalda la transferencia en vez del originante real ([WS-300](https://bindpsp.atlassian.net/browse/WS-300)).

### Gobierno del endpoint de consulta directa a Coelsa (W 67, 2026-01-27)

> Fuente: Jira bindpsp.atlassian.net, versión W 67, tickets WS-16, WS-19, WS-377 (Epic de conciliación directa, IDEA finalizada).

- **Habilitación por organización** ([WS-16](https://bindpsp.atlassian.net/browse/WS-16)): el endpoint de consulta directa a Coelsa se habilita organización por organización — por defecto ninguna puede usarlo. Se resolvió **a nivel infraestructura** (no por especificación de BD): se pidió a Infra habilitarlo solo para Astropay.
- **Conteo de pegadas para facturación** ([WS-19](https://bindpsp.atlassian.net/browse/WS-19), 7 SP): cada invocación se cuenta por organización vía header `x-internalclienteId` (= APLICACION+IdOrganización, ej. `WALLET14`) enviado desde los MS Operaciones/DispatcherCoelsaBind/StateMonitor hacia SharedDebin — el consumo de este endpoint **se factura aparte** (no entra en el esquema normal de pegadas a Api Bank) y se guarda al menos 3 meses. Nota: en enero 2026 el PM lo bajó de prioridad ("si queda tiempo, se prueba").
- **Validación de dirección de la transferencia** ([WS-377](https://bindpsp.atlassian.net/browse/WS-377)): Astropay enviaba CoelsaIds de transferencias **salientes** al endpoint de conciliación de entrantes — el sistema procesaba igual y fallaba con un 500 críptico. Desde W 67 responde el error de negocio explícito `4072 "La transferencia no es entrante"` sin ir a Coelsa.

### Ajustes del endpoint `/ConciliacionCoelsa` publicados en W 68 (2026-03-11)

> Fuente: Jira bindpsp.atlassian.net, versión W 68, tickets WS-412, WS-413, WS-448, WS-509 (Epic WS-3, IDEA de conciliación directa Coelsa ya finalizada).

- **Validación de pertenencia del CVU** ([WS-412](https://bindpsp.atlassian.net/browse/WS-412)): si se envía `cvuDestino`, se valida que el CVU pertenezca a la organización del token — si no pertenece, responde `422` "El CVU indicado no pertenece a la Organización". Antes se podía correr conciliación sobre CVUs ajenos.
- **Fechas opcionales con CVU** ([WS-413](https://bindpsp.atlassian.net/browse/WS-413)): si se envía `cvuDestino` sin `fechaHoraDesde`/`fechaHoraHasta`, se interpreta el día corriente completo; si se envían, la amplitud máxima del rango es **24 hs**. También se eliminó la validación de "proceso activo en el rango" para consultas por CVU.
- **Timezone del default** ([WS-448](https://bindpsp.atlassian.net/browse/WS-448)): el `fechaHoraDesde` por defecto arrancaba en `00:00Z` (21:00 del día anterior en Argentina) — corregido a `03:00Z` para abarcar desde las 00:00 UTC-3.

> Documentación de referencia adicional: PDF "BindPSP - Consulta de operaciones directo a Coelsa" adjunto en la fuente Notion original.

### Habilitación del proceso de conciliación para organizaciones más allá de Astropay (2026-07-13)

> Fuente: Reunión "Reunión del 13 jul 2026 a las 14:47 GMT-03:00" (2026-07-13), minuta Gemini.

- **Antes de esta sesión, solo la organización Astro tenía habilitado** el proceso de conciliación de transferencias entrantes por CVU (§5). Nicolás Colón detectó que **Credicuotas (ID 16)** y **BSF (ID 24)** no lo tenían habilitado, y lo habilitó para ambas durante la reunión mediante el alta de una **especificación** (`scope: operaciones`, `tabla: organizaciones`, clave = ID de organización, valor `true`).
- **⚠️ Posible contradicción con §"Gobierno del endpoint..." (WS-16):** esa sección documenta que la habilitación por organización se resolvió **a nivel infraestructura** ("no por especificación de BD"), pidiendo a Infra habilitarlo solo para Astropay. Esta sesión habilita Credicuotas/BSF **vía especificación de BD**, no vía Infra — no está claro si el mecanismo cambió después de WS-16, si conviven ambos, o si la habilitación de Astro por Infra fue un caso puntual y el mecanismo real siempre fue por especificación. Sin resolver — ver `../../../2_areas/gaps_y_preguntas.md`.
- **Prueba realizada:** proceso de conciliación para BSF sobre rangos horarios progresivos (13-14hs → 16-17hs → 10-13hs), funcionando correctamente — encontró y concilió diferencias reales entre Coelsa y los registros internos.
- **Hallazgo de negocio:** BSF venía reclamando "falta de transferencias entrantes" — el equipo confirmó que **no había pérdida real**, sino una baja de volumen esperable por franja horaria (el proceso de conciliación no había estado habilitado antes para poder demostrarlo con datos).
- **Pendiente (acción de Nicolás Colón, sin fecha):** redactar un manual/guía del proceso de conciliación por organización (endpoints, especificaciones, tablas involucradas — `Conciliation processes`, `Conciliation process events`, `Conciliation process details`), con referencia directa a Swagger. No hay Jira asociado a esta sesión (no es tema de un PRD vivo).

### Mapeo de campos `reference`/`external_id` para conciliación de Wallet QR (2026-08-06)

> Fusionado desde `detalle_productos/wallet/otros_manuales.md §14` en la reestructuración PARA en cascada (2026-08-12). Fuente: Reunión "Análisis COBRO" (2026-08-06), minuta Gemini. Sesión de sync semanal Cobro con Fintexa (Daniela Collia, Melisa Belpassi, Flavia Salmerón, Marcos Sánchez, Cristian Medina, Julieta Giménez).

- **Requerimiento de Administración (ticket 1495):** hoy los campos `reference` y `external_id` de los comprobantes de Wallet QR se pueblan con el identificador de transacción interno. Administración pide mapear `reference`→"referencias pago" y `external_id`→"ID Coelsa" para poder conciliar contra el extracto bancario. **Pendiente de validar con Mariano y Euge** si algún proceso crítico de conciliación depende del valor actual (se perdería la referencia al ID de transacción) antes de tocarlo — ver [2_areas/tareas.md](../../../2_areas/tareas.md) T-091. Reclasificado de mejora a **bugfix** y priorizado para la próxima versión.
- **Falso positivo de un análisis de IA sobre contracargos:** una consulta a una IA externa había señalado que los contracargos ("desconocimientos") tardarían "más de 3 días en aprobarse". El equipo confirmó que técnicamente se procesan y aprueban sin estados intermedios — **no corresponde a un caso de negocio real**, se descarta el ajuste. Precedente documentado: la síntesis automática de una IA sobre un dataset puede llevar a una falsa alarma si no se contrasta con el comportamiento real del sistema.
- **Cache para `GET comisiones` (ticket 1444):** aprobado para la próxima versión — mejora de rendimiento para entidades de alta frecuencia (caso Tienda Nube, ver [3_recursos/arquitectura_sistema/incidentes_de_plataforma.md §4](../../arquitectura_sistema/incidentes_de_plataforma.md)). Clave compuesta por forma de pago + canal + código de comercio, TTL de 10 minutos.
- **Mapeo de errores de pago externos:** muchos errores se reportaban como código 500 (falla de servidor) cuando en realidad eran 422 (validación) — genera alertas falsas y complica el diagnóstico. Fix aprobado y reclasificado como bugfix.
- **Hotfix descartado:** eliminación de una regla de convenio en el panel de administración que afecta incorrectamente a otras entidades — el problema persiste desde marzo, sin riesgo crítico inmediato. Se descarta el hotfix, se investiga en Staging para corrección en versión futura estándar.

---

## 6. Archivos de Cuadratura (resumen de saldos y comprobantes) — diseño para publicar en la Web

> Fuente: mail "Diseño de Cuadratura en prod - Wallet" (Mariana Nadalín, 2026-08-14) — diseño formal de los archivos de cuadratura para publicar en la Web, mismo criterio que los archivos de movimientos/saldos ya documentados en §1.

**Dos archivos nuevos:**
- `CUADRATURA-RESUMENSALDOS-{{codigoOrganizacion}}-AAAAMMDD`
- `CUADRATURA-RESUMENCOMP-{{codigoOrganizacion}}-AAAAMMDD`

**Formato:** delimitado por punto y coma (`;`). Se genera un archivo diario, agrupado y zipeado por fecha de proceso, con la misma lógica de generación que los archivos de movimientos ya existentes — solo se generan en días hábiles.

**`CUADRATURA-RESUMENSALDOS` — campos:** Fecha, Saldo CVU, Saldo S/extracto, Diferencia, Consumos.
- **Saldo CVUs**: sumarización (suma/resta) de los saldos de todos los CVU de la organización al cierre del día.
- **Mov Extracto**: sumarización (suma/resta) de todos los movimientos registrados en el extracto bancario en esa fecha.
- **Saldo S/Extracto**: saldo al cierre del día — se toma el valor del último movimiento del día en el extracto.
- **Diferencia**: cálculo entre Saldo CVUs y Saldo S/Extracto. **Si es negativo, es observado por el BCRA** — los saldos de las CVU deben ser iguales o menores a los saldos de la cuenta recaudadora (CBU).
- **Consumos**: sumarización (considerando el signo) de los comprobantes de la organización.
- Ejemplo de fila: `11/12/2024;22302808.70;19051866.42;22369580.41;66771.71;19060113.41`

**`CUADRATURA-RESUMENCOMP`:** contiene el consumo del saldo del día, desagregado por tipo de comprobante.
