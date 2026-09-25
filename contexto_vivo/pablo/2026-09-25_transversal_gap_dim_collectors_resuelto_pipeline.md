---
id: 2026-09-25_transversal_gap_dim_collectors_resuelto_pipeline
pm: pablo
fecha_captura: 2026-09-25
fuente: "sesión libre con el PM (Pablo Gomes) — aplicación directa del mapeo ya confirmado 5 veces, sobre pipeline.py en el clon de CEREBRO_CORE"
producto: transversal
tema: Cierre del gap dim_collectors (COLUMN_ORDER_HEADERLESS en pipeline.py) — mapeo ya confirmado 5 veces, ahora aplicado en código
tipo: gap
destino_propuesto: 2_areas/gaps_y_preguntas.md
tipo_destino: actualizar
contradice: "no"
confianza: alta
estado: en_cola
merge_commit:
---

## Qué se resolvió

El gap `[2026-08-18] — dim_collectors sin orden posicional de columnas definido para exports sin encabezado` (`2_areas/gaps_y_preguntas.md`) llevaba **cinco reconfirmaciones consecutivas** del mismo mapeo (2026-08-26, 08-31, 09-14, 09-22, y el intento de regresión detectado en la corrida de 09-22) sin que el cambio de código se aplicara nunca.

En esta sesión se agregó la entrada `"dim_collectors"` a `COLUMN_ORDER_HEADERLESS` en `.claude/skills/sync_metrics/scripts/pipeline.py` (editado directo sobre el clon de `CEREBRO_CORE`, no sobre este install — el mismo archivo que pide el propio gap), con el mapeo ya confirmado y nunca contradicho:

```python
"dim_collectors": ["Id", "CollectAccountId", "Name", "Cuit", "Psp", "Cbu", "Webhook",
                    "FechaAlta", "_c9", "Codigo", "BankId", "_c12"],
```

12 columnas — longitud única dentro de `COLUMN_ORDER_HEADERLESS` (no comparte forma con ningún otro recurso headerless, así que no entra en `_NCOLS_AMBIGUOS` ni necesita desambiguación por contenido/nombre de archivo). Los campos que `RESOURCES["dim_collectors"]["val"]`/`["key"]` realmente usan (`Id`, `Name`, `Cuit`, `Codigo`, `BankId`) quedan en las posiciones correctas; `_c9` y `_c12` son las dos columnas que nunca se identificaron (NULL en toda la muestra / código compuesto), sin uso en el pipeline.

**Estado del cambio:** commiteado (`0b8d6e8`, "Agregar dim_collectors a COLUMN_ORDER_HEADERLESS en pipeline.py") y pusheado a `origin/main` de `CEREBRO_CORE` con OK explícito del usuario — ya visible para Nicolás y Luciana en su próximo pull.

## Para `/context_merge`

Actualizar la entrada `[2026-08-18]` de `gaps_y_preguntas.md`: agregar una línea de cierre "**Resuelto (2026-09-25)** — mapeo aplicado en `COLUMN_ORDER_HEADERLESS['dim_collectors']` de `pipeline.py`, ver commit correspondiente" y cambiar el campo **Estado** de "Pendiente" a "Resuelto". Candidato a rotar a `4_archivos/gaps_resueltos.md` en el próximo ciclo de limpieza (mismo criterio que el gap de Terra Blockchain/Sucredito).
