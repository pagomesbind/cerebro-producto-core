# Endpoint — Crear cuenta

> Fuente: https://psp.bind.com.ar/developers/apis/crear-cuenta
> Producto: Wallet — Cuentas

## Descripción

Crea una nueva cuenta para un cliente.

Este endpoint no será utilizado por la organización si la misma usa nuestro Onboarding para dar de altas las cuentas de sus usuarios.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `POST` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Cuenta` |
| Content-Type | `application/json` |

## Parámetros del Request

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `codigo` | string | OPTIONAL | Identificador externo de la entidad. |
| `cuitCuil` | string | REQUIRED | CUIT/CUIL del titular de la cuenta. |
| `nombre` | string | REQUIRED | Nombres del titular de la cuenta. |
| `apellido` | string | REQUIRED | Apellidos del titular de la cuenta. |
| `razonSocial` | string | REQUIRED | Razón Social del titular de la cuenta. |
| `email` | string | REQUIRED | Correo electrónico del titular de la cuenta. |
| `celular` | string | REQUIRED | Número de teléfono celular del titular de la cuenta. |
| `actividadAfip` | string | REQUIRED | Código de actividad económica en ARCA (6 dígitos). Sin actividad: "000007"=Jubilado, "000008"=Estudiante, "000009"=Ama de casa, "000010"=Ex Agente Adm. Publica, "000011"=Trabajo Relac. Dependencia, "000012"=Sin Actividad, "000013"=Agricultura Familiar |
| `habilitado` | boolean | OPTIONAL | Indica si la cuenta debe ser creada habilitada o deshabilitada. Por defecto, una cuenta se crea deshabilitada. |
| `domicilio.calle` | string | REQUIRED | Calle del domicilio. |
| `domicilio.numero` | string | REQUIRED | Número del domicilio. |
| `domicilio.piso` | string | OPTIONAL | Piso del domicilio. |
| `domicilio.departamento` | string | OPTIONAL | Departamento del domicilio. |
| `domicilio.localidadCodigo` | int | REQUIRED | Código de localidad. Valores: Consultar localidades. |
| `domicilio.provinciaCodigo` | int | REQUIRED | Código de provincia. Valores: Consultar provincias. |
| `domicilio.cp` | string | REQUIRED | Código postal. |
| `esPep` | boolean | REQUIRED | Indica si el titular es una persona políticamente expuesta. |
| `esFatca` | boolean | REQUIRED | Indica si el titular es FATCA. |
| `esUif` | boolean | REQUIRED | Indica si el titular es sujeto obligado ante la UIF. |
| `nacionalidad` | string | REQUIRED | Nacionalidad en formato ISO dos letras. Ej: "AR" |
| `fechaNacimiento` | datetime | REQUIRED | Fecha de nacimiento del titular. |
| `ocupacion` | string | OPTIONAL | Valores: "JUBILADO", "ESTUDIANTE", "TRABAJADOR EN RELACIÓN DE DEPENDENCIA", "AMA DE CASA", "DESOCUPADO", "TRABAJADOR INDEPENDIENTE" |
| `estadoCivil` | string | OPTIONAL | Valores: "SOLTERO", "CASADO", "VIUDO", "SEPARADO", "DIVORCIADO" |
| `dni` | string | REQUIRED | DNI del titular. Opcional si es persona jurídica. |

## Bloque curl request

```bash
curl --location 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Cuenta' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
"codigo": "codigo125",
"cuitCuil": "20374315679",
"nombre": "Juan",
"apellido": "Perez",
"razonSocial": "Juan Perez SA",
"email": "juanperez@gmail.com",
"celular": "1168599999",
"actividadAfip": "000012",
"habilitado": true,
"datosDomicilio": {
"calle": "Maipu",
"numero": "1012",
"piso": "7",
"departamento": null,
"localidadId": 247,
"provinciaId": 1,
"cp": "1006"
},
"esPep": false,
"esFacta": false,
"esUif": false,
"nacionalidad": "AR",
"fechaNacimiento":"1989-02-16",
"ocupacion":"ESTUDIANTE",
"estadoCivil":"CASADO",
"dni":"37431567"
}'
```

## Response

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | string | Identificador de la cuenta creada. Se utiliza para realizar acciones sobre la misma, por ejemplo: Crear CVU. |
| `habilitado` | boolean | Indica si la cuenta se creó habilitada o deshabilitada. |

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `201` | Creación de cuenta realizada |
| `409` | El código ya existe |
| `400` | Algún dato ingresado tiene un formato inválido |
| `401` | Token de autenticación inválido |
