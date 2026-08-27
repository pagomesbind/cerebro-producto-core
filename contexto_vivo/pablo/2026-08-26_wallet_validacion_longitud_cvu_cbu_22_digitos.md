---
id: 2026-08-26_wallet_validacion_longitud_cvu_cbu_22_digitos
pm: pablo
fecha_captura: 2026-08-26
fuente: "/sync_releases — Jira bindpsp.atlassian.net, versión W 72 (publicada 2026-08-18), tickets WS-1191, WS-1113, WS-1083"
producto: wallet
tema: Hardening de plataforma — validación de longitud exacta de CVU/CBU (22 dígitos) en toda la cadena Wallet
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/organizaciones_y_configuracion.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Iniciativa de hardening publicada en un solo release (W 72), en 3 tickets simultáneos, uno por microservicio — Epic WS-7.** Hasta esta versión, ningún microservicio de Wallet validaba que un CVU/CBU tuviera exactamente 22 caracteres numéricos (norma BCRA Com. A 2622 para CBU / Com. A 6510 para CVU); un valor inválido podía propagarse sin control hasta BIND, Dispatcher y COELSA.

**Hallazgo crítico de base de datos** (descubierto en el análisis, MS Cuenta): la columna `CuentasCVU.CVU` estaba definida como `nvarchar(100)` — permitía hasta 100 caracteres. `CuentasProcesadores.CBU` (`VARCHAR(22)`) era la única columna correctamente dimensionada en todo el ecosistema. Se corrigió vía migración Flyway `ALTER CuentasCVU.CVU → NVARCHAR(22) NOT NULL`, con safety-check que aborta el script si hay registros legacy con longitud ≠ 22 (no los hubo).

**Los 3 microservicios cubiertos:**

- **MS Cuenta + Cuenta Queries** ([WS-1113](https://bindpsp.atlassian.net/browse/WS-1113)) — origen de los CVU en el ecosistema: los crea, almacena y expone al resto. Cubre `POST /cuentaProcesador`, `POST /debinSuscripcion`, y las búsquedas `byCvu`/`byCbuCvuOrAlias` de Queries. El CVU no lo genera Wallet.Cuenta sino que lo recibe de BIND/Dispatcher como respuesta — la validación se aplica post-respuesta del proveedor externo, antes de persistir (defense-in-depth de 5 capas: API, dominio/EF `[MaxLength(22)]`, repository post-respuesta, application pre-publish del evento `AltaCvuEvent`, y una capa 0 pre-persist agregada durante el desarrollo al detectarse 3 rutas que aún escapaban la validación).
- **MS Operaciones** ([WS-1083](https://bindpsp.atlassian.net/browse/WS-1083)) — 4 flujos de negocio: Transferencia Saliente (`/transferir`, `/IntencionTransferencia`, `/TransferirConCostos`), Transferencia Pull (`/transferenciaPull`), Pago QR (`/pagoQR`) y Debin Recurrente (`/DebinRecurrenteCredito`). 4 entidades de dominio corregidas de `nvarchar(30)`/`varchar(30)` a 22. Importante: un CVU/CBU de 22 dígitos que falle el dígito verificador (mod-10) o la estructura interna **no se rechaza acá** — queda fuera de este scope (lo rechazaría COELSA/BIND aguas abajo).
- **Wallet.Bind** ([WS-1191](https://bindpsp.atlassian.net/browse/WS-1191)) — el wrapper directo de la API externa de BIND, expuesto por Swagger a cualquier consumidor interno. Cubre CVU Controller (update/delete/setalias), Transfer Controller (`maketransfer`, banks transaction-requests) y Account/Debin Controllers.

**Comportamiento resultante (aplica a los 3):**
- Código de error **HTTP 422** (no 400) con `ErrorDetailModel`, discriminado por marker técnico para no romper el resto de las validaciones `ModelState` existentes (que siguen devolviendo 400).
- Comparación **ASCII estricta** (`c>='0' && c<='9'`), no `char.IsDigit` — evita que un dígito Unicode no-ASCII (ej. dígito arábigo-índico) bypasee la validación.
- **Las búsquedas por alias no se rompen**: el campo mixto CVU/CBU-o-alias tiene un discriminador — solo valida longitud=22 cuando el valor recibido es numérico; un alias alfanumérico (o numérico de otra longitud) sigue funcionando como alias.
- **Validación condicional en flujos con alias**: `MakeTransfer`/transferencias con intención solo valida el CVU/CBU destino cuando no viene un alias informado.
- Seguridad: la respuesta 422 no ecoa el CVU/CBU completo; los logs tampoco (con una deuda preexistente señalada aparte — varios handlers ya logueaban `{@Request}` con un paquete de masking externo no verificable desde este repo, no introducida por este cambio).
- **Cambio de comportamiento para integraciones existentes** (no de contrato): inputs mal formados que antes se propagaban a BIND (con error genérico aguas abajo) ahora se rechazan en Wallet con 422 antes de la llamada externa. El camino feliz (datos correctos) no cambia.

Cobertura de tests: 90/90 + 57/57 (Wallet.Bind), 348/348 + 156/156 (MS Operaciones), 44/44 (MS Cuenta) — 0 regresiones reportadas. Verificado en STG por Ana (QA) contra el gateway real APIM (`gw-staging-qrbind.epays.services`), el mismo contrato que consumen BFFs/portales/mobile/POS.

**Al mergear:** agregar como nueva sección temática (ej. §8 "Validación de longitud CVU/CBU (22 dígitos)") en `organizaciones_y_configuracion.md` — es transversal a los 3 microservicios documentados en ese archivo, no encaja en ninguna sección existente de alta/config puntual.
