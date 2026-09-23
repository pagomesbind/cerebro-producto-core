---
id: 2026-09-21_ardid_gap_credenciales_cpf_pendientes_desde_junio
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_meetings — reunión \"Producto\" (14:01, con Emma Vignoles/Nicolás Colón), 2026-09-21"
producto: ardid
tema: Credenciales de acceso a CPF pendientes de entrega desde junio; falta de listados de transacciones de Credicuotas/Coto bloquea el cobro de facturas de Ardid a esos clientes
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/ardid/index.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit:
---

**Descripción:** en la misma reunión donde se repasó la arquitectura de segmentación PJ (ver item de canon relacionado), se enumeraron tres exigencias pendientes con el equipo de Ardid y Soporte, sin resolver:

1. **Entrega de credenciales de acceso a CPF** (Central de Prevención de Fraude, Coelsa — ver también `contexto_vivo` histórico sobre CPF/COELSA.PREVENT capturado el 2026-09-11) — pendiente, sin fecha.
2. **Envío de listados de transacciones para Credicuotas y Coto** — pendiente **desde junio de 2026**. Consecuencia directa y concreta: sin esos listados, Bind PSP no puede facturarle el servicio de Ardid a esos dos clientes — el cobro de facturas está bloqueado por esta falta de información, no por una disputa comercial.
3. **Enrutamiento del 100% de las transacciones a través de Ardid** — pendiente, sin más detalle en la minuta sobre qué transacciones quedan hoy fuera del enrutamiento.

**Por qué es relevante ahora:** conecta con el riesgo de performance de Ardid capturado el mismo día (`2026-09-21_ardid_riesgo_performance_afecta_ventas_coto_desa`) — Coto es justamente uno de los dos clientes con facturación bloqueada por este gap, además de tener el problema de performance reportado en paralelo.

**Estado:** sin owner ni fecha de resolución mencionados en la reunión — no está claro si el bloqueo depende de Fintexa (proveedor de Ardid), del propio equipo de Bind, o de un tercero.
