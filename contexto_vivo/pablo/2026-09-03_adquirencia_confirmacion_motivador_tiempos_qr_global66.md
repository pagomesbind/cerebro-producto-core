---
id: 2026-09-03_adquirencia_confirmacion_motivador_tiempos_qr_global66
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_meetings — reunión 'Bind Global66, proximos pasos' 2026-09-02 16:59 (docId 1u64akvbqsmyyaqDU9nJ7o88NgdTHDy6F5grWugqtHac) y 'Join Soporte Clientes' 2026-09-02 10:01 (docId 1eBqiPncYkZgzw693JLN5rmLGwtIZST14zx6LKb3Pn_g), minutas Gemini"
producto: adquirencia
tema: Evidencia técnica nueva sobre la mecánica de tiempos de consulta QR — confirma a Global66 como cliente real con reclamo activo de latencia
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/mecanica_qr_coelsa.md
tipo_destino: actualizar
contradice: "2_areas/gaps_y_preguntas.md [2026-09-02] 'Adquirencia: contradicción sin resolver sobre qué cliente motivó el ajuste de tiempos de Pagos QR (TPay vs. BSF/Global66)' — este item no resuelve la contradicción (no hay evidencia de que Global66 sea el motivador específico del ajuste de parametrización de la reunión del 2026-08-31), pero aporta evidencia independiente y reciente (2026-09-02) de que Global66 es, como mínimo, un cliente real con reclamo activo y documentado de latencia QR — refuerza que la versión 'BSF/Global66' no es una atribución errónea, sin descartar que TPay también haya reclamado por separado."
confianza: media
estado: en_cola
merge_commit:
---

**Contexto:** `2_areas/gaps_y_preguntas.md` tiene abierta desde el 2026-09-02 una contradicción entre dos items de `contexto_vivo/` de distinto PM sobre quién motivó el ajuste de tiempos de consulta de Pagos QR acordado en la reunión "Configuración de tiempos de consulta de Pagos QR" (2026-08-31): un item (Nicolás Colón) dice BSF/Global66, descartando explícitamente "TPay" como nombre no reconocido (decisión D-002); otro item (Pablo Gomes, misma fuente) identifica a TPay.

**Lo que aporta esta corrida (2026-09-02, dos reuniones distintas y posteriores a esa del 08-31):**

1. **"Bind Global66, proximos pasos" (16:59):** reunión dedicada exclusivamente a resolver un reclamo de latencia QR de Global66 (ver `2026-09-03_clientes_global66_latencia_qr_transferencias`). Confirma con evidencia técnica dura (logs cruzados, casos puntuales validados por Fintexa) que Global66 tiene un reclamo activo, real y ya escalado a una mesa técnica dedicada — no es una atribución dudosa ni un nombre mal transcripto.
2. **"Join Soporte Clientes" (10:01):** Mauro Suppan reportó, en la misma jornada, "el descontento de Global 66 respecto a la latencia en el proceso de lectura de códigos QR" como tema de agenda de soporte — Gonzalo Rivera respondió que las pruebas internas de Bind dan 7 segundos, y se pidieron evidencias adicionales al cliente. Mismo patrón de reclamo que la reunión dedicada del punto 1, confirmando que no es un hecho aislado de una sola conversación.

**Lo que esto NO resuelve:** ninguna de las dos reuniones de esta corrida menciona la reunión "Configuración de tiempos de consulta de Pagos QR" (2026-08-31) ni confirma que el ajuste de parametrización acordado ahí (agregar una segunda consulta a Coelsa, ver `mecanica_qr_coelsa.md` y la decisión ya documentada en `2026-09-03_contexto_fijo_comunicacion_novedades_producto`) haya sido una respuesta directa al reclamo de Global66 en particular. Tampoco descarta que TPay haya hecho un reclamo separado y también real. La contradicción de `gaps_y_preguntas.md` sigue sin ganador — este item solo suma evidencia a uno de los dos lados, no lo cierra.

**Detalle técnico adicional confirmado en "Bind Global66" (refuerza lo ya documentado en `mecanica_qr_coelsa.md`):** el flujo de consulta a Coelsa hace una primera consulta a los 4,5 segundos y, si no resuelve, una segunda a los 6,5-7 segundos — cubre el 99% de los casos; el remanente pasa al "state monitor", que reconsulta cada 30 segundos.

> Fuentes: reuniones "Bind Global66, proximos pasos" y "Join Soporte Clientes", ambas 2026-09-02, minutas Gemini.
