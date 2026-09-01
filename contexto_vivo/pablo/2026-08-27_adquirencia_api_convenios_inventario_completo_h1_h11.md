---
id: 2026-08-27_adquirencia_api_convenios_inventario_completo_h1_h11
pm: pablo
fecha_captura: 2026-08-27
fuente: "/idea_solution — cierre del análisis técnico-funcional de convenios_configuracion; enriquecimiento del contrato OpenAPI ya destilado, mismo spec ya citado en gestion_convenios_comisiones.md"
producto: adquirencia
tema: Inventario endpoint-por-endpoint completo (16 endpoints) y 3 hallazgos nuevos (H9-H11) del contrato de la API de Convenios/Comisiones — enriquece el item ya mergeado
tipo: conocimiento
destino_propuesto: 3_recursos/detalle_productos/adquirencia/gestion_convenios_comisiones.md
tipo_destino: actualizar
contradice: "no — enriquece, no contradice, el contenido ya mergeado en ese archivo (item de contexto_vivo 2026-08-24, ya archivado en 4_archivos/contexto_ingestado/)"
confianza: alta
estado: ingestado
merge_commit:
---

## Qué pasó

El item original de `contexto_vivo/` que dio origen a `3_recursos/detalle_productos/adquirencia/gestion_convenios_comisiones.md` (capturado 2026-08-24) quedó con una destilación **parcial** del contrato — 8 gaps documentados, y el propio archivo mergeado dice en su fuente "ver `/idea_solution` en curso". Al cerrar `/idea_solution` (2026-08-27), un subagente dedicado releyó el spec completo endpoint por endpoint (con línea de origen citada para cada uno) y encontró 3 hallazgos adicionales (H9-H11) más el detalle línea-a-línea de los 16 endpoints que el archivo canon todavía no tiene. Además, se confirmó con el PM un hecho de arquitectura que tampoco está en el canon todavía: **el flujo transaccional de cobro consulta la misma API que el Admin** para resolver comisión/plazo en el momento de un cobro real — dato relevante para cualquiera que toque este contrato (cualquier cambio arriesga romper el path transaccional, no solo el Admin).

## Conocimiento nuevo a mergear (agregar a `gestion_convenios_comisiones.md`, no reemplazar lo ya escrito)

**3 hallazgos nuevos, a sumar a la lista de "Gaps/ambigüedades del contrato" ya existente (que hoy llega hasta el punto 8):**

9. `ValorComision` tiene `minimum: 0, maximum: 1` en el schema, pero ningún `description` aclara la unidad — a confirmar si `0.025` = 2,5% siempre, o si hay algún caso donde ese rango de 0 a 1 significa otra cosa.
10. Existen **dos endpoints solapados** para "actualizar una comisión de comercio": `PUT /comercios/{id}/comisiones/{idComisionComercio}` (body: solo `{id}`) y `PUT /comercios/{idComercio}/comision/{idComision}` (body: `{nuevoValor, comisionNombreGrupo, comisionTipoId}`) — nombres de path casi idénticos (singular/plural), payloads incompatibles entre sí, sin indicio en el spec de cuál es la vigente o si una está deprecada.
11. No existe ningún `PUT` para `ComercioConvenio` — a diferencia de `Convenio` (que sí tiene `PUT /convenios/{codConvenio}`), el nivel comercio-convenio solo ofrece alta y baja (`POST`/`DELETE`). Cualquier "edición" de un override existente requiere inferir un patrón de baja+alta, no documentado como tal en el contrato.

**Dato de arquitectura nuevo, a sumar a "Por qué importa" o como sección propia:**

El flujo transaccional de cobro (el que decide qué comisión/plazo aplicar a una operación real) consulta la **misma API** (`Shared.Comercio.Api`) que usa el Admin — confirmado explícitamente por el PM (Pablo Gomes) el 2026-08-27. En la práctica, esto significa que `GET /comercio/{id}/convenios/{codEntidad}` (el único endpoint con schema de respuesta real y fusionado, ya documentado en el archivo) probablemente sea el que ese flujo consulta — cualquier cambio de contrato ahí arriesga romper el path transaccional, no solo el Admin. Insumo directo para cualquier evolución futura de este contrato, no solo para `convenios_configuracion`.

**Inventario completo de los 16 endpoints** (con línea de origen del spec, autenticación exacta, y los 7 headers opcionales repetidos en todas las operaciones): queda documentado con el mayor detalle en `1_proyectos/convenios_configuracion/artefactos/convenios_configuracion-solution.md` (Sección 4) — este item resume las novedades respecto de lo ya mergeado, no repite lo que `gestion_convenios_comisiones.md` ya tiene bien.

## Por qué importa

`gestion_convenios_comisiones.md` es la única fuente canon de este contrato — que se haya mergeado con una destilación parcial ("en curso") es una brecha real: cualquier sesión futura que lo use tal como está hoy no sabe que faltan 3 hallazgos ni que el flujo transaccional depende del mismo contrato. Cerrar esta brecha ahora evita que quede la impresión de que el archivo canon está completo cuando no lo está.

## Estado de propagación

Pendiente de `/context_push` + `/context_merge`. El item original que dio origen a este archivo ya fue ingerido y archivado en `4_archivos/contexto_ingestado/2026-08-24_adquirencia_api_convenios_comercios_contrato_real.md` — este es un item nuevo y separado (no se edita un item ya archivado), con `tipo_destino: actualizar` sobre el mismo archivo canon.
