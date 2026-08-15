# Criptomonedas — Compra/Venta (API) y caso DIRECTA — Wallet

> Estado: en producción.

> Fuente: Notion histórico, Epics **"API crypto: Compra/venta"** (~120 SP, motor genérico) y **"DIRECTA Crypto"** (~55 SP, cliente específico que reutiliza gran parte del backlog de la Epic genérica — ambas comparten ~11 tickets). Proveedor: **Lirium** (exchange cripto), en paralelo/complemento a IVSA-Poincenot que se usa para [Dólar CCL](dolar_ccl.md) y [Dólar FX](dolar_fx.md).

## 1. API crypto: Compra/Venta — motor genérico

### 1.1 Alcance

Una organización de Wallet debe poder **comprar y vender cualquier criptomoneda con pesos ARS**, y guardar la posición en una billetera cripto propia (dirección/"address" en Lirium).

- Consulta de cotización de compra/venta en ARS, **24/7** (a diferencia de CCL/FX que dependen de horario de mercado bursátil/MULC).
- Consulta de cotización de todas las criptos disponibles, indicando con qué moneda FIAT se opera.
- Intención de compra/venta iniciable **por dos caminos**: indicando el importe de cripto a operar, o el importe de FIAT a utilizar.
- **Supuesto de diseño clave**: la ejecución de la compra/venta de dólar CCL asociada a la operatoria cripto **puede ejecutarse de forma asíncrona** y no bloquea completar la operación cripto de cara al usuario — es decir, el usuario ve su cripto acreditada antes de que Bind PSP termine de compensar internamente contra CCL.

### 1.2 Relación con Dólar CCL — el diseño combina ambos proveedores

La arquitectura consume **Lirium** (cripto) y **API Broker/IVSA-Poincenot** (CCL) en conjunto: los pesos recaudados por la venta de cripto (o a comprometer en la compra) se compensan contra el circuito de dólar CCL ya existente (ver [dolar_ccl.md](dolar_ccl.md)) — reutilizando el wrapper y el modelo operativo ya construido para CCL en vez de duplicar lógica de mercado de cambios.

### 1.3 Confirmación y mantenimiento post-MVP (Jira PRD-9)

> Fuente: Jira `bindpsp.atlassian.net`, IDEA **PRD-9** "API Cripto: MVP - Compra, venta y tenencia de cualquier moneda" (Finalizada) → Epic **WS-10** (mismo Epic ya documentado en §1 vía Notion). Confirma que el MVP se lanzó y agrega una cola corta de ajustes menores post-lanzamiento, todos ya Finalizados: estandarización a camelCase de query params de consulta (antes en PascalCase), mensaje de error genérico en vez de exponer el nombre interno del método que falló (`Wallet.InvestmentService.Lirium.Repository.CreateOrderBuy()`), y corrección de `fechaHoraVencimiento` inconsistente en la consulta de una intención de compra/venta (el valor no reflejaba los 120 segundos reales de vigencia).
- **Gap de documentación pendiente** (registrado en un comentario de la IDEA, sin resolver a la fecha de esta ingesta): falta documentar el flujo de **creación de cuenta cripto** para integradores externos.

## 2. Caso DIRECTA — expatriación de fondos vía cripto (compliance-driven)

### 2.1 Problema de negocio real

**DIRECTA** (oportunidad de negocio traída por **Astropay**) es una entidad que presta servicios de cobranza a casas de apuestas online. Necesita recaudar en pesos argentinos y sacar esos fondos al exterior, pero por tratarse de un rubro de riesgo (juegos/apuestas), **el área de Cumplimiento de Bind PSP no permite** que DIRECTA recaude pesos a nombre de su cliente y luego los expatríe directamente comprando dólar CCL a nombre de DIRECTA o de Bind PSP. **La solución cripto sortea esa restricción normativa**: los fondos se usan para comprar criptomonedas (destino de fondos distinto y justificable), no para comprar divisas directamente.

### 2.2 Modelo de titularidad (decisión de diseño clave)

- Cada usuario final tiene su propia cuenta Wallet + CVU + address cripto, pero **la titularidad de la cuenta+CVU es de DIRECTA**, no del usuario final — el onboarding valida al usuario final (KYC, legajo) pero la cuenta resultante queda a nombre de DIRECTA. El **address cripto en Lirium sí queda a nombre del usuario final**.
- Cobro por **transferencia a CVU** o por **QR interoperable** (aceptador 184), ambos bajo titularidad de DIRECTA; el QR se liquida en línea.

### 2.3 Flujo end-to-end

1. Plataforma de apuestas online pide comprar créditos → consulta cotización cripto→pesos para informar cuánto pagar.
2. Usuario paga (transferencia a CVU asignado o QR) → los pesos se acreditan como saldo en la cuenta (titularidad DIRECTA) del usuario.
3. **En cualquier momento del día** (no en línea con el cobro), la organización convierte los pesos recaudados en criptomonedas en el address del usuario.
4. La organización transfiere las criptos desde el address del usuario hacia un address propio de DIRECTA.
5. DIRECTA convierte esas criptos a dólares en una cuenta en EE.UU. mediante su acuerdo con Lirium (fuera del alcance de Bind PSP).
6. Para **pagar premios**: camino inverso — venta de cripto y transferencia de los pesos resultantes al CBU/CVU del usuario final.

### 2.4 Operatoria interna de Bind PSP (compensación de CCL)

Administración de Bind PSP concilia diariamente lo operado en Lirium, calcula el neto de compras/ventas de cripto del día, y **compra o vende dólares CCL para compensar a Lirium** por lo utilizado en la operatoria — replicando a nivel de tesorería lo que el cliente final operó en cripto. Quedó parametrizable por organización si cada operación cripto dispara en línea su operación CCL asociada o no (por diseño, para DIRECTA se decidió que **no** sea en línea — solo se registra el cambio en el momento y se compensa después, ver §1.1).

### 2.5 Alcance construido vs. pendiente (MVP)

**MVP lanzado**: recaudar con transferencia a CVU + operar cripto (comprar/vender, consultar cotización y saldo, onboarding con cuenta a nombre de la organización).

**Quedó para etapas posteriores** (verificar estado real en Jira): recaudar con QR interoperable (mencionado como "próxima etapa" en el PRD pese a que el modelo de titularidad del QR ya está definido en §2.2), transferir criptos entre distintas addresses como funcionalidad expuesta, convertir criptos a dólares en una cuenta del exterior de forma integrada (hoy es un proceso manual/externo de DIRECTA-Lirium), y soporte multi-entidad contra Lirium.

## 3. Publicación y mantenimiento en producción (vía `/sync_releases`)

- El grueso del motor cripto/DIRECTA se publicó en **W 65** (2025-11-17, lanzamiento del espacio WS): webhooks de compra/venta e integración del webhook de Lirium al flujo (WS-11/12/13), consulta de intenciones (WS-14).
- **El vencimiento de una intención cripto lo fija Lirium dinámicamente** ([WS-75](https://bindpsp.atlassian.net/browse/WS-75), publicado W 66 2025-12-15): no es un valor fijo (los "120 segundos" que se creía eran una referencia incorrecta) — Bind PSP setea el vencimiento que Lirium establece por orden, que puede variar (se observaron ~45 s). Definición funcional explícita de Fintexa. Impacta a integradores que asuman una vigencia fija.
- **Contrato camelCase** ([WS-88](https://bindpsp.atlassian.net/browse/WS-88), W 66): el endpoint de consulta cripto pedía query params en PascalCase — homogeneizado a camelCase como todo Wallet.

## Ver también

- [dolar_ccl.md](dolar_ccl.md) — circuito de dólar CCL con el que se compensa la operatoria cripto.
- [dolar_fx.md](dolar_fx.md) — otros circuitos de cambio de moneda de Wallet vía el mismo proveedor IVSA-Poincenot.
