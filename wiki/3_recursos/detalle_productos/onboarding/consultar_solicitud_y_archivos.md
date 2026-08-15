# Consultar Solicitud de Onboarding y sus Archivos

> Estado: en producción. Reubicado desde `detalle_productos/onboarding/manuales_operativos.md §1` en la reestructuración PARA en cascada (2026-08-12). Alcance: informativo y apto para desarrollo. Objetivo: guiar al desarrollador de la Organización que necesita recuperar información o archivos de un onboarding previamente realizado.

## Consultar solicitud de onboarding por id

Devuelve toda la información de una solicitud de onboarding previamente creada.

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}` |
| PRODUCCIÓN | GET | `https://api.bindpagos.com.ar/orquestador/api/v1/solicitudes/{id}` |

**Request:** `id` (string, path, REQUERIDO) — identificador único del onboarding (GUID).

El response incluye datos completos de la solicitud: datos personales (nombre, DNI, domicilio, fecha de nacimiento), estado del documento (`documentoValido`, `documentoExiste`, vencimiento), validaciones (OTP email/SMS, listas negra/blanca, `esPEP`/`esFatca`/`esOcde`/`esUif`, `errorAfip`/`errorNosis`/`errorUif`/`errorWorldsys`, `puntajeRiesgo`), datos de wallet asociada (`cuenta`, `cuentaCvu`, `cvuCreado`, `idOrganizacion`), comercio asociado (si aplica), y tres colecciones históricas: `archivos[]` (documentos adjuntos con id/nombre/tipo/fecha), `historial[]` (cambios de estado con fecha/hora/estado anterior/comentario) y `movimientoSolicitud[]` (acciones técnicas del flujo: `update-morfologia`, `update-renaper`, `update-lista-negra`, `send-email-otp`, `alta-Wallet`, `alta-cuenta-qr`, etc., cada una con timestamp y estado).

También trae `json[]`: el detalle crudo de cada validación externa (PDF417 del DNI, respuesta completa de Renaper, Nosis, DDJJ, AFIP, UIF, Matriz de Riesgo, Alta Wallet, Alta Comercio, Asignar Comercio, Informar entidad) — útil para diagnosticar por qué una solicitud tomó una decisión puntual.

## Consultar solicitud de onboarding por id externo

Mismo response que arriba, consultando por el id de referencia externo que indicó la entidad al crear la solicitud.

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}/externalRefid` |
| PRODUCCIÓN | GET | `https://api.bindpagos.com.ar/orquestador/api/v1/solicitudes/{id}/externalRefid` |

## Obtener archivo por id

Devuelve la información de un archivo asociado a una solicitud de onboarding.

| Ambiente | Método | URL |
|---|---|---|
| STAGING | GET | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/archivos/{id}` |
| PRODUCCIÓN | GET | `https://api.bindpagos.com.ar/orquestador/api/v1/archivos/{id}` |

**Request:** `id` (string, path, REQUERIDO) — identificador del archivo (`archivos[].id` de la consulta de solicitud).

**Response:** `id`, `nombre` (con extensión), `tipo` (código de tipo de archivo), `fecha`, `hora` (UTC-3), `contenido` (base64 del archivo), `legajoDigitalUrl` (link al legajo digital — acceso solo Bind PSP o entidad con el servicio contratado).

## Ver también
- [configuracion_alta_wallet.md](configuracion_alta_wallet.md) — cómo se configura el paso de alta wallet que aparece en `movimientoSolicitud[]`.
- [detalle_productos/wallet/comercio_qr_acreditacion_wallet.md](../wallet/comercio_qr_acreditacion_wallet.md) — alta de comercio, mencionada en `archivos[]`/`json[]` cuando el onboarding incluye comercio.

---
*Última actualización: 2026-08-12 — Reubicado desde `detalle_productos/onboarding/manuales_operativos.md §1` (reestructuración PARA en cascada). Ejemplos JSON reales condensados, campos de referencia sin cambios.*
