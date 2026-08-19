# Métricas semanales — North Star Metrics

> Reporte incremental de [`/sync_metrics`](../../../.claude/skills/sync_metrics/SKILL.md). **La semana más
> reciente va arriba**; nada se borra — este archivo es el registro de todo lo que se fue reportando semana
> a semana. Cada entrada tiene la misma estructura: (1) estado de las NSM, (2) hallazgos, (3) anexo de
> soporte.
>
> **Fuente:** store acumulado en [`datos_metricas_semanales/`](datos_metricas_semanales/index.md),
> alimentado con los CSV agregados que el PM exporta de la base cada semana. Agregados puros, sin PII.
> **Definición de las NSM:** ver [`north_star.md`](../../2_areas/direccion/north_star.md) y el detalle de scope en
> el SKILL.
> **Objetivo:** las dos NSM (top 2 API BANK, top 6 Payway) **no tienen todavía un valor de mercado conocido**
> — ese gap está reconocido desde el origen del objetivo, y cuando se consiga va a venir expresado en
> **volumen mensual** (indicación del usuario, 2026-07-22). Hasta entonces, todo porcentaje de esta serie es
> contra **baseline interno**, no contra la meta.
>
> **Unidad de medida — el WoW (semana vs. semana anterior) es el KPI principal**, el número más cercano y el
> que más importa mirar semana a semana (indicación del usuario, 2026-07-22). La **vista mensual (MoM)** se
> agrega como contexto adicional — importa porque el objetivo de mercado de ambas NSM se va a expresar en
> volumen mensual — pero no reemplaza al semanal. **MoM se mide siempre por el mismo tramo de semanas**: si el
> mes en curso lleva cerradas 3 semanas, se compara esa suma contra la suma de las primeras 3 semanas del mes
> anterior (nunca mes completo contra mes completo, que compararía cosas de distinto tamaño), simplificando
> a que **1 mes = 4 semanas**. Una semana se asigna al mes que contiene su **jueves** (igual que ISO asigna
> semana→año) — eso solo define la etiqueta ("junio", "julio"), la comparación en sí siempre es por tramo.

---

## Semana 202633 · 10 → 17 de agosto de 2026

*Reportado el 2026-08-18. 50 semanas cerradas en el store (202536 → 202633). Corrida sin fila de encabezado
en los CSV de origen, resuelta por forma/orden de columnas como de costumbre. La dimensión `dim_collectors`
llegó en el lote (`collectors.csv`) pero quedó pendiente de ingesta — su export no tiene una fila de
encabezado y el pipeline nunca tuvo definido el orden posicional de columnas de esa tabla (a diferencia de
operaciones/transacciones/cuentas/comercios/transferencias, que sí lo tienen desde el 2026-08-11). No bloqueó
el resto de la corrida — `dim_collectors` es opcional para el `ingest` — pero los nombres de collectors
nuevos que hayan aparecido esta semana no se actualizaron; ver gap abierto.*

### 1 · Estado de las NSM

#### 1a · Detalle semanal (WoW) — KPI principal

| | **NSM #1 — Volumen API BANK** *(oficial: Wallet + Agente de Cobros)* | **NSM #2 — Volumen Payway** |
|---|---|---|
| **Volumen de la semana** | **$284.837 M** | **$11.783 M** |
| Operaciones / transacciones | 1.614.543 | 103.128 |
| Ticket promedio | $176.420 | $114.255 |
| WoW | **−22,0%** | **−19,8%** |
| vs. promedio 4 semanas | +5,8% | +14,8% |
| vs. baseline 13 semanas | +19,0% *(baseline $239.446 M)* | +75,6% *(baseline $6.711 M)* |
| vs. máximo histórico | −32,1% *(máx $419.802 M, sem. 202610)* | −19,8% *(máx $14.687 M, sem. 202632)* |
| Tendencia 6 semanas | +3,0% por semana | +8,4% por semana |
| z-score vs. 8 previas | +0,48 | +1,07 |

#### 1b · Tendencia — ventana móvil de 4 semanas (protagonista; NO es un cierre de mes calendario)

> **Nota de metodología:** compara las últimas 4 semanas cerradas contra las 4 inmediatamente anteriores,
> sin relación a mes calendario — se actualiza todas las semanas. No leer como facturación de "el mes". La
> caída WoW de esta semana en ambas NSM se explica en gran parte por estacionalidad — ver hallazgo 1.

| | **NSM #1 — Volumen API BANK** | **NSM #2 — Volumen Payway** |
|---|---|---|
| Últimas 4 semanas (202630 → 202633) | $1.064.222 M | $42.263 M |
| 4 semanas previas (202626 → 202629) | $1.059.022 M | $33.281 M |
| Tendencia | **+0,5%** | **+27,0%** |

*Serie mensual completa (mes completo vs. mes completo) desde sep-2025 en el anexo (sección 3).*

#### 1c · Composición de NSM#1 — Operaciones (Wallet) vs. Transferencias Agente de Cobros

| | Volumen | Share | WoW |
|---|---|---|---|
| Operaciones (Wallet) | $147.181 M | 51,7% | −35,1% |
| Transferencias Agente de Cobros | $137.656 M | 48,3% | −0,4% |

**Desglose NSM #1 — IN / OUT (total oficial):**

| | Volumen | Share | WoW | Tendencia 6s |
|---|---|---|---|---|
| **OUT** | $200.757 M | 70,5% | −11,9% | +2,9% |
| **IN** | $84.081 M | 29,5% | −38,7% | +3,3% |

Por tipo (Operaciones/Wallet): Transferencia Saliente $73.765 M (50,1% de Wallet, WoW −29,3%) ·
Transferencia Entrante $69.605 M (47,3%, WoW −41,4%) · Pago con QR $3.778 M (2,6%, WoW +4,4%) · Debin
Recurrente Crédito $33,6 M (WoW −26,9%) · **Transf. Pull Crédito y Débito en $0** (sigue el postmortem de
marzo 2026).

Por tipo (Agente de Cobros — ya sumado arriba): Saliente $123.214 M (89,5% de TAC, WoW +2,7%) · Entrante
CVU $14.382 M (10,4%, WoW −20,9%) · Entrante CBU $59,7 M (0,0%, WoW −31,0%).

Top 8 collectors (TAC): Bind PSP liquidaciones cta 14 $47.448 M (34,5%) · Banelsip $24.945 M (18,1%) ·
Bind PSP liquidaciones cta 2 $19.322 M (14,0%) · BindPSP pagos Cencosud $8.319 M (6,0%) · Tienda Nube
$6.354 M (4,6%) · Credicuotas $2.845 M (2,1%) · Cucuru $2.482 M (1,8%) · Bind PSP liquidaciones cta 8
$2.434 M (1,8%).

**Desglose NSM #2 — canal y medio de pago:**

| | Volumen | Share | WoW |
|---|---|---|---|
| Botón Simple | $11.070 M | 94,0% | −20,5% |
| Botón 2.0 | $713 M | 6,0% | −5,7% |
| Tarjeta de Débito | $7.586 M | 64,4% | −21,2% |
| Tarjeta de Crédito | $4.177 M | 35,5% | −16,8% |
| Tarjeta Prepaga | $19,8 M | 0,2% | −46,7% |

#### 1d · Palancas — cada una atada a su NSM (Tendencia de 4 semanas móviles como protagonista; WoW secundario)

**NSM#1:**

| Palanca | Categoría | Volumen | % del padre | Tendencia | Prev. tendencia | WoW |
|---|---|---:|---:|---:|---:|---:|
| OUT | Entrante / Saliente | $200.757 M | 70,5% | +1,1% | $673.037 M | −11,9% |
| Operaciones (Wallet) | Componente de NSM#1 | $147.181 M | 51,7% | −2,0% | $675.350 M | −35,1% |
| Transferencias Agente de Cobros | Componente de NSM#1 | $137.656 M | 48,3% | +4,9% | $383.672 M | −0,4% |
| Saliente (Agente de Cobro) | Tipo (Agente de Cobros) | $123.214 M | 89,5% | +5,1% | $335.388 M | +2,7% |
| Saliente | Entrante / Saliente (TAC) | $123.214 M | 89,5% | +5,1% | $335.388 M | +2,7% |
| IN | Entrante / Saliente | $84.081 M | 29,5% | −0,6% | $385.985 M | −38,7% |
| Transferencia Saliente | Tipo de operación (Wallet) | $73.765 M | 50,1% | −3,3% | $324.643 M | −29,3% |
| Transferencia Entrante | Tipo de operación (Wallet) | $69.605 M | 47,3% | −1,2% | $337.664 M | −41,4% |
| Entrante | Entrante / Saliente (TAC) | $14.442 M | 10,5% | +3,3% | $48.284 M | −20,9% |
| Entrante CVU | Tipo (Agente de Cobros) | $14.382 M | 10,4% | +3,3% | $48.054 M | −20,9% |
| Pago con QR | Tipo de operación (Wallet) | $3.778 M | 2,6% | +7,8% | $13.007 M | +4,4% |
| Entrante CBU | Tipo (Agente de Cobros) | $59,7 M | 0,0% | +15,5% | $230 M | −31,0% |
| Debin Recurrente Crédito | Tipo de operación (Wallet) | $33,6 M | 0,0% | +173,5% | $36,9 M | −26,9% |
| Transf. Pull Crédito | Tipo de operación (Wallet) | $0,00 M | 0,0% | s/d | $0,00 M | s/d |
| Transf. Pull Débito | Tipo de operación (Wallet) | $0,00 M | 0,0% | s/d | $0,00 M | s/d |
| *Transf. interna saliente* | *Palanca indirecta* | *$3.158 M* | *1,1%* | *−53,0%* | *$66.333 M* | *−27,0%* |
| *Transf. interna entrante* | *Palanca indirecta* | *$3.158 M* | *1,1%* | *−53,0%* | *$66.333 M* | *−27,0%* |
| *Viaje QR* | *Palanca indirecta* | *$38,9 M* | *0,0%* | *−12,0%* | *$181 M* | *−4,3%* |
| *Compra Dólar CCL* | *Palanca indirecta* | *$0,05 M* | *0,0%* | *−36,4%* | *$5,3 M* | *−98,4%* |
| *Pago FX* | *Palanca indirecta* | *$0,03 M* | *0,0%* | *s/d* | *$0,00 M* | *s/d* |
| *Cuentas de Wallet creadas* | *Leading indicator* | *25.680* | — | *−19,0%* | *143.637* | *−16,2%* |
| *Venta Dólar CCL* | *Palanca indirecta* | *$0,00 M* | *0,0%* | *−1,8%* | *$0,00 M* | *−75,9%* |
| *Ingreso con tarjeta* | *Palanca indirecta* | *$0,00 M* | *0,0%* | *s/d* | *$0,00 M* | *s/d* |

*(en cursiva: palancas de contexto, no suman al total de NSM#1)*

**NSM#2:**

| Palanca | Categoría | Volumen | % del padre | Tendencia | Prev. tendencia | WoW |
|---|---|---:|---:|---:|---:|---:|
| Botón Simple | Canal (Payway) | $11.070 M | 94,0% | +28,6% | $31.274 M | −20,5% |
| Tarjeta de Débito | Medio de pago (Payway) | $7.586 M | 64,4% | +22,6% | $21.667 M | −21,2% |
| Tarjeta de Crédito | Medio de pago (Payway) | $4.177 M | 35,5% | +35,0% | $11.564 M | −16,8% |
| Botón 2.0 | Canal (Payway) | $713 M | 6,0% | +1,6% | $2.007 M | −5,7% |
| Tarjeta Prepaga | Medio de pago (Payway) | $19,8 M | 0,2% | +59,6% | $50,4 M | −46,7% |
| Tarjeta de Crédito Cuotas | Medio de pago (Payway) | $0,00 M | 0,0% | s/d | $0,00 M | s/d |
| *Liquidador* | *Fuera de Payway* | *$25.574 M* | *217,0%* | *+0,7%* | *$67.579 M* | *+22,4%* |
| *Transferencia 3.0* | *Fuera de Payway* | *$18.877 M* | *160,2%* | *+2,1%* | *$65.745 M* | *−21,2%* |
| *Transf. Entrante CVU* | *Fuera de Payway* | *$15.767 M* | *133,8%* | *+2,1%* | *$46.933 M* | *−4,3%* |
| *MPOS / POS* | *Fuera de Payway* | *$1.533 M* | *13,0%* | *−5,2%* | *$5.065 M* | *+5,2%* |
| *Comercios de Adquirencia creados* | *Leading indicator* | *149* | — | *+316,0%* | *119* | *−17,2%* |
| *EcoCerrado* | *Fuera de Payway* | *$0,00 M* | *0,0%* | *+13400,0%* | *$0,00 M* | *s/d* |

*(en cursiva: palancas de contexto, fuera del scope de NSM#2 hoy)*

---

### 2 · Hallazgos y puntos más importantes de la semana

#### 🔴 1. La caída semanal en ambas métricas se explica por estacionalidad, no por un problema de negocio.

Esta semana (10 al 17 de agosto) cayó −22,0% en Volumen API Bank y −19,8% en Volumen Payway frente a la
semana anterior. La semana anterior (3 al 10 de agosto) coincidió con la ventana de pico de cobro de
servicios y facturas de inicio de mes, que empuja fuerte el volumen de Payway y, más débilmente, el de
Wallet. Al salir de esa ventana, es esperable que el volumen vuelva a un nivel más bajo.
**Por qué importa:** la comparación contra el promedio de las últimas 4 semanas sigue siendo positiva
(+5,8% y +14,8% respectivamente), lo que confirma que no hay una desaceleración real detrás de la caída
semanal. **Qué hacer:** no leer el WoW negativo como alarma; mirar la tendencia de ventana móvil, que sigue
en positivo en ambas NSM.

#### 🔴 2. Terra Blockchain profundiza su caída por tercera semana consecutiva.

El volumen de Terra Blockchain en Wallet volvió a caer, esta vez −87,9% frente a su promedio de las últimas
4 semanas ($7.660 M a $925 M). Es la tercera semana seguida de caída sostenida: pasó de −75,7% (semana del
4 de agosto) a −79,5% (semana del 11 de agosto) y ahora a −87,9%.
**Por qué importa:** el patrón ya no admite lectura de ruido semanal. **Qué hacer:** confirmar con el
cliente si sigue operativo con normalidad — escalar a Soporte/Comercial si no hay explicación conocida.

#### 🟡 3. BSF concentra el 60,5% del volumen de Wallet.

BSF (Carrefour) sigue siendo, por lejos, el mayor cliente de Operaciones de Wallet, con el 60,5% del
volumen de la semana y el top-3 (BSF, Sociedad Militar, Global 66) acumulando el 82,6%.
**Por qué importa:** expone la métrica a cualquier variación puntual de este cliente. **Qué hacer:** sin
acción inmediata — se sigue reportando como recordatorio de que la volatilidad semanal de NSM#1 va a seguir
atada al comportamiento de este cliente en particular.

#### 🟡 4. La Virginia sostiene un ritmo de altas de comercios fuera de lo habitual por tercera semana.

Las altas de comercios de Adquirencia siguen en un nivel estructuralmente más alto que hace tres meses
(+148,7% comparando el promedio de las últimas 4 semanas contra el de hace 13 semanas). Esta semana, 142 de
las 149 altas totales (95,3%) corresponden a La Virginia — mismo patrón que las dos semanas anteriores.
**Por qué importa:** ya no es un pico puntual sino un ritmo sostenido de alta en lote. **Qué hacer:**
confirmar con Comercial/Onboarding si responde a una campaña planificada, para poder proyectar cuánto más
va a durar.

#### 🟢 5. El volumen de Payway sostiene una tendencia de crecimiento fuerte.

Volumen Payway viene creciendo a un ritmo de +8,4% por semana en las últimas 6 semanas, acumulando +75,6%
contra el baseline de 13 semanas. La ventana móvil de las últimas 4 semanas cerradas ($42.263 M) creció
+27,0% contra las 4 semanas previas.
**Por qué importa:** el crecimiento está bien distribuido entre Débito, Crédito y Botón Simple, no
concentrado en un solo medio de pago — es la señal más sólida de la semana.

#### 🟢 6. Las transferencias internas de Wallet vienen en caída sostenida.

Las transferencias internas dentro de Wallet (que no suman a Volumen API Bank pero alimentan el saldo que
después opera contra el banco) cayeron a una tendencia de −28,9% por semana en las últimas 6 semanas, con
una caída acumulada de −53,0% en la ventana móvil de 4 semanas.
**Por qué importa:** el volumen en sí es chico ($3.158 M, 1,1% del total), pero la caída sostenida vale la
pena monitorearla como posible antecedente de menor actividad interna de saldo.

---

### 3 · Anexo — Métricas de soporte

**Serie mensual completa (desde sep-2025) — volumen total del mes, para ver la magnitud absoluta.**

| Mes | NSM #1 *(oficial)* | MoM (mes completo) | NSM #2 | MoM (mes completo) |
|---|---|---|---|---|
| 2025-09 | $476.139 M | s/d | $4.172 M | s/d |
| 2025-10 | $730.477 M | +53,4% | $5.042 M | +20,8% |
| 2025-11 | $625.391 M | −14,4% | $4.401 M | −12,7% |
| 2025-12 | $813.380 M | +30,1% | $4.640 M | +5,4% |
| 2026-01 | $1.546.504 M | +90,1% | $5.211 M | +12,3% |
| 2026-02 | $1.323.010 M | −14,5% | $6.268 M | +20,3% |
| 2026-03 | $1.451.705 M | +9,7% | $9.611 M | +53,3% |
| 2026-04 | $1.069.065 M | −26,4% | $12.021 M | +25,1% |
| 2026-05 | $853.360 M | −20,2% | $11.768 M | −2,1% |
| 2026-06 | $884.400 M | +3,6% | $20.850 M | +77,2% |
| 2026-07 | $1.310.086 M | +48,1% | $43.962 M | +110,9% |
| 2026-08* | **$649.833 M** | −50,4% | **$26.470 M** | −39,8% |

*(*) mes en curso, todavía no cerraron todas sus semanas — no comparable 1:1 contra un mes completo.*

**Salud (no suman al volumen NSM):**

| Métrica | Semana | Media 8 semanas |
|---|---|---|
| NSM #1 — tasa de rechazo | 0,3% | 0,7% |
| NSM #1 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 — tasa de rechazo | 20,0% | 21,6% |
| NSM #2 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 / Crédito — rechazo | 29,3% | 30,3% |
| NSM #2 / Débito — rechazo | 14,9% | 16,6% |
| NSM #2 / Prepaga — rechazo | 35,3% | 29,7% |
| TAC Agente de Cobros — tasa de falla (no COMPLETED) | 0,3% | 0,3% |

**Altas (leading indicator del volumen):**

- **Cuentas de Wallet:** 25.680 en la semana (media 8 semanas 32.246; −16,2% WoW). Top: BSF 8.945 (34,8%) ·
  CENCOSUD 5.690 (22,2%) · Credicuotas 4.563 (17,8%) · Global 66 3.038 (11,8%) · Coppel 1.029 (4,0%).
- **Comercios de Adquirencia:** 149 en la semana (ver hallazgo 4). Top: La Virginia 142 (95,3%) · Consorcio
  Abierto 2 · Pedidos Ya 2 · BINDPAGO 1 · Fletalo TECH SA 1.

**Top clientes NSM #1 (Operaciones/Wallet):** BSF $88.985 M (60,5%, ver hallazgo 3) · Sociedad Militar
$18.576 M (12,6%) · Global 66 $13.987 M (9,5%) · CENCOSUD $11.452 M (7,8%) · Credicuotas $5.653 M (3,8%) ·
Depay $2.271 M (1,5%) · GALLO $1.811 M (1,2%) · Terra Blockchain $925 M (0,6%, ver hallazgo 2).

**Top entidades NSM #2:** EDEA $2.803 M (23,8%) · EDESA $2.281 M (19,4%) · EDEN $1.998 M (17,0%) · EDELAP
$1.868 M (15,9%) · EDES $929 M (7,9%) · FAVACARD $514 M (4,4%) · RIPSA $395 M (3,3%) · Tarjeta Sucredito
$296 M (2,5%).

---

*Próxima corrida: semana 202634 (17 → 24 de agosto de 2026).*

---

## Semana 202632 · 3 → 10 de agosto de 2026

*Reportado el 2026-08-11. 49 semanas cerradas en el store (202536 → 202632). **Corrida sin fila de
encabezado en los CSV de origen** (la herramienta de export del usuario no la incluye) — el pipeline
resolvió los 7 archivos afectados por forma/orden de columnas (posición, no nombre), con la asunción
impresa en el log de `inspect`/`ingest`; ver nota en `changelog.md`. **Primera corrida con la tendencia de
ventana móvil de 4 semanas como protagonista** (reemplaza a la vista mensual por tramo "1b · MoM" de
semanas anteriores, decisión del usuario del 2026-08-04) — la serie mensual completa se conserva igual en
el anexo (sección 3) como contexto histórico.*

### 1 · Estado de las NSM

#### 1a · Detalle semanal (WoW) — KPI principal

| | **NSM #1 — Volumen API BANK** *(oficial: Wallet + Agente de Cobros)* | **NSM #2 — Volumen Payway** |
|---|---|---|
| **Volumen de la semana** | **$364.995 M** | **$14.687 M** |
| Operaciones / transacciones | 1.712.725 | 134.613 |
| Ticket promedio | $213.108 | $109.106 |
| WoW | **+52,3%** | **+79,3%** |
| vs. promedio 4 semanas | +47,2% | +69,0% |
| vs. baseline 13 semanas | +55,7% *(baseline $234.450 M)* | **+149,3%** *(baseline $5.891 M)* |
| vs. máximo histórico | −13,1% *(máx $419.802 M, sem. 202610)* | **+0,0%** *(máximo histórico de la serie)* |
| Tendencia 6 semanas | −0,1% por semana | +7,0% por semana |
| z-score vs. 8 previas | +2,22 | +3,49 |

#### 1b · Tendencia — ventana móvil de 4 semanas (protagonista; NO es un cierre de mes calendario)

> **Nota de metodología:** compara las últimas 4 semanas cerradas contra las 4 inmediatamente anteriores,
> sin relación a mes calendario — se actualiza todas las semanas. No leer como facturación de "el mes".

| | **NSM #1 — Volumen API BANK** | **NSM #2 — Volumen Payway** |
|---|---|---|
| Últimas 4 semanas (202629 → 202632) | $1.076.874 M | $41.060 M |
| 4 semanas previas (202625 → 202628) | $927.976 M | $26.587 M |
| Tendencia | **+16,0%** | **+54,4%** |

*Serie mensual completa (mes completo vs. mes completo) desde sep-2025 en el anexo (sección 3).*

#### 1c · Composición de NSM#1 — Operaciones (Wallet) vs. Transferencias Agente de Cobros

| | Volumen | Share | WoW |
|---|---|---|---|
| Operaciones (Wallet) | $226.733 M | 62,1% | **+24,3%** |
| Transferencias Agente de Cobros | $138.263 M | 37,9% | **+141,7%** |

**Desglose NSM #1 — IN / OUT (total oficial):**

| | Volumen | Share | WoW | Tendencia 6s |
|---|---|---|---|---|
| **OUT** | $227.910 M | 62,4% | +67,7% | +0,6% |
| **IN** | $137.086 M | 37,6% | +32,2% | −1,2% |

Por tipo (Operaciones/Wallet): Transferencia Entrante $118.780 M (52,4% de Wallet, WoW +25,5%) ·
Transferencia Saliente $104.290 M (46,0%, WoW +23,5%) · Pago con QR $3.617 M (1,6%, WoW +9,8%) · Debin
Recurrente Crédito $46,0 M (WoW +208,3%) · **Transf. Pull Crédito y Débito en $0** (sigue el postmortem de
marzo 2026).

Por tipo (Agente de Cobros — ya sumado arriba): Saliente $120.003 M (86,8% de TAC, WoW +149,0%) · Entrante
CVU $18.173 M (13,1%, WoW +102,7%) · Entrante CBU $86,6 M (0,1%, WoW +219,1%).

Top 8 collectors (TAC): Bind PSP liquidaciones cta 14 $39.674 M (28,7%) · Bind PSP liquidaciones cta 2
$21.246 M (15,4%) · Banelsip $20.268 M (14,7%) · BindPSP pagos Cencosud $12.602 M (9,1%) · Tienda Nube
$6.827 M (4,9%) · Bind PSP liquidaciones cta 39 $6.647 M (4,8%, ver hallazgo 3) · Credicuotas $5.419 M
(3,9%) · Travel Rock $2.858 M (2,1%).

**Desglose NSM #2 — canal y medio de pago:**

| | Volumen | Share | WoW |
|---|---|---|---|
| Botón Simple | $13.931 M | 94,9% | +76,2% |
| Botón 2.0 | $756 M | 5,1% | +166,9% |
| Tarjeta de Débito | $9.632 M | 65,6% | +104,1% |
| Tarjeta de Crédito | $5.018 M | 34,2% | +45,1% |
| Tarjeta Prepaga | $37,2 M | 0,3% | +213,1% |

#### 1d · Palancas — cada una atada a su NSM (Tendencia de 4 semanas móviles como protagonista; WoW secundario)

**NSM#1:**

| Palanca | Categoría | Volumen | % del padre | Tendencia | Prev. tendencia | WoW |
|---|---|---:|---:|---:|---:|---:|
| OUT | Entrante / Saliente | $227.910 M | 62,4% | +26,0% | $556.528 M | +67,7% |
| Operaciones (Wallet) | Componente de NSM#1 | $226.733 M | 62,1% | +4,3% | $634.733 M | +24,3% |
| Transferencias Agente de Cobros | Componente de NSM#1 | $138.263 M | 37,9% | +41,5% | $293.243 M | +141,7% |
| IN | Entrante / Saliente | $137.086 M | 37,6% | +1,1% | $371.448 M | +32,2% |
| Saliente (Agente de Cobro) | Tipo (Agente de Cobros) | $120.003 M | 86,8% | +49,8% | $246.585 M | +149,0% |
| Saliente | Entrante / Saliente (TAC) | $120.003 M | 86,8% | +49,8% | $246.585 M | +149,0% |
| Transferencia Entrante | Tipo de operación (Wallet) | $118.780 M | 52,4% | +1,6% | $324.755 M | +25,5% |
| Transferencia Saliente | Tipo de operación (Wallet) | $104.290 M | 46,0% | +6,9% | $297.657 M | +23,5% |
| Entrante | Entrante / Saliente (TAC) | $18.260 M | 13,2% | −2,2% | $46.658 M | +103,0% |
| Entrante CVU | Tipo (Agente de Cobros) | $18.173 M | 13,1% | −2,0% | $46.273 M | +102,7% |
| Pago con QR | Tipo de operación (Wallet) | $3.617 M | 1,6% | +13,0% | $12.286 M | +9,8% |
| Entrante CBU | Tipo (Agente de Cobros) | $86,6 M | 0,1% | −31,5% | $385 M | +219,1% |
| Debin Recurrente Crédito | Tipo de operación (Wallet) | $46,0 M | 0,0% | +119,7% | $34,9 M | +208,3% |
| Transf. Pull Crédito | Tipo de operación (Wallet) | $0,00 M | 0,0% | s/d | $0,00 M | s/d |
| Transf. Pull Débito | Tipo de operación (Wallet) | $0,00 M | 0,0% | s/d | $0,00 M | s/d |
| *Transf. interna saliente* | *Palanca indirecta* | *$4.324 M* | *1,2%* | *−28,6%* | *$64.019 M* | *−31,9%* |
| *Transf. interna entrante* | *Palanca indirecta* | *$4.324 M* | *1,2%* | *−28,6%* | *$64.019 M* | *−31,9%* |
| *Viaje QR* | *Palanca indirecta* | *$40,7 M* | *0,0%* | *−11,9%* | *$187 M* | *+2,7%* |
| *Compra Dólar CCL* | *Palanca indirecta* | *$3,3 M* | *0,0%* | *−35,5%* | *$5,3 M* | *+9567,2%* |
| *Cuentas de Wallet creadas* | *Leading indicator* | *30.652* | — | *−9,1%* | *135.129* | *+1,9%* |
| *Venta Dólar CCL* | *Palanca indirecta* | *$0,00 M* | *0,0%* | *+199,7%* | *$0,00 M* | *+226,8%* |
| *Ingreso con tarjeta* | *Palanca indirecta* | *$0,00 M* | *0,0%* | *s/d* | *$0,00 M* | *−100,0%* |

*(en cursiva: palancas de contexto, no suman al total de NSM#1)*

**NSM#2:**

| Palanca | Categoría | Volumen | % del padre | Tendencia | Prev. tendencia | WoW |
|---|---|---:|---:|---:|---:|---:|
| Botón Simple | Canal (Payway) | $13.931 M | 94,9% | +56,7% | $24.918 M | +76,2% |
| Tarjeta de Débito | Medio de pago (Payway) | $9.632 M | 65,6% | +48,3% | $17.355 M | +104,1% |
| Tarjeta de Crédito | Medio de pago (Payway) | $5.018 M | 34,2% | +66,0% | $9.186 M | +45,1% |
| Botón 2.0 | Canal (Payway) | $756 M | 5,1% | +19,9% | $1.669 M | +166,9% |
| Tarjeta Prepaga | Medio de pago (Payway) | $37,2 M | 0,3% | +60,8% | $46,1 M | +213,1% |
| Tarjeta de Crédito Cuotas | Medio de pago (Payway) | $0,00 M | 0,0% | s/d | $0,00 M | s/d |
| *Transferencia 3.0* | *Fuera de Payway* | *$23.958 M* | *163,1%* | *+3,8%* | *$61.228 M* | *+96,6%* |
| *Liquidador* | *Fuera de Payway* | *$20.900 M* | *142,3%* | *+48,6%* | *$49.766 M* | *+147,8%* |
| *Transf. Entrante CVU* | *Fuera de Payway* | *$16.469 M* | *112,1%* | *+18,5%* | *$39.960 M* | *+113,9%* |
| *MPOS / POS* | *Fuera de Payway* | *$1.458 M* | *9,9%* | *+10,3%* | *$4.453 M* | *+65,0%* |
| *Comercios de Adquirencia creados* | *Leading indicator* | *180* | — | *−8,0%* | *410* | *+56,5%* |
| *EcoCerrado* | *Fuera de Payway* | *$0,00 M* | *0,0%* | *s/d* | *$0,00 M* | *−100,0%* |

*(en cursiva: palancas de contexto, fuera del scope de NSM#2 hoy)*

---

### 2 · Hallazgos y puntos más importantes de la semana

#### 🔴 1. Payway toca su máximo histórico ($14.687 M) — el pico está concentrado en distribuidoras eléctricas, consistente con el cobro de servicios de inicio de mes.

El volumen de NSM#2 subió +79,3% WoW y superó por primera vez el techo anterior de $10.579 M (sem. 202629).
Más del 85% del volumen de la semana lo explican distribuidoras de energía eléctrica (EDESA, EDEA, EDEN,
EDELAP, EDES) — coincide con la ventana de días 1 a 10 del mes, el pico habitual de cobro de facturas de
servicios ya documentado como estacionalidad conocida de esta NSM.
**Por qué importa:** parte del salto es estacional, no estructural — pero la tendencia de ventana móvil
también acelera fuerte (+54,4% vs. las 4 semanas previas), así que conviene revisar el nivel una vez pasada
la ventana de cobro de servicios para separar ambos efectos. **Qué hacer:** no leer $14.687 M como el nuevo
piso semanal permanente todavía; comparar contra la semana 11-17 de agosto (fuera de la ventana 1-10) antes
de sacar conclusiones de tendencia.

#### 🔴 2. Las altas de comercios de Adquirencia se triplicaron (+309,1%) — segunda semana seguida concentradas en "La Virginia".

180 altas nuevas vs. una mediana de 8 semanas de 44, con **"La Virginia" explicando 161 (89,4%)**. La semana
pasada (202631) el mismo cliente ya había explicado el 61% de un salto similar (115 altas). Dos semanas
seguidas del mismo patrón deja de leerse como una carga puntual.
**Por qué importa:** es consistente con una activación comercial en curso, y coincide con el trabajo activo
de onboarding de personas jurídicas para este mismo cliente. **Qué hacer:** confirmar con el equipo
comercial si es una campaña de alta en lote planificada (y si va a seguir en las próximas semanas), para no
volver a leer cada salto como una sorpresa nueva.

#### 🟡 3. Transferencias salientes del Agente de Cobros casi se duplican (+149,0% WoW) — "Bind PSP liquidaciones cta 39" salta de casi cero a $6,6 M.

El lado saliente de TAC llegó a $120.003 M y ya es el 86,8% de esa palanca. Dentro de ese salto, la cuenta
"Bind PSP liquidaciones cta 39" pasó de un volumen marginal a $6.647 M (4,8% de TAC, WoW +4.563,9%) — un
salto demasiado grande para pasar como ruido.
**Por qué importa:** las cuentas de liquidación interna (cta 14, cta 2) ya son conocidas como las de mayor
volumen de TAC — esta es la primera vez que "cta 39" aparece con un salto de este tamaño, y no hay contexto
todavía sobre si es una cuenta operativa interna o un movimiento de cliente real.
**Qué hacer:** confirmar el origen de "cta 39" antes de contarlo como crecimiento comercial.

#### 🟢 4. Las altas de cuentas de Wallet sostienen una tendencia estructural al alza (+35,8% vs. 13 semanas atrás).

El promedio de las últimas 4 semanas (30.710 altas) sigue firme por encima del de hace 13 semanas (22.613),
repartido entre los mismos clientes de siempre (BSF, CENCOSUD, Credicuotas, Global 66).
**Por qué importa:** es un leading indicator saludable — la base de cuentas activas sigue ampliándose, lo
que suele adelantar crecimiento de volumen en NSM#1.

#### 🟢 5. La concentración de BSF en Wallet se mantiene estable (~63%) — riesgo conocido, sin cambios esta semana.

BSF explica $142.518 M de Operaciones/Wallet (62,9%, prácticamente igual al 63,2% de la semana pasada) y el
top-3 (BSF + Sociedad Militar + Global 66) llega a 84,5%.
**Por qué importa:** sin novedad — se sigue reportando como recordatorio de que la volatilidad semanal de
NSM#1 va a seguir atada al comportamiento de este cliente en particular.

---

### 3 · Anexo — Métricas de soporte

**Serie mensual completa (desde sep-2025) — volumen total del mes, para ver la magnitud absoluta.**

| Mes | NSM #1 *(oficial)* | MoM (mes completo) | NSM #2 | MoM (mes completo) |
|---|---|---|---|---|
| 2025-09 | $476.139 M | s/d | $4.172 M | s/d |
| 2025-10 | $730.477 M | +53,4% | $5.042 M | +20,8% |
| 2025-11 | $625.391 M | −14,4% | $4.401 M | −12,7% |
| 2025-12 | $813.380 M | +30,1% | $4.640 M | +5,4% |
| 2026-01 | $1.546.504 M | +90,1% | $5.211 M | +12,3% |
| 2026-02 | $1.323.010 M | −14,5% | $6.268 M | +20,3% |
| 2026-03 | $1.451.705 M | +9,7% | $9.611 M | +53,3% |
| 2026-04 | $1.069.065 M | −26,4% | $12.021 M | +25,1% |
| 2026-05 | $853.360 M | −20,2% | $11.768 M | −2,1% |
| 2026-06 | $884.400 M | +3,6% | $20.850 M | +77,2% |
| 2026-07 | $1.310.086 M | +48,1% | $43.962 M | +110,9% |
| 2026-08* | **$364.995 M** | −72,1% | **$14.687 M** | −66,6% |

*(*) mes en curso, todavía no cerraron todas sus semanas — no comparable 1:1 contra un mes completo.*

**Salud (no suman al volumen NSM):**

| Métrica | Semana | Media 8 semanas |
|---|---|---|
| NSM #1 — tasa de rechazo | 0,5% | 1,0% |
| NSM #1 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 — tasa de rechazo | 18,5% | 22,9% |
| NSM #2 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 / Crédito — rechazo | 28,1% | 31,7% |
| NSM #2 / Débito — rechazo | 13,5% | 17,8% |
| NSM #2 / Prepaga — rechazo | 25,4% | 31,0% |
| TAC Agente de Cobros — tasa de falla (no COMPLETED) | 0,3% | 0,4% |

**Altas (leading indicator del volumen):**

- **Cuentas de Wallet:** 30.652 en la semana (media 8 semanas 31.630; +1,9% WoW). Top: BSF 10.276 (33,5%) ·
  CENCOSUD 6.880 (22,4%) · Credicuotas 5.980 (19,5%) · Global 66 3.291 (10,7%) · Coppel 1.249 (4,1%). Deriva
  estructural de 13 semanas: +35,8% (30.710 vs. 22.613) — ver hallazgo 4.
- **Comercios de Adquirencia:** 180 en la semana (ver hallazgo 2). Top: La Virginia 161 (89,4%) · Demo Bind
  PSP 3 · BIND PSP 2 · PMC 2 · BIND PAGO QA 2.

**Top clientes NSM #1 (Operaciones/Wallet):** BSF $142.518 M (62,9%, ver hallazgo 5) · Sociedad Militar
$29.826 M (13,2%) · Global 66 $19.137 M (8,4%) · CENCOSUD $17.662 M (7,8%) · Credicuotas $8.832 M (3,9%) ·
Depay $2.259 M (1,0%) · Terra Blockchain $2.052 M (0,9%) · GALLO $1.264 M (0,6%).

**Top entidades NSM #2:** EDESA $3.333 M (22,7%) · EDEA $3.149 M (21,4%) · EDEN $2.571 M (17,5%) · EDELAP
$2.283 M (15,5%) · EDES $1.287 M (8,8%) · FAVACARD $532 M (3,6%) · RIPSA $456 M (3,1%) · Tarjeta Sucredito
$268 M (1,8%).

---

*Próxima corrida: semana 202633 (10 → 17 de agosto de 2026).*

---

## Semana 202631 · 27 de julio → 3 de agosto de 2026

*Reportado el 2026-08-04. 48 semanas cerradas en el store (202536 → 202631). **Cambio de estructura del
reporte (usuario, 2026-08-04):** a partir de esta semana, cada palanca del árbol de oportunidades recibe el
mismo tratamiento que las dos NSM — WoW y MoM, con el valor de comparación anterior explícito — en la nueva
sección 1d. En el email ejecutivo esto reemplaza a las grillas 1a/1b (quedaban redundantes con las cards
nuevas); acá en la wiki se mantienen las tablas 1a/1b como venían, más la tabla nueva de palancas, como
registro histórico completo. Esta corrida además corrigió el `DECLARE @FechaFin` de las 5 queries de hechos
(ver `../../2_areas/gaps_y_preguntas.md` y `decisiones.md` del mismo día) — la ventana de esta semana llegó exacta, sin
desalineación ISO.*

### 1 · Estado de las NSM

#### 1a · Detalle semanal (WoW) — KPI principal

| | **NSM #1 — Volumen API BANK** *(oficial: Wallet + Agente de Cobros)* | **NSM #2 — Volumen Payway** |
|---|---|---|
| **Volumen de la semana** | **$239.619 M** | **$8.190 M** |
| Operaciones / transacciones | 1.379.727 | 75.625 |
| Ticket promedio | $173.671 | $108.304 |
| WoW | **+37,1%** | **+7,7%** |
| vs. promedio 4 semanas | −10,5% | −8,4% |
| vs. baseline 13 semanas | +4,3% *(baseline $229.763 M)* | **+52,0%** *(baseline $5.388 M)* |
| vs. máximo histórico | −42,9% *(máx $419.802 M, sem. 202610)* | −22,6% *(máx $10.579 M, sem. 202629)* |
| Tendencia 6 semanas | −0,4% por semana | +4,5% por semana |
| z-score vs. 8 previas | −0,08 | +0,53 |

#### 1b · Vista mensual (MoM) — contexto adicional

Julio 2026 ya tiene 5 semanas ISO (202627-202631), pero el tramo de comparación sigue capado a 4
(simplificación "1 mes = 4 semanas", ver SKILL.md) — por eso el acumulado y el MoM de esta tabla salen
**idénticos** a los del reporte de la semana pasada: la 5ª semana de julio no se suma al tramo. No es un
error, es el recorte esperado.

| | **NSM #1 — Volumen API BANK** *(oficial)* | **NSM #2 — Volumen Payway** |
|---|---|---|
| **Mes actual** | Julio 2026 *(tramo de 4 semanas, capado)* | Julio 2026 *(tramo de 4 semanas, capado)* |
| Acumulado a la fecha (tramo) | $1.070.467 M | $35.772 M |
| MoM (4 sem. vs. mismas 4 sem. de junio) | **+21,0%** *(junio: $884.400 M)* | **+71,6%** *(junio: $20.850 M)* |
| vs. baseline 3 meses (mismo tramo) | +22,2% *(baseline $876.043 M)* | **+149,7%** *(baseline $14.327 M)* |
| vs. máximo histórico (mismo tramo) | −26,3% *(máx $1.451.705 M, marzo 2026)* | **+71,6%** *(máx $20.850 M, junio 2026)* |
| Objetivo | **PENDIENTE** — sin volumen mensual de mercado | **PENDIENTE** — sin volumen mensual de mercado |

*Serie mensual completa (mes completo vs. mes completo) desde sep-2025 en el anexo (sección 4). Julio 2026
mes completo (incluida la 5ª semana): NSM#1 $1.310.086 M (+48,1% vs. junio) · NSM#2 $43.962 M (+110,9%).*

#### 1c · Composición de NSM#1 — Operaciones (Wallet) vs. Transferencias Agente de Cobros

| | Volumen | Share | WoW |
|---|---|---|---|
| Operaciones (Wallet) | $182.425 M | 76,1% | **+72,9%** |
| Transferencias Agente de Cobros | $57.193 M | 23,9% | −17,5% |

**Desglose NSM #1 — IN / OUT (total oficial):**

| | Volumen | Share | WoW | Tendencia 6s |
|---|---|---|---|---|
| **OUT** | $135.936 M | 56,7% | +17,3% | +0,7% |
| **IN** | $103.683 M | 43,3% | **+76,1%** | −2,1% |

Por tipo (Operaciones/Wallet): Transferencia Entrante $94.673 M (51,9% de Wallet, WoW +86,8%) · Transferencia
Saliente $84.444 M (46,3%, WoW +64,2%) · Pago con QR $3.294 M (1,8%) · Debin Recurrente $14,9 M (+131,0%) ·
**Transf. Pull Crédito y Débito en $0** (sigue el postmortem de marzo 2026).

Por tipo (Agente de Cobros — ya sumado arriba): Saliente $48.198 M (84,3% de TAC, WoW −21,1%) · Entrante CVU
$8.968 M (15,7%) · Entrante CBU $27,1 M (0,0%, WoW −70,5%).

Top 8 collectors (TAC): Bind PSP liquidaciones cta 14 $13.648 M (23,9%) · Bind PSP liquidaciones cta 2
$11.029 M (19,3%) · Banelsip $8.213 M (14,4%) · BindPSP pagos Cencosud $5.364 M (9,4%) · Tienda Nube
$4.207 M (7,4%) · Credicuotas $2.282 M (4,0%) · Cucuru $1.734 M (3,0%) · Jugadon San Luis $810 M (1,4%).
Las dos cuentas de Administración (cta 14/cta 2) siguen siendo las más grandes de TAC (43,2% combinado) —
patrón ya resuelto (ver hallazgo 2 del reporte 202630), no es un cliente.

**Desglose NSM #2 — canal y medio de pago:**

| | Volumen | Share | WoW |
|---|---|---|---|
| Botón Simple | $7.907 M | 96,5% | +8,1% |
| Botón 2.0 | $283 M | 3,5% | −1,2% |
| Tarjeta de Débito | $4.720 M | 57,6% | +1,9% |
| Tarjeta de Crédito | $3.458 M | 42,2% | +16,9% |
| Tarjeta Prepaga | $11,9 M | 0,1% | +2,9% |

#### 1d · Palancas — cada una atada a su NSM (WoW + MoM, mismo tratamiento que las NSM)

**Novedad de esta semana (usuario, 2026-08-04):** primera corrida con el registro unificado de palancas —
cada rama del árbol de oportunidades de las NSM lleva ahora WoW y MoM, con el valor de comparación anterior
explícito en las dos, igual que las NSM. Reemplaza a las líneas de texto sueltas (solo volumen + WoW) que
tenían las palancas indirectas y fuera de Payway hasta la semana pasada.

**NSM#1:**

| Palanca | Categoría | Volumen | % del padre | WoW | Semana ant. | MoM | Tramo ant. |
|---|---|---:|---:|---:|---:|---:|---:|
| Operaciones (Wallet) | Componente de NSM#1 | $182.425 M | 76,1% | +72,9% | $105.479 M | +22,6% | $548.736 M |
| OUT | Entrante / Saliente | $135.936 M | 56,7% | +17,3% | $115.885 M | +21,6% | $565.616 M |
| IN | Entrante / Saliente | $103.683 M | 43,3% | +76,1% | $58.886 M | +20,1% | $318.785 M |
| Transferencia Entrante | Tipo de operación (Wallet) | $94.673 M | 51,9% | +86,8% | $50.693 M | +21,3% | $275.177 M |
| Transferencia Saliente | Tipo de operación (Wallet) | $84.444 M | 46,3% | +64,2% | $51.442 M | +24,4% | $261.608 M |
| Transferencias Agente de Cobros | Componente de NSM#1 | $57.193 M | 23,9% | −17,5% | $69.292 M | +18,5% | $335.665 M |
| Saliente (Agente de Cobro) | Tipo (Agente de Cobros) | $48.198 M | 84,3% | −21,1% | $61.105 M | +19,4% | $292.072 M |
| Saliente | Entrante / Saliente (TAC) | $48.198 M | 84,3% | −21,1% | $61.105 M | +19,4% | $292.072 M |
| Entrante | Entrante / Saliente (TAC) | $8.995 M | 15,7% | +9,9% | $8.187 M | +12,4% | $43.593 M |
| Entrante CVU | Tipo (Agente de Cobros) | $8.968 M | 15,7% | +10,8% | $8.095 M | +12,9% | $43.199 M |
| Pago con QR | Tipo de operación (Wallet) | $3.294 M | 1,8% | −1,3% | $3.338 M | +13,3% | $11.935 M |
| Entrante CBU | Tipo (Agente de Cobros) | $27,1 M | 0,0% | −70,5% | $91,9 M | −45,3% | $393 M |
| Debin Recurrente Crédito | Tipo de operación (Wallet) | $14,9 M | 0,0% | +131,0% | $6,5 M | +147,2% | $15,6 M |
| Transf. Pull Crédito | Tipo de operación (Wallet) | $0,00 M | 0,0% | s/d | $0,00 M | s/d | $0,00 M |
| Transf. Pull Débito | Tipo de operación (Wallet) | $0,00 M | 0,0% | s/d | $0,00 M | s/d | $0,00 M |
| *Transf. interna saliente* | *Palanca indirecta* | *$6.349 M* | *2,6%* | *−63,4%* | *$17.332 M* | *+3,3%* | *$64.994 M* |
| *Transf. interna entrante* | *Palanca indirecta* | *$6.349 M* | *2,6%* | *−63,4%* | *$17.332 M* | *+3,3%* | *$64.994 M* |
| *Viaje QR* | *Palanca indirecta* | *$39,6 M* | *0,0%* | *−1,3%* | *$40,2 M* | *−17,9%* | *$209 M* |
| *Compra Dólar CCL* | *Palanca indirecta* | *$0,03 M* | *0,0%* | *−0,5%* | *$0,03 M* | *+1781,7%* | *$0,28 M* |
| *Ingreso con tarjeta* | *Palanca indirecta* | *$0,00 M* | *0,0%* | *s/d* | *$0,00 M* | *s/d* | *$0,00 M* |
| *Venta Dólar CCL* | *Palanca indirecta* | *$0,00 M* | *0,0%* | *+815,8%* | *$0,00 M* | *−19,7%* | *$0,00 M* |

*(en cursiva: palancas de contexto, no suman al total de NSM#1)*

**NSM#2:**

| Palanca | Categoría | Volumen | % del padre | WoW | Semana ant. | MoM | Tramo ant. |
|---|---|---:|---:|---:|---:|---:|---:|
| Botón Simple | Canal (Payway) | $7.907 M | 96,5% | +8,1% | $7.316 M | +77,3% | $19.029 M |
| Tarjeta de Débito | Medio de pago (Payway) | $4.720 M | 57,6% | +1,9% | $4.634 M | +75,8% | $13.218 M |
| Tarjeta de Crédito | Medio de pago (Payway) | $3.458 M | 42,2% | +16,9% | $2.957 M | +64,1% | $7.604 M |
| Botón 2.0 | Canal (Payway) | $283 M | 3,5% | −1,2% | $287 M | +12,1% | $1.820 M |
| Tarjeta Prepaga | Medio de pago (Payway) | $11,9 M | 0,1% | +2,9% | $11,6 M | +113,5% | $26,8 M |
| Tarjeta de Crédito Cuotas | Medio de pago (Payway) | $0,00 M | 0,0% | s/d | $0,00 M | s/d | $0,00 M |
| *Transferencia 3.0* | *Fuera de Payway* | *$12.189 M* | *148,8%* | *+0,8%* | *$12.097 M* | *+12,7%* | *$59.685 M* |
| *Liquidador* | *Fuera de Payway* | *$8.435 M* | *103,0%* | *−35,8%* | *$13.140 M* | *+12,2%* | *$62.930 M* |
| *Transf. Entrante CVU* | *Fuera de Payway* | *$7.699 M* | *94,0%* | *−3,6%* | *$7.990 M* | *+11,9%* | *$42.561 M* |
| *MPOS / POS* | *Fuera de Payway* | *$883 M* | *10,8%* | *−4,9%* | *$929 M* | *+6,3%* | *$4.844 M* |
| *EcoCerrado* | *Fuera de Payway* | *$0,00 M* | *0,0%* | *+30,8%* | *$0,00 M* | *s/d* | *$0,00 M* |

*(en cursiva: palancas de contexto, fuera del scope de NSM#2 hoy)*

---

### 2 · Hallazgos y puntos más importantes de la semana

#### 🔴 1. NSM#1 se recupera +37,1% WoW — vuelve a estar en línea con el baseline, no es un quiebre de tendencia.

La semana pasada (202630) NSM#1 había caído −41,3%. Esta semana recuperó +37,1% y quedó en $239.619 M,
apenas +4,3% sobre el baseline de 13 semanas ($229.763 M) y con tendencia de 6 semanas casi plana (−0,4%
por semana; z-score −0,08, dentro de lo habitual).
**Por qué importa:** leídas juntas, las dos últimas semanas no cuentan una historia de crecimiento ni de
caída — el negocio volvió al rango en el que venía operando. **Qué hacer:** en el email a gerencia, mostrar
el WoW junto al vs. baseline 13 semanas para que no se lea como una recuperación mayor a lo que es.

#### 🔴 2. BSF sigue concentrando el 63,2% del volumen de Wallet — riesgo de dependencia conocido, no nuevo.

BSF explica $115.228 M de los $182.425 M de Operaciones/Wallet de la semana (63,2%), y el top-3 (BSF +
Sociedad Militar + Global 66) llega a 85,6%. Es uno de los 5 clientes que históricamente concentran la
mayor parte del volumen (BSF, Credicuotas, CENCOSUD, Sociedad Militar, Global 66).
**Por qué importa:** el patrón no es nuevo, pero sigue siendo el riesgo de concentración más grande de la
NSM — mientras la cartera no se diversifique, la volatilidad semanal de NSM#1 va a seguir alta.

#### 🟡 3. Las altas de comercios saltan +238,2% — pero 91% del salto son 2 clientes nuevos sin contexto todavía.

115 altas de comercios en la semana vs. una mediana de 8 semanas de 34 (el z-score no lo marca porque un
pico previo en la ventana infla el desvío). "La Virginia" (70 altas, 61%) y "Consorcio Abierto" (35, 30%)
explican casi todo el salto. No tenemos contexto todavía sobre ninguno de los dos.
**Qué hacer:** confirmar con Comercial si es una alta legítima en lote (ej. una cadena sumando sucursales)
o carga de datos/testing antes de leerlo como una señal de crecimiento real.

#### 🟡 4. El balance IN/OUT de NSM#1 se movió por el salto de Transferencia Entrante (+86,8% WoW).

El OUT pasó a ser 56,7% del volumen oficial (venía de 66,3% la semana pasada) porque IN creció +76,1% WoW,
impulsado por Transferencia Entrante ($94.673 M, +86,8%) más que por Transferencia Saliente (+64,2%).
**Qué mirar:** si el mix se sostiene la semana que viene o si fue una semana atípica — con una sola
observación no alcanza para llamarlo cambio de tendencia.

#### 🟢 5. Terra Blockchain y Sucredito caen fuerte sin explicación conocida.

Terra Blockchain (Wallet) cayó −75,7% vs. su promedio de 4 semanas ($12.854 M → $3.125 M) y Tarjeta
Sucredito (NSM#2) cayó −70,9% ($191 M → $55,4 M). Ninguna de las dos caídas tiene una explicación de
negocio conocida todavía.
**Qué hacer:** confirmar con Soporte/Comercial que ambos clientes siguen activos.

---

### 3 · Anexo — Métricas de soporte

**Serie mensual completa (desde sep-2025) — volumen total del mes, para ver la magnitud absoluta.**

| Mes | NSM #1 *(oficial)* | MoM (mes completo) | NSM #2 | MoM (mes completo) |
|---|---|---|---|---|
| 2025-09 | $476.139 M | s/d | $4.172 M | s/d |
| 2025-10 | $730.477 M | +53,4% | $5.042 M | +20,8% |
| 2025-11 | $625.391 M | −14,4% | $4.401 M | −12,7% |
| 2025-12 | $813.380 M | +30,1% | $4.640 M | +5,4% |
| 2026-01 | $1.546.504 M | +90,1% | $5.211 M | +12,3% |
| 2026-02 | $1.323.010 M | −14,5% | $6.268 M | +20,3% |
| 2026-03 | $1.451.705 M | +9,7% | $9.611 M | +53,3% |
| 2026-04 | $1.069.065 M | −26,4% | $12.021 M | +25,1% |
| 2026-05 | $853.360 M | −20,2% | $11.768 M | −2,1% |
| 2026-06 | $884.400 M | +3,6% | $20.850 M | +77,2% |
| 2026-07 | **$1.310.086 M** | +48,1% | **$43.962 M** | +110,9% |

**Salud (no suman al volumen NSM):**

| Métrica | Semana | Media 8 semanas |
|---|---|---|
| NSM #1 — tasa de rechazo | 0,9% | 0,9% |
| NSM #1 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 — tasa de rechazo | 22,4% | 22,6% |
| NSM #2 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 / Crédito — rechazo | 30,5% | 31,6% |
| NSM #2 / Débito — rechazo | 16,9% | 17,5% |
| NSM #2 / Prepaga — rechazo | 27,7% | 36,0% |
| TAC Agente de Cobros — tasa de falla (no COMPLETED) | 0,2% | 0,4% |

**Altas (leading indicator del volumen):**

- **Cuentas de Wallet:** 30.075 en la semana (media 8 semanas 31.010; +0,5% WoW). Top: BSF 8.609 (28,6%) ·
  Credicuotas 7.720 (25,7%) · CENCOSUD 5.944 (19,8%) · Global 66 3.406 (11,3%) · Coppel 1.465 (4,9%). Deriva
  estructural de 13 semanas: +74,4% (39.153 vs. 22.445) — cambio estructural positivo, no ruido semanal.
- **Comercios de Adquirencia:** 115 en la semana (ver hallazgo 3). Top: La Virginia 70 · Consorcio Abierto
  35 · Demo Bind PSP 5 · POSBerry 1 · RIPSA 1.

**Top clientes NSM #1 (Operaciones/Wallet):** BSF $115.228 M (63,2%) · Sociedad Militar $26.456 M (14,5%) ·
Global 66 $14.469 M (7,9%) · CENCOSUD $12.691 M (7,0%) · Credicuotas $5.094 M (2,8%) · Terra Blockchain
$3.125 M (1,7%, ver hallazgo 5) · Depay $2.075 M (1,1%) · GALLO $1.006 M (0,6%).

**Top entidades NSM #2:** EDEA $2.043 M (24,9%) · EDESA $1.640 M (20,0%) · EDEN $1.600 M (19,5%) · EDELAP
$1.429 M (17,4%) · EDES $676 M (8,3%) · RIPSA $299 M (3,7%) · FAVACARD $230 M (2,8%) · Tarjeta Sucredito
$55,4 M (0,7%, ver hallazgo 5).

*Nota: las palancas indirectas de NSM#1 y la Adquirencia fuera de Payway ahora tienen su detalle completo
(volumen, WoW y MoM) en la sección 1d — este anexo ya no las repite en formato de bullets.*

---

*Próxima corrida: semana 202632 (3 → 10 de agosto de 2026).*

---

## Semana 202630 · 20 → 27 de julio de 2026

*Reportado el 2026-07-27. Semana 202630 pasa de parcial (ingerida el 2026-07-23 con ~3 días, sin `comercios`)
a completa con el export full de las 5 fuentes. 47 semanas cerradas en el store (202536 → 202630).*

### 1 · Estado de las NSM

#### 1a · Detalle semanal (WoW) — KPI principal

| | **NSM #1 — Volumen API BANK** *(oficial: Wallet + Agente de Cobros)* | **NSM #2 — Volumen Payway** |
|---|---|---|
| **Volumen de la semana** | **$174.771 M** | **$7.603 M** |
| Operaciones / transacciones | 1.305.406 | 70.670 |
| Ticket promedio | $133.883 | $107.582 |
| WoW | **−41,3%** | **−28,1%** |
| vs. promedio 4 semanas | −34,0% | −8,6% |
| vs. baseline 13 semanas | −22,9% *(baseline $226.624 M)* | **+53,7%** *(baseline $4.948 M)* |
| vs. máximo histórico | −58,4% *(máx $419.802 M, sem. 202610)* | −28,1% *(máx $10.579 M, sem. 202629 — máximo de la serie)* |
| Tendencia 6 semanas | +5,0% por semana | +13,1% por semana |
| z-score vs. 8 previas | −1,07 | +0,45 |

#### 1b · Vista mensual (MoM) — contexto adicional

Julio 2026 ya lleva sus 4 semanas cerradas (202627-202630) — primer mes de la serie que se compara tramo
completo contra tramo completo desde que arrancó el reporte.

| | **NSM #1 — Volumen API BANK** *(oficial)* | **NSM #2 — Volumen Payway** |
|---|---|---|
| **Mes actual** | Julio 2026 *(4 de 4 semanas)* | Julio 2026 *(4 de 4 semanas)* |
| Acumulado a la fecha | $1.070.467 M | $35.772 M |
| MoM (4 sem. vs. mismas 4 sem. de junio) | **+21,0%** *(junio: $884.400 M)* | **+71,6%** *(junio: $20.850 M)* |
| vs. baseline 3 meses (mismo tramo) | +22,2% *(baseline $876.043 M)* | **+149,7%** *(baseline $14.327 M)* |
| vs. máximo histórico (mismo tramo) | −26,3% *(máx $1.451.705 M, marzo 2026)* | **+71,6%** *(máx $20.850 M, junio 2026 — máximo del tramo)* |
| Objetivo | **PENDIENTE** — sin volumen mensual de mercado | **PENDIENTE** — sin volumen mensual de mercado |

*Serie mensual completa (mes completo vs. mes completo) desde sep-2025 en el anexo (sección 3).*

#### 1c · Composición de NSM#1 — Operaciones (Wallet) vs. Transferencias Agente de Cobros

| | Volumen | Share | WoW |
|---|---|---|---|
| Operaciones (Wallet) | $105.479 M | 60,4% | −28,4% |
| Transferencias Agente de Cobros | $69.292 M | 39,6% | **−53,9%** |

**Desglose NSM #1 — IN / OUT (total oficial):**

| | Volumen | Share | WoW | Tendencia 6s |
|---|---|---|---|---|
| **OUT** | $115.885 M | 66,3% | −47,7% | +7,8% |
| **IN** | $58.886 M | 33,7% | −22,4% | −0,1% |

Por tipo (Operaciones/Wallet): Transferencia Saliente $51.442 M (48,8% de Wallet) · Transferencia Entrante
$50.693 M (48,1%) · Pago con QR $3.338 M (3,2%) · Debin Recurrente $6,5 M ·
**Transf. Pull Crédito y Débito en $0** (sigue el postmortem de marzo 2026).

Por tipo (Agente de Cobros — ya sumado arriba): Saliente $61.105 M (88,2% de TAC, WoW −56,3%) · Entrante CVU
$8.095 M (11,7%) · Entrante CBU $91,9 M (0,1%).

Top 8 collectors (TAC): Bind PSP liquidaciones cta 14 $21.276 M (30,7%) · Banelsip $12.786 M (18,5%) ·
Bind PSP liquidaciones cta 2 $11.106 M (16,0%) · BindPSP pagos Cencosud $4.893 M (7,1%) ·
Tienda Nube $4.030 M (5,8%) · Cucuru $1.823 M (2,6%) · Credicuotas $1.533 M (2,2%) · Travel Rock $1.056 M
(1,5%). **Ver hallazgo 2: cta 14 y cta 2 son la misma CUIT que Bind PSP SA — 46,7% de TAC no es un cliente.**

**Desglose NSM #2 — canal y medio de pago:**

| | Volumen | Share | WoW |
|---|---|---|---|
| Botón Simple | $7.316 M | 96,2% | −26,1% |
| Botón 2.0 | $287 M | 3,8% | −57,6% |
| Tarjeta de Débito | $4.634 M | 61,0% | −31,4% |
| Tarjeta de Crédito | $2.957 M | 38,9% | −22,5% |
| Tarjeta Prepaga | $11,6 M | 0,2% | −14,3% |

---

### 2 · Hallazgos y puntos más importantes de la semana

#### 🔴 1. La caída semanal de ambas NSM es mayormente reversión de una semana previa atípicamente alta — no un quiebre de tendencia.

El WoW aislado asusta: NSM#1 −41,3%, NSM#2 −28,1%, TAC −53,9%. Pero la semana anterior (202629) fue ella
misma un pico — NSM#2 cerró en **máximo histórico** ($10.579 M) y TAC venía de un cambio de nivel real
(hallazgo 9 del reporte anterior, z=+2,94). Mirado contra ventanas más largas, la caída es mucho más chica:
NSM#1 vs. 4 semanas −34,0%, vs. baseline 13 semanas −22,9% (z-score apenas −1,07, no atípico); NSM#2 vs. 4
semanas solo −8,6% y **sigue +53,7% arriba del baseline de 13 semanas**. La tendencia de 6 semanas de ambas
sigue positiva (+5,0%/sem NSM#1, +13,1%/sem NSM#2).

**Por qué importa:** leído solo el WoW, parece que el negocio se desplomó. El resto de los indicadores dice
"vuelta a la media después de una semana rara", no un cambio estructural. La concentración de siempre sigue
igual de fondo — BSF 53,8% de Wallet (top-3 74,4%) — así que la volatilidad semanal seguirá siendo alta
mientras la cartera no se diversifique (ver hallazgo 2 del reporte de la semana 202629).
**Qué hacer:** en el email a gerencia, acompañar el número del WoW con la lectura de 4/13 semanas para que
no se lea como una caída del negocio.

#### 🔴 2. *(Resuelto 2026-07-27)* Los dos collectors más grandes de la palanca TAC ("Bind PSP liquidaciones cta 14" y "cta 2") son cuentas del propio Bind PSP, no de un cliente — y explican gran parte de la volatilidad semanal de NSM#1.

> **Actualización 2026-07-27:** el usuario confirmó que son cuentas creadas por el equipo de **Administración**
> para transferencias de pagos — **cuentan como volumen normal hacia las NSM**, no se separan del resto de
> TAC en el reporte (decisión registrada en `decisiones.md`). El resto de este hallazgo describe el hecho
> tal como se detectó y sigue siendo útil para entender la volatilidad semanal, pero la pregunta de scope
> queda cerrada: no es un riesgo de concentración de cartera, es el patrón normal de operación de
> Administración. El refresh de `Collectors` pedido en el gap asociado también llegó: `CollectorId 158/159`
> (warning separado, hallazgo 5) son dos cuentas más del mismo patrón — "cta 83" y "cta 120".

Cruzando `dim_collectors` contra el CUIT de Bind PSP (30717449076): **"Bind PSP liquidaciones cta 14"
(30,7% de TAC), "Bind PSP liquidaciones cta 2" (16,0%) y "Bind PSP SA" comparten esa misma CUIT** — juntas,
**46,7% del volumen de TAC de esta semana no es un cliente externo, es tesorería/liquidación interna de la
propia empresa**. Esta semana esas cuentas cayeron fuerte (cta 14 −65,4%, cta 2 −34,8%; la semana pasada
además cta 39 −90,0%, cta 25 −92,7%, cta 137 −74,9% y Bind PSP SA −89,8% salieron del top-8 tras haber sido
grandes en 202629) — el mismo grupo de cuentas que la semana pasada explicó buena parte del salto +50,3% de
TAC.

**Por qué importa:** el hallazgo 9 del reporte anterior ya marcó que cta 14 es el collector más concentrado
de TAC "mismo patrón de riesgo de dependencia de un solo collector que BSF" — pero si es una cuenta interna,
la lectura correcta es otra: no es dependencia comercial de un cliente, es la cadencia de liquidación/
tesorería propia de Bind PSP, probablemente por lotes y no diaria, lo que explicaría buena parte del "ruido"
semana a semana de NSM#1 sin ser ni señal de negocio de un cliente ni riesgo real de cartera.
**Qué hacer:** preguntarle a Finanzas/Tesorería qué son estas cuentas y con qué cadencia liquidan; evaluar
si el reporte debería separar "TAC-clientes reales" de "TAC-interno" para no mezclar ambas lecturas. Ver
pregunta registrada en `../../2_areas/gaps_y_preguntas.md`.

#### 🟡 3. Cucuru YPF casi desaparece de TAC: −99,4% ($190 M → $1,1 M).

Chico en peso (0,2% de TAC) pero la caída es casi total y abrupta, y a diferencia de Octagon (hallazgo 6 del
reporte anterior, cuya salida ya estaba anticipada por la cronología del cliente) **no hay ningún evento
conocido en la wiki que lo explique**.
**Por qué importa:** vale un chequeo rápido con Comercial antes de asumir que es estacional o un corte
puntual del cliente.

#### 🟡 4. Primera señal de repunte en altas de comercios de Adquirencia — aunque la deriva estructural de T-041 sigue vigente.

51 altas esta semana, muy por encima del promedio de 4 semanas (33, +54,5%) y de la mediana de 8 semanas (34,
+50,0%) — el salto más alto en varias semanas. Pero el promedio de 4 semanas (33) sigue muy por debajo del
nivel de hace 13 semanas (74, −55,2%), la deriva estructural que ya trackea T-041. Casi todo el salto de esta
semana es **Consorcio Abierto** (34 altas, 66,7% del total) más La Virginia (10). Incluye 2 altas de una
entidad nueva (**#509, sin nombre — dimensión Entidad desactualizada**, ver gap abajo).
**Por qué importa:** un dato no revierte una tendencia de 3 meses, pero es la primera semana reciente donde
las altas superan claramente la mediana. Vale seguirlo la próxima corrida antes de descartarlo como ruido —
no cierra T-041, la aporta como dato a favor de que puede ser algo puntual y no solo estructural.

#### 🟡 5. *(Resuelto 2026-07-27)* Dos de los tres warnings de dimensión de esta corrida son nuevos y afectan al reporte.

`EntidadId 509` (comercios, 2 altas) y `CollectorId 158/159` (transferencias TAC, $10 y $698 respectivamente
— marginal en volumen) no tienen fila en las dimensiones de referencia. Los otros dos warnings de la corrida
(`FormadePago=70` y `Type=NULL` en TAC) ya estaban trackeados desde semanas anteriores, no son nuevos.
**Qué hacer:** ver pregunta puntual en `../../2_areas/gaps_y_preguntas.md` — pedir el refresh de `Entidad` y `Collectors`.

> **Actualización 2026-07-27:** el usuario pasó el refresh de ambas tablas. `EntidadId 509` = **PRISMA**.
> `CollectorId 158/159` = "Bind PSP liquidaciones cta 83" y "cta 120" — dos cuentas más del mismo patrón del
> hallazgo 2 (Administración, misma CUIT de Bind PSP). Además: `FormadePago = 70` = **Eco Cerrado** (agregado
> a `DIM_FORMA_PAGO` en `pipeline.py`, deja de marcarse como warning — consistente con `TipoTransaccion = 3`,
> que ya se llama "EcoCerrado" en la dimensión de tipo de transacción: las mismas filas caen en ambos
> códigos); `Type = NULL` en TAC quedó en manos de **Nicolás Colón**, que lo está revisando como posible bug
> — sin novedad propia hasta que él reporte algo.
>
> **Dato adicional — Eco Cerrado no es nuevo, pero creció fuerte esta semana:** ya existía desde 202629
> (entidad A130, $24 en 2 operaciones), pero en 202630 pasó a **$1.819** (×76) — $117 `ACREDITADO` y
> **$1.702 `DEVUELTA`, 93,6% de devolución**. Es marginal en volumen absoluto (no cruza el piso de
> materialidad ni afecta a NSM#2, que ya excluye `TipoTransaccion = 3` de su scope), pero la tasa de
> devolución tan alta en una entidad que recién empieza a operar este medio es una señal a seguir la semana
> que viene — si el volumen sigue creciendo y la devolución se mantiene arriba del 90%, ahí sí cruzaría el
> piso de materialidad como hallazgo de calidad.

---

### 3 · Anexo — Métricas de soporte

**Serie mensual completa (desde sep-2025) — volumen total del mes, para ver la magnitud absoluta.**

| Mes | NSM #1 *(oficial)* | MoM (mes completo) | NSM #2 | MoM (mes completo) |
|---|---|---|---|---|
| 2025-09 | $476.139 M | s/d | $4.172 M | s/d |
| 2025-10 | $730.477 M | +53,4% | $5.042 M | +20,8% |
| 2025-11 | $625.391 M | −14,4% | $4.401 M | −12,7% |
| 2025-12 | $813.380 M | +30,1% | $4.640 M | +5,4% |
| 2026-01 | $1.546.504 M | +90,1% | $5.211 M | +12,3% |
| 2026-02 | $1.323.010 M | −14,5% | $6.268 M | +20,3% |
| 2026-03 | $1.451.705 M | +9,7% | $9.611 M | +53,3% |
| 2026-04 | $1.069.065 M | −26,4% | $12.021 M | +25,1% |
| 2026-05 | $853.360 M | −20,2% | $11.768 M | −2,1% |
| 2026-06 | $884.400 M | +3,6% | $20.850 M | +77,2% |
| 2026-07 | **$1.070.467 M** | +21,0% | **$35.772 M** | +71,6% |

**Salud (no suman al volumen NSM):**

| Métrica | Semana | Media 8 semanas |
|---|---|---|
| NSM #1 — tasa de rechazo | 1,7% | 0,8% |
| NSM #1 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 — tasa de rechazo | 22,9% | 22,4% |
| NSM #2 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 / Crédito — rechazo | 31,9% | 31,2% |
| NSM #2 / Débito — rechazo | 17,2% | 17,4% |
| NSM #2 / Prepaga — rechazo | 23,5% | 38,9% |
| TAC Agente de Cobros — tasa de falla (no COMPLETED) | 0,5% | 0,4% |

**Altas (leading indicator del volumen):**

- **Cuentas de Wallet:** 29.920 en la semana (media 8 semanas 29.696; −7,1% WoW). Top: Credicuotas 11.232
  (37,5%) · BSF 7.781 (26,0%) · CENCOSUD 5.266 (17,6%) · Global 66 2.498 (8,3%) · COTO 796 (2,7%). Sociedad
  Militar sale del top-5 esta semana — el alta masiva de las últimas dos semanas (T-043) parece haber
  terminado.
- **Comercios de Adquirencia:** 51 en la semana (ver hallazgo 4). Top: Consorcio Abierto 34 · La Virginia 10
  · entidad #509 2 · POSBerry 1 · RIPSA 1.

**Top clientes NSM #1 (Operaciones/Wallet):** BSF $56.716 M (53,8%) · Sociedad Militar $11.544 M (10,9%) ·
Global 66 $10.233 M (9,7%) · Terra Blockchain $9.911 M (9,4%) · CENCOSUD $8.199 M (7,8%) · Credicuotas
$3.486 M (3,3%) · Depay $2.081 M (2,0%) · GALLO $747 M (0,7%).

**Top entidades NSM #2:** EDEA $1.754 M (23,1%) · EDESA $1.552 M (20,4%) · EDEN $1.532 M (20,1%) · EDELAP
$1.328 M (17,5%) · EDES $704 M (9,3%, +119,2% WoW) · FAVACARD $236 M (3,1%) · RIPSA $201 M (2,6%) · Tarjeta
Sucredito $86,5 M (1,1%). El grupo DESA + RIPSA sigue concentrando ~90% de NSM#2 (ver hallazgo 3 del reporte
de la semana 202629).

**Palancas indirectas de la NSM #1** (no suman, alimentan el saldo que después opera): transferencias
internas $17.332 M por pata · Viaje QR $40,2 M · dólar CCL en volúmenes marginales.

**Adquirencia fuera de Payway** (contexto): Liquidador $13.140 M (−58,3%) · Transferencia 3.0 $12.097 M
(−21,1%) · Transf. Entrante CVU $7.990 M (−47,4%) · **MPOS / POS presente $929 M** (−43,4%) — cuando el
proyecto de POS por Payway se shippee, ese volumen pasa a sumar a la NSM #2.

---

*Próxima corrida: semana 202631 (27 de julio → 3 de agosto de 2026).*

---

## Semana 202629 · 13 → 20 de julio de 2026

*Reportado el 2026-07-21; actualizado el 2026-07-22 (se agregó la vista mensual/MoM) y de nuevo el mismo día
(el WoW vuelve a ser el KPI principal, y el MoM pasa a medirse por el mismo tramo de semanas del mes anterior
en vez de mes completo contra mes completo). Primera corrida de la skill, con backfill de 46 semanas
(202536 → 202629). Historia disponible: 01-sep-2025 en adelante. La semana 202630 quedó excluida por estar
todavía abierta. Actualizado de nuevo el 2026-07-23: la palanca de transferencias del producto Agente de
Cobros y Pagos (entrantes CVU/CBU, salientes) se sumó al **total oficial de NSM#1**, decisión del usuario
("desde siempre y hacia adelante también") — no es un bloque aparte, es parte del número. Todos los valores
de NSM#1 de esta entrada (§1a, §1b, §1c, anexo) se recalcularon con la fusión; los de NSM#2 no cambiaron. Las
secciones que analizan solo la componente Operaciones/Wallet (top clientes, hallazgos 1 y 2) quedan
explícitamente marcadas como tales.*

### 1 · Estado de las NSM

#### 1a · Detalle semanal (WoW) — KPI principal

| | **NSM #1 — Volumen API BANK** *(oficial: Wallet + Agente de Cobros)* | **NSM #2 — Volumen Payway** |
|---|---|---|
| **Volumen de la semana** | **$297.488 M** | **$10.579 M** |
| Operaciones / transacciones | 1.444.653 | 96.857 |
| Ticket promedio | $205.924 | $109.227 |
| WoW | **+6,3%** | **+26,2%** |
| vs. promedio 4 semanas | +28,2% | +59,2% |
| vs. baseline 13 semanas | +36,8% *(baseline $217.516 M)* | **+144,7%** *(baseline $4.324 M)* |
| vs. máximo histórico | −29,1% *(máx $419.802 M, sem. 202610)* | **máximo histórico de la serie** |
| Tendencia 6 semanas | +8,2% por semana | +16,9% por semana |

#### 1b · Vista mensual (MoM) — contexto adicional

MoM siempre compara el **mismo tramo de semanas**: julio 2026 lleva 3 semanas cerradas (202627-202629), así
que se compara esa suma contra la suma de las **primeras 3 semanas** de junio (no contra junio completo).

| | **NSM #1 — Volumen API BANK** *(oficial)* | **NSM #2 — Volumen Payway** |
|---|---|---|
| **Mes actual** | Julio 2026 *(en curso, 3 de ~4 semanas)* | Julio 2026 *(en curso, 3 de ~4 semanas)* |
| Acumulado a la fecha | $895.696 M | $28.169 M |
| MoM (3 sem. vs. mismas 3 sem. de junio) | **+24,2%** *(junio: $721.074 M)* | **+79,0%** *(junio: $15.737 M)* |
| vs. baseline 3 meses (mismo tramo) | +23,8% *(baseline $723.324 M)* | **+155,0%** *(baseline $11.048 M)* |
| vs. máximo histórico (mismo tramo) | −23,3% *(máx $1.168.263 M, marzo 2026)* | **máximo histórico de la serie** |
| Objetivo | **PENDIENTE** — sin volumen mensual de mercado | **PENDIENTE** — sin volumen mensual de mercado |

*Serie mensual completa (mes completo vs. mes completo, para ver la magnitud absoluta) desde sep-2025 en el
anexo (sección 3).*

#### 1c · Composición de NSM#1 — Operaciones (Wallet) vs. Transferencias Agente de Cobros

No es una vista alternativa: es la apertura del mismo número oficial de §1a.

| | Volumen | Share | WoW |
|---|---|---|---|
| Operaciones (Wallet) | $147.326 M | 49,5% | −18,2% |
| Transferencias Agente de Cobros | **$150.162 M** | 50,5% | **+50,3%** |

La palanca de Agente de Cobros ya es **más grande que Operaciones de Wallet** en esta semana — ver
hallazgo 9.

**Desglose NSM #1 — IN / OUT (total oficial)**, con Pull Débito contado como OUT y la palanca TAC fusionada
(Saliente → OUT, Entrante CVU/CBU → IN):

| | Volumen | Share | WoW | Tendencia 6s |
|---|---|---|---|---|
| **OUT** | $221.624 M | 74,5% | +29,0% | +9,2% |
| **IN** | $75.864 M | 25,5% | −29,8% | +6,4% |

Por tipo (Operaciones/Wallet): Transferencia Saliente $78.013 M (53,0% de Wallet) · Transferencia Entrante
$65.664 M (44,6%) · Pago con QR $3.640 M (2,5%) · Debin Recurrente $9,4 M ·
**Transf. Pull Crédito y Débito en $0**.

Por tipo (Agente de Cobros — ya sumado arriba): Saliente $139.971 M (93,2% de TAC, WoW +70,6%) ·
Entrante CVU $10.133 M (6,7%) · Entrante CBU $57,8 M (0,04%) ·
**Sin clasificar (`Type=NULL`) $3,8 M** — suma al total oficial pero no se asigna a IN ni OUT (usuario,
2026-07-23: "debe ser un error... igualmente suma al volumen de API BANK", ver `../../2_areas/gaps_y_preguntas.md`).

Top 8 collectors (TAC): Bind PSP liquidaciones cta 14 $61.462 M (40,9%) · Banelsip $30.765 M (20,5%) ·
Bind PSP liquidaciones cta 2 $17.044 M (11,4%) · BindPSP pagos Cencosud $10.718 M (7,1%) ·
Tienda Nube $4.618 M (3,1%).

**Desglose NSM #2 — canal y medio de pago:**

| | Volumen | Share | WoW |
|---|---|---|---|
| Botón Simple | $9.903 M | 93,6% | +27,4% |
| Botón 2.0 | $676 M | 6,4% | +11,3% |
| Tarjeta de Débito | $6.751 M | 63,8% | +17,3% |
| Tarjeta de Crédito | $3.814 M | 36,1% | +46,1% |
| Tarjeta Prepaga | $13,5 M | 0,1% | −16,2% |

---

### 2 · Hallazgos y puntos más importantes de la semana

> Los hallazgos 1 y 2 analizan solo la componente **Operaciones de Wallet** de NSM#1 (calculados antes de
> fusionar la palanca de Agente de Cobros) — Astropay y BSF son clientes de esa tabla, no de Collectors. Las
> cifras narrativas de NSM#1 mensual/histórica de estos dos hallazgos siguen siendo las de Wallet-only y
> **no coinciden con la serie oficial fusionada de §1b/anexo**; ver hallazgo 9 para el impacto de la fusión.

#### 🔴 1. La "caída" de la NSM #1 (Operaciones/Wallet) desde su pico de enero es 100% la salida de Astropay — sin ese cliente, el negocio creció.

La vista mensual (nueva esta semana) muestra algo que la semanal no podía ver: la NSM #1 cayó de **$1.152.974 M
en enero de 2026 a $514.607 M en mayo** (−55,4%). Se ve como un problema estructural grave del North Star.
No lo es: **Astropay solo** hizo $707.985 M en enero (62% del total de ese mes) y colapsó a **$37,8 M en mayo**
— una caída de $707.947 M, **más grande que toda la caída neta de la NSM en el mismo período**. Calculando la
NSM #1 *ex-Astropay*: pasó de $444.990 M a $514.569 M — **creció +15,6%**.

Astropay dejó de ser cliente de Bind PSP en **marzo de 2026** por decisión del Grupo BIND (motivos de
compliance, ver [`empresa.md`](../../2_areas/overview_empresa/overview_empresa_general.md#contexto-actual-2026) y el
[postmortem del incidente de fraude](../../4_archivos/postmortem_transferencias_pull_marzo_2026.md)) — su
volumen ya venía sostenido hasta marzo ($653.898 M) y se derrumbó recién en abril ($62.421 M), consistente con
un apagado gradual tras la salida formal.

**Por qué importa:** el North Star #1 no está en problemas — está midiendo un hueco ya conocido y ya
explicado. Es la primera vez que se cuantifica cuánto de esa pérdida representa en volumen mensual, justo
cuando el objetivo (top 2 en API BANK) se va a medir en esa misma unidad. El negocio real (todo menos
Astropay) viene creciendo desde entonces.
**Qué hacer:** cuando se calcule el gap contra el target de "top 2", descontar explícitamente el efecto
Astropay para no confundir una pérdida ya asumida con una tendencia de negocio en curso.

#### 🟠 2. La NSM #1 (Operaciones/Wallet) semanal bajó por Carrefour — y BSF ya es ~65-67% de esa componente mensual, no solo de la semana.

BSF (Carrefour) hizo $80.975 M contra $118.262 M la semana anterior (**−31,5%**); toda la caída semanal de
−18,2% es ese movimiento. Con la vista mensual se ve la foto completa: el share de BSF sobre la NSM #1 saltó
de ~29% (enero-marzo) a **~65-67% desde abril** — justo cuando Astropay desapareció del todo. No es que BSF
haya crecido tanto en términos absolutos (se mantiene entre $330-430 M/mes); es que **al vaciarse el resto de
la cartera, BSF pasó a ser, de lejos, el cliente dominante** de lo que queda.

**Por qué importa:** con Astropay afuera, la concentración de riesgo de la NSM #1 es hoy más alta que nunca —
y la empresa ya conoce el costo de depender de un solo cliente. Sumado a la tensión abierta con BSF por el
incidente fraudulento de abril ([ficha del cliente](../../2_areas/clientes/casos_de_uso_clientes.md)), el riesgo no es
teórico.
**Qué hacer:** entender si la caída semanal puntual de BSF es estacional u operativa, y empezar a reportar la
NSM #1 también *ex-BSF* además de *ex-Astropay*, para ver qué tan grande es el negocio realmente diversificado.

#### 🔴 3. Todo el crecimiento de la NSM #2 es un solo grupo de clientes: DESA es el 86,8%.

Las distribuidoras eléctricas del Grupo DESA (Edelap, Edesa, Edea, Eden, Edes) más su recaudador RIPSA
hicieron **$9.179 M de los $10.579 M** de la semana. Su share pasó de ~60% en abril a **86,8%** hoy, y es
exactamente lo que explica el +144,7% contra baseline. **EDES facturó por primera vez esta semana**
($321 M), completando el plan de altas escalonadas en Payway que figura en la ficha del cliente.

**Por qué importa:** la NSM #2 está en máximo histórico y con tendencia de +16,9% semanal — pero es la rampa
de onboarding de un solo grupo, no crecimiento de cartera. Cuando esas 5 distribuidoras terminen de escalar,
la curva se aplana sola salvo que haya otra cosa detrás.
**Qué hacer:** proyectar el techo de DESA (facturación de servicio público es estacional y acotada) y ver qué
hay en el pipeline capaz de sostener la pendiente después.

#### 🟠 4. Las altas de comercios cayeron 66% en un trimestre — y es la palanca upstream de la NSM #2.

Promedio de las últimas 4 semanas: **30 comercios nuevos por semana**, contra **87** trece semanas atrás
(−65,8%). No es ruido semanal: es un escalón sostenido. El opportunity tree de `north_star.md` pone
"+ comercios" como la palanca común aguas arriba de Botón Simple **y** de POS.

**Por qué importa:** el punto 2 dice que el crecimiento actual de la NSM #2 no tiene reemplazo en la cartera;
este dice que tampoco lo está entrando. Son el mismo problema visto desde los dos extremos del funnel.
**Qué hacer:** entender si la caída es comercial (menos venta), operativa (cuello en el alta) o de
clasificación. Es la pregunta más accionable de la semana.

#### 🟠 5. Sociedad Militar pasó de $24 M a $17.274 M en ocho semanas y ya es el #2 de Wallet.

Volumen semanal: $24 M (sem. 202621) → $2.042 M → $1.861 M → $8.509 M → **$17.274 M**. En paralelo, **37.438
altas de cuentas en la semana 202628** y 8.055 en ésta — un alta masiva, no crecimiento orgánico.

**Por qué importa:** es la primera diversificación real de la concentración del punto 1, y es una de las 5
organizaciones dominantes del [KR1 del foco Onboarding](../../2_areas/direccion/estado_actual.md). Un cliente que
suma decenas de miles de cuentas de golpe mueve el denominador de la cobertura KYC.
**Qué hacer:** confirmar que esas altas entran con legajo — si no, este cliente empeora el KR1 mientras
mejora la NSM.

#### 🟠 6. Octagon se está apagando: de ~$1.000 M semanales a $65 M.

Cayó **−88,3%** contra su promedio de 4 semanas ($559 M → $65,2 M), con $30 M la semana previa. La cronología
del cliente lo anticipaba: 25/06 se dio de baja la Cuenta Remunerada (se fue con otro proveedor) y 02/07
migró su Onboarding a integración directa con RENAPER, dejando de usar el de Bind.

**Por qué importa:** es chico en volumen (0,4%), pero el patrón es el de una salida en curso, no una mala
semana. Vale confirmarlo antes de que sea un hecho consumado.

#### 🟡 7. Dos de las seis palancas de la NSM #1 siguen apagadas.

Transferencia Pull Crédito y Pull Débito están en **$0** — consistente con el
[postmortem de marzo 2026](../../4_archivos/postmortem_transferencias_pull_marzo_2026.md), no es un problema
de la ingesta. Se mantienen dentro de la definición de la NSM para que, el día que se reactiven, sumen solas
y se vea el salto.

#### 🟡 8. Uno de cada cinco pagos con tarjeta se rechaza.

Tasa de rechazo de la NSM #2: **21,4%** (media 8 semanas 24,5%). Por medio de pago: crédito 29,8%, débito
16,9%, prepaga 21,6% (venía de 44,0% — mejora fuerte). El nivel absoluto es alto aunque la tendencia sea
buena, y cada punto de rechazo es volumen que no llega al gateway.
**Qué hacer:** separar rechazo del emisor (fuera de nuestro control) de rechazo por validación propia, para
saber cuánto de ese 21,4% es recuperable.

#### 🔴 9. *(Actualizado 2026-07-23)* NSM#1 pasa a incluir la palanca de Agente de Cobros — el volumen oficial casi se duplica.

El usuario confirmó que las transferencias del producto Agente de Cobros y Pagos (entrantes CVU/CBU,
salientes) se suman al número oficial de NSM#1, **"desde siempre y hacia adelante también"** — corren
contra la misma API BANK que Operaciones de Wallet. Con la fusión, NSM#1 de esta semana pasa de
**$147.326 M (solo Wallet) a $297.488 M (oficial)** — la palanca ($150.162 M) es hoy **más grande que la
propia Operaciones de Wallet** (50,5% del total), con tendencia de 6 semanas de +9,5%/semana y `z=+2,94`
contra las 8 semanas previas (cambio de nivel real, no ruido). Todo el histórico ya reportado de NSM#1
(incluidos los hallazgos 1 y 2 de esta misma entrada, que siguen hablando de la componente Wallet-only) debe
leerse ahora junto con esta salvedad — ver §1c para el detalle de la fusión.

Además la palanca está tan concentrada como BSF en Operaciones: **"Bind PSP liquidaciones cta 14" es el
40,9% del volumen TAC y el top-3 el 72,8%** — mismo patrón de riesgo de dependencia de un solo collector que
ya se ve en el hallazgo 2 con BSF. Y ~$3,8 M de la semana quedan sin clasificar (`Type=NULL`, ver gap en
`../../2_areas/gaps_y_preguntas.md`) — suman al total pero no se les asigna IN ni OUT.

**Por qué importa:** cualquier lectura previa de "qué tan cerca estamos de top 2 en API BANK" hecha solo con
Operaciones de Wallet quedaba corta en un orden de magnitud comparable a su propio volumen. La serie mensual
completa del anexo (§3) también cambia sustancialmente: enero 2026 pasa de $1.152.974 M a $1.546.504 M, por
ejemplo — la magnitud del "pico de enero" del hallazgo 1 crece, aunque la narrativa Astropay (calculada
sobre Wallet) se mantiene igual.
**Qué hacer:** de acá en adelante, citar siempre "NSM#1 = $297.488 M (oficial, Wallet + Agente de Cobros)" —
nunca solo la componente Wallet — al reportar hacia la gerencia o comparar contra el objetivo de "top 2".

---

### 3 · Anexo — Métricas de soporte

**Serie mensual completa (desde sep-2025) — volumen total del mes, para ver la magnitud absoluta.**
La columna "MoM" acá es **mes completo vs. mes completo** (no el tramo de semanas de la vista principal en
§1b) — sirve para ver la tendencia de fondo mes a mes, no para el KPI de MoM del reporte.

| Mes | NSM #1 *(oficial)* | MoM (mes completo) | NSM #2 | MoM (mes completo) |
|---|---|---|---|---|
| 2025-09 | $476.139 M | s/d | $4.172 M | s/d |
| 2025-10 | $730.477 M | +53,4% | $5.042 M | +20,8% |
| 2025-11 | $625.391 M | −14,4% | $4.401 M | −12,7% |
| 2025-12 | $813.380 M | +30,1% | $4.640 M | +5,4% |
| 2026-01 | **$1.546.504 M** | +90,1% | $5.211 M | +12,3% |
| 2026-02 | $1.323.010 M | −14,5% | $6.268 M | +20,3% |
| 2026-03 | $1.451.705 M | +9,7% | $9.611 M | +53,3% |
| 2026-04 | $1.069.065 M | −26,4% | $12.021 M | +25,1% |
| 2026-05 | $853.360 M | −20,2% | $11.768 M | −2,1% |
| 2026-06 | $884.400 M | +3,6% | **$20.850 M** | +77,2% |
| 2026-07* | $895.696 M | +1,3% | $28.169 M | +35,1% |

*(\*) julio 2026 en curso — 3 de ~4 semanas informadas, no comparable 1:1 contra un mes cerrado (por eso el
KPI de MoM de §1b usa el tramo de 3 semanas, no este total). Serie recalculada 2026-07-23 con la fusión de
Operaciones + Transferencias Agente de Cobros; los valores de meses pre-2026-01 no cambian porque el store no
tiene datos de esa tabla antes de esa fecha (el backfill de TAC empieza en 202601).*

**NSM #1 — Astropay vs. resto de la cartera, por mes, SOLO componente Operaciones/Wallet** (ver hallazgo 1;
estas cifras no incluyen la palanca de Agente de Cobros, que no tiene concepto de "cliente Astropay"):

| Mes | Total (Wallet) | Astropay | Resto (ex-Astropay) |
|---|---|---|---|
| 2026-01 | $1.152.974 M | $707.985 M | $444.990 M |
| 2026-02 | $967.066 M | $607.207 M | $359.858 M |
| 2026-03 | $1.045.040 M | $653.898 M | $391.142 M |
| 2026-04 | $665.532 M | $62.421 M | $603.111 M |
| 2026-05 | $514.607 M | $0,04 M | $514.569 M |
| 2026-06 | $548.736 M | $0,02 M | $548.712 M |

**Salud (no suman al volumen NSM):**

| Métrica | Semana | Media 8 semanas |
|---|---|---|
| NSM #1 — tasa de rechazo | 0,4% | 0,8% |
| NSM #1 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 — tasa de rechazo | 21,4% | 24,5% |
| NSM #2 — tasa de devolución | 0,0% | 0,0% |
| NSM #2 / Crédito — rechazo | 29,8% | 33,1% |
| NSM #2 / Débito — rechazo | 16,9% | 19,6% |
| NSM #2 / Prepaga — rechazo | 21,6% | 44,0% |
| TAC Agente de Cobros — tasa de falla (no COMPLETED) | 0,5% | 0,4% |

**Altas (leading indicator del volumen):**

- **Cuentas de Wallet:** 32.192 en la semana (media 8 semanas 28.111; −50,0% WoW contra el pico de 64.425 de
  la semana anterior, explicado por el alta masiva de Sociedad Militar). Top: BSF 8.280 (25,7%) ·
  Sociedad Militar 8.055 (25,0%) · CENCOSUD 5.969 (18,5%) · Credicuotas 4.614 (14,3%) · Global 66 2.249 (7,0%).
  **COTO viene escalando** (37 → 476 → 798 → 1.030 → 999 en cinco semanas): el pipeline comercial de
  `north_star.md` empezó a operar.
- **Comercios de Adquirencia:** 31 en la semana (media 8 semanas 77; ver hallazgo 3). Top: Consorcio Abierto
  17 · GST 5 · PMC 2 · Desarrollos del Litoral 2.

**Top clientes NSM #1 (Operaciones/Wallet):** BSF $80.975 M (55,0%) · Sociedad Militar $17.274 M (11,7%) ·
Terra Blockchain $15.554 M (10,6%) · CENCOSUD $11.970 M (8,1%) · Global 66 $11.683 M (7,9%) ·
Credicuotas $4.236 M (2,9%). *(Ver §1c para el top de collectors de la palanca Agente de Cobros.)*

**Top entidades NSM #2:** EDEA $2.432 M (23,0%) · EDESA $2.265 M (21,4%) · EDEN $2.018 M (19,1%) ·
EDELAP $1.849 M (17,5%) · FAVACARD $517 M (4,9%) · EDES $321 M (3,0%, primera semana) · RIPSA $294 M (2,8%).

**Palancas indirectas de la NSM #1** (no suman, alimentan el saldo que después opera): transferencias
internas $17.692 M por pata (son las dos patas de la misma operación, no se suman entre sí) · Viaje QR
$44,6 M · dólar CCL y cripto en volúmenes marginales.

**Adquirencia fuera de Payway** (contexto): Liquidador $31.480 M (+133,4%) · Transferencia 3.0 $15.331 M ·
Transf. Entrante CVU $15.180 M · **MPOS / POS presente $1.641 M** — cuando el proyecto de POS por Payway se
shippee, ese volumen pasa a sumar a la NSM #2 (hoy sería ~+15%).

---

*Próxima corrida: semana 202630 (20 → 27 de julio de 2026), con el export completo de esa semana.*
