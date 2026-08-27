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

## Por qué importa

Es la fuente primaria para diseñar cualquier rediseño de la herencia de convenios (`1_proyectos/convenios_configuracion/`, en discovery de `/idea_solution` al momento de esta captura). El PM subió el spec completo (`entidad-comercio-v1.json`, OpenAPI 3.0.1) el 2026-08-24; el archivo fuente completo queda en `1_proyectos/convenios_configuracion/referencias/convenios_configuracion-openapi_comercios_v1.json` para cualquier sesión futura que necesite volver al detalle línea por línea (parámetros de query completos, schemas de error, etc. — este item resume lo esencial, no lo reemplaza).

## Ver también

- [configuracion_de_entidades.md §4](configuracion_de_entidades.md) — descripción previa (informal, en disputa) del mecanismo de herencia de convenios.
- [mejoras_admin_backoffice_prd88.md §2](mejoras_admin_backoffice_prd88.md) — Epic AD-8 (`canal_entidad`/`canal_comercio`), también en disputa como referencia de patrón reusable para convenios.

---
*Última actualización: 2026-08-27 — `/context_merge`: archivo nuevo, item de `contexto_vivo/` (spec OpenAPI, 2026-08-24). Contradice la caracterización previa de `configuracion_de_entidades.md §4` y `mejoras_admin_backoffice_prd88.md §2` — gap escalado, ver `gaps_y_preguntas.md`.*
