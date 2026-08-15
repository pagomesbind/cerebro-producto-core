# TIN — Wallet white-label con tarjetero (MVP y cash-in con tarjeta)

> Estado: en producción.

> Fuente: Notion histórico, Epics **"TIN: MVP"** (43 tickets) y **"TIN: APP Tarjetero en Wallet MVP cash in"** (~89 SP estimados, 58 tickets — el ticket-set más grande relevado hasta ahora en una sola Epic de Wallet). **TIN** es el codename interno de una instancia white-label de Wallet con foco en app mobile propia (a diferencia de otros clientes de esta wiki que son API-first). Por el volumen de tickets y la pérdida de la cuota de queries SQL de Notion durante esta ingesta (ver [archivo de control](../../../4_archivos/ingesta_epics_notion.md), completado y rotado a `4_archivos/`), estas dos Epics se documentan a nivel de mecánica y aprendizajes principales — sin triage ticket por ticket completo.

## 1. TIN: MVP — dimensionamiento y riesgos de lanzamiento

- **Escala proyectada**: hasta 1.000.000 de CVU potenciales, 350.000 CVU de uso habitual — mismo orden de magnitud que Astropay (ver [clientes_white_label.md](clientes_white_label.md)), confirmando que Wallet white-label apunta a clientes de volumen masivo, no nicho.
- **Equipos de desarrollo mixtos**: se asignaron recursos de dos proveedores/equipos externos en paralelo — "KeepIT" (2.5 backend + 2-3 mobile) y "TF" (1 backend) — para este MVP, evidencia de que Bind PSP terceriza desarrollo puntual en clientes de alta prioridad.
- **Riesgos de lanzamiento identificados**:
  - **Sin credenciales de Renaper API Rostro** al momento del análisis — bloqueante potencial para cualquier validación biométrica de identidad en el onboarding.
  - **Riesgo de fraude explícito**: un usuario podría sacarle captura de pantalla al mismo QR de cobro varias veces y presentarlo repetidamente con el mismo saldo aparente — quedó documentado como riesgo conocido, no como bug resuelto.
  - **Tiempos de aprobación de Apple/Google stores** identificados como riesgo de cronograma (no controlable por el equipo).
- **Feature particular mencionada**: "Micronauta" — una funcionalidad/micro-servicio cuya visibilidad debía restringirse exclusivamente a ese cliente dentro de la misma base de código — patrón de **feature flag por cliente** en una app blanca compartida.
- **Detalle técnico suelto**: el flujo de QR local tiene la restricción de que un usuario **nunca puede tener más de un QR local vivo** a la vez (invariante de diseño, no configurable).

## 2. TIN: APP Tarjetero — cash-in con tarjeta guardada

### Qué es y cómo funciona

Funcionalidad de la app que permite **guardar tarjetas de crédito/débito y usarlas para cargar saldo** (cash-in) — el usuario puede agregar, ver y eliminar tarjetas, y luego ingresar dinero usando una guardada.

- El cobro con tarjeta se procesa contra un **comercio del propio ecosistema de Cobro/Adquirencia de Bind PSP** — cada recarga se liquida neta de comisiones e impuestos, igual que cualquier otro comercio de Adquirencia. Es decir: el tarjetero de Wallet **consume la infraestructura de cobro de Adquirencia** en vez de integrar un procesador de tarjetas propio — mismo patrón de reutilización interno visto en otras Epics (CCL reutilizado por PIX/DIRECTA, Adquirencia reutilizada acá).
- **Todas las operaciones se monitorean por ARDID** (antifraude) — coherente con el riesgo de fraude de tarjeta señalado en el MVP general de TIN.
- **Fuera de alcance explícito**: usar la tarjeta guardada para otros pagos que no sean cash-in (no es un tarjetero "genérico" de e-commerce).
- **Requisito operativo**: antes de habilitar, hay que crear la entidad/comercio correspondiente en Cobro y parametrizarlo contra la organización de Wallet dueña de la app.
- **Igual que DEBIN Recurrente en APP** ([debin_y_fondeo.md §5](debin_y_fondeo.md)): está disponible y funcionando en producción pero **no se publicó la versión en las stores** — el propio equipo de producto señaló que la publicación masiva debía analizarse aparte por el riesgo de la operatoria (fraude con tarjeta ajena).

### Bugs de UX reales (ya documentados en el piloto de esta ingesta)

Del backlog de esta Epic ya se habían relevado en la ingesta piloto: mensajes de error confusos cuando la tarjeta tiene la fecha de vencimiento mal cargada o el CVV es incorrecto, y falta de información de qué tarjeta se usó en el comprobante de cash-in — todos indicando que el frontend no propagaba con claridad los motivos de rechazo del procesador de tarjetas al usuario final.

## 3. Mejoras chicas de UX en la app (Epics "TIN: APP Opción ingresar dinero" e "Historial de destinatarios frecuentes")

- **Botón "Agregar dinero" en el Home**: pantalla informativa con las opciones de cash-in disponibles (transferencia, efectivo en locales/agencias, cuentas vinculadas por trx pull, tarjetas). **Patrón de configuración por organización**: la opción de transferencia está siempre habilitada para todas las organizaciones, pero el resto de las alternativas se muestran u ocultan **por organización individual** — mismo patrón de "feature flag por cliente en app compartida" visto en TIN: MVP (§1, caso Micronauta).
- **Transferir desde el detalle de un movimiento**: al ver el detalle de una transferencia entrante o saliente en "últimos movimientos", el usuario puede iniciar una nueva transferencia precargando los datos del destinatario, o repetir la misma operación tal cual — reduce fricción sin tocar el flujo de transferencia base.
- **Bug real de transparencia de errores**: cuando una transferencia saliente fallaba, el detalle devuelto al usuario/organización traía vacíos justamente los campos que explican el motivo (`MotivoRechazo`, `CoelsaId`, datos de la contraparte) — se esperaba que informara si el rechazo vino de ARDID o de API Bank, y no lo hacía. Mismo patrón de "error poco transparente" ya visto en otras Epics de Wallet (CCL, DEBIN).

## 4. Epic "TIN" (Dolor) — bolsa de bugs menores sin tema común

Epic contenedor con bugs puntuales de bajo impacto individual (ej. campos vacíos en detalle de transferencias, ya cubierto arriba) — no aporta mecánica de producto nueva más allá de lo ya documentado en las Epics específicas de TIN.

## 5. TIN: Mantenimiento (51 tickets: 31 Funcional/No funcional, 20 Bug — cola de mejoras y fixes post-lanzamiento)

> Fuente: Epic Notion "[EPIC] TIN: Mantenimiento" (Tipo Negocio). Ingesta MANT, 2026-07-06 — cierra por completo el grupo TIN.

Cola larga de ajustes UX y bugs de la app TIN acumulados post-MVP, sin un tema único — agrupados acá por tipo de aprendizaje:

- **Performance**: "Tarda mucho en iniciar la app" aparece duplicado como bug de front (L) y de BFF back (M) — el mismo síntoma percibido por el usuario tenía causa raíz en ambas capas y se atacó por separado.
- **Seguridad**: la app permitía grabar pantalla y capturas en iOS durante flujos sensibles (corregido); la contraseña aparecía sugerida en el teclado predictivo del dispositivo en la pantalla de login (corregido); se agregó validación para no permitir espacios como carácter válido en la contraseña.
- **Integración con Ardid**: bug en el esquema de reintentos al crear cliente en Ardid (Bug, L) — mismo dominio de fragilidad de integración documentado en [ardid/integracion_con_productos_bind.md](../ardid/integracion_con_productos_bind.md), acá del lado wallet/TIN.
- **Integración con Recycle**: "Podés consultar recycles" (L) + "Adaptar viajeTIN a nuevo recycle genérico" (L) — TIN necesitó adaptarse cuando el motor de recycle pasó de una lógica específica de viajes a un motor genérico (ver [recycle_cobro_automatico.md](recycle_cobro_automatico.md)).
- **Multi-tenant / white-label**: parametrización por organización de URLs de Términos y Condiciones y Preguntas Frecuentes (repetido en app y en back) — mismo patrón de configuración por organización que en TIN: MVP y en el botón "Agregar dinero" (§3).
- **UX acumulativa**: separador de miles en saldo, orden de movimientos duplicados/desordenados en "ver más", tamaño del comprobante, mostrar hora y minutos en movimientos, botón "Volver" sin funcionalidad en varias pantallas, botón "Actualizar" que no redirige al store, recordar usuario en login, mostrar versión de la app en el menú y en staging con prefijo "[TEST]", timeout de QR ajustado de 15 a 20 segundos vía parámetro.
- **AccessManagement**: interpretación de la respuesta de bloqueo de cuenta del AccessManagement directamente en el login de la app (antes no se comunicaba al usuario por qué no podía entrar).

**Lectura para estimaciones futuras**: una Epic "Mantenimiento" de una app madura (TIN llevaba ~2 años en producción) trae mayormente tickets M/S de UX + bugs de integración puntuales — el ratio 31 Funcional / 20 Bug es consistente con "cola de deuda técnica menor" más que con problemas estructurales nuevos.

### 5.0 Reproceso de viajes con error (W 65/W 66, vía `/sync_releases`)

- **Viajes QR con comprobante pero sin operación** ([WS-70](https://bindpsp.atlassian.net/browse/WS-70), publicado W 66 2025-12-15, SOPORTE): casos productivos con el comprobante generado pero sin el registro de la operación. La solución fue el endpoint **`POST /api/v1/Viaje/ReprocesarPorId`** en Wallet.Tin para que Soporte reprocese viajes generados con errores (faltantes de `IdComprobante`/`IdOperacion`), con **máximo 3 viajes por solicitud** como control. Nota de QA: el alcance real del endpoint no estaba informado ni en la US ni en el GLPI original — se documentó después.

### 5.1 Fixes de Viajes QR publicados en W 68 (2026-03-11, vía `/sync_releases`)

- **Timeout contra Micronauta** ([WS-402](https://bindpsp.atlassian.net/browse/WS-402)): una caída del MS de Micronauta (proveedor del QR de viaje) el 20/01/2026 expuso que la llamada a `SolicitarQR` no tenía timeout definido (default 100 segundos) y casi sin logs — se bajó el timeout a **30 segundos** y se agregaron logs por CorrelationId en la creación de ViajeQR.
- **Validación de organización en reprocesos** ([WS-259](https://bindpsp.atlassian.net/browse/WS-259)): el endpoint de reprocesar Viajes QR (`/api/v1/Viaje/ReprocesarPorId`) no validaba que los viajes indicados pertenecieran a la organización del header `x-entidad` — una organización podía reprocesar viajes de otra. Corregido: si no coinciden, responde error 1025 "Viajes QR no encontrados". (Preventivo: TIN era la única organización usando viajes, pero el multi-tenant lo exigía.)

## 6. Reevaluación estratégica de la billetera de transporte (2026-07-21)

> Fuente: Reunión "Productos - Weekly Seguimiento" (minuta Gemini, 2026-07-21). Luciana Rudaz/Nicolás Colón evaluando el frente de recaudación de transporte de TIN — el Cerebro solo recopila esta información, no organiza el trabajo de otros PMs (ver `1_proyectos/index.md §1`).

- **Se evalúa descontinuar la billetera (app) para el caso de uso de transporte**, no el cliente TIN en su totalidad: los costos de mantenimiento y los riesgos de fraude (ver riesgo de QR reutilizado por captura de pantalla, §1) superarían los ingresos que genera. La alternativa en discusión es ofrecer **únicamente servicios de recaudación** (digitalización del cobro), sin que Bind PSP tenga que gestionar saldos de usuarios.
- **Micronauta** (proveedor del QR de viaje, ver §5.1 — timeout WS-402) queda bajo investigación operativa: hay que entender su proceso de gestión de saldos y conciliación para diseñar cómo digitalizar la recaudación sin depender de la billetera.
- Sin decisión cerrada todavía — el PM de este frente evaluará qué elementos priorizar antes de fin de año.

## Ver también

- [debin_y_fondeo.md §5](debin_y_fondeo.md) — mismo patrón (feature de cash-in construida y en producción, pero nunca publicada en stores).
- [clientes_white_label.md](clientes_white_label.md) — Astropay como referencia de otro cliente de escala similar (millones de CVU).
- [adquirencia/liquidaciones_y_devoluciones.md §0](../adquirencia/devoluciones_y_contracargos.md) — "Desconocimientos de tarjeta" es una Epic de Adquirencia/Botón Simple, no de TIN/Wallet pese a la etiqueta ambigua del nombre — reclasificada durante esta ingesta.
- [recycle_cobro_automatico.md](recycle_cobro_automatico.md) — motor de cobro automático de deudas pendientes: nació acotado a los viajes QR de TIN (Recycle V1) y luego se generalizó a cualquier comprobante de Wallet (Recycle V2). Mismo caso de reclasificación: las Epics traen etiqueta `wallet back`/`wallet app`, no de Agente de Cobros, pese a que el checklist de la ingesta las agrupaba bajo "Cobros".
