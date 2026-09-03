---
id: 2026-09-03_clientes_global66_latencia_qr_transferencias
pm: pablo
fecha_captura: 2026-09-03
fuente: "/sync_meetings — reunión 'Bind Global66, proximos pasos' 2026-09-02 16:59 (docId 1u64akvbqsmyyaqDU9nJ7o88NgdTHDy6F5grWugqtHac), minuta Gemini"
producto: adquirencia
tema: Global66 — reclamo de latencia percibida en pagos QR y transferencias salientes, análisis conjunto en curso
tipo: conocimiento
destino_propuesto: 2_areas/clientes/casos_de_uso_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

**Cliente:** Global 66 (Argpagos SA) — ficha existente en `log_clientes.md` (Wallet, Billetera, Pequeño).

**Hallazgo (2026-09-02):** reunión conjunta Bind PSP / Global66 para reconciliar una discrepancia de métricas de latencia en pagos QR — el equipo interno de Bind mide ~7 segundos de demora en el procesamiento, mientras Global66 reporta 15-20 segundos percibidos por el usuario final (promedio de respuesta 10-12s, percentil 95 en 16s, según análisis propio de los últimos 3 días).

**Diagnóstico técnico avanzado en la reunión (sin cerrar del todo):**
- Al comparar un caso puntual con logs de ambos lados (validado por Agustín Grau, Fintexa), el tiempo real de procesamiento del lado de Bind fue de **6,8 segundos** (petición entrante 21:04:02 → response 21:04:09) — consistente con la medición interna, no con la de Global66.
- La hipótesis que quedó abierta: la medición de Global66 arranca desde que el usuario presiona el MFA para autorizar el pago, no desde que la petición llega al servidor de Bind — la demora adicional podría estar ocurriendo **antes** de que la petición llegue a Bind (del lado de Global66/cliente), no en el procesamiento de Bind.
- Marco Narváez (Global66) reconoció esto en la propia reunión y se comprometió a revisar ese tramo internamente.
- Agustín Grau (Fintexa) quedó a cargo de analizar las peticiones que ingresan con las credenciales de Global66 para sacar un promedio de tiempo más preciso del lado de Bind.

**Transferencias salientes — segundo tema, mismo cliente:** Global66 también reportó demoras de 8-10 segundos en transferencias salientes pesos-a-pesos, y casos donde una transferencia figura como existente pero no queda acreditada hasta una consulta posterior — hipótesis de Bind (Nicolás Colón/Gonzalo Rivera): podría no estarse insertando la transacción al recibir el webhook, sino recién en la consulta posterior. Alejandro López Torres (Global66) queda a cargo de revisar ese flujo la semana siguiente.

**Seguimiento:** reunión de avance agendada para la semana del 2026-09-08 (sin fecha exacta confirmada en la minuta).

**Conexión con el resto del Cerebro:** esta reunión aporta evidencia técnica concreta al lado "BSF/Global66" de la contradicción abierta en `2_areas/gaps_y_preguntas.md` [2026-09-02] sobre qué cliente motivó el ajuste de tiempos de consulta de Pagos QR (TPay vs. BSF/Global66) — ver item separado `2026-09-03_adquirencia_confirmacion_motivador_tiempos_qr_global66` con el detalle de esa conexión.

> Fuente: reunión "Bind Global66, proximos pasos" (2026-09-02 16:59), minuta Gemini. Participantes Bind PSP: Pablo Gomes, Nicolás Colón, Gonzalo Rivera, Emma Vignoles, Franco Giménez, Pablo Salto. Participantes Global66: Marco Narváez, Alejandro López Torres, Jonathan Castañeda, Sebastián Díaz. Fintexa: Agustín Grau.
