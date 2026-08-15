# Estado Actual — Cómo Venimos

> Tabla de métricas vivas: valor actual de cada North Star Metric y cada KR de foco estratégico, con fecha de medición, fuente y gap contra el target. Completa a [north_star.md](north_star.md) (qué perseguimos) y [estrategia/index.md](estrategia/index.md) (cómo lo ejecutamos) con la pregunta que ninguno de los dos responde: **¿cómo venimos hoy?**
>
> Mantenimiento: se actualiza cuando una fuente (dataset, barrido de Jira, reporte del PM) aporta una medición nueva — no tiene rutina de sync propia todavía. Si un valor no tiene medición, se declara explícitamente "sin baseline" en vez de omitirse o estimarse.

## North Star Metrics

| Métrica | Target | Valor actual | Fecha de medición | Fuente | Gap |
|---|---|---|---|---|---|
| **NSM #1** — Top 2 en volumen operado por API BANK (Banco Industrial) | Top 2 (~30% de crecimiento mensual vs. baseline fin 2025) | **$548.736 M en junio 2026** (+6,6% MoM; −26,0% vs. baseline de 3 meses; −52,4% vs. máximo histórico $1.152.974 M de enero 2026) | Último mes cerrado: junio 2026, con serie mensual desde sep-2025 (46 semanas) | [`2_areas/datasets/metricas_semanales.md`](../../3_recursos/datos/metricas_semanales.md) — `/sync_metrics`, corrida semanal | **El volumen propio ya se mide en la unidad mensual del target; el gap contra el target sigue abierto** porque no se conoce el ranking real de PSPs en API BANK. ⚠️ La caída desde el pico de enero es prácticamente 100% explicada por la salida de Astropay (ver `metricas_semanales.md`, hallazgo 1): *ex-Astropay*, la NSM viene **creciendo** (+15,6% enero→mayo). Ver `../gaps_y_preguntas.md` (2026-07-21). |
| **NSM #2** — Top 6 adquirentes en volumen operado con Payway (Decidir/Prisma) | Top 6 | **$20.850 M en junio 2026 — máximo histórico** (+77,2% MoM; +87,3% vs. baseline de 3 meses) | Último mes cerrado: junio 2026, con serie mensual desde sep-2025 (46 semanas) | [`2_areas/datasets/metricas_semanales.md`](../../3_recursos/datos/metricas_semanales.md) — `/sync_metrics`, corrida semanal | **Idem:** el volumen propio ya se mide, falta el volumen de los primeros 6 adquirentes del gateway para calcular el gap. ⚠️ El 86,8% del volumen (semana 202629) es un solo grupo de clientes (Grupo DESA), que probablemente esté cerca de terminar su rampa de altas. |

> **Qué cambió el 2026-07-21/22:** hasta el 2026-07-21 ambas NSM figuraban como "sin baseline medido". Con la puesta en marcha de [`/sync_metrics`](../../../.claude/skills/sync_metrics/SKILL.md) el Cerebro mide ambas semana a semana, y desde el 2026-07-22 también en **volumen mensual (MoM)** — la unidad en la que el usuario confirmó que se va a expresar el target de mercado. Lo que sigue faltando —y por eso el gap no está cerrado— es ese valor de mercado. Todo porcentaje de arriba es contra baseline interno, no contra la meta. La vista mensual además destapó que la aparente caída de la NSM #1 desde su pico es un artefacto de la salida ya conocida de Astropay, no una tendencia de negocio nueva.

## KRs por foco estratégico

### Foco Onboarding (Pablo Gomes) — [estrategia/foco_onboarding.md](estrategia/foco_onboarding.md)

| KR | Target fin 2026 | Valor actual | Fecha de medición | Fuente | Gap |
|---|---|---|---|---|---|
| **KR1 — Flujo:** % de nuevas cuentas de Wallet validadas en Onboarding (solicitud aprobada) y con legajo guardado | ≥80% | **~5,2%** (15.827 solicitudes aprobadas vs. 304.356 cuentas creadas) | Mayo–julio 2026 (dataset único, no hay serie histórica) | [`2_areas/datasets/hallazgos_2026-07-16_onboarding_vs_wallet.md`](../../3_recursos/datos/hallazgos_2026-07-16_onboarding_vs_wallet.md) | **~75 puntos.** Concentrado en 5 organizaciones dominantes (BSF, Credicuotas, CENCOSUD, Sociedad Militar, Global 66) — sin migrarlas, no hay forma de llegar a 80%. |
| **KR2 — Stock:** % de cuentas existentes con legajo guardado | 30% | **Sin baseline** — tamaño total del stock histórico desconocido, % con legajo presumiblemente ~0 | — | Gap de medición abierto desde 2026-07-17, ver `../gaps_y_preguntas.md` | No se puede calcular el gap sin dimensionar el stock total — primer hito pendiente del roadmap de KR2. |
| KR3 (fricción del funnel) | Sin definir — reservado para cuando KR1 avance | Tasa de rechazo actual: **~47,5%** (61,5% de eso es fricción técnica de OCR, 0,03% es control de riesgo real) | Mayo–julio 2026 | Mismo dataset | No aplica todavía — candidato de referencia para cuando se defina el KR. |

### Foco Pagos FX (Luciana Rudaz) — [estrategia/foco_pagos_fx.md](estrategia/foco_pagos_fx.md)

OKR pendiente de definir por la PM. Sin métrica que trackear todavía.

### Foco Ardid (Nicolás Colón) — [estrategia/foco_ardid.md](estrategia/foco_ardid.md)

OKR pendiente de definir por el PM. Sin métrica que trackear todavía.

## Restricción de capacidad (contexto obligatorio para leer cualquier gap de arriba)

**~1 IDEA entregada cada 3 meses, frente a ~6 IDEAs abiertas simultáneamente en Jira** (dato aportado por el PM en la reunión de validación de estrategia del 2026-07-20, ver T-035 en [`2_areas/tareas_producto.md`](../tareas.md)). Ningún target de arriba es alcanzable sin priorizar duro contra esta restricción — es el dato que debería vetar cualquier lectura optimista de "vamos a cerrar varios KRs en paralelo".

---
*Última actualización: 2026-07-21 — primera medición real de ambas NSM ($147.326 M API BANK, $10.579 M Payway, semana 202629) a partir de `/sync_metrics`. El gap contra el target sigue abierto: falta el valor de mercado.*
*Creado: 2026-07-20 — primer archivo de la capa de Dirección (`0_direccion/`), en el marco de la reforma estructural del Cerebro (ver `0_direccion/decisiones.md`). Sin sync automático propio todavía — se actualiza a mano cuando aparece una medición nueva.*
