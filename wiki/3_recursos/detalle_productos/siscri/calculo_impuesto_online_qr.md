# Cálculo de impuesto "en línea" para QR con liquidación Plazo 0 — diagnóstico de latencia

> Estado: en producción.

> Fuente: análisis ad-hoc (2026-07-06) sobre dos muestras CSV extraídas por el usuario directamente de producción (`Transaccion` y `LIQ_IMP`), no una ingesta de Notion/documentación. Complementa [configuracion_entidades.md](configuracion_entidades.md) (alta de comercios en SISCRI) con la mecánica de ejecución del cálculo para el caso QR + Plazo 0. Ver también [siscri/index.md](index.md) y el rol de SISCRI en liquidación de Adquirencia en [adquirencia_overview.md](../../../2_areas/overview_productos/overview_adquirencia.md#liquidaciones-e-impuestos-siscri).

## 1. Mecánica del flujo

Cuando se acredita un cobro con **forma de pago QR** y **liquidación en línea (`Plazo=0`)**, el camino de cálculo de impuesto es:

```
Transaccion  --(evento asíncrono, RabbitMQ)-->  ServiceProcess  -->  LIQ_IMP
```

- `ServiceProcess` es la tabla pivot intermedia que recibe el evento y dispara el cálculo real.
- `LIQ_IMP` registra cada cálculo de impuesto ejecutado, enlazado por `ID_TX` = `Transaccion.Id`.
- El diseño esperado (confirmado por el usuario) es que, aunque la comunicación entre etapas sea siempre asíncrona, el resultado sea **casi instantáneo** — no un proceso batch con demora de horas.
- **Solo las transacciones en `Estado=ACREDITADO` deben generar cálculo de impuesto** (regla de negocio confirmada). El resto (`RECHAZADA`, `DEVUELTA`, etc.) no debería generar nunca una fila en `LIQ_IMP`.

## 2. Metodología del diagnóstico

Muestra analizada: 10.000 filas de `Transaccion` (top 100k filtrado a `FormadePago=20` (QR) y `Plazo=0`) cruzadas contra `LIQ_IMP` buscando cada uno de esos 10.000 `Id` como `ID_TX` (9.911 filas encontradas). **`ServiceProcess` no fue consultado en este pase** por volumen — queda pendiente para un pase posterior con muestra más chica, necesario para atribuir causa raíz (ver §6).

Zonas horarias confirmadas por el usuario: `Transaccion.FechaProceso` y `LIQ_IMP.FEC_REG_AUD` están **ambos en UTC+0** (no hace falta ningún ajuste entre sí); `Transaccion.FechaLocalNegocio`/`HoraLocalNegocio` está en UTC-3. La latencia se calculó directamente como `LIQ_IMP.FEC_REG_AUD − Transaccion.FechaProceso`, sin conversión de huso horario.

## 3. Volumen y throughput de la muestra

Contexto necesario para dimensionar el procesamiento por lotes: **SISCRI no soporta cálculo verdaderamente online** — la solución de diseño pasada y futura es correr lotes chicos con frecuencia alta. Para dimensionar esos lotes hace falta saber cuántas transacciones de este tipo entran por unidad de tiempo, y sobre todo el **pico**, no solo el promedio.

- **Volumen analizado**: 10.000 filas de `Transaccion` (9.914 `ACREDITADO` — el universo real que dispara el evento hacia SISCRI).
- **Período cubierto**: 2026-07-04 17:00:34 UTC → 2026-07-06 02:57:31 UTC (**~33,95 horas**, prácticamente el día completo del 5 de julio más las puntas del 4 y el 6). La muestra no es un sorteo aleatorio disperso en el tiempo: son las ~10.000 transacciones QR+Plazo0 más recientes en un tramo contiguo real, lo que la hace representativa del tráfico real de esa ventana.
- **Promedio global**: **4,87 transacciones/minuto** (`ACREDITADO`) en todo el período. De los 2.038 minutos del período, el 86,3% tuvo al menos 1 transacción de este tipo.

**Distribución de transacciones/minuto** (la métrica clave para dimensionar):

| Percentil | Tx/minuto |
|---|---|
| Mediana (p50) | 3 |
| p75 | 7 |
| p90 | 12 |
| p95 | 14 |
| p99 | 19 |
| **Máximo** | **23** (a las 17:25 UTC del 2026-07-04) |

**Por ventana de tiempo** (útil si el lote corre cada 5 o 15 minutos en vez de cada minuto):

| Ventana | Mediana | p90 | p95 | p99 | Máximo |
|---|---|---|---|---|---|
| 5 min | 19 | 58 | 70 | 80 | 88 |
| 15 min | 56 | 170 | 204 | 234 | 244 |

**Pico vs. valle según hora del día**: agrupando por hora de `FechaProceso` (UTC+0), el tráfico varía muchísimo durante el día — el pico está entre las **20h y 23h UTC** (17h-20h hora Argentina) con **7,9 a 9,9 tx/min**, contra un valle entre las **8h y 11h UTC** (05h-08h hora Argentina) con solo **0,17 a 0,52 tx/min**. Es decir, un factor de **~20-30x entre el momento más cargado y el más tranquilo del día**.

**Implicancia directa para el dimensionamiento de lotes**: diseñar la capacidad del lote en base al promedio (24 tx/5min o 73 tx/15min) subestima el pico real por un factor de ~3-4x — conviene dimensionar contra el p95/p99 (70-80 tx/5min, 204-234 tx/15min), no contra el promedio. Este subdimensionamiento coincide, además, con el momento exacto del atasco documentado en §4: el lote varado del comercio C11174 ocurrió entre las 22:39 y 22:41 UTC, **dentro de la franja pico** (hora 22 UTC = 9,88 tx/min, la más alta de todo el día).

## 4. Hallazgo principal: alta varianza, con evidencia de atascos y ráfagas de backlog

Sobre 9.910 transacciones `ACREDITADO` con match en `LIQ_IMP`:

| Percentil     | Latencia           |
| ------------- | ------------------ |
| Mínimo        | 6,2 s              |
| p25           | 0,92 h (~55 min)   |
| Mediana (p50) | 1,71 h (~1h 42min) |
| p75           | 2,40 h             |
| p90           | 2,92 h             |
| p95           | 3,19 h             |
| p99           | 5,18 h             |
| Máximo        | 5,38 h             |

**El camino rápido existe y funciona**: el mínimo real es de segundos (ver ejemplo `Id=28884063`: `FechaProceso` 23:56:44.972 → `FEC_REG_AUD` 23:56:51.190, latencia 6,22 s). El problema no es un piso de demora fijo, sino la **enorme varianza**: la mitad de las transacciones tarda más de 1h42, un 10% supera las 2,92h, y hay una cola de hasta 5,38h — muy lejos de "casi instantáneo" como diseño esperado para la mayoría del volumen.

**Evidencia concreta de atasco y ráfaga de backlog** (no solo cola estadística): las 30 transacciones con mayor latencia de la muestra pertenecen todas al comercio `C11174`, con `FechaProceso` concentrado entre las **22:39:10 y 22:41:02 UTC del 2026-07-04** (menos de 2 minutos de diferencia entre todas), pero quedaron registradas en `LIQ_IMP` recién entre las **03:57:42 y 04:02:19 UTC del 2026-07-05** (~5,3-5,4h después, todas juntas en una ventana de 5 minutos). Es decir: un lote completo de transacciones casi simultáneas quedó parado ~5,3h y se liberó de golpe en una sola corrida — consistente con un backlog/cola que se acumula y se drena en ráfaga, no con notificación instantánea por evento individual.

**Evidencia de cadencia tipo batch/cron**, no consumo puro de evento (este hallazgo no depende de la corrección de huso horario, ya que un desfase de horas completas no cambia el minuto): el minuto-de-hora de `FEC_REG_AUD` muestra picos muy marcados y repetidos en los minutos **:00 (598 casos), :15 (630), :33 (621) y :53 (539)** de cada hora, contra un piso de ~100-190 casos en el resto de los minutos. Sugiere que el registro en `LIQ_IMP` (o una etapa previa) corre atado a un job periódico, no a una notificación instantánea por transacción — compatible con la ráfaga de backlog descripta arriba.

**Latencia peor en ciertas franjas horarias**: agrupando por hora de `FechaProceso` (UTC+0), la mediana sube a ~2,5h en las horas 17 y 20-23 UTC (equivalente a ~14h y ~17-20h hora Argentina) contra ~0,5-1h en horas de madrugada Argentina. Por comercio, `C15946` (mediana 2,53h) y `C02025` (2,14h, el de mayor volumen con 2.243 casos) están entre los más lentos; `C15618` (0,80h) y `C15647` (0,87h) entre los más rápidos.

## 5. Anomalías de cobertura e integridad

- **Cobertura**: 9.910 / 9.914 transacciones `ACREDITADO` de la muestra tienen su `LIQ_IMP` (99,96%). Las 4 restantes (`Id` 28869826, 28850643, 28843085, 28827946 — comercios C11174, C17824, C02025, C11174) están `ACREDITADO` pero **no tienen ningún registro en `LIQ_IMP`**. El dato más reciente de la muestra (`LIQ_IMP.FEC_REG_AUD` máximo, UTC+0) es 2026-07-06 04:02:17; tomando ese momento como referencia y comparando contra `FechaProceso` (mismo huso, UTC+0) de cada una, las 4 transacciones huérfanas tienen entre ~10,3h y ~33,8h de antigüedad — muy por encima del máximo de latencia observado en toda la muestra (5,38h). No son transacciones recientes en tránsito: son transacciones acreditadas que, al momento del corte, **nunca calcularon impuesto** — bug real a trazar en producción.
- **Violación de la regla de negocio**: la transacción `Id=28838417` (comercio C11174) tiene `Estado=DEVUELTA` pero **sí tiene** una fila en `LIQ_IMP` (`ID_LIQ_IMP=24846790`, calculada el 2026-07-04 23:11:45). Su `EstadoMotivo` es `DEBINCOELSA:ACREDITADO`, lo que sugiere que la transacción se acreditó primero (y el impuesto se calculó normalmente) y **luego** pasó a `DEVUELTA` — es decir, el estado cambió después de disparado el cálculo. Queda abierto si el sistema debería reversar/anular ese cálculo de impuesto cuando la transacción se revierte (ver el mecanismo de reversa ya documentado para Wallet en [integracion_wallet.md §3](integracion_wallet.md#3-reversa-de-impuestos-quedó-listo-para-desarrollo-no-confirmado-si-se-construyó) — no está confirmado si existe un equivalente para el flujo QR/comercios de este documento).
- **Duplicados**: no se detectó ningún `ID_TX` con más de una fila en `LIQ_IMP` en esta muestra (9.911/9.911 únicos). Sin evidencia de doble cálculo.

## 6. Qué queda pendiente

- **Atribución de causa raíz**: con esta muestra no se puede saber en qué hop ocurren los atascos/ráfagas de backlog (Transaccion→ServiceProcess o ServiceProcess→LIQ_IMP), ni por qué el comercio C11174 tuvo un lote entero varado ~5,3h en un momento puntual. Requiere sumar una muestra de `ServiceProcess` (pendiente, el usuario lo hará con una muestra más chica).
- **Confirmar si las 4 `ACREDITADO` huérfanas siguen sin `LIQ_IMP`** tiempo después del snapshot, o si eran solo transacciones muy recientes en tránsito.
- **Confirmar si existe reversa de impuesto para transacciones QR/comercios que pasan a `DEVUELTA`** después de acreditadas (como sí existe documentado para Wallet).
- Registrado como gap abierto en [../../../2_areas/gaps_y_preguntas.md](../../../2_areas/gaps_y_preguntas.md).

## 7. Decisión de diseño y alcance confirmado — caso PedidosYa (minutas 2026-07-06/07, cerrado 2026-07-16)

> Fuente: mail "Minuta - Modelo PedidosYa: performance del liquidador y próximos pasos" (julieta.gimenez@fintexa.tech, hilo 2026-07-06 → 2026-07-17, minuta final del 16/07). Cierra con decisiones concretas el diagnóstico de §1-6 para el caso puntual de PedidosYa (cliente que usa Aceptador para dar QR a sus comercios).

**Modelo acordado — NO es liquidación online real:** se descarta definitivamente el proceso "de a uno" (transacción por transacción, el cuello de botella actual que compite con el proceso batch por la misma base). Todo pasa a un esquema **por lotes pequeños, continuos y parametrizables** (tamaño N cada X segundos — valor tentativo de arranque ~30 tx/30s, a validar en Staging contra la volumetría real de §3). Referencia de diseño: el modelo ya usado en Wallet.

**Reglas de armado del lote:**
- **Prioridad por transacción online (`Plazo=0`), no por entidad** — se descarta el filtro por `CódigoEntidad` que se había considerado. Para SISCRI, "plazo=0" equivale a "pago online" (Rendiciones siempre envía a liquidar plazo=0 en línea, independientemente de que Impuestos/Retenciones no interprete el plazo en sí).
- Si el lote no se llena en la frecuencia definida, se procesa igual con las transacciones online disponibles en ese momento — **nunca se completa con transacciones de pago diferido** (cláusula eliminada de las condiciones de aceptación).
- **Pago diferido queda fuera de alcance**: sigue como proceso separado de madrugada, sin mezclarse con el lote online.
- **Filtro por entidad**: pasa a backlog como mejora futura (permitiría sumar entidades nuevas con un simple insert a tabla de prioridades), no es parte del alcance actual.

**Alcance técnico confirmado (3 tareas, detalladas en ticket [AD-1383](https://bindpsp.atlassian.net/browse/AD-1383)):** (1) separar la API de Retenciones en una de bajada/recepción (`DownloadRetenciones`, en ServiceProcess) y otra dedicada solo a liquidar/consultar; (2) hacer configurable el proceso online (poder frenarlo/relanzarlo) para eliminar el "de a uno"; (3) priorizar transacciones online al armar el lote (marcar por plazo=0, sin filtro por entidad).

**Punto abierto para las pruebas:** riesgo planteado de que, con flujo online constante, el proceso diferido tarde en encontrar su ventana libre para correr (hoy son procesos separados que se consultan entre sí para no competir por la misma tabla) — a validar en Staging.

**Alcance fiscal inicial:** mientras Bind actúe como agente de retención para PeYa, solo se liquida un impuesto (SIRTAC) — camino más simple. Si en el futuro PeYa pasa a ser agente de retención, se sumarían percepciones/retenciones de régimen particular (camino más largo, fuera de alcance actual).

**Relación con el resto de este documento:** esta decisión es la resolución del mismo problema diagnosticado en §1-6 (alta varianza de latencia, mediana ~1,71h, ráfagas de backlog) — el modelo por lotes parametrizable **es** el mecanismo de mitigación, no un fix del "camino rápido" de 6 segundos. La pregunta de causa raíz de §6 (en qué hop ocurren las ráfagas de backlog) sigue sin resolverse — el nuevo diseño ataca el síntoma (falta de control/throttling explícito) más que la causa raíz puntual del atasco de C11174.

**Riesgo planteado por Fintexa (Pablo Serra, no presente en la reunión):** la performance del liquidador es el punto central del proyecto, no un riesgo más de la lista — sobre la muestra de ~10.000 transacciones QR, la mediana es 1h30 y el máximo ~5h30 (cifras consistentes con §4 de este documento), muy lejos de lo que se le comunicó al cliente ("casi online"). Fintexa no se compromete a esos tiempos hasta medir en Staging; considera que lotes/bifurcación son parches para arrancar, no la solución de fondo (normalizar y escalar el liquidador, a dimensionar por separado).

**Próximos pasos acordados:** dejar trazabilidad en DAD-2215/AD-1383 con lo acordado, liberar la historia para desarrollo; crear ticket de backlog para el filtro por entidad; coordinar con Sergio Pavetto la propuesta de mover el acumulado por comercio a una tabla separada de `LIQ_IMP` (fuera de alcance actual, depende de Pavetto no de Fintexa/Bind).

## Ver también

- [configuracion_entidades.md](configuracion_entidades.md) — alta y configuración de comercios en SISCRI.
- [integracion_wallet.md](integracion_wallet.md) — mecanismo de reversa de impuestos ya documentado del lado Wallet, referencia para la pregunta abierta de §5.
- [adquirencia_overview.md](../../../2_areas/overview_productos/overview_adquirencia.md#liquidaciones-e-impuestos-siscri) — rol de SISCRI en el flujo de liquidación de Adquirencia.
- [adquirencia/psp_as_a_service_normativa_8432.md](../adquirencia/psp_as_a_service_normativa_8432.md) — el otro frente de la relación con PeYa (modelo de aceptador/agrupador normativo), distinto de la performance del liquidador documentada acá.

---
*Última actualización: 2026-07-17 — `/sync_mails`: nueva §7 con la decisión de diseño confirmada para PedidosYa (modelo por lotes parametrizable, prioridad online, alcance de AD-1383) — cierra el diagnóstico de §1-6 con una resolución concreta.*
*Última actualización anterior: 2026-07-06 — Agregada sección de volumen/throughput (tx por minuto, ventana de 5/15 min, pico vs. valle horario) para dimensionar el procesamiento por lotes de SISCRI.*
