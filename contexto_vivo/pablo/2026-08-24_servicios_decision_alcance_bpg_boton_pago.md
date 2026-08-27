---
id: 2026-08-24_servicios_decision_alcance_bpg_boton_pago
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Proyecto BPG' (docId 1QAB4a1KzkjOzmF1_iCMn_l1R4aiSCzt0C3lK0PtpNHY), 2026-08-24, con Adriana Endzeliz"
producto: servicios
tema: Alcance inicial del pago de servicios (BPG) limitado a botón de pago, sin uso de saldo de wallet
tipo: decision
destino_propuesto: 2_areas/direccion/decisiones.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: 75959e2
---

## Alcance inicial de pagos de servicios (BPG): solo botón de pago, sin saldo de wallet

- **Contexto/Problema:** integradores externos (caso concreto: Octagon) que tienen su propia wallet quieren que sus usuarios paguen servicios (ej. facturas) usando el **saldo disponible en su wallet**, no solo con tarjeta/QR vía botón de pago. Bind PSP no tiene hoy desarrollada la funcionalidad de pago de servicios con saldo de billetera de terceros.
- **Decisión tomada:** el producto de pago de servicios se lanza **limitado exclusivamente a la modalidad de botón de pago**, excluyendo temporalmente el uso de saldo en wallet. El **desarrollo de pago con saldo de billetera queda condicionado** a que el equipo comercial presente un **caso de negocio** que demuestre viabilidad y volumen transaccional suficiente — no se construye especulativamente para un solo cliente. El PM señaló que, si el volumen fuera bajo (limitado a un solo cliente como Octagon), el desarrollo no sería rentable comparado con captar actores de mayor volumen (ej. Coto, Arcos Dorados).
- **Impacto en el Roadmap/Producto:** a nivel arquitectónico, cuando se retome, la dirección preferida por el PM es que la integración de pago de servicios con saldo se resuelva a nivel **Wallet integrándose directo al producto de Deuda** (no como una solución ad-hoc por cliente) — para no generar una solución desprolija donde cada integrador tenga que orquestar manualmente las consultas contra el producto de deuda de Bind PSP. Comercial (Adriana Endzeliz) se lleva la tarea de elaborar el caso de negocio y coordinar con el equipo técnico la revisión de los aspectos arquitectónicos.
- **Estado:** Aprobado (alcance inicial); En Revisión (desarrollo de pago con saldo, condicionado a caso de negocio).

> Fuente: Reunión "Proyecto BPG" (2026-08-24), minuta Gemini — Adriana Endzeliz y Pablo Gomes. Ver también [`2026-08-24_servicios_oportunidad_pago_saldo_wallet_terceros`](2026-08-24_servicios_oportunidad_pago_saldo_wallet_terceros.md) y [`2026-08-24_servicios_esquema_subagentes_bpg_apis_externas`](2026-08-24_servicios_esquema_subagentes_bpg_apis_externas.md).
