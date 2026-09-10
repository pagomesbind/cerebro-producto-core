# Automatización de Creación Masiva de QR (SFTP → ETL → SP Orquestador → Webhook)

> Estado: en producción desde 2026-08-13. Mecanismo técnico construido bajo el ticket AD-660 (Epic AD-497, PRD-66 — ver [`1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md §4`](../../../1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md)). Es la contracara técnica del [incidente de saturación de cola de QR por PNET](incidente_qr_masivo_provincia_net.md): este documento explica el mecanismo que produce el patrón de carga sostenida observado en los datos.
>
> Fuente: documento funcional/operativo generado por `sql-data-explorer@fintexa-sqlserver` vía `/fsql` a partir del código fuente y tablas de `PaymentAcceptorDeudaDB` (ambiente qrbind-stg, solo lectura) — autora Daniela Collia (Fintexa), generado 2026-07-06, revisado 2026-07-07.

## 1. Propósito

El proceso permite que una entidad (hoy **Provincia NET**, código de producción `A046` / stage `A026`) genere masivamente QR de deuda a partir de un archivo `.csv` o `.zip`, sin pasar por la creación de a una. Capacidad objetivo: **~1.000.000 de registros por lote**. SLA objetivo de procesamiento: **ventana de 3 horas**. Confirmado en producción el 2026-08-13.

La entidad deposita el archivo en un directorio compartido mediante SFTP (`qr_masivo/{CodigoEntidad}/A_Procesar`). A partir de ahí, el proceso: valida el archivo → lo toma para procesamiento → carga la información en la base de datos → crea las deudas → asocia un QR a cada deuda utilizando un pool de QR pre-generados → genera los archivos de resultado → deja los reportes disponibles para descarga → notifica a la entidad mediante un webhook.

## 2. Actores

| Actor | Ubicación / componente | Responsabilidad |
|---|---|---|
| Worker Service / Monitores | `PaymentAcceptor.Deuda.Api/HostedServices/WorkerService.cs` | Tareas programadas (timers, `AutoReset=false` + semáforo anti-reentrancia por tarea) que mueven archivos entre carpetas y actualizan el estado del archivo en `EjecucionFlujo`. |
| Job ETL | Servidor de tierra (on-prem), `DeudaQRMasivo/mvp_v2/cross_server/` | Si el archivo viene comprimido (`.zip`) lo descomprime para obtener el `.csv`; copia el archivo a una tabla temporal, luego a `dbo.DeudaLoteAuxTest`, y registra el archivo en `dbo.ArchivosProvinciaNetProcesados` con `Procesado = False`. |
| Job SQL de orquestación | `src/scripts/jobs/01_Crear_Jobs_Orquestacion.sql` | Lee `ArchivosProvinciaNetProcesados`, toma el primer archivo con `Procesado = False` (el subido primero), lo marca `Procesado = True` y ejecuta el SP Orquestador pasándole el nombre del archivo. |
| SP Orquestador + SPs de paso | Base `PaymentAcceptorDeudaDB` | Prepara los datos, crea las deudas y asocia los QR desde el pool, y finaliza dejando el estado en `PROCESADO`. Ante fallo de un paso obligatorio, setea `ERROR` — no mueve archivos, de eso se encarga el Monitor. |
| Job de generación de reportes | Lado SQL / servidor | Al detectar `Estado = PROCESADO`, genera los reportes CSV (zippeados) del lote y los deja en `/Procesados` de la estructura File Manager del cliente; al terminar deja el estado en `COMPLETADO`. **La API `PaymentAcceptor.Deuda` no reconoce el estado `PROCESADO` ni genera el reporte** — es responsabilidad exclusiva de este Job. |
| WebhookSender | Servicio transversal | Envía el webhook HTTP de notificación a la entidad, con headers firmados para verificación en destino. Solo se envía en la rama exitosa. |
| Shared.FileManager | Servicio transversal | Descarga y navegación de los archivos de resultado, vía token cifrado. |

> La creación de las deudas y la asociación de los QR ocurren del lado SQL, dentro del SP Orquestador — la API `PaymentAcceptor.Deuda` interviene únicamente en el manejo de archivos y estados; el `EjecucionFlujoRepository` lee y actualiza el estado, pero no inserta ejecuciones.

## 3. Flujo end-to-end (fases)

**Fase 1 — Ingreso del archivo (`A_Procesar → En_Proceso`).** Tarea programada `REED_QR_MASIVO_FILE` (comando `MoverArchivoAProcesarCommand`). Toma un archivo solo si: `PATH_FOLDER` y `CODIGO_ENTIDAD` están configurados; la carpeta `En_Proceso` está **vacía** (procesamiento secuencial, un archivo a la vez por entidad); la extensión es `.csv`/`.zip`; la nomenclatura es válida y la entidad coincide (`{entidad}_{caja}_qrmasivo_yyyymmddhhmm.ext`); el archivo está **estable** (antigüedad y tamaño sin cambios, para no tomarlo mientras se sube); y se toma un **lock** por archivo (evita doble procesamiento). Entre candidatos válidos toma el más antiguo.

**Fase 2 — ETL a la base (servidor de tierra).** Si el archivo viene comprimido lo descomprime, copia a tabla temporal y de ahí a `dbo.DeudaLoteAuxTest` en `PaymentAcceptorDeudaDB`, y registra el archivo en `dbo.ArchivosProvinciaNetProcesados` con `Procesado = False`.

**Fase 3 — Orquestación en base de datos.** Un job SQL lee `ArchivosProvinciaNetProcesados`, marca `Procesado = True` y ejecuta el SP principal `sp_EjecutarFlujoDinamico` — un orquestador **table-driven** (pasos configurables en `FlujoProceso`/`FlujoPaso`, flujo `FLUJO_AUTOMATIZADO`). Registra trazabilidad completa en `EjecucionFlujo` / `EjecucionPaso` / `LogEventoFlujo` / `MigracionLog`. Tres pasos:
- **Paso 1 · Preparar** — valida que no haya registros repetidos, valida que la caja esté preconfigurada, genera o repone el stock de QR de la caja (`QrPoolConfiguracion`/`QrPoolLog`/`ReponerStockQrPool_Automatico`), hace la revisión e informe, y copia `DeudaLoteAuxTest → DeudaLoteAux`. Si la copia falla, el SP setea `ERROR` (no mueve el archivo).
- **Paso 2 · Procesar** — crea la deuda y le asocia un QR tomándolo de `QrPoolPrecalculado` (pool pre-generado), y valida la correcta creación de deudas. La migración real de datos (`sp_MigrarDeudasLote`/`sp_EjecutarMigracion`) mueve `DeudaLoteAux → Deuda + CodigoExterno + MedioPagoDisponible`.
- **Paso 3 · Finalizar** — guarda la información de las deudas generadas y los errores de los pasos anteriores, y deja el estado del archivo en `PROCESADO`.

Existe además una implementación alternativa, `sp_OrquestadorProcesoCarga` (control explícito paso a paso, con modo manual/aprobación y tablas `OrquestacionControl`/`OrquestacionLog`) — la documentación no aclara si está en uso o es solo una alternativa disponible; **la que efectivamente corre en producción es `sp_EjecutarFlujoDinamico`** según el texto.

**Fase 4 — Generación de reportes (`PROCESADO → COMPLETADO`).** Un Job detecta `Estado = PROCESADO`, genera los reportes CSV (zippeados) y los deja en `/Procesados` de la estructura File Manager del cliente (donde quedan disponibles para descarga). Al finalizar, deja el estado en `COMPLETADO`.

**Fase 5 — Archivado y notificación (`COMPLETADO → NOTIFICADO`).** Tarea programada `QR_MASIVO_PROCESADOS_NOTIFICAR` (comando `MoverArchivoEnProcesoAProcesadosCommand`). Cuando detecta `COMPLETADO`: mueve el archivo original de `En_Proceso` a `/Procesados` de la gestión interna; deja copia en `/Historico` de la gestión; en la estructura File Manager del cliente copia el archivo a `/Historico` y mueve los reportes anteriores de `/Procesados` a `/Historico` (queda disponible solo el último reporte); envía el webhook; y deja el estado final en `NOTIFICADO`.

**Rama de ERROR.** Si falla un paso obligatorio, el SP Orquestador setea `EjecucionFlujo.Estado = ERROR` pero **no mueve el archivo**. El Monitor (`MoverArchivoEnProcesoAProcesadosCommand`), al detectar un archivo en `En_Proceso` cuyo `EjecucionFlujo` está en `ERROR`, lo mueve a `/Fallidos` (si es `.csv` lo comprime a `.zip` en esta rama). **No se generan reportes ni se envía webhook** en esta rama.

## 4. Máquina de estados (`EjecucionFlujo.Estado`)

```
PENDIENTE → EN_PROCESO → PROCESADO → COMPLETADO → NOTIFICADO
                │
                └─ ERROR (falla paso obligatorio) → Monitor mueve a /Fallidos, sin webhook
```

| Estado | Lo establece | Significado |
|---|---|---|
| `PENDIENTE` | Job / default | Se creó la ejecución. |
| `EN_PROCESO` | SP Orquestador | El proceso está ejecutando sus pasos. |
| `PROCESADO` | SP Orquestador (Paso Finalizar) | Las deudas y QR fueron creados en la base de datos. |
| `COMPLETADO` | Job de reportes | Los reportes fueron generados y están disponibles en `/Procesados`. |
| `NOTIFICADO` | Monitor / API | El archivo fue archivado y la entidad fue notificada por webhook — estado final del flujo exitoso. |
| `ERROR` | SP Orquestador (setea) / Monitor (mueve) | Falló un paso obligatorio; el archivo termina en `/Fallidos`, sin webhook. |

## 5. Consulta, descarga y estructura de carpetas

- **Consulta de estado:** `GET /api/v1/status-deuda-masivo?nombreArchivo={archivo}` → devuelve estado de la ejecución y detalle de los pasos. Grupos habilitados: `ADMINISTRADOR`, `ENTIDAD`.
- **Descarga de resultados:** vía `Shared.FileManager`, con descarga por token cifrado y navegación de carpetas.
- **Carpetas:** `A_Procesar/` (entrada), `En_Proceso/` (archivo tomado, uno a la vez), `Procesados/` (completados OK), `Fallidos/` (con error), `Historico/` (copias con timestamp), `Locks/` (locks lógicos por archivo). Existen **dos estructuras** en paralelo: la de gestión interna (`PATH_FOLDER`) y la que usa el cliente vía File Manager (`PATH_FOLDER_FILE_MANAGER`, donde el Job deja los reportes descargables).
- **Nomenclatura obligatoria:** `{entidad}_{caja}_qrmasivo_yyyymmddhhmm.(csv|zip)` — el primer segmento debe coincidir con el `CODIGO_ENTIDAD` configurado para la tarea. Config de entidad: Stage `A026` · Producción `A046`.
- **Procesamiento secuencial por entidad** — `En_Proceso` debe estar vacía para que el siguiente archivo de esa entidad pueda ser tomado (no es secuencial cross-entidad, es por entidad).

## 6. Por qué importa para el incidente de saturación de cola QR

Desde el pase a producción el 13/08, los picos de PNET pasaron de tener la firma de una "carga manual puntual" (estallido aislado desde una base casi en cero) a la firma de un "proceso automático continuo" (base ya alta, se sostiene elevada varios días) — ver [incidente_qr_masivo_provincia_net.md](incidente_qr_masivo_provincia_net.md). Esta mecánica explica el *cómo*: un job que procesa hasta 1M de registros en una ventana de 3 horas, de forma secuencial por entidad — mientras corre un lote, la cola de generación de QR de esa entidad (y, según la hipótesis en investigación, potencialmente la cola compartida con otras entidades) queda ocupada de forma sostenida durante horas, no en un pico instantáneo. No resuelve por sí sola la pregunta de "por qué el reclamo apareció recién en septiembre", pero es la pieza de mecánica que faltaba para entender cómo se genera el patrón sostenido observado en los datos.

## 7. Fuentes citadas en el documento original

Diagrama de flujo `Deuda 1.0 - Automatización creación masiva de QR - Flujo v2.png`/`.svg` (regenerado 2026-07-07) · `PaymentAcceptor.Deuda.Api/HostedServices/WorkerService.cs` · `PaymentAcceptor.Deuda.Application/Commands/QrMasivo/` · SP Orquestador primario `DeudaQRMasivo/mvp_v2/02_SP_Orquestador_Dinamico_v2.sql` · SP Orquestador alternativo `DeudaQRMasivo/src/procedures/sp_OrquestadorProcesoCarga.sql` · Jobs `DeudaQRMasivo/src/scripts/jobs/01_Crear_Jobs_Orquestacion.sql` · ETL `DeudaQRMasivo/mvp_v2/cross_server/` · Base `PaymentAcceptorDeudaDB` (ambiente qrbind-stg, solo lectura).

## Ver también

- [incidente_qr_masivo_provincia_net.md](incidente_qr_masivo_provincia_net.md) — la investigación de la demora de cola que afecta a PNET/DEPAY, para la que esta mecánica es la pieza técnica que faltaba.
- `1_proyectos/prd-66_provincianet_creacion_masiva_qr/proyecto.md` §4/§7 — historial de entrega y puesta en producción (13/08) de este mismo mecanismo.

---
*Creado: 2026-09-10 — `/context_merge` desde `contexto_vivo/` (Pablo Gomes): mecánica técnica completa del flujo automatizado de creación masiva de QR (SFTP → ETL → SP Orquestador → reportes → webhook) para PRD-66/Provincia NET.*
