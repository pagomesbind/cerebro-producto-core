# Dólar CCL — Wallet

> Estado: en producción.

Configuración del circuito de Dólar Contado con Liquidación (CCL) para organizaciones de Wallet (modelo COMBI genérico y caso PYXPAY), y mecánica funcional completa del flujo de compra vía API (proveniente del Notion histórico, Epic "Compra CCL MVP" — primer cliente: Inter/Banza).

---

## 1. Configurar organización de Wallet para Dólar CCL — modelo COMBI (STG+PROD)

Basado en el instructivo elaborado por Nicolás Colón.

### Índice de pasos

1. Configuración / creación de Cuenta Comitente.
2. Creación de Cargos en Wallet Calculador de Costos.
3. Solicitud de seteo de especificaciones en `WalletCuentaDB`.
4. Parametrización de la organización con Poincenot en `WalletInvestmentServiceDB`.

### 1. Configurar o crear Cuenta Comitente

Configuración o creación de la Cuenta Comitente que operará en Poincenot. Dos escenarios posibles:

**Opción 1 — Única Cuenta Comitente (similar a Coinbase):** la organización canaliza toda la operatoria de sus usuarios a través de una única cuenta propia con su propio CUIT.
- Acción requerida: comunicarse con Poincenot/IVSA para obtener un Id externo de Cuenta Comitente.
- Configuración: configurar este Id en la tabla `WalletInvestmentServiceDB.CuentasComitentes`.
- Precondición: la Cuenta de Wallet y los CVU ya deben existir y estar habilitados.
- Ejemplo de consulta SQL:

```sql
SELECT *
FROM [dbo].[CuentasComitentes]
Where OrganizacionId = 73
```

(Muestra CuentaId **276358**, OrganizacionId **73**, IdExterno **99**, ProcesadorId **1**, Estado **ACTIVA**.)

**Opción 2 — Cuenta Comitente por Cliente:** la organización provee Cuenta de Wallet, CVU y Cuenta Comitente a cada cliente bajo el CUIT/CUIL de ellos mismos.
- Acción requerida: dar de alta la Cuenta Comitente.
- Endpoint: `https://portal-staging-qrbind.epays.services/api-details#api=entidad-wallet-cuenta-v1&operation=post-api-v1-201-cuentaycvuconcuentacomitente`

### 2. Creación de cargos en el Calculador de Costos

Se deben crear **seis cargos en total**: tres para compra, tres para venta. Los valores pueden variar y deben consultarse según el contrato.

| Flujo | Cargo | Descripción |
|---|---|---|
| Compra CCL | Cargo X | Comisión de BindPSP para el flujo de compra |
| Compra CCL | Cargo Y | Deprecado, pero debe configurarse |
| Compra CCL | Cargo Z | Comisión de IVSA para el flujo de compra |
| Venta CCL | Cargo X | Comisión de BindPSP para el flujo de venta |
| Venta CCL | Cargo Y | Deprecado, pero debe configurarse |
| Venta CCL | Cargo Z | Comisión de IVSA para el flujo de venta |

**Configuración en Swagger:** API `Wallet.CalculadorCostos`.
- Swagger Staging: `http://10.210.1.97/swagger/index.html`
- Swagger Producción: `http://10.22.0.92/swagger/index.html`
- Endpoint: `POST /api/v1/Cargo`

**Campos a completar:**

| Campo | Valor | Notas |
|---|---|---|
| `x-entidad` | Id de Organización | Id de Organización a configurar |
| `nombre` | Descripción | Descripción a utilizar |
| `tipo` | `Comision` | Siempre |
| `tipoCalculo` | `Porcentaje` | Siempre |
| `tipoRecurrencia` | `Operacion` | Siempre |
| `importe` | `0` | Siempre, a menos que se establezca un importe fijo |
| `porcentaje` | Valor numérico | Dependiendo del cargo (ej: 0.97) |
| `tipoTransaccionId` | `9` (Compra STG) / `12` (Venta STG) | `4` (Compra PROD) / `7` (Venta PROD) |
| `entidadIdExterno` | Id de Organización | Id de Organización a configurar |

Ejemplo de body (Cargo X Dólar CCL Compra, `x-entidad = 123`, `entidadIdExterno = 123`):

```json
{
  "nombre": "Cargo X Dolar CCL Compra Nombreorga",
  "tipo": "Comision",
  "tipoCalculo": "Porcentaje",
  "tipoRecurrencia": "Operacion",
  "tipoTransaccionId": 9,
  "importe": 0,
  "porcentaje": 1,
  "codigoTipoTransaccionExterno": null,
  "codigoTipoTransaccionDevolucionExterno": null,
  "entidadIdExterno": 123
}
```

### 3. Solicitud de seteo de especificaciones (Fintexa)

Solicitar a un responsable de Fintexa con permisos de escritura en la base de datos que inserte los registros correspondientes.

- Base de datos / tabla: `WalletCuentaDB.Especificaciones`.
- El campo `IdTabla` debe reemplazarse por el Id de la Organización a configurar.

Ejemplo de registros (Coinbase en Staging):

| Id | Scope | Tabla | IdTabla | Clave | Valor |
|---|---|---|---|---|---|
| 66 | Cuentas | Organizaciones | 73 | CUENTA_COMITENTE_IVSA_HABILITADA | true |
| 70 | Operaciones | Organizaciones | 73 | DOLAR_COMBI_HABILITADO | true |

### 4. Solicitud de parametrización (Fintexa)

> ⚠️ Nota de la fuente: este paso está marcado "REVISAR CON GOMES!!!!!" en el documento original — pendiente de confirmación.

Solicitar a un responsable de Fintexa con permisos de escritura que inserte los registros de parámetros.

- Base de datos / tabla: `WalletInvestmentServiceDB.ParametrosOrganizaciones`.
- El campo `OrganizacionId` debe reemplazarse por el Id de la Organización a configurar.

Ejemplo de consulta SQL:

```sql
SELECT *
FROM [dbo].[ParametrosOrganizaciones]
where OrganizacionId = 73
and CanalOperacion = 'CCL'
```

Ejemplo de registro (Coinbase en Staging):

| Id | OrganizacionId | PspOwner | Entidad | Procesador | CanalOperacion |
|---|---|---|---|---|---|
| 4 | 73 | COIN | COIN | POICENOT | CCL |

---

## 2. Configuración Dólar CCL — caso PYXPAY

**Objetivo:** configurar el circuito de Dólar CCL para PYXPAY, incluyendo creación del CVU, habilitaciones necesarias y configuración de cargos.

### 1. Crear CVU

- CuentaId: `649162`

### 2. Configuración de cargos

Configurar los cargos X, Y y Z, tanto para Compra como para Venta (ticket a FINTEXA).

### 3. Configuraciones en base de datos

**3.1 `WalletInvestmentServiceDB` — Cuentas Comitentes.** Insertar en `[WalletInvestmentServiceDB].[CuentasComitentes]`:

| CuentaId | OrganizacionId | IdExterno | ProcesadorId | Estado |
|---|---|---|---|---|
| 649162 | 126 | 99 | 1 | ACTIVA |

**3.2 `WalletCuentaDB` — Especificaciones.** Insertar en `WalletCuentaDB.[Especificaciones]`:

| Scope | Tabla | IdTabla | Clave | Valor |
|---|---|---|---|---|
| Cuentas | Organizaciones | 126 | CUENTA_COMITENTE_IVSA_HABILITADA | true |
| Operaciones | Organizaciones | 126 | DOLAR_COMBI_HABILITADO | true |

**3.3 `WalletInvestmentServiceDB` — Parámetros de Organización.** Insertar en `[WalletInvestmentServiceDB].[ParametrosOrganizaciones]`:

| OrganizacionId | PspOwner | Entidad | Procesador | CanalOperacion |
|---|---|---|---|---|
| 126 | BIND_COIN | COIN | POICENOT | CCL |

### 4. Definición de cargo (ejemplo)

Swagger: `http://10.210.1.97/swagger/index.html` (base `WalletCalculadorCostosDB`).

```json
{
"nombre":"Cargo Y - Dolar CCL - PYXPAY",
"tipo":"Comision",
"tipoCalculo":"Porcentaje",
"tipoRecurrencia":"Operacion",
"tipoTransaccionId":4,
"importe":0,
"porcentaje":0,
"codigoTipoTransaccionExterno":null,
"codigoTipoTransaccionDevolucionExterno":null,
"entidadIdExterno":44
}
```

### 5. Swagger de referencia

`http://10.22.0.92/swagger/index.html`

---

## 3. Mecánica funcional del flujo de Compra de Dólar CCL (API para organizaciones)

> Fuente: Notion histórico, Epic **"Compra CCL MVP"** (⭐ Epics). Producto API-first para organizaciones de Wallet; el primer cliente fue **Inter/Banza**. El desarrollo core salió entre las versiones W 37 y W 48, con ajustes posteriores hasta W 62.

### 3.1 Arquitectura de la integración

- La compra/venta de dólar CCL se ejecuta contra el **broker IVSA**, cuya API ("API Broker") es provista por **Poincenot** (proveedor tecnológico). Bind PSP construyó un **wrapper** propio sobre API Broker IVSA-Poincenot.
- Cada usuario final opera a través de una **Cuenta Comitente** (entidad propia en Wallet, creada para este producto). Ver §1 para los dos modelos: cuenta comitente única de la organización vs. una por cliente.
- Se creó un **endpoint de onboarding específico** ("flujo Inter") que da de alta en un solo paso: cuenta de Wallet + CVU + Cuenta Comitente.
- **API Posicionamiento**: para el alta de comitentes se integraron códigos ISO de provincias y países, y los códigos propios de Poincenot (incluye la recuperación del código Poincenot de *nacionalidad*). El alta de cuentas de usuarios no argentinos quedó pendiente (deuda conocida del MVP).
- La cotización CCL se **consulta y cachea en paralelo cada X minutos**, y la DDJJ se cachea cada X horas; el endpoint de cotización expuesto al cliente lee del caché. Poincenot confirmó que su API de cotización devuelve el último valor disponible si el mercado está cerrado.
- Los **webhooks de IVSA** son el disparador principal de los cambios de estado (con un esquema de polling de contingencia, ver §3.5).

### 3.2 Modelo de precios: X + Y

- **X** = comisión de Bind PSP. **Y** = costo adicional para cubrir el riesgo de operar **fuera de horario de mercado** (el precio puede moverse hasta que el mercado abra).
- `precioCompra = precio IVSA + X + Y` · `precioVenta = precio IVSA − X − Y`.
- **Y = 0 si es horario de mercado**; solo aplica fuera de horario.
- X e Y se parametrizan **como porcentaje, por organización + tipo de operación**, con endpoints propios de consulta y actualización.
- El "Cargo Y" que aparece en la configuración de cargos (§1.2) quedó **deprecado pero debe configurarse igual** — el cálculo vigente del riesgo fuera de horario se hace por esta parametrización.
- Existió además un **Cargo Z** = comisión de IVSA (§1.2).

### 3.3 Flujo en dos pasos: Intención → Ejecución

**Paso 1 — Intención de compra** (`POST` iniciar compra):
- Request: `idCuenta`, `monto`, `idExterno` (opcional, único por organización), bearer token OAuth2 con la entidad.
- El sistema consulta "gastos de compra" a API Broker usando `amount = monto − X − Y` y arma la intención con: `montoOrdenado` (lo que va al mercado = monto − cargo), `montoEjecutadoEstimado`, `vueltoEstimado`, `totalGastos` (gastos IVSA + cargo Bind), `precioDolarCotizado` (precio IVSA + X+Y), `precioDolarCclReferencia` (precio IVSA puro), fechas de inicio/fin de operación (la operación tiene *parking*: termina el día hábil siguiente), `mercadoAbierto`, fecha de vencimiento de la intención (parametrizable por tipo de dólar).
- Validaciones al crear: saldo suficiente, `idExterno` no repetido, precio de referencia recuperable (si falla, no se crea nada).
- **Estados de la intención**: `Creada` → `En proceso` → `Completada parcial` → `Completada` | `Rechazada` | `Expirada` (más el estado operativo `A Auditar`, ver §3.5).

**Paso 2 — Ejecución** (`POST` ejecutar compra, por `id` o `idExterno` de la intención):
- Validaciones previas: cuenta origen habilitada, cuenta IVSA asociada, intención no vencida. Si falla → HTTP 422, intención Rechazada, no se crea operación.
- **Débitos separados para contabilizar correctamente** (decisión de negocio): primero un comprobante de débito "Cargo por compra de dólar CCL" (= monto × X·Y) y luego otro "Compra de dólar CCL" (= `montoOrdenado`). Si falla cualquiera, se reversa el/los realizados con créditos análogos. Si la operación luego falla o es rechazada en API Broker, se reversan ambos.
- `vuelto = montoOrdenado − montoInvertido`, y se acredita al usuario con su propio comprobante de crédito.

### 3.4 Las "dos patas" de la operación

La compra de CCL se materializa en el mercado como **compra de un bono en pesos (pata 1) y venta de ese bono en dólares (pata 2)** — en la evidencia real: compra de `BYMA.AL30` en T0 (ARS) y venta de `BYMA.AL30C` (USD) al día hábil siguiente.

- **Pata 1 completada** (mismo día): se actualiza la intención (estado `Completada parcial`, `montoEjecutado`, vuelto), se acredita el vuelto, y se envía el **primer webhook** a la organización (id/idExterno, monto original, monto ejecutado, vuelto, estado, id de operación, tipo de dólar).
- **Pata 2 completada** (día hábil siguiente): se actualiza la intención (`Completada`, `montoDolares`), la Operación pasa a `Aprobada`, y se envía el **segundo webhook** (mismos datos + monto de dólares comprado).

### 3.5 Esquemas de contingencia (si no llegan los webhooks de IVSA)

- **Pata 1**: si a las 3 hs de creada la operación no llegó el webhook, se consulta el estado en API Broker **cada 5 minutos hasta las 20:00 (ARG)**. Si a esa hora no hay estado definitivo → Operación e intención pasan a **Rechazada** ("No se registró concreción de la compra del bono") y se devuelve el dinero.
- **Pata 2**: si a las 11:00 (ARG) del día hábil siguiente no llegó el webhook, ídem polling cada 5 min hasta las 20:00. Si no se confirma → pasa a **A Auditar** (no se rechaza automáticamente: la plata ya está invertida y requiere revisión manual).

### 3.6 Bugs y aprendizajes reales (llegaron a producción)

- **Días no hábiles no considerados**: el cálculo de "día hábil siguiente" para la pata 2 no contemplaba fines de semana/feriados — una compra ejecutada un viernes pasaba a `AUDITAR` el fin de semana en lugar de esperar al lunes 20:00. Se corrigió, pero **reincidió** (hubo una OBS posterior "seguimos sin validar días hábiles para cambios de estado"). Aprendizaje: toda lógica de tiempos de este flujo debe usar calendario de días hábiles bursátiles, no días corridos.
- **Webhooks de IVSA que llegan pero no se procesan**: en producción hubo intenciones que no cambiaban de estado ni por webhook ni por el polling de contingencia. Causa observada: el webhook entrante de IVSA **no se podía vincular a la intención** (el `CorrelationId` y el body no alcanzaban para matchear), y el registro de llegada fallaba de forma sistemática para toda la casuística. Aprendizaje: el matching webhook→intención necesita una clave explícita (id de operación de broker) y trazabilidad de webhooks entrantes.
- **Intención en `COMPLETADA_PARCIAL` con webhook de pata 2 OK** (caso límite del ordenamiento de eventos entre patas — quedó "No aplica" tras análisis).
- **Error 500 en el endpoint de intención de compra** (corregido).
- **No crear comprobante de comisión cuando X = 0** (ajuste tardío: evita comprobantes de $0).
- Deuda conocida al freeze del Notion: validación de **mínimo de compra** de dólar CCL quedó pendiente; **alta de cuentas de usuarios no argentinos** pendiente; en el flujo Inter quedó en refinamiento la recuperación del código Poincenot de nacionalidad para el alta de comitente (back).
- **Correcciones de comisiones en Combi** ([WS-588](https://bindpsp.atlassian.net/browse/WS-588), publicado W 69 2026-04-29): se persiste el `MontoAObtener` calculado en la creación de la Intención (nuevo campo en `dbo.Intenciones`); el `montoAObtener` de la **ejecución** pasa a calcularse **neto de todas las comisiones** (antes iba bruto de las comisiones de Bind PSP, inconsistente con la creación); y el `montoObtenido` que informa Poincenot (bruto de su comisión IVSA del 0,97%) se recalcula a neto — con la advertencia de que restar el porcentaje directo pierde decimales, por lo que se definió calcularlo como `TotalInvested / PrecioDolarReferencia` validando que no haya diferencia grave contra lo informado por IVSA.
- **Cancelación de operaciones CCL — publicada "EN QA", con conflicto abierto con PCNT** ([WS-181](https://bindpsp.atlassian.net/browse/WS-181), publicado W 69 en estado EN QA): no existía forma de cancelar operaciones de dólar CCL (Inter ni Combi); se construyó el endpoint que cancela la intención, refleja el estado en la Operación de Wallet y reversa los comprobantes. El desarrollo quedó **trabado en QA por un problema del lado de Poincenot**: una intención que de nuestro lado está "a auditar" figura "aprobada" en PCNT, y PCNT usa su propio estado para rechazar la modificación — al cierre de esta ingesta el reclamo a PCNT seguía sin resolverse. Contexto: existen casos donde Poincenot hace validaciones **posteriores** a la confirmación de la compra del bono y reversa la transacción de su lado.
- **No se notificaban las Ventas CCL exitosas** ([WS-306](https://bindpsp.atlassian.net/browse/WS-306), publicado W 67 2026-01-27): el webhook de Venta de dólar CCL (eventoId 12) solo salía en rechazos — nunca en aprobaciones (verificado en STG y PROD) — y además el `mensajeId` no viajaba en el JSON. Corregido: notificación también en éxito, con toda la información.
- **Ventas aprobadas sin comprobantes de Venta y Cargo** ([WS-107](https://bindpsp.atlassian.net/browse/WS-107), publicado W 65.1 2025-11-26, reclamo org 20 en PROD): intenciones de venta aprobadas cuyos comprobantes nunca se crearon.
- **DDJJ de la organización equivocada** ([WS-160](https://bindpsp.atlassian.net/browse/WS-160), W 66): una cuenta de Coinbase (org 73) obtenía aleatoriamente la DDJJ de Inter al crear la intención — la DDJJ es **por organización** y el mecanismo de selección fallaba de forma intermitente.
- **Error 422 "habilitada para combi pero no se obtuvo hash"** ([WS-363](https://bindpsp.atlassian.net/browse/WS-363), W 67): no era un bug del endpoint de cotización — la organización estaba configurada en modo **INTER** y se la consultaba como Combi. Síntoma típico de configuración cruzada de modo CCL.
- **Race conditions entre pods** ([WS-374](https://bindpsp.atlassian.net/browse/WS-374)/[WS-375](https://bindpsp.atlassian.net/browse/WS-375), W 67): los background services (`WorkerService` de Operaciones e `IntencionesCCLPendientesBackgroundService` de Investment) corren en 2+ pods en paralelo y pisaban el mismo trabajo — se agregó un delay aleatorio (1-5 s) entre instancias.

**Correcciones al flujo de venta y comprobantes de cargo (W 71 / W 71.4 FIX, 2026-07-15 a 2026-07-30):**

- **Interpretación de webhooks Poincenot con estado `ERROR`** ([WS-1217](https://bindpsp.atlassian.net/browse/WS-1217), W 71): Poincenot tiene un bug recurrente — operaciones rechazadas de su lado a veces devuelven `GENERAL_ERROR` genérico al consultarlas en vez de la info real de rechazo. Poincenot confirmó que el estado que viaja en los webhooks "Pata 1"/"Pata 2" es el fehaciente. Nueva lógica: si el WH Pata 1 de **compra** viene `ERROR` y la consulta posterior da `GENERAL_ERROR` → rechazar, devolver fondos, avisar por webhook a la organización. Si es el WH Pata 2 de compra → mantener el flujo actual (queda en "Auditar", intervención operativa, porque si ocurrió Pata 2 ya se compró el bono). Si es el WH Pata 1 de **venta** (no existe Pata 2 en ventas) → rechazar y avisar por webhook.
- **Orden de comprobantes en venta corregido** ([WS-1217](https://bindpsp.atlassian.net/browse/WS-1217)): antes se debitaba primero el cargo de comisión (exigiendo saldo disponible del cliente) y recién después se acreditaba el monto obtenido — invertido: ahora primero se acredita `montoObtenido`, después se debita el cargo.
- **Fórmula de comisión de venta corregida** ([WS-1217](https://bindpsp.atlassian.net/browse/WS-1217)): pasa de `monto × precioDolar × porcentajeCargo` a `totalObtained × porcentajeCargo` (bug introducido entre el 2026-02-02 y el 2026-02-10, sin ticket propio). También se corrige `montoObtenido` para que sea `totalObtained − ComisionInterna` (lo que el cliente ve acreditado), no el bruto.
- **`MontoObtenido` no se actualizaba si la compra se resolvía el mismo día** ([WS-1427](https://bindpsp.atlassian.net/browse/WS-1427), W 71.4 FIX): cuando una compra de dólar CCL pasaba PENDING → APPROVED → EXCHANGED en el día, el campo `MontoObtenido` (tabla `dbo.Intenciones`) no se pisaba con el `totalObtained` real — el cliente no podía saber cuánto obtuvo. Fix: pisar siempre que el estado obtenido en Poincenot sea `EXCHANGED`, sin importar cuándo ocurra ni por qué mecanismo (webhook o reintento automático); nunca pisar en estado `APPROVED` intermedio.
- **Reubicación de IDs de comprobante de cargo** ([WS-1285](https://bindpsp.atlassian.net/browse/WS-1285), W 71.4 FIX): los IDs de comprobantes de cargo se guardaban en campos con nombres contraintuitivos. Ahora: cargos debitados (compra o venta) → campo `CargoDebitoComprobanteId`, expuesto como `cargoDebitoComprobanteId` en `GET Intencion` y en `POST EjecutarCompraCCL`. Cargos acreditados por devolución de error en compra → campo `CargoCreditoComprobanteId`, expuesto como `cargoCreditoComprobanteId` en los mismos endpoints.

### 3.6bis Despliegue V72 aprobado pese a regresiones sin cerrar (2026-08-18)

> Fuente: mail "Re: MINUTA: Análisis de riesgo Emisión V 72" (2026-08-18), minuta de la reunión de PRE-Despliegue V72 del mismo día, 14:30.

En la reunión de PRE-Despliegue de Emisión V72 (18/08/2026) se aprobó avanzar con el despliegue de los cambios de Dólar CCL pese a no poder finalizar las pruebas de regresión en ambiente de homologación, por errores persistentes originados en **Apibank** (ambiente de homologación, no productivo). Se confirmó que el impacto de este bloqueo es mínimo — afecta solo a un ticket de compra de dólar fallida detectado desde visión interna. Para no desenfocar al equipo de QA (Ana), se dispuso centralizar toda la comunicación técnica sobre este tema exclusivamente a través de Andrea Orsini.

Queda en Stand-by/Parking Lot la corrección definitiva de los errores de Apibank (reportados vía Poison) que bloquean hoy las pruebas end-to-end de CCL en ambientes no productivos — no resuelto para el despliegue del 19/08.

### 3.7 Venta de Dólar CCL (mecánica espejo)

> Fuente: Epic histórica **"Venta CCL MVP"**.

- Mismo modelo de dos pasos (intención → ejecución) y dos patas, pero invertido: se vende un bono comprado en dólares para obtener pesos.
- Variables de negocio en la ejecución: `montoNeto`, `precioDolar`, `totalGastos` (a mostrar al cliente), `monto` (ingresado), `montoBruto`, `montoInvertido`, `montoObtenido` (resultado final en pesos, neto de comisión).
- Webhook de aviso al completarse la venta con la información de la operación.
- Validaciones antes de ejecutar: cuenta habilitada, CVU no eliminado, cuenta comitente asociada, intención no expirada.
- **Soporte multi-entidad** agregado sobre el wrapper base.
- **Bug real (causa raíz confirmada)**: intenciones que terminaban `APROBADA` pero sin `montoInvertido`/`montoObtenido` — se verificó que ambos webhooks de IVSA (pata 1 y pata 2) sí llegaban y se hacía el GET correspondiente, pero el valor de `montoObtenido` no se estaba tomando del response en el flujo de captura. De 61 intenciones aprobadas relevadas, solo 36 tenían ambos atributos completos. Aprendizaje: `montoInvertido` debe capturarse en el webhook de pata 1, `montoObtenido` en el de pata 2 — ambos son pasos de guardado independientes, no un cálculo derivado, y uno de los dos no se estaba persistiendo.
- Otros ajustes de negocio en producción: costo Z (comisión IVSA) expuesto/ajustado, validación de diferencia entre `montoEsperado` y `montoAObtener`, validación de diferencia entre `precioDolarReferencia` y `precioDolar`, cambio de nomenclatura de cotización a `buyPrice`/`sellPrice`.

### 3.8 Modelo "Combi": precio fijo y operatoria fuera de horario de mercado

> Fuente: Epic histórica **"Compra/Venta CCL Combi: precio fijo y fuera de horario de mercado"**. Extiende el flujo estándar (§3.1-3.7) para organizaciones marcadas `combi = true` en IVSA — mismo endpoint de API Broker, pero con comportamiento distinto server-side según la configuración de la organización.

- **Cotización**: para organizaciones Combi, **nunca se usa el caché** (§3.1) — cada consulta va en vivo a IVSA, porque la respuesta incluye un **`hash`** de precio con su propio tiempo de expiración (`priceLimitTime`) que cambia en cada tiro. La respuesta a la organización debe incluir `buyPrice`, `sellPrice`, `timestamp`, `hash` y `priceLimitTime`.
- **Crear intención**: la organización debe enviar `priceHash` (el hash recibido en la cotización); si combi=true y no lo envía, API Broker devuelve error, así que Bind valida el campo antes de llamar. El `priceHash` se guarda en la intención para usarlo al ejecutar. La fecha de expiración de la intención se alinea al `priceLimitTime` del hash (con fallback al cálculo estándar si API Broker no lo informa en ese endpoint).
- **Ejecutar intención**: se reenvía el `priceHash` guardado. Si IVSA lo considera inválido/vencido, responde `INVALID_PRICE_HASH` — la intención pasa a `RECHAZADA` con ese motivo.
- Si la organización no es Combi, opera exactamente como el flujo estándar (§3.1-3.7).
- Aplica simétricamente a compra y venta.

### 3.9 Decisiones de exposición al cliente (API)

- No exponer a la organización campos internos: `montoOrdenado`, `intencionRespuestajson`, `operacionRespuestajson` (responses crudos del broker) se ocultaron del GET de intención; a la vez se agregaron los campos de negocio que faltaban (`montoEsperado`/`montoAObtener` en ejecutar compra y GET, `horarioMercado` en GET cotización, info para el **boleto** en el GET de intención).
- La DDJJ (declaración jurada de inversor) se solicita con id + timestamp de aceptación (requerimiento de Inter); el modelo quedó preparado para validarla al momento de la compra.
