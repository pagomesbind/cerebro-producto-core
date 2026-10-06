---
id: 2026-10-06_oportunidad-id-unico-ardid-wallet-para-conciliar-facturacion
pm: nicolas
fecha_captura: 2026-10-06
fuente: "Mail 'Dolor en facturación de ARDID - COTO' — Gonzalo Rivera, 2026-10-05"
producto: ardid
tema: Identificador único que persista entre Ardid y Wallet para conciliar la facturación de Ardid por entidad
tipo: oportunidad
destino_propuesto: 2_areas/direccion/oportunidades.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
---

- **Oportunidad:** que toda transacción evaluada por Ardid tenga un identificador único que persista en Ardid y en Wallet, también en los QR entrantes y en las rechazadas por Ardid (que hoy no generan operación en Wallet). Con eso, la facturación mensual de Ardid a cada entidad se podría conciliar de forma automática y certera contra las bases transaccionales.
- **Producto:** Ardid / Wallet.
- **Origen:** Mail "Dolor en facturación de ARDID - COTO" (2026-10-05).
- **Señal de demanda:** Gonzalo Rivera (Integraciones y Soporte) lo levanta como un dolor concreto de la facturación de agosto a COTO (entidad 4845), con planilla de ejemplo. Lo plantea como un problema que va a repetirse con cada entidad nueva que se facture así (Credicuotas ya se está integrando directo a Ardid). Hoy el cruce es manual y, para QR entrante y rechazos, imposible.
- **Foco estratégico:** Ardid.
- **Nota:** hay que ver si Ardid ya expone algún ID que se pueda persistir en Wallet al momento de la evaluación (el `ArdidTransactionId` ya existe para entrantes externas) y si para los rechazos alcanza con que Ardid entregue su propio detalle. Sin dueño asignado entre los 3 PM (ver T-110 en el backlog de nicolas).

> Fuente: Mail "Dolor en facturación de ARDID - COTO" — Gonzalo Rivera (2026-10-05).
