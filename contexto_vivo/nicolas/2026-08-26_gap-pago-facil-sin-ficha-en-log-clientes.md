---
id: 2026-08-26_gap-pago-facil-sin-ficha-en-log-clientes
pm: nicolas
fecha_captura: 2026-08-26
fuente: "Mail \"Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA Minuta 19-8\" (2026-08-19 → 2026-08-25) + wiki/2_areas/clientes/log_clientes.md"
producto: servicios
tema: Pago Fácil (Western Union/SEPSA) es cliente en producción documentado técnicamente, pero no aparece en el log maestro de clientes
tipo: gap
destino_propuesto: "2_areas/gaps_y_preguntas.md"
tipo_destino: actualizar
contradice: "wiki/2_areas/clientes/log_clientes.md (200 clientes, barrido 2026-07-07) no tiene ninguna fila para 'Pago Fácil', 'Western Union' ni 'SEPSA'"
confianza: alta
estado: en_cola
---

**Contradicción/vacío detectado:** `3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md` documenta a Pago Fácil como cliente en producción del producto "Servicios" desde al menos 2026-06-04 (versión SER 1, 39 tickets), y el mail "Seguimiento Desarrollo Pasarela de Pagos Bind-SEPSA" (hilo 2026-08-19 → 2026-08-25, ver `[[2026-08-26_pago-facil-sepsa-piloto-productivo-admin-y-pendientes]]`) confirma que sigue activo hoy con un Piloto Productivo en curso (entidades UAT confirmadas, plataforma admin propia). Sin embargo, `wiki/2_areas/clientes/log_clientes.md` (mantenido por `/sync_customers` desde Notion, 200/200 clientes al 2026-07-07) no tiene ninguna fila para "Pago Fácil", "Western Union" ni "SEPSA" — ni en producción ni en ningún otro estado.

Posibles explicaciones a resolver por `/sync_customers` contra Notion: (a) existe con otro nombre legal en el legajo de Notion (candidatos vistos en el mail: "SEPSA", "Western Union") y el matching por nombre lo está pasando por alto; (b) el legajo de Notion de este cliente nunca se creó porque la relación se gestiona fuera del proceso comercial estándar (cliente histórico/legacy, o gestionado directamente por Comercial sin paso por Notion); (c) es un caso real de legajo faltante.

No se resuelve acá — queda para el próximo barrido de `/sync_customers`, que es el único dominio autorizado a tocar `log_clientes.md`.

> Fuente: mail citado arriba + `wiki/2_areas/clientes/log_clientes.md` + `wiki/3_recursos/detalle_productos/servicios/pago_facil_mantenimiento.md`.
