# Integración de Ardid/Akurtech con los productos de Bind PSP

> Estado: en producción.

> Contenido destilado de 4 Epics de Notion sobre cómo Wallet, Adquirencia (Botón Simple/Centralizador) y SUR FINANZAS **consumen** Ardid como motor antifraude — a diferencia del resto de este módulo, que documenta a Ardid como producto del proveedor (manual técnico, catálogo de APIs). Este archivo documenta el lado Bind PSP de la integración: qué eventos se le informan, qué bugs surgieron y qué patrones de resiliencia se adoptaron.

## 1. Integración con Wallet — Transferencias (46 SP aprox., etiqueta `wallet back`/`wallet app`)

- **Transferencias salientes**: dos caminos de integración — vía "intención de transferencia" (2 pasos, con confirmación) y transferencia directa (sin intención). Ardid analiza la operación y responde si requiere 2FA adicional; Wallet interpreta esa respuesta para decidir si pedir el factor extra al usuario.
- **Transferencias entrantes**: también se informan a Ardid para su análisis (no solo salientes).
- **Sincronización de estado de cliente**: al crear un cliente, actualizar su segmento, o completar el alta, esos cambios se replican en Ardid (alta de cliente, actualización de segmento) para que el scoring de Ardid tenga la data actualizada.
- **Seguridad en la app**: se estableció como obligación pedir siempre la huella dactilar en una transferencia saliente desde la APK, y garantizar que exista al menos un método de seguridad configurado (biometría o PIN) tanto en iOS como Android — requisito de seguridad ligado directamente a la confianza del análisis antifraude de Ardid (sin un factor de autenticación fuerte del lado del dispositivo, el análisis de Ardid pierde valor).
- **Enmascaramiento de dato sensible por canal**: el CUIT destino se envía como string vacío en las llamadas a **APIs externas** de Ardid, y con el valor real solo en las llamadas **internas** — patrón deliberado de minimización de datos según de qué lado de la integración se está llamando.

### Bug crítico encontrado en regresión

**Se creaban reglas restrictivas en Ardid y las transacciones igual pasaban** — es decir, el motor antifraude podía estar configurado para bloquear cierto patrón de operación, pero el flujo de Wallet no respetaba esa restricción y la transacción se completaba de todos modos. Bug de alto impacto (bypass del control antifraude), detectado en regresión y validado en STG.

### Patrón de resiliencia — "esquivar" a Ardid

Dos reglas explícitas de fallback cuando Ardid no puede responder bien:
- Si Ardid responde error 500 en una transferencia saliente, el flujo debe seguir adelante sin bloquear la operación por la caída del proveedor.
- Si Ardid responde que el cliente no existe (por ejemplo, porque el alta en Ardid no llegó a sincronizarse), tampoco debe bloquear la transferencia.

**Lectura de riesgo**: es un patrón "fail-open" deliberado — prioriza la disponibilidad del servicio de Wallet por sobre el control antifraude cuando Ardid falla o está desincronizado. Coherente con el bug de reglas restrictivas de arriba: hay una tensión de diseño recurrente entre "no bloquear al usuario por una falla de un tercero" y "no dejar pasar operaciones que deberían frenarse".

## 2. Integración con Botón Simple / Centralizador (Adquirencia)

- **Endpoint "business rules" unificado**: se construyó un endpoint que centraliza la decisión de negocio consultando tanto a Ardid como al procesador de turno en una sola llamada (etiqueta `🐙 Centralizador`) — luego sufrió un refactor propio ("Refactor de Business Rules").
- **Wrapper de Ardid Analyze + NotRealized**: Centralizador expone un wrapper que llama tanto al endpoint de análisis de transacción de Ardid como al de "NotRealized" (marcar una operación que no llegó a concretarse, para que Ardid la considere en su scoring de comportamiento).
- **Alta automática de Entity en Ardid**: al crearse una entidad nueva en Centralizador, un evento dispara la creación de la Entity correspondiente en Ardid y la asociación entre ambas — mismo patrón de sincronización automática visto también del lado Wallet (§3).
- **Botón Simple**: ajustes puntuales — enviar comercio id y email a Ardid, contemplar PAN+fecha de expiración en el hash de tarjeta (para que Ardid pueda identificar reintentos con la misma tarjeta), adaptar el llamado a Business Rules + Ardid tanto en el analyze como en el NotRealized al momento del pago, y crear el link de pago informando DNI/email/idExternoCliente (más datos de identidad = mejor análisis antifraude por parte de Ardid).

### 2.1 Extensión de cobertura a Post/POS (2026-07-30, en definición)

> Fuente: reunión "Análisis COBRO" (2026-07-30), minuta Gemini.

A la fecha, el monitoreo transaccional de Ardid en Adquirencia cubre solo **Botón Simple 1.0 y 2.0** — no el canal **Post (punto de venta físico)**. El equipo definió como objetivo sumar Post a la cobertura para mejorar las métricas de monitoreo, reutilizando el mismo patrón ya construido para Botón Simple: llamar a la API `analyze` de Ardid antes de enviar la operación al procesador, y a `NotRealized` para los pagos rechazados posteriormente — asegurando que se persistan los identificadores de transacción en ambos casos. Sin ticket ni fecha formal todavía; queda como intención de roadmap del área de Cobro.

## 3. Integración con SUR FINANZAS

Mismo patrón de integración que Wallet pero para la plataforma white-label SUR FINANZAS (ver [transversal/sur_finanzas.md](../ecosistema_wallet_adquirencia/sur_finanzas_multi_comercio.md)): alta de clientes en Ardid, análisis de transacción (Analyze) y de operaciones no concretadas (NotRealized), e "IntenciónTransferencia" con envío de OTP como parte del circuito.

## 4. Bóveda (Botón Simple) — integración y gap de visibilidad

Se integraron los pagos de "Bóveda" (guardado de credenciales de pago recurrente en Botón Simple) al análisis de Ardid.

- **Bug de visibilidad**: los pagos de Bóveda de Botón Simple no se visualizaban en el portal de Ardid — se analizaban pero no aparecían en el dashboard operativo, limitando la capacidad de un analista de revisar esas transacciones puntualmente.
- Bug relacionado no resuelto (marcado "No aplica" al cierre): error al intentar realizar un ingreso de dinero (Cash In) — sin causa raíz documentada en el ticket.

## 5. Cluster de bugs — "Reparar Ardid+Wallet: Alta de cuentas y de segmentos" (50 SP estimados)

Epic de estabilización dedicada exclusivamente a la sincronización de alta de cuentas/segmentos entre Wallet y Ardid — evidencia de que esta integración tuvo una segunda ronda de arreglos después del desarrollo inicial (§1):

- **Error 400 "Falta enviar entityCode"**: llamadas a Ardid sin un dato obligatorio.
- **`CreateProduct` usa un `name` incompleto** (bug de payload, sin más detalle).
- **No se creaban `ClientType` ni `ClientProduct` en Ardid al crear una cuenta de Wallet** — la cuenta quedaba dada de alta en Wallet pero incompleta del lado Ardid, replicando el patrón de desincronización que motivó el fallback "esquivar si el cliente no existe" (§1).
- **Concatenar "Wallet" al final del nombre de la Entity en Ardid**: para poder distinguir, dentro del mismo Ardid, entidades que operan en más de un producto de Bind PSP (Wallet vs. Adquirencia vs. SurFin) bajo el mismo nombre comercial.
- **Separar los parámetros de activación** de "creación de cuentas" y de "transferencias salientes" — antes de este fix, activar una función activaba la otra también, sin poder habilitarlas de forma independiente por organización.
- **Crear un segmento en Wallet debe reflejarse en Ardid** — mismo patrón de sincronización de segmento que en transferencias (§1), pero para el alta del segmento en sí.
- **Informar email en el análisis de transferencia** (`analyze transfer`) — dato adicional de identidad enviado a Ardid para mejorar el scoring.
- **Alta de parámetros de Ardid al crear una organización**, dividida en 2 partes de desarrollo — mismo patrón de "setear organización en Ardid" que aparece repetido como ticket separado, sugiriendo que este paso de configuración inicial se fue completando de forma incremental.

## 6. Discovery nunca construido — datos de localización/dispositivo (35 SP estimados entre las 2 Epics)

Dos Epics quedaron en **Status "Discovery - Priorización"** (nunca pasaron a desarrollo — todos sus tickets quedaron en estado "Pendiente"):

- **Ajustes Ardid+Wallet: Informar datos de localización en operaciones** (20 SP estimados). Origen del pedido: un requerimiento de cumplimiento/investigación (probablemente PLAFT) que pedía poder responder con datos que el sistema todavía no exponía — direcciones IP de conexión con fecha/hora y huso horario regional, producto asociado a la cuenta investigada y domicilio de recepción, medio/dispositivo/software usado para operar, y geo-referencia al momento de cada conexión. Nunca se priorizó su desarrollo.
- **Ajustes Ardid+Botón: Informar localización e informar devoluciones** (15 SP estimados, 3 tickets sin contenido más allá del título — plantillas vacías, nunca refinadas): agregar el motivo en el evento "NotRealized" que Botón Simple informa a Ardid, informar el "return" al momento de devolver una transacción, e informar IP y dispositivo — mismo objetivo que la Epic de Wallet (§ arriba), pero para el circuito de Botón Simple/Adquirencia.

**Lectura**: ambas Epics muestran que el enriquecimiento de contexto (IP, dispositivo, geo-referencia) que ya se pedía para Wallet en 2024 nunca llegó a implementarse ni para Wallet ni para Botón Simple — queda como gap de producto abierto, no como funcionalidad ya resuelta.

### 6.1 Tarea abierta — mapeo de motivos de rechazo hacia Onboarding (2026-08-21)

> Fuente: Reunión "Producto" (2026-08-18), minuta Gemini.

En la reunión "Producto" (2026-08-18) se acordó mapear específicamente los motivos de rechazo que hoy informa Ardid, para poder comunicarle al usuario final de Onboarding una razón concreta en vez de un mensaje genérico. La tarea quedó asignada a Nicolás Colón: mapear los motivos de rechazo de Ardid basándose en la información que provee Wallet (ver tarea T-006 en el `tareas.md` personal de Nicolás). Es un límite de producto distinto del gap de arriba (§6, datos de localización/dispositivo pedidos desde 2024 y nunca desarrollados) — ambos son huecos de UX/observabilidad sobre el mismo circuito de integración Wallet↔Ardid↔Onboarding, pero este es una tarea activa en curso, no un discovery abandonado.

## 7. Integración con Pagos QR de Wallet (IDEA Jira PRD-115, Finalizada — Go Live 2026-04-28)

Extiende el control antifraude de Ardid (§1, hasta entonces limitado a transferencias) al canal de **Pago QR**, que hasta este desarrollo permitía cashouts de cuentas Wallet sin pasar por Ardid — motivado por un fraude real detectado por ese canal descontrolado.

- **Mecánica**: antes de impactar en Coelsa, el Pago QR se manda a analizar en Ardid vía el mismo endpoint `/Analyze` que ya usan las Transferencias, con un `scope` propio ("4") para diferenciarlo. Parametrizable por Organización (tabla `dbo.Especificaciones`) para poder des/habilitarlo selectivamente.
- **Mismo patrón fail-open que transferencias (§1)**: si Ardid responde que el cliente no existe (no está replicado en Ardid), el pago sigue su flujo normal sin bloquearse — para no cortar la operatoria de organizaciones que aún no están en Ardid.
- **NOT_REALIZED**: se informa a Ardid cuando el Pago QR falla en Coelsa, queda inconcluso, o sufre una devolución **TOTAL** (una única devolución total, o varias parciales que en conjunto suman el 100%). Las devoluciones parciales que no llegan a completar el 100% del importe no disparan NOT_REALIZED — decisión de alcance explícita para simplificar el desarrollo, dado el bajo volumen de devoluciones parciales.
- **Resiliencia**: reintentos ante timeout de Ardid hasta obtener 200 OK.
- **Rollout**: quedó operativo automáticamente para todas las organizaciones; único paso manual pendiente es que Integraciones cree el scope en Ardid por organización nueva (ya solicitado a Ardid automatizarlo).
- Story points estimados: 5.

## 8. Incidente de disponibilidad — todos los endpoints de Ardid respondiendo 403 (vía `/sync_releases`)

> Fuente: Jira, [ARD-3](https://bindpsp.atlassian.net/browse/ARD-3), publicado en la versión **ARD 1.16.1** (Jira; no confundir con el release del proveedor documentado en [historico/historial_versiones.md](historico/historial_versiones.md), que es el mismo número de versión pero otro tipo de entrega). Todas las APIs de Ardid empezaron a devolver 403 — el reclamo a Ardid confirmó que sus propios swagger respondían bien, **la causa era del lado de Bind PSP**. Tras dos rondas de "ya está resuelto" que resultaron falsas (el problema reapareció), se confirmó la resolución definitiva casi 3 semanas después del reporte inicial (12-ene a 23-ene-2026), validada con una regresión completa Wallet+Ardid.

## 9. Hotfix — ampliar reglas de transferencias entrantes (vía `/sync_releases`)

> Fuente: Jira, [ARD-20](https://bindpsp.atlassian.net/browse/ARD-20), publicado en **ARD 1.16.3 HF** (2026-05-07). Pedido a Pentass (ticket Pentass #1518) para ampliar la parametría disponible al crear reglas de **transferencias entrantes** — desplegado primero en Staging y luego en Producción.

## 10. Versiones de publicación — línea de tiempo Jira (vía `/sync_releases`)

Las entregas del proveedor ya documentadas en [historico/historial_versiones.md](historico/historial_versiones.md) también quedaron trackeadas como tickets Jira propios de tipo "Historia" (sin contenido adicional más allá del informe de cambios ya transcripto ahí): [ARD-1](https://bindpsp.atlassian.net/browse/ARD-1) "Entrega de versión ARDID 1.16.1" (versión Jira **ARD 1.16.1**, 2026-02-12) y [ARD-23](https://bindpsp.atlassian.net/browse/ARD-23) "Entrega de versión ARDID 1.18.2" (versión Jira **ARD 1.18.2**, 2026-05-10). Espacio ARD backfill completo (4 tickets, 3 versiones) — vía export XML, 2026-07-13.

**Versión adicional confirmada vía `/sync_releases` (barrido incremental 2026-08-15):** [ARD-32](https://bindpsp.atlassian.net/browse/ARD-32) "Solicitamos aplicar fix de Ardid para resolver problemas de ejecución de los Stored Procedures en PROD" (versión Jira **ARDID V 1.18.2.1 HF**, releaseDate 2026-07-22) — solo atribución, sin contenido técnico nuevo en Jira más allá de la descripción de la solicitud (adjunto PDF no accesible por API). Es el mismo hotfix ya documentado en §11 ("Incidente de reinicio de límites diarios y hotfix de reintentos de Pentass") — coincide la fecha de despliegue (miércoles 7:30am, 2026-07-22) y el objeto del fix (reintentos automáticos en los SP de Pagos y Transferencias). Ver §11 para la referencia cruzada inversa. Espacio ARD nuevamente al día tras esta versión.

## 11. Incidente de reinicio de límites diarios (2-3 julio) y hotfix de reintentos de Pentass

> Fuente: Reunión "Análisis de Riesgo - Ardid Actualización" (2026-07-17), minuta Gemini.

**Incidente:** el 2 y 3 de julio de 2026, el proceso automático que resetea a cero los límites diarios de transferencias y pagos falló porque las bases de datos no respondieron a tiempo (timeouts, no un error de aplicación). Al no reiniciarse los contadores, el sistema rechazó operaciones válidas interpretando que los clientes ya habían superado su tope diario, dejando miles de operaciones temporalmente pendientes. El equipo de Pentass resolvió el incidente puntual reiniciando los contadores manualmente.

> Ticket Jira de este hotfix: [ARD-32](https://bindpsp.atlassian.net/browse/ARD-32), versión **ARDID V 1.18.2.1 HF** (releaseDate 2026-07-22) — ver §10 para la atribución completa de versión.

**Hotfix (contingencia, no causa raíz):** Pentass agregó reintentos automáticos (hasta 3 intentos, con margen de espera adicional) a los stored procedures (SP) afectados antes de que tiren error. Rocío Díaz (Pentass) confirmó que el hotfix **no modifica tablas, columnas ni SPs existentes** — solo envuelve la ejecución con reintentos. Riesgo de despliegue calificado "amarillo" (no verde) porque toca los servicios principales de transacción y transferencia, aunque el cambio funcional sea mínimo. Plan de rollback: revertir a la versión anterior de la app (sin impacto en datos, ya que el hotfix no tocó la base). Despliegue por servidor (cluster de 3), sin caída total del servicio, ~30-60 min incluyendo regresión — miércoles 2026-07-22 a las 7:30am (ventana de menor transaccionalidad), con bypass de componentes durante el pase (práctica ya establecida).

**Riesgo señalado en la propia reunión (Pablo Gomes, PM):** el hotfix trata el síntoma, no la causa. Si el SP sigue dando timeout en los 3 reintentos, el problema persiste igual. Acción acordada: avisar a Rocío Díaz que es probable que el problema de fondo reaparezca.

**Causa raíz aún abierta:** picos de CPU y timeouts de base de datos que aparecieron después de la actualización a la versión 1182 del proveedor, agravados por mayor volumen transaccional. Pentass (Osmel Mata) mitigó parcialmente agregando índices, pero la investigación de performance sigue abierta. Hernán Clarich (CTO) propuso llevar un seguimiento de qué "reglas duras" (hard rules) se van agregando en Ardid, ya que una regla sin índice de soporte podría estar entre las causas del degrade de performance.

**Nota aparte (mismo hilo, mejora ya en curso, no parte de este hotfix):** Pentass confirmó que ya modificó adquirente y emisión para que las operaciones sigan cursando aunque Ardid deje de responder (antes el ecosistema quedaba "acéfalo" sin Ardid) — pruebas terminadas la semana previa a esta reunión, a desplegarse en el próximo release conjunto de Aceptador y Wallet.

### 11.1 El problema reapareció como advirtió el PM — contadores mensuales, no solo diarios (2-17 julio)

> Fuente: Mail "Restauración Contadores Mensuales" — Mateo Capitanich (Pentass, Servicios de Seguridad), 2026-07-17, con seguimiento de Rocío Revelli (Bind PSP).

Pentass envió un informe formal (`260717_Informe_Recuperacion_Contadores.pdf`, no leído — ver limitación de adjuntos) sobre la restauración de los **contadores mensuales** (no solo diarios, ver §11) de Transferencias enviadas y recibidas. Rocío Revelli (Bind PSP) sumó la cronología real de idas y vueltas, que confirma la advertencia del PM en la reunión del 17/07 (§11: *"si el SP sigue dando timeout... el problema persiste igual"*):

- **2/7:** Bind reporta que los acumuladores diarios no estaban funcionando — se quita el rechazo de las reglas (queda solo alertando, sin bloquear operaciones).
- **3/7:** los contadores corren de forma manual — se vuelve a prender el rechazo en las transacciones.
- **Lunes 13/7 (tarde):** el problema reaparece — se vuelve a apagar el rechazo en las reglas.
- **Viernes 17/7:** se vuelve a prender el rechazo en las reglas (mismo día del informe de restauración de Pentass y de la reunión de §11).

**Lectura:** entre el 13 y el 17 de julio, Bind PSP operó **~4 días con el rechazo por límites desactivado** (solo alertando) mientras el problema de fondo de performance/timeouts de base (mismo origen que el incidente de límites diarios de §11) persistía. No hay confirmación en este mail de que la causa raíz (picos de CPU post-actualización a la versión 1182, ver §11) ya esté resuelta — el hotfix de reintentos recién se despliega el 2026-07-22.

## 12. Bug de alta de organización — API de Ardid no registra tipo/categoría/producto correctamente (postergado a v72)

> Fuente: reunión "Análisis de riesgos - W 71.6" (2026-08-05), minuta Gemini.

Falla identificada en producción en los endpoints de **API Product** de Ardid: al dar de alta una **organización nueva**, no se registra correctamente el **tipo, categoría y producto** requeridos. El fix ya está desarrollado, pero quedó empaquetado junto con el resto de cambios de la versión 72 (actualmente en Staging) — no se puede desplegar de forma aislada sin conflictos, y el equipo decidió **no forzarlo como hotfix** (el hotfix inyecta código directo a producción sin pasar por las validaciones de Staging, lo cual no se justificaba para un caso de baja frecuencia como creación de organizaciones nuevas).

**Decisión y workaround temporal:** postergar el fix a la v72 (próxima semana). Mientras tanto, cuando el equipo de integraciones cree una organización nueva, debe **avisar al equipo técnico para completar manualmente** el alta de tipo/categoría/producto en Ardid — Gonzalo Rivera comunicó este proceso temporal al grupo de integraciones.

Esta falla es independiente del despliegue del mismo día del servicio de autenticación externa (migración a Auto External v2, continuación de la iniciativa de infraestructura ya documentada — ver `wallet/otros_manuales.md §12`); ambos tickets se evaluaron juntos en el mismo análisis de riesgo pero se desacoplaron para el pase a producción.

## 13. Premisa de robustez "100% por Ardid" y contingencia ante caídas (discovery de diseño, 2026-08-11)

> Fuente: Reunión "Productos - Weekly Seguimiento" (2026-08-11), minuta Gemini (Luciana Rudaz, Pablo Gomes, Nicolás Colón) — sesión de foco de Nicolás Colón (Ardid), documentada acá por relevancia transversal a Wallet.

Nicolás Colón presentó una hoja de ruta de robustez para lo que resta del año, con 2 puntos centrales debatidos en la reunión:

- **Replicación del 100% de las cuentas de Wallet en Ardid:** hoy el error "cliente no existe" ocurre porque no todas las cuentas están dadas de alta en Ardid al momento de monitorear una operación. Diseño propuesto: un endpoint dedicado para reprocesar altas fallidas (más allá del reintento único que ya existe), usado tanto por el conciliador (sincronización constante) como manualmente si hace falta.
- **Contingencia para cuando Ardid no puede analizar una operación:** hoy, si el análisis falla, la operación se procesa igual del lado de Wallet pero **se pierde para siempre la estadística de fraude** (nunca se reintenta el análisis). Diseño propuesto: tabla intermedia que registre las operaciones no analizadas para reprocesarlas después, con reintento automático antes de insertar en la tabla (para no llenarla de ruido).
- **Debate de fondo, sin resolver:** ¿debería el sistema autorizar operaciones cuando Ardid está caído (postura de Pablo Gomes: no — "no podés dar por hecho una transferencia si no la estás monitoreando", riesgo de ventana de fraude no controlada) o debería tener una "palanca" manual gestionada por Riesgo/Ema para casos excepcionales, con trazabilidad de quién la activó? Consenso alcanzado en la reunión: el sistema debe estar preparado para ser **100% rígido por defecto** (nunca dejar pasar una operación sin pasar por Ardid), con una palanca de apagado explícita y auditada como única vía de excepción — la decisión de activarla no le corresponde a Producto/desarrollo, sino a Riesgo/Compliance. Queda pendiente llevar esta premisa a Ema Vignoles para su aprobación formal.
- **Otras decisiones operativas de la misma sesión:** daily de sincronización de 10 minutos a las 9:30 para todo el equipo (Producto+QA); las dudas de QA sobre criterios de aceptación se resuelven en esa daily en vez de procesos ad-hoc; objetivo de completar pruebas de un pago en producción con Mastercard/banco antes de fin de agosto.

## 14. Continuación del discovery de robustez — especificación global, rechazo por caída y state monitor (revisión técnica, 2026-08-21)

> **Estado: diseño en discovery — nada de esto está construido ni desplegado todavía.** Es la revisión técnica de un diseño que Nicolás Colón todavía va a ajustar antes de pasarlo a desarrollo. Filado acá como subsección delimitada y marcada como discovery (mismo criterio que §13) — no representa el comportamiento ya vigente en producción que describe el resto de este archivo.

Continuación técnica del discovery de robustez de Ardid presentado por Nicolás Colón el 2026-08-11 (§13) — en esa sesión se había alcanzado consenso de que el sistema debe ser "100% rígido por defecto" (nunca dejar pasar una operación sin pasar por Ardid), con una palanca de apagado explícita y auditada como única excepción, pendiente de aprobación formal de Emma Vignoles. En esta reunión ("Revisión Wallet - BIND", 2026-08-21) Nicolás Colón trajo el diseño técnico concreto de esa palanca para revisión de Juan Pablo Carubelli y Martín Hovanyecz (Wallet, Keep IT Simple), antes de pasarlo a desarrollo. Tres piezas — dos ya definidas, una tercera (la más extensa) en revisión en esta misma reunión.

### 14.1 Especificación de habilitación de análisis: global + por operación

Hoy existe una especificación por tipo de operación (transferencias internas/externas, pago QR, transferencia pool, pago de teléfono, etc.) que decide si esa operación puntual pasa por Ardid. Se agrega una nueva especificación **global**, con más peso que las de por operación — para que una operación vaya a Ardid, **las dos especificaciones (global Y por operación) tienen que estar en `true`**; si cualquiera de las dos falta o está en `false`, esa operación no pasa por Ardid.

**Decisión de diseño acordada con Juan Pablo Carubelli:** el comportamiento por defecto se invierte respecto al patrón histórico. Hoy, para que una operación pase por Ardid, hace falta que exista y esté en `true` la especificación (patrón "por la positiva" — sin especificación, no se analiza). El nuevo default es "por la negativa": **todo pasa por Ardid salvo que exista una especificación explícita en `false` para desactivarlo**. Aplica también a futuro: cuando la operatoria de Cobro pase por Ardid (hoy solo Wallet), debería seguir el mismo criterio.

**Por qué importa el cambio de default — antecedente real de falla operativa:** el "botón rojo" (kill switch) ya existe hoy, pero de forma poco confiable — es un script que ejecuta Infra para poner en `false` todas las especificaciones por tipo de operación. Cuando Wallet fue agregando operaciones nuevas (Pago FX, BIM recurrente, etc.), el script nunca se actualizó — la última vez que se intentó apagar todo, quedaron 2-3 operaciones activas sin que nadie lo supiera, precisamente porque el script no las conocía. La especificación global resuelve esto de raíz: un solo booleano, no un script a mantener por cada operación nueva.

### 14.2 Rechazar toda operación cuando Ardid está caído o responde error (deja de ser laxo)

Hoy, ante ciertas respuestas de error o falta de respuesta de Ardid, Wallet **deja pasar la operación igual** ("fue la definición que hubo en su momento de no cortarlo obligatorio... que pase, después veremos"). Nueva regla: **cualquier respuesta de Ardid que no sea `200` rechaza la operación** — con una excepción ya mapeada de antes que sigue funcionando igual: los rechazos de negocio propios de Ardid (`409`, ej. una regla/scoring que bloquea la operación) siguen su circuito normal de rechazo ya conocido.

**Matiz importante sobre el `409` de "cliente no encontrado":** hoy ese caso concreto (cliente no sincronizado en Ardid) también debería empezar a rechazar bajo la nueva regla, pero primero hay que hacer un **saneamiento de cuentas** — ya se había hecho antes "por los problemas que hemos tenido", pero quedaron cuentas que nunca se dieron de alta correctamente en Ardid y hoy siguen respondiendo `409`. Sin ese saneamiento previo, activar el rechazo por esta causa específica bloquearía operaciones de cuentas legítimas. Acción pendiente antes de habilitar esta parte de la regla.

**Manejo de error de cara al cliente:** los rechazos por caída/error de Ardid deben distinguirse de un rechazo de negocio real — código de error específico (tentativo: `99`) con mensaje "el sistema de monitoreo no se encuentra disponible", distinto del código ya usado para un rechazo real por regla de Ardid — para que soporte pueda diagnosticar por dónde viene un reclamo sin ambigüedad. Aplica a las mismas 5 operaciones que hoy se analizan: transferencias internas, externas de Bind, pago UR, transferencia pool y pago de teléfono.

### 14.3 State monitor — qué pasa con las peticiones que no llegaron a destino mientras Ardid está caído (la pieza más extensa, en revisión)

Nicolás ya tiene esto construido pero lo trajo a revisar antes de pasarlo, para no tener que modificarlo después. La regla se parte según el tipo de operación:

- **Alta de cuentas (siempre, sin importar la especificación global):** debe llegar a Ardid sí o sí. Si falla por intermitencia/timeout (no por estar la especificación apagada), se **encola** para reprocesar — específicamente el alta del `ClientType` (el alta del CUIT para una organización) y el `ClientProduct` (la asociación de ese cliente con un CVU).
- **Operaciones entrantes (transferencias entrantes):** mismo criterio — si falla por intermitencia/timeout, se guarda para procesar después vía el state monitor, sin importar la especificación (siempre se quiere que termine llegando a análisis).
- **Operaciones salientes (transferencia, pago QR, débito, etc.):** acá el comportamiento depende de la especificación (global/por operación) — si Ardid no responde o da timeout estando la conexión "activa" (se supone que debería analizarse), se **rechaza directamente la operación**, no se encola — coherente con la regla del §14.2 (nunca dejar pasar una saliente sin análisis).

**Distinción clave que Nicolás remarcó:** alta de cuentas y entrantes se encolan porque "siempre" tienen que terminar entrando al sistema tarde o temprano; las salientes se rechazan en el momento porque dejar pasar una salida de dinero sin haber podido analizarla es exactamente el riesgo que todo este trabajo busca evitar.

### 14.4 Punto sin resolver — relación entre el feature flag y el "botón rojo"

Juan Pablo Carubelli planteó una tensión de diseño sin cerrar en la reunión: si el feature flag de "no puedo conectar → dejar pasar/rechazar" convive con el botón rojo (especificación global manual), **hay una zona gris de cuándo se activa cada uno** — "che, la toma de decisión de es el feature flag o es el botón rojo, tenemos que tener claro cuándo sí, cuándo el otro." Nicolás lo ve como un salvavidas adicional ("no debería ser necesario, pero es como un salvavidas por las dudas"), pero Juan Pablo advierte que sin claridad de cuándo usar cada mecanismo se repite el mismo problema de confusión operativa que motivó todo este trabajo (hoy soporte recibe reclamos y "no sabemos para qué son" las especificaciones existentes). Queda para seguir discutiéndolo — no bloqueante para avanzar con el desarrollo de las 2 piezas ya definidas (§14.1, §14.2).

**Estado al cierre de la reunión (2026-08-21):** Martín Hovanyecz ya está analizando el rechazo-por-caída aplicado al circuito de marketplace, sin dudas hasta el momento. Nicolás va a ajustar el diseño del state monitor con lo discutido y pasarlo. Juan Pablo cerró pidiendo visibilidad de conjunto: si estas 3 piezas (más otras 2 que Wallet ya tiene en análisis, una ya desarrollada) tienen que salir todas en la misma versión — preocupación de capacidad de equipo (análisis + desarrollo + QA) mencionada junto con otros frentes compitiendo por la misma versión (FCI, Mastercard) — sin resolver en esta reunión, a discutir en la planificación de versión.

---
*Fuente: Notion histórico, Epics "Ardid para wallet: Transferencias" (21 tickets), "Ardid para botón simple MVP" (11 tickets), "Ardid - Bóveda: integrar" (3 tickets, 7 SP), "Reparar Ardid+Wallet: Alta de cuentas y de segmentos" (11 tickets, 50 SP), "Ajustes Ardid+Wallet: Informar datos de localización en operaciones" (1 ticket, 20 SP, discovery) y "Ajustes Ardid+Botón: Informar localización e informar devoluciones" (3 tickets, 15 SP, discovery) — ingesta 2026-07-06. §7: Jira `bindpsp.atlassian.net`, IDEA PRD-115 + Epic WS-548 (3 Historias: WS-549, WS-550, WS-551) — ingesta 2026-07-06. §8-10: backfill `/sync_releases` vía export XML, 2026-07-13. §11: `/sync_meetings`, reunión 2026-07-17. §11.1: `/sync_mails`, mail "Restauración Contadores Mensuales", 2026-07-20. §12: `/sync_meetings`, reunión "Análisis de riesgos - W 71.6", 2026-08-05. §13: `/sync_meetings`, reunión "Productos - Weekly Seguimiento", 2026-08-11. §6.1: `/sync_meetings`, reunión "Producto", 2026-08-18. §14: transcripción manual en sesión libre (no vía `/sync_meetings`), reunión "Revisión Wallet - BIND", 2026-08-21.*
