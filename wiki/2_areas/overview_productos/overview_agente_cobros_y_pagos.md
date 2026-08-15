# Agente de Cobros y Pagos — Overview de Producto

> Fuente: `raw/Product overview_Agente de cobros y pagos.docx` (ingesta Fase 1, 2026-07-02). Área de negocio: [equipo.md](../overview_empresa/overview_equipo.md). Nombre anterior: **CVUCollect**.

## Qué es

Capa multi-collector construida por Bind PSP sobre **API BANK** (el producto de APIs de **Banco Industrial** para operar cuentas). Cada cliente de Bind PSP (**collector**) queda asociado a una **única subcuenta CBU** de la cuenta de Bind PSP en Banco Industrial, con credenciales de API propias que le dan acceso a funcionalidades de API BANK acotadas a esa cuenta.

## Funcionalidades

- Ver saldo de la cuenta recaudadora.
- Crear **CVUs**.
- Realizar transferencias desde el CBU.
- Recibir transferencias tanto a un CVU como al CBU recaudador.

## Modelo de uso

- Nació para aprovechar la licencia de **PSP** de Bind PSP: un cliente puede crear CVUs sobre la cuenta/PSP de Bind y asignarlos internamente a un cliente final o deuda según su caso de negocio. Cualquier transferencia recibida en ese CVU permite conciliar en línea el pago o la recaudación asociada.
- **Los CVU no son cuentas de pago** — Bind PSP no lleva saldo de estas cuentas; solo se usan para recibir transferencias. Todos los CVU son de titularidad del collector.
- Si la cuenta recaudadora asignada a un collector es un **CBU en dólares**, no tiene disponible la herramienta de CVU; en ese caso el collector puede exigir a su cliente final transferir desde una cuenta de su misma titularidad para conciliar por CUIT.
- Los collectors aprovechan las cuentas **exentas de impuestos al débito y crédito** de las que goza Bind PSP por su condición de PSP.

## Integraciones con otros productos

- **Adquirencia**: sustenta los canales **Botón simple 2.0** y **Recaudación por transferencia** (ver [adquirencia_overview.md](overview_adquirencia.md)). Si el collector no usa ninguno de esos modelos, puede consumir las APIs de Agente de cobros directamente — en ese caso se asocia internamente el collector a la entidad de Adquirencia, de modo que cada transferencia recibida genera una transacción en Adquirencia y así aprovecha sus archivos batch, liquidaciones y cobro de comisiones.

---
*Última actualización: 2026-07-02 — Ingesta Fase 1.*
