---
id: 2026-09-01_adquirencia_qr_tarjeta_post_payments
pm: pablo
fecha_captura: 2026-09-01
fuente: "/sync_meetings — reunión 'Análisis COBRO' (2026-08-31 12:01, minuta Gemini), participantes Luciana Rudaz, Pablo Gomes, Nicolás Colón, Matías Alzogaray + equipo Fintexa (Daniela Collia, Melisa Belpassi, Flavia Salmerón, Marcos Sánchez, Cristian Medina, Julieta Giménez)"
producto: adquirencia
tema: QR Tarjeta — separación de especificación Post-payments y uso de código de comercio como terminal ID en API Resolve
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/boton_simple_2_0.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: ingestado
merge_commit:
---

En la reunión recurrente "Análisis COBRO" con Fintexa (2026-08-31) se cerraron dos decisiones sobre **QR Tarjeta** (pago con tarjeta desde wallets terceras, ya documentado en `boton_simple_2_0.md` por el cliente MODO):

1. **Post-payments necesita especificación técnica propia, separada de Botón Simple.** Daniela Collia (Fintexa) planteó que la funcionalidad de "post payments" de QR Tarjeta no puede reutilizar tal cual la configuración/especificación de "botón simple" — necesita su propio ticket y especificación técnica, porque las reglas de configuración de canales de pago no coinciden entre ambos flujos. Pablo Gomes confirmó la separación. Nicolás Colón queda a cargo de crear el ticket correspondiente y asociarlo a las nuevas reglas de QR tarjeta.

2. **API Resolve: se mantiene el código de comercio como terminal ID.** Quedaba abierto cómo identificar el "terminal" en la API Resolve para QR Tarjeta — se había considerado usar un dato aleatorio, pero Nicolás Colón propuso seguir usando el código de comercio (mismo criterio que ya se usa hoy), interpretando que, para este flujo, el alta por comercio representa la caja. Se acordó consultar con Pablo Gomes para validar la interpretación antes de cerrarlo del todo — Nicolás Colón crea un ticket para dejarlo definido formalmente, consultando también con Modo (la contraparte del caso de uso QR Tarjeta).

Adicional (mismo bloque de la reunión, no ligado a QR Tarjeta puntualmente): se acordó implementar una validación en la configuración del canal — si el rubro del comercio no coincide con el `site ID` configurado, el sistema debe mostrar una advertencia y requerir corrección manual (antes no había ningún control cruzado ahí). También se decidió mover el botón de "guardar" de la configuración de canal en el Admin a estar dentro de cada sección de canal (en vez de un botón único), eliminándolo una vez que la sección ya está configurada — mejora de UX pedida por el equipo, sin ticket propio identificado en la minuta.

> Fuente: Reunión "Análisis COBRO" (2026-08-31), minuta Gemini — sección Decisiones/Detalles.
