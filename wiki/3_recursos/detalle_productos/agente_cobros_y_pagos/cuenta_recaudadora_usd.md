# Cuenta Recaudadora en USD y Consulta de Saldo — Agente de Cobros y Pagos

> Estado: en producción.

> Contenido destilado de las Epics de Notion "Astro: Agente de cobros y pagos en USD" y "Astro: Consulta de saldo. Agente de cobros y pagos en ARS".

## 1. Cuenta Recaudadora en USD — qué es y cómo funciona

Extensión del Agente de Cobros y Pagos que permite a cada entidad tener una cuenta recaudadora en dólares para realizar y recibir transferencias exclusivamente por API. Cliente de origen: Astropay (caso de uso: cuenta corriente interna en USD por usuario, referenciada por CUIT/CUIL, fondeada same-name desde la CBU recaudadora en USD de Bind PSP).

- Todas las transferencias entran/salen desde una única cuenta recaudadora CBU en USD, de titularidad de Bind PSP, asociada a la entidad.
- Vía API la entidad puede: instruir transferencias salientes en USD a cualquier CBU; recibir webhook por cada transferencia entrante (con CUIT del originante); consultar histórico de transferencias con filtros; consultar saldo disponible.
- Requisitos: CBU en USD de Bind PSP exenta asociada a la entidad, entidad creada en el sistema de Agente de Cobros y Pagos, credenciales de API exclusivas.
- Fuera de scope (a definir/priorizar): reportes batch, acceso vía portal web/admin, conciliación automática, consumo por Wallet services, cuenta corriente por usuario reflejando movimientos por CBU, potenciación con API Broker (remuneración de saldos / compra de dólar MEP), API PSI → CBU en USD por usuario.
- Documentación pública ya publicada: [Cómo recibir transferencias en USD](https://psp.bind.com.ar/developers/apis/guia-agente-de-cobro-usd).

### Diferenciación CBU vs CVU en webhook entrante

Al recibir un webhook de transferencia (`type=transfer.cbu.received`), Financial debe determinar a qué collector corresponde:
1. Si el body incluye el campo `cbu`, el collector es el que tiene ese CBU asociado.
2. Si no, se extrae el número de subcuenta del `net_id` del webhook (6ta columna al partir por guiones, ej. `NSBT-1-1-749049-66-4-20250605-241-30-7270-1` → subcuenta `4`) y se matchea contra el número de subcuenta del `account_id` del collector (4ta columna, ej. `20-1-749049-4-50` → subcuenta `4`).

Si es una transferencia a CVU, se sigue tratando como siempre (se determina el CVU destino y se induce el collector). El ajuste (`[US] Interpretar Webhook CBU received`) modificó la estructura del body y requirió cambios coordinados en Financial y Aggregator.

## 2. Cluster de bugs de la puesta en producción (USD)

La habilitación de USD sobre el circuito CVUCollect (pensado originalmente solo para ARS) generó un cluster de bugs de moneda/formato, todos bajo la etiqueta `🧲 CVUCollect`:

- **`CBU_INVALID_CURRENCY`**: transferencias en USD entre collectors devolvían error de Wallet.Bind.Repository.GetIncomingTransfer; ocurría de forma intermitente — para un collector funcionaba y para otro no, aun con la misma configuración de cuenta exenta en USD.
- **Balance sin moneda**: al consultar saldo de una cuenta USD (`GET /v1/Balance/:id`), la respuesta no informaba el tipo de moneda de la cuenta.
- **Webhook saliente no se envía**: transferencias salientes en USD completadas en API Bank no disparaban el webhook de resolución; quedaban en la tabla `Transferences` con `IsProcessed=0`.
- **Transferencias entrantes no se registran**: para ciertos collectors, transferencias entrantes confirmadas por banco/consulta de saldo no aparecían registradas en `Transferences` (sólo se veían las del collector contraparte).
- **Formato de webhook USD ≠ formato webhook ARS**: campos `created`/`start_date`/`end_date` con formato de fecha distinto (sin zona) y sin `Z`; además `object`, `bank_routing.scheme`, `origin_debit`/`origin_credit` llegaban vacíos/null en USD cuando en ARS traían valor.
- **Conciliación no soporta USD**: el endpoint de conciliación de transferencias por CBU en dólares usaba internamente el tipo de transacción `TRANSFER` en vez de `TRANSFER-CVU`, devolviendo siempre `conError` — se corrigió apuntando al endpoint correcto (`[US] Conciliar transferencias con CBU`).
- **StateMonitor inconsistente**: transferencias salientes que resultaban `COMPLETED` igual quedaban con `IsProcessed=0` en StateMonitor (debían aparecer sólo las que no llegaron a un estado definitivo).
- **Transferencias salientes en `IN_PROGRESS` indefinidamente**: no entraban al circuito de StateMonitor para reconsultar y actualizar su estado final.
- **Consulta de transferencia por ID no filtra**: el endpoint de consulta (header `id`) devolvía todas las transferencias del collector en vez de sólo la solicitada.
- **No se puede transferir a alias**: sólo se soportaba destino por CBU/CVU explícito, no por alias.
- **Latencia del envío de webhook acopla al request de transferencia**: si la URL de notificación del cliente fallaba (ej. 404), los reintentos de envío de webhook (~7s con 3 retries) demoraban la respuesta del propio endpoint de creación de transferencia — quedó pendiente separar ambos procesos (`[US][OBS][RxT] Separar el proceso de envío de transferencia de envío de webhook`, estado "Refinar" al cierre del relevamiento).

## 3. Consulta de saldo — Cuenta Recaudadora en ARS

Feature simple y anterior a USD: endpoint GET para que un collector que consume directamente las APIs de Financial obtenga el saldo actual de su cuenta recaudadora, con un timestamp que indica a qué momento exacto corresponde ese saldo (usa el endpoint de API Bank de consulta de cuentas).

- **Bug corregido**: el endpoint pedía el `collector_id` como parámetro de request cuando debía inferirse directamente del token de autenticación (`[OBS][CuentaARS] El endpoint pide el collector id`).

---
*Fuente: Notion histórico, Epics "Astro: Agente de cobros y pagos en USD" (19 SP) y "Astro: Consulta de saldo. Agente de cobros y pagos en ARS" — ingesta 2026-07-06.*
