# GET — Consultar Solicitud por ID (Validación por Partes)

> Fuente: https://psp.bind.com.ar/developers/apis/consultar-solicitud-por-id-copy
> Producto: Onboarding — Validación por partes

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
| `id` | string (path) | REQUIRED | Identificador de la solicitud de onboarding. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/solicitudes/12345' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Ocp-Apim-Subscription-Key: 123455f9d2544347b07dfb37be925c3e'
```

## Response — Campos principales

| Campo | Tipo | Req | Descripción |
|-------|------|-----|-------------|
| `id` | string | REQ | UUID de la solicitud de onboarding. |
| `entidadId` | string | REQ | UUID de la entidad a la que pertenece la solicitud. |
| `estado` | int | REQ | `1`=Pendiente, `2`=Aprobada, `3`=Rechazada, `4`=Validación Manual, `5`=Pendiente credenciales, `6`=Error alta, `7`=Aprobado a Revisar, `8`=Aprobado sin notificar, `9`=Vencida, `10`=Menor pendiente, `11`=Menor habilitado |
| `fecha` | string | REQ | Fecha de generación del registro. |
| `hora` | string | REQ | Hora exacta de creación del trámite. |
| `apellidos` | string | REQ | Apellidos del usuario. |
| `nombres` | string | REQ | Nombres completos del titular. |
| `documento` | string | REQ | DNI del usuario. |
| `documentoEjemplar` | string | REQ | Letra del ejemplar del DNI. |
| `documentoEmision` | string | REQ | Fecha de emisión del ejemplar. |
| `documentoExpiracion` | string | REQ | Fecha de expiración del DNI. |
| `documentoTramite` | string | REQ | Número de trámite del DNI. |
| `documentoValido` | boolean | REQ | Si el documento superó controles lógicos. |
| `documentoExiste` | boolean | REQ | Si el documento existe y es legítimo. |
| `documentoListaBlanca` | boolean | REQ | Si el DNI está en lista blanca. |
| `documentoListaNegra` | boolean | REQ | Si el DNI está bloqueado en listas de fraude. |
| `documentoListaNegraBind` | string | OPT | Si el DNI está en listas negras internas de Bind. |
| `fallecido` | boolean | REQ | Si figura como fallecido en Renaper. |
| `cuil` | string | REQ | CUIT/CUIL sin guiones. |
| `cuilCalculado` | boolean | REQ | Si el CUIL fue calculado algorítmicamente. |
| `genero` | string | REQ | `"M"` / `"F"` / `"X"` |
| `fechaNacimiento` | string | REQ | Fecha de nacimiento. |
| `email` | string | REQ | Correo electrónico. |
| `emailListaNegra` | boolean | REQ | Si el email está en lista negra de fraude. |
| `telefono` | string | REQ | Número telefónico. |
| `telefonoListaNegra` | boolean | REQ | Si el teléfono está en lista negra de fraude. |
| `estadoCivil` | string | REQ | Estado civil. |
| `nacionalidad` | string | REQ | Nacionalidad. |
| `calle` | string | REQ | Calle del domicilio. |
| `numeracion` | string | REQ | Numeración del domicilio. |
| `departamento` | string | OPT | Departamento del domicilio. |
| `piso` | string | OPT | Piso del domicilio. |
| `ciudad` | string | REQ | Ciudad del domicilio. |
| `localidad` | string | REQ | Localidad. |
| `municipalidad` | string | REQ | Municipio. |
| `codigoPostal` | string | REQ | Código postal. |
| `provincia` | string | REQ | Provincia. |
| `pais` | string | REQ | País. |
| `cbu` | string | REQ | CBU externa vinculada o informada. |
| `esPEP` | boolean | OPT | Si es Persona Políticamente Expuesta. |
| `esFatca` | boolean | OPT | Si es sujeto FATCA. |
| `esOcde` | boolean | OPT | Si responde a criterios OCDE. |
| `esUif` | boolean | OPT | Si es Sujeto Obligado ante la UIF. |
| `aceptaTyc` | boolean | REQ | Si aceptó los TyC. |
| `aceptaTycComitente` | boolean | OPT | Si aceptó TyC de cuenta comitente. |
| `addaliaPruebaVida` | boolean | REQ | Resultado de prueba de vida biométrica. |
| `addaliaValidacionFacial` | boolean | REQ | Resultado de comparación facial contra Renaper. |
| `errorNosis` | boolean | REQ | Si hubo error al consultar Nosis. |
| `errorUif` | boolean | REQ | Si hubo error al verificar UIF. |
| `uifSujetoObligado` | boolean | REQ | Si el usuario es Sujeto Obligado ante la UIF. |
| `worldsysTerrorista` | boolean | REQ | Si coincide con listas de terrorismo en Worldsys. |
| `worldsysPep` | boolean | REQ | Si figura como PEP en Worldsys. |
| `errorWorldsys` | boolean | REQ | Si hubo error en comunicación con Worldsys. |
| `puntajeRiesgo` | int | REQ | Puntaje consolidado de la matriz de riesgo. |
| `ip` | string | OPT | IP desde la que se inició el onboarding. |
| `dispositivo` | string | OPT | Huella digital del dispositivo utilizado. |
| `afipActividad` | string | OPT | Actividad económica del CUIT en AFIP. |
| `externalRefId` | string | OPT | Referencia externa de la entidad. |
| `step` | string | REQ | Nombre técnico del último paso procesado. |
| `tipoSolicitud` | string | REQ | Código del flujo de onboarding configurado. |
| `fechaActualizacion` | string | REQ | Fecha y hora ISO-8601 de la última modificación. |
| `legajoDigitalTramiteId` | string | REQ | Identificador del trámite de legajo digital interno. |

### Campos comerciales (opcionales)

| Campo | Descripción |
|-------|-------------|
| `idComercio` | Identificador del comercio. |
| `codigoCaja` | Código de la caja. |
| `codigoSucursal` | Código de la sucursal. |
| `nombreFantasia` | Nombre de fantasía del comercio. |
| `calleComercio` / `numeracionComercio` / `departamentoComercio` / `codigoPostalComercio` / `ciudadComercio` / `municipalidadComercio` / `pisoComercio` / `provinciaComercio` / `paisComercio` | Domicilio comercial. |

### Objeto `wallet`

| Campo | Tipo | Req | Descripción |
|-------|------|-----|-------------|
| `wallet.cuenta.id` | int | REQ | ID de la cuenta en Wallet. |
| `wallet.cuenta.cuitCuil` | string | REQ | CUIT/CUIL del titular. |
| `wallet.cuenta.nombre` | string | REQ | Nombres del titular. |
| `wallet.cuenta.apellido` | string | REQ | Apellidos del titular. |
| `wallet.cuenta.razonSocial` | string | OPT | Razón social (cuentas corporativas). |
| `wallet.cuenta.email` | string | REQ | Email asociado a la cuenta. |
| `wallet.cuenta.celular` | string | REQ | Celular vinculado a la cuenta. |
| `wallet.cuenta.habilitado` | boolean | REQ | Si la cuenta está habilitada. |
| `wallet.cuentaCvu.id` | int | REQ | ID del CVU creado. |
| `wallet.cuentaCvu.cvu` | string | REQ | CVU de 22 dígitos. |
| `wallet.cuentaCvu.nombre` | string | REQ | Nombre del titular en Coelsa. |
| `wallet.cuentaCvu.motivoError` | string | OPT | Error al aprovisionar el CVU. |
| `wallet.cuentaInvestment.id` | int | OPT | ID de la cuenta comitente. |
| `wallet.cvuCreado` | boolean | REQ | Si el CVU fue creado exitosamente. |
| `wallet.idOrganizacion` | int | REQ | ID de la organización. |
| `wallet.cuentaComitenteCreado` | boolean | OPT | Si la cuenta comitente fue creada. |

### Array `archivos[]`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | UUID del archivo. |
| `nombre` | string | Nombre del archivo con extensión. |
| `tipo` | string | Tipos: `"Documento - Frente"`, `"Documento - Dorso"`, `"Renaper"`, `"Worldsys"`, `"Nosis"`, `"Enrollment Create"`, `"Validar Enrollamiento"`, `"SelfieSN"`, `"DDJJ"`, `"Terminos & Condiciones"` |
| `fecha` | string | Fecha de carga. |

### Array `historial[]`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | ID de la línea de auditoría. |
| `fecha` | string | Fecha del cambio de estado. |
| `hora` | string | Hora del cambio de estado. |
| `estadoAnterior` | int | Estado previo. |
| `estado` | int | Nuevo estado. |
| `usuario` | string | Operador (si fue manual). |
| `comentario` | string | Motivo del cambio. |

### Array `json[]`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | ID del registro JSON. |
| `tipo` | string | Tipos: `"PDF417"`, `"Renaper"`, `"Worldsys"`, `"Nosis"`, `"Validar Enrollamiento"`, `"Enrollment Create"`, `"Consultar Enrollamiento"`, `"DDJJ"`, `"Uif"`, `"Matriz de Riesgo"`, `"Alta Wallet"` |
| `fecha` | string | Fecha de ejecución de la consulta. |
| `contenido` | string | Respuesta nativa del proveedor serializada como string. |

### Array `movimientoSolicitud[]`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | ID del movimiento del workflow. |
| `accion` | string | Nombre técnico de la acción ejecutada. |
| `horaMovimiento` | string | Marca temporal del procesamiento. |
| `estado` | int | Estado asignado tras el paso. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Consulta exitosa |
| `204` | No se encontró una solicitud con el ID indicado |
| `400` | Algún campo del request no es válido |
| `401` | Token de autenticación inválido |
