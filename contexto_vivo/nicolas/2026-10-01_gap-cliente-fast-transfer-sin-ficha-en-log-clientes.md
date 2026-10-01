---
id: 2026-10-01_gap-cliente-fast-transfer-sin-ficha-en-log-clientes
pm: nicolas
fecha_captura: 2026-10-01
fuente: "Reunión \"Join Soporte Clientes\" (2026-09-30), solo el resumen del mail de Gemini (Drive desconectado, sin minuta completa)"
producto: transversal
tema: "Fast Transfer" aparece como cliente que pagó su configuración, pero no figura en log_clientes.md
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: baja
estado: ingestado
merge_commit: PENDING
---

## Qué se detectó

En la reunión "Join Soporte Clientes" del 2026-09-30 se dijo que **"Fast Transfer"** pagó el **cargo de configuración** después de varias demoras. Eso sugiere que es un cliente nuevo, o en proceso de alta, de Bind PSP. Sin embargo, **no aparece en `2_areas/clientes/log_clientes.md`** ni en ningún item de `contexto_vivo/`.

En la misma reunión también se habló de:
- **Ventas en baja**: se atribuye a la época del año y a que los clientes no responden. No se nombran clientes.
- **Demoras en los modelos de contrato.**
- **Un problema de facturación resuelto "con Pago Fácil".** Diego Weledniger va a pedirle a Emilio que confirme cómo se factura en pesos. También va a emitir una nota de crédito por una factura en dólares para poder cobrar en pesos. La minuta no aclara si este punto es sobre Fast Transfer o sobre Pago Fácil. Es un tema administrativo, así que no generó tarea de Producto.

## Qué hay que resolver

1. Confirmar si "Fast Transfer" es un cliente nuevo, para que `/sync_customers` lo levante desde Notion. Revisar también la grafía: puede ser un error de transcripción de Gemini.
2. Aclarar si la inconsistencia del contrato y la refacturación USD→ARS son de Fast Transfer o de Pago Fácil.

> Fuente: Reunión "Join Soporte Clientes" (2026-09-30), resumen del mail de Gemini. Doc `1qAhV4ttix0uoPPHzuh2PsZNKgy1wUo2us4pgt4lRD9s`, no se pudo leer porque el conector de Drive está invalidado.
