# Wallet — Overview de Producto

> Fuente: `raw/Product overview_Wallet.docx` (ingesta Fase 1, 2026-07-02). Área de negocio: [equipo.md](../overview_empresa/overview_equipo.md). Provisto por: Keepit (subcontratada de FINTEXA).

## Qué es

Producto construido a partir de la licencia de **PSP** que Bind PSP obtuvo del BCRA, para poder comenzar a explotarla y ofrecer servicios de billetera as a service a organizaciones que no podían ni pensar en esto por ser de otros rubros (como retail) — brindarles la licencia les acorta mucho el camino para ser billetera. Ofrece funcionalidades de billetera digital ("Wallet as a Service") vía API.

## Modelo de cliente y cuentas

- El cliente de este producto es una **organización**.
- A cada organización se le asigna una **cuenta recaudadora** (subcuenta CBU dentro de las cuentas de Bind PSP en **Banco Industrial**) y **credenciales de API** propias.
- Las organizaciones crean **cuentas** en el sistema; cada cuenta tiene un **titular** (persona física o jurídica) y debe tener CUIT. Un mismo CUIT puede tener más de una cuenta.
- Sinergia con **Onboarding**: el alta de cuenta puede ser una acción automática del flujo de onboarding tras validar a una persona (ver [onboarding_overview.md](overview_onboarding.md)).

## PSP as a Service / multiPSP

- Bind PSP ofrece su tecnología junto con su licencia de PSP ("PSP as a Service"). Organizaciones bajo este modelo generan CVUs para sus clientes bajo la entidad **PSPCP** de Bind PSP (ej.: los CVU de Mercado Pago son técnicamente de Bind PSP, aunque pertenecen operativamente a distintas organizaciones internas).
- **multiPSP:** para clientes que tienen su **propia licencia de PSP** pero quieren usar la tecnología de Bind. Condición: el cliente debe ser también cliente de **API BANK** (Banco Industrial), ya que esas son las APIs que sustentan las funcionalidades de wallet. En estos casos se usan las credenciales de API BANK de cada organización a su propio nombre.

## Funcionalidades clave

- CVU por cuenta (no obligatorio, pero necesario para casi todas las funcionalidades de wallet en Argentina).
- Saldo en pesos por cuenta, modificado mediante **comprobantes** (movimientos de débito/crédito, cada uno con un tipo que justifica su uso).
- **Operaciones**: tienen distintos tipos según la funcionalidad (transferencias, compra de dólares, etc.), se procesan con un externo, y su estado se monitorea hasta un estado definitivo. Al llegar a estado definitivo suelen enviar un **webhook** a la organización, y generan comprobantes que debitan/acreditan saldo según el flujo.
- App mobile (Android/iOS) marca blanca: no es prioridad de producto — se usa solo para clientes específicos sin capacidad de desarrollo propio. Incluye onboarding, login, transferencias, ver saldo, cambiar alias, pagar QR interoperable, guardar tarjetas, ingreso de dinero (débito recurrente o tarjeta). Caso ad hoc: funcionalidad de QR para viajar en la empresa de autobuses **TIN**.

## Cálculo de impuestos (SISCRI)

Existe una instancia del motor **SISCRI** dentro de Wallet (distinta de la de Adquirencia — ver [adquirencia_overview.md](overview_adquirencia.md)), con lógica orientada a **personas** (no comercios). Conoce al titular de cada cuenta (informado al alta de cada CVU) y los tipos de movimiento (informados al crear cada tipo de comprobante). Puede parametrizarse para excluir movimientos u organizaciones del cálculo. El pedido de cálculo es síncrono en su disparo pero la respuesta es **asíncrona**; si corresponde cobrar impuesto, SISCRI instruye a Wallet para crear el comprobante de débito correspondiente.

El área **Impuestos y Contabilidad** (líder: Natalia Frea) es sponsor de SISCRI en esta instancia también: detecta necesidades de actualización del software y gestiona/levanta los requerimientos de desarrollo correspondientes. Ver [equipo.md](../overview_empresa/overview_equipo.md).

## Integraciones con otros productos

- **Ardid** (monitoreo transaccional): al crear una organización o un CVU se crea una entity en Ardid. Cada operación se analiza contra reglas restrictivas antes de cursarse con el procesador correspondiente. Ver [ardid_overview.md](overview_ardid.md).
- **Adquirencia**: un comercio puede asociarse a una cuenta de wallet, habilitando acceso al portal de Adquirencia con esa cuenta. El CVU se crea y asocia desde Adquirencia al dar de alta el comercio, para que las cobranzas se acrediten en la cuenta de wallet. Cuando la acreditación de QR es en línea, Adquirencia crea comprobantes de crédito (cobro) y débito (impuestos) en la cuenta de wallet. Ver [adquirencia_overview.md](overview_adquirencia.md).
- **Onboarding**: puede dar de alta cuenta / cuenta+CVU / cuenta+CVU+cuenta comitente en Wallet como parte de sus altas automáticas. Ver [onboarding_overview.md](overview_onboarding.md).

## Procesadores por funcionalidad

| Funcionalidad | Procesador |
|---|---|
| Transferencia saliente/entrante externa | API BANK (Banco Industrial) |
| Transferencia saliente/entrante interna | Interno (Wallet) |
| Pagos QR | Coelsa (directo — no está en API BANK) — mecánica técnica completa en [mecanica_interna_productos/](../../3_recursos/detalle_productos/wallet/index.md) |
| Débito recurrente (DEBIN) | API BANK (Banco Industrial) |
| Transferencia pull | Coelsa (directo — no está en API BANK) |
| Cuenta remunerada | API Broker (Banco Industrial Inversiones / IVSA / POINCENOT) |
| Dólar CCL | API Broker (Banco Industrial Inversiones / IVSA / POINCENOT) |
| Cripto | Lirium |
| Pago PIX | Pag Brasil |

---
*Última actualización: 2026-07-02 — Ingesta Fase 1.*
