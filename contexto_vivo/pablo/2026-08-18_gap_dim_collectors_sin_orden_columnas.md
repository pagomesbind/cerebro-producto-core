---
id: 2026-08-18_gap_dim_collectors_sin_orden_columnas
pm: pablo
fecha_captura: 2026-08-18
fuente: "/sync_metrics — ingesta semanal, semana 202633"
producto: transversal
tema: dim_collectors sin orden posicional de columnas definido para exports sin encabezado
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: crear
contradice: "no"
confianza: alta
estado: ingestado
---

**Severidad:** Media.

**Descripción:** El export de `SELECT * FROM [dbo].[Collectors]` que pide `/sync_metrics` (query 8 del
SKILL) nunca incluye fila de encabezado (misma limitación de la herramienta del usuario ya conocida para
el resto de los recursos, confirmada 2026-08-11). A diferencia de `operaciones`, `transacciones`,
`cuentas`, `comercios` y `transferencias_agente_cobro` — que sí tienen su orden posicional de columnas
definido en `COLUMN_ORDER_HEADERLESS` de `pipeline.py` desde el 2026-08-11 — la dimensión `dim_collectors`
nunca lo tuvo, así que el pipeline no puede resolverla por forma/contenido y la marca `[ABORT]` en
`inspect`. En la corrida de la semana 202633 esto obligó a sacar `collectors.csv` de `raw/` antes de poder
correr `ingest` sobre el resto de los recursos.

La primera fila del export de esta corrida, para referencia:
```
1;20-1-749049-1-5;Bind PSP SA;30717449076;184;3220001805007490490019;https://amorenobind.pythonanywhere.com/webhook;2023-05-10 14:22:21.6389709;NULL;100;322;7$$C17105$$B00009548213
```
12 columnas. El registro `RESOURCES["dim_collectors"]` de `pipeline.py` solo necesita mapear con certeza 5
de ellas para poder ingerir el recurso: `Id`, `Name`, `Cuit`, `Codigo`, `BankId` (más `CollectAccountId`
por la firma de columnas del recurso). Lectura tentativa sin confirmar: `Id, CollectAccountId, Name, Cuit,
PSP/EntidadId, CBU, WebhookUrl, FechaAlta, ?, BankId, ?, Codigo` — no se aplicó porque el protocolo de
ingesta prohíbe inventar un mapeo de columnas sin confirmación.

**Pregunta para el usuario:** ¿Podés confirmar el orden real de columnas de `SELECT * FROM Collectors` (o
pasar los nombres de columna de la tabla)? Con eso se agrega `dim_collectors` a
`COLUMN_ORDER_HEADERLESS` en `pipeline.py` y deja de ser un problema en cada corrida futura.

**Impacto mientras esté pendiente:** ninguno sobre el volumen de las NSM (la dimensión es solo para
resolver nombres de collectors) — pero los collectors nuevos que se hayan dado de alta no tienen nombre
resuelto en el store hasta que se ingiera un refresh de la tabla, y el archivo `collectors.csv` de esta
corrida quedó fuera de `raw/` (movido al scratchpad de la sesión) sin ingerir.

**Estado:** Pendiente.
