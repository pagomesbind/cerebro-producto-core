# EVENT — Webhook: Aviso de Onboarding Aprobado

> Fuente: https://psp.bind.com.ar/developers/apis/aviso-de-onboarding-aprobado
> Producto: Onboarding — Registro único

## Descripción

Se envía un POST a un endpoint expuesto por la Entidad cada vez que ocurre un onboarding **APROBADO**, con información general del usuario.

Cada webhook debe responderse con HTTP 200. De lo contrario, el envío ingresará en un esquema de reintentos.

La URL de destino se configura en el backoffice del Onboarding. Algunos campos pueden ser vacíos si no aplican para el flujo de onboarding en cuestión.

## Campos del Payload

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `idSolicitud` | string | Identificador interno de la solicitud. |
| `habilitado` | boolean | Si el comercio está habilitado. |
| `fecha` | string | Fecha en que se realizó la solicitud. |
| `hora` | string | Hora en que se realizó la solicitud. |
| `apellidos` | string | Apellidos del usuario onboardeado. |
| `nombres` | string | Nombres del usuario onboardeado. |
| `cuil` | string | CUIL/CUIT del usuario. |
| `documento` | string | DNI del usuario. |
| `documentoEjemplar` | string | Letra del ejemplar del DNI. |
| `documentoEmision` | string | Fecha de emisión del ejemplar del DNI. |
| `documentoExpiracion` | string | Fecha de expiración del ejemplar del DNI. |
| `documentoTramite` | string | Número de trámite del DNI. |
| `fechaNacimiento` | string | Fecha de nacimiento. |
| `genero` | string | Género. |
| `nacionalidad` | string | País de nacimiento. |
| `calle` | string | Calle del domicilio. |
| `numeracion` | string | Numeración del domicilio. |
| `departamento` | string | Departamento del domicilio. |
| `piso` | string | Piso del domicilio. |
| `ciudad` | string | Ciudad del domicilio. |
| `localidad` | string | Localidad del domicilio. |
| `municipalidad` | string | Municipio del domicilio. |
| `codigoPostal` | string | Código postal del domicilio. |
| `provincia` | string | Provincia del domicilio. |
| `pais` | string | País del domicilio. |
| `email` | string | Correo electrónico del usuario. |
| `telefono` | string | Teléfono del usuario. |
| `nombreFantasia` | string | Nombre de fantasía del comercio. |
| `calleComercio` | string | Calle del domicilio comercial. |
| `numeracionComercio` | string | Numeración del domicilio comercial. |
| `departamentoComercio` | string | Departamento comercial. |
| `codigoPostalComercio` | string | Código postal comercial. |
| `ciudadComercio` | string | Ciudad comercial. |
| `municipalidadComercio` | string | Municipio comercial. |
| `pisoComercio` | string | Piso comercial. |
| `provinciaComercio` | string | Provincia comercial. |
| `paisComercio` | string | País comercial. |
| `afipActividad` | string | Actividad del CUIT en AFIP. |
| `externalRefid` | string | Identificador externo de la entidad. |
| `wallet.cuenta.id` | int | ID de la cuenta creada en Wallet. |
| `wallet.cuenta.cuitCuil` | string | CUIT/CUIL del titular. |
| `wallet.cuenta.nombre` | string | Nombres del titular. |
| `wallet.cuenta.apellido` | string | Apellidos del titular. |
| `wallet.cuenta.email` | string | Email de la cuenta. |
| `wallet.cuenta.celular` | string | Celular de la cuenta. |
| `wallet.cuenta.habilitado` | boolean | Si la cuenta está habilitada. |
| `wallet.cuentaCvu.id` | int | ID del CVU creado. |
| `wallet.cuentaCvu.cvu` | string | CVU de 22 dígitos. |
| `wallet.cuentaCvu.nombre` | string | Nombre del titular en Coelsa. |
| `wallet.cvuCreado` | boolean | Si el CVU fue creado exitosamente. |
| `wallet.idOrganizacion` | int | ID de la organización. |

## Ejemplo JSON real

```json
{
  "idSolicitud": "eba47c9e-6588-4e7c-5597-08dec896f7c3",
  "idComercio": "C23823",
  "habilitado": false,
  "fecha": "12/06/2026",
  "hora": "12:45",
  "apellidos": "HOLA",
  "nombres": "PAOLA CECILIA",
  "cuil": "27319012340",
  "documento": "31901234",
  "documentoEjemplar": "A",
  "documentoEmision": "18/10/2012",
  "documentoExpiracion": "18/10/2027",
  "documentoTramite": "00143211234",
  "calle": "BANDERA DE LOS ANDES",
  "ciudad": "RODEO DE LA CRUZ",
  "codigoPostal": "5525",
  "departamento": null,
  "fechaNacimiento": "30/07/1986",
  "genero": "F",
  "localidad": "RODEO DE LA CRUZ",
  "municipalidad": "GUAYMALLéN",
  "nacionalidad": "ARGENTINA",
  "numeracion": "1234",
  "pais": "ARGENTINA",
  "email": "123@123.com.ar",
  "telefono": "2615611234",
  "externalRefid": null,
  "Wallet": {
    "cuenta": {
      "id": 1509399,
      "cuitCuil": "27319012340",
      "nombre": "PAOLA CECILIA",
      "apellido": "HOLA",
      "razonSocial": null,
      "email": "123@123.com.ar",
      "celular": "2615611234",
      "habilitado": true
    },
    "cuentaCvu": {
      "id": 173453,
      "cvu": "000053260950001509123",
      "nombre": "PAOLA CECILIA HOLA",
      "motivoError": null
    },
    "cvuCreado": true,
    "idOrganizacion": 78,
    "pendienteTutor": false
  }
}
```
