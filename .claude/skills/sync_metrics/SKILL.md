---
name: sync_metrics
description: Ingesta SEMANAL de los CSV agregados que el PM exporta de la base (operaciones y cuentas de Wallet, transacciones y comercios de Adquirencia, transferencias Agente de Cobros, más las dimensiones Organizacion/Entidad/Collectors) y medición de las dos North Star Metrics de Bind PSP — volumen operado por API BANK (Banco Industrial) y volumen operado con el gateway Payway. Acumula el histórico en un store propio (wiki/3_recursos/datos/datos_metricas_semanales/ (espejo; escritura vía contexto_vivo/)), calcula NSM y CADA PALANCA del árbol de oportunidades (registro único en pipeline.py, incluye leading indicators de altas) con WoW semanal (dato secundario) y TENDENCIA de ventana móvil de 4 semanas (protagonista — últimas 4 semanas cerradas vs. las 4 previas, sin nombre de mes calendario), y analiza con ojo de PM y analista de datos: cambios de nivel y tendencia sobre toda palanca, churn y activación de clientes, concentración de riesgo, degradación de calidad (rechazos y devoluciones), mix shift, deriva de altas y estacionalidad conocida. Produce un reporte incremental en wiki/3_recursos/datos/metricas_semanales.md y un borrador de email ejecutivo con árbol jerárquico de palancas (render_email.py) a pagomes@bind.com.ar.
when_to_use: Se activa cuando el usuario ejecuta /sync_metrics tras depositar en raw/ los CSV de la semana vencida exportados de la base. Uso semanal, típicamente los lunes con el corte de la semana anterior. Claude NO puede consultar la base por política de seguridad — los datos siempre llegan por raw/. Skill de fuente compartida: la corre solo el runner designado (ver `identidad.local.md`).
disable-model-invocation: true
argument-hint: "[SemanaId opcional, ej. 202629 — por defecto la última semana cerrada]"
---

# 📈 MEDICIÓN SEMANAL DE LAS NSM: /sync_metrics

## 🔒 Paso 0 obligatorio — verificar que sos el runner

Leé `identidad.local.md` (raíz del repo). Si `runner_fuentes_compartidas` no es `true`, **abortá** con un mensaje claro: esta skill lee una fuente objetiva compartida entre los tres PM/PO — correrla en más de un cerebro triplica trabajo sin agregar valor. Avisale al usuario quién es el runner designado y sugerí pedirle que la corra él.

## 🎯 Por qué existe esta skill

Bind PSP tiene dos North Star Metrics fijadas por el CEO ([`north_star.md`](../../../wiki/2_areas/direccion/north_star.md)):
**top 2 en volumen operado por API BANK** y **top 6 adquirentes en volumen Payway**. Ese mismo archivo
documenta el problema real: la empresa *"no tenía una métrica conocida para entender cuánto le faltaba"* —
un **gap de medición, no solo de ejecución**. Esta skill cierra ese gap: convierte el export semanal del PM
en una serie temporal viva de las dos NSM, con lectura de negocio encima.

El foco es doble y en este orden: **(1) cómo venimos contra las NSM**, y **(2) qué aprendimos esta semana**
mirando los datos como PM y como analista — patrones, cambios de tendencia, problemas y oportunidades.

## 🔌 Mecánica: motor + store acumulado

Toda la lógica vive en [`scripts/pipeline.py`](scripts/pipeline.py) (Python, solo stdlib). Cuatro subcomandos:
`inspect` (lee y reporta sin escribir), `ingest` (mergea al store), `analyze` (calcula NSM + palancas +
hallazgos, texto para vos) y `palancas` (mismo cálculo, JSON puro — insumo de
[`scripts/render_email.py`](scripts/render_email.py)), **los dos últimos solo desde el store**, sin volver
a mirar `raw/`.

**Registro de palancas — fuente de verdad única (2026-08-04).** `registro_palancas()` en `pipeline.py`
enumera cada palanca de las dos NSM (componentes Wallet/TAC, IN/OUT, tipos de operación, tipos de TAC,
canales y formas de pago de NSM#2, indirectas de NSM#1, fuera de Payway, y los **leading indicators** —
altas de cuentas de Wallet para NSM#1, altas de comercios de Adquirencia para NSM#2) con su NSM padre,
categoría, si suma al total, su eje (para no contarla dos veces si hay otra partición del mismo total),
su `formato` ("monto" en pesos por default, "entero" para los leading indicators — son una cantidad, no
un monto) y de qué serie de `Datos` sale. `medir_palancas(d, actual)` mide cada una una sola vez — WoW,
z-score, tendencia de regresión de 6 semanas, y la **tendencia de ventana móvil** (`bloque_movil`, ver
más abajo) — y esa medición alimenta por igual el desglose de `analyze`, los detectores
(`_detectar_palancas`) y el JSON de `palancas`.

**Tendencia de ventana móvil — protagonista, reemplaza al "MoM" mensual-calendario (decisión del usuario,
2026-08-04).** `bloque_movil()` compara las últimas `VENTANA_TENDENCIA` (4) semanas cerradas contra las 4
semanas inmediatamente anteriores — **sin relación a mes calendario, sin nombre de mes**. Reemplaza a la
vista mensual por tramo (`bloque_mensual`, que seguía existiendo semanas atrás): esa vista etiquetaba el
número como "julio" cuando en realidad era un tramo capado de hasta 4 semanas, y en un mes de 5 semanas
ISO el número quedaba "congelado" (no se movía) varias semanas seguidas — con riesgo real de que alguien
(el CEO, por ejemplo) leyera "$1.070.467 M" como si fuera el cierre contable exacto de julio, cuando no
lo era. La ventana móvil se actualiza **todas** las semanas y no se puede confundir con un cierre mensual
porque no lleva nombre de mes. `bloque_mensual` no se eliminó — sigue alimentando la "serie mensual
completa" del anexo (mes completo vs. mes completo, para ver magnitud absoluta histórica), que es contexto,
no el número protagonista.

**WoW — dato secundario, no protagonista (revierte la decisión del 2026-07-22).** Hasta el 2026-08-04, el
WoW era el KPI principal del reporte. El usuario lo bajó a secundario cuando se adoptó la tendencia de
ventana móvil como protagonista — el WoW sigue imprimiéndose siempre (chico, sin negrita, coloreado según
signo) porque sigue siendo información real y útil, pero ya no es el número que se destaca primero.

**Contrato de escritura (pipeline multi-PM, 2026-08-15):** esta skill ya no escribe el canon directo — `wiki/3_recursos/datos/` es espejo read-only en este install. `pipeline.py ingest` siembra una copia de trabajo en `contexto_vivo/_staging_sync_metrics/` desde el espejo (mismo mecanismo, mismas rutas relativas, ver el docstring del script) y opera ahí exactamente igual que antes. Al cerrar la corrida, empaquetá esa carpeta como **un item `tipo: dato`** en `wiki/1_proyectos/contexto_vivo/`, `destino_propuesto: 3_recursos/datos/` — `/context_merge` lo aplica por copia byte a byte. El reporte narrado (`metricas_semanales.md`) y el hallazgo de la semana van como item `tipo: conocimiento` aparte (ver Paso de cierre).

**Store acumulado — fuente de verdad (espejo, solo lectura directa; la escritura pasa por el item de arriba):** `wiki/3_recursos/datos/datos_metricas_semanales/`
- `fact_operaciones.csv` · `fact_transacciones.csv` · `fact_cuentas.csv` · `fact_comercios.csv` ·
  `fact_transferencias_agente_cobro.csv`
- `dim_organizaciones.csv` · `dim_entidades.csv` · `dim_tipos_operacion.csv` · `dim_estados_operacion.csv` ·
  `dim_collectors.csv`
- `semanas.csv` — qué semanas hay, su corte y si están cerradas

Nunca hace falta releer un CSV histórico: una vez ingerida, la semana vive en el store para siempre.

**Por qué el store está en la wiki y no en `datasets_locales/`:** son agregados puros (cantidades y volúmenes
por dimensión de negocio), **sin una sola fila de PII**. La regla dura de
[`datasets/index.md`](../../../wiki/3_recursos/datos/index.md) sigue vigente para todo lo demás — pero no
aplica acá, y versionarlos en git da respaldo e historial. **Si alguna vez el PM manda un export con grano
de persona (cuenta, CUIT, email), ese archivo NO entra al store**: va a `datasets_locales/` y se registra
como dataset, no como métrica.

## 📐 Definición de las NSM (confirmada por el usuario, 2026-07-21; ampliada 2026-07-23)

### NSM #1 — Volumen operado por API BANK
**Dos fuentes fusionadas, ambas cursan contra la misma API BANK (Banco Industrial):**
1. Operaciones de Wallet: `TipoOperacionId ∈ {1, 2, 3, 6, 8, 14}` con `EstadoId = 2` (Aprobada).
2. Transferencias del producto **Agente de Cobros y Pagos** (entrantes CVU/CBU, salientes) con
   `Status = COMPLETED` (decisión del usuario, 2026-07-23 — ver más abajo).

Son las operaciones que **efectivamente se cursan contra la API del banco**.

| | Tipos |
|---|---|
| **OUT** | 1 Transferencia Saliente · 3 Pago con QR · 8 Transf. Pull Débito |
| **IN** | 2 Transferencia Entrante · 6 Transf. Pull Crédito · 14 Debin Recurrente Crédito |

> ⚠️ El opportunity tree de `north_star.md` agrupa "transferencias pull" entero bajo IN. **Pull Débito es
> OUT** (debita la cuenta de la wallet); solo Pull Crédito es IN. Manda esta definición.

**Palancas indirectas** (dólar CCL 9/10, cripto 11/12, Pago FX 16, QR Pix 15, CashIn tarjeta 13, internas
4/5, Viaje QR 7): **no suman a la NSM**, se reportan en bloque aparte. Alimentan el saldo que después opera
contra el banco — para comprar dólares alguien primero tuvo que transferirse la plata.

**Transferencias del producto Agente de Cobros y Pagos — SE SUMAN al total oficial de NSM#1 (decisión del
usuario, 2026-07-23, todo el histórico y hacia adelante).** Entrantes a CVU, entrantes a CBU y salientes se
procesan contra la **misma API BANK** que las Operaciones de Wallet — a diferencia de las palancas indirectas
de arriba, esto **mueve NSM#1 directamente**, no de forma indirecta. Vive en una tabla propia
(`Transferences` / `Collectors`, no `Operaciones`), por eso es un fact separado
(`transferencias_agente_cobro`) con su propia dimensión (`dim_collectors`, análoga a
`dim_organizaciones`/`dim_entidades`). `Datos.nsm1_oficial()` / `nsm1_oficial_out()` / `nsm1_oficial_in()` en
`pipeline.py` hacen la fusión con Operaciones; `Datos.nsm1()` (Operaciones-only, sin fusionar) se sigue
usando para el desglose "por tipo de operación" y el análisis por Organizacion, que no tienen equivalente en
la tabla de Collectors.

| Campo del export | Mapeo |
|---|---|
| `Type = TRANSFER` | Saliente (Agente de Cobro) — cuenta como OUT |
| `Type = transfer.cvu.received` | Entrante CVU — cuenta como IN |
| `Type = transfer.cbu.received` | Entrante CBU — cuenta como IN |
| `Type = NULL` | **Sin clasificar** (usuario, 2026-07-23: "debe ser un error, no sabemos qué es... igualmente suma al volumen de API BANK"). Suma al total oficial pero **no se le asigna IN ni OUT** — se reporta en un bucket "Sin clasificar" aparte. No se adivina a qué lado cae. |
| `Status = COMPLETED` | Único estado que suma volumen (confirmado por el usuario, 2026-07-23) |
| Cualquier otro `Status` (`FAILED`, `PENDING`, `UNKNOWN`, `CREDIT_ERROR`, `DATA_ERROR`, `IN_PROGRESS`, `NO_WARRANTY`) | No suma volumen — "no fue exitoso". Se miden como **anomalía** (tasa agregada + detalle por status individual), no como parte del negocio |

> ⚠️ **Es material, no un detalle menor.** En el backfill del 2026-07-23, esta palanca movió **$150.162 M en
> la última semana cerrada — más que la propia NSM#1 vía Operaciones ($147.326 M)**. Antes de esta fusión,
> NSM#1 estaba subestimada en un orden de magnitud comparable a su propio volumen. Cualquier lectura previa
> de "cuánto falta para top 2 en API BANK" hecha solo con Operaciones de Wallet quedó corta — ver el gap
> resuelto en `../../../wiki/2_areas/gaps_y_preguntas.md`.
> ⚠️ **`Type = NULL`** sigue sin explicación de origen — el usuario asume que es un bug/error de la fuente,
> pero confirmó que igual debe sumar al volumen. No se reclasifica por analogía si en el futuro aparece un
> patrón; cualquier ajuste a esa regla necesita una nueva confirmación del usuario.

### NSM #2 — Volumen operado con el gateway Payway
`TipoTransaccion ∈ {6 Botón Simple, 7 Botón 2.0}` **y** `FormadePago ∈ {10 Créd. Cuotas, 60 Prepaga,
80 Crédito, 90 Débito}` **y** `Estado = ACREDITADO`. Es el cobro **no presente** con tarjeta.

**Fuera de Payway hoy** (se reporta como contexto, no como NSM): 4 MPOS / POS presente — **ese proyecto
todavía no se shippeó**, cuando entre a Payway hay que sumarlo a la NSM —, 1 Transf. Entrante CVU,
2 Liquidador, 3 EcoCerrado, 9 Transferencia 3.0, 12 TAP2PHONE.

### Rechazos y devoluciones
**No suman al volumen.** Se miden aparte como salud: tasa de rechazo y de devolución, global y por medio de
pago. Un salto ahí suele ser un problema técnico o de procesador, no comercial.

### Baseline y objetivo
El valor de mercado (qué volumen hace falta para ser top 2 / top 6) **no se conoce todavía** — es el mismo
gap que documenta `north_star.md`. Hasta que el usuario lo aporte, la skill usa un **baseline interno**:
promedio de 13 semanas y máximo histórico. La fila "Objetivo" se reporta como **PENDIENTE**, nunca se inventa
un número.

## Paso 0 — Verificar insumos (si falta alguno, FRENÁ)

**Pedí siempre las 8 queries** (decisión del usuario, 2026-08-04) — los 5 hechos (operaciones, cuentas,
transacciones, comercios, transferencias Agente de Cobros) **y las 3 dimensiones** (Entidades,
Organizaciones, Collectors). Antes las dimensiones solo se pedían en la primera corrida o cuando aparecía
un Id desconocido; en la práctica siempre terminan haciendo falta (altas de organizaciones/entidades/
collectors nuevos son frecuentes), así que pedirlas de entrada ahorra una vuelta. Si el usuario ya las tiene
a mano de una corrida reciente, puede omitirlas — pero la skill nunca asume que no van a hacer falta.

Corré `inspect`. Si falta cualquiera de los **4 archivos de hechos core** (operaciones, cuentas,
transacciones, comercios) **en una corrida que ya trae alguno de los otros tres**, no escribas nada: pedile
al usuario que lo exporte y lo deje en `raw/`, **mostrándole la query exacta**, y esperá a que avise. Si
falta una dimensión, es `[WARN]` (no bloquea): el store ya tiene historia y los nombres siguen resolviendo,
pero avisá igual — a partir de esta decisión es un olvido, no el caso normal. Las tablas estables (tipos de
operación, estados, tipos de transacción, formas de pago) no cambian; si aparece un valor nuevo,
**preguntale al usuario qué significa antes de correr** — no lo deduzcas.

**La palanca de transferencias Agente de Cobros (`transferencias_agente_cobro`) es la excepción a la regla
de "todo o nada" entre los 5 hechos:** se pide y se mide todas las semanas igual que los 4 FACTS core, pero
si falta **no bloquea el `ingest`** de los demás — es una métrica complementaria a NSM#1, no una de las dos
NSM, y forzar su presencia impediría backfills o correcciones puntuales de esa sola tabla. Si falta en una
corrida que sí trae los 4 FACTS core, `inspect` avisa con un `[WARN]` (no un `[FALTA]`): preguntale al
usuario si se olvidó el export o si de verdad no hubo movimiento esa semana.

> ⚠️ **Corré la query un día que no sea lunes y vas a tener una ventana corrida.** Las 5 queries de hechos
> anclan `@FechaFin` al lunes de la semana en curso (`DATEADD(week, DATEDIFF(week,0,GETDATE()),0)`) — así
> da la semana ISO exacta corriéndola cualquier día. Si alguna vez ves una query vieja con
> `@FechaFin = CAST(GETDATE() AS DATE)`, es la versión rota (solo da la semana correcta corriéndola un
> lunes): corregila antes de pedirla. El pipeline igual aborta solo si detecta una ventana desalineada
> (`_validar_alineacion_iso` en `pipeline.py`, corrida desde `inspect` e `ingest`) — no confíes en que
> "si no avisa, está bien" reemplace este chequeo, pero tampoco hace falta pedirle al usuario que confirme
> el día: el guardarraíl ya lo cubre.

<details>
<summary><b>Queries a pedirle al usuario</b> (copiar tal cual)</summary>

**1) Operaciones (Wallet)** — si falta el archivo de operaciones:
```sql
-- 1. Definimos dinámicamente las fechas de corte
DECLARE @FechaFin DATETIME = DATEADD(week, DATEDIFF(week, 0, GETDATE()), 0); -- Lunes de la semana en curso (funciona cualquier día)
DECLARE @FechaInicio DATETIME = DATEADD(day, -7, @FechaFin); -- Lunes pasado a las 00:00:00

-- 2. Generamos el ID de semana (Formato YYYYWW -> Ej: 202415)
DECLARE @SemanaId INT = (YEAR(@FechaInicio) * 100) + DATEPART(iso_week, @FechaInicio);

-- 3. Consulta de agrupación con EstadoId
SELECT
    @SemanaId AS SemanaId,
    @FechaInicio AS FechaInicioCorte,
    @FechaFin AS FechaFinCorte,
    OrganizacionId,
    TipoOperacionId,
    EstadoId,
    COUNT(*) AS Cantidad,
    SUM(Importe) AS Volumen
FROM [dbo].[Operaciones]
WHERE FechaCreacion >= @FechaInicio
  AND FechaCreacion < @FechaFin
GROUP BY OrganizacionId, TipoOperacionId, EstadoId
ORDER BY OrganizacionId, TipoOperacionId, EstadoId;
```

**2) Cuentas (altas de Wallet)** — si falta el archivo de cuentas:
```sql
DECLARE @FechaFin DATETIME = DATEADD(week, DATEDIFF(week, 0, GETDATE()), 0); -- Lunes de la semana en curso
DECLARE @FechaInicio DATETIME = DATEADD(day, -7, @FechaFin);
DECLARE @SemanaId INT = (YEAR(@FechaInicio) * 100) + DATEPART(iso_week, @FechaInicio);

SELECT
    @SemanaId AS SemanaId,
    @FechaInicio AS FechaInicioCorte,
    @FechaFin AS FechaFinCorte,
    OrganizacionId,
    COUNT(*) AS Cantidad
FROM [dbo].[Cuentas]
WHERE FechaAlta >= @FechaInicio AND FechaAlta < @FechaFin
GROUP BY OrganizacionId
ORDER BY OrganizacionId;
```

**3) Transacciones (Adquirencia)** — si falta el archivo de transacciones:
```sql
DECLARE @FechaFin DATETIME = DATEADD(week, DATEDIFF(week, 0, GETDATE()), 0); -- Lunes de la semana en curso
DECLARE @FechaInicio DATETIME = DATEADD(day, -7, @FechaFin);
DECLARE @SemanaId INT = (YEAR(@FechaInicio) * 100) + DATEPART(iso_week, @FechaInicio);

SELECT
    @SemanaId AS SemanaId,
    @FechaInicio AS FechaInicioCorte,
    @FechaFin AS FechaFinCorte,
    EntidadIdentificador,
    TipoTransaccion,
    FormadePago,
    Estado,
    COUNT(*) AS Cantidad,
    SUM(ImporteBruto) AS Volumen
FROM [dbo].[Transaccion]
WHERE FechaProceso >= @FechaInicio AND FechaProceso < @FechaFin
GROUP BY EntidadIdentificador, TipoTransaccion, FormadePago, Estado
ORDER BY EntidadIdentificador, TipoTransaccion, FormadePago, Estado;
```

**4) Comercios (altas de Adquirencia)** — si falta el archivo de comercios:
```sql
DECLARE @FechaFin DATETIME = DATEADD(week, DATEDIFF(week, 0, GETDATE()), 0); -- Lunes de la semana en curso
DECLARE @FechaInicio DATETIME = DATEADD(day, -7, @FechaFin);
DECLARE @SemanaId INT = (YEAR(@FechaInicio) * 100) + DATEPART(iso_week, @FechaInicio);

SELECT
    @SemanaId AS SemanaId,
    @FechaInicio AS FechaInicioCorte,
    @FechaFin AS FechaFinCorte,
    EntidadId,
    COUNT(*) AS Cantidad
FROM [dbo].[Comercios]
WHERE FechaAlta >= @FechaInicio AND FechaAlta < @FechaFin
GROUP BY EntidadId
ORDER BY EntidadId;
```

**5) Entidades** (dimensión, solo si falta o hay Ids nuevos): `SELECT * FROM Entidad`

**6) Organizaciones** (dimensión, solo si falta o hay Ids nuevos): `SELECT * FROM Organizacion`

**7) Transferencias Agente de Cobros y Pagos** — palanca directa adicional a NSM#1 (no bloquea el ingest
si falta, ver arriba):
```sql
-- 1. Definimos las fechas de corte (Últimos 7 días)
DECLARE @FechaFin DATETIME = DATEADD(week, DATEDIFF(week, 0, GETDATE()), 0); -- Lunes de la semana en curso (funciona cualquier día)
DECLARE @FechaInicio DATETIME = DATEADD(day, -7, @FechaFin); -- Lunes anterior a las 00:00:00

-- 2. ID de la semana (YYYYWW)
DECLARE @SemanaId INT = (YEAR(@FechaInicio) * 100) + DATEPART(iso_week, @FechaInicio);

-- 3. Agrupación semanal
SELECT
    @SemanaId AS SemanaId,
    @FechaInicio AS FechaInicioCorte,
    @FechaFin AS FechaFinCorte,
    [Type],
    CollectorId,
    [Status],
    COUNT(*) AS Cantidad,
    SUM(ChargeAmount) AS Volumen
FROM [dbo].[Transferences]
WHERE Created >= @FechaInicio
  AND Created < @FechaFin
GROUP BY [Type], CollectorId, [Status]
ORDER BY [Type], CollectorId, [Status];
```

**8) Collectors** (dimensión, solo si falta o hay CollectorId nuevos): `SELECT * FROM [dbo].[Collectors]`

</details>

## Paso 1 — Inspección previa (obligatoria antes de escribir)

```
python .claude/skills/sync_metrics/scripts/pipeline.py inspect
```

Detecta cada CSV **por firma de header** (no por nombre: el PM parte y renombra los archivos), y reporta:

- Recursos y semanas del lote, con `[PARCIAL]` para las semanas todavía abiertas.
- `[SPLIT]` — filas que llegaron partidas entre archivos y se **suman** (ver gotchas).
- `[OVERLAP]` — semanas que ya están en el store y se van a pisar. Normal en un backfill o una corrección;
  sospechoso si el PM subió la semana de siempre y aparecen meses viejos: preguntá antes de seguir.
- `[WARN]` — Ids fuera de dimensión, huecos en la serie histórica, archivos duplicados.
- `[ABORT]` — un archivo que no matchea ninguna firma. **No inventes el mapeo**: registralo en
  `../../../wiki/2_areas/gaps_y_preguntas.md` y consultá al usuario antes de tocar `RESOURCES` en `pipeline.py`.

## Paso 2 — Ingesta

```
python .claude/skills/sync_metrics/scripts/pipeline.py ingest
```

Mergea contra el store y actualiza `semanas.csv` y `log_metricas_semanales.md`.

## Paso 3 — Análisis

```
python .claude/skills/sync_metrics/scripts/pipeline.py analyze [SemanaId]
```

Sin argumento usa la última semana cerrada. Imprime, en este orden: detalle semanal (WoW) de las dos NSM,
su composición y desgloses; la sección **Palancas** (Tendencia de ventana móvil como protagonista + WoW
como dato secundario, cada una atada a su NSM — ver abajo); salud, altas; **TENDENCIA — ventana móvil**
de las dos NSM y serie mensual completa (contexto histórico); y los **candidatos a hallazgo**.

**Tendencia de ventana móvil — protagonista (reemplaza al "MoM" mensual-calendario, decisión del usuario,
2026-08-04).** `bloque_movil()` en `pipeline.py` compara las últimas `VENTANA_TENDENCIA` (4) semanas
cerradas contra las 4 inmediatamente anteriores — **sin nombre de mes, sin relación a calendario**. La
vista mensual anterior (`bloque_mensual`, comparación por tramo de hasta 4 semanas etiquetada "julio" vs.
"junio") se retiró como protagonista porque mezclaba mal la etiqueta (mes calendario) con el cálculo real
(un tramo capado): en un mes de 5 semanas ISO el número quedaba "congelado" varias semanas seguidas, y
alguien que no conociera el detalle (el CEO, por ejemplo) podía leer la cifra como un cierre contable
exacto del mes, cuando no lo era. La ventana móvil se actualiza **todas** las semanas y no se confunde con
un cierre mensual porque no lleva nombre de mes. **El email y el reporte llevan una nota de metodología
explícita** en un lugar visible (antes de cualquier número) para dejar esto claro — ver Paso 4.
`bloque_mensual` no se eliminó: sigue alimentando la "serie mensual completa" del anexo (mes completo vs.
mes completo, magnitud absoluta histórica, contexto — no la base de la tendencia).

**WoW — dato secundario (revierte la decisión del 2026-07-22, que lo tenía como KPI principal).** Sigue
imprimiéndose siempre, coloreado según signo, pero chico y sin negrita — subordinado visualmente a la
tendencia de ventana móvil.

**Palancas — cada una atada a su NSM, un renglón por palanca (usuario, 2026-08-04, iterado en 9 rondas de
diseño).** Todo lo que antes eran líneas de texto sueltas con solo volumen y WoW —componentes de NSM#1
(Wallet/TAC), IN/OUT, tipos de operación de Wallet, tipos de TAC, canales y formas de pago de NSM#2,
indirectas de NSM#1, fuera de Payway— ahora lleva **Tendencia de ventana móvil** (protagonista, con el
valor de la ventana previa como referencia) **y WoW** (secundario, solo el %), igual que las NSM. Suma
además dos **leading indicators**: altas de cuentas de Wallet (para NSM#1) y altas de comercios de
Adquirencia (para NSM#2) — no suman volumen, pero su crecimiento antecede al de la NSM correspondiente;
se formatean como cantidad entera, no como pesos (`p["formato"] == "entero"`). La fuente es
`registro_palancas()` + `medir_palancas()` en `pipeline.py` (ver "Mecánica" arriba): se mide una sola vez
y de ahí comen el desglose de `analyze`, los detectores y el JSON de `palancas`.

**El script detecta; vos interpretás.** Los candidatos son señales estadísticas, no conclusiones. Tu trabajo
es: descartar los que son ruido conocido, cruzarlos con lo que ya sabe la wiki (`2_areas/direccion/`,
`1_proyectos/`, `4_archivos/` — postmortems, salidas de clientes, releases) y convertirlos en 3 a 6 hallazgos
con lectura de negocio. **Si un movimiento no tiene explicación en la wiki, no inventes la causa**:
registrá la pregunta en `../../../wiki/2_areas/gaps_y_preguntas.md` y planteásela al usuario.

**El texto del hallazgo es para gente de negocio ajena al Cerebro — nunca menciones la infraestructura
interna (decisión del usuario, 2026-08-05).** Los que reciben el reporte/email (el CEO, gerencia, otras
áreas) no saben qué es "la wiki", "../../../wiki/2_areas/gaps_y_preguntas.md", "estado_actual.md" ni ningún otro artefacto de
este segundo cerebro — para ellos esos nombres son ruido sin sentido. El *título* y el *texto* de cada
hallazgo tienen que leerse como si los escribiera un analista de negocio, sin una sola referencia a
archivos, carpetas o mecánica interna:
- ❌ "...no se puede confirmar — registrado en ../../../wiki/2_areas/gaps_y_preguntas.md."
- ✅ "...no se puede confirmar. Vale la pena chequearlo con Comercial."
- ❌ "...documentados en estado_actual.md."
- ✅ "...ya identificados como los clientes que más pesan en el volumen."
- ❌ "...sin ficha en la wiki."
- ✅ "...sin contexto disponible sobre este cliente todavía."

Esto **no cambia el protocolo interno**: la pregunta sin resolver se sigue registrando en
`../../../wiki/2_areas/gaps_y_preguntas.md` como siempre (Paso 5) — nada más que el texto que ve el lector no debe decir dónde
quedó anotada. Pensalo como dos capas separadas: la interna (para vos y el usuario, en la wiki) y la
externa (para quien recibe el reporte, en lenguaje de negocio puro). Aplica al email, a los hallazgos de
la wiki y a cualquier otro texto que un tercero pueda llegar a leer.

**Nombrar siempre la entidad detrás de un hallazgo puntual, nunca dejarlo en genérico (usuario,
2026-08-12).** Si un hallazgo describe un movimiento concentrado en un caso puntual — un cliente, una
organización, un collector — el título y el texto tienen que nombrarlo explícitamente cuando el dato está
disponible, cruzando con `dim_entidades.csv`/`dim_organizaciones.csv`/`dim_collectors.csv`. Nunca "un solo
cliente", "una cuenta puntual", "ese cliente": el nombre real (ej. "La Virginia", "BSF", "Bind PSP
liquidaciones cta 39"). Esto **no contradice** la regla de arriba de no mencionar infraestructura interna
del Cerebro — nombrar un cliente o una cuenta real es información de negocio que el lector necesita para
actuar, no jerga de archivos/carpetas. Aplica a los tres lugares donde vive el texto de un hallazgo: el
título y cuerpo en `metricas_semanales.md`, el JSON de `hallazgos.json` que alimenta el email, y por lo
tanto el email renderizado — si se corrige uno hay que corregir los tres para que no queden desalineados
entre sí (pasó en la corrida del 2026-08-12: la wiki ya nombraba las entidades pero el email seguía en
genérico, tuvo que reconciliarse a mano).

**Estacionalidad (usuario, 2026-08-04):** antes de mandar un movimiento sin explicar a
`../../../wiki/2_areas/gaps_y_preguntas.md`, cruzalo contra
[`2_areas/direccion/estacionalidad_metricas.md`](../../../wiki/2_areas/direccion/estacionalidad_metricas.md) —
calendario de negocio (no estadística) con patrones confirmados por el usuario: días 1-10 del mes = pico de
cobro de servicios/facturas en NSM#2 (fuerte) y en NSM#1/Wallet (más débil, no asumir sin verificar caso a
caso); feriados nacionales AR = caída esperable de volumen (verificar el calendario vigente del año, las
fechas cambian); fechas comerciales (Hot Sale, Cyber Monday) = picos en NSM#2, fecha exacta variable por
edición. Un patrón de ese archivo solo se cita si la semana realmente cae dentro de su ventana — no lo
asumas por parecido. Esto reduce falsos gaps, no reemplaza el criterio: si el movimiento no cae en ninguna
ventana conocida, sigue yendo a `../../../wiki/2_areas/gaps_y_preguntas.md` como siempre. Cuando confirmes con el usuario un
patrón estacional nuevo (o el detalle fino de uno existente, ej. qué palanca de Wallet sí tiene
estacionalidad), sumalo a ese archivo para las corridas futuras.

Detectores implementados: cambio de nivel (z-score vs 8 semanas) y tendencia (regresión 6 semanas) sobre
**TODO** `registro_palancas()` — las dos NSM, sus componentes (Wallet/TAC), el núcleo (tipos de operación,
tipos de TAC, IN/OUT, canales y formas de pago de NSM#2) y las palancas de contexto (indirectas de NSM#1,
fuera de Payway) — vía `_detectar_palancas` en `pipeline.py`; más mix shift (IN/OUT, Botón Simple↔2.0,
medio de pago), churn y caída de cliente, activación, concentración (top-1 y top-3), calidad (rechazos y
devoluciones, global y por medio de pago), y altas de cuentas de Wallet y de comercios de Adquirencia
(z-score, mediana robusta y deriva estructural de 13 semanas — mismo peso para las dos, ninguna es
"secundaria" de la otra).

**Piso de materialidad por categoría (`_piso_de` en `pipeline.py`), no un número único**: 0,1%
(`PISO_PALANCA_CORE`) del volumen típico de su NSM de referencia para las palancas que SUMAN al total (si
se mueven, la NSM se movió, así que son materiales por construcción aunque sean chicas); 0,5%
(`PISO_PALANCA_SECUNDARIA`) para las de contexto, que no forman parte del número reportado; sin piso para
las dos NSM y sus 2 componentes (Wallet/TAC). Antes del 2026-08-04 solo las dos NSM y el componente TAC
tenían detector — los 6 tipos de operación de Wallet, los 3 tipos de TAC, los 2 canales y las 4 formas de
pago de NSM#2 no tenían ninguno.

**Monitoreo total, reporte selectivo (decisión del usuario, 2026-07-27).** El pipeline corre el detector de
nivel/tendencia sobre *todas* las palancas del registro en cada `analyze`, no solo sobre las dos NSM — pero
el reporte y el email **no listan cada palanca todas las semanas**. Si una palanca no tiene nada raro, no
aparece: el silencio es la respuesta esperada. Solo se convierte en hallazgo (y entra al reporte/email) si
el candidato es material y sobrevive tu criterio editorial, igual que cualquier otro candidato de esta lista.

## Paso 4 — Reporte incremental + email

**Reporte → item `tipo: dato` en `contexto_vivo/`** (mismo mecanismo que el store: es contenido acumulado, se aplica por copia), `destino_propuesto: 3_recursos/datos/metricas_semanales.md`. Redactá la entrada nueva **antepuesta** al contenido actual del espejo — el histórico se conserva íntegro debajo, el item lleva el archivo completo resultante, no solo el delta. Estructura fija de cada entrada:

1. **Estado de las NSM** — WoW con el valor de comparación anterior, vs baseline 13 semanas, vs máximo
   histórico, tendencia de regresión de 6 semanas (tabla 1a, sin cambios). La vista mensual por tramo
   (antes "1b · MoM") se reemplazó por la **tendencia de ventana móvil** (Paso 3) en el cuerpo del reporte;
   la wiki también conserva la serie mensual completa (mes completo vs. mes completo) como anexo histórico.
2. **Composición de NSM#1** (Operaciones de Wallet vs. Transferencias Agente de Cobros, con su propio
   desglose entrante/saliente y top collectors) y **Palancas — árbol jerárquico por NSM** (Tendencia móvil
   protagonista + WoW secundario en un solo renglón por palanca; las que suman al total primero, las de
   contexto —indirectas / fuera de Payway / leading indicators— después).
3. **Hallazgos y puntos más importantes de la semana** — 3 a 6, priorizados por severidad, cada uno con
   *qué pasó · magnitud · por qué importa · qué mirar o hacer*.
4. **Anexo de soporte** — altas, tasas de rechazo y devolución, ticket promedio, top movers, y la **serie
   mensual completa (mes completo vs. mes completo)** para ver magnitud absoluta. Solo en la wiki.

**Flujo de generación (2026-08-04, rediseño iterado en 9 rondas con el usuario):**
```
python .claude/skills/sync_metrics/scripts/pipeline.py palancas [SemanaId] > <scratch>/palancas.json
# Escribí <scratch>/hallazgos.json con tu lectura de negocio (3 a 6 items, priorizados):
#   [{"severidad": "Alta", "tipo": "...", "titulo": "...", "texto": "...", "palanca_id": "nsm1_tac" | null}]
python .claude/skills/sync_metrics/scripts/render_email.py <scratch>/palancas.json <scratch>/hallazgos.json --email > <scratch>/email.html
python .claude/skills/sync_metrics/scripts/render_email.py <scratch>/palancas.json <scratch>/hallazgos.json --md > <scratch>/tablas.md
```
`render_email.py` **no calcula nada de negocio** — arma el email de "el pipeline mide, Claude interpreta,
el renderer maqueta". Diseño final:
- **Cards SOLO para las dos NSM raíz**, tituladas con su significado completo — "NSM#1: Volumen en API
  Bank" / "NSM#2: Volumen en Payway" (nadie recuerda qué es "NSM1" a secas). Headline: "últimas 4 semanas
  cerradas" (NO acumulado de mes calendario), con la tendencia móvil protagonista y el WoW chico abajo.
- **El resto de las palancas va como árbol jerárquico** (viñetas + indentación por nivel de negocio, no
  cards individuales) — mucho más compacto para leer de un vistazo. La jerarquía core (qué cuelga de qué)
  está **hardcodeada** en `ARBOL_CORE_NSM1`/`ARBOL_CORE_NSM2` de `render_email.py` porque no se puede
  derivar genéricamente del campo `padre` del JSON (ver gotcha abajo) — si se agrega un tipo nuevo a
  `NSM1_TIPOS`/`TAC_TIPOS`/`NSM2_TIPOS`/`NSM2_FORMAS` en `pipeline.py`, hay que sumarlo también ahí.
- **Cada palanca del árbol es un solo renglón**, con dos columnas de **ancho fijo** al final —
  WoW (angosta, texto justificado a la **izquierda** de su columna) y Tendencia (más ancha, también
  justificada a la **izquierda** de su columna, NO a la derecha) — así todas las flechitas de tendencia
  quedan alineadas verticalmente entre renglones, sin importar el nivel de indentación ni el largo del
  nombre. Decisión visual explícita del usuario, iterada dos veces (primero probamos justificado a la
  derecha, no le gustó — ver historial de decisiones).
- **Nota de metodología visible arriba de todo**, antes de cualquier número: explica qué es "Tendencia"
  (ventana móvil de 4 semanas) y aclara que no es un cierre mensual — mitiga el riesgo de que el CEO u
  otro lector lea el número como una cifra de facturación exacta.
- Paleta: azul para NSM#1, violeta para NSM#2 (cards), verde/rojo semántico según signo en WoW y
  Tendencia por igual. `<table>` anidadas + CSS inline (sin flex/grid, sin imágenes externas, sin JS, sin
  `<details>` — mismas restricciones de Gmail/Outlook de siempre).

**Email:** pegá el HTML de `email.html` y creá el borrador con el conector de Gmail (`create_draft` para
uno nuevo, `update_draft` con el `draftId` si ya existe uno de la misma semana — **pasale el HTML real
generado por el script, nunca una sustitución de shell tipo `$(cat archivo)` como valor del parámetro**:
las tool calls no son un shell, ese texto se manda literal y rompe el draft).

> ⚠️ **El conector de Gmail no puede enviar, solo dejar el borrador.** Avisale al usuario que quedó listo
> para revisar y mandar con un click. No intentes enviarlo por otra vía.
> ⚠️ **Carga de tools:** el prefijo hash del conector varía entre sesiones — si falla por nombre,
> `ToolSearch query:"gmail draft"` (keyword, no `select:`).
> ⚠️ **Verificá que el borrador existe de verdad — `create_draft`/`update_draft` pueden devolver un ID sin
> error aunque el borrador nunca haya persistido.** Pasó en la corrida del 2026-08-05: `create_draft`
> devolvió un `id` válido, y varias llamadas a `update_draft` sobre ese mismo `id` "funcionaron" sin error
> — pero el borrador nunca apareció en la bandeja del usuario ni en `list_drafts`. Después de crear (o
> actualizar) el borrador, confirmá con `list_drafts` (`query: 'subject:"..."'` con el asunto exacto) que
> aparece en la lista antes de decirle al usuario que ya está listo. Si no aparece, no reintentes
> `update_draft` sobre el mismo ID — creá uno nuevo con `create_draft`.

## Paso 5 — Protocolos de control del CLAUDE.md

Todo lo de acá nace como item en `wiki/1_proyectos/contexto_vivo/` (nunca directo). **Todo item que crees en esta corrida — el store y el reporte del Paso 4 incluidos, no solo gaps/decisiones/oportunidades — nace con `estado: capturado`, nunca `en_cola` ni `ingestado`.** Ese campo lo actualiza `/context_push` cuando efectivamente sube el item al core, no vos: escribirlo ya en `en_cola` deja el item con un estado que miente sobre dónde vive de verdad (ver gotcha al final del archivo — pasó el 2026-08-26 y quedó 5 items "fantasma" hasta que se detectó en un `/context_pull` posterior).

1. **Gaps** → `tipo: gap`, `destino_propuesto: 2_areas/gaps_y_preguntas.md`: todo `[WARN]` sin resolver, todo movimiento sin explicación, todo valor de dimensión desconocido. Y preguntáselos al usuario explícitamente al cerrar tu turno.
2. **Decisiones** → `tipo: decision`, `destino_propuesto: 2_areas/direccion/decisiones.md`: si el usuario define algo al revisar el reporte (cambia el scope de una NSM, fija un objetivo, descarta una métrica).
3. **Oportunidades** → `tipo: oportunidad`, `destino_propuesto: 2_areas/direccion/oportunidades.md`: si el análisis destapa una candidata a IDEA (un segmento creciendo solo, un producto con rechazo estructural, un cliente pidiendo capacidad).
4. **Tareas** → `wiki/1_proyectos/tareas.md` (personal, **directo**, dedupe primero). Si es de interés de todo el equipo, sumá además un item `tipo: tarea_equipo`.

## Paso 6 — Rotación de `raw/` (obligatoria)

Mover los CSV procesados a `wiki/4_archivos/historial_raw/YYYY-MM_metricas_semanales_<SemanaId>/` y
confirmar en el reporte final que `raw/` quedó vacía.

## Paso 7 — Cierre

Regenerá `contexto_vivo/index.md` con los items nuevos (el del store `tipo: dato`, el del reporte `tipo: dato`, y los de gaps/decisiones/oportunidades si aplicaron). **Sin índices de `2_areas/`/`3_recursos/`** (los actualiza `/context_merge`) y **sin git** — el commit del repo personal lo hace el hook `SessionStart` una vez al día.

## ⚠️ Gotchas conocidos

- **Exports partidos que cortan una semana al medio (el gotcha central).** Cuando la query no entra en una
  sola corrida, el PM la parte en varios archivos cortando **por fecha, no por semana** — así que la semana
  del borde llega en dos pedazos, en dos archivos distintos, con cantidades complementarias. Verificado en el
  backfill del 2026-07-21: las semanas 202601 y 202610 aparecían en dos archivos cada una. Por eso
  `agregar_lote()` **suma** las filas repetidas dentro de un mismo lote, mientras que el merge contra el
  store **reemplaza** (ahí un combo repetido es una reingesta o una corrección de la misma semana). Si esto
  se invirtiera, se perdería medio volumen de las semanas borde sin que nada falle a la vista.
- **Archivo duplicado en `raw/`.** Como el lote se suma, dejar el mismo export dos veces duplicaría el
  volumen. El pipeline descarta archivos byte-a-byte idénticos (hash) y avisa. Un export del mismo período
  con contenido *distinto* (una corrección) no lo detecta el hash: eso lo tenés que ver en el `[OVERLAP]`.
- **Semanas parciales.** El export tomado a mitad de semana trae la semana en curso incompleta (en el
  backfill, 202630 con un solo día: $6.736 M contra ~$147.000 M de una semana normal). Se guardan con
  `Completa=0` y quedan **excluidas de todo cálculo** hasta que llegue el export completo, que las pisa. No
  las borres del store: sirven para saber que ya se vio ese corte.
- **Transferencias internas se cuentan dos veces por diseño.** Los tipos 4 y 5 (interna saliente/entrante)
  son las dos patas de la misma operación y dan siempre el mismo volumen. No suman a la NSM, pero si alguna
  vez se los reporta juntos, aclarar que no se suman entre sí.
- **Transferencias Pull en cero desde el incidente de marzo 2026.** Los tipos 6 y 8 aparecen en $0 — es
  consistente con el [postmortem](../../../wiki/4_archivos/postmortem_transferencias_pull_marzo_2026.md), no
  es un bug de la ingesta. Siguen en la definición de la NSM porque el día que se reactiven tienen que sumar
  solos.
- **`FormadePago = 70` y `Estado = REALIZADA`** aparecieron en el backfill con 2 filas cada uno y **no están
  en las tablas de referencia del usuario**. Quedan registrados en `../../../wiki/2_areas/gaps_y_preguntas.md`. Son marginales
  (no mueven ninguna NSM), pero no los mapees por analogía: preguntá.
- **`EntidadIdentificador` ≠ `EntidadId`.** Las transacciones se joinean por `Entidad.Codigo` (valores tipo
  `A130`, `N`, `VIRG`, `6`); los comercios por `Entidad.Id` (numérico). Son dos claves distintas de la misma
  tabla — no las confundas al leer el store a mano.
- **Piso de materialidad en los hallazgos de cliente.** Sin él, cada semana escupe una decena de "caídas del
  99%" de organizaciones de test. `PISO_MATERIALIDAD` (0,1% del volumen típico) filtra el ruido y
  `MATERIAL_ALTA` (2%) decide la severidad. Si el usuario pide ver clientes más chicos, bajá el piso — no
  saques el filtro.
- **z-score ciego a los outliers.** Un pico aislado en la ventana de 8 semanas infla el desvío y esconde
  caídas posteriores. Por eso los detectores de altas suman una comparación contra la **mediana** y una
  **deriva de 13 semanas** — así se vio la caída estructural de altas de comercios (-65,8%) que el z-score
  no marcaba.
- **El WoW es el KPI principal; el MoM es contexto adicional — no al revés.** Primera versión de la skill
  (2026-07-21/22 temprano) puso el mensual primero y el semanal como "soporte" colapsado; el usuario corrigió
  (2026-07-22): "qué pasó la última semana" es el foco principal y el más cercano, y tiene que ir primero y
  sin colapsar, en la wiki y en el email. El mensual se agrega **además**, nunca en reemplazo.
- **MoM nunca compara mes completo contra mes completo — siempre el mismo tramo de semanas.** Si julio lleva
  3 semanas cerradas, se compara esa suma contra la suma de las **primeras 3 semanas** de junio (no contra
  junio completo, que tiene 4). Esto es válido tanto si el mes actual está en curso como si ya cerró —
  simplifica el código: no hace falta distinguir "mes cerrado" de "mes parcial", `bloque_mensual()` siempre
  usa `k = min(TRAMO_MAX, semanas del mes actual)` y recorta todo (mes actual, mes anterior, baseline de 3
  meses, máximo histórico) al mismo `k`. **`TRAMO_MAX = 4`** es la simplificación explícita del usuario
  ("1 mes = 4 semanas"), aunque el calendario real a veces le asigne una quinta semana a un mes.
- **La "serie mensual completa" del anexo usa mes completo, no tramo — es una tabla distinta con un propósito
  distinto.** Sirve para ver la magnitud absoluta de cada mes (ahí se apoyó el hallazgo de Astropay, que
  necesitaba los totales reales de enero/mayo, no un recorte de 3-4 semanas). No confundir su columna "MoM"
  con el KPI de MoM de la vista principal — están etiquetadas distinto a propósito.
- **`Fuentes` en `semanas.csv` ACUMULA entre corridas, nunca se reemplaza (bug real, corregido el
  2026-07-23).** La primera versión de la lógica de "Semanas" en `cmd_ingest` reescribía `sem[s]["fuentes"]`
  solo con los recursos presentes en **esa** corrida — al ingerir el backfill de
  `transferencias_agente_cobro` (que no traía `operaciones`/`transacciones`, ya en el store de una corrida
  anterior) esto **le borró `Completa=1` a las 30 semanas** que se cruzaban con el nuevo lote, dejándolas en
  `Completa=0` con `Fuentes=transferencias_agente_cobro` a secas. Se detectó de inmediato porque el
  `ingest` mostró "17 completas" cuando debían ser ~46, y se corrigió restaurando `semanas.csv` desde git
  (estaba trackeado, sin pérdida) y arreglando `cmd_ingest` para que la completitud de una semana se calcule
  sobre la **unión** de `Fuentes` históricas + las de la corrida actual, no solo estas últimas. Si algún día
  se toca esa sección de nuevo: cualquier ingest que no traiga todos los FACTS de siempre (algo ahora posible
  a propósito, ver la palanca TAC) tiene que **acumular** `Fuentes`, no pisarlas.
- **La palanca de transferencias Agente de Cobros se backfilleó limpia por semana, sin el gotcha de los
  exports cortados a la mitad.** A diferencia del backfill original de operaciones/transacciones (que
  partía una semana al medio entre dos archivos), el backfill del 2026-07-23 vino con rango disjunto:
  archivo 1 = semanas 202601-202609, archivo 2 = 202610-202630, sin solapamiento. No hubo `[SPLIT]`. No
  asumas que esto se repite — si un futuro export de esta tabla sí corta una semana al medio, `agregar_lote`
  ya la suma igual que a los demás FACTS (mismo mecanismo genérico).
- **Un mes se asigna por el jueves, no por el primer día** (solo para la ETIQUETA, no para la comparación).
  `mes_de()` usa `FechaInicio + 3 días` (lunes de la semana + 3 = jueves) para decidir a qué mes calendario
  pertenece cada semana ISO — así una semana que arranca el 29 de junio pero cuyo jueves cae en julio (como
  la 202627 del backfill) queda del lado de julio, igual que ISO asigna semana→año. Verificado contra el
  backfill: la suma de los 11 meses (mes completo) coincide centavo a centavo con la suma de las 46 semanas.
- **El objetivo de las NSM sigue sin dato de mercado.** El usuario confirmó (2026-07-22) que ese valor va a
  venir expresado en **volumen mensual**. Cuando lo aporte, cargalo en `bloque_mensual()` y reemplazá la fila
  "PENDIENTE" por el % de avance real (probablemente comparando contra el tramo/mes acumulado, no contra el
  mes completo, para ser consistente con el resto del bloque). Hasta entonces, todo % es contra baseline
  interno y hay que decirlo así en el reporte.
- **`analyze <SemanaId>` respeta el corte histórico también para la vista mensual.** `bloque_mensual()` recibe
  el scope de semanas ya recortado a `d.semanas[:i+1]` (no todo el store) — si algún día se vuelve a tocar
  esta función, no pasarle `d.semanas` completo de nuevo, o un `analyze` de una semana vieja mostraría meses
  que en ese momento todavía no habían pasado.
- **Las palancas necesitan su propio piso de materialidad, distinto al de clientes (`PISO_MATERIALIDAD`).**
  Ese piso se calcula sobre el volumen típico del *cliente individual* dentro de una NSM; las palancas
  necesitan uno sobre el volumen típico de la *palanca completa* dentro de su NSM de referencia
  (`_piso_de()` en `pipeline.py`: 0,1% para las que suman al total, 0,5% para las de contexto), o ramas
  casi en cero (ej. "Compra Dólar CCL" con $0,03 M) generan z-scores gigantes de puro ruido en base chica —
  no es una caída real, es que $30.000 vs. $12.000 ya es "+150%". Si algún día se ajusta este piso, probarlo
  contra una semana con ramas chicas (202630 tiene varias) antes de asumir que el umbral nuevo no vuelve a
  inundar de ruido. *(Hasta el 2026-08-04 esta lógica vivía solo en `_palancas_secundarias`, que cubría
  únicamente las palancas de contexto; se unificó en `_detectar_palancas` para cubrir también el núcleo de
  las dos NSM — ver el registro de palancas más abajo.)*
- **El registro de palancas evita el doble conteo agrupando por `eje`, no confíes en `suma=True` solo.**
  `canal_nsm2` y `medio_pago_nsm2` son DOS particiones independientes del mismo total de NSM#2 (cada una
  suma el 100% por su cuenta); lo mismo `componente_nsm1` (Wallet vs. TAC) vs. `split_in_out` vs.
  `sin_clasificar+lado` para NSM#1. Sumar "todas las palancas con `suma=True`" de una NSM sin agrupar por
  `eje` cuenta el volumen dos (o más) veces. Verificado: la suma de cada `eje` coincide al centavo con el
  volumen de su `padre` (`python pipeline.py palancas | python -m json.tool` + chequeo manual).
- **`padre` de una palanca no siempre es su NSM.** Los tipos de operación de Wallet se reportan como % de
  "Operaciones (Wallet)" (no del total oficial fusionado de NSM#1) y los tipos de TAC como % de
  "Transferencias Agente de Cobros" — así está impreso desde el 2026-07-23 y el usuario lee esos % como
  "composición de esta fuente", no "peso sobre la NSM". No lo cambies sin preguntarle.
- **La ventana ISO se corre si la query no se corre un lunes — y el pipeline aborta, no avisa y sigue.**
  Verificado en la corrida del 2026-08-04 (martes): con el `@FechaFin = CAST(GETDATE() AS DATE)` viejo, el
  export de SemanaId=202631 trajo la ventana 2026-07-28→2026-08-04 en vez de la real 2026-07-27→2026-08-03
  — faltaba el lunes 27 y sobraba el lunes 3 de agosto (de la semana siguiente). Como el export ya viene
  agregado (SUM/COUNT), no hay grano diario para corregirlo en el pipeline: la corrección es en el origen
  (`@FechaFin = DATEADD(week, DATEDIFF(week,0,GETDATE()),0)`, ver Paso 0). `_validar_alineacion_iso()` en
  `pipeline.py` corre en `inspect` e `ingest` y aborta (no solo avisa) porque el costo de dejarlo pasar es
  alto: corrompe la serie en silencio y garantiza doble conteo del día que sobra en la corrida siguiente.
- **El borde de año de `@SemanaId` es un riesgo preexistente, no introducido por el fix de la ventana ISO.**
  `@SemanaId = YEAR(@FechaInicio)*100 + DATEPART(iso_week, @FechaInicio)` puede desalinearse en la última
  semana de diciembre / primera de enero, cuando el año ISO no coincide con el año calendario de
  `@FechaInicio` (ej. el 30-dic-2029 es lunes de la semana ISO 1 de 2030). `_validar_alineacion_iso()`
  también lo atraparía como desalineado si pasa (compara contra `date.fromisocalendar`, que sí respeta el
  año ISO) — pero no está probado en producción todavía. Registrado en `../../../wiki/2_areas/gaps_y_preguntas.md`: revisar antes
  de la primera corrida de diciembre 2026.
- **"MoM" se retiró como protagonista el 2026-08-04 — no lo reintroduzcas sin preguntar.** La vista mensual
  por tramo (`bloque_mensual`, etiquetada "julio"/"junio") tenía dos problemas de fondo: (1) mezclaba la
  etiqueta de mes calendario con un cálculo que en realidad era un tramo capado a `TRAMO_MAX` (4) semanas,
  así que en un mes de 5 semanas ISO el número quedaba "congelado" varias semanas seguidas sin que nada
  avisara por qué; (2) el usuario identificó riesgo real de que alguien sin el contexto completo (el CEO,
  por ejemplo) leyera esa cifra como un cierre contable mensual exacto. Se reemplazó por `bloque_movil()` —
  ventana móvil de `VENTANA_TENDENCIA` (4) semanas cerradas vs. las 4 previas, sin nombre de mes, que se
  actualiza toda semana. `bloque_mensual` **no se eliminó**: sigue viva para la "serie mensual completa"
  del anexo (mes completo vs. mes completo, magnitud histórica absoluta) — es contexto, ya no es la base
  del número protagonista. Se evaluó también prorratear una semana de borde entre dos meses por días
  calendario (usando `FechaInicioCorte`/`FechaFinCorte`, que ya se ingieren) para tener un "acumulado real
  del mes" sin pedirle nada nuevo al usuario — **el usuario lo descartó explícitamente** (2026-08-04): no
  quiere cubrir "cómo venimos contra el objetivo del mes" con datos semanales aproximados; prefiere que el
  reporte sea explícito en que solo mide "¿aceleramos o desaceleramos?" (tendencia) y no un cierre mensual.
  Si en el futuro se agrega medición mensual real, va a requerir un cambio de ingesta (grano diario o un
  `GROUP BY` adicional por mes calendario en las queries), no un cambio de cálculo sobre lo que ya se pide.
- **El árbol jerárquico del email (`ARBOL_CORE_NSM1`/`ARBOL_CORE_NSM2` en `render_email.py`) está
  hardcodeado por `id`, no se deriva del campo `padre` del JSON.** El campo `padre` de una palanca define
  contra qué se calcula su `share` (ver gotcha de arriba, "`padre` no siempre es su NSM"), pero **no**
  necesariamente coincide con dónde debería anidarse visualmente en el árbol — los tipos de operación de
  Wallet tienen `padre="nsm1_wallet"`, no `"nsm1_out"`/`"nsm1_in"`, aunque visualmente se muestran anidados
  bajo OUT/IN porque así se lee como negocio (igual que el árbol de referencia que pidió el usuario). Si se
  agrega un tipo nuevo a `NSM1_TIPOS`, `TAC_TIPOS`, `NSM2_TIPOS` o `NSM2_FORMAS` en `pipeline.py`, hay que
  sumar la entrada correspondiente a mano en `ARBOL_CORE_NSM1`/`ARBOL_CORE_NSM2` — no aparece solo.
- **Las columnas de WoW y Tendencia del árbol usan ancho FIJO en píxeles (`WOW_COL_W`/`TEND_COL_W` en
  `render_email.py`), y se justifican a la IZQUIERDA de su propia columna, no a la derecha del todo.**
  Esto es lo que hace que las flechitas (▲/▼) queden alineadas verticalmente entre renglones sin importar
  el nivel de indentación — el padding-left del indentado no afecta el ancho de las columnas de la derecha
  porque cada nivel usa su propia tabla anidada al 100% del espacio que le queda. Se probó primero
  justificado a la derecha del todo (v5) y el usuario pidió cambiarlo a la izquierda de la columna (v6) —
  no revertir sin que lo pida de nuevo.
- **Los leading indicators (altas de cuentas/comercios) son una CANTIDAD, no un monto — `formato: "entero"`
  en el registro evita que se impriman como pesos.** `fmt_valor()`/`_valor()` en `pipeline.py`/
  `render_email.py` despachan a `fmt_n`/`_entero` en vez de `fmt_m`/`_monto` cuando `p.get("formato") ==
  "entero"`. Si se agrega otra palanca de conteo (no de pesos) en el futuro, hay que marcarla igual — si no,
  sale como "$0,03 M" en vez de "30.075".
- **Al armar el borrador de email con el conector de Gmail, pasale el HTML real — nunca una sustitución de
  shell como `$(cat archivo)` en el valor del parámetro.** Las tool calls no son un shell: ese texto se
  manda tal cual, literal, como si fuera el contenido del email. Pasó en la corrida del 2026-08-05 (se
  mandó `$(cat)` literal al primer intento de `update_draft`); se corrigió leyendo el archivo con `Read` y
  pegando el contenido real como valor del parámetro.
- **Los items de `contexto_vivo/` de esta skill nacen con `estado: capturado`, nunca otro valor — no lo
  copies del ejemplo equivocado.** En la corrida del 2026-08-26 los 5 items de esa fecha (el store, el
  reporte, la decisión de metodología de ventana móvil y los dos gaps actualizados) se escribieron con
  `estado: en_cola` directo en el frontmatter, probablemente por copiar como plantilla un item de una
  corrida anterior que ya estaba en esa etapa (post-`/context_push`) en vez de arrancar de `_plantilla.md`.
  Consecuencia: quedaron marcados como "ya subidos al core" sin estarlo de verdad, invisibles para el
  inventario normal de `/context_push` (que solo busca `estado: capturado`) — el `/context_pull` del
  2026-08-27 los encontró como anomalía (`en_cola` en el frontmatter, ausentes en `CEREBRO_CORE`) y hubo
  que subirlos manualmente con permiso explícito del usuario, saltando el paso intermedio. El campo
  `estado` es un handoff entre skills (`capturado` → lo escribe quien crea el item → `/context_push` lo
  pasa a `en_cola` al subirlo → `/context_merge` lo pasa a `ingestado` al mergearlo) — ninguna corrida de
  `/sync_metrics` debe escribir otra cosa que `capturado`.
