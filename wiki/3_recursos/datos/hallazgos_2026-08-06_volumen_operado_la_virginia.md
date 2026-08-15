# Hallazgo — Volumen operado por La Virginia en Wallet, evolución y estimación de referencia para el caso de negocio de OB PJ (2026-08-06)

> Motivado por: [proyecto La Virginia — OB PJ](../../1_proyectos/proyecto-la-virginia-ob-pj/proyecto.md) — el usuario pidió interpolar métricas reales de Bind PSP (cuentas/volumen de Wallet, comercios/volumen de Cobro) para dimensionar el caso de negocio del stock de 2.000 personas jurídicas pendientes de dar de alta.
> Fuente: store acumulado de [`/sync_metrics`](datos_metricas_semanales/index.md) — `fact_operaciones.csv`/`fact_cuentas.csv` filtrados por `OrganizacionId=30` (La Virginia, ver `dim_organizaciones.csv`) para Wallet, y `fact_transacciones.csv`/`fact_comercios.csv` filtrados por `EntidadIdentificador="VIRG"`/`EntidadId=423` (ver `dim_entidades.csv`) para Cobro/Adquirencia. Rango disponible: semana 202536 (2025-09-01) a 202631 (2026-08-03), 48 semanas cerradas. Agregados puros, sin PII — cálculo vía `awk` en línea de comandos.
> **Complementa** (no reemplaza) a [`hallazgos_2026-07-20_volumen_la_virginia.md`](hallazgos_2026-07-20_volumen_la_virginia.md), que usó un dataset distinto (CSV puntual de cuentas/solicitudes, solo mayo-julio 2026, con desglose PF/PJ) — este hallazgo usa el store semanal oficial de NSM, con casi un año de historia pero **sin discriminador de persona física vs. jurídica** (esa distinción no está en `fact_operaciones.csv`/`fact_cuentas.csv`).

## 1. Evolución del volumen operado en Wallet — crecimiento fuerte y sostenido

| Ventana | Volumen promedio semanal | Operaciones promedio semanal |
|---|---|---|
| Primeras 4 semanas del store (sep-2025, 202536-202539) | $15,45 M | 68,5 |
| 4 semanas previas a la última (202624-202627) | $464,23 M | 998,2 |
| Últimas 4 semanas cerradas (202628-202631) | $458,83 M | 590,5 |

- **La Virginia multiplicó por ~30x su volumen operado en Wallet en el último año** (de ~$15 M/semana a ~$460 M/semana) — es un cliente con momentum real, no solo el problema de onboarding jurídico puntual que motivó este proyecto.
- El último mes-tramo (últimas 4 semanas) está prácticamente estable respecto al anterior (−1,2% en volumen), aunque con **menos operaciones y ticket promedio más alto** (990→590 ops/semana) — no se investigó la causa, queda como observación, no como hallazgo cerrado.

## 2. Cuentas de Wallet dadas de alta — todo el período

- **1.508 altas de cuenta acumuladas** en las 48 semanas del store (`fact_cuentas.csv`, todas las semanas, `OrganizacionId=30`) — no hay forma de discriminar PF/PJ en este dataset (a diferencia del hallazgo de julio, que sí podía por tener otro origen). Dado que la wiki ya documentó que el circuito de PJ es marginal hasta ahora (~2% de las cuentas, ver hallazgo anterior), la enorme mayoría de estas 1.508 son personas físicas.
- Volumen promedio por cuenta (usando el promedio de volumen semanal de las últimas 8 semanas cerradas, $461,5 M, sobre el total acumulado de 1.508 cuentas): **≈ $306.000/semana por cuenta ≈ ~$1,3 M/mes por cuenta**. **⚠️ Piso conservador, no el promedio de una cuenta activa** — ver §5.

## 3. Interpolación para el stock de 2.000 personas jurídicas pendientes — techo teórico, no proyección

Si el stock represado de 2.000 PJ se diera de alta y cada cuenta operara con el **mismo promedio** que la cuenta típica de La Virginia hoy (~$1,3 M/mes), el volumen incremental sería del orden de:

**2.000 × ~$1,3 M/mes ≈ $2.600 M/mes adicionales** — una cifra que **más que duplicaría** el volumen total actual de La Virginia (~$1.835 M/mes en las últimas 4 semanas).

**Esto es un techo teórico extremo, no una proyección realista, por 3 motivos:**
1. El promedio usado mezcla mayoritariamente cuentas de **persona física** (incluyendo las "Cajas" de repartidores de alto movimiento documentadas en la ficha de cliente) — el comportamiento transaccional de una cuenta corporativa (PJ) probablemente no es comparable al de esas cuentas.
2. No hay ningún supuesto de **ritmo de activación** — las 2.000 no se van a dar de alta ni a operar todas de una vez (pregunta ya abierta en el problem statement: no hay un plan/ritmo definido).
3. Es un promedio, no una mediana — un puñado de cuentas de muy alto volumen (posiblemente las cuentas de distribución/repartidores) puede estar arrastrando el promedio muy por encima de lo que operaría una PJ típica.

**Uso recomendado de esta cifra:** sirve como **orden de magnitud** para argumentar que el stock de 2.000 PJ no es un número chico frente al volumen ya operado por el cliente — no como un forecast a comprometer con el negocio. Ver pregunta abierta relacionada en el [problem statement](../../1_proyectos/proyecto-la-virginia-ob-pj/artefactos/2026-08-06_problem_statement_onboarding_pj_la_virginia.md) (target/ritmo de activación del stock, sin definir).

## 4. Cobro/Adquirencia — resuelto: el cruce correcto es por `Codigo` ("VIRG"), no por `EntidadId` numérico

**Causa raíz encontrada (2026-08-06, 2):** `fact_transacciones.csv` no usa el `EntidadId` numérico de `dim_entidades.csv` en su columna `EntidadIdentificador` — para La Virginia, esa columna guarda directamente el **`Codigo` de la entidad, `"VIRG"`** (string), no `423`. Es una inconsistencia del propio store: otras filas del dataset sí usan el `Id` numérico para identificar la entidad, así que `EntidadIdentificador` mezcla dos espacios de identificador distintos según la fila. Filtrando correctamente por `EntidadIdentificador="VIRG"` aparecen los datos:

| Ventana | Volumen (ACREDITADO) | Operaciones |
|---|---|---|
| Histórico completo (41 semanas con datos, desde semana 202543, oct-2025) | $123,52 M acumulado | 4.570 |
| Últimas 8 semanas cerradas (202624-202631) | $73,06 M acumulado, **$9,13 M/semana promedio** | 1.456 |

- Todas las transacciones encontradas son del mismo tipo (`TipoTransaccion=9`, `FormadePago=20`) — no se identificó a qué combinación corresponde exactamente en la documentación de producto disponible; queda sin decodificar, no bloquea el cálculo de volumen.
- **Comercios dados de alta acumulados:** 1.558 (`fact_comercios.csv`, `EntidadId=423`, todo el período — mismo criterio que las cuentas de Wallet en §2, ver limitaciones en §5).
- **Volumen promedio por comercio:** $9,13 M/semana ÷ 1.558 comercios ≈ **$5.860/semana por comercio ≈ ~$25.400/mes por comercio** (mismo método que §2 para cuentas de Wallet). **⚠️ Piso conservador, no el promedio de un comercio activo** — ver §5.

### Interpolación para los 2.000 comercios del stock represado

Si los 2.000 comercios asociados a las PJ represadas operaran al mismo promedio (~$25.400/mes por comercio), el volumen incremental de Cobro/Adquirencia sería del orden de:

**2.000 × ~$25.400/mes ≈ $50,8 M/mes adicionales** — techo teórico de referencia, con las mismas 3 limitaciones que la interpolación de Wallet en §3 (promedio no mediana, mezcla de perfiles, sin supuesto de ritmo de activación).

## 5. Limitaciones metodológicas

- **Los promedios por cuenta/comercio (§2, §4) son un piso conservador, no el promedio de una unidad activa — confirmado, no solo sospechado (2026-08-06, 3).** El store solo tiene agregados **semanales por entidad completa** (`fact_transacciones.csv`, `fact_operaciones.csv`) — no una fila por comercio o cuenta individual — así que no hay forma de calcular una mediana ni de aislar "solo los que efectivamente operan" con este dataset. Evidencia de que la brecha es real, no un detalle menor: en las últimas 8 semanas, Adquirencia de La Virginia tuvo **~182 operaciones/semana contra 1.558 comercios acumulados** (~0,12 operaciones/comercio/semana si estuviera repartido uniformemente), y Wallet tuvo **~798 operaciones/semana contra 1.508 cuentas** (~0,53 operaciones/cuenta/semana). Es consistente con que una parte importante del stock acumulado (probablemente varias de las "Cajas" de repartidores) esté dado de alta pero opere con muy baja frecuencia o no opere — eso infla el denominador sin aportar al numerador y **deprime el promedio muy por debajo de lo que genera una cuenta/comercio realmente en uso**. Usar estas cifras como piso conservador (decisión del usuario, 2026-08-06) — no como el promedio esperable de una PJ activa.
- `fact_cuentas.csv`/`fact_comercios.csv` son **altas nuevas por semana** (leading indicators), no stock total activo — el acumulado de 1.508/1.558 asume que las cuentas/comercios dados de alta siguen activos, sin dar de baja, lo cual es razonable pero no está verificado.
- No hay forma de aislar volumen específico de cuentas/comercios PJ dentro de `fact_operaciones.csv`/`fact_transacciones.csv` — los promedios de §2 y §4 son una mezcla de todo el mix de La Virginia (mayoritariamente persona física).
- La inconsistencia de `EntidadIdentificador` (Codigo vs. Id numérico, ver §4) puede repetirse en otras entidades del store — no se auditó el dataset completo, solo se resolvió el caso puntual de La Virginia.
- Cálculo hecho sobre agregados semanales oficiales del store de `/sync_metrics` — no requirió acceso a ningún dataset con PII. Para un promedio real de "cuenta/comercio activo" haría falta un dataset con grano por unidad individual (ej. conteo de comercios/cuentas con al menos 1 transacción en una ventana), que no existe hoy en este store.

---
*Última actualización: 2026-08-06 (3) — §5 confirma con evidencia cuantitativa (ratio operaciones/semana vs. stock acumulado) que los promedios por cuenta/comercio son un piso conservador, no el promedio de una unidad activa — decisión del usuario: mantener las cifras, aclarándolo explícitamente donde se usan.*
*Última actualización anterior: 2026-08-06 (2) — §4 resuelta: el cruce correcto de Cobro/Adquirencia es por `Codigo` ("VIRG"), no por `EntidadId` numérico — agrega volumen real y referencia de interpolación para los 2.000 comercios represados.*
*Creado: 2026-08-06 — a pedido del usuario, para el caso de negocio del proyecto La Virginia OB PJ.*
