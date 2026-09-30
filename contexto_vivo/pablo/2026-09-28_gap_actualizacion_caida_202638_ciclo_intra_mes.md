---
id: 2026-09-28_gap_actualizacion_caida_202638_ciclo_intra_mes
pm: pablo
fecha_captura: 2026-09-28
fuente: "/sync_metrics — análisis semana 202639 (store acumulado 202536–202639)"
producto: transversal
tema: La caída generalizada de 202638 (asociada a despliegues del 15/9 y 17/9) encaja en un ciclo intra-mes de las NSM — posible patrón estacional nuevo a confirmar
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "2_areas/gaps_y_preguntas.md §[2026-09-22] caída generalizada de volumen coincide con despliegues de riesgo — la evidencia de 202639 sugiere una explicación alternativa (ciclo del mes), no causal"
confianza: media
estado: ingestado
merge_commit: 3492d04
---

**Actualiza el gap `[2026-09-22]` sobre la caída generalizada de volumen de la semana 202638 coincidente con
los despliegues del 15/9 (actualización masiva de domicilios Wallet) y 17/9 (W72.3 Pagos FX)** en
`2_areas/gaps_y_preguntas.md`. Ese gap cerraba preguntando "¿se sostiene en 202639 o fue puntual?".

**Actualización (2026-09-28, semana 202639):** mirando la serie completa, las dos NSM muestran un **ciclo
intra-mes repetido al menos en los últimos tres meses**: pico en la primera semana del mes calendario y
descenso hasta el cierre.

| Mes | Semana 1 | Semana 2 | Semana 3 | Semana 4 |
|---|---|---|---|---|
| NSM#1 jul (202627–202630) | $318.242 M | $279.965 M | $297.488 M | $174.771 M |
| NSM#1 ago (202632–202635) | $364.995 M | $284.837 M | $179.788 M | $207.559 M |
| NSM#1 sep (202636–202639) | $387.389 M | $322.438 M | $197.263 M | $166.577 M |
| NSM#2 ago | $14.687 M | $11.783 M | $7.659 M | $8.094 M |
| NSM#2 sep | $12.197 M | $12.525 M | $8.198 M | $7.942 M |

Contra su semana equivalente de agosto (202634), la semana 202638 estuvo **arriba** en las dos NSM (API BANK
$197.263 M vs. $179.788 M; Payway $8.198 M vs. $7.659 M). Es decir, el −38,8%/−34,5% WoW de 202638 se explica
por la posición en el mes (la semana previa, 202637, todavía caía dentro de la ventana 1-14 del mes), no
necesariamente por los despliegues. Para NSM#2 esto es consistente con el patrón 1 ya confirmado en
`direccion/estacionalidad_metricas.md` (días 1-10, cobro de servicios). **Para NSM#1/Wallet ese mismo archivo
dice que el patrón es "más débil e inconsistente, no asumir sin verificar caso a caso"** — la serie de arriba
es esa verificación: en Wallet el ciclo aparece tres meses seguidos, concentrado en BSF, Sociedad Militar,
CENCOSUD y Credicuotas (probablemente acreditación de sueldos/haberes en los primeros días hábiles).

**Estado propuesto:** la hipótesis causal de los despliegues queda **debilitada, no descartada** (nadie de
Ingeniería/Fintexa confirmó ni negó impacto). Sigue abierta la pregunta original a Ingeniería, pero con
prioridad baja.

**Preguntas para el usuario:**
1. ¿Se da por cerrado el gap de 202638 con esta explicación (ciclo intra-mes), o se mantiene abierta la
   consulta a Ingeniería/Fintexa sobre los despliegues del 15/9 y 17/9?
2. ¿Confirmás el ciclo intra-mes de NSM#1/Wallet (pico en la primera semana, valle al cierre) como patrón
   estacional para sumar a `direccion/estacionalidad_metricas.md`? Si sí, el merge debería agregar ahí una
   entrada "Wallet — pico de primera semana del mes (BSF, Sociedad Militar, CENCOSUD, Credicuotas),
   verificado jul–sep 2026". Requiere permiso explícito (archivo de `direccion/` fuera de los ledgers libres).
