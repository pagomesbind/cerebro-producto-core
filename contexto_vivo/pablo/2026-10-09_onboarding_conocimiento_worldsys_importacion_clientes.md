---
id: 2026-10-09_onboarding_conocimiento_worldsys_importacion_clientes
pm: pablo
fecha_captura: 2026-10-09
fuente: "/idea_solution — mail de Matias Quimey Larumbe (Worldsys) del 2026-09-09 con la documentación técnica de importación de clientes (PDF de 28 págs.) y un JSON de ejemplo; contrastado con los endpoints /import/* del Swagger de ComplianceOne v1.0.0"
producto: onboarding
tema: Importación "Clientes" de Worldsys/ComplianceOne — cuerpo, equivalencias, campos no importables, entityId
tipo: conocimiento
destino_propuesto: wiki/3_recursos/detalle_productos/onboarding/integracion_worldsys_complianceone.md
tipo_destino: actualizar
contradice: "wiki/3_recursos/detalle_productos/onboarding/integracion_worldsys_complianceone.md — si describe la creación de persona con POST /profile/customers (cuerpo igual al PATCH), esa hipótesis queda superada: Worldsys indicó usar el cuerpo de la importación 'Clientes'"
confianza: media
estado: en_cola
merge_commit:
---

## Qué es

Worldsys (Matias Quimey Larumbe, mail del 2026-09-09) envió la "Documentación Técnica para Importación API" de la configuración **Clientes** y un JSON de ejemplo, para que Bind PSP vea los valores admitidos y el significado de cada campo (por ejemplo `tab2grp1ctl6`). Indicó: usar de esos documentos **solo el cuerpo** de la llamada; el endpoint y el resto de los parámetros son los del Swagger (el documento menciona `PUT https://bind_psp.apicompliance.worldsysweb.com/api/data/capture/v1/import`, que es de la versión 1). Las equivalencias y valores son los mismos que Worldsys maneja a nivel archivo (el CSV histórico de clientes del batch).

## Estructura

Cuerpo: `{ "configurationName": "Clientes", "item": { ...52 propiedades... } }`. Autenticación Bearer.

- **Obligatorias:** `identification` (string, máx. 128), `identificationTypeId` (`11` CUIT, `01`/`1` DNI, `00` otros), `personType` (`1`/`01` persona física, `2`/`02`/`PJ` jurídica, `00` N/A).
- **Importables opcionales:** `name` (256), `idTributaria` (128), `apellidoMaterno`/`apellidoPaterno`/`primerNombre`/`segundoNombre` (150), `fechaNacimiento` (`yyyy-MM-dd`), `lugarNacimiento` (50), `nacionalidadId` (ISO-2 más `N/A`), `sexoId` (`M`, `F`, `N/A`), `esPep`, `pepCargo` y `pepOrganismo` (100), `pepFechaAltaCargo`, `estadoCivilId` (1 soltero, 2 casado, 3 viudo, 4 divorciado, 5 concubino), `fechaConstitucionSociedad`, `fechaInscripcion`, `numeroInscripcion` (20), `email1`/`email2` (256), `phonePrefix1`/`phonePrefix2` (15), `phone1`/`phone2` (32), `esSujetoObligado`, `fechaIngreso`, `perfilTransaccional` y `perfilDocumental` (decimal), `dispositivo` (100), `entityId`, `isDeleted`, `deletionTime`.
- **No importables con esta configuración** ("no hay equivalencias configuradas"): `pepCaracterInvocadoId`, `pepPaisId`, `ocupacionId`, `condicionLaboralId`, `formaJuridicaId`, `tipoSociedadId`, `sucursalTransId`, `tipoSujetoObligadoId`, `actividadId`, `condicionFiscalId`, `oficialCuentaUserId`, `canalOperacionId`, `perfilInversorId`, `tab2grp1ctl5` (Canal de Captación), `tab2grp1ctl3` (Riesgo PLD), `tab2grp1ctl6` (Excluir cliente de alertas). `empresaTransId` tiene valor constante: no se envía.
- **`entityId`:** códigos propios de Worldsys por organización, con prefijo "Wallet - X" o "Comercios - X" (ejemplos: Credicuotas `A038`/`D`/`Cred`; Astropay `Astr`; Manteca `MANT`; BindX `BIND`). Hay organizaciones con varios códigos y la misma organización puede figurar como Wallet y como Comercios; cada organización nueva requiere que Worldsys cargue su equivalencia.
- **Errores (documento v1):** `200`, `400`, `401`, `403`, `409` (misma descripción que `400`), `500`, con cuerpo `{code, message, target, details[]}`; códigos `BadRequest`, `ConfigurationInvalidated`, `InvalidJsonDocument`, `RepositoryNotFound`, `SaveChangesFailed`, `ValidationException`.

## Cómo se usaría (inferencia de Bind, sin confirmar con Worldsys)

El Swagger tiene `POST /import/entity?templateId=` (un registro), `POST /import/bulk?templateId=` (lote) y `GET /import/template/{id}/metadata` (devuelve un `payload` de ejemplo), con `data` sin schema en la respuesta; `GET /import/process` cuenta `newRecords` y `updateRecords`, lo que sugiere semántica crear-o-actualizar. Falta el `templateId` de "Clientes". Si se confirma, reemplaza a `POST /profile/customers` (cuerpo sin documentar) como vía de alta online de la persona.

## Otros datos del mismo mail

- Actividades y domicilios corresponden a otros endpoints y estructuras (Worldsys pidió confirmar si se enviarán; el PM respondió que sí).
- Envío por ZIP: "no hay restricciones".
- Ambiente de pruebas: Worldsys lo gestionaría de forma temporal (no tienen uno incluido) y estimaba compartir el acceso a más tardar el viernes 2026-09-11. Al 2026-10-09 no hay constancia de entrega; el PM volvió a preguntar ese día.
- Costo: hay un costo asociado al storage; Worldsys lo revisa a nivel contractual para confirmar el tope incluido y el valor adicional.

Detalle completo del diseño que usa esto: análisis técnico-funcional de PRD-147 v3.0 (`wiki/1_proyectos/proyecto-onboarding-estrategico/prd-147_legajo_worldsys/artefactos/legajo_worldsys-solution.md`).
