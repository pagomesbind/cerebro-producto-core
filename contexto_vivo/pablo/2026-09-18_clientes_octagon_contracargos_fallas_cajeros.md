---
id: 2026-09-18_clientes_octagon_contracargos_fallas_cajeros
pm: pablo
fecha_captura: 2026-09-18
fuente: "/sync_meetings — reunión 'Join Soporte Clientes' (2026-09-16), minuta Gemini"
producto: ardid
tema: pico de contracargos de Octagon (300-500 en 3 días) por fallas físicas de cajeros automáticos, no por fraude
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit: f230716c54a5ca6600a2bce4e46bf0292d56a58c
---

## Hallazgo

Gonzalo Rivera reportó un volumen inusual de entre 300 y 500 contracargos en 3 días por parte del cliente **Octagon** (además de un problema de fraude señalado por separado con "BCF"). Diego Weledniger explicó que la causa no es fraude ni un problema de Ardid: se debió a **devoluciones automáticas generadas por fallas físicas en extracciones de cajeros automáticos** (el cajero no entrega el efectivo pero la transacción queda iniciada, y el banco emisor la contracarga). Diego aclaró además un dato de mecánica relevante: **las transacciones de código QR no pasan por Ardid** — solo las de tarjeta sí. Adriana Endzeliz consultó si tenía sentido sumar QR a la hoja de ruta de Ardid; Matias Alzogaray respondió que hoy no es una prioridad.

## Nota

No se registró ninguna acción de Producto derivada de este hallazgo — es informativo, para que quede en el caso de uso del cliente ante un futuro pico similar de contracargos que alguien pueda confundir con fraude.
