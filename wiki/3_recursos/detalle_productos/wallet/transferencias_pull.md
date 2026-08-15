# Transferencias Pull (Débito/DEBIN) — Consentimiento Tácito

> ⚠️ **Estado: documentación desactualizada — no confiar en §3 sin verificar contra el código actual.** Este archivo describe la lógica de reversa tal como estaba **antes** del incidente de fraude de marzo 2026 (~$11.500M explotando exactamente esta regla) y **no fue actualizado con la corrección aplicada post-incidente**. Ver [`4_archivos/postmortem_transferencias_pull_marzo_2026.md`](../../../4_archivos/postmortem_transferencias_pull_marzo_2026.md) para el detalle del exploit, y el gap abierto en [`../../../2_areas/gaps_y_preguntas.md`](../../../2_areas/gaps_y_preguntas.md). Reubicado desde `detalle_productos/cobros/transferencias_pull.md` en la reestructuración PARA en cascada (2026-08-12) — es una funcionalidad de Wallet (débito directo sobre CVU), no del Agente de Cobros y Pagos.

Contenido destilado de la Epic de Notion "API: TRX PULL cons tacito" (transferencias pull / débito directo vía Coelsa, roles CRÉDITO y DÉBITO), más una capacitación interna con ejemplos reales de integración (fusionada desde `detalle_productos/wallet/otros_manuales.md §1` en la reestructuración PARA en cascada, 2026-08-12).

## 0. Qué es y cómo integrarlo (capacitación interna)

### ¿Qué es?

Solución de APIs para crear o recibir transferencia pull. Es una funcionalidad similar al DEBIN: al ejecutarla desde Bind PSP se puede traer dinero de una cuenta externa, pero también puede ejecutarse desde afuera y debitar dinero de una cuenta propia.

Existen dos tipos: transferencia pull con consentimiento explícito y con consentimiento tácito. Bind PSP sólo tiene **consentimiento tácito**: pueden hacerse transferencias pull sin suscripción y aceptación previa, siempre que sea entre dos cuentas del mismo CUIT (se entiende que existe "consentimiento implícito").

### ¿Por qué es importante?

- Es una funcionalidad normativa: el BCRA obliga a que todas las PSP puedan al menos aceptar transferencias pull.
- Fomenta el cash in por su simplicidad de uso.
- A diferencia de DEBIN recurrente (limitado a CBU), transferencia pull permite operar entre CBU o CVU.

### ¿Qué está alcanzado?

- Endpoint para crear una transferencia pull desde una cuenta de una organización.
- Recepción de solicitud de transferencia pull desde un externo (otro PSP o banco): crea una operación de un nuevo tipo.

### ¿Qué no está alcanzado?

- No hay herramientas en Ardid para monitorear esta operatoria (fraude/desarbitraje de fondos).
- No integrada aún en la app marca blanca de wallet ni en el portal comercio.
- No hay esquemas automáticos para tratar contracargos (desconocimientos) de transferencia pull.

### ¿Cómo funciona?

- Para fondear una cuenta, la organización invoca el endpoint de transferencia pull. Esto crea una operación de un nuevo tipo; si es exitosa, acredita con un nuevo tipo de comprobante. La operación (aprobada o rechazada) dispara un webhook a la organización.
- Cuando un PSP o banco externo realiza una transferencia pull sobre la cuenta de una organización, el sistema la recibe y, si hay saldo suficiente, la registra: crea una operación de un nuevo tipo y debita con un nuevo tipo de comprobante. La operación aprobada dispara un webhook.

### Consideraciones importantes

- Sólo puede usarse en personas físicas. El BCRA la normó para uso exclusivo de fondeo de cuentas (no cobros de cuotas, préstamos, etc.). Para personas jurídicas se sigue ofreciendo DEBIN recurrente.
- Puede tener contracargos: si el usuario desconoce una transferencia pull realizada desde una cuenta propia, hay que devolver el dinero. No hay funcionalidad automática para tratar contracargos; deben tratarse manual y administrativamente por ahora.
- La procesa Coelsa directamente (el Banco Industrial no la desarrolló ni la disponibiliza en API Bank); se integró directo a Coelsa usando las credenciales de APIDEBIN de Coelsa.
- El cliente final tiene hasta 60 días desde la creación para contracargar el dinero.

### Requisitos para usarlo

- PSP = 184: no se necesita nada, ya tiene configuradas las credenciales de APIDEBIN Coelsa de Bind PSP.
- PSP ≠ 184: deben gestionarse con el Banco Industrial las credenciales de Coelsa de API DEBIN para ese PSP específico y solicitar a Fintexa que las configure.

### Ejemplo 1 — transferencia pull saliente (traer dinero desde un CVU de Mercado Pago)

Request:

```bash
curl --location 'https://api.bindpagos.com.ar/walletentidad-operaciones/v1/api/v1.201/transferenciaPull' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
    "cuentaId": 2534830,
    "cbuCvuComprador": "0000003100082591772269",
    "cuitComprador": "20374312759",
    "importe": 1589.11,
    "referencia": "fondeo"
}'
```

Respuesta:

```json
{
    "operacionId": 182288695,
    "operacionIdExterno": "76V4MR2Z7078MRWLNDEZOL",
    "estadoExterno": "ACREDITADO",
    "estadoId": 2,
    "origenCuentaId": 3399303,
    "contraparteCuit": "27413550861",
    "contraparteCbuCvu": "",
    "contraparteNombre": "",
    "fechaExpiracion": "2026-02-25T12:41:20.6626421+00:00",
    "comprobanteId": 453696610,
    "mensajeAdicional": null,
    "estaFinalizado": true,
    "estaRechazado": false,
    "estaAAuditar": false,
    "estaPendiente": false
}
```

Webhook recibido por la organización (evento `TRANSFERENCIA_PULL_ENTRANTE`, `operacionTipo: TransferenciaPullCredito`).

### Ejemplo 2 — transferencia pull entrante (desde Mercado Pago debitan a la cuenta de la organización)

Webhook recibido (evento `TRANSFERENCIA_PULL_SALIENTE`, `operacionTipo: TransferenciaPullDebito`) — mismo formato que el Ejemplo 1, con `importe` y `operacionId` propios de la operación de débito.

## 1. Contexto (Epic de diseño)

Ajustes al circuito de transferencia pull (débito directo iniciado por la contraparte, sobre CVU) para que Bind PSP admita tanto consentimiento **explícito** (con token) como **tácito** (sin token), cumpliendo la norma de Coelsa que exige soportar ambos modelos. El circuito distingue dos roles posibles para la cuenta de Bind PSP en la operación:

- **Rol CRÉDITO**: una organización de Bind PSP inicia una transferencia pull para *cobrarse* fondos de otra cuenta same-name (misma titularidad/CUIT) de su propio cliente, sin necesitar consentimiento porque es tácito.
- **Rol DÉBITO**: un banco o PSP externo inicia una transferencia pull para *debitar* fondos de una cuenta de Bind PSP, con o sin token de consentimiento explícito.

## 2. Condiciones de aceptación — Rol CRÉDITO

- Enviar el header de consentimiento vacío (token tácito).
- La transferencia pull debe ser siempre entre cuentas de la misma titularidad (CUIT) que la cuenta origen.
- Si la cuenta origen está deshabilitada: debe rechazarse y la operación crearse como RECHAZADA (o ni siquiera crearse, según el caso).
- Si la cuenta está habilitada y Coelsa procesa OK: la operación pasa a APROBADA y se crea el comprobante de crédito asociado.
- Si Coelsa devuelve error: operación RECHAZADA, sin comprobantes asociados.
- Si Coelsa responde "en progreso": la operación queda en proceso, sin comprobante de crédito hasta que Coelsa apruebe.

## 3. Condiciones de aceptación — Rol DÉBITO ⚠️ ver banner de vigencia arriba

- No aceptar intentos de débito con token de consentimiento explícito si Bind PSP no otorgó ningún consentimiento (evita débitos no autorizados).
- La transferencia pull debe ser entre cuentas de la misma titularidad (CUIT) que la cuenta de débito.
- Al enviar el `ConfirmaDebitoCVU` a Coelsa, debe crearse de inmediato un comprobante de débito + operación "En Proceso".
- Si Coelsa responde error en el `ConfirmaDebitoCVU`, o error (código ≠ 00) en el `AvisoOperacionFinalizada`: debe crearse un comprobante de crédito de reversa asociado al débito original y la operación pasa a RECHAZADA.
- Debe rechazarse la transferencia pull si la cuenta de débito está deshabilitada o no tiene saldo suficiente.

## 4. Adecuaciones de formato de request y moneda

- **Adecuaciones al request de transferencia pull entrante**: se ajustó el formato para indicar la cuenta de origen por `IdCuenta` y el CVU comprador por `IdCuentaEnrolada` (cambio de contrato con el banco).
- **Ajuste de moneda en trx pull débito**: Coelsa solicitó normalizar el request para incluir explícitamente el campo `moneda` dentro del bloque `detalle` de la operación (junto a `ori_trx`, `ori_terminal`, `ori_adicional`, `importe`), como parte de la adecuación general del mensaje de operación.

## 5. ⚠️ Incidente de fraude (marzo 2026)

La regla de negocio descripta en §3 ("Si Coelsa responde error... debe crearse un comprobante de crédito de reversa asociado al débito original") es, tal como está documentada acá, la lógica que un incidente crítico de fraude explotó en marzo de 2026: el sistema generaba el crédito de reversa sin validar que el débito original se hubiese ejecutado realmente, permitiendo la creación de fondos ficticios (~$11.500 millones robados). Ver el detalle técnico completo del exploit y la corrección aplicada en [postmortem_transferencias_pull_marzo_2026.md §5.1](../../../4_archivos/postmortem_transferencias_pull_marzo_2026.md). **Este archivo no fue actualizado con la lógica corregida post-incidente.**

---
*Fuente: Notion histórico, Epic "API: TRX PULL cons tacito" — ingesta 2026-07-06. Nota: 3 tickets de esta Epic devolvieron 404/blank en Notion (páginas eliminadas o de acceso restringido: "Consentimiento lado PSP" —Cancelado—, "Transferencias Pull Entrantes (lado billetera)" —contenedor sin contenido— y una página de prueba QA vinculada); no aportan info adicional a la ya cubierta acá.*
*Actualización 2026-07-07: agregada nota de incidente de fraude (§5).*
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/cobros/transferencias_pull.md` a Wallet en la reestructuración PARA en cascada; banner de vigencia agregado en el encabezado para que no se lea como documentación confiable de §3 sin la advertencia.*
