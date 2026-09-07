---
id: 2026-09-04_adquirencia-provincianet-masividad-qr-satura-cola-general
pm: nicolas
fecha_captura: 2026-09-04
fuente: "Reunión \"Producto - Prioridades\" (2026-09-04)"
producto: adquirencia
tema: ProvinciaNET genera códigos QR de forma masiva (por lote) y satura la cola general de generación de QR, demorando hasta 35 segundos a otros clientes — ticket AD-935, prioridad 1
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/pedidos_de_clientes_y_hallazgos_operativos.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: ingestado
---

En la reunión "Producto - Prioridades" (2026-09-04), Pablo Gomes y Nicolás Colón identificaron que cuando **ProvinciaNET** genera códigos QR de forma masiva (por batch/lote), esa carga satura la cola general de generación de QR — afectando a **todos** los clientes que generan QR en simultáneo, no solo a ProvinciaNET. El síntoma reportado: hasta **35 segundos** de demora para que le aparezca el QR a una persona que está pagando en el momento (deuda generada en vivo). El patrón es recurrente a principios de mes (coincide con el ciclo de facturación de ProvinciaNET) y ya generó reclamos de otro cliente además de ProvinciaNET: **Pay Evolution (Europagos)** — según confirmó Alan a Nicolás Colón durante la reunión ("de Pay es uno más que se le quejó, pero solo esos dos").

Detalle técnico aportado en la reunión: ProvinciaNET usa ambos tipos de creación de QR (deuda normal QR y QR masivo); no está confirmado si el masivo es por batch. Se propuso como solución de fondo una **cola diferenciada** (una para corridas masivas, otra para el flujo normal) para que no se afecten entre sí — sin desarrollo iniciado todavía.

**Decisión tomada en la misma reunión:** se asignó **prioridad 1** al ticket **AD-935** (aún sin cotizar al momento de la reunión) para resolverlo cuanto antes, dado el impacto recurrente a clientes múltiples. Matías Alzogaray evaluará con Meli (Fintexa) si puede salir como fix rápido o requiere fecha de despliegue formal — con la salvedad de que fixear algo de cobro los primeros días del mes (ventana de mayor uso) implica cierto riesgo.

> Fuente: Reunión "Producto - Prioridades" (2026-09-04, tramo 14:01-14:12), minuta Gemini.
