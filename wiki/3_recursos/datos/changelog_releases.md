# Changelog de Releases — qué cambió en los productos con cada versión publicada

> Mantenido por [`/sync_releases`](../../.claude/skills/sync_releases/SKILL.md). Una entrada por versión publicada en producción, en orden cronológico inverso, redactada con mirada de **Product Manager**: qué valor agregó cada cambio (arreglos de errores, nuevos comportamientos, mejoras funcionales, mejoras de rendimiento, nuevos requerimientos), sin detalle técnico del cómo. Pensado para que cualquier área de Bind PSP (Soporte, Comercial, C-levels) entienda qué cambió en el producto con cada versión. El detalle de control (tickets, fechas de ingesta) vive en [`log_versiones_publicadas.md`](log_versiones_publicadas.md).

## Formato de entrada

```
## YYYY-MM-DD — <ESPACIO> <versión> (<producto>)

**Arreglos de errores:** ...
**Nuevos comportamientos:** ...
**Mejoras funcionales:** ...
**Mejoras de rendimiento:** ...
**Nuevos requerimientos:** ...
```

(Solo se incluyen las categorías que la versión realmente trae. Si algo quedó publicado pero apagado por feature flag, se dice explícitamente.)

---

## 2026-08-24 — AD 71.3 (Adquirencia)

**Mejoras funcionales:**
- Se completó el pasaje a producción del nuevo esquema de autenticación externa (AuthExternal V2) para los microservicios compartidos de CVU, DEBIN y Alias Coelsa — última etapa (3 de 3) de una migración de infraestructura que venía en curso desde julio. Sin cambio de comportamiento visible para el usuario final; mejora la base de autenticación de estos servicios compartidos.

## 2026-08-18 — W 72 (Wallet)

**Arreglos de errores:**
- La cache de credenciales de proveedores externos (Poincenot, Lirium, PagBrasil, Payway, etc.) nunca había funcionado desde su creación — todas las consultas de token pegaban innecesariamente a la base de datos. Corregido; sin impacto para el usuario final, pero reduce carga innecesaria en momentos de tráfico alto.
- Corregido un error de configuración que impedía dar de alta correctamente una organización nueva en el módulo antifraude (Ardid).
- Eliminar solo el CVU de una cuenta (sin eliminar la cuenta completa) ya no deshabilita la cuenta por error.
- Corregidos dos casos donde un contracargo de DEBIN recurrente no se procesaba correctamente: uno por una consulta incorrecta al banco central de cámara compensadora, y otro cuando el aviso del contracargo llegaba antes de que la operación original terminara de confirmarse.
- Corregido que una compra de dólar CCL fallida, con comisión de $0, no devolvía el dinero al usuario.
- El endpoint de liquidaciones por usuario (en desarrollo) ahora valida correctamente que la cuenta consultada pertenezca a la organización y esté habilitada para operar con cuentas remuneradas.

**Nuevos comportamientos:**
- El sistema ahora rechaza explícitamente (en vez de propagar sin control) cualquier CVU o CBU que no tenga el formato correcto (22 dígitos numéricos), en los tres microservicios principales de Wallet. Endurece la integridad de datos de cara a normativa BCRA. Cambio de comportamiento: una integración que hoy envía datos mal formados empezará a recibir un error explícito en vez de un comportamiento indefinido aguas abajo.
- La consulta de una operación por su identificador externo ahora encuentra operaciones de hasta 6 meses de antigüedad (antes, solo 3 días).

**Mejoras funcionales:**
- Se completó la migración de infraestructura de mensajería del flujo de transferencias entrantes a un mecanismo más resiliente a fallas de conexión (ya cubría solo una parte del flujo, ahora lo cubre completo).
- El tiempo de espera para reconsultar el estado de una operación (pago con QR, transferencia saliente, DEBIN recurrente) ahora es configurable sin necesidad de un nuevo despliegue — funcionalidad todavía en pruebas de calidad al momento de esta publicación.
- Mejoras de resiliencia en el proceso diario de cuentas remuneradas (FCI) ante errores temporales del proveedor externo.

## 2026-08-12 — AD 71.2 FIX (PNET) (Adquirencia)

**Mejoras funcionales:**
- El proceso de carga masiva de deudas para ProvinciaNET ahora comprime los archivos de salida (evita fallos de descarga por tamaño) y puede procesar archivos de entrada comprimidos.
- Los archivos con datos mal generados que quedaban trabados indefinidamente en el proceso de carga masiva ahora se mueven automáticamente a una carpeta de fallidos, sin bloquear el resto de la cola.
- El historial de archivos procesados de la carga masiva ahora se archiva ordenadamente, liberando la carpeta de trabajo activo.

**Nota:** esta versión también incluyó cambios sobre el webhook de deudas y las devoluciones de Simple Button 2.0 (montoProximoVencimiento, integración con Carnot) — ya cubiertos en la entrada de novedades de producto correspondiente al release v71.2 (2026-08-10, vía minutas de reunión).

## 2026-08-10 — W 71.8 (PagosFX) (Wallet)

**Nuevos requerimientos:**
- Configuración de infraestructura en producción: se completaron hosts faltantes de varios microservicios de Wallet (Comprobantes, Consulta de Cuenta, Inversiones, Operaciones, Mastercard) y de la integración con Ardid. Cambio de configuración pura, sin impacto funcional para el usuario.

## 2026-08-10 — W 71.7 FIX (Wallet)

**Nuevos requerimientos:** alta de una nueva organización (PAFX) en producción.

## 2026-08-06 — W 71.6 FIX (Wallet)

**Nuevos requerimientos:** segunda etapa de la migración de autenticación externa (AuthExternal V2) a producción, cubriendo los servicios de Wallet.BIND y transferencias compartidas (SharedDebin).

## 2026-07-31 — W 71.5 FIX (Wallet)

**Mejoras funcionales:** ajuste de configuración menor en la app de demostración interna.

## 2026-07-30 — W 71.4 FIX (Wallet)

**Arreglos de errores:**
- El monto obtenido en una compra de Dólar CCL ahora se actualiza siempre que la operación se confirme, incluso cuando eso pasa el mismo día.
- Los comprobantes de cargo de Dólar CCL ahora quedan mejor identificados y expuestos correctamente en las consultas de la API.

**Nuevos requerimientos:** primera etapa de la migración de autenticación externa (AuthExternal V2) a producción.

## 2026-07-28 — W 71.3 FIX (Wallet)

**Nuevos requerimientos:** alta de 2 nuevas organizaciones en producción (HAPSA y una app de demostración interna para pruebas productivas de Bind PSP).

## 2026-07-23 — W 71.2 FIX (Wallet)

**Arreglos de errores:**
- Los reportes de movimientos ya no muestran el código de PSP en 0.
- Mejoras de infraestructura para distribuir mejor la carga entre servidores y reducir la sobrecarga de algunos nodos.

**Mejoras de rendimiento:** la consulta interna de días feriados dejó de pasar por un gateway externo, reduciendo errores de conexión y latencia.

**Nota técnica:** se llevó a producción una actualización mayor del componente que envía notificaciones (webhooks) a las organizaciones — incluye la base para soportar colas de mensajería más resilientes a futuro (todavía no activadas).

## 2026-07-22 — ARDID V 1.18.2.1 HF (Ardid)

**Arreglos de errores:** hotfix de motor antifraude (proveedor Ardid/Pentass): se agregaron reintentos automáticos a los procesos internos de validación de pagos y transferencias que en algunos casos tardaban demasiado en responder — mitiga (sin resolver la causa de fondo) el incidente del 2-3 de julio en el que operaciones válidas fueron rechazadas por una falla en el reinicio de los límites diarios de transferencias/pagos.

## 2026-07-16 — W 71.1 FIX (Wallet)

**Arreglos de errores:** mejora de resiliencia en el procesamiento de transferencias entrantes ante fallas de conexión internas.

## 2026-07-15 — W 71 (Wallet)

**Arreglos de errores:**
- Corregido el flujo de venta de Dólar CCL: ahora primero se acredita el monto obtenido y después se debita la comisión (antes exigía saldo disponible innecesariamente), y la comisión se calcula correctamente sobre el monto real obtenido.
- Mejorada la interpretación de errores del proveedor de cambio de moneda en compras y ventas de Dólar CCL, evitando que operaciones rechazadas queden mal clasificadas.
- Corregido el mapeo del identificador de contracargos de DEBIN, que guardaba el dato incorrecto.
- Corregido que eliminar una cuenta ahora también la deshabilita correctamente, evitando inconsistencias al intentar reactivarla.
- Las transferencias saliente ya no quedan "atascadas" en estado de espera indefinida cuando el banco responde que no encuentra la operación: pasado un margen de tiempo se rechazan automáticamente.
- Corregido un bug de duplicación de registros en el proceso de cuentas remuneradas (FCI).

**Nuevos comportamientos:**
- Nuevo endpoint para que Soporte pueda registrar manualmente un contracargo de DEBIN cuando no llegó por el canal automático.
- La consulta de cuenta por CBU/CVU/alias ahora puede devolver todos los cotitulares de la cuenta, no solo el primero.
- Los comprobantes ahora pueden crearse y consultarse también por su código, además de por su identificador interno — pensado para clientes que operan en varios ambientes con configuraciones distintas.
- El endpoint de totalizadores de Coelsa ahora también está disponible para el flujo de onboarding.

**Mejoras funcionales:** control de duplicidad reforzado para evitar comprobantes de Cobro QR interoperable repetidos.

## 2026-06-25 — WS 70.3 HF (Wallet)

**Arreglos de errores:** hotfix de configuración para el PSP de Cencosud (nuevo PSP 406): las consultas de cuenta por alias fallaban porque faltaban las credenciales del PSP en la configuración productiva — corregido. Aprendizaje operativo: todo PSP nuevo requiere ese alta de credenciales además de la configuración habitual.

## 2026-06-16 — WS 70.2.1 (Fix) (Wallet)

**Mejoras de rendimiento/confiabilidad:** se corrigió un caso en el que, ante una falla puntual de conexión a la caché (Redis) usada por el microservicio de Comprobantes, la operación seguía procesándose silenciosamente sin quedar con su comprobante asociado — y como no se generaba ningún error, el reintento automático nunca se disparaba. Ahora ese tipo de falla sí dispara el reintento correctamente. Alcance validado por QA: transferencias entrantes externas.

## 2026-06-10 — WS 70.2 (Wallet)

**Arreglos de errores:**
- Corregido un caso crítico donde ciertas transferencias internas devolvían error al cliente (HTTP 500) pero el dinero se debitaba igual de la cuenta origen, sin acreditarse en destino y sin avisar por webhook — quedaba "perdido" en tránsito desde la perspectiva del usuario. Causa: un nombre de contraparte demasiado largo rompía el guardado de la operación a mitad de camino.
- El cálculo de rendimiento (TNA) informado para cuentas remuneradas por FCI promediaba también los días en que el proceso había terminado con error, distorsionando el valor mostrado al cliente. Ahora esos días quedan excluidos del promedio.
- Al crear una organización de Wallet faltaba una especificación de habilitación para Ardid que había que cargar manualmente después del alta — ahora se crea automáticamente junto con el resto.
- El identificador de cuenta del webhook que avisa la deshabilitación de una cuenta por contracargo de DEBIN sin saldo llegaba con un formato distinto (`IdCuenta`) al resto de los webhooks de Wallet (`cuentaId`) — corregido para que sea consistente.
- Primera etapa de un fix de confiabilidad en la generación de comprobantes: bajo ciertas fallas de conexión a caché, algunas operaciones podían quedar sin comprobante asociado y sin reintento automático. Este ticket cubrió una de las dos rutas internas afectadas; la segunda se completó en la versión siguiente (70.2.1, ver arriba).

**Mejoras de rendimiento/confiabilidad:**
- Se mejoró el esquema de reintentos para el alta de cuentas y CVU de Wallet cuando la integración con Ardid responde con timeout, reduciendo los casos en que una cuenta quedaba sin sincronizar del lado de Ardid. Queda pendiente (deuda técnica reconocida) un mecanismo de reintento de mayor alcance para caídas prolongadas de Ardid.

## 2026-06-03 — WS 70.1 (Wallet)

Versión grande (26 tickets) — incluye el punto de partida del fix de confiabilidad de comprobantes que se terminó de cerrar en las dos versiones siguientes (ver 70.2 y 70.2.1 arriba), y varias mejoras de herramientas internas para Soporte.

**Arreglos de errores:**
- **Origen del fix de comprobantes sin generar** (ver también 70.2/70.2.1): se incorporaron reintentos automáticos ante errores de conexión (base de datos, caché, entre microservicios) en el flujo de generación de comprobantes, más un mecanismo de reintento de mayor alcance para fallos más persistentes. Esta primera versión no cubrió todos los casos — de ahí las dos rondas de ajuste posteriores.
- El webhook real que el banco envía al procesar un contracargo de DEBIN no coincidía con el formato que el sistema esperaba, lo que podía impedir identificar correctamente la operación afectada — corregido para tolerar el formato real, sin perder compatibilidad con el anterior.
- El alta automática de organizaciones de Wallet **nunca había funcionado correctamente en producción** (solo en el ambiente de pruebas) por una diferencia de configuración entre ambientes — corregido.
- El estado de un CVU podía mostrarse como habilitado en Wallet mientras ya estaba deshabilitado del lado del banco (tras una baja no registrada correctamente) — se refuerza la consulta al banco para evitar esa desincronización.
- A una organización nueva podía faltarle una especificación necesaria para que el análisis de DEBIN pase correctamente por el motor antifraude (Ardid) — ahora se crea junto con el resto en el alta automática.

**Mejoras funcionales:**
- Soporte ahora puede asignar (o quitar) manualmente la fecha de alta impositiva de una cuenta sin depender de un ticket a Fintexa, agilizando la resolución de reclamos de cálculo de impuestos.
- Nuevos endpoints internos para que Soporte pueda: deshabilitar/habilitar cuentas de forma masiva (antes era una por una), dar de alta un tipo de comprobante sin asociarlo a ninguna organización puntual (para ajustes), y gestionar el alta/baja/modificación de PSPs sin recurrir a scripts de base de datos.
- Nueva especificación para poder habilitar o deshabilitar puntualmente el Debin recurrente crédito de una organización específica, sin afectar el resto de su configuración.

**Mejoras de rendimiento/confiabilidad:**
- Corregido un caso de concurrencia donde el impuesto de una operación se calculaba y quedaba registrado, pero el comprobante de ese impuesto nunca se generaba — el cliente veía el cobro reflejado en sus liquidaciones pero sin comprobante asociado.

Además, esta versión trajo varios ajustes menores ya cubiertos por el seguimiento de iniciativas vivas de Producto (mantenimiento de FCI Cuenta Remunerada, contracargos de DEBIN recurrente, reactivación de transferencia pull) — ver `1_proyectos/` para el detalle de esas IDEAs.

## 2026-05-27 — WS 70 (Wallet)

**Mejoras funcionales (Pagos FX):** el alta de beneficiarios del exterior suma un paso de verificación del banco destino — un nuevo endpoint consulta a Mastercard la información oficial del banco (por país + BIC o nombre) y devuelve los datos estandarizados para completar el alta, reduciendo rechazos en la ejecución de pagos. Las consultas de movimientos ahora muestran también el beneficiario y el concepto de cada pago FX.

**Arreglos de errores:** se corrigió un incidente de FCI en producción causado por un despliegue incompleto de una mejora interna de mensajería (los componentes quedaron desalineados entre microservicios). El incidente expuso además una debilidad del proceso de deploy (dependencias entre servicios sin tag de versión), reconocida y corregida por el proveedor.

## 2026-05-21 — Portal 2.0 V1 y V2, Adquirencia (rollout de mayo, ingestado retroactivamente el 2026-08-15 por un gap del backfill anterior)

**Arreglos de errores (rollout de Portal 2.0, incluye variante Mayorista):**
- Login bloqueado incorrectamente por reCAPTCHA para usuarios con VPN activa, pese a tener credenciales válidas.
- Usuarios recién creados con rol Administrador no obtenían el menú completo esperado.
- En el perfil Mayorista: no se podía asignar caja a un usuario Operador, la sección Transacciones no cargaba datos ni permitía devoluciones, y la sección QR daba error de carga.
- Transferencias con concepto distinto de "Varios" eran rechazadas incorrectamente.
- El saldo no se actualizaba después de un cobro con QR, impidiendo procesar la devolución correspondiente.
- Los PDF de liquidaciones exportados no podían abrirse.
- La columna de fecha de devolución quedaba vacía al exportar transacciones a Excel.
- En el Portal Web de Pagos al Exterior: la etiqueta de tipo de cuenta bancaria del beneficiario no distinguía correctamente entre los distintos formatos internacionales (IBAN vs. BAN), y el filtro de país en la búsqueda de beneficiarios quedaba pegado entre sesiones.

**Mejoras funcionales:** ocultar detalles de comisión/neto/retención en las vistas de perfil Mayorista (esa información no corresponde a ese nivel de usuario); a pedido de un cliente con gran volumen de sucursales, el filtro de sucursales ahora puede ordenarse alfabéticamente.

## 2026-05-20 — WS 69.4 HF (Coppel) (Wallet)

**Nuevos comportamientos:** hotfix dedicado exclusivamente a dejar operativa la funcionalidad de **Cuenta Remunerada por FCI para Coppel** en producción (configuración de la organización, código de fondo, credenciales contra el broker y habilitación de cuentas comitentes). Con esto Coppel quedó habilitado a remunerar los saldos de sus cuentas.

## 2026-05-13 — WS 69.3 HF (Tin) (Wallet)

**Arreglos de errores:** hotfix para TIN — a algunos usuarios se les descontaba correctamente un viaje QR de colectivo pero el viaje quedaba registrado internamente como "en proceso", por lo que la app les seguía mostrando una deuda que ya habían pagado (y podía bloquearles nuevos viajes). Corregida la sincronización de estados; validado con pruebas de stress.

## 2026-05-12 — WS 69.2 HF (PLD) (Wallet)

**Arreglos de errores:** hotfix de cumplimiento normativo — las operaciones creadas justo en el filo de la medianoche (23:59:59) quedaban fuera del archivo diario de operaciones para PLD de ese día **y también del siguiente**, generando diferencias entre los archivos reportados y la base real. Corregido el corte horario.

## 2026-05-05 — WS 69.1 Fix (Contracargo Debin Recurrente) (Wallet)

**Arreglos de errores** (ambos sobre la funcionalidad de contracargos de DEBIN recurrente, entonces recién lanzada — iniciativa PRD-140):
- Cuando un contracargo llegaba y no se podía debitar nada del cliente (saldo cero), la organización **no recibía ningún aviso** — ahora el webhook se envía siempre, indicando que quedó un débito pendiente.
- Cuando se lograba debitar solo una parte, la operación no cambiaba de estado — ahora pasa correctamente a "Devuelta parcial" (y a "Devuelta" al completarse el total, ya sea en línea o por cobros posteriores automáticos).

⚠️ Ambos fixes se validaron con flujo simulado en el ambiente de pruebas; la validación con el flujo productivo completo quedó pendiente al momento de la publicación (✅ luego confirmada exitosa por el PM, 2026-07-09).

## 2026-04-29 — WS 69 (Wallet)

Versión mayor (43 tickets). **Hito de producto: quedó publicado el corazón de Pagos FX** — desde esta versión una organización habilitada puede ejecutar pagos al exterior de punta a punta.

**Nuevos comportamientos:**
- **Ejecutar Pago FX end-to-end**: con una cotización vigente, un beneficiario validado y la declaración jurada, el pago retiene los fondos en pesos, compra los dólares (CCL) en línea y dispara el pago internacional por la red de Mastercard — con reversa automática de fondos si la compra de dólares falla. Conceptos de pago acotados a una lista normativa (honorarios, importación de bienes/servicios, regalías, etc.) y documentación respaldatoria adjunta. *Nota: al publicarse, el circuito completo estaba probado solo con el corredor Canadá modalidad B2B.*
- Webhook de resultado del pago FX (aprobado/rechazado con motivo), conciliación automática contra Mastercard cada 30 minutos, y APIs de consulta (pagos, movimientos, beneficiarios, corredores habilitados).
- **Los pagos con QR de Wallet ahora pasan por el motor antifraude (Ardid)** antes de ir a Coelsa, configurable por organización y transparente para el cliente; si el pago falla o se devuelve por completo, Ardid queda consistente.
- Nuevo webhook para las organizaciones que usan cobro automático de deudas (Recycle): aviso inmediato cuando un cobro queda **pendiente** por falta de saldo (antes solo se avisaba al concretarse), más un endpoint para consultar todas las deudas pendientes por cuenta.
- Soporte de Bind PSP ahora puede **revertir la eliminación de una cuenta** y **rehabilitar un CVU dado de baja** sin depender del proveedor, con auditoría de cada movimiento.

**Arreglos de errores:**
- **Impuestos cobrados de más en transferencias**: al no ser obligatorio informar el CUIT destino, las transferencias entre cuentas del mismo titular tributaban como si fueran de titulares distintos. Desde esta versión el CUIT destino es **obligatorio** en transferencias salientes (cambio comunicado a los clientes con un mes de aviso).
- **Saldos mal calculados bajo ráfagas de operaciones** (reclamo de Consorcio Abierto): corregido con un mecanismo de concurrencia más robusto en la generación de comprobantes de impuestos.
- Transferencia pull: corregido un bug crítico que generaba **fondos sin respaldo** (una devolución automática indebida cuando la operación fallaba por falta de saldo).
- Contracargos de pagos QR que llegaban al extracto pero no se registraban en el sistema; y pérdida de trazabilidad de pagos QR cuando Coelsa fallaba (ahora el identificador se guarda antes de llamar a Coelsa).
- Cancelación de operaciones de dólar CCL: se construyó el endpoint, pero quedó **trabado en QA por un conflicto de estados con el proveedor bursátil (Poincenot)** — publicado sin cerrar.
- Reportes PLD: unificado el criterio de fechas entre los endpoints de generación de archivos (eran inconsistentes entre sí) y corregido un timeout.

## 2026-04-14 — WS 68.3 HF (Wallet)

**Nuevos requerimientos (configuración):** alta del PSP **CencoPAY** en producción y habilitación del flujo onboarding→wallet para dos organizaciones nuevas: **Coop Unión Justiniano Posse** y **GST** — tres clientes/configuraciones que entraron por hotfix operativo.

## 2026-03-11 — WS 68 (Wallet)

Versión grande (60 tickets). Trajo el **primer tramo de las APIs de Pagos FX** y una tanda importante de robustez.

**Nuevos comportamientos:**
- **Pagos FX — cotización y beneficiarios**: consulta de cotización compuesta (pesos→dólares→moneda destino, modalidades por monto origen o destino, expiración a 15 minutos), consulta de corredores habilitados, declaración jurada con identificador trazable, y validación de dirección y de cuenta bancaria del beneficiario contra Mastercard (verificación de titularidad incluida). También el nuevo microservicio orquestador del proceso.
- Soporte ahora gestiona los **aceptadores de QR** (alta/baja/modificación y asignación por organización) sin tickets al proveedor; un aceptador nuevo nace habilitado para todas las organizaciones.

**Arreglos de errores:**
- Cluster de robustez del circuito de impuestos (SISCRI): identificadores únicos de tipos de comprobante entre organizaciones, alta de personas por eventos con reintentos, razón social obligatoria para personas jurídicas, y habilitación de impuestos sobre comprobantes de sistema (caso MAX PAY, con riesgo normativo ARCA por retenciones no aplicadas).
- Confiabilidad de transferencias y comprobantes: devolución automática cuando la operación falla después de crear el comprobante (evita dinero debitado sin destino), primer mecanismo de "redelivery" para mensajes perdidos, y el monitor de estados pasa antes las operaciones trabadas a revisión manual.
- Cluster PLD: valores no numéricos y registros duplicados que rompían o distorsionaban los archivos de cumplimiento.
- El alta automática de organizaciones **nunca había funcionado en producción** por una diferencia de configuración entre ambientes — corregido.
- Conciliación directa contra Coelsa: validación de pertenencia del CVU, rango horario correcto y fechas opcionales.

## 2026-02-19 — WS 67.4 (Wallet)

**Nuevos comportamientos:** versión dedicada a **Pagos FX** — se publicó el "wrapper" completo de integración con Mastercard Move: 8 endpoints espejo (cotizaciones, confirmación, pago, consulta de pago, balance, validaciones de dirección y cuenta, guía de requisitos por corredor) más la autenticación segura contra Mastercard, consumibles internamente sin manejar credenciales. Un endpoint (notificaciones de cambio de estado) quedó publicado sin poder probarse. También un fix del cálculo de saldos del proceso diario de FCI.

## 2026-02-12 — WS 67.3 HF (Wallet)

**Mejoras de rendimiento/confiabilidad:** hotfix operativo — el monitor de estados de transferencias pasa a revisar las operaciones trabadas cada 1 hora (antes 3), para que caigan antes a resolución manual cuando Api Bank se cuelga.

## 2026-01-30 — WS 67.2 HF (Wallet)

**Arreglos de errores:** hotfix doble — (1) el alta de billetera vía onboarding podía confirmarse "exitosa" sin haberse creado el CVU realmente (quedaba una cuenta inutilizable que aparentaba estar bien); ahora queda en error y permite reintento. (2) El alta de cuenta comitente rechazaba requests válidos por exigir un dato que ya tenía.

## 2026-01-29 — WS 67.1 HF (Wallet)

**Arreglos de errores:** hotfix por reclamo de Consorcio Abierto — demoras de hasta una hora en la aplicación de los cálculos de impuestos de su organización.

## 2026-01-27 — WS 67 (Wallet)

Versión grande (50 tickets), fuerte en correcciones del día a día.

**Arreglos de errores:**
- Varios webhooks salían **sin el identificador del comprobante** (transferencias internas, DEBIN recurrente, contracargos QR) — primer capítulo de un problema de fondo que se terminó de resolver meses después.
- Un pago con QR podía responder **error al cliente y acreditarse igual** (caso BSF: el cliente devolvía la plata a su usuario y el pago después entraba — doble egreso). También se corrigieron cobros QR que fallaban cuando el vendedor era una billetera (faltaba un dato de sucursal) y un rechazo de Coelsa sin mapear ("adquiriente deniega operación", casos Maxiconsumo/Tienda Júbilo).
- **Impuestos**: la devolución de una transferencia no devolvía el impuesto cobrado (corregido); los webhooks de impuestos se normalizaron al formato estándar.
- **Ventas de dólar CCL exitosas no se notificaban** a las organizaciones (solo los rechazos) — corregido.
- Altas de cuenta: dos solicitudes simultáneas con el mismo CUIL podían crear cuentas duplicadas (se agregó bloqueo); en BANZA el onboarding no asignaba alias (configuración faltante); y se descubrió que si una organización no tiene configurado el motor antifraude, sus cuentas tampoco se daban de alta en el sistema de impuestos (acoplamiento no evidente).

**Mejoras funcionales:** las consultas de movimientos exponen el identificador de red (Coelsa) con nombre unificado; la cotización CCL usada por PIX pasó a configurarse por organización; los parámetros del proceso diario de FCI se cambian por base de datos sin necesidad de deploy; y el endpoint de consulta directa a Coelsa quedó gobernado (habilitación por organización — solo Astropay — y conteo de uso para facturarlo aparte).

**Mejoras de rendimiento:** creación de transferencias más rápida (consulta optimizada + menor espera de reconsulta) y primera adopción de una librería de mensajería más performante en el servicio de comprobantes.

## 2026-01-21 — WS 66.4 HF (Wallet)

**Arreglos de errores:** hotfix operativo — alta manual masiva de todos los tipos de comprobante de todas las organizaciones en el sistema de impuestos (el mapeo automático recién llegaría meses después).

## 2026-01-15 — WS 66.3 HF (Wallet)

**Arreglos de errores:** hotfix — resolución masiva de operaciones que quedaban colgadas en estado "a consultar" por caídas de Api Bank; primer capítulo de un patrón que se formalizó más adelante.

## 2026-01-08 — WS 66.2 HF (Wallet)

**Arreglos de errores:** hotfix por reclamo urgente — Coelsa empezó a exigir un dato de sucursal que Wallet no enviaba, rompiendo los cobros con QR en ambiente de pruebas desde fin de año. Precursor del fix definitivo que llegó en W 67.

## 2025-12-18 — WS 66.1 (Wallet)

**Arreglos de errores:** un hotfix de webhooks de transferencias entrantes (BANZA) perdió un campo tras un deploy previo — corregido. Se afinó la información con la que se registran transferencias conciliadas por consulta directa a Coelsa, y se corrigió el cálculo del monto a suscribir/rescatar en FCI (contaba ganancia de más).

## 2025-12-15 — WS 66 (Wallet)

Versión de estabilización post-lanzamiento (20 tickets).

**Nuevos comportamientos:** Ardid suma un segmento de "cliente menor" con graduación automática a estándar al cumplir 18 años, sin intervención manual — soporte de Cuentas para Menores. Se agregó la posibilidad de reversar impuestos ya calculados, y de recibir devoluciones de pago en PIX Rol Emisor (funcionalidad que originalmente se había descartado del MVP por bajo volumen esperado).

**Arreglos de errores:** un endpoint nuevo de integración con Ardid no devolvía el identificador creado; una regresión impedía dar de alta CVUs en Ardid; el vencimiento real de una operación de cripto no coincidía con lo informado (lo fija el proveedor dinámicamente, no un valor fijo); pagos QR quedaban todos "iniciados" sin resolverse por una falla de Api Bank; un rechazo de Coelsa quedaba sin traducir; liquidaciones de impuestos dejaban de enviarse al sistema fiscal; y la declaración jurada de cambio de divisas mostraba mal el nombre del proveedor en un caso puntual.

**Mejoras funcionales:** se sentó la regla general de manejo de excepciones en los consumers de eventos (base de la mejora de confiabilidad de meses siguientes), y se reordenó/adelgazó el proceso interno de creación de comprobantes (toca todos los flujos: recycle, PIX, transferencias, cripto, CCL, viajes QR, impuestos). Nuevo endpoint operativo para que Soporte reprocese viajes QR con comprobante pero sin operación registrada.

## 2025-12-05 — WS 65.2 (Wallet)

**Arreglos de errores:** el cálculo de ganancia diaria de FCI daba un resultado inflado por un error de fórmula (faltaba restar 1); el proceso diario de FCI se rompía por un nombre de columna mal referenciado; y el paso de copia de saldos a veces no se ejecutaba, dejando cuentas con el saldo del día anterior. Se agregó también un campo de control para excluir del cálculo de impuestos a los comprobantes que deben chequearse contra el padrón SIRTAC.

## 2025-11-26 — WS 65.1 (Wallet)

**Nuevos comportamientos:** primeras piezas de Cuentas para Menores — alta de cuenta y aprobación por parte del tutor. El contrato de los webhooks de operaciones se amplía con el identificador del comprobante y fechas de creación/actualización — sienta las bases para que las organizaciones puedan relacionar operación↔comprobante↔impuesto, un problema recurrente en meses siguientes.

**Arreglos de errores:** no se generaban los comprobantes de venta y cargo del circuito de dólar CCL; y el proceso diario de FCI remuneraba cuentas que ya habían sido rescatadas (el estado no se actualizaba entre corridas).

## 2025-11-17 — WS 65 (Wallet)

**Lanzamiento del espacio Wallet en Jira.** Primera versión publicada con tracking formal.

**Nuevos comportamientos:** motor de compra/venta de criptomonedas (proveedor Lirium) con el caso DIRECTA (expatriación de fondos vía cripto para casas de apuestas, compliance-driven); motor general de Recycle V2 (cobro automático de deudas pendientes) con sus pasos de manejo de errores/reintentos y actualización diaria de estado; webhook de aviso de comprobante para cobro QR interoperable.

**Arreglos de errores:** cuentas nuevas nacían deshabilitadas pese a que el alta respondía éxito (reclamo Gallo/Banza); el saldo no se reflejaba de inmediato tras crear un comprobante (reclamo Astropay); ajustes de cálculo y webhook en el proceso diario de FCI.

**Otros:** segunda fase del pentest mobile de la app (sin detalle técnico adicional accesible).

---

> ⚠️ **Nota de orden**: las entradas de **Adquirencia (AD)** que siguen se agregaron en bloque el 2026-07-13 (backfill vía export XML) y están en orden cronológico inverso **entre sí**, pero no están intercaladas por fecha con las entradas de Wallet de arriba — para eso ver [`log_versiones_publicadas.md`](log_versiones_publicadas.md), que sí tiene la fecha real de cada versión de ambos espacios.

## 2026-07-02 — AD 70.2 (Adquirencia)

**Arreglos de errores:** un contracargo QR sobre una cuenta Wallet sin saldo suficiente quedaba pendiente para siempre en vez de rechazarse — ahora Wallet informa el motivo real y el contracargo pasa a Rechazado (aunque el Admin todavía no le muestra ese motivo al comercio). Corregida también la sincronización del nombre de una caja hacia Coelsa/ApiBank tras editarlo, y un problema de acceso al portal comercio productivo.

## 2026-06-24 — AD 70.1 (Adquirencia)

Versión más grande de Adquirencia en todo el período relevado (26 tickets).

**Nuevos comportamientos:** se lanzó el **Portal Web de Pagos FX** — plataforma propia para que un cliente cargue beneficiarios, haga pagos al exterior y consulte su historial sin integrarse por API (dashboard, gestión de destinatarios, módulo de operaciones). El Ministerio de Justicia suma un flujo de POS que levanta automáticamente la orden de venta pendiente de la caja para cobrarla. Nuevo filtro por código de comercio en la API de links de pago (pedido de RIPSA).

**Arreglos de errores:** ajustes de UX en el Portal de Pagos FX (indicadores de carga duplicados, cartel de "operación en proceso" que desaparecía muy rápido).

**Otros:** la habilitación de PRISMA como procesador de POS desde el Admin sigue **bloqueada** — persisten incompatibilidades entre los nuevos requisitos de alta de comercio de los procesadores y el modelo de configuración actual.

## 2026-06-23 — AD 70.1 FIX (Adquirencia)

**Arreglos de errores:** hotfix — el endpoint de consulta de transferencias de Recaudación por Transferencia no devolvía resultados para transferencias recibidas.

## 2026-06-04 — AD 70 (Adquirencia)

**Nuevos comportamientos:** el Ministerio de Justicia ahora puede asociar productos a transacciones que provienen de una Orden de Venta (no solo de Deuda).

## 2026-05-27 — AD 69.3 HF (Vupra) (Adquirencia)

**Arreglos de errores:** hotfix dedicado — error en pago de Botón Simple 2.0 para el cliente Vupra.

## 2026-05-11 — AD 69.2 HF (Fixes Canales: POS) (Adquirencia)

**Arreglos de errores:** hotfix del rediseño de canales de cobro — el alta de POS con arancel reducido pedía datos indebidos (teléfono, fecha de nacimiento) y bloqueaba el alta; un alta con arancel reducido no quedaba realmente reflejada en el procesador; y reprocesar un canal con error no lo dejaba habilitado.

## 2026-05-07 — AD 69.1 HF (Adquirencia)

**Arreglos de errores:** hotfix — transacciones de Recaudación por Transferencia con fecha de liquidación errónea.

## 2026-04-29 — AD 69 (Adquirencia)

**Nuevos comportamientos:** el Ministerio de Justicia puede ver el detalle de productos en la consulta de Deuda, devolver una deuda vencida que tuvo pago parcial, y considerar pagos hechos después del vencimiento de la deuda. Automatización vía SFTP de la carga masiva de deudas para el cliente ProvinciaNET (antes manual).

**Arreglos de errores:** ajustes menores de Admin (falta botón para eliminar convenios, búsqueda de Collector en transferencias por CBU), UX de Botón de Pago (validación de DNI, maquetación en la pasarela de un cliente), y de webhooks (estado de deuda mal informado tras pago por transferencia).

## 2026-04-24 — AD 68.5 HF Vupra (Adquirencia)

**Arreglos de errores:** hotfix — error en pago de Botón Simple 2.0 cuando dos deudas compartían el mismo CVU.

## 2026-04-23 — AD 68.4 HF Favacard (Adquirencia)

**Arreglos de errores:** hotfix — tras una migración de comercio (Favacard), se veían transacciones de otras cajas.

## 2026-04-14 — AD 68.3 HF (Adquirencia)

**Arreglos de errores:** hotfix — liquidaciones de Recaudación por Transferencia con resultados en null.

## 2026-04-06 — AD 68.2 HF (Adquirencia)

**Arreglos de errores:** hotfix — webhook de Recaudación por Transferencia con error por falta de un dato de referencia.

## 2026-04-01 — AD 68.1 HF (Adquirencia)

**Arreglos de errores:** hotfix — webhooks de Recaudación por Transferencia que no se estaban enviando.

## 2026-03-30 — AD 68 (Adquirencia)

Versión grande (39 tickets).

**Nuevos comportamientos:** nace la funcionalidad de **asociar productos a una transacción** (Deuda u Orden de Venta) para el Ministerio de Justicia — el detalle de ítems viaja hasta el webhook de pago y queda consultable. Se agregó mostrar el código externo al crear una orden de venta o caja (cliente Hipódromo de Palermo).

**Arreglos de errores:** el CVU de una deuda no se daba de baja cuando pasaba a pagada o vencida; un pop-up viejo quedaba visible al transferir un monto menor al esperado; corregido el importe a debitar al comercio en devoluciones de Eco Cerrado; canales de cobro POS que quedaban con datos vacíos al asignarse; y una serie de bugs de Alta de Entidad (Siscri, validación de campos).

## 2026-03-04 — AD 67.6 HF (Adquirencia)

**Arreglos de errores:** hotfix — falta de webhook para el cliente La Virginia.

## 2026-03-03 — AD 67.5 [Canales + Fixes ADMIN] (Adquirencia)

Versión foco: el grueso del **rediseño de arquitectura de canales de cobro** (23 tickets) — la funcionalidad de habilitar/migrar/reintentar canales QR, POS y Botón Simple desde el Admin, reemplazando el modelo anterior donde la habilitación general de un comercio disparaba infraestructura de QR sin que correspondiera.

**Arreglos de errores:** el reporte de liquidaciones a nivel comercio no se generaba; el CSV/reporte de transacciones no mostraba el identificador de Split; cambiar sucursal/caja en un canal de Botón Simple daba error 500.

## 2026-02-19 — AD 67.3 (Adquirencia)

**Arreglos de errores:** varios bugs generales de Orden de Venta, encontrados por el cliente GST antes del release principal de códigos externos — una orden de venta vencida podía pagarse igual si el QR se había leído antes de vencer, y crear una nueva orden sobre la misma caja no expiraba la anterior (permitía pagar ambas).

## 2026-02-10 — AD 67.2 (Adquirencia)

Versión grande (30 tickets), con dos clusters de estabilización.

**Arreglos de errores:** cluster de bugs del webhook de contracargos/devoluciones para el cliente COTO (formato de fecha, estado informado incorrecto, contracargos parciales rechazados sin webhook). Cluster de bugs del objeto "Deuda" de Botón Simple 2.0 (consultas de devolución con error incorrecto, timer del checkout desfasado 3 horas). Se corrigió el mapeo invertido de importe neto/comisión en transacciones de Eco Cerrado.

**Nuevos comportamientos:** Eco Cerrado suma el comprobante de débito por impuestos y el endpoint de devolución. Un link de pago vencido ahora redirige a la URL de error configurada por el comercio (pedido de RIPSA).

**Otros:** quedó reconocida como deuda técnica la falta de un endpoint de devolución de Recaudación por Transferencia desde el sistema de Cobro (solo existe desde Financial).

## 2026-01-30 — AD 67.1 (Adquirencia)

**Arreglos de errores:** no se permitía intentar otra devolución de Recaudación por Transferencia si el estado había quedado en UNKNOWN; mejorado el mensaje de error al devolver una transferencia de otro Collector.

## 2026-01-20 — AD 66.3 HF (Adquirencia)

**Arreglos de errores:** hotfix dedicado — operaciones del cliente Fletalo colgadas en un estado intermedio de Botón 2.0.

## 2026-01-13 — AD 66.1 HF (Adquirencia)

**Arreglos de errores:** se sacó la validación de monto máximo para pagos QR, que bloqueaba indebidamente pagos de importes altos en caja.

## 2025-12-16 — AD 66 (Adquirencia)

Versión de lanzamiento del cluster **Botón Simple 2.0** en el tracking de Jira (46 tickets) — el grueso de bugs de sincronización del objeto "Deuda" con sus medios de pago (tarjeta, QR, transferencia).

**Nuevos comportamientos:** Eco Cerrado suma la creación de comprobante de crédito y el ajuste del endpoint de informar el cobro. Alcance base de devoluciones parciales para el cliente COTO (endpoint de consulta de contracargo, más información en el webhook).

**Arreglos de errores:** reportes del Admin con errores de formato (caracteres rotos, separador decimal incorrecto, orden de fechas invertido); webhooks de contracargo con campos mal mapeados.

## 2025-12-04 — AD 65.2 (Adquirencia)

**Arreglos de errores:** una operación creada por Swagger en Recaudación por Transferencia no figuraba en la base de Transacciones; archivos de PLD con errores; error en un cashout puntual (cliente Jugadón); hotfix de una versión de POS.

## 2025-12-01 — AD 65.1 (fix SISCRI PERSONA) (Adquirencia)

**Arreglos de errores:** hotfix dedicado — alta de persona en el sistema de impuestos (Siscri) para un cliente puntual (Pavetto).

## 2025-11-17 — AD 65 (Adquirencia)

**Lanzamiento del tracking formal de Jira para el espacio Adquirencia.**

**Nuevos comportamientos:** primer atributo de Botón Simple 2.0 (medio de pago tarjeta al crear un link). Continúa la migración a AccessManagement 2.0 (roles y permisos reutilizables).

**Arreglos de errores:** cola de ajustes menores de UX en POS y Admin/Portal (calendario, mensajes de confirmación, filtros de movimientos, legibilidad del comprobante por email).

---

## 2026-05-10 — ARD 1.18.2 (Ardid)

**Nuevos comportamientos:** entrega del proveedor Pentass — mejoras en controles y reglas de pagos, ráfagas de transferencias, reportes custom, e integración con la Lista de Informados de WorldSys.

## 2026-05-07 — ARD 1.16.3 HF (Ardid)

**Nuevos comportamientos:** a pedido de Bind PSP, el proveedor amplió la parametría disponible para configurar reglas de transferencias entrantes.

## 2026-02-12 — ARD 1.16.1 (Ardid)

**Arreglos de errores:** incidente de disponibilidad — todos los endpoints de Ardid respondían error 403 por una causa del lado de Bind PSP (no del proveedor); tardó cerca de tres semanas en resolverse de forma definitiva, con dos falsos cierres intermedios.

**Nuevos comportamientos:** entrega de versión del proveedor con migración completa de aprobaciones pendientes a MongoDB (reglas ML/IA/comportamentales/reputacionales/blacklist), unificación de colas de mensajería por módulo, y nuevo flujo de creación de usuarios en 3 pasos.

---

## 2026-06-17 — OB PJ 1.7.2 (Onboarding)

**Mejoras funcionales:** cola de mejoras UX sobre onboarding jurídico — sugerencia automática de dominio Gmail en el campo email, botón para asociar el CUIT de la empresa relacionada al representante legal, cambio de estado automático a "Vencida" para solicitudes que superan el plazo, y corrección del flujo de Representante Legal/Apoderado en iPhone.

## 2026-05-21 — OB Jurídico V1.7.1 (Onboarding)

**Arreglos de errores:** tanda grande (11 tickets) de incidentes de producción reportados por el cliente La Virginia sobre el onboarding jurídico — problemas para restablecer la clave del portal, error al ingresar domicilios sin número de puerta, límite indebido de un solo documento por beneficiario final, y una Razón Social marcada como obligatoria por error.

## 2026-04-06 — OB Jurídico V1.7 1 HF (Onboarding)

**Arreglos de errores:** hotfix — error puntual en el alta de onboarding jurídico para el cliente Octagon.

## 2026-02-20 — OB Jurídico V1.7 (Onboarding)

**Arreglos de errores:** correcciones en el backoffice de onboarding jurídico reportadas por el cliente La Virginia.

## 2026-02-02 — OB 2 HF (Onboarding)

**Arreglos de errores:** hotfix — error en la validación contra listas de Terrorista/PEP del proveedor Worldsys.

## 2026-01-28 — OB 1 HF (Onboarding)

**Arreglos de errores:** hotfix — error puntual en el alta de onboarding para el cliente Inter.

---

## 2026-06-04 — SER 1 (Servicios)

**Primera versión publicada del producto Servicios**, nacido del MVP de Pago Fácil (link de pago que busca la deuda del usuario en el sistema del proveedor sin requerir un id técnico previo).

**Nuevos comportamientos:** el link de pago ahora vence según la fecha configurada, mostrando un aviso claro si el usuario llega tarde; si se paga un monto mayor al de la deuda, se devuelve el total automáticamente; webhook dedicado que avisa a la Entidad cuando se confirma o rechaza el pago; esquema de reintentos tanto para confirmar el pago contra el proveedor externo como para las devoluciones, evitando que una operación quede indefinida.

**Arreglos de errores:** una entidad dada de baja podía seguir generando links de pago (corregido); el cargo de servicio no se reflejaba correctamente en el comprobante ni en el monto total mostrado al usuario; una serie de ajustes de UX encontrados en la homologación con el proveedor externo (formato de fecha, nombre del proveedor visible, mensajes de error más claros); y dos errores de reCaptcha que aparecían en producción al vencer un link o al consultar el estado de un pago repetidamente.

