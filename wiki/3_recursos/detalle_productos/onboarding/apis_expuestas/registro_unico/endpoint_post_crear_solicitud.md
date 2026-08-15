# POST — Crear Solicitud de Onboarding (Registro Único CVU)

> Fuente: https://psp.bind.com.ar/developers/apis/crea-una-solicitud-de-onboarding
> Producto: Onboarding — Registro único

## Descripción

Crea una solicitud de onboarding para validación de un usuario y posterior creación de cuenta y CVU.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/orquestador/api/v1/onboarding` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `externalrefid` | string | OPTIONAL | Identificador externo indicado por la Entidad. |
| `frente` | string | REQUIRED | Foto del frente del DNI en Base64. Máx 1 MB. |
| `dorso` | string | REQUIRED | Foto del dorso del DNI en Base64. Máx 1 MB. |
| `documento` | string | OPTIONAL | Número de DNI. Para usar si no puede extraerse del PDF417 (error `PDF417_NO_ENCONTRADO`). |
| `documentoTramite` | string | OPTIONAL | Número de trámite del documento. Para usar si no puede extraerse del PDF417. |
| `genero` | string | OPTIONAL | Género: `"M"` / `"F"` / `"X"`. Para usar si no puede extraerse del PDF417. |
| `selfie` | string | REQUIRED | Foto selfie del usuario en Base64. Máx 1 MB. |
| `email` | string | REQUIRED | Correo electrónico del usuario. |
| `telefono` | string | REQUIRED | Número telefónico del usuario. |
| `maritalState` | string | REQUIRED | Estado civil: `"SOLTERO"` / `"CASADO"` / `"VIUDO"` / `"SEPARADO"` / `"DIVORCIADO"` |
| `occupation` | string | REQUIRED | Ocupación: `"JUBILADO"` / `"ESTUDIANTE"` / `"TRABAJADOR EN RELACIÓN DE DEPENDENCIA"` / `"AMA DE CASA"` / `"DESOCUPADO"` |
| `isOcde` | boolean | REQUIRED | Si el usuario declaró ser OCDE. |
| `ocdeTimeStamp` | string | REQUIRED | Fecha y hora de la declaración jurada OCDE. |
| `ocdeCountryTaxResidencePrincipal` | string | OPTIONAL | País principal donde tributa (ISO 2 letras). Obligatorio si `isOcde=true`. |
| `ocdeNitPrincipal` | string | OPTIONAL | NIT principal. Obligatorio si `isOcde=true`. |
| `ocdeNitOpcional` | string | OPTIONAL | NIT opcional. Obligatorio si `isOcde=true`. |
| `isFatca` | boolean | REQUIRED | Si el usuario declaró ser FATCA. |
| `fatcaTimeStamp` | boolean | REQUIRED | Fecha y hora de la declaración jurada FATCA. |
| `factaSsn` | string | OPTIONAL | Número SSN de FATCA. Obligatorio si `isFatca=true`. |
| `isPEP` | boolean | REQUIRED | Si el usuario declaró ser PEP. |
| `pepTimeStamp` | string | REQUIRED | Fecha y hora de la declaración jurada PEP. |
| `pepDescription` | boolean | OPTIONAL | Descripción del puesto político. Obligatorio si `isPEP=true`. |
| `isUIF` | boolean | REQUIRED | Si el usuario declaró ser UIF. |
| `uifTimeStamp` | string | REQUIRED | Fecha y hora de la declaración jurada UIF. |
| `isTyc` | boolean | REQUIRED | Si el usuario aceptó los TyC. |
| `tycTimeStamp` | string | REQUIRED | Fecha y hora en que el usuario aceptó los TyC. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/orquestador/api/v1/onboarding' \
--header 'Cache-Control: no-cache' \
--header 'Content-Type: application/json' \
--header 'Authorization: {{access_token}}' \
--data-raw '{
  "externalrefid": "789654",
  "frente": "fotoEnBase64DelFrenteDelDni",
  "dorso": "fotoEnBase64DelDorsoDelDni",
  "documento": null,
  "documentoTramite": null,
  "genero": null,
  "selfie": "fotoEnBase64SelfieDelUsuario",
  "email": "usuario@ejemplo.com",
  "telefono": "1169991243",
  "maritalState": "SOLTERO",
  "occupation": "TRABAJADOR EN RELACIÓN DE DEPENDENCIA",
  "isOcde": false,
  "ocdeTimeStamp": "2024-10-23 10:10:48",
  "ocdeCountryTaxResidencePrincipal": null,
  "ocdeNitPrincipal": null,
  "ocdeCountryTaxResidenceOptional": null,
  "ocdeNitOpcional": null,
  "isFatca": false,
  "fatcaTimeStamp": "2024-10-23 10:10:48",
  "factaSsn": null,
  "isPep": false,
  "pepTimeStamp": "2024-10-23 10:10:48",
  "pepDescription": null,
  "isUIF": false,
  "uifTimeStamp": "2024-10-23 10:10:48",
  "isTyc": true,
  "tycTimeStamp": "2024-10-23 10:10:48"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | Identificador de la solicitud de onboarding creada. |
| `externalrefid` | string | Identificador externo indicado por la Entidad. |
| `estado` | int | Estado del onboarding: `1`=Pendiente, `2`=Aprobada, `3`=Rechazada, `4`=Validación Manual, `5`=Pendiente credenciales, `6`=Error alta, `7`=Aprobado a Revisar, `8`=Aprobado sin notificar, `9`=Vencida, `10`=Menor pendiente, `11`=Menor habilitado |
| `cuenta` | object | Información de la cuenta principal creada en Wallet. |
| `cuentaCvu` | object | Información del CVU creado asociado a la cuenta. |
| `cuentaInvestment` | object | Información de la cuenta comitente creada asociada a la cuenta. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Onboarding aprobado. Cuentas creadas satisfactoriamente. |
| `422` | Onboarding rechazado: no se puede extraer información del PDF417 del DNI. Puede reintentarse enviando los datos manualmente. |
| `422` | Onboarding rechazado: ya existe una solicitud aprobada de la persona. |
| `422` | Onboarding rechazado: Renaper no reconoce el documento. |
| `422` | Onboarding rechazado: el DNI corresponde a una persona fallecida en Renaper. |
| `422` | Onboarding rechazado: el ejemplar del DNI no está vigente para Renaper. |
| `422` | Onboarding rechazado: el usuario tiene una edad menor a la permitida. |
| `401` | Token de autenticación inválido. |
