# Endpoint — Crear cuenta comitente

> Fuente: https://psp.bind.com.ar/developers/apis/crear-cuenta-comitente
> Producto: Wallet — Cuenta remunerada

## Descripción

Crea una cuenta comitente. Puede crearse sólo la cuenta comitente para una cuenta con CVU existente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaYCVUConCuentaComitente` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `cuentaId` | int | REQUERIDO | Identificador de la cuenta para la cual se quiere crear la cuenta comitente. |
| `cuentaRemuneradaActiva` | boolean | REQUERIDO | Si la funcionalidad de cuenta remunerada debe estar activada o no. |
| `cuentaComitente` | object | REQUERIDO | Objeto con la información para dar de alta la cuenta comitente en el broker. |
| `cuentaComitente.persona.personaFisica` | boolean | REQUERIDO | Si el titular es persona física. Si es falso, se procesa como persona jurídica. |
| `cuentaComitente.persona.nombre` | string | REQUERIDO | Nombres del titular. Máx 80 chars. Sin números ni caracteres especiales. |
| `cuentaComitente.persona.apellido` | string | REQUERIDO | Apellidos del titular. Máx 80 chars. Sin números ni caracteres especiales. |
| `cuentaComitente.persona.nacionalidad` | string | REQUERIDO | Código ISO 3166-1 alfa-2 de 2 letras. Ej: `"AR"` |
| `cuentaComitente.persona.paisResidencia` | string | OPCIONAL | Código ISO 3166-1 alfa-2. |
| `cuentaComitente.persona.tipoIdentificacion` | string | REQUERIDO | Valor fijo: `"DNI"` |
| `cuentaComitente.persona.identificacion` | string | REQUERIDO | Número de DNI. Formato numérico sin guiones. |
| `cuentaComitente.persona.paisIdentificacion` | string | REQUERIDO | País de emisión del documento. Código ISO alfa-2. |
| `cuentaComitente.persona.estadoCivil` | string | OPCIONAL | Valores: `"SINGLE"`, `"WIDOWED"`, `"MARRIED"`, `"DIVORCED"`, `"CONCUBINAGE"`, `"OTHER"` |
| `cuentaComitente.persona.fechaNacimiento` | string | REQUERIDO | Formato ISO-8601 `YYYY-MM-DD`. El titular debe ser mayor de edad. |
| `cuentaComitente.persona.lugarNacimiento` | string | REQUERIDO | Código ISO alfa-2 del país de nacimiento. |
| `cuentaComitente.persona.genero` | string | REQUERIDO | Valores: `"M"` (Masculino), `"F"` (Femenino) |
| `cuentaComitente.persona.informacionFiscal.tipo` | string | REQUERIDO | Valor fijo: `"CUIT"` |
| `cuentaComitente.persona.informacionFiscal.numero` | string | REQUERIDO | CUIT/CUIL de 11 dígitos sin guiones. |
| `cuentaComitente.persona.informacionFiscal.actividadComercial` | string | REQUERIDO | Código ARCA de 6 chars o código especial de ocupación (1-2 dígitos). Ej: `"939030"`, `"11"` |
| `cuentaComitente.persona.informacionFiscal.pep.esPep` | boolean | REQUERIDO | Si la persona es Políticamente Expuesta. |
| `cuentaComitente.persona.informacionFiscal.pep.descripcion` | string | REQUERIDO | Cargo PEP. Puede ser vacío si esPep es falso. No puede ser null. |
| `cuentaComitente.persona.informacionFiscal.inscripcionIngresos.tipo` | string | REQUERIDO | Valores: `"EXE"`, `"INS"`, `"NOINS"` |
| `cuentaComitente.persona.informacionFiscal.inscripcionIngresos.fecha` | string | REQUERIDO | Fecha alta ganancias (`YYYY-MM-DD`). Obligatorio si tipo=`"INS"`. Puede ser vacío. |
| `cuentaComitente.persona.informacionFiscal.condicionIva` | string | REQUERIDO | Valores: `"RI"`, `"RNI"`, `"EX"`, `"RM"`, `"CF"` |
| `cuentaComitente.persona.informacionFiscal.paisResidenciaFiscal` | string | REQUERIDO | Código ISO alfa-2 del país donde tributa. |
| `cuentaComitente.persona.informacionFiscal.fatca.esFatca` | boolean | REQUERIDO | Si aplica FATCA. |
| `cuentaComitente.persona.informacionFiscal.fatca.ssn` | string | REQUERIDO | SSN de EE.UU. Puede ser vacío si esFatca es falso. No puede ser null. |
| `cuentaComitente.persona.informacionFiscal.ocde.esOcde` | boolean | REQUERIDO | Si declara obligaciones OCDE. |
| `cuentaComitente.persona.informacionFiscal.ocde.paisResidenciaFiscalPrincipal` | string | REQUERIDO | Código ISO alfa-2. Admite vacío o null. |
| `cuentaComitente.persona.informacionFiscal.ocde.nitPrincipal` | string | REQUERIDO | NIT principal. Admite vacío o null. |
| `cuentaComitente.persona.informacionFiscal.ocde.paisResidenciaFiscalOpcional` | string | REQUERIDO | Código ISO alfa-2 secundario. Admite vacío o null. |
| `cuentaComitente.persona.informacionFiscal.ocde.nitOpcional` | string | REQUERIDO | NIT secundario. Admite vacío o null. |
| `cuentaComitente.persona.informacionFiscal.sujetosObligados.esSujetoObligado` | boolean | REQUERIDO | Si es Sujeto Obligado ante la UIF. |
| `cuentaComitente.persona.informacionFiscal.sujetosObligados.tipo` | string | REQUERIDO | Clasificación UIF. Admite vacío o null. |
| `cuentaComitente.persona.informacionFiscal.sujetosObligados.fechaCreacion` | string | REQUERIDO | Fecha inscripción UIF. Admite vacío o null. |
| `cuentaComitente.direccion.tipo` | string | REQUERIDO | Valores: `"LEGAL"`, `"HOME"`, `"WORK"` |
| `cuentaComitente.direccion.calle` | string | REQUERIDO | Nombre de la calle. Sin guiones ni diéresis. |
| `cuentaComitente.direccion.numero` | string | REQUERIDO | Numeración. Máx 5 chars alfanuméricos. |
| `cuentaComitente.direccion.piso` | string | REQUERIDO | Piso. Máx 5 chars. Admite vacío o null. |
| `cuentaComitente.direccion.departamento` | string | REQUERIDO | Depto. Máx 5 chars. Admite vacío o null. |
| `cuentaComitente.direccion.bloque` | string | REQUERIDO | Bloque. Máx 5 chars. Admite vacío o null. |
| `cuentaComitente.direccion.sector` | string | REQUERIDO | Sector. Máx 5 chars. Admite vacío o null. |
| `cuentaComitente.direccion.torre` | string | REQUERIDO | Torre. Máx 5 chars. Admite vacío o null. |
| `cuentaComitente.direccion.codigoPostal` | string | REQUERIDO | CP de 4 dígitos o CPA de 8 chars. |
| `cuentaComitente.direccion.pais` | string | REQUERIDO | Código ISO alfa-2. |
| `cuentaComitente.direccion.provincia` | string | REQUERIDO | Ej: `"AR-C"`. Admite vacío o null. |
| `cuentaComitente.direccion.localidad` | string | REQUERIDO | Ciudad/localidad. Sin guiones ni diéresis. |
| `cuentaComitente.contacto.codigoArea` | string | REQUERIDO | Código de área sin el prefijo 0. Ej: `"11"`, `"351"` |
| `cuentaComitente.contacto.correoElectronico` | string | REQUERIDO | Email válido. |
| `cuentaComitente.contacto.telefono` | string | REQUERIDO | Teléfono sin código de área ni prefijo 15. Máx 10 chars. |
| `cuentaComitente.documentos[].tipo` | string | REQUERIDO | Valor: `"FRONT_DNI"` |
| `cuentaComitente.documentos[].descripcion` | string | REQUERIDO | Descripción del documento. |
| `cuentaComitente.documentos[].nombreArchivo` | string | REQUERIDO | Nombre del archivo. |
| `cuentaComitente.documentos[].extension` | string | REQUERIDO | Extensión del archivo. Ej: `"jpg"`, `"base64"` |
| `cuentaComitente.documentos[].verificado` | boolean | REQUERIDO | Si el documento fue pre-verificado por la organización. |
| `cuentaComitente.documentos[].archivo.url` | string | OPCIONAL | URL pública para descarga de la imagen. |
| `cuentaComitente.documentos[].archivo.base64` | string | OPCIONAL | Imagen en Base64 cuando no hay URL disponible. |
| `cuentaComitente.verificacionIdentidad` | string | OPCIONAL | ID del proceso de validación biométrica. No puede ser vacío ni null si se envía. |
| `cuentaComitente.bancos.tipo` | string | REQUERIDO | Valor fijo: `"CVU"` |
| `cuentaComitente.bancos.identificacion` | string | REQUERIDO | CVU de 22 dígitos del usuario. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/CuentaYCVUConCuentaComitente' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "cuentaId": 279138,
  "cuentaRemuneradaActiva": true,
  "cuentaComitente": {
    "persona": {
      "personaFisica": true,
      "nombre": "Eros",
      "apellido": "Martinez",
      "nacionalidad": "AR",
      "paisResidencia": "AR",
      "tipoIdentificacion": "DNI",
      "identificacion": "12348812",
      "paisIdentificacion": "AR",
      "estadoCivil": "MARRIED",
      "fechaNacimiento": "1985-03-15",
      "lugarNacimiento": "AR",
      "genero": "M",
      "informacionFiscal": {
        "tipo": "CUIT",
        "numero": "20123488128",
        "actividadComercial": "12",
        "pep": {"esPep": false, "descripcion": ""},
        "inscripcionIngresos": {"tipo": "INS", "fecha": "2015-10-04"},
        "condicionIva": "RI",
        "paisResidenciaFiscal": "AR",
        "fatca": {"esFatca": false, "ssn": ""},
        "ocde": {"esOcde": false, "paisResidenciaFiscalPrincipal": "", "nitPrincipal": "", "paisResidenciaFiscalOpcional": "", "nitOpcional": ""},
        "sujetosObligados": {"esSujetoObligado": false, "tipo": "", "fechaCreacion": ""}
      }
    },
    "direccion": {
      "tipo": "HOME",
      "calle": "Juan B justo",
      "numero": "517",
      "piso": "1",
      "departamento": "A",
      "bloque": null,
      "sector": null,
      "torre": null,
      "codigoPostal": "5500",
      "pais": "AR",
      "provincia": "AR-M",
      "localidad": "Mendoza"
    },
    "contacto": {
      "codigoArea": "11",
      "correoElectronico": "eros.martinez@example.com",
      "telefono": "1130121234"
    },
    "documentos": [
      {
        "tipo": "FRONT_DNI",
        "descripcion": "DNI Frente",
        "nombreArchivo": "document_id_front",
        "extension": "base64",
        "verificado": true,
        "archivo": {"url": null, "base64": "{{base64_de_foto_del_frente_del_dni}}"}
      }
    ],
    "verificacionIdentidad": {"id": "123456789"},
    "bancos": {"tipo": "CVU", "identificacion": "0000532609100002749260"}
  }
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `cuenta` | object | Información de la cuenta. |
| `cuentaCVU` | object | Información del CVU. |
| `cuentaComitente.id` | string | Identificador de la cuenta comitente. |
| `cuentaComitente.procesador` | string | Nombre del broker. |
| `cuentaComitente.estado` | string | Estado de la cuenta comitente en el broker. |
| `cuentaComitente.motivoError` | string | Descripción del error (si aplica). |
| `cvuCreado` | boolean | Si la cuenta tiene un CVU creado. |
| `idOrganizacion` | int | Identificador de la organización. |
| `cuentaComitenteCreado` | boolean | Si la cuenta tiene una cuenta comitente asociada. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación de cuenta comitente exitosa |
| `206` | El broker indica un error al crear la comitente |
| `401` | Token de autenticación inválido |
