---
id: 2026-09-07_gap-gct-cliente-no-identificado-reclamo-tiempos-qr
pm: nicolas
fecha_captura: 2026-09-07
fuente: "Reunión \"Weekly - Producto / Operaciones\" (2026-09-07)"
producto: transversal
tema: Cliente mencionado como "GCT" con reclamo activo de tiempos de resolución de Pagos QR (hasta 15s) — sin match exacto en log_clientes.md
tipo: gap
destino_propuesto: 2_areas/clientes/log_clientes.md
tipo_destino: actualizar
contradice: "no"
confianza: baja
estado: ingestado
merge_commit: PENDING_2026-09-14
---

En la reunión "Weekly - Producto / Operaciones" (2026-09-07), Gonzalo Rivera y Pablo Gomes discutieron un reclamo de un cliente transcripto como **"GCT"**: demoras de hasta 15 segundos en la resolución de cobros con QR, mientras las mediciones internas de Bind muestran ~7 segundos en base de datos y >10 segundos vía APIM (según lo que Agustín Grau/Fintexa reportó el miércoles previo). Pablo Gomes pidió a Nicolás Colón hacer una prueba en vivo desde un endpoint público para verificar el rendimiento real (ver tarea T-032 en `tareas.md`, ligada a `bajar-tiempos-pagos-qr`).

**Búsqueda en `log_clientes.md`:** no hay ningún cliente cuyo nombre coincida con "GCT". El caso de uso (cliente con volumen de cobro QR relevante, quejándose de latencia, con reunión de seguimiento directa con el equipo técnico) es del mismo patrón que **GST (Hipódromo de Palermo)** — cliente Gambling de riesgo Alto con productos Onboarding+Wallet+QRI, ya con pedidos puntuales documentados en `wallet/pedidos_de_clientes_y_hallazgos_operativos.md` — pero **no hay confirmación**, solo similitud fonética entre "GCT" y "GST" (mismo patrón de error de transcripción de Gemini ya visto con otros nombres este mes, ej. Facard/Favacard, Copel/Coppel). Se registra el texto literal de la minuta ("GCT") sin asumir la identidad.

Este cliente/reclamo es del mismo dominio que el proyecto activo [bajar-tiempos-pagos-qr](../bajar-tiempos-pagos-qr/proyecto.md) (PRD-199) — mismo síntoma que ya reportaron BSF, Global66 y Depay. Al ejecutar T-032, conviene confirmar la identidad real del cliente antes de escribir cualquier hallazgo específico en su ficha.

> Fuente: Reunión "Weekly - Producto / Operaciones" (2026-09-07, minuta Gemini).
