# GET — Consultar Solicitud por ID (Registro Único)

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-solicitud-por-id
> Producto: Onboarding — Registro único

## Descripción

Devuelve información asociada a la solicitud y que se fue registrando en cada validación a servicios externos. Algunos campos pueden ser vacíos ya que no aplican para el flujo de onboarding en cuestión.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `GET` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/{id}` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | string | REQUIRED | Identificador de la solicitud de onboarding. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/12345' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Ocp-Apim-Subscription-Key: {{subscription_key}}'
```

## Response — Campos principales

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | UUID de la solicitud de onboarding. |
| `entidadId` | string | UUID de la entidad a la que pertenece la solicitud. |
| `estado` | int | `1`=Pendiente, `2`=Aprobada, `3`=Rechazada, `4`=Validación Manual, `5`=Pendiente credenciales, `6`=Error alta, `7`=Aprobado a Revisar, `8`=Aprobado sin notificar, `9`=Vencida, `10`=Menor pendiente, `11`=Menor habilitado |
| `fecha` | string | Fecha de generación del registro. |
| `hora` | string | Hora exacta de creación del trámite. |
| `apellidos` | string | Apellidos del usuario. |
| `nombres` | string | Nombres completos del titular. |
| `documento` | string | DNI del usuario. |
| `documentoTramite` | string | Número de trámite del DNI. |
| `cuil` | string | CUIT/CUIL del usuario sin guiones. |
| `cuilCalculado` | boolean | Si el CUIL fue calculado algorítmicamente. |
| `genero` | string | Género: `"M"` / `"F"` / `"X"` |
| `fechaNacimiento` | string | Fecha de nacimiento del titular. |
| `email` | string | Correo electrónico del usuario. |
| `telefono` | string | Número telefónico del usuario. |
| `estadoCivil` | string | Estado civil del usuario. |
| `nacionalidad` | string | Nacionalidad del usuario. |
| `documentoValido` | boolean | Si el documento superó los controles lógicos. |
| `documentoExiste` | boolean | Si el documento existe y es legítimo. |
| `fallecido` | boolean | Si la persona figura como fallecida en Renaper. |
| `addaliaPruebaVida` | boolean | Resultado del control biométrico de prueba de vida. |
| `addaliaValidacionFacial` | boolean | Resultado de la comparación facial contra Renaper. |
| `errorNosis` | boolean | Si hubo error al consultar Nosis. |
| `errorUif` | boolean | Si hubo error al verificar UIF. |
| `uifSujetoObligado` | boolean | Si el usuario es Sujeto Obligado ante la UIF. |
| `worldsysTerrorista` | boolean | Si el CUIT coincide con listas de terrorismo en Worldsys. |
| `worldsysPep` | boolean | Si el CUIT figura como PEP en Worldsys. |
| `errorWorldsys` | boolean | Si hubo error en la comunicación con Worldsys. |
| `puntajeRiesgo` | int | Puntaje consolidado de la matriz de riesgo. |
| `esPEP` | boolean | Si el titular es Persona Políticamente Expuesta. |
| `esFatca` | boolean | Si el titular es sujeto FATCA. |
| `esOcde` | boolean | Si el titular responde a criterios OCDE. |
| `esUif` | boolean | Si el usuario es Sujeto Obligado ante la UIF. |
| `aceptaTyc` | boolean | Si el usuario aceptó los TyC. |
| `externalRefId` | string | Referencia externa de la entidad. |
| `step` | string | Nombre técnico del último paso procesado. |
| `tipoSolicitud` | string | Código del flujo de onboarding configurado. |
| `fechaActualizacion` | string | Fecha y hora ISO-8601 de la última modificación. |
| `wallet.cuenta.id` | int | ID de la cuenta creada en Wallet. |
| `wallet.cuenta.cuitCuil` | string | CUIT/CUIL del titular. |
| `wallet.cuenta.habilitado` | boolean | Si la cuenta está habilitada para operar. |
| `wallet.cuentaCvu.cvu` | string | CVU de 22 dígitos asignado. |
| `wallet.cvuCreado` | boolean | Si el CVU fue creado exitosamente. |
| `wallet.cuentaComitenteCreado` | boolean | Si la cuenta comitente fue creada exitosamente. |
| `archivos[]` | array | Documentos adjuntos al legajo digital. Tipos: `"Documento - Frente"`, `"Documento - Dorso"`, `"Renaper"`, `"Worldsys"`, `"Nosis"`, `"SelfieSN"`, `"DDJJ"`, `"Terminos & Condiciones"`, etc. |
| `historial[]` | array | Auditoría de cambios de estado de la solicitud. |
| `json[]` | array | Payloads crudos de validadores externos. Tipos: `"PDF417"`, `"Renaper"`, `"Worldsys"`, `"Nosis"`, `"Uif"`, `"Matriz de Riesgo"`, `"Alta Wallet"`, etc. |
| `movimientoSolicitud[]` | array | Logs del orquestador de cada acción ejecutada en el flujo. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No se encontró una solicitud con el ID indicado |
| `400` | Algún campo del request no es válido |
| `401` | Token de autenticación inválido |
