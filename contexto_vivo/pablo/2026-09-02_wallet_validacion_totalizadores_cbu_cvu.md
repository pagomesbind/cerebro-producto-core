---
id: 2026-09-02_wallet_validacion_totalizadores_cbu_cvu
pm: pablo
fecha_captura: 2026-09-02
fuente: "ingesta directa de Jira a pedido del PM (cierre/go-live PRD-200) — PRD-200, WS-1312, WS-1313 y sus 6 subtareas (WS-1451, WS-1452, WS-1481, WS-1485, WS-1486, WS-1487), comentarios completos"
producto: wallet
tema: validación de totalizadores CBU/CVU en alta de cuenta (mandato Banco Industrial/BCRA)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/validacion_totalizadores_cbu_cvu.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

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

**Endpoints alcanzados:** `POST /api/v1/Cuenta` (S1), `POST /api/v1/CuentaYCVU` (S2), `POST /api/v1/CuentaYCVUConCuentaComitente` (S3) — los tres terminan en `AddCuentaCommandHandler → ValidarLimites`. S2/S3 con `Id`/`CuentaId` ya existente (no es alta nueva) no pasan por la validación. También alcanza a las altas hechas por **Onboarding** vía su BFF (`orquestador/api/v1/onboarding-cuenta-comitente`) — confirmado en pruebas (WS-1486): el motor interno de Onboarding sí llama al mismo flujo de validación y devuelve el mismo `eventId` de rechazo, pero **no lo expone al llamador** — la respuesta pública de Onboarding solo trae `cuenta`/`cuentaCvu`/`cuentaInvestment` en `null` sin indicar la causa; hay que ir a la herramienta interna "Respuestas Servicios" o a `dbo.Solicitud` para ver el motivo real. Queda registrado como oportunidad de mejora (ver item separado en `contexto_vivo/`), candidata al alcance de PRD-118.

**Respuesta de rechazo:** `HTTP 422` con `eventId` de dominio — **1272** (supera límite de CBU), **1273** (supera límite de CVU), **1274** (supera límite de CBU+CVU/Total). Nota: el planteo original de la IDEA proponía `HTTP 409`, pero la implementación final usó `422` (Automation for Jira lo confirma en un comentario técnico de WS-1313, 2026-08-04). Logs de evidencia de que se consultó Coelsa: **1271** + **1276**, independientemente del resultado.

## Evidencia de QA (8/8 casos de matriz de bordes)

Probado con CUITs de referencia reales contra Coelsa (no valores sintéticos), en dos escenarios — organización sin configuración propia (usa límites globales) y organización con override propio — cada uno con happy path + rechazo CBU + rechazo CVU + rechazo Total: los 8 casos confirmaron el comportamiento esperado. También probados en aislamiento los límites de "solo CVU" y "solo Total" (sin CBU configurado).

**Aprendizaje operativo para pruebas futuras sobre el mismo mecanismo:** el CUIT de referencia usado en QA no es estable entre corridas — cualquier alta que efectivamente cree un CVU sube el total real que Coelsa devuelve para ese CUIT (se vio subir de 79 a 80 CVU a mitad de una tanda de pruebas, causando un resultado inesperado). Recomendado: usar solo `POST /api/v1/Cuenta` (sin crear CVU) para pruebas de borde, y reconsultar `GetTotalizadoresCoelsa` antes de cada tanda en vez de asumir valores fijos.

## Fuente

Jira: PRD-200, WS-1312, WS-1313 (comentario técnico completo de Mariano, 2026-08-04) y subtareas WS-1451/1452/1481/1485/1486/1487. Confirmación operativa de producción: reunión "Emisión V 72: Reunión Pre-despliegue" (2026-08-18), fixVersion W72 liberada 2026-08-18.
