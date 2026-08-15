# Endpoint — Modificar cuenta

> Fuente: https://psp.bind.com.ar/developers/apis/modificar-cuenta
> Producto: Wallet — Cuentas

## Descripción

Modifica los datos de la cuenta de un cliente.

## URL / Método

| Campo | Valor |
|-------|-------|
| Método | `PUT` |
| URL (Staging) | `https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Cuenta/{id}` |
| Content-Type | `application/json` |

## Parámetros del Request

Mismos campos que Crear cuenta, más el parámetro de path:

| Parámetro | Tipo | Requerido | Descripción |
|-----------|------|-----------|-------------|
| `id` | int | REQUIRED | Identificador de la cuenta (path param). |
| `codigo` | string | OPTIONAL | Identificador externo de la entidad. |
| `cuitCuil` | string | REQUIRED | CUIT/CUIL del titular. |
| `nombre` | string | REQUIRED | Nombres del titular. |
| `apellido` | string | REQUIRED | Apellidos del titular. |
| `razonSocial` | string | REQUIRED | Razón Social del titular. |
| `email` | string | REQUIRED | Correo electrónico del titular. |
| `celular` | string | REQUIRED | Número de teléfono celular del titular. |
| `actividadAfip` | string | REQUIRED | Código de actividad económica ARCA (6 dígitos). |
| `habilitado` | boolean | OPTIONAL | Estado de habilitación. |
| `domicilio` | object | REQUIRED | Datos del domicilio (mismos campos que en Crear). |
| `esPep` | boolean | REQUIRED | Persona políticamente expuesta. |
| `esFatca` | boolean | REQUIRED | FATCA. |
| `esUif` | boolean | REQUIRED | Sujeto obligado UIF. |
| `nacionalidad` | string | REQUIRED | ISO dos letras. |
| `fechaNacimiento` | datetime | REQUIRED | Fecha de nacimiento. |
| `ocupacion` | string | OPTIONAL | Ocupación. |
| `estadoCivil` | string | OPTIONAL | Estado civil. |
| `dni` | string | REQUIRED | DNI del titular. |

## Bloque curl request

```bash
curl --location --request PUT 'https://gw-staging-qrbind.epays.services/walletentidad-cuenta/v1/api/v1.201/Cuenta/274926' \
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
"datosDomicilio": {"calle": "Maipu","numero": "1012","piso": "7","departamento": null,"localidadId": 247,"provinciaId": 1,"cp": "1006"},
"esPep": false,"esFacta": false,"esUif": false,
"nacionalidad": "AR","fechaNacimiento":"1989-02-16",
"ocupacion":"ESTUDIANTE","estadoCivil":"CASADO","dni":"37431567"
}'
```

## Response

Respuesta sin contenido.

## Códigos HTTP

| Código | Descripción |
|--------|-------------|
| `204` | Cuenta modificada con éxito |
| `400` | Algún dato de la solicitud tiene un formato inválido |
| `401` | Token de autenticación inválido |
