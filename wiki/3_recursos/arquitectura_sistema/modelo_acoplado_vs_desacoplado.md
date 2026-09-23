# Modelo Acoplado vs. Desacoplado — Split QR PSP 184 y Migración de Personal Pay

> Reubicado desde `detalle_productos/wallet/otros_manuales.md §15` en la reestructuración PARA en cascada (2026-08-12) — es infraestructura/arquitectura de plataforma (relación con Banco Industrial, migración de clientes entre modelos técnicos), no mecánica de producto Wallet. Fuente: Reunión "BIND PSP - Desacoplado" (2026-08-06), minuta Gemini. Sesión técnica con Banco Industrial (Pablo Ramal, Ignacio Ghillini, Marcelo Diz, Ariel Matías Galano, Gisela Fernández, Alan Marchesi, Leandro Torres, Álvaro Aguirreburualde) y Bind PSP (Emma Vignoles, Hernán Clarich, Nicolás It, Gonzalo Genna, Inti Benites, Pablo Gomes). Continuación técnica de T-083 ([2_areas/tareas.md](../../2_areas/tareas.md)) — bloqueo de PSP 184 con Split QR reactivado con Banco Industrial tras 5 meses sin movimiento.

## Contexto

Bind PSP necesitaba la funcionalidad de **split en pagos QR** del PSP 184, que hoy solo existe en el modelo **desacoplado** (mismo mecanismo que ya usa el PSP 164). La migración al desacoplado se evaluaba como única vía para destrabar el split.

## Cambio de la foto

Banco Industrial confirmó que el fix de split para el PSP 184 **ya está en preproducción para el modelo acoplado** (servicio y conciliación, ambos en fase de pruebas) — la migración completa al desacoplado **deja de ser necesaria solo por el split**. Bind PSP queda habilitado a probarlo en preproducción cuanto antes.

## Decisiones acordadas

- **Migración de Personal Pay al modelo desacoplado confirmada para el lunes por la madrugada** — es el cliente de mayor volumen y el que más incidentes genera hoy; su salida del acoplado debería reducir ~60% de los incidentes actuales de bloqueo en el registro de saldo (todos concentrados en ese único cliente).
- **Pausa en la migración de otros clientes al desacoplado** hasta implementar y probar el fix de split en el modelo acoplado.
- **Reunión de seguimiento en 10 días** (~2026-08-16) para evaluar resultado de las pruebas de split y performance post-salida de Personal Pay.

## Riesgo operativo del modelo desacoplado — ventana de sincronización de 2 minutos

El saldo se actualiza contra un caché, no en tiempo real contra el core. Si un usuario ejecuta operaciones simultáneas por distintas APIs dentro de esa ventana (ej. cashout por CB corta + transferencia por CB larga, que no está desacoplada), el sistema puede autorizar ambas y dejar la cuenta en descubierto — requiere que los PCP que migren tengan control de saldo exhaustivo y acuerdos de descubierto acordes al negocio ("modelo PCP de confianza"). Riesgo de fraude si no hay proceso de conciliación robusto (ej. explotar la ventana con montos chicos y alta frecuencia).

**Mitigación confirmada (no es un mecanismo técnico nuevo):** el propio banco explicó (análisis técnico-funcional `/idea_solution` sobre `resiliencia_api_bank`, 22/09/2026) que la forma de mitigar este riesgo es puramente una **política operativa de saldo mínimo**: "debemos asegurar que las organizaciones con las que operamos nunca queden cerca de cero el saldo, porque puede ser que en un momento en que en la realidad no tengan saldo suficiente, saquen plata y puedan porque virtualmente tienen saldo porque aún no ha actualizado el sistema." No hay caché adicional, bloqueo ni validación de saldo distinta a la ya existente — las cuentas/organizaciones migradas deben mantener siempre un colchón suficiente para que ningún movimiento las deje en descubierto real durante la ventana.

**Precisión importante: el riesgo aplica a la consulta de saldo, no a la consulta de estado de una operación puntual.** Confirmado directamente por Banco Industrial (Ignacio Ghillini, Álvaro Aguirreburualde): (1) el `origin_id` propio sigue sirviendo para reconsultar el estado de una transferencia sin importar el modelo ("con el origin ID siempre van a poder buscarlo") — distinto del cambio de identificador en el archivo de conciliación (`REFERENCIA_MONI`, ver más abajo), que es sobre el batch, no sobre la reconsulta vía API; (2) la consulta de estado de una operación puntual se resuelve siempre contra una **base intermedia** del banco, no contra su core contable — "te va a devolver el completed, no vamos al core a buscar ese estado, lo respondemos desde la base intermedia". Es decir: la consulta de **saldo agregado de la cuenta** puede quedar desactualizada durante la ventana; la consulta de **estado de una transferencia ya confirmada** es confiable de inmediato, sin la misma exposición.

**Confirmaciones adicionales de arquitectura (mismo análisis, 22/09/2026):** no hay ningún flag ni disparador del lado de la compañía para activar el modelo desacoplado — es 100% configuración interna del banco por cuenta/subcuenta, sin llamado de API ni parámetro de Bind involucrado. El contrato de API de transferencia desde CVU (creación y consulta de estado) no cambia entre modelo acoplado y desacoplado — el propio campo `id` de la respuesta ya distingue el circuito con un prefijo (`WP` = interna desacoplada). El único frente de impacto real y confirmado sigue siendo la conciliación de Administración y Recaudaciones (cambio de identificador, pérdida del reporte horario) — ajuste interpretativo/manual de ese equipo, no desarrollo de Ingeniería.

## Cutover de Banco Industrial (BIN 24/Bind 24) — regresiones reales encontradas y resueltas en vivo (22/09/2026)

> Fuente: reunión "GD-6592 - Imple Divorcio" (war room técnica del pase a producción, 01:45 a ~08:00 GMT-3, 22/09/2026) — Banco Industrial, proveedor tecnológico Poincenot y Bind PSP.

El pase a producción de la plataforma decoupled de Banco Industrial (migración de Personal Pay al modelo desacoplado, ver arriba) expuso tres regresiones reales, todas encontradas y mitigadas la misma madrugada del cutover — patrón genérico a anticipar como checklist en cualquier futura migración de cliente/producto a este modelo:

1. **Pérdida de webhooks de acreditación/devolución/contracargo de BIN, causada por el propio desacople.** Las notificaciones de Coelsa, que antes resolvía directamente el entorno de Coelsa hacia el PCP, empezaron a pasar por Webbank hacia el middleware público de BIN 24, que intentaba disparar erróneamente una notificación web — los webhooks de devoluciones/contracargos dejaron de invocarse, impidiendo devolver saldo a usuarios afectados. Solución temporal esa noche: redirigir el webhook al middleware de Coelsa y desactivar las notificaciones innecesarias vía una propiedad; solución definitiva: parche en Apibank Web para que Webbank no reciba webhooks ajenos (desplegado en preproducción y producción esa misma madrugada).
2. **Pagos duplicados/triplicados en Bin Cash, por routing incorrecto entre entornos.** Bin Cash usaba Webbank en un entorno BIN 24 que no soportaba transferencias "sin beneficiario", así que se redirigieron a API — pero las **consultas de estado seguían apuntando al entorno BIN 24 viejo**, donde esas operaciones no existían, marcándolas erróneamente como rechazadas. Los clientes reintentaban manualmente sin saber que el débito ya se había efectuado, duplicando pagos reales. Impacto cuantificado: 327 operaciones de Bin Cash sin acreditar, 113 marcadas como fallidas en reintento, caso confirmado Cántar SRL (7 operaciones duplicadas) — el servicio estuvo a punto de darse de baja temporalmente. Resuelto reapuntando las consultas de estado al entorno de API correcto.
3. **Gap de fecha de nacimiento por la migración desde Antotal, bloqueando el login de ~10.000 usuarios.** La fecha de nacimiento pasó a ser obligatoria para validar el "secreto memorizado" (autenticación), pero ~10.179 de ~80.000 registros migrados desde Antotal la tienen nula (mayormente autorizados/apoderados no presentes en el sistema origen). Workaround en producción esa noche: fecha por defecto 1900-01-01 (variante puntual 1901) para permitir operar, mientras Atención Telefónica resuelve casos uno por uno. Bug relacionado (zona horaria): fechas grabadas a las 00:00 se convertían restando un día, bloqueando el login a usuarios el día de su propio cumpleaños — corregido fijando la hora a las 12:00 del mediodía como solución provisional.

**Otros hallazgos operativos del cutover:** error de certificado API que requirió reinicio de pods; feature flags de la pestaña "API" (transferencias/desembolsos) desactivados por defecto en producción, activados durante la ventana; liberación de iOS 3.11 completada esa madrugada, Android postergado sin forzar actualización obligatoria hasta estabilizar; snapshots/backups de bases de datos ejecutados como parte del propio cutover.

## Otras diferencias operativas

- **Cambio de identificadores en conciliación:** en el modelo desacoplado, los débitos usan el **ID de Coelsa** en vez del **ID interno (Origin ID)** actual, porque la operación se cursa primero en Coelsa — impacto directo en los procesos de conciliación de Administración.
- **Reporte horario de conciliación:** en revisión si sigue siendo necesario en el nuevo esquema de contabilidad global — hoy resuelve ~35% de las conciliaciones como parche ante fallos de notificación (CIN sin respuesta tras 3 reintentos). Otros clientes de alto volumen (Personal Pay) no lo necesitan.
- **Performance comparada:** modelo desacoplado ~99,93% (caso Meli) vs. ~99,7-99,8% del acoplado actual.
- **Clientes de mayor volumen identificados:** BCF (billetera Carrefour, cobro con QR + fondeo/gasto interno vía CB corta, sin salida de la recaudadora) y Coto (creciendo con un modelo similar) — candidatos naturales a evaluar para el desacoplado una vez resuelto el split.

## PSP 164 — mismo dilema, split ya roto (2026-08-12)

> Fuente: Reunión "Esquema desacoplado/migra PSP 164" (2026-08-12), minuta Gemini (Hernan Clarich, Pablo Gomes, Emma Vignoles, Diego Weledniger, Gonzalo Rivera, Maria Eugenia Vila).

El PSP 164 tiene su propia urgencia de split (a diferencia del 184, tratado arriba): el split para pagos QR **falla hoy en el esquema acoplado estándar**, con un bug del lado del banco que **ya estaba parcheado en pre-producción**, pero sin fecha confirmada de pase a Producción.

**Decisiones acordadas:**
- **Se posterga la migración al desacoplado** mientras se espera la fecha de pase a producción del fix de split del banco — Pablo Gomes hace seguimiento directo con Alan Marchesi (PM del banco) y escala por mail al final de la semana si no hay respuesta.
- **Si el banco no da fecha, migración escalonada de bajo riesgo:** empezar por una sola cuenta de bajo riesgo (agente de cobro/QR, ej. la cuenta de dispersión), dejando afuera las cuentas de Wallet de alto riesgo (billeteras con transferencias salientes, que sí pueden quedar en descubierto durante la ventana de sincronización).

**Mecánica del desacoplado, explicada en la sesión (complementa el contexto de arriba):** el banco notifica directo en vez de pasar primero por el core bancario ("B total") — mejora tiempos y reduce caídas, pero abre una ventana de **2 a 5 minutos** donde el saldo puede quedar desactualizado del lado del banco. Cualquier salida de fondos de la cuenta (no solo QR) puede generar un descubierto transitorio en esa ventana — no es exclusivo de billeteras: agentes de cobro/dispersión también quedan expuestos, aunque con mucho menor riesgo real (no hay transferencias salientes de terceros).

**Otros costos del cambio, ya identificados:** cambio de identificador en transferencias externas (pasa a usar el ID de Coelsa en vez del ID interno — mejor para el cliente, pero rompe procesos de conciliación que dependen del ID actual); se pierde el reporte de conciliación **por hora** (la V2 del esquema desacoplado solo trae reportería diaria).

## Banco Industrial — dos tracks pendientes de definiciones de Bind (2026-09-02)

> Fuente: mail "Bind PSP - próximos pasos" — Alan Marchesi (Banco Industrial), 2026-09-02.

Banco Industrial dejó registrado que quedan **dos tracks** esperando "los requerimientos y definiciones pendientes" de parte de Bind para poder avanzar: (a) la **migración a desacoplado** ya documentada en este archivo, y (b) la **migración de CBU link a Coelsa** — track nuevo, sin responsable único explícito del lado de Bind en el mail (Cristian Natale, Gonzalo Rivera, Hernán Clarich y Mariana Nadalin en el hilo directo, Pablo Gomes en copia).

**El track (b) queda resuelto por la decisión registrada el mismo día** ([`direccion/decisiones.md`](../../2_areas/direccion/decisiones.md) [2026-09-02]): no es un servicio de vinculación externo, es la migración de **transferencias salientes de CBU larga**, cursadas hoy por la red **Link**, hacia **Coelsa** — motivada por conciliación (Link no da a Bind una referencia utilizable, Coelsa sí). Piloto en curso con Cucurú y Tienda Nube como clientes candidatos (Gonzalo Rivera a cargo del caso de prueba).

## Especificación técnica exacta del archivo de conciliación `MovimientosComp` en el modelo desacoplado

> Fuente: mail "RE: [sin asunto]" de Gonzalo Genna (Banco Industrial), originalmente 2026-09-08, reenviado con Pablo Gomes en copia el 2026-09-21.

Completa, con precisión técnica, lo ya dicho arriba sobre cambio de ID de conciliación y pérdida del reporte horario:

- **No hay cambio de formato de interfaz ni de nombre de archivo** — sigue siendo `MovimientosComp`.
- **Campo `REFERENCIA_MONI`:** en débitos, pasa a enviarse el ID de Coelsa — igual que ya ocurre hoy en los créditos. Ejemplo textual del banco: hoy (Origin ID/ID interno) `1-30717449076-W93400014586895-1`; con desacoplado (ID Coelsa) `WGRXJE27Q6W7W0P97MYQL3`. El banco deja abierta una pregunta técnica: "hay que ver cuál persisten uds al momento de ejecutar la transacción" — Bind tiene que decidir/confirmar qué identificador persiste en su propia base al ejecutar la transacción.
- **NSBT — nuevo formato de armado:** `NSBTD-1-1-749049-264-1-20260310-125-41-1-1`, máximo posible de **68 caracteres**.
- **Contracargos:** si Bind usa códigos de movimiento para conciliar, va a recibir mayor nivel de diferenciación (nuevos códigos) en esa operatoria.
- **Confirmación explícita y sin matices:** "el reporte 'online' (cada una hora) no va a poder utilizarse para conciliar ésta operatoria" en el modelo desacoplado.

**Pregunta técnica sin responder por el banco:** qué ID persiste Bind al ejecutar la transacción — trabajo de definición técnica de Bind (equipo de Administración), no un gap del banco. Ver `1_proyectos/resiliencia_api_bank/proyecto.md §7` (Pablo Gomes) para cuando el proyecto avance a Fase 3/implementación.

## Ver también
- [incidentes_de_plataforma.md §6](incidentes_de_plataforma.md) — mismo hilo de "Repaso Semanal líderes" donde se menciona el esquema desacoplado extendiéndose a "BM PCP".

---
*Última actualización: 2026-09-23 — `/context_merge`: riesgo de ventana de sincronización ampliado con la mitigación confirmada (política de saldo mínimo) y la precisión saldo vs. estado de operación; nueva sección con las 3 regresiones reales del cutover de Banco Industrial (22/09/2026) — pérdida de webhooks, pagos duplicados en Bin Cash, gap de fecha de nacimiento migrada.*
*Última actualización anterior: 2026-09-21 — `/context_merge`: nueva sección con la especificación técnica exacta de `MovimientosComp` en el modelo desacoplado (campo `REFERENCIA_MONI`, formato NSBT, contracargos, reporte horario) aportada por Banco Industrial.*
*Última actualización anterior: 2026-09-03 — `/context_merge`: nueva sección con los dos tracks pendientes reportados por Banco Industrial (2026-09-02) y su resolución cruzada con la decisión de migración CBU Link→Coelsa.*
*Última actualización anterior: 2026-08-14 — `/sync_meetings`: nueva sección "PSP 164 — mismo dilema, split ya roto" (decisión de postergar la migración mientras se espera el fix del banco, con plan escalonado de bajo riesgo como fallback). Ver reunión "Esquema desacoplado/migra PSP 164" (2026-08-12) en `wiki/2_areas/control/log_reuniones.md`.*
*Última actualización anterior: 2026-08-12 — Reubicado desde `detalle_productos/wallet/otros_manuales.md §15` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
