# Gestión de Jira en Bind PSP

> Fuente: `raw/Proceso forma de uso de Jira en Bind PSP.docx` + `raw/Responsables bind psp - Página 1.png` (ingesta 2026-07-04). Reubicado desde `detalle_productos/transversal/gestion_jira.md` en la reestructuración PARA en cascada (2026-08-12) — es proceso interno del equipo, no conocimiento de producto. El §1.8 original ("Proceso de Análisis de Riesgo de Despliegue") pasó a su propio archivo, [analisis_de_riesgo_de_despliegue.md](analisis_de_riesgo_de_despliegue.md).
>
> Describe cómo se usa Jira de punta a punta en Bind PSP: hay **dos instancias distintas** que no se mezclan entre sí — `bindpsp.atlassian.net` (Producto y Desarrollo) y el Jira Service Management del grupo Bind (`bindtm.atlassian`, Soporte — ver [overview_equipo.md](../overview_empresa/overview_equipo.md)).

## 1. Instancia `bindpsp.atlassian.net` — Producto y Desarrollo

### 1.1 Espacios de Desarrollo (Jira Software)

Hay un Espacio de Jira por cada producto:

| Producto | Código de espacio |
|---|---|
| Emisión / Wallet | **WS** |
| Adquirencia | **AD** |
| Onboarding | **OB** |
| Ardid | **ARD** |
| Pago Fácil | **SER** |

> Corrección 2026-07-06 (verificado contra el Jira real vía `getVisibleJiraProjects`): el código de espacio de Ardid es **ARD**, no AR; y el proyecto **SER** se llama "PAGO FÁCIL" en Jira, no "Servicios". También existen los espacios **QA** y **PQ** (Prueba QA), de tipo Xray (test cases), fuera del alcance de tickets de desarrollo de este documento. El espacio de Producto (§2) tiene código **PRD** (no documentado explícitamente antes de esta corrección).

En cada espacio se crean tickets de desarrollo y se gestiona su ciclo de vida completo.

### 1.2 Tipos de ticket de desarrollo

Un ticket de desarrollo es de tipo **Historia** o tipo **Error**. Puede originarse de dos formas:

1. **Iniciativa de producto** — analizada, priorizada y aprobada por Producto. Se crean epics o historias relacionadas a partir de tickets de tipo **IDEA** en el espacio de Producto (ver §2).
2. **Incidente productivo** — surge generalmente de un reclamo que Soporte levantó al equipo de desarrollo en su Jira Service Management (ver §3). Ese ticket requiere desarrollo o deploy para resolverse; según su urgencia puede requerir un **Hotfix** o acomodarse en una versión normal. Se crea entonces un ticket de desarrollo en el Espacio correspondiente al producto para que el Project Manager pueda planificar su desarrollo y deploy. En general son de tipo **Error**.

### 1.3 Subtipos de Error (detectados durante QA en staging)

Los tickets tipo Error llevan un prefijo en el nombre según el momento y origen del hallazgo:

| Prefijo | Cuándo se usa |
|---|---|
| *(sin prefijo)* | Error del software detectado directamente en producción, que debe repararse. |
| **[OBS]** | Observación encontrada durante el QA en staging mientras se probaba un ticket nuevo, y el error **no existía antes** — lo ocasionó el desarrollo actual. |
| **[DEF]** | Observación encontrada durante el QA en staging, pero se identifica que el error **ya existía desde antes** y no es consecuencia de la versión actual. |
| **[REQ]** | Observación encontrada durante el QA en staging, pero se identifica que el error es consecuencia de una **mala definición de la historia de usuario**. |

Las pruebas de QA se hacen con los tipos de issue propios del aplicativo **Xray**.

### 1.4 Prioridad, versión y story points

- **Prioridad:** la define el Product Owner al crear el ticket, mientras está en estado `BACKLOG`.
- **Versión:** los tickets se etiquetan bajo una versión corregida — cada versión agrupa los tickets que pasan a producción todos juntos (ver ceremonias de publicación mensual en [publicaciones_mensuales.md](publicaciones_mensuales.md)).
- **Story points:** indican el tamaño relativo de esfuerzo que le llevó al desarrollador completar el ticket.
- **Convención de conversión Talle de camiseta → Story Points** (confirmada por el usuario, 2026-07-06): `S = 1 SP` · `M = 3 SP` · `L = 7 SP` · `XL = 15 SP`. Es la convención vigente del proceso actual de Jira/gestión de desarrollo de Bind PSP. Útil para estimar el total de SP de tickets que solo tienen talle de camiseta registrado y no un valor de Story Points directo (ver uso en [referencia_estimaciones.md](referencia_estimaciones.md)). No hay talle `XXL` confirmado en esta convención — si aparece, tratarlo como gap y consultar al usuario antes de asumir un valor.

### 1.5 Épicas principales

Cada issue va bajo una épica Principal, que agrupa tickets de un mismo proyecto, funcionalidad o tema. Hay épicas generales fijas:

- **SOPORTE** — tickets surgidos por reclamos desde el área de Soporte.
- **INICIATIVAS TÉCNICAS** — tickets que crea el propio equipo de desarrollo sobre deuda técnica, performance o arquitectura.
- **COE** — tickets que crea el equipo de arquitectura técnica.
- **REQUERIMIENTOS INTERNOS** — pedidos de stakeholders internos (ej. áreas de soporte) que no son incidentes.

Ver el detalle de cómo se solicita cada tipo de ticket (formularios Jira por producto y por rol solicitante) en [requerimientos_al_equipo_tecnico.md](requerimientos_al_equipo_tecnico.md).

### 1.6 Estados del ticket de desarrollo

| Estado | Significado |
|---|---|
| `BACKLOG` | El ticket está siendo definido y priorizado por el equipo de Producto. |
| `ASIGNADO` | Ya fue definido y priorizado; debe analizarse técnicamente y desarrollarse. Pasa a ser responsabilidad del **Project Manager**. |
| `LISTO PARA DESARROLLO` | Fue refinado técnicamente y está listo para empezar a desarrollarse. |
| `EN CURSO` | Está siendo trabajado por el desarrollador. |
| `EN QA` | Ya está en el ambiente de staging funcional y debe probarlo el equipo de QA de Bind PSP. |
| `CON DEFECTO` | Fue probado y tiene algún defecto que lo bloquea. |
| `FINALIZADO` | Fue aprobado por QA. |

**Regla de pasaje a producción:** por definición, no deberían pasarse a producción tickets que no estén en estado `FINALIZADO` (no fueron probados). Pueden hacerse excepciones puntuales con el debido análisis de riesgo, pero como mínimo el ticket tiene que estar en estado `EN QA`.

> `FINALIZADO` es el nombre real y único del estado terminal — confirmado por el usuario el 2026-07-04.

### 1.7 Relación con Jira de FINTEXA

Bind PSP trabaja con **FINTEXA** como software factory proveedor externo (ver [overview_equipo.md](../overview_empresa/overview_equipo.md)), que gestiona su propio ciclo de desarrollo en un Jira separado. Bind PSP trata de replicar el estado de ese ciclo en su propio tablero:

- Hay **automatizaciones**: cuando un ticket pasa a estado `ASIGNADO` en el espacio de Bind PSP, se crea automáticamente el ticket correspondiente en el Jira de FINTEXA para que lo analicen sus analistas técnico-funcionales.
- A medida que el ticket avanza de estado del lado de FINTEXA, debería actualizarse también del lado de Bind PSP.
- **Cambio de estado más importante:** cuando FINTEXA termina de desarrollar el ticket y su propio equipo de QA lo valida y aprueba, formalizan la "entrega" del ticket en ambiente de staging (el ticket ya estaba en staging para que ellos lo prueben) pasándolo en el tablero de Bind PSP a estado `EN QA`. Esto habilita al equipo de QA de Bind PSP a probarlo.
- FINTEXA propone las versiones disponibles para deployar y consensúa con el Project Manager de Bind PSP el alcance, quien valida que todos los controles se hayan realizado y documentado antes de confirmar la fecha de pasaje a producción.

## 2. Espacio de Producto — Jira Product Discovery (`PRD`)

Producto usa un Espacio de **Jira Product Discovery** llamado **Producto (PRD)**, donde cada Product Owner crea iniciativas de tipo **IDEA**. Llegado el momento, el PO crea tickets en el espacio de Jira Software correspondiente al producto (§1), define cada ticket como historia de usuario, le coloca una Prioridad, y lo pasa a `ASIGNADO` — a partir de ahí es responsabilidad del Project Manager que se desarrollen con calidad y se pasen a producción.

### 2.1 Estados de una IDEA

| Estado | Significado |
|---|---|
| `PARKING LOT` | Iniciativa recién creada; ningún PO trabajó en ella todavía. |
| `DISCOVERY` | El PO está analizando y trabajando en el discovery. En este estado es responsable de completar el **PRD** (Product Requirements Definition), que se escribe en la descripción de la IDEA. |
| `EN APROBACION` | El PRD se definió y está a disposición del comité para revisión y aprobación. |
| `LISTO PARA EMPEZAR` | La iniciativa fue aprobada y puede desarrollarse. El PO debe crear los tickets de desarrollo asociados necesarios para completar el alcance aprobado. |
| `EN CURSO` | Los tickets de desarrollo de esta iniciativa fueron creados y asignados al equipo de desarrollo. |
| `SHIPPING` | Los tickets ya fueron publicados en producción, o hubo un gran progreso que permite trabajar en las tareas necesarias para el Go Live. El PO debe traccionar y concretar los pendientes para el Go Live. |
| `FINALIZADA` | La iniciativa fue finalizada y ya está productiva. |
| `CANCELADO` | La iniciativa se cancela para siempre — no se hará. |
| `EN STAND BY` | La iniciativa se pausa y no se hará por el momento. |

Cada IDEA tiene:
- **Datos Relevantes** — funcionalidad propia de Jira Product Discovery donde el PO adjunta información esencial para la definición.
- **Comentarios** — donde se registran novedades y, explícitamente, las aprobaciones.

## 3. Espacio de Soporte — Jira Service Management (grupo Bind, `bindtm`)

Soporte usa un espacio llamado **Bind PSP** dentro del Jira del grupo Bind (`bindtm`) — **sin relación directa** con los espacios de Producto y Desarrollo en `bindpsp.atlassian.net` (son instancias distintas). Es la vía por la que los clientes crean tickets de reclamos o pedidos.

En general los tickets son:
- Pedidos de soporte puntuales por temas de producción, o pedidos de nuevas configuraciones/altas.
- Un tipo de tarea específico para **Integraciones**: un Jira de integraciones lo crea el equipo Comercial, y el equipo de Integraciones agrega como clientes a los representantes de la entidad a integrar — da soporte, responde dudas, pasa credenciales y gestiona evidencia de homologación (ver [overview_equipo.md](../overview_empresa/overview_equipo.md), fila Comercial/Soporte).

Cuando desde un ticket de Soporte se identifica la necesidad de un desarrollo, se crea un nuevo ticket de desarrollo en el `BACKLOG` del espacio correspondiente (§1) — es el puente entre Soporte y Desarrollo.

## 4. Responsables por etapa del flujo (diagrama `Responsables bind psp`)

El diagrama fuente mapea qué rol es dueño de cada tramo del flujo combinado IDEA → ticket de desarrollo → producción:

| Rol | Personas (iniciales del diagrama) | Tramo del que es dueño |
|---|---|---|
| **Equipo Producto** | LR = Luciana Rudaz, NC = Nicolás Colón, PG = Pablo Gomes (ver [overview_equipo.md](../overview_empresa/overview_equipo.md), fila Producto) | Todo el flujo de la IDEA: `PARKING LOT` → `DISCOVERY` → `APROBACIÓN` → `LISTO` → `EN CURSO` → `SHIPPING` → `FINALIZADO`, y la creación del ticket de desarrollo nuevo. |
| **Project Manager** | MA = Matías Alzogaray (PM de desarrollo, área IT — ver [overview_equipo.md](../overview_empresa/overview_equipo.md)) | Desde que el ticket de desarrollo entra a `BACKLOG` hasta `EN CURSO`, y el ciclo completo de vuelta hasta que el ticket se publica en producción. |
| **Equipo QA** | AO = Andrea Orsini, BT = Bethania Tornari, AM = Ana Moreno — Analistas de QA, área IT (ver [overview_equipo.md](../overview_empresa/overview_equipo.md)) | Estado `EN QA`. |

Flujo resumido del diagrama: *Nueva iniciativa* → (flujo IDEA de Producto) → *Nueva ticket de desarrollo* → `BACKLOG` → `ASIGNADO` → `LISTO PARA DESARROLLO` → `EN CURSO` → `EN QA` → `FINALIZADO` → *Ticket publicado en prod* → retorno de shipping hacia *Go Live iniciativa*. En paralelo, *Cliente crea Jira de soporte con reclamo* puede derivar en "se identifica necesidad de desarrollo desde soporte", que alimenta la creación de una nueva ticket de desarrollo (mismo punto de entrada que las iniciativas de Producto, ver §1.2).

## Acceso a Jira ampliado a todo el equipo (2026-08-13)

> Fuente: Reunión "Priorizacion y backlog" (2026-08-13), minuta Gemini — sesión de repaso del flujo de priorización/versionado/pases a producción con Mariana Nadalin (nueva referente de Integraciones y Soporte), Hernán Clarich, Matias Alzogaray, Gonzalo Rivera, Maria Eugenia Vila.

**Decisión acordada:** dar acceso completo a Jira a todos los involucrados, para que cualquiera pueda verificar por cuenta propia si un desarrollo entró a producción, sin depender de consultas constantes ni perderse entre reuniones. Motivada por la dificultad de Gonzalo Rivera para seguir el estado de las versiones.

**Diagnóstico compartido en la misma sesión** (relevante para leer el flujo de §1 con más contexto): ~50% de la capacidad de desarrollo se consume en soporte/mantenimiento/corrección de errores, dejando margen limitado para iniciativas nuevas; los tickets `Highest` históricamente promediaron 16 días de resolución; 18% del tiempo de desarrollo va a tickets derivados de soporte y 25% a bugs — el equipo identificó mejorar la calidad de las historias de usuario (criterios de aceptación más claros) como la palanca principal para bajar ese retrabajo, en vez de agregar más proceso de control. Se acordó además una **mesa quincenal con Sebastián (Fintexa)** para mejorar la comunicación y pedir datos concretos de tiempos de análisis/atención, y evaluar mocks de servicios externos + automatización de pruebas del portal admin (hoy manuales).

## Relación con otros documentos de la wiki

- [publicaciones_mensuales.md](publicaciones_mensuales.md) — ceremonias de publicación mensual (que operan sobre estos mismos estados).
- [requerimientos_al_equipo_tecnico.md](requerimientos_al_equipo_tecnico.md) — proceso de autogestión de requerimientos vía formularios Jira.
- [analisis_de_riesgo_de_despliegue.md](analisis_de_riesgo_de_despliegue.md) — informe de riesgo previo a cada despliegue (ex-§1.8 de este documento).
- [overview_equipo.md](../overview_empresa/overview_equipo.md) — mapeo de iniciales/roles a personas (Producto, IT/PM, QA, Soporte).
- [../gaps_y_preguntas.md](../gaps_y_preguntas.md) — historial de los 2 gaps ya resueltos (nombre del estado terminal, identidad de BT/AM).

---
*Última actualización: 2026-08-14 — `/sync_meetings`: nueva sección "Acceso a Jira ampliado a todo el equipo" (decisión de transparencia + diagnóstico de capacidad de desarrollo y mesa quincenal con Fintexa). Ver reunión "Priorizacion y backlog" (2026-08-13) en `wiki/2_areas/control/log_reuniones.md`.*
*Última actualización anterior: 2026-08-12 — Reubicado desde `detalle_productos/transversal/gestion_jira.md` (reestructuración PARA en cascada); §1.8 extraído a archivo propio; links a `equipo.md` y `../gaps_y_preguntas.md` corregidos a su ruta nueva.*
*Última actualización anterior: 2026-07-06 — Corrección de códigos de espacio (ARD, SER=Pago Fácil) verificada contra el Jira real durante el piloto de ingesta de Jira de Producto. También se confirmó que el link formal entre IDEA (§2) y ticket de desarrollo (§1) es de tipo "Polaris work item link" (`implements`/`is implemented by`), y que casi siempre apunta primero a una Epic contenedora (que suele quedar vacía) antes que a la Historia/Error real.*
