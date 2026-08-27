---
id: 2026-08-21_adquirencia_bug_vista_iibb_liquidacion_lote
pm: pablo
fecha_captura: 2026-08-21
fuente: "/sync_mails — mail 'VISTA - RET_IIBB_REC_ACUM_LOTE - Impuestos Adquirencia', Ariel Profitti (Fintexa) a Sergio Pavetto/mvila@bind.com.ar, hilo `1a01fd096e45f889` (2026-08-20)"
producto: adquirencia
tema: Bug de performance (fan-out JOIN) y de NULL constraint en la vista de cálculo de percepción de IIBB para liquidación por lote
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/impuestos_iibb_liquidacion_lote.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Contexto

Fintexa (Ariel Profitti) reportó un cuello de botella real de performance en la vista `RET_IIBB_REC_ACUM_LOTE`, usada por el proceso de liquidación por lote para calcular la percepción de Ingresos Brutos (IIBB) sobre las transacciones de Adquirencia. El disparador fue el modelo propuesto días antes para transaccionar por lotes sobre un comercio en particular — al probarlo, la vista mostró un comportamiento de fan-out no previsto en producción (no reproducible en ambientes bajos, que no tienen ese volumen ni esa repetición de CUIT↔comercio).

## Causa raíz — fan-out por JOIN sin discriminar sucursal

La vista hace `INNER JOIN` entre `LIQ_IMP` (una fila por transacción liquidada) y `COMERCIO` usando solo `CUIT`:

```sql
FROM LIQ_IMP
INNER JOIN COMERCIO ON COMERCIO.CUIT = LIQ_IMP.CUIT
```

Cuando un mismo CUIT tiene múltiples comercios/sucursales dadas de alta (caso real observado: un CUIT con 200 filas en `COMERCIO`, una por sucursal — `C02025`, `C07885`, `C11175`, `C15887`... hasta 200), el JOIN no elige una fila — trae el producto cartesiano de todas las combinaciones. Una única transacción liquidada termina generando 200 filas de salida en vez de 1.

Impacto medido/estimado por Fintexa:

| | 10 transacciones (medido) | 500 transacciones (estimado) |
|---|---|---|
| Scan count sobre `COMERCIO` | 53 | ~2.650 |
| Logical reads sobre `LIQ_IMP` | 9.810.203 | ~490.510.150 |
| Tiempo real | 28,4 minutos | probablemente varias horas |

No ocurre en ambientes bajos (staging/QA) porque no tienen ni el volumen transaccional ni la repetición de CUIT-con-múltiples-comercios que sí existe en producción — es un caso donde el ambiente bajo no es representativo para detectar este tipo de bug de escalado.

## Bug derivado — NULL rompe el INSERT cuando no hay percepción aplicable

Sobre el mismo proceso, aparece un segundo error real en producción (`SharedImpuestoDB_prd`):

```
Msg 515, Level 16, State 2, Procedure dbo.GEN_LIQ_IMP_LOTE, Line 129
Cannot insert the value NULL into column 'PERC_IIBB_PORC', table 'SharedImpuestoDB_prd.dbo.LIQ_IMP'; column does not allow nulls.
```

Causa: para la mayoría de las transacciones (el caso normal) no existe ninguna percepción de IIBB aplicable, por lo que no hay fila para ese `ID_TX` en `LIQ_IMP_CALCULAR_LOTE_PERC_IIBB`. Un `LEFT JOIN` sin coincidencia devuelve `NULL` (no "0" automáticamente), y ese `NULL` choca contra una columna destino que no permite nulos.

Fix propuesto por Fintexa (sin confirmar si ya se aplicó): envolver las columnas de percepción con `ISNULL` en la vista —

```sql
ISNULL(PERC_IIBB_BASE, 0) AS PERC_IIBB_BASE,
ISNULL(PERC_IIBB_PORC, 0) AS PERC_IIBB_PORC,
ISNULL(PERC_IIBB, 0) AS PERC_IIBB
```

## Estado

Ambos hallazgos quedaron reportados por Fintexa a `sergio.pavetto@siane.com.ar` y `mvila@bind.com.ar` el 2026-08-20, sin confirmación de resolución al momento de este barrido (2026-08-21). No se identificó una IDEA de Jira asociada en este mail.

> Fuente: Mail "VISTA - RET_IIBB_REC_ACUM_LOTE - Impuestos Adquirencia" — Ariel Profitti (Fintexa), 2026-08-20.
