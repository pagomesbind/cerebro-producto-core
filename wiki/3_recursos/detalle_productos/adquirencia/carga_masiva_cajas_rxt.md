# Creación Masiva de Cajas con CVU (RxT)

> Estado: en producción. Contenido destilado de la Epic de Notion "Creación masiva de cajas con cvu". Reubicado desde `detalle_productos/cobros/carga_masiva_cajas.md` en la reestructuración PARA en cascada (2026-08-12) — es una herramienta de RxT (Recaudación por Transferencia), un canal de Adquirencia, no del Agente de Cobros y Pagos.

## 1. Qué es y por qué

Funcionalidad interna de Bind PSP (no publicada a entidades/clientes) para crear masivamente cajas con CVU y alias para el producto RxT, vía un endpoint que recibe un CSV. Resuelve pedidos de creación masiva que hacen las entidades que no se integran por API y tienen bases grandes de clientes — antes se hacían a mano, uno por uno.

- **Input**: CSV con un registro por caja a crear (`idexterno`, `alias`), pidiendo `EntidadId`, `ComercioId`, `SucursalId` en el request. Todas las cajas del lote pertenecen a la misma entidad/comercio/sucursal.
- **Objetivo de velocidad**: al menos 40 mil cajas+cvu+alias por hora, admitiendo 2-3 hilos en simultáneo para superar el límite de velocidad de creación de CVU + asignación de alias en API Bank.
- **Consulta de proceso**: se puede consultar el estado del lote (id, estado, total cajas creadas, total CVUs creados, total alias asignados, y el detalle de cada `idexterno`→caja→CVU→alias creado).
- **No alcanzado**: uso por entidades directamente (sólo Bind PSP de forma controlada), lanzar creaciones masivas en paralelo.

### Diseño en 3 entregas

1. **(1/3) Creación de cajas "En Proceso" + Lotes**: endpoint con input CSV y publishers; consumers crean las cajas sin CVU ni alias todavía ("En Proceso"); se generan Lotes de CVU por cliente particular (mismo CUIT) a demanda, con `FechaAlta`/`FechaBaja`/`Motivo`.
2. **(2/3) Completitud de cajas + consulta de proceso**: eventos de asignación de CVUs y alias según los lotes del cliente; endpoint de consulta de estado del proceso de generación.
3. **(3/3) Api Carga Masiva**: se migra el flujo a una API nueva y genérica de "Cargas Masivas" (proceso identificado como `CargaMasivaCajas`, reutilizable a futuro para otros procesos de carga), integrando la lectura de archivos con la asignación de CVUs y la creación completa de cajas en Api Comercios.

## 2. Features relacionadas

- **Cajas: idExterno**: al crear una caja (no sólo por carga masiva) se puede enviar un `idExterno` propio de hasta 50 caracteres; se valida que la entidad no tenga ya otra caja con ese mismo `idExterno` (si lo tiene, error "idExterno ya existente"; si el formato es inválido, error "idExterno inválido"). El GET de cajas permite filtrar y devuelve el `idExterno`.
- **nombreCaja = nombreCVU**: si al crear una caja (por API individual o por carga masiva) se especifica un nombre ≠ null, el CVU asociado se crea con ese nombre + el CUIT del comercio (en vez del nombre genérico del comercio). Si la caja se crea sin nombre y luego se le asigna uno, el próximo CVU que se cree para ella también usa ese nombre. Validación: nombre de caja entre 4 y 40 caracteres, sin caracteres especiales (rompía la creación del CVU en Coelsa).

## 3. Cluster de bugs de estabilización

La puesta en producción de la carga masiva generó una seguidilla de defectos, la mayoría bajo la etiqueta `[AltaMasivaCajas]` / `[RxT]`:

- **TipoCaja=2 por defecto**: el alta masiva creaba todas las cajas con `TipoCaja=2`, un valor que derivaba en un error conocido en producción; debían crearse con `TipoCaja=1`.
- **Alias del CSV no se asigna**: las cuentas se creaban en CVU Collect (`dbo.Accounts`) sin el alias indicado en el CSV.
- **Cajas creadas sin cuentas**: en algunos lotes las cajas se creaban pero no se creaba ninguna cuenta asociada, o sólo una parte (ej. 3 de 6 registros).
- **CVUs con nombre del comercio en vez del nombre del CSV**: contradecía la regla de `nombreCaja=nombreCVU` (ver §2) — el alta masiva no la respetaba.
- **No se valida preexistencia de alias**: si el CSV traía un alias ya usado (dentro del mismo archivo o ya existente en Coelsa/DB), igual se daba de alta.
- **No se valida cantidad de caracteres del alias**: debía validarse mínimo 6 y máximo 20 caracteres.
- **Nuevo endpoint (Api Carga Masiva, 3/3) con error 500** al migrar el flujo a la nueva API.
- **GET estado de Lote incompleto**: la consulta de proceso de la nueva API no devolvía id/estado del lote, total cajas creadas, total alias asignados, ni dentro del detalle de cada caja el `idExterno` (null si no vino en el CSV) o el CVU.
- **No se puede asignar `idExterno` desde el CSV de carga masiva** (a diferencia del alta individual — ver §2); además la columna CUIT del CSV es redundante porque se usa el CUIT del comercio de la sucursal, y podría reemplazarse por la columna de `idExterno`.
- **Registros sin Nombre (dnicliente) no se validan y arrastran error a otros registros del mismo lote que estaban completos**: la regla correcta es que sólo deben fallar los registros incompletos, sin afectar a los demás del mismo archivo.
- **Error 422 en el campo `resultado` cuando el Alias viene vacío**: debía indicarse el código de caja creada y estado `PROCESADO`, no un error 422, ya que la caja y la cuenta sí se creaban correctamente sin alias.

---
*Fuente: Notion histórico, Epic "Creación masiva de cajas con cvu" (27 SP) — ingesta 2026-07-06.*
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/cobros/carga_masiva_cajas.md` a Adquirencia (RxT) en la reestructuración PARA en cascada. Contenido sin cambios.*
