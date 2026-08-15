# Hallazgos — Cruce Onboarding × Wallet (mayo 2026 en adelante)

> Análisis motivado por [PRD-202](../../1_proyectos/proyecto-onboarding-estrategico/prd-202_onboarding_consolidado/proyecto.md) (en particular, por resolver el kill-assumption #4 del `/red-team` del 2026-07-16), sobre los 2 datasets registrados en [`index.md`](index.md), decodificados con [`organizaciones_wallet.md`](organizaciones_wallet.md) y el legend de `Estado` provisto por el usuario (2026-07-16). Todo lo de acá es **agregado** — ningún dato individual ni PII. Reutilizable para cualquier otra idea de producto que necesite el mismo tipo de análisis (volumetría de altas, cobertura de Onboarding, segmentación de clientes de Wallet).

## 0. ⚠️ Hallazgo más importante: ~47,5% de las solicitudes de Onboarding terminan Rechazadas

Con el legend de `Estado` confirmado por el usuario, la distribución real de las 38.152 solicitudes desde mayo-2026 es:

| Estado | Descripción | Cantidad | % |
|---|---|---|---|
| 3 | Rechazada | 18.110 | **47,47%** |
| 2 | Aprobada | 15.760 | 41,31% |
| 1 | Pendiente | 3.968 | 10,40% |
| 4 | Validación Manual | 214 | 0,56% |
| 8 | Aprobado sin notificar | 59 | 0,15% |
| 6 | Error alta | 29 | 0,08% |
| 7 | Aprobado a Revisar | 8 | 0,02% |
| 9 | *(sin código en el legend, anomalía menor)* | 3 | 0,01% |
| 5 | Pendiente credenciales | 1 | 0,00% |

**Por qué esto importa para PRD-202:** el PRD propone que el 100% de las altas nuevas de Wallet (empezando por Fase 1) pasen obligatoriamente por Onboarding. Hoy, de las solicitudes que **sí** pasan por Onboarding, **casi la mitad termina rechazada**. Si ese ratio se mantiene cuando se vuelva obligatorio para las organizaciones de mayor volumen (que hoy tienen ~0% de rechazo porque directamente no pasan por ninguna validación), el impacto en el volumen de altas exitosas podría ser mucho mayor de lo que el caso de negocio actual contempla — hoy el PRD no menciona en ningún lado una tasa de rechazo esperada.

### ⚠️⚠️ El motivo dominante de rechazo NO es fraude/riesgo — es fricción técnica de lectura de documento

Con el legend de `MotivoRechazo` confirmado por el usuario (33 códigos), la distribución real de las 18.110 solicitudes rechazadas es:

| Código | Descripción | Cantidad | % de los rechazos |
|---|---|---|---|
| 2 | **PDF417_NO_ENCONTRADO** | 8.822 | **48,71%** |
| — | *(sin motivo registrado, `NULL`)* | 2.723 | 15,03% |
| 3 | INTENTOS_EXCEDIDOS | 2.115 | 11,68% |
| 9 | SOLICITUD_PREVIA_APROBADA | 1.402 | 7,74% |
| 43 | *(código sin mapear — no está en el legend de 33 provisto, requiere confirmación de desarrollo)* | 1.338 | 7,39% |
| 4 | PERSONA_NO_ENCONTRADA | 1.327 | 7,33% |
| 37 | *(sin mapear)* | 144 | 0,80% |
| 10 | INTENTOS_EXCEDIDOS_OTP_EMAIL | 112 | 0,62% |
| 11 | INTENTOS_EXCEDIDOS_OTP_SMS | 81 | 0,45% |
| 36 | *(sin mapear)* | 39 | 0,22% |
| 8 | **RECHAZO_MATRIZ_DE_RIESGO** | 5 | 0,03% |
| 38 | *(sin mapear)* | 2 | 0,01% |

Agrupando por naturaleza del motivo:

- **Fricción técnica/UX (no es una decisión de riesgo):** `PDF417_NO_ENCONTRADO` + `INTENTOS_EXCEDIDOS` + `INTENTOS_EXCEDIDOS_OTP_EMAIL` + `INTENTOS_EXCEDIDOS_OTP_SMS` = **11.130 casos, 61,5% de todos los rechazos.** El motivo #1 por lejos (`PDF417_NO_ENCONTRADO`, casi la mitad de todos los rechazos) significa que el sistema no pudo leer el código de barras del DNI en la foto — una falla de captura/UX, no una señal de fraude.
- **Administrativo, no es un "fracaso" del solicitante:** `SOLICITUD_PREVIA_APROBADA` = 7,74% — la persona ya tiene una solicitud aprobada, el sistema bloquea el duplicado. No es un rechazo por incumplimiento.
- **La validación de riesgo/compliance realmente funcionando como se espera:** `RECHAZO_MATRIZ_DE_RIESGO` = **solo 5 casos, 0,03% de los rechazos.** `PERSONA_NO_ENCONTRADA` (7,33%) podría sumarse acá con matices (puede ser fraude real o un error de tipeo/dato). Combinados, en el mejor de los casos para la lectura "compliance funcionando", **no llegan al 7,4% de los rechazos.**
- **Sin explicar:** `NULL` (15,03%) + códigos sin mapear `43`/`37`/`36`/`38` (8,4% combinado) = 23,4% de los rechazos sin causa clara todavía.

**Conclusión, reemplaza la lectura anterior:** el ~47,5% de rechazo de Onboarding **no refleja, en su gran mayoría, al sistema atrapando fraude o incumplimiento normativo** — refleja sobre todo **fricción técnica del flujo actual** (lectura de PDF417, límites de intentos). Esto es una noticia relativamente buena y mala a la vez para PRD-202: **mala**, porque confirma que si se generaliza el flujo tal cual está hoy, gran parte de esos rechazos serían usuarios legítimos perdidos por un problema de UX, no fraude evitado — impacto directo de negocio. **Buena**, porque a diferencia de un problema de diseño normativo, esto es un problema de producto/UX bastante más resoluble (mejorar la captura de PDF417, revisar límites de reintentos) antes de convertir la validación en obligatoria. **Este hallazgo se vuelve el kill-assumption de mayor prioridad de todo el discovery de PRD-202 — ver Riesgos del PRD.**

## 1. Cobertura real de Onboarding (refresca el dato de PRD-108 con datos frescos)

- **304.356 cuentas de Wallet creadas** desde 2026-05-01 vs. **38.152 solicitudes de Onboarding** en la misma ventana.
- Ratio bruto: ~12,5% de las cuentas de Wallet tienen alguna solicitud de Onboarding asociada en el mismo período (no es un join exacto por cuenta, es una comparación de volumen total) → **~87,5% de las altas de Wallet ocurren sin pasar por Onboarding** en esta ventana reciente. Mismo orden de magnitud que el ~95% ya citado en PRD-108 (snapshot de dic-2025), levemente menor pero confirma que el patrón sigue vigente en 2026.
- **⚠️ Refinamiento del PM (2026-07-17, sesión de estrategia):** el ratio bruto de ~12,5% **sobreestima la cobertura real**, porque incluye solicitudes rechazadas y pendientes que nunca se convierten en cuenta. Contando solo las solicitudes **aprobadas** (estado 2 + 8 + 7 = 15.760 + 59 + 8 = **15.827**), la **cobertura KYC real es ~5,2%** de las cuentas creadas → **~95% de las altas de Wallet ocurren sin una validación de Onboarding exitosa** — coincide casi exactamente con el ~95% del snapshot de PRD-108. Esta es la definición de baseline adoptada para el KR1 del [foco estratégico de Onboarding](../../2_areas/direccion/estrategia/foco_onboarding.md).

## 2. Cero superposición entre las organizaciones que más cuentas crean y las que más usan Onboarding

**Top organizaciones por cuentas de Wallet creadas (por `OrganizacionId`, decodificado con [`organizaciones_wallet.md`](organizaciones_wallet.md)):**

| OrganizacionId | Nombre | Cuentas creadas | ¿Coincide con el top de Onboarding? |
|---|---|---|---|
| 24 | **BSF** | 105.187 | No |
| 16 | **Credicuotas** | 52.471 | No |
| 4 | **CENCOSUD** | 51.492 | No |
| 56 | **Sociedad Militar** (alta 2026-02-27, no estaba entre las "4 dominantes" de PRD-108) | 45.996 | No |
| 50 | **Global 66 (Argpagos psp)** (alta 2026-01-26, no estaba entre las "4 dominantes" de PRD-108) | 27.583 | No |

**Top organizaciones por solicitudes de Onboarding (por `IdOrganizacion`):** 9 = **TINPAY** (6.560), 43 = **Coppel** (4.344), 33 = **Inter** (3.358), 30 = **La Virginia** (214), 49 = **MC DONALD'S** (65), 60 = **Coop. Union Justiniano Posse** (17) — **un conjunto completamente distinto**, sin ningún nombre en común con el top de Wallet. (Nota de calidad de dato: 61,8% de las solicitudes tiene `IdOrganizacion` en `NULL`, así que este ranking de Onboarding hay que tomarlo con cautela — ver §5.)

**Lectura para el PRD:** esto es evidencia empírica directa y concreta del problema que da origen a PRD-108/PRD-202 — las organizaciones de mayor volumen de Bind PSP son, hoy, las que menos pasan por Onboarding. No es una estimación, es lo que muestran los datos de mayo en adelante. **Implicación directa para Fase 1 de PRD-202:** el foco comercial debería actualizarse de "Astropay/Cenco/BSF/Credicuotas" a **BSF, Credicuotas, Cenco, Sociedad Militar y Global 66 (Argpagos psp)** — 5 organizaciones, no 4, y 2 de ellas (Sociedad Militar, Global 66 Argpagos) son clientes relativamente nuevos (dados de alta en 2026) que no habían sido mencionados hasta ahora en el discovery de este PRD.

### Astropay (Id 5) no aparece en el top 15 de creación de cuentas — pero su registro de organización sigue activo

En la volumetría de PRD-108 (snapshot dic-2025), Astropay (Id 5) era una de las 4 organizaciones dominantes. En esta extracción (mayo 2026 en adelante), **el Id 5 no aparece ni siquiera en el top 15** de organizaciones por cuentas creadas. Esto es evidencia empírica a favor de un gap ya abierto en `../../2_areas/gaps_y_preguntas.md` (2026-07-13): *"Astropay dejó de operar en PROD"*. **Matiz nuevo (tabla de organizaciones, 2026-07-16):** el registro de Astropay como organización **no tiene `Fecha baja`** — sigue "activa" a nivel de configuración, lo que sugiere que se trata de **inactividad transaccional** (dejó de generar altas nuevas) y no de una baja formal de la cuenta/organización en el sistema. No resuelve del todo la pregunta original del gap (¿por qué dejó de operar, fue total o parcial, desde cuándo?), pero la acota. **Si Astropay efectivamente dejó de traer altas nuevas de forma sostenida**, el "Contexto" de PRD-202 (que lo usa como ejemplo central) y el foco comercial de Fase 1 deberían actualizarse — ver también el punto anterior sobre las 5 organizaciones dominantes reales.

## 3. Segmentación por tipo de persona y edad — resuelve el kill-assumption #4 del red-team

Usando el prefijo de `CuitCuil` (20/23/24/27 = persona física, 30/33 = persona jurídica — estándar argentino, no requiere el campo `RazonSocial`):

- **Persona física: 304.048 de 304.356 (99,9%)**
- **Persona jurídica: 304 de 304.356 (0,1%)**

Usando `FechaNacimiento` vs. `FechaAlta` para bucket de edad (donde el dato está disponible):

- **Menores de edad: máximo 5 cuentas** de 304.356 (0,002%) — calculado por diferencia de años de nacimiento/alta.
- **Cuentas con vínculo a tutor (`CuentaTutorId` poblado): 0** — el mecanismo de "cuenta de menor vinculada a tutor" no tiene ningún caso en esta ventana.
- **16,3% de las cuentas (49.548) no tiene `FechaNacimiento` cargada** — gap de calidad de dato real, en la misma línea del déficit de "actividad económica" ya señalado en el PRD (ver §5).

**Conclusión para el red-team:** el kill-assumption #4 ("¿la Fase 1 realmente cubre la enorme mayoría del volumen?") queda **resuelto a favor del PRD** — la porción de persona jurídica y de menores en el volumen actual es marginal (0,1% y ~0,002% respectivamente), muy por debajo del umbral de "no marginal" (15-20%) que se había propuesto como criterio de corte. El caso de negocio de Fase 1 (persona física mayor de edad) está bien fundamentado en los datos reales. El único matiz: 16,3% de los registros no tiene edad confirmada, así que no se puede descartar del todo que ahí haya una proporción distinta — pero no hay ninguna señal de que así sea.

## 4. Hallazgos técnicos relevantes para el diseño de PRD-202

- **`ExternalRefid` ya existe y ya se usa hoy** (poblado en 27,9% de las solicitudes de Onboarding) — **no es un campo nuevo**, como se había asumido en una sesión anterior del PRD. Lo que propone PRD-202 es formalizar su rol (identificador único cross-producto + idempotencia), no crear el campo desde cero. Ajustar esa afirmación en el PRD.
- **`UrlEnrollment` está vacío en el 100% de las solicitudes** (0 de 38.152) — el patrón asíncrono "`PENDIENTE` + URL de prueba de vida" que diseña PRD-202 **no existe todavía en producción**, confirma que es una funcionalidad nueva a construir, no una que ya funcione parcialmente.
- **⚠️ Discrepancia de nomenclatura detectada:** el campo real en la base es `AddaliaPruebaVida` (poblado en 23,9% de las solicitudes) y `AddaliaValidacionFacial` — **no "Socialnet"**. Todo el journey map y las decisiones de esta sesión sobre PRD-202 (incluida la decisión de que "hoy solo está integrado Socialnet") usaron el nombre "Socialnet" como el proveedor de prueba de vida vigente. Esto necesita aclaración del usuario: ¿"Addalia" es el nombre técnico/histórico del campo y "Socialnet" es el proveedor comercial actual (posible rebranding), o hay una confusión de nombres en las sesiones anteriores? Registrado como gap en `../../2_areas/gaps_y_preguntas.md`.

## 5. Gaps de calidad de dato detectados (relevantes para cualquier análisis futuro sobre estos datasets)

- ✅ **Resuelto (2026-07-16) — `Estado` (solicitudes):** legend confirmado por el usuario, ver §0.
- ✅ **Resuelto (2026-07-16) — `MotivoRechazo` (solicitudes):** legend confirmado por el usuario (33 códigos, ver §0) — reveló que el ~61,5% de los rechazos es fricción técnica (`PDF417_NO_ENCONTRADO`, límites de intentos), no fraude/riesgo (`RECHAZO_MATRIZ_DE_RIESGO` es solo 0,03% de los rechazos). 4 códigos observados en los datos (`36`, `37`, `38`, `43`) no están en el legend de 33 provisto — pendiente de confirmar con desarrollo.
- ✅ **Parcialmente aclarado (2026-07-16) — `TipoSolicitud` (solicitudes):** 23% de las filas en `NULL`; el valor dominante `Tin` coincide con el `CodigoEntidad` de la organización **TINPAY** (Id 9, la organización #1 en volumen de solicitudes) — sugiere que este campo usa códigos específicos por entidad/flujo, no necesariamente la taxonomía abstracta de "7 tipos de consumo" del PRD-202. Confirmar con desarrollo antes de asumir un mapeo directo.
- **`IdOrganizacion` (solicitudes):** 61,8% de las filas en `NULL` — cualquier análisis por organización sobre este dataset específico es parcial.

---

**Nota metodológica:** todo el análisis se hizo vía `awk` sobre los CSV crudos (ubicados en `datasets_locales/`, fuera del control de versiones — ver `index.md`), sin cargar los archivos completos en memoria y sin imprimir en ningún momento filas individuales ni valores de columnas de identidad.
