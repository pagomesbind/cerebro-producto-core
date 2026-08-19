---
id: 2026-08-14_wallet_fci_webhook_finalizacion_virginia
pm: pablo
fecha_captura: 2026-08-17
fuente: "/sync_mails — mail \"Consultas sobre webhook de FCI y finalización de procesamiento de paquetes\" (threadId 1a00055854107921), Franco Gimenez (Soporte BIND) a Poincenot, 2026-08-14"
producto: wallet
tema: Webhook de FCI nunca recibido en PROD + finalización de procesamiento desalineada entre organizaciones (La Virginia vs. Coppel)
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/wallet/cuenta_remunerada_fci.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

**Fuente:** mail de Franco Gimenez (Analista de Implementaciones y Soporte, BIND PSP) a Poincenot (mariano.zanier@poincenot.com, martin.brambilla@poincenot.com), con copia a Producto, 14/08/2026. Sin respuesta de Poincenot todavía al momento de este barrido — queda como pregunta abierta, no como hallazgo cerrado.

**Consulta 1 — Webhook de FCI ausente en PROD:** BIND nunca recibió el webhook de FCI de parte de Poincenot en ambiente productivo. Se pidió que indiquen qué hay que configurar del lado de BIND o qué coordinar para poder recibirlo correctamente.

**Consulta 2 — Finalización de procesamiento desalineada entre organizaciones:** para **La Virginia**, el proceso de FCI siempre queda en estado "Pendiente" salvo que Soporte avise por Telegram a Poincenot para que lo finalicen manualmente. **Coppel** suele finalizar correctamente solo (alrededor de las 17:00/17:30), mientras que La Virginia normalmente termina 1-2 horas después. Se pidió ajustar el proceso para que todas las organizaciones finalicen aproximadamente al mismo horario — el problema va a crecer porque se sigue sumando entidades (próxima: **HIPO**), y sin alineación la brecha de horarios se agranda con cada organización nueva.

**Relación con el informe semanal del mismo día:** el informe de Fintexa (ver ítem `2026-08-14_wallet_fci_mvp2_avance.md`) señala como bloqueo activo "controlar diariamente el proceso de Coppel y La Virginia en PROD" — es el mismo problema visto desde el lado de Soporte/operación.

**Oferta:** BIND ofreció coordinar una reunión con Infra si hace falta para resolver cualquiera de los dos puntos.
