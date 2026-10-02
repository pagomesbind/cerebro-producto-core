# Validación de totalizadores CBU/CVU en alta de cuenta (mandato Banco Industrial/BCRA)

> Estado: en producción (desde W72, 2026-08-19).

> Fuente: Jira PRD-200, WS-1312, WS-1313 (comentario técnico completo de Mariano, 2026-08-04) y subtareas WS-1451/1452/1481/1485/1486/1487. Confirmación operativa de producción: reunión "Emisión V 72: Reunión Pre-despliegue" (2026-08-18), fixVersion W72 liberada 2026-08-18.

## Qué es

Desde el pase a producción de la versión W72 (2026-08-19), Wallet valida — antes de dar de alta cualquier cuenta — que el titular (CUIT) no supere una cantidad máxima de CBU/CVU totales, consultando el servicio de totalizadores de Coelsa. Es un requisito normativo (BCRA, exigido en el cortísimo plazo por Banco Industrial) para prevenir altas fraudulentas. Construido como vía rápida directo en Wallet (IDEA **PRD-200**, Epic **WS-1312**, Historia **WS-1313**) mientras la versión definitiva integrada a Onboarding (**PRD-118**) sigue pendiente — ambas conviven a propósito, no es duplicación.

## Mecánica

**Configuración (specs por clave):**

| Clave | Scope | Rol |
|---|---|---|
| `TOTALIZADORES_VALIDACION_HABILITADA` | Sistema | Kill-switch global ("botón rojo") — apaga la validación para todas las organizaciones |
| `TOTALIZADORES_CBU_LIMITE` | Sistema o Organización | Tope de CBU |
| `TOTALIZADORES_CVU_LIMITE` | Sistema o Organización | Tope de CVU |
| `TOTALIZADORES_CBUCVU_LIMITE` | Sistema o Organización | Tope de la suma CBU+CVU |
| `TOTALIZADORES_CUIT_WHITELIST` | Sistema | CSV de CUITs exentos de la validación |

El override de organización pesa más que el valor global (solo para esa organización). Semántica del corte: `>=` bloquea (si el total es igual o mayor al límite, rechaza). Si no hay ningún límite configurado (ni global ni de organización), el sistema no consulta Coelsa y deja pasar el alta.

**Exclusiones automáticas:**
- **Personas jurídicas** (CUIT que empieza con `3`): no pasan por esta validación en absoluto — exit directo antes de consultar Coelsa (log de evidencia 1279). El requisito normativo es sobre personas físicas.
- **CUIT en whitelist:** exit sin consultar Coelsa (log 1277). En la práctica no se usa — el caso que la motivaba (whitelist por CUIT jurídico) ya está cubierto por la exclusión de personas jurídicas.
- **Owner del PSP faltante en la organización:** no se puede consultar Coelsa sin credenciales — la validación no avanza y responde `422`/evento **1278** (no se da de alta, a diferencia de las otras exclusiones que sí dejan pasar).

**Endpoints alcanzados:** `POST /api/v1/Cuenta` (S1), `POST /api/v1/CuentaYCVU` (S2), `POST /api/v1/CuentaYCVUConCuentaComitente` (S3) — los tres terminan en `AddCuentaCommandHandler → ValidarLimites`. S2/S3 con `Id`/`CuentaId` ya existente (no es alta nueva) no pasan por la validación. También alcanza a las altas hechas por **Onboarding** vía su BFF (`orquestador/api/v1/onboarding-cuenta-comitente`) — confirmado en pruebas (WS-1486): el motor interno de Onboarding sí llama al mismo flujo de validación y devuelve el mismo `eventId` de rechazo, pero **no lo expone al llamador** — la respuesta pública de Onboarding solo trae `cuenta`/`cuentaCvu`/`cuentaInvestment` en `null` sin indicar la causa; hay que ir a la herramienta interna "Respuestas Servicios" o a `dbo.Solicitud` para ver el motivo real. Queda registrado como oportunidad de mejora (ver [`direccion/oportunidades.md`](../../../2_areas/direccion/oportunidades.md) OP-018), candidata al alcance de PRD-118.

**Respuesta de rechazo:** `HTTP 422` con `eventId` de dominio — **1272** (supera límite de CBU), **1273** (supera límite de CVU), **1274** (supera límite de CBU+CVU/Total). Nota: el planteo original de la IDEA proponía `HTTP 409`, pero la implementación final usó `422` (Automation for Jira lo confirma en un comentario técnico de WS-1313, 2026-08-04). Logs de evidencia de que se consultó Coelsa: **1271** + **1276**, independientemente del resultado.

## Evidencia de QA (8/8 casos de matriz de bordes)

Probado con CUITs de referencia reales contra Coelsa (no valores sintéticos), en dos escenarios — organización sin configuración propia (usa límites globales) y organización con override propio — cada uno con happy path + rechazo CBU + rechazo CVU + rechazo Total: los 8 casos confirmaron el comportamiento esperado. También probados en aislamiento los límites de "solo CVU" y "solo Total" (sin CBU configurado).

**Aprendizaje operativo para pruebas futuras sobre el mismo mecanismo:** el CUIT de referencia usado en QA no es estable entre corridas — cualquier alta que efectivamente cree un CVU sube el total real que Coelsa devuelve para ese CUIT (se vio subir de 79 a 80 CVU a mitad de una tanda de pruebas, causando un resultado inesperado). Recomendado: usar solo `POST /api/v1/Cuenta` (sin crear CVU) para pruebas de borde, y reconsultar `GetTotalizadoresCoelsa` antes de cada tanda en vez de asumir valores fijos.

## Coelsa actualiza el servicio de origen — ABM de CBU vinculado al Totalizador, con fecha de alta/baja de cuenta (2026-10-01)

> Fuente: mail "Homologación ABM de CBU" (threadId `1a0f7c4a7d26484a`), Coelsa (`icm@coelsa.com.ar`), 2026-10-01. Destinatarios principales: equipo de desarrollo/productos de Banco Industrial e Implementaciones de Bind PSP — Pablo Gomes en copia.

Coelsa notificó una actualización del servicio **ABM de CBU vinculado al Totalizador de cuentas** (el mismo servicio que este mecanismo consulta antes de dar de alta una cuenta, ver "Qué es" arriba): la nueva versión incorpora el registro de **fecha de alta y fecha de baja** de las cuentas bancarias, en línea con requerimientos normativos vigentes (sin especificar cuál en el mail — a confirmar si se relaciona con alguno de los ya trackeados en [`cumplimiento_normativo/`](../../cumplimiento_normativo/index.md)).

**Cronograma:** ambiente de Homologación disponible desde el 24/08/2026 hasta el 16/10/2026 inclusive; salida a Producción a partir del **18/10/2026**.

**Documentación técnica publicada por Coelsa:** API nuevo `https://documentacion.coelsa.com.ar/aliascbu/#api-cbu-nuevo`; Batch nuevo `https://documentacion.coelsa.com.ar/aliascbu/#batch-cbu-nuevo`.

**Sin acción puntual identificada para Producto en el mail** — de requerirse homologar antes del 16/10, es responsabilidad operativa de Implementaciones/Integraciones. No confirmado todavía si este cambio de fondo (fecha alta/baja de cuenta) impacta el mecanismo de validación de límites documentado arriba.

---
*Última actualización: 2026-10-02 — `/context_merge`: nueva sección — Coelsa actualiza el servicio ABM de CBU/Totalizador con fecha de alta/baja de cuenta, salida a producción 18/10/2026 (Pablo Gomes).*
*Creado: 2026-09-03 — `/context_merge`: nuevo archivo, mecánica completa de validación de totalizadores CBU/CVU (PRD-200), destilado de Jira (WS-1312/WS-1313 y subtareas) a pedido del PM en el cierre/go-live del proyecto.*
