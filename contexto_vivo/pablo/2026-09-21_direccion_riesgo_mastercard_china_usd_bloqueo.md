---
id: 2026-09-21_direccion_riesgo_mastercard_china_usd_bloqueo
pm: pablo
fecha_captura: 2026-09-21
fuente: "/sync_mails — mail 'Fw: Implementation plan CIS-2026-13184 PVT XBS' (threadId 1a05e59f178140ee), varios, 2026-09-15/17"
producto: transversal
tema: Pagos Mastercard cross-border a China en USD siguen bloqueados; clientes esperando, riesgo de reclamo si la acreditación por default es en moneda local
tipo: riesgo
destino_propuesto: 2_areas/riesgos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: f230716c54a5ca6600a2bce4e46bf0292d56a58c
---

Hilo liderado por Luciana Rudaz (pm_destino) con Mastercard sobre el proyecto de implementación CIS-2026-13184 (PVT XBS, pagos cross-border). Pablo Gomes está en copia pero no es el dueño de este proyecto — se captura como novedad para que Luciana la evalúe.

- **Estado general del proyecto:** Omar Gómez (Mastercard) confirmó que la validación de Suiza (B2P) tiene status success; solo queda pendiente resolver la transacción P2P de Canadá (en curso al 15/09).
- **Bloqueo específico señalado por Luciana Rudaz (15-16/09):** los pagos a **China en USD** siguen sin habilitarse — "nos urge cuanto antes que nos habiliten los pagos a China en USD, tenemos clientes que ya lo están esperando" (pedido directo a Juan Carlos Lozano Cortes, Mastercard).
- **Riesgo de negocio señalado por Gerardo Guastavino (Head de Internacional e Inst. Financieras, 16/09):** la funcionalidad de pago en USD con acreditación en destino (optativo USD o moneda local) es clave para la aceptación inicial del producto en los segmentos objetivo. Si la acreditación en moneda local queda como opción "por default" de la rampa, puede leerse como compulsiva para el pagador — cuya instrucción de pago (a instancias del beneficiario) es 99% en USD, en particular para China. Riesgo concreto: reclamos del proveedor externo hacia el pagador argentino por recibir una moneda distinta de la facturada.
- **Respuesta de Mastercard (Federico Darnond, 17/09):** "vemos lo mismo" — el tema se toma con prioridad; el cambio de RSP en China trajo complicaciones no previstas, están armando un plan para compartir a la brevedad (compromiso: antes de fin de esa semana). Sin fecha concreta de resolución al momento de este barrido.

> Fuente: mail "Fw: Implementation plan CIS-2026-13184 PVT XBS" (hilo Mastercard/Luciana Rudaz/Gerardo Guastavino, threadId `1a05e59f178140ee`), 2026-09-15 a 2026-09-17.
