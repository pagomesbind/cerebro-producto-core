# Gestión de Convenios y Comisiones — Contrato Real de la API (Convenio + ComercioConvenio)

> Estado: documentación desactualizada / en disputa — ver nota de contradicción abajo. El contrato de API en sí está en producción (es lo que hoy usa el Admin/Centralizador de Cobro); lo que está en disputa es la caracterización previa e informal del mecanismo de herencia de convenios en otros dos documentos de este módulo.
>
> Fuente: `/idea_solution` — discovery técnico del proyecto `convenios_configuracion`; spec OpenAPI 3.0.1 "Api Comercios" (`Shared.Comercio.Api`, release 30/7/2026) aportado por el PM (Pablo Gomes), destilado vía subagente. Item capturado 2026-08-24.

## ⚠️ Contradicción con otros documentos de este módulo — leer antes de usar

Este archivo **reemplaza** la descripción informal que tenían [`configuracion_de_entidades.md §4`](configuracion_de_entidades.md) y [`mejoras_admin_backoffice_prd88.md §2`](mejoras_admin_backoffice_prd88.md) sobre el mecanismo de herencia de convenios entidad→comercio — ambos documentos describían el mecanismo **sin conocer el contrato real** de la API. Ver la nota de contradicción espejada en cada uno de esos dos archivos. **Gap escalado a `gaps_y_preguntas.md` — pendiente de decisión del usuario**, acá no se elige una versión "ganadora".

## Qué es

Contrato real (OpenAPI 3.0.1, servidor de staging `https://gw-staging-qrbind.epays.services/bindentidad-comercio/v1`) de los 16 endpoints bajo el tag `Convenios - Comercios` de la "Api Comercios" (`Shared.Comercio.Api`) — la API que hoy usa el Admin/Centralizador de Cobro para gestionar convenios (comisión, plazo de acreditación, canal, forma de pago) a nivel Entidad y Comercio. Autenticación: API key vía header `Ocp-Apim-Subscription-Key` o query `subscription-key` (típico API Management de Azure) — la resolución de negocio (a qué entidad/comercio corresponde la llamada) va por headers propios (`x-entidad`, `x-aplicacion`, etc.), no por el esquema de seguridad.

## Modelo de datos confirmado

```
Convenio (maestro, tabla propia)
  Codigo, Descripcion, TipoComision, ValorComision, Acreditacion, UniAcreditacion,
  MontoMin, MontoMax, CodCanal, FPago, VigDesde, VigHasta
  — CRUD: POST /convenios, PUT /convenios/{codConvenio}, DELETE /convenios/{id}, GET /convenios (sin 200 documentado, ver gap)

Entidad → convenios
  Único campo expuesto: CodConvenioGrupo (string, maxLength 10)
  — POST/PUT /entidad/{id}/convenios setea ese campo. NO hay ningún endpoint que gestione
    el "grupo" como recurso (no se puede listar qué Convenios pertenecen a un grupo, ni
    asociar un Convenio a un grupo al crearlo) — el campo es una caja negra desde esta API.

Comercio → Convenio (ComercioConvenio, la relación real)
  POST/DELETE /comercio/{id}/conveniocomercio/{codConvenio}  (y variante .../conveniocomercioQR/{codConvenio},
    contractualmente idéntica — la diferencia de canal no es visible en el contrato)
  Body de alta: CodEntidad (requerido), VigDesde (requerido), VigHasta, y los overrides
    OPCIONALES ValorComision / Acreditacion / UniAcred.
  El comercio NO puede overridear CodCanal/FPago/MontoMin/MontoMax/TipoComision — esos
    campos son siempre los del Convenio maestro.

Lectura con herencia expuesta (GET /comercio/{id}/convenios/{codEntidad}):
  Por cada convenio-comercio devuelve EN PARALELO:
    ValorComision / Acreditacion / UniAcred        → valor del Convenio maestro (heredado)
    ValorComisionCom / AcreditacionCom / UniAcredCom → valor efectivo a nivel comercio
    FromCommerce: boolean                            → true si el valor efectivo vino de
                                                        un override propio del comercio
```

**Lectura de negocio:** el contrato ya modela exactamente el par "valor heredado / valor con override + flag de origen" que el negocio pide (ver ejemplo canónico de `1_proyectos/convenios_configuracion/proyecto.md`, Gate 1) — la pregunta abierta (no resoluble solo con el spec) es si `ValorComision` en esa respuesta es un **join en vivo** contra la fila actual del Convenio maestro (en cuyo caso editar el Convenio maestro ya propagaría en tiempo real a todo comercio sin override) o si es una **copia congelada** al momento del alta del `ComercioConvenio`. El comportamiento real reportado hoy por el equipo operativo (herencia = copia única al crear el comercio, sin retroactividad) sugiere que en la práctica el override se completa siempre al crear el link — pero el contrato en sí no lo impide ni lo confirma. Queda como pregunta técnica a validar contra staging/backend antes de decidir el rediseño.

## Gaps/ambigüedades del contrato (para quien lo use en un desarrollo futuro)

1. Sin API para gestionar "grupos de convenios" como recurso — solo el campo `CodConvenioGrupo` en Entidad.
2. `GET /convenios` (listado maestro) no documenta ningún `200` en el spec.
3. `GET /entidad/{id}/convenios` tiene filtros de query ricos pero un `200` tipado como `string` plano, no como array — inconsistente con su equivalente en Comercio.
4. `conveniocomercio` y `conveniocomercioQR` son contractualmente idénticos (mismo body, misma respuesta) — la diferenciación de canal no se ve en el contrato.
5. Naming inconsistente del path param de convenio entre operaciones (`codConvenio` en `PUT /convenios/{codConvenio}`, `id` en `DELETE /convenios/{id}`) — no confirmado si son el mismo valor de negocio.
6. Ningún body de alta/modificación declara campos `required` (ni siquiera `Codigo` en alta de Convenio) — probablemente el spec no refleja las validaciones reales del backend.
7. `CodCanal`/`FPago`/`TipoComision` son strings con `maxLength` pero sin `enum` — los valores válidos no están documentados en esta API.
8. El modelo general de Comercio (`GET /comercios/{id}` → `ComercioDto`) NO trae convenios embebidos — es un dominio de datos separado, requiere llamada aparte. `ComercioDto.comisiones` es un mecanismo de comisión genérico distinto (`Comision`/`Comisiones`, tags separados en el spec) sin relación de datos con `Convenio`/`ComercioConvenio` — no confundir los dos.
9. `ValorComision` tiene `minimum: 0, maximum: 1` en el schema, pero ningún `description` aclara la unidad — a confirmar si `0.025` = 2,5% siempre, o si hay algún caso donde ese rango de 0 a 1 significa otra cosa.
10. Existen **dos endpoints solapados** para "actualizar una comisión de comercio": `PUT /comercios/{id}/comisiones/{idComisionComercio}` (body: solo `{id}`) y `PUT /comercios/{idComercio}/comision/{idComision}` (body: `{nuevoValor, comisionNombreGrupo, comisionTipoId}`) — nombres de path casi idénticos (singular/plural), payloads incompatibles entre sí, sin indicio en el spec de cuál es la vigente o si una está deprecada.
11. No existe ningún `PUT` para `ComercioConvenio` — a diferencia de `Convenio` (que sí tiene `PUT /convenios/{codConvenio}`), el nivel comercio-convenio solo ofrece alta y baja (`POST`/`DELETE`). Cualquier "edición" de un override existente requiere inferir un patrón de baja+alta, no documentado como tal en el contrato.

## Confirmación de negocio del modelo de herencia (reunión "Análisis COBRO", 2026-08-27)

En la misma reunión donde el PM presentó el prototipo (ver `1_proyectos/convenios_configuracion/`), Pablo Gomes describió en palabras de negocio el mecanismo que el contrato real de API ya modela arriba:

- Las **entidades** establecen parámetros generales (ej. botón simple débito con 2% de comisión y 3 días de plazo) que se **heredan automáticamente** por los comercios nuevos creados bajo esa entidad.
- Modificar un parámetro puntual en un comercio (ej. cambiar la comisión de crédito de 1,3% a 99% en un comercio específico) crea una **regla específica que prevalece sobre la entidad** para ese comercio — coincide con el flag `FromCommerce` documentado arriba. Al intentar desactivar esa regla puntual, el sistema alerta y ofrece volver al valor heredado de la entidad o desactivar el canal completo.
- Las modificaciones a nivel comercio **no impactan** a la entidad matriz ni a otros comercios (que mantienen su herencia intacta). Un cambio global (ej. eliminar un medio de pago a nivel entidad) sí baja en cascada a los comercios sin excepciones propias; los que tienen configuración propia la conservan.
- Daniela Collia (Fintexa) advirtió que, aunque el panel visual muestra la edición de una sola línea, el backend genera un **nuevo registro por cada modificación** (crecimiento de datos, trazabilidad/auditoría) — el PM respondió que el volumen actual (~50 entidades operativas) mitiga el riesgo de escala y que los estados anulados conservan el historial.

Esta descripción de negocio es consistente con el modelo `Convenio`/`ComercioConvenio`/`FromCommerce` ya documentado arriba — no lo contradice, lo confirma desde otro ángulo (negocio vs. contrato técnico). No cierra por sí sola la pregunta abierta en [`gaps_y_preguntas.md`](../../../2_areas/gaps_y_preguntas.md) [2026-08-27] sobre si corresponde actualizar `configuracion_de_entidades.md §4` y `mejoras_admin_backoffice_prd88.md §2` para apuntar acá como fuente de verdad.

> Fuente: Reunión "Análisis COBRO" (2026-08-27) — mismo item de fuente que la confirmación de negocio de arriba, capturado independientemente por Nicolás Colón, 2026-09-02.

## Dato de arquitectura — el flujo transaccional usa el mismo contrato que el Admin

El flujo transaccional de cobro (el que decide qué comisión/plazo aplicar a una operación real) consulta la **misma API** (`Shared.Comercio.Api`) que usa el Admin — confirmado explícitamente por el PM (Pablo Gomes) el 2026-08-27. En la práctica, esto significa que `GET /comercio/{id}/convenios/{codEntidad}` (el único endpoint con schema de respuesta real y fusionado, ver arriba) probablemente sea el que ese flujo consulta — cualquier cambio de contrato ahí arriesga romper el path transaccional, no solo el Admin. Insumo directo para cualquier evolución futura de este contrato, no solo para `convenios_configuracion`.

## Por qué importa

Es la fuente primaria para diseñar cualquier rediseño de la herencia de convenios (`1_proyectos/convenios_configuracion/`, en discovery de `/idea_solution` al momento de esta captura). El PM subió el spec completo (`entidad-comercio-v1.json`, OpenAPI 3.0.1) el 2026-08-24; el archivo fuente completo queda en `1_proyectos/convenios_configuracion/referencias/convenios_configuracion-openapi_comercios_v1.json` para cualquier sesión futura que necesite volver al detalle línea por línea (parámetros de query completos, schemas de error, etc. — este item resume lo esencial, no lo reemplaza).

## Ver también

- [configuracion_de_entidades.md §4](configuracion_de_entidades.md) — descripción previa (informal, en disputa) del mecanismo de herencia de convenios.
- [mejoras_admin_backoffice_prd88.md §2](mejoras_admin_backoffice_prd88.md) — Epic AD-8 (`canal_entidad`/`canal_comercio`), también en disputa como referencia de patrón reusable para convenios.

---
*Última actualización: 2026-08-31 — `/context_merge`: inventario completo de los 16 endpoints (3 hallazgos nuevos H9-H11) y dato de arquitectura sobre el flujo transaccional, del cierre de `/idea_solution` de `convenios_configuracion` (2026-08-27). Enriquece, no reemplaza, la destilación parcial del 2026-08-27.*
