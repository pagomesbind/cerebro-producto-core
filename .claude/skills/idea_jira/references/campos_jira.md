# Referencia técnica: campos y transiciones de Jira (`bindpsp.atlassian.net`)

> Uso interno de `/idea_jira` — no es contenido de negocio, es el mapeo de campos/IDs del conector Jira MCP para esta instancia. Si algún valor de acá deja de funcionar (Jira lo cambió), corregí esta tabla en la misma corrida antes de seguir, no improvises un ID a mano.

- **Sitio:** `bindpsp.atlassian.net` (Producto y Desarrollo) — cloudId `d07593ee-e5cd-4b6c-a371-d360063c167b`. No confundir con `bindtm.atlassian.net` (Soporte), sin conector disponible.
- **Verificado por última vez:** 2026-08-26, contra IDEAs y tickets reales vía `getJiraIssue`/`searchJiraIssuesUsingJql` (no hay forma de listar opciones de un campo directamente con las tools del conector — `getJiraIssueTypeMetaWithFields` solo devuelve los campos de sistema obligatorios, no los custom fields con sus `allowedValues`).

## 1. Espacio de Producto (`PRD`, Jira Product Discovery)

Issuetype **Idea**: `id 10035`.

### 1.1 Campos personalizados de la IDEA

| Campo | customfield | Tipo | Notas |
|---|---|---|---|
| Categoría | `customfield_10102` | single-select | payload: `{"id": "<opción>"}` |
| Producto | `customfield_10124` | multi-select | payload: `[{"id": "<opción>"}, ...]` |
| Cliente | `customfield_10322` | multi-select | payload: `[{"id": "<opción>"}, ...]` |
| SP estimado | `customfield_10389` | numérico | payload: número directo, ej. `3` (no objeto) |

### 1.2 Opciones confirmadas — Categoría (`customfield_10102`)

| Valor | id |
|---|---|
| BAU | `10073` |
| BUILD | `10072` |
| NORMATIVO | `10365` |

### 1.3 Opciones confirmadas — Producto (`customfield_10124`)

| Valor | id | Espacio de desarrollo asociado |
|---|---|---|
| Wallet | `10086` | WS |
| Cobro | `10087` | AD *(el campo dice "Cobro", el desarrollo real cae en Adquirencia/AD — patrón ya señalado como gap abierto en `gaps_y_preguntas.md`, no lo resuelvas vos, solo aplicalo)* |
| Onboarding | `10152` | OB |
| Ardid | `10327` | ARD |
| Servicios | `10185` | SER *("Pago Fácil" en el nombre del proyecto Jira, "Servicios" en esta opción del campo)* |

Si la IDEA no encaja claramente en ninguna de estas (ej. Adquirencia como tal, o un producto no listado acá todavía), **no asumas un id nuevo**: buscá primero por JQL (`project = PRD AND cf[10124] = "<valor a probar>"`) si ya existe con otro nombre: si no aparece ningún resultado, es una opción que este documento nunca vio — avisá al PM antes de forzar el valor más parecido.

### 1.4 Opciones confirmadas — Cliente (`customfield_10322`)

Catálogo abierto (una opción por cliente real, crece todo el tiempo) — no se puede enumerar acá. La única fija y reservada para esta skill:

| Valor | id | Cuándo usarla |
|---|---|---|
| SOPORTE | `10400` | IDEA originada por pedido interno (Soporte, Operaciones, Administración, Integraciones) o bug productivo transversal sin cliente puntual — nunca un cliente específico. |

Si la IDEA nace por pedido de un cliente externo concreto, buscá primero si ya existe como opción (`project = PRD AND cf[10322] = "<nombre>"`) antes de asumir que hay que crear una opción nueva — el conector no tiene una tool para dar de alta una opción de campo nueva; si no existe, avisale al PM (puede ser un typo de nombre, o necesitar alta manual en Jira admin).

### 1.5 Prioridad (campo de sistema, mismo esquema en toda la instancia)

| Valor | id |
|---|---|
| Highest | `1` |
| High | `2` |
| Medium | `3` |
| Low | `4` |
| Lowest | `5` |

Payload: `{"priority": {"id": "<n>"}}`.

### 1.6 Transiciones del workflow de la IDEA

Confirmadas contra una IDEA real (transiciones `isGlobal: true` — disponibles casi desde cualquier estado, no dependen de un estado previo puntual):

| id | Nombre / destino |
|---|---|
| 2 | EN STAND BY |
| 3 | DISCOVERY |
| **4** | **EN APROBACION** ← la que usa esta skill siempre al cerrar |
| 7 | Regresar al backlog (destino real: `PENDIENTE`) |
| 8 | CANCELADO |
| 11 | EN CURSO |
| 12 | Shipping |
| 14 | LISTO PARA EMPEZAR |
| 21 | Finalizar (destino real: `Finalizada`) |

`PARKING LOT` es el estado inicial de creación (no aparece como transición porque es el punto de partida, no un destino alcanzable desde otro estado en esta lista).

## 2. Espacios de Desarrollo (WS/AD/OB/ARD/SER, Jira Software)

Issuetype **Historia**: `id 10036` — confirmado en WS, asumido igual en AD/OB/ARD/SER por compartir el mismo esquema de tipos de incidencia de la instancia; **verificá con `getJiraIssueTypeMetaWithFields` sobre el proyecto real antes de crear si es la primera vez que esta skill toca ese espacio**, no repliques el id a ciegas. Issuetype **Epic**: `id 10000` (mismo criterio de verificación).

### 2.1 Transiciones del workflow de Historia — confirmadas en WS

| id | Nombre / destino |
|---|---|
| 2 | Asignado |
| 3 | EN QA |
| 4 | Con defecto |
| 5 | LISTO PARA DESARROLLO |
| 6 | No aplica |
| 7 | Bloqueado |
| **11** | **Backlog** ← estado en el que esta skill deja siempre a las Historias nuevas |
| 31 | En curso |
| 41 | Listo (destino real: `Finalizada`) |

**Backlog no es el resultado de una transición explícita si la Historia ya nace ahí por defecto** — confirmá el `status` inmediato después de `createJiraIssue`; solo transicioná con el id 11 si no nació ya en Backlog. Estos ids son específicos de WS — en AD/OB/ARD/SER pueden diferir (mismo nombre de estado, id de transición distinto); usá `getTransitionsForJiraIssue` sobre el ticket recién creado en ese espacio antes de asumir el mismo número.

### 2.2 Link IDEA↔Epic

Tipo **"Polaris work item link"** (`id 10006`). Dirección confirmada contra un caso histórico real (PRD-115↔WS-548) y contra `gestion_jira.md`:

- La **IDEA** va del lado **outward** (`"implements"`).
- La **Epic** va del lado **inward** (`"is implemented by"`).

O sea: `createIssueLink(inwardIssue=<EPIC-KEY>, outwardIssue=<IDEA-KEY>, type="Polaris work item link")`.

**Antes de crear el link, revisá `issuelinks` de la IDEA** (`getJiraIssue` con `fields: ["issuelinks"]`) — si ya existe un link "Polaris work item link" hacia esa Epic (en cualquier dirección), no crees uno nuevo. Un caso real de esta skill (PRD-224↔WS-1555, 2026-08-26) terminó con **dos** links por crear uno en la dirección incorrecta primero y corregir agregando el segundo en vez de poder borrar el primero (el conector no tiene tool de borrado de link) — no repitas ese error: verificá primero, creá una sola vez, en la dirección correcta.

### 2.3 Épica contenedora — sin transición forzada

Al crear la Epic, **no la transiciones a ningún estado en particular** — dejala en el estado en el que nazca por defecto. Es coherente con la Regla dura de que las Historias quedan en Backlog hasta que el PM las revise: nada bajo esta IDEA se "asigna" solo porque la skill corrió.
