---
id: 2026-08-24_servicios_esquema_subagentes_bpg_apis_externas
pm: pablo
fecha_captura: 2026-08-24
fuente: "/sync_meetings — reunión 'Proyecto BPG' (docId 1QAB4a1KzkjOzmF1_iCMn_l1R4aiSCzt0C3lK0PtpNHY), 2026-08-24, con Adriana Endzeliz"
producto: servicios
tema: Esquema de subagentes para disponibilizar las APIs de BPG (pago de servicios/Pago Fácil) a integradores externos
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/servicios/pago_facil.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 75959e2
---

## Esquema operativo para exponer BPG (pago de servicios) a integradores externos vía subagentes

**Contexto:** Adriana Endzeliz (Comercial) planteó al PM que varios clientes externos están consultando activamente por integrarse al cobro de servicios de BPG (Pago Fácil) — el caso concreto en discusión es **Octagon**, que quiere ofrecer pago de servicios (ej. factura de electricidad) dentro de su propia app/wallet.

**Estado técnico confirmado:** cuando se construyó BPG, se lo pensó **todo por API** para que cualquier cliente con capacidad de desarrollo pudiera integrarse — esas APIs ya están en producción, no están ocultas ni deshabilitadas, simplemente **no están activamente disponibilizadas/promocionadas** como oferta comercial estándar hacia afuera.

**Esquema operativo propuesto (a validar):** Bind PSP actúa como **agente** del acuerdo con Pago Fácil (Bin PCP / BPG) — el acuerdo comercial de fondo ya existe: Bind PSP puede actuar como subagente de Pago Fácil. La propuesta en discusión es crear una **entidad relacionada al producto** donde clientes externos como Octagon funcionen como **comercios/subagentes** dentro de esa entidad — análogo al modelo ya usado en Adquirencia, donde cada comercio de Pago Fácil es formalmente "Pago Fácil" independientemente de su rubro real (escuela, municipio, etc.). Quedó abierta la pregunta de si conviene que la titularidad del "agente" recaiga en Bind PSP (como entidad) con Octagon como comercio dentro de ella, o si correspondería un convenio directo Octagon↔Pago Fácil — Adriana Endzeliz se lleva a validar con su equipo cuál esquema conviene más, considerando que las liquidaciones se calculan por comercio.

**Caso de uso descripto para Octagon:** usuario de la wallet de Octagon entra a pago de servicios dentro de la app de Octagon, busca la empresa/deuda a pagar, paga con tarjeta o QR (vía botón de pago externo, no con saldo — ver decisión asociada), la transacción impacta la deuda en BPG, se registra para evitar doble pago, y se emite comprobante.

> Fuente: Reunión "Proyecto BPG" (2026-08-24), minuta Gemini — Adriana Endzeliz y Pablo Gomes.
