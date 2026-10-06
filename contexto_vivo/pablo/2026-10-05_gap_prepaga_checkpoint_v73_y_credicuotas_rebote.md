---
id: 2026-10-05_gap_prepaga_checkpoint_v73_y_credicuotas_rebote
pm: pablo
fecha_captura: 2026-10-05
fuente: "/sync_metrics — análisis semana 202640"
producto: transversal
tema: Checkpoint post-v73 del gap de Tarjeta Prepaga (2026-09-14) y nuevo dato sobre el gap de Credicuotas/cta 2 (2026-09-28)
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: media
estado: en_cola
merge_commit:
---

## [2026-10-05] — Dos actualizaciones de gaps abiertos, semana 202640

### A) Checkpoint post-v73 del gap `[2026-09-14]` (Tarjeta Prepaga)

- **Severidad:** Media
- **Descripción:** El gap de Tarjeta Prepaga proponía tomar el despliegue de v73 (29/09, corrección de la
  base de identificación de BINes) como punto de control, revisando en las corridas 202640-202641 si el
  rechazo de Prepaga y Débito bajaba. Resultado de la primera corrida post-despliegue: **el rechazo de
  Débito bajó de 20,2% a 14,7%** (ya por debajo del promedio de 8 semanas, 17,2%) y **el de Crédito bajó de
  27,3% a 23,7%** (vs. 30,9% de promedio) — mejora clara en ambos medios, consistente con que la corrección
  de BINes esté ayudando. **El rechazo de Tarjeta Prepaga, en cambio, se mantiene en 34,6%** (vs. 34,2% de
  promedio de 8 semanas — prácticamente sin cambio) y **su volumen sigue sin frenar**: $193 M esta semana
  (+39,6% WoW), tendencia de ventana móvil de 4 semanas +494,7%. La corrección de BINes parece explicar
  parte de la mejora en Débito/Crédito, pero no alcanza para explicar ni el rechazo elevado ni el
  crecimiento explosivo de volumen de Prepaga específicamente.
- **Pregunta para el usuario:** ¿Adquirencia confirma si el crecimiento de Prepaga sigue viniendo del alta
  de Western Union (agosto) u otro cliente puntual? Dado que Débito/Crédito sí mejoraron, ¿hay algo
  específico de la configuración de Prepaga que no se corrigió en v73?
- **Estado:** Pendiente — queda una corrida más (202641) del plan de checkpoint original antes de sacar una
  conclusión definitiva sobre si v73 resolvió el problema.

### B) Nuevo dato para el gap `[2026-09-28]` (Credicuotas / Bind PSP liquidaciones cta 2)

- **Severidad:** Media
- **Descripción:** El gap de 2026-09-28 documentaba que Credicuotas venía corriendo volumen de Wallet al
  Agente de Cobros, coincidente con el apagado de "Bind PSP liquidaciones cta 2". Esta semana, **Credicuotas
  en Wallet se recuperó fuerte**: $4.332 M (+157,2% WoW), después de tres semanas en baja ($7.695 M →
  $1.689 M entre 202636 y 202639). Al mismo tiempo, Credicuotas como collector del Agente de Cobros **se
  mantuvo elevado** ($18.392 M, +35,0% WoW) — no bajó para compensar el rebote de Wallet. El rebote de
  Wallet coincide con el arranque de mes de otros clientes grandes (BSF, Sociedad Militar, CENCOSUD), así
  que probablemente sea estacionalidad y no una reversión de la migración — pero **debilita la hipótesis de
  "migración neta"**, ya que ambas fuentes crecieron a la vez esta semana en lugar de moverse en espejo.
  "Bind PSP liquidaciones cta 2" y "cta 8" siguen en $0 (cuarta semana consecutiva) — ver también el gap de
  "cta 39" capturado hoy, que aporta una tercera cuenta de la misma familia con comportamiento sin explicar.
- **Pregunta para el usuario:** sigue abierta la pregunta original — ¿Credicuotas cambió su operatoria a
  fines de agosto? ¿Qué pasó con "cta 2"/"cta 8"? El rebote de esta semana en Wallet no la responde, solo
  agrega un dato a favor de que Wallet y Agente de Cobros se mueven por motivos estacionales independientes,
  más que por una migración 1 a 1.
- **Estado:** Pendiente.
