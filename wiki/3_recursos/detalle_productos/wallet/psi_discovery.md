# PSI (Proveedor de Servicios de Iniciación de Pagos) — Discovery (nunca construido)

> Estado: discovery — no construido. Fuente: Epic Notion "[EPIC] PSI" (Tipo Negocio, Tamaño estimado 104 SP, Status "Discovery - Priorización" — nunca pasó a desarrollo: las 16 US del backlog quedaron todas en estado "Pendiente"). Reubicado desde `detalle_productos/transversal/psi_discovery.md` en la reestructuración PARA en cascada (2026-08-12).

## Problema y solución propuesta

Las fintechs que emiten **CVU** tienen acceso limitado a productos financieros exclusivos de la banca tradicional (CBU): transacciones en USD, descubiertos, acreditación de sueldos. La propuesta: Bind PSP actuando como **PSI (Proveedor de Servicios de Iniciación de Pagos)**, en alianza con **Banco Industrial**, permitiría que fintechs clientes ofrezcan a sus usuarios la apertura y vinculación de **cuentas bancarias reales (CBU en ARS y USD)** dentro de sus propias apps — sin que la fintech necesite ser un banco.

**Mercado objetivo:** fintechs con billetera propia que quieren expandir su oferta (ej. AstroPay, mencionado explícitamente como candidato a beta cerrada) + empresas no-fintech que quieran ofrecer productos bancarios a sus clientes.

**Referencia competitiva relevada (documento "Bench" de la Epic):** el mercado ya tiene 2 modelos en convivencia — jugadores con **CVU propio + CBU vinculada de un banco partner** bajo figura PSP-CP (UALÁ+Wilo Bank, Naranja X+Galicia), y jugadores puramente **PSI** que solo enrolan CBUs de terceros sin banco propio (MODO, MovyPay), bajo figura PSP-PSI. El modelo propuesto para Bind PSP es este segundo esquema, con Banco Industrial como partner.

## Alcance funcional (MVP y fuera de MVP)

**Must have (MVP):**
1. Onboarding y apertura de cuenta: KYC + apertura de CBU (ARS/USD) en Banco Industrial + vinculación (enrolamiento) automática a la wallet + alta de TD Digital (para operar en red Link) + notificación de apertura exitosa.
2. Envío y recepción de pagos: transferencias desde la CBU vinculada a otras CBU/CVU, validación de saldo, webhook de recepción de pagos entrantes.
3. Consulta de saldo e historial de movimientos de la CBU.

**Should have (fuera de MVP):** cash-in/cash-out hacia la CBU vía otros medios (DEBIN, QR, TRX PULL), vinculación de una CBU ya existente en otro banco (modelo MODO) con validación de titularidad.

**Could have:** descubiertos/créditos sobre la CBU, expansión a otros bancos además de Banco Industrial.

## Backlog nunca ejecutado (16 US, todas "Pendiente")

Cubría: wrapper de integración a los endpoints de API Bank para PSI, alta/consulta/saldo/movimientos de cuenta CBU vía endpoint público, crear transferencias salientes y recibir entrantes (con webhook a la organización), habilitar/deshabilitar la funcionalidad PSI por organización y por cuenta, manejo del token `delegate.apibank` (ver nota técnica abajo), adaptación de conciliación y state monitor, e integración con Ardid tanto en alta de cuenta como en flujos de transferencia entrante/saliente.

## Nota técnica de integración (API Bank)

El modelo PSI reutiliza los mismos endpoints de API Bank que ya usa Bind PSP para cuentas propias, cambiando el segmento de URL `owner` por `delegate` (ej. `.../accounts/delegate`, `.../accounts/{cbu}/delegate/transactions`). Al crear la cuenta, API Bank devuelve un token de autorización (**`Delegate-Authentication`**) que Bind PSP debe persistir y enviar en cada operación posterior sobre esa CBU — es el mecanismo que le permite a Banco Industrial distinguir cuentas propias de cuentas de terceros iniciadas vía PSI.

---
*Fuente: Notion histórico, Epic "PSI" — ingesta N3, 2026-07-06 (discovery nunca construido).*
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/transversal/psi_discovery.md` (reestructuración PARA en cascada). Contenido sin cambios.*
