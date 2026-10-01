---
id: 2026-09-30_wallet_gap_mastercard_move_mtf_vs_prod_inconsistencia_datos
pm: pablo
fecha_captura: 2026-09-30
fuente: "/sync_mails — hilo \"Re: Re: Re: Re: BIND - MC | XBS\" (threadId 19ee187f2b0bcb25), Luciana Rudaz (Productos), 2026-09-29"
producto: wallet
tema: "Pagos FX Mastercard Move — datos de campos del sender inconsistentes entre ambiente de pruebas (MTF) y producción, bloquea ajustes y pruebas"
tipo: gap
destino_propuesto: 3_recursos/detalle_productos/wallet/pagos_internacionales_mastercard_move.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
merge_commit: 9bf60c5
---

Proyecto Pagos FX (integración Mastercard Move / XBS, liderado por Luciana Rudaz — no es un proyecto de este PM, se captura porque Pablo Gomes está en copia del hilo desde julio). Luciana Rudaz reporta a Mastercard (José Guarín) un nuevo caso, dentro de una serie ya recurrente en este hilo (ver antecedente de julio sobre el campo `purpose_of_payment` en corredores canadienses): al repasar todos los campos de `additional_data.XXX` relacionados con el sender (que Bind no vuelve a pedir al usuario porque ya lo conoce por ser cuenta propia), encontraron que **el ambiente de pruebas (MTF) devuelve `supportedValues` para varios campos que el ambiente de producción no devuelve** para los mismos campos — listado adjunto por Luciana en el mail (no legible en texto plano, solo como imagen).

**Por qué importa:** esta inconsistencia entre MTF y PROD dificulta aplicar los ajustes pedidos por Mastercard y validar el comportamiento antes de pasar a producción, porque el comportamiento que se prueba en MTF no es el que después corre en PROD. Luciana pide a Mastercard que lo revisen y lo equiparen; sin resolución en este hilo todavía.

> Fuente: mail "Re: Re: Re: Re: BIND - MC | XBS", Luciana Rudaz (Bind PSP), 2026-09-29 13:23, threadId `19ee187f2b0bcb25` — hilo abierto desde julio 2026, mismo patrón de discrepancias MTF/PROD ya reportado antes (ej. `purpose_of_payment` en corredores de Canadá, agosto 2026).
