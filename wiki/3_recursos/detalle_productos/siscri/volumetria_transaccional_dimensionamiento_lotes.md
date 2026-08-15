# Volumetría transaccional para dimensionar el procesamiento por lotes de SISCRI

> Estado: en producción.

> Fuente: análisis ad-hoc (2026-07-07) sobre una muestra de 100.000 filas de `Transaccion` ("top 100k", sin filtrar por forma de pago ni plazo), provista por el usuario. Complementa [calculo_impuesto_online_qr.md](calculo_impuesto_online_qr.md) (que analiza específicamente latencia y cobertura de QR + Plazo 0): ese documento responde "¿qué tan rápido se calcula el impuesto?"; este responde **"¿cuánto volumen hay que soportar, y compite con qué otra cosa?"** — el dato necesario para dimensionar los lotes chicos y frecuentes con los que se resuelve el cálculo de impuesto, dado que **SISCRI no soporta cálculo verdaderamente online**.

## 1. Volumen y período de la muestra

- **100.000 filas totales**, sin filtrar por `FormadePago` ni `Plazo` (a diferencia de la muestra usada en `calculo_impuesto_online_qr.md`, que ya venía filtrada a QR+Plazo0).
- `Estado`: 96.333 `ACREDITADO`, 3.656 `RECHAZADA`, 8 `DEVUELTA`, 2 `REALIZADA`, 1 `ENPROCESO`.
- `Plazo`: 64.922 en `0` (liquidación en línea), 28.527 en `1`, 4.088 en `18`, 2.463 en `2`.
- `FormadePago`: `50` (55.325), `20`=QR (19.801), `90` (11.819), `40` (8.964), `80` (3.958), `60` (133).

## 2. Hallazgo metodológico: `FormadePago=50` no es tráfico transaccional real, es una carga masiva de archivo

Antes de poder calcular cualquier distribución de "transacciones por minuto" hay que descartar esto, porque distorsiona todo el análisis si se lo mezcla con tráfico real:

- **`Transaccion.FechaProceso` no sirve como timestamp para `FormadePago=50`**: viene siempre con hora fija `00:00:00.0000000 -03:00` (solo fecha, sin precisión real) en las 55.325 filas de este tipo. Por eso todo este análisis usa `FechaLocalNegocio+HoraLocalNegocio` como fuente de tiempo (única con precisión real en el 100% de las filas de la muestra).
- **`IdentificadorProcesadorPago` de estas filas contiene literalmente una referencia a archivo plano**: ej. `ESUR04072026143919147312.92TE260707.txtlinea:18321` — nombre de archivo `TE260707.txt` (Transferencias Electrónicas del 2026-07-07) y número de línea. Esto es un **import de archivo de transferencias**, no una API transaccional en tiempo real.
- **El espaciado entre timestamps consecutivos es de ~2,7-3,9 milisegundos** (mediana ~2.785 µs) — el ritmo de un loop de carga a base de datos, no de arribo orgánico de pagos.
- **Las 55.325 filas quedaron concentradas en una ventana de ~28 minutos** (10:09:27 a 10:37:17, hora local), a un ritmo promedio de **~33 filas/segundo** (~1.988 filas/minuto), con picos de hasta 3.000 filas en un solo minuto.
- **100% de estas filas son `Plazo=0` y `ACREDITADO`** — por eso, si no se excluyen, contaminan por completo cualquier análisis de "Plazo=0" con un volumen que no tiene nada que ver con tráfico de cobro online.

**Conclusión**: para el resto de este documento, `FormadePago=50` se analiza aparte (§4) y se excluye del análisis de "tráfico real" (§3).

## 3. Distribución de transacciones/minuto — tráfico real (excluyendo la carga de archivo)

- **Muestra de tráfico real**: 44.675 filas (100.000 − 55.325 de `FormadePago=50`).
- **Período cubierto**: 2026-07-07 07:09:31 → 16:03:37 (hora local Argentina) — **~8,90 horas continuas**.
- `FormadePago` de este subconjunto: `20`=QR (19.801), `90` (11.819), `40` (8.964), `80` (3.958), `60` (133).
- **De estas, `Plazo=0` real es casi exclusivamente QR**: 9.572 de 9.597 filas `Plazo=0` (99,7%) son `FormadePago=20`; las otras 25 son `FormadePago=40`. Esto confirma que el universo relevante para el cálculo online de impuesto (documentado en `calculo_impuesto_online_qr.md`) es, en la práctica, sinónimo de QR+Plazo0.

### Transacciones/minuto

| Percentil | Total (todas las formas/plazos) | Plazo = 0 | Plazo ≠ 0 |
|---|---|---|---|
| Mínimo | 9 | 0 | 7 |
| Mediana (p50) | 73 | 14 | 59 |
| p75 | 125 | 29 | 95 |
| p90 | 151 | 38 | 113 |
| p95 | 158 | 41 | 121 |
| p99 | 171 | 49 | 130 |
| **Máximo** | **181** | **55** | **141** |

### Por ventana de tiempo (para lotes de 5 o 15 minutos)

| Ventana | Métrica | Total | Plazo = 0 | Plazo ≠ 0 |
|---|---|---|---|---|
| 5 min | Mediana | 367 | 69 | 296 |
| 5 min | p95 | 769 | 197 | 581 |
| 5 min | **Máximo** | **795** | **216** | **606** |
| 15 min | Mediana | 1.042 | 189 | 856 |
| 15 min | p95 | 2.272 | 564 | 1.701 |
| 15 min | **Máximo** | **2.295** | **598** | **1.747** |

### Pico vs. valle por hora del día (hora local Argentina, tx/min)

| Hora | Total | Plazo = 0 | Plazo ≠ 0 |
|---|---|---|---|
| 07h | 29,5 | 4,6 | 24,9 |
| 08h | 62,7 | 13,0 | 49,7 |
| 09h | 104,5 | 24,0 | 80,5 |
| 10h | 136,2 | 34,2 | 102,0 |
| **11h** | **151,4** | **38,0** | **113,4** |
| 12h | 117,6 | 25,6 | 92,0 |
| 13h | 48,2 | 6,2 | 42,1 |
| 14h | 45,2 | 4,7 | 40,5 |
| 15h | 50,1 | 9,8 | 40,3 |
| 16h | 53,8 | 10,3 | 43,5 |

El pico del día (dentro de la ventana cubierta por la muestra) está en la hora 11h, con **151 tx/min en total** y **38 tx/min de Plazo=0**. Nota: esta muestra cubre solo ~8,9h del día (07h-16h); no permite ver el comportamiento nocturno ni el pico de tarde-noche (17h-21h) que sí se observó en la muestra específica de QR+Plazo0 de `calculo_impuesto_online_qr.md` (con datos de un período más largo).

**Plazo=0 y Plazo≠0 están fuertemente correlacionados minuto a minuto** (correlación 0,89 tras excluir la carga de archivo — suben y bajan juntos porque comparten el mismo ciclo de actividad comercial del día), pero **Plazo=0 es sistemáticamente una fracción menor**: entre ~11% y ~25% del total según la hora (promedio por hora), nunca la mayoría del tráfico.

## 4. Perfil de la carga de archivo (`FormadePago=50`) — competencia de infraestructura, no de negocio

Aunque no es tráfico transaccional online, **si comparte base de datos o infraestructura con el procesamiento de SISCRI, sí puede competir por recursos**:

- Ventana de carga: 2026-07-07 10:09:27 → 10:37:17 (**~28 minutos**), un evento que —a juzgar por el patrón— corre como job/import programado (probablemente asociado a la recepción diaria de un archivo bancario de transferencias).
- Ritmo: ~33 filas/segundo promedio, con minutos puntuales de hasta 3.000 filas.
- **Coincide en el tiempo con horario de tráfico real ya alto** (10h-11h, cerca del pico de 151 tx/min total) — es decir, el momento de mayor carga transaccional orgánica del día es también cuando corre esta carga masiva de archivo.

## 5. Implicancias para el diseño de lotes

1. **El universo relevante para el cálculo online de impuesto es acotado**: Plazo=0 real (excluyendo la carga de archivo) nunca superó **55 tx/min**, **216 tx/5min** ni **598 tx/15min** en esta muestra. Un lote dimensionado contra el p95/p99 de estos valores (41 tx/min, ~200 tx/5min, ~565-600 tx/15min) cubriría cómodamente el tráfico online real observado.
2. **No hace falta dimensionar el lote de impuesto online contra el volumen total (incluyendo Plazo≠0)** — ese tráfico no es parte del alcance de "cálculo en línea" (los `Plazo≠0` no requieren el mismo nivel de premura), salvo que compartan la misma cola/infraestructura de procesamiento.
3. **La carga de archivo (`FormadePago=50`) es el verdadero pico de volumen del día** (hasta 3.000 filas/minuto) y **no está sincronizada con el volumen de Plazo=0 online** — es un proceso aparte. Si comparte base de datos/infraestructura con SISCRI o `ServiceProcess`, conviene verificar si su ventana de ejecución (aprox. 10h-10:30h local) coincide con backlog o degradación del cálculo online, y considerar aislar o reprogramar uno de los dos procesos si hay contención.
4. Esta muestra cubre una ventana más corta (~8,9h, un solo día) que la de `calculo_impuesto_online_qr.md` (~34h) — para confirmar el pico real de tarde-noche (17h-21h, que en la otra muestra mostró hasta 9,9 tx/min de QR+Plazo0 solamente) convendría repetir este mismo análisis de volumen con una muestra que cubra esas horas.

## 6. Escenario transitorio: la misma distribución sin excluir `FormadePago=50`

**Por qué se agrega esta sección**: el usuario indicó que el cliente/forma de pago asociado a `FormadePago=50` probablemente se dé de baja en el corto plazo. Hasta que eso ocurra, es volumen real que el sistema tiene que absorber hoy — por eso, además del escenario "limpio" de §3 (que es el que va a quedar vigente a mediano plazo), acá va el mismo cálculo **sin excluir nada**, para dimensionar contra el presente.

### Transacciones/minuto (100.000 filas, sin excluir `FormadePago=50`)

| Percentil | Total (todas las formas/plazos) | Plazo = 0 (incluye `FormadePago=50`) | Plazo ≠ 0 |
|---|---|---|---|
| Mínimo | 9 | 0 | 7 |
| Mediana (p50) | 73 | 14 | 59 |
| p75 | 130,5 | 30 | 95 |
| p90 | 161 | 41 | 113 |
| p95 | **445** | **347** | 121,3 |
| p99 | **2.850** | **2.742** | 129,7 |
| **Máximo** | **3.144** | **3.041** | **141** |

Nota: `Plazo ≠ 0` es idéntico a la tabla de §3 — `FormadePago=50` es 100% `Plazo=0`, así que no lo afecta. Todo el salto entre p90 y p95 (de 41 a 347 tx/min en Plazo=0) es la carga de archivo entrando de golpe.

### Por ventana de tiempo

| Ventana | Métrica | Total | Plazo = 0 (incl. F50) | Plazo ≠ 0 |
|---|---|---|---|---|
| 5 min | Mediana | 367 | 69 | 296 |
| 5 min | p95 | **4.647** | **4.128** | 581 |
| 5 min | **Máximo** | **11.196** | **10.684** | 606 |
| 15 min | Mediana | 1.042 | 189 | 856 |
| 15 min | p95 | **13.865** | **12.530** | 1.701 |
| 15 min | **Máximo** | **31.964** | **30.493** | 1.747 |

### Pico vs. valle por hora del día (hora local Argentina, tx/min)

| Hora | Total | Plazo = 0 (incl. F50) | Plazo ≠ 0 |
|---|---|---|---|
| 07h | 29,5 | 4,6 | 24,9 |
| 08h | 62,7 | 13,0 | 49,7 |
| 09h | 104,5 | 24,0 | 80,5 |
| **10h** | **1.058,3** | **956,3** | 102,0 |
| 11h | 151,4 | 38,0 | 113,4 |
| 12h | 117,6 | 25,6 | 92,0 |
| 13h | 48,2 | 6,2 | 42,1 |
| 14h | 45,2 | 4,7 | 40,5 |
| 15h | 50,1 | 9,8 | 40,3 |
| 16h | 53,8 | 10,3 | 43,5 |

La hora 10h queda completamente distorsionada por la ventana de carga del archivo (~956 tx/min de Plazo=0 solo en esa hora, contra 24-38 tx/min en las horas vecinas). **La correlación minuto a minuto entre Plazo=0 y Plazo≠0 cae de 0,89 (sin F50, §3) a 0,21 con F50 incluido** — confirma que esta forma de pago se mueve con un patrón propio (ráfaga de archivo), desacoplado del ciclo de actividad comercial real que sí comparten QR y el resto de los medios de pago.

### Lectura para el dimensionamiento mientras `FormadePago=50` siga activo

- Si el lote de impuesto trata a `FormadePago=50` igual que al resto del tráfico `Plazo=0` (mismo pipeline, sin distinguir forma de pago), hoy mismo tiene que poder absorber picos de **hasta ~3.041 tx en un minuto** y **~30.493 tx en una ventana de 15 minutos** — un orden de magnitud completamente distinto al del tráfico QR real (máximo 55 tx/min, ver §3). Dimensionar el lote contra estos números en vez de contra los de §3 sería sobredimensionar para siempre un volumen que, según el usuario, es transitorio.
- Alternativa más razonable: si es técnicamente viable, **tratar la carga de `FormadePago=50` en un camino separado** (batch dedicado a la ingesta de archivo, no el mismo lote pensado para cálculo "en línea" de QR) — evita que un cliente que se va a dar de baja defina el dimensionamiento permanente de la feature.
- **Mientras tanto**, conviene confirmar si el pipeline actual ya distingue estos dos casos o si efectivamente los procesa juntos — no verificado en `calculo_impuesto_online_qr.md` (esa muestra ya venía filtrada a QR, por lo que no incluía `FormadePago=50`).

## Ver también

- [calculo_impuesto_online_qr.md](calculo_impuesto_online_qr.md) — diagnóstico de latencia y cobertura del cálculo online para QR+Plazo0 (el "qué tan rápido"; este documento es el "cuánto volumen").
- [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md) — pregunta abierta sobre contención de infraestructura entre la carga de archivo y el procesamiento online, y sobre el pipeline de `FormadePago=50`.

---
*Última actualización: 2026-07-07 — Agregada §6 con el escenario transitorio (sin excluir `FormadePago=50`), a pedido del usuario, para dimensionar mientras ese cliente/forma de pago siga activo.*
