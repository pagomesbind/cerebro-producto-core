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

## Ver también
- [incidentes_de_plataforma.md §6](incidentes_de_plataforma.md) — mismo hilo de "Repaso Semanal líderes" donde se menciona el esquema desacoplado extendiéndose a "BM PCP".

---
*Última actualización: 2026-09-03 — `/context_merge`: nueva sección con los dos tracks pendientes reportados por Banco Industrial (2026-09-02) y su resolución cruzada con la decisión de migración CBU Link→Coelsa.*
*Última actualización anterior: 2026-08-14 — `/sync_meetings`: nueva sección "PSP 164 — mismo dilema, split ya roto" (decisión de postergar la migración mientras se espera el fix del banco, con plan escalonado de bajo riesgo como fallback). Ver reunión "Esquema desacoplado/migra PSP 164" (2026-08-12) en `wiki/2_areas/control/log_reuniones.md`.*
*Última actualización anterior: 2026-08-12 — Reubicado desde `detalle_productos/wallet/otros_manuales.md §15` (reestructuración PARA en cascada). Contenido sin cambios de fondo.*
