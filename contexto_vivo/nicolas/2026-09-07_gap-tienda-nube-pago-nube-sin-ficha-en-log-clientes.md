---
id: 2026-09-07_gap-tienda-nube-pago-nube-sin-ficha-en-log-clientes
pm: nicolas
fecha_captura: 2026-09-07
fuente: "Reunión \"Daily producto\" (2026-09-07) + reunión \"Weekly - Producto / Operaciones\" (2026-09-07)"
producto: transversal
tema: Cliente mencionado como "Pago Nube"/"Tienda Nube" en dos reuniones distintas del mismo día, con problemas activos, sin fila propia en log_clientes.md
tipo: gap
destino_propuesto: 2_areas/clientes/log_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: c07b365
---

El mismo día aparece un cliente mencionado con dos nombres ligeramente distintos, en dos reuniones separadas, ambas con problemas operativos activos:

- Reunión "Daily producto" (09:31): Luciana Rudaz menciona que las mejoras de conciliación Coelsa (reintento de alias + inclusión cashout/CAS) "deberían reducir los problemas que presenta **Pago Nube** con CBU Collect".
- Reunión "Weekly - Producto / Operaciones" (14:56): Luciana Rudaz alerta sobre una **degradación del servicio de agente de cobro reportada por Tienda Nube en las transferencias salientes**; Pablo Gomes revisó los tableros y notificó al grupo de interacciones para que soporte lo verifique.

No se encontró ninguna fila en `2_areas/clientes/log_clientes.md` para "Tienda Nube" ni "Pago Nube" (búsqueda por ambos nombres, sin match). Es plausible que ambas menciones sean el mismo cliente real (**Tienda Nube**, plataforma de e-commerce ampliamente conocida en Argentina) con "Pago Nube" como error de transcripción de Gemini, y que use CBU Collect/Agente de Cobros y Pagos — pero sin ficha en el log no se puede confirmar tamaño/riesgo/canónico ni si ya tiene relación comercial activa documentada en Notion.

Mismo patrón que los gaps ya abiertos de Pago Fácil/Western Union (2026-09-03) y PedidosYa (2026-09-04): cliente con actividad operativa real pero sin fila propia en el log maestro — a levantar en el próximo barrido de `/sync_customers`.

> Fuente: Reunión "Daily producto" (2026-09-07, minuta Gemini) + reunión "Weekly - Producto / Operaciones" (2026-09-07, minuta Gemini).
