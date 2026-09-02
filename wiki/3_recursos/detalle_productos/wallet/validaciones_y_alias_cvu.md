# Validaciones y mecánica de CVU/CBU — Wallet

> Estado: en producción.

Reglas de plataforma sobre CVU/CBU que aplican de forma transversal a cualquier organización de Wallet (no son parte del alta/configuración de una organización puntual — para eso ver [organizaciones_y_configuracion.md](organizaciones_y_configuracion.md)): la mecánica de Coelsa para asignación de alias al crear un CVU, y el hardening de validación de longitud exacta de CVU/CBU en toda la cadena de microservicios.

---

## 1. Mecánica de Coelsa cuando el alias no se asigna a tiempo tras crear un CVU

**La ventana de 5 segundos está oficialmente documentada, no es solo conocimiento empírico (confirmado 2026-08-25, `/idea_solution`).** El endpoint público de creación de CVU y su guía documentan explícitamente: *"al momento de crear un CVU, Coelsa le asignará un alias aleatorio a menos que la entidad le asigne un alias válido dentro de los 5 segundos desde la creación"* — y que esto aplica **igual** tanto si Bind asigna el alias automáticamente como si la organización lo gestiona ella misma vía API (mismo plazo de 5 segundos en ambos casos, sin delay adicional para ninguno de los dos). También documentado: solo se puede asignar/modificar un alias una vez cada 24hs, y esa restricción incluye el alias que haya asignado Coelsa automáticamente.

- Cuando el alias por defecto no queda asignado dentro de esos 5 segundos desde la creación del CVU, **Coelsa le asigna al CVU un alias arbitrario por su propia cuenta**.
- A partir de ese momento, **Coelsa bloquea cualquier reasignación de alias durante 24 horas** — ni la plataforma ni la organización pueden corregirlo antes de que pase ese plazo, sea por reintento automático o por acción manual de Soporte.

**Mecanismo de la falla original (caso MDA-292391, Banco Industrial):** el flujo de asignación automática de alias de Wallet, tras crear el CVU, llama a un endpoint interno de asignación de alias contra el banco emisor (producto "apibank" de Banco Industrial). **Corrección de atribución** (confirmada por el propio proveedor bancario en conversación directa): quien hace la consulta previa contra Coelsa antes de proceder es **el banco emisor internamente**, no Wallet — Wallet solo ve un único llamado (la asignación de alias) que el banco responde con error si su consulta previa a Coelsa indica que el CVU todavía no propagó a la réplica que usa para resolver esa consulta (separada del flujo transaccional real, según explicó el proveedor por analogía con su API de débito recurrente). El código de error observado en producción es `422` con detalle `VW006 | El CVU no existe`.

**Comportamiento actual del sistema ante esta falla:**
- Cuando la falla ocurre **dentro del flujo automático de creación de CVU** (parámetro `aliasAutomatico=true`, el valor por defecto): el endpoint público de creación responde igual `201` (éxito), pero con el campo `alias` **vacío** — sin ningún error explícito hacia quien integró. Es un fallo silencioso desde la perspectiva de la organización integradora.
- Cuando la falla ocurre en una llamada **directa** al endpoint público de asignación de alias (`aliasAutomatico=false`, o una reasignación posterior): ese endpoint **sí devuelve el error real del banco** (`422`, "no existe el id de CVU" en la documentación pública) — a diferencia del camino anterior, acá la organización sí se entera de que algo falló.

**Solución adoptada:** reintento de 700ms, cubriendo ambos caminos de invocación (ver `1_proyectos/asignacion_alias_cvu/artefactos/asignacion_alias_cvu-solution.md` para el análisis técnico completo — contrato, diagramas, máquina de estados).

> Fuente: discovery `/idea_start` de `1_proyectos/asignacion_alias_cvu/` (2026-08-25) — ticket MDA-292391 (Banco Industrial/apibank) + conversación técnica del PM con el proveedor bancario (Google Hangouts, 2026-08-24); actualizado por `/idea_solution` (2026-08-25) contra la documentación pública oficial de los endpoints de CVU/alias y aclaraciones del PM sobre el comportamiento actual del sistema.

**Tope anual de modificaciones y formato del alias (confirmado 2026-08-28, todavía no reflejado en `apis_expuestas/cvu/guia_cvu.md`).** Dos reuniones independientes del mismo día citan, de forma consistente entre sí, dos datos que la guía pública hoy no documenta: un alias de CBU/CVU corto puede modificarse un **máximo de diez (10) veces al año** (normativa BCRA, citada explícitamente en la reunión "Web de developers") y debe tener **entre 6 y 20 caracteres**. Una segunda fuente ("Daily producto") citó el mismo tope con un número ambiguo en el dictado ("tres o diez") — se toma 10 como correcto por coincidir con la fuente que cita la normativa de origen. Como la corrección de `apis_expuestas/` es dominio exclusivo de `/sync_web`, este dato queda documentado acá mientras tanto — ver gap señalizado en [`gaps_y_preguntas.md`](../../../2_areas/gaps_y_preguntas.md) [2026-08-31] para que `/sync_web` lo aplique a la guía pública en su próxima corrida.

> Fuente adicional: reuniones "Daily producto" y "Web de developers" (ambas 2026-08-28), en el marco del discovery de `1_proyectos/alias_cvu_checkout/`.

**Reintento automático adicional en la creación de alias ante error de APIBank (2026-08-31, confianza media).** En la reunión "Weekly - Producto / Operaciones" (2026-08-31), Pablo Gomes informó que se implementó un reintento automático en la creación de alias de cuenta cuando la operación recibe un error de APIBank — descripto como mitigación de un error frecuente y como una regresión nueva ("antes andaba bien"), no un error histórico. No se detalló el mecanismo (cantidad de intentos, backoff) más allá de la mención en la reunión. Es un reintento **distinto** del fix de 700ms de MDA-292391/Banco Industrial documentado arriba — mismo tipo de problema (falla de asignación de alias ante error de APIBank), mecanismo de reintento separado, a confirmar contra el ticket/desarrollo real si se necesita el detalle técnico.

## 3. Nota operativa — nuevas necesidades regulatorias mencionadas para 2024 (confianza baja)

En la misma reunión "Weekly - Producto / Operaciones" (2026-08-31) se mencionaron, sin mucho detalle, dos necesidades regulatorias que el equipo va a integrar en su planificación de cumplimiento: (1) obligación de **capturar el domicilio real** de los usuarios finales (personas humanas) en el request de alta de cuenta (CBU/Postcuenta) — coincide con lo ya documentado en detalle en [`cumplimiento_normativo/identificacion_personas_fisicas_cvu.md`](../../cumplimiento_normativo/identificacion_personas_fisicas_cvu.md) (matriz de domicilio real, Art. 13 inc. e); (2) necesidad de **consultar la actividad ante AFIP** durante las altas en wallets — dato nuevo, no cubierto todavía en la matriz de cumplimiento normativo citada. La minuta las etiqueta como "requerimientos regulatorios para 2024" sin más contexto (norma/comunicación de origen, fecha límite, alcance exacto). Confianza baja por lo escueto de la mención; capturado igual porque toca directamente el flujo de alta de cuenta (ver también el gap normativo abierto "CPA no se completa en el 72% de cuentas con domicilio" en [`organizaciones_y_configuracion.md`](organizaciones_y_configuracion.md) §0).

---

## 2. Validación de longitud CVU/CBU (22 dígitos) — hardening de plataforma (W 72)

**Iniciativa de hardening publicada en un solo release (W 72, 2026-08-18), en 3 tickets simultáneos, uno por microservicio — Epic [WS-7](https://bindpsp.atlassian.net/browse/WS-7).** Hasta esta versión, ningún microservicio de Wallet validaba que un CVU/CBU tuviera exactamente 22 caracteres numéricos (norma BCRA Com. A 2622 para CBU / Com. A 6510 para CVU); un valor inválido podía propagarse sin control hasta BIND, Dispatcher y COELSA.

**Hallazgo crítico de base de datos** (descubierto en el análisis, MS Cuenta): la columna `CuentasCVU.CVU` estaba definida como `nvarchar(100)` — permitía hasta 100 caracteres. `CuentasProcesadores.CBU` (`VARCHAR(22)`) era la única columna correctamente dimensionada en todo el ecosistema. Se corrigió vía migración Flyway `ALTER CuentasCVU.CVU → NVARCHAR(22) NOT NULL`, con safety-check que aborta el script si hay registros legacy con longitud ≠ 22 (no los hubo).

### Los 3 microservicios cubiertos

- **MS Cuenta + Cuenta Queries** ([WS-1113](https://bindpsp.atlassian.net/browse/WS-1113)) — origen de los CVU en el ecosistema: los crea, almacena y expone al resto. Cubre `POST /cuentaProcesador`, `POST /debinSuscripcion`, y las búsquedas `byCvu`/`byCbuCvuOrAlias` de Queries. El CVU no lo genera Wallet.Cuenta sino que lo recibe de BIND/Dispatcher como respuesta — la validación se aplica post-respuesta del proveedor externo, antes de persistir (defense-in-depth de 5 capas: API, dominio/EF `[MaxLength(22)]`, repository post-respuesta, application pre-publish del evento `AltaCvuEvent`, y una capa 0 pre-persist agregada durante el desarrollo al detectarse 3 rutas que aún escapaban la validación).
- **MS Operaciones** ([WS-1083](https://bindpsp.atlassian.net/browse/WS-1083)) — 4 flujos de negocio: Transferencia Saliente (`/transferir`, `/IntencionTransferencia`, `/TransferirConCostos`), Transferencia Pull (`/transferenciaPull`), Pago QR (`/pagoQR`) y Debin Recurrente (`/DebinRecurrenteCredito`). 4 entidades de dominio corregidas de `nvarchar(30)`/`varchar(30)` a 22. Importante: un CVU/CBU de 22 dígitos que falle el dígito verificador (mod-10) o la estructura interna **no se rechaza acá** — queda fuera de este scope (lo rechazaría COELSA/BIND aguas abajo).
- **Wallet.Bind** ([WS-1191](https://bindpsp.atlassian.net/browse/WS-1191)) — el wrapper directo de la API externa de BIND, expuesto por Swagger a cualquier consumidor interno. Cubre CVU Controller (update/delete/setalias), Transfer Controller (`maketransfer`, banks transaction-requests) y Account/Debin Controllers.

### Comportamiento resultante (aplica a los 3)

- Código de error **HTTP 422** (no 400) con `ErrorDetailModel`, discriminado por marker técnico para no romper el resto de las validaciones `ModelState` existentes (que siguen devolviendo 400).
- Comparación **ASCII estricta** (`c>='0' && c<='9'`), no `char.IsDigit` — evita que un dígito Unicode no-ASCII (ej. dígito arábigo-índico) bypasee la validación.
- **Las búsquedas por alias no se rompen**: el campo mixto CVU/CBU-o-alias tiene un discriminador — solo valida longitud=22 cuando el valor recibido es numérico; un alias alfanumérico (o numérico de otra longitud) sigue funcionando como alias.
- **Validación condicional en flujos con alias**: `MakeTransfer`/transferencias con intención solo valida el CVU/CBU destino cuando no viene un alias informado.
- Seguridad: la respuesta 422 no ecoa el CVU/CBU completo; los logs tampoco (con una deuda preexistente señalada aparte — varios handlers ya logueaban `{@Request}` con un paquete de masking externo no verificable desde este repo, no introducida por este cambio).
- **Cambio de comportamiento para integraciones existentes** (no de contrato): inputs mal formados que antes se propagaban a BIND (con error genérico aguas abajo) ahora se rechazan en Wallet con 422 antes de la llamada externa. El camino feliz (datos correctos) no cambia.

Cobertura de tests: 90/90 + 57/57 (Wallet.Bind), 348/348 + 156/156 (MS Operaciones), 44/44 (MS Cuenta) — 0 regresiones reportadas. Verificado en STG por Ana (QA) contra el gateway real APIM (`gw-staging-qrbind.epays.services`), el mismo contrato que consumen BFFs/portales/mobile/POS.

> Fuente: Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), tickets WS-1191, WS-1113, WS-1083.

---
*Última actualización: 2026-09-02 — `/context_merge`: reintento automático de alias ante error de APIBank (§1) y nueva §3 con nota operativa de baja confianza sobre requisitos regulatorios 2024 (domicilio real, consulta de actividad AFIP).*
*Última actualización anterior: 2026-08-26 — creado en el merge de `contexto_vivo/` (2026-08-25/26): §1 mecánica de alias de Coelsa (discovery `asignacion_alias_cvu`) y §2 hardening de longitud CVU/CBU (W 72). Separado de `organizaciones_y_configuracion.md` por tema (mecánica de CVU/CBU transversal a la plataforma, no alta/configuración de una organización puntual) y para no seguir engrosando ese archivo.*
