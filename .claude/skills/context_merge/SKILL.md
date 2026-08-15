---
name: context_merge
description: Ingiere al canon compartido (2_areas/3_recursos de CEREBRO_CORE) todos los items en_cola de contexto_vivo/ de los tres PM/PO. Es el único proceso autorizado a escribir esas dos capas. Corre exclusivamente el líder, sobre el clon del repo compartido. Cadencia recomendada: semanal.
when_to_use: Se activa cuando el usuario ejecuta /context_merge. Solo lo corre el PM líder (identidad.local.md, rol: lider) — la skill aborta si no lo sos.
disable-model-invocation: true
argument-hint: ""
---

# 🔀 MERGE DE CONTEXTO AL CANON: /context_merge

## 🎯 Por qué existe esta skill

Es la bisagra de todo el pipeline de sincronización multi-PM: el único proceso que tiene permiso para escribir `wiki/2_areas/` y `wiki/3_recursos/` de `CEREBRO_CORE`. Todo lo que las skills de las tres instalaciones capturaron en sus `contexto_vivo/` y subieron con `/context_push` converge acá. La regla que hace confiable todo el diseño: **este merge escribe los archivos finales reales, nunca instrucciones para que otro proceso reinterprete** — es lo que garantiza que las tres instalaciones terminen con el mismo canon byte a byte después de un `/context_pull`.

## 🔒 Paso -1 obligatorio — verificar que sos el líder

Leé `identidad.local.md` (raíz del repo). Si `rol` no es `lider`, **abortá** con un mensaje claro: solo el PM líder corre esta skill — es intencional, no un descuido de permisos. Avisale al usuario quién es el líder designado.

## 🔌 Prerrequisitos

1. `ruta_clon_core` en `identidad.local.md` debe apuntar a un clon existente de `CEREBRO_CORE`. Si no existe, abortá.
2. **Toda esta skill corre dentro de ese clon, nunca en el repo personal.** El repo personal no se toca en ningún paso.
3. `git pull --ff-only` primero, para tener los últimos `/context_push` de los tres PM antes de arrancar. Si falla (no fast-forward inesperado — no debería pasar si solo esta skill escribe canon), avisá y no sigas sin resolverlo a mano.

## 🏃 Pipeline

### Paso 1 — Inventario de items pendientes

Recorré `contexto_vivo/<pm>/` de cada PM (las subcarpetas que existan — no asumas que los tres tienen actividad) y listá todos los items en `estado: en_cola`. Agrupalos por `producto` + `tema` para detectar duplicados/contradicciones cross-PM antes de procesar uno por uno.

Si no hay ningún item en `en_cola`: reportá "nada para mergear" y terminá.

### Paso 2 — Clasificar cada item por régimen de escritura

Para cada item (o grupo de items del mismo tema), resolvé `destino_propuesto` contra el árbol de ruteo PARA de `CLAUDE.md` y determiná el régimen:

| Régimen | Rutas | Cómo procede el merge |
|---|---|---|
| **A — Ledgers propios de esta skill** | `2_areas/tareas.md`, `2_areas/riesgos.md`, `2_areas/gaps_y_preguntas.md`, `2_areas/direccion/decisiones.md`, `2_areas/direccion/oportunidades.md`, `2_areas/direccion/iniciativas.md`, `2_areas/changelog.md`, `3_recursos/changelog.md` | Escritura libre — sigue al Paso 3. |
| **B — `3_recursos/` general** | `detalle_productos/`, `arquitectura_sistema/`, `cumplimiento_normativo/` | Escritura libre. **Crear una carpeta nueva** (producto nuevo, módulo nuevo) requiere permiso explícito del usuario — pausá y preguntá antes de crearla. |
| **C — `3_recursos/datos/`** | cualquier archivo bajo `datos/` | Ver Paso 4 — mecánica de copia, no de redacción. |
| **D — Resto de `2_areas/`** | overviews, `procesos/`, `clientes/`, `direccion/{north_star,estado_actual,estacionalidad,estrategia}` | **Requiere permiso explícito del usuario antes de crear o modificar**, sin excepción — es la capa que debe moverse lo menos posible. Presentá el item y esperá confirmación antes de escribir. |

### Paso 3 — Verificar y escribir (regímenes A y B)

Para cada item de régimen A o B, antes de escribir:

1. **Verificá el destino contra las reglas anti-cajón de `CLAUDE.md`**: nombres vetados (`transversal/`, `otros/`, `varios/`, etc.), nunca apilar un tema nuevo en un archivo que trata de otro tema, nunca rutear un producto por descarte.
2. **Umbral de fisión:** si escribir el item deja el archivo de `detalle_productos/` por encima de ~300 líneas o cubriendo más de un tema, partilo en el momento (crear el archivo temático que falte) en vez de simplemente apilar.
3. **Filtro editorial en régimen A** (`tareas.md`/`riesgos.md`/`direccion/*`): solo entra lo general e importante para **los tres** PM/PO — un item que es en realidad detalle operativo de un solo proyecto no debería haber llegado hasta acá (si pasa, se lo devuelve al PM con nota, no se ingiere).
4. **Verificá `Estado:` declarado** si el destino es `detalle_productos/` — todo archivo nuevo o sección nueva declara su estado (`en producción` / `discovery — no construido` / `documentación desactualizada / en disputa`) según corresponda al origen del conocimiento.
5. **Escribí el contenido final real** — el item ya trae el texto trabajado, tu trabajo es integrarlo correctamente al archivo (delta: qué ya existe, qué es genuinamente nuevo, no duplicar), no reescribir la prosa del PM.
6. Si el item trae `contradice` distinto de `"no"`: aplicá el Protocolo de Contradicción (ver abajo) **en vez de** escribir directo.

### Protocolo de Contradicción

Si dos items (del mismo PM en distintas fechas, o de PMs distintos) traen versiones incompatibles del mismo hecho, **el merge nunca elige ganador**:

1. Escribí **ambas versiones**, cada una marcada con su fuente y fecha, en el archivo destino.
2. Abrí un item de gap: `tipo: gap` propio del merge (mismo mecanismo, generado por vos), `destino_propuesto: 2_areas/gaps_y_preguntas.md`, describiendo la contradicción exacta y qué se necesita para resolverla.
3. Escalá a los PMs involucrados en el reporte de cierre — no lo dejes solo en el archivo, decilo explícitamente en el resumen que le das al usuario.

Lo mismo aplica si dos PMs proponen el mismo store de datos (régimen C) con contenido distinto — ver Paso 4.

### Paso 4 — Items `tipo: dato` (régimen C) — copia, no redacción

Estos items no pasan por criterio editorial. Para cada uno:

1. Verificá que `destino_propuesto` apunte dentro de `3_recursos/datos/`.
2. **Copiá el cuerpo del item byte a byte** al archivo (o archivos, si el item referencia una carpeta completa como `datos_metricas_semanales/`) de destino. No reformatees, no resumas, no "mejores" la redacción — es un store de datos, no prosa.
3. **Si dos PMs mandaron items `tipo: dato` con el mismo `destino_propuesto`** (no debería pasar salvo que dos hayan corrido la misma skill de fuente compartida por error — ver `identidad.local.md`/`runner_fuentes_compartidas`): no seleccione uno arbitrariamente. Aplicá el Protocolo de Contradicción — escalá, no ingieras ninguno hasta que se resuelva.

### Paso 5 — Items `tipo: iniciativa`

1. **Upsert** de la fila en `2_areas/direccion/iniciativas.md` — clave = `proyecto` (PRD/slug). Si la fila ya existe, **anteponé** la novedad fechada del item a las anteriores (no reemplaces el histórico de novedades). Si no existe, creala.
2. Si el item marca **cierre** (finalizada/cancelada): agregá la fila de calibración en `3_recursos/datos/log_iniciativas_producto.md` (SP estimado vs. real, dónde quedó el conocimiento) y quitá la fila de la cartera viva en `iniciativas.md` (ya no está "en curso").
3. **Si el item trae `pm_destino`:** no escribas nada en la carpeta de proyecto de ese PM (no tenés acceso ni corresponde) — listalo aparte en el manifiesto (Paso 7) bajo una sección "Novedades para <pm_destino>", para que `/context_pull` se las reporte cuando ese PM pulee.

### Paso 6 — Régimen D — pedir permiso

Antes de tocar cualquier archivo de este régimen, presentale al usuario el item completo (fuente, contenido, destino propuesto) y esperá una confirmación explícita. Si no la da en esta sesión, dejá el item en `en_cola` (no lo ingieras) y anotalo como pendiente de decisión en el reporte de cierre — no lo fuerces ni lo descartes por tu cuenta.

### Paso 7 — Cerrar cada item procesado

Por cada item efectivamente ingerido (regímenes A/B/C, y D con permiso):
1. Actualizá su frontmatter: `estado: ingestado`, `merge_commit: <se completa después del commit del Paso 9>`.
2. Movelo de `contexto_vivo/<pm>/` a... no lo muevas vos — el archivo queda en el core marcado `ingestado`; es `/context_pull` quien lo archiva en el install de cada PM a `4_archivos/contexto_ingestado/`. Tu trabajo termina en marcarlo.

Los items **no** procesados (régimen D sin permiso, contradicciones sin resolver) quedan en `en_cola` tal cual — no los toques.

### Paso 8 — Changelog por capa

Por cada archivo tocado en `2_areas/` o `3_recursos/`, agregá una línea al `changelog.md` de esa capa (agrupadas bajo la fecha de este merge): `` `ruta/archivo.md` — creado/actualizado: <resumen de una línea> (<pm de origen>) ``. Sin detalle de contenido — eso está en el archivo.

### Paso 9 — Manifiesto

Escribí `manifiestos/YYYY-MM-DD.md` en la raíz del clon core (creá la carpeta si no existe, con su `index.md` si es la primera vez):

```markdown
# Manifiesto de merge — YYYY-MM-DD

## Items ingeridos
| PM | Item | Tipo | Destino | Régimen |
|---|---|---|---|---|

## Permisos pedidos
(qué se le preguntó al usuario en el Paso 6, y qué respondió)

## Contradicciones abiertas
(qué se escaló, a quién, con link al gap)

## Novedades para otro PM (tipo: iniciativa con pm_destino)
| Para | Proyecto | Novedad |
|---|---|---|

## Items sin procesar (quedan en_cola)
(y por qué — permiso pendiente, contradicción sin resolver)
```

### Paso 10 — Índices, commit y push

1. Actualizá los índices de `2_areas/` y `3_recursos/` afectados (regla de integridad de índices de `CLAUDE.md`) — es tu responsabilidad exclusiva, ninguna otra sesión la comparte.
2. `git add` de todo lo tocado en el clon core (canon + changelogs + manifiesto + items marcados `ingestado`), commit `context_merge — YYYY-MM-DD (N items, M pendientes)`, `git push origin main`.
3. Completá el campo `merge_commit` de los items ingeridos con el hash de este commit (un segundo commit chico si hace falta, o incluilo en el mismo si el hash se puede predecir — lo importante es que quede registrado).
4. Reportá al usuario: qué entró, qué quedó pendiente de permiso, qué contradicciones se abrieron.
