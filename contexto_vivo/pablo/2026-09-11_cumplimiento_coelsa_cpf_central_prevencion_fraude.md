---
id: 2026-09-11_cumplimiento_coelsa_cpf_central_prevencion_fraude
pm: pablo
fecha_captura: 2026-09-11
fuente: "Ingesta manual de documentación pública de Coelsa (VPN habilitada) — https://documentacion.coelsa.com.ar/CPF/#introduccion — sitio completo. Consultado 2026-09-11."
producto: "transversal"
tema: Central de Prevención de Fraude (CPF) de Coelsa — base compartida de cuentas sospechosas/fraudulentas del ecosistema, API REST y mensajería RabbitMQ
tipo: conocimiento
destino_propuesto: wiki/3_recursos/cumplimiento_normativo/coelsa_cpf_central_prevencion_fraude.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 201b3e0
---

## Qué es la CPF y por qué importa

La **Central de Prevención de Fraude (CPF)** es una base de datos **compartida por todo el ecosistema** (bancos, PSP, procesadores) de cuentas (CBU/CVU) y CUIT involucrados en operaciones sospechosas o fraudulentas. Objetivo explícito de Coelsa: *"servir como herramienta en el análisis de fraude al identificar datos y patrones sospechosos"* — es decir, cualquier entidad puede reportar un caso y **cualquier otra entidad puede consultarlo**, incluso antes de operar con esa cuenta. Es distinta de COELSA.PREVENT (scoring transaccional automático, ver item separado) — la CPF es un **registro colaborativo manual/semi-manual** de casos, no un modelo de IA en tiempo real, aunque ambas viven bajo el mismo paraguas comercial "COELSA.PREVENT" (el menú de PREVENT_WEB tiene un acceso directo a CPF).

**Alcance de operaciones cubiertas** (explícito en la documentación): transferencias inmediatas minoristas (Prisma/Link), CREDIN, DEBIN, **Echeq** (excluido de esta ronda de ingesta salvo por esta mención transversal), Pagos con Transferencia (PCT), transferencias inmediatas mayoristas (Interbanking) — personas físicas y jurídicas.

## Autenticación y permisos

Mismo esquema OAuth2 que el resto de los productos Coelsa. Dos perfiles de sistema distintos en CoelsaAdmin:

- **`CPF`** (API): alta, modificación, consulta por ID/CUIT/CBU/CVU/estado, baja, alta masiva, consulta por fecha, consulta de CUIT por código de banco.
- **`CPF_WEB`** (interfaz web + API): todo lo anterior más notificaciones personales/generales y consulta de permisos — es el rol para operadores humanos.

## Catálogo de la API (`/api/v1/operaciones/...` y `/api/V1/operaciones`)

Todo mensaje lleva como dato común `ent_id` (entidad/billetera que envía), `cli_id` (cliente/procesador), `mdt` (fecha/hora del mensaje) — viajan implícitos en el token.

| Método | Endpoint | Función |
|---|---|---|
| POST | `/api/V1/operaciones` | Alta de operación sospechosa/fraudulenta |
| PUT | `/api/v1/operaciones/operacion` | Modificación (cambio de estado, ver abajo) |
| GET | `/api/v1/operaciones/operacion` | Consulta por ID |
| GET | `/api/v1/operaciones/GetOperacionesByCuitCbuCvu/{valor}/{estado}` | Consulta por CUIT/CUIL/CBU/CVU + estado |
| GET | `/api/v1/operaciones/GetOperacionesByCuit` | Consulta por CUIT de entidad receptora/reportante |
| DELETE | `/api/v1/operaciones/operacion` | Eliminación (**solo** la entidad reportante, **solo** si el estado sigue en `CASO_VERIFICAR`) |
| GET | `/api/v1/operaciones/GetDataByCBUCVUCuentaReceptora` | Autocompletado (solo Web) — trae denominación/CUIT/entidad del receptor a partir de un CBU/CVU |
| GET | `/api/v1/operaciones/GetCuitByBankCode` | Autocompletado del CUIT de la entidad reportante logueada |
| POST | `/api/v1/operaciones/AltaMasiva` | Alta masiva vía archivo CSV |
| GET | `/api/v1/operaciones/GetOperationByDate` | Descarga por rango de fechas (máx. 90 días) |
| GET | `/api/v1/operaciones/GetNotificacionesPersonales` / `GetCantidadNotificacionesPersonales` | Notificaciones de casos pendientes de gestionar por la entidad logueada |
| GET | `/api/v1/operaciones/GetNotificacionesGenerales` | Casos reportados por todo el ecosistema en el último mes (solo lectura, informativo) |

**Regla de privacidad importante:** el campo **`Importe`** de una operación solo es visible para las entidades **Reportante y Receptora** de esa operación puntual — el resto del ecosistema que consulta no lo ve.

## Ciclo de estados de una operación

- Nace en **`CASO_VERIFICAR`** (o pasa por `VERIFICACION_AUTOMATICA`/`SOSPECHOSO_NO_VERIFICADO` según el flujo).
- La entidad **Receptora** puede moverla a **`CASO_VERIFICADO`** u **`OPERACION_GENUINA`** — son estados terminales; una vez en cualquiera de los dos, **ninguna otra entidad puede seguir modificándola** (ni Reportante ni Receptora).
- Mientras está en `CASO_VERIFICAR`, la **Reportante** puede seguir editando campos no críticos (metodología, tipificación de cuenta, canal, submetodología, observaciones) — siempre que la Receptora todavía no la haya tratado.
- Solo se puede **eliminar** una operación en estado `CASO_VERIFICAR`, y solo la entidad Reportante.

## Alta masiva y descargas

- **Alta masiva por CSV**: UTF-8, delimitado por `;`, máximo **20 registros por archivo** (nota: la Web menciona 20; a confirmar si el límite de la API `AltaMasiva` es el mismo o distinto).
- **Descargas parametrizables**: rango máximo de 90 días, hasta 50.000 registros por consulta (pagina si se supera), formatos `.XLSX`/`.CSV` desde el front o `.JSON` desde el back. **Ventana horaria restringida: solo entre las 17:00 y las 23:00 hs** del mismo día.

## Mensajería RabbitMQ — notificaciones de novedades de CPF

Las entidades pueden suscribirse (por única vez) al producto **`CPFNEWS`** para recibir en una cola propia las novedades de altas/modificaciones de operaciones relevantes para ellas, sin tener que hacer polling de la API:

| Endpoint | Función |
|---|---|
| `POST /api/Suscripcion/Suscribir` | Suscribirse al producto `CPFNEWS` (crea la cola) |
| `DELETE /api/Suscripcion/Cancelar/{queue}/{productCode}` | Cancelar suscripción (baja lógica, no borra la cola) |
| `POST /api/Cola/Limpiar` | Vaciar la cola de mensajes pendientes sin cancelar la suscripción |
| `GET /api/Suscripcion/{productCode}` | Consultar el nombre de cola asignado |

Mensajes tipo `STRING` en formato JSON, ej. novedad `CPF_ALTA`:
```json
{
  "CUIT_iniciador": "...", "CUIT_reportante": "...", "CUIT_receptor": "...",
  "CBU_receptor": "...", "Id_operacion": "...", "Novedad": "CPF_ALTA",
  "Message": ""
}
```
Una variante más rica (solo consumo Link/Prisma) agrega `Estado`, `Fecha_ocurrencia`, `Denominacion_Receptor`, `ID_Moneda`, `Importe`, `Caso_verificado`, `Id_caso_verificado`.

## Relevancia y siguiente paso sugerido

No hay evidencia en la wiki de que Bind ya consuma la CPF (ni por API ni por la cola RabbitMQ) — `cumplimiento_normativo/gestion_riesgo_fraude_bcra.md` documenta la normativa BCRA (COM 8471/8473) pero no menciona la CPF como herramienta operativa concreta. Vale la pena que el PM confirme con el equipo de Fraude/Cumplimiento si Bind ya opera contra esta API (alta de casos propios, consulta antes de operar con una cuenta nueva) — no lo registro como gap por no haber contradicción, pero es una pregunta de negocio abierta y de alto valor potencial (evitar fraude cruzando contra una base compartida de todo el ecosistema).

## Confianza

Alta — documentación oficial completa, sin contradicciones detectadas.
